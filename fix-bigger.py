import os
import re

os.chdir('/home/node/.openclaw/workspace/site')

# Update button
old_button = r'&lt;button id=\\\"menu-btn\\\" class=\\\"md:hidden p-2 text-charcoal\\\" onclick'
new_button = r'&lt;button id=\\\"menu-btn\\\" class=\\\"md:hidden p-3 rounded-lg text-charcoal hover:bg-cream/50 w-12 h-12 flex items-center justify-center shadow-sm onclick'

# Update svg
old_svg = r'&lt;svg class=\\\"w-6 h-6\\\" fill=\\\"none\\\" stroke=\\\"currentColor\\\" viewBox=\\\"0 0 24 24\\\"&gt;'
new_svg = r'&lt;svg class=\\\"w-7 h-7\\\" fill=\\\"none\\\" stroke=\\\"currentColor\\\" stroke-width=\\\"3\\\" viewBox=\\\"0 0 24 24\\\"&gt;'

pages = ['brochure.html', 'contact.html', 'gallery.html', 'index.html', 'pricing.html', 'pvc-doors.html', 'quote.html', 'vinyl-doors.html']

for page in pages:
  if os.path.exists(page):
    with open(page, 'r') as f:
      content = f.read()
    content = content.replace(old_button, new_button)
    content = content.replace(old_svg, new_svg)
    with open(page, 'w') as f:
      f.write(content)
    print(f'Updated {page}')

print('Bigger button complete')