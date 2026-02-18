import os
import re

os.chdir('/home/node/.openclaw/workspace/site')

old_button = '''<button id="menu-btn" class="md:hidden p-2 text-charcoal">
  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
  </svg>
</button>'''

new_button = '''<input type="checkbox" id="nav-toggle" class="sr-only peer">
<label for="nav-toggle" class="md:hidden cursor-pointer p-3 rounded-lg hover:bg-cream/50 shadow-sm flex items-center justify-center w-12 h-12 text-charcoal">
  <svg class="w-7 h-7 transition-transform duration-200" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24">
    <path class="hamburger" stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h16"/>
    <path class="close hidden peer-checked:block peer-checked:rotate-180" stroke-linecap="round" stroke-linejoin="round" d="M6 18L18 6M6 6l12 12"/>
  </svg>
</label>'''

old_mobile_class = r'class=\\"hidden md:hidden bg-white border-t px-4 py-4 space-y-3\\"'

new_mobile_class = r'class=\\"md:hidden bg-white border-t px-4 py-4 space-y-3 hidden peer-checked:flex flex-col w-full z-40 absolute top-full left-0 right-0 shadow-lg order-last\\"'

pages = ['brochure.html', 'contact.html', 'gallery.html', 'index.html', 'pricing.html', 'pvc-doors.html', 'quote.html', 'vinyl-doors.html']

for page in pages:
  if os.path.exists(page):
    with open(page, 'r') as f:
      content = f.read()
    content = content.replace(old_button, new_button)
    content = re.sub(old_mobile_class, new_mobile_class, content)
    with open(page, 'w') as f:
      f.write(content)
    print(f'Updated {page}')

print('CSS menu complete')