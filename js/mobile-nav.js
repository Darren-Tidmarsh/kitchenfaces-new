(function () {
  function initMobileNav() {
    var btn = document.getElementById('menu-btn') || document.querySelector('.hamburger');
    var nav = document.getElementById('mobile-nav') || document.querySelector('.mobile-nav');
    if (!btn || !nav) return;

    if (btn.getAttribute('data-mobile-nav-bound') === '1') return;
    btn.setAttribute('data-mobile-nav-bound', '1');
    btn.setAttribute('aria-expanded', 'false');

    function isOpen() {
      return !nav.classList.contains('hidden') || nav.classList.contains('open');
    }

    function setOpen(open) {
      nav.classList.toggle('hidden', !open);
      nav.classList.toggle('open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    }

    // Capture phase: prevent duplicate inline handlers from toggling twice.
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopImmediatePropagation();
      setOpen(!isOpen());
    }, true);

    nav.querySelectorAll('a').forEach(function (link) {
      link.addEventListener('click', function () { setOpen(false); });
    });

    document.addEventListener('click', function (e) {
      if (!btn.contains(e.target) && !nav.contains(e.target)) {
        setOpen(false);
      }
    });

    // Active page highlight
    var currentPage = (window.location.pathname.split('/').pop() || 'index.html').replace('.html', '') || 'index';
    document.querySelectorAll('.nav-link').forEach(function (link) {
      var page = link.getAttribute('data-page');
      if (!page) return;
      if (page === currentPage || ((currentPage === 'vinyl-doors' || currentPage === 'pvc-doors') && page === 'doors')) {
        link.classList.remove('text-warmgray');
        link.classList.add('text-accent', 'font-semibold');
      }
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initMobileNav);
  } else {
    initMobileNav();
  }
})();
