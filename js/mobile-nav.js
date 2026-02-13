(function(){
  document.addEventListener('DOMContentLoaded', function(){
    var btn = document.querySelector('.hamburger');
    var nav = document.querySelector('.mobile-nav');
    if(!btn || !nav) return;
    function closeNav(){ nav.classList.remove('open'); btn.setAttribute('aria-expanded','false'); }
    btn.addEventListener('click', function(){
      var isOpen = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', String(isOpen));
    });
    // close when clicking outside
    document.addEventListener('click', function(e){
      if(!nav.contains(e.target) && e.target !== btn){ closeNav(); }
    });
  });
})();