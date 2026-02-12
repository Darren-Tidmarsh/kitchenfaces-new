// Component loader - loads header and footer from shared files
document.addEventListener('DOMContentLoaded', function() {
  // Load header
  const headerEl = document.getElementById('site-header');
  if (headerEl) {
    fetch('components/header.html')
      .then(r => r.text())
      .then(html => {
        headerEl.innerHTML = html;
        // Re-run any inline scripts
        headerEl.querySelectorAll('script').forEach(script => {
          const newScript = document.createElement('script');
          newScript.textContent = script.textContent;
          document.body.appendChild(newScript);
        });
      });
  }

  // Load footer
  const footerEl = document.getElementById('site-footer');
  if (footerEl) {
    fetch('components/footer.html')
      .then(r => r.text())
      .then(html => {
        footerEl.innerHTML = html;
      });
  }
});
