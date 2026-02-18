import os
import re

os.chdir('/home/node/.openclaw/workspace/site')

old_pattern = r'&lt;script&gt;\\s*//\\s*Mobile menu toggle[\\s\\S]*?&lt;/script&gt;'
new_script = '''&lt;script&gt;
  document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu toggle + enhancements
    const btn = document.getElementById('menu-btn');
    const nav = document.getElementById('mobile-nav');
    const hamburger = btn ? btn.querySelector('svg path') : null;
    if (btn && nav) {
      btn.addEventListener('click', function() {
        const isOpen = !nav.classList.contains('hidden');
        nav.classList.toggle('hidden');
        if (hamburger) {
          hamburger.setAttribute('d', isOpen ? 'M6 18L18 6M6 6l12 12' : 'M4 6h16M4 12h16M4 18h16');
        }
      });

      // Close on link click
      nav.querySelectorAll('a').forEach(link =&gt; {
        link.addEventListener('click', () =&gt; nav.classList.add('hidden'));
      });

      // Close on outside click
      document.addEventListener('click', function(e) {
        if (!btn.contains(e.target) &amp;&amp; !nav.contains(e.target)) {
          nav.classList.add('hidden');
        }
      });
    }

    // Highlight active page
    const currentPage = window.location.pathname.split('/').pop().replace('.html', '') || 'index';
    document.querySelectorAll('.nav-link').forEach(link =&gt; {
      if (link.dataset.page === currentPage || 
          (currentPage === 'vinyl-doors' || currentPage === 'pvc-doors') &amp;&amp; link.dataset.page === 'doors') {
        link.classList.remove('text-warmgray');
        link.classList.add('text-accent', 'font-semibold');
      }
    });
  });
&lt;/script&gt;'''

pages = ['brochure.html', 'contact.html', 'gallery.html', 'index.html', 'pricing.html', 'pvc-doors.html', 'quote.html', 'vinyl-doors.html']
backup_pages = ['index-old-backup.html']  # Skip

for page in pages:
  if os.path.exists(page):
    with open(page, 'r') as f:
      content = f.read()
    new_content = re.sub(old_pattern, new_script, content, flags=re.DOTALL | re.MULTILINE)
    with open(page, 'w') as f:
      f.write(new_content)
    print(f'Updated {page}')

print('Batch fix complete')