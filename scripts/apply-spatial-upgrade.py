#!/usr/bin/env python3
"""
Apply the spatial UI upgrade to all HTML pages.

For each page:
  1. Insert <div class="scroll-progress" aria-hidden="true"></div> right after <body>
  2. Insert <div class="hero-orb" aria-hidden="true"></div> in the .hero (where present)
  3. Add --i custom property to practice-area cards
  4. Add data-state="active" to first .timeline-step, rest "pending"
  5. Add icon-bg class to the brand logo icon
"""
import re, sys, os

PAGES = ['index.html', 'about.html', 'contact.html', 'torts.html', 'mva.html',
         'ssdi.html', 'mortgage.html', 'compliance.html', 'privacy.html']

def add_scroll_progress(html):
    if 'scroll-progress' in html:
        return html
    # Insert right after <body...>
    return re.sub(
        r'(<body[^>]*>)',
        r'\1\n  <div class="scroll-progress" aria-hidden="true"></div>',
        html, count=1)

def add_hero_orb(html):
    if 'hero-orb' in html:
        return html
    # Insert inside .hero, after .hero-media
    return re.sub(
        r'(<div class="hero-media"[^>]*>.*?</div>)',
        r'\1\n      <div class="hero-orb" aria-hidden="true"></div>',
        html, count=1, flags=re.S)

def stagger_practice_cards(html):
    """Add --i custom property to each card in the practice-area grid."""
    if 'style="--i:' in html:
        return html
    # Find each <article class="card reveal"> in the .grid.grid--2 block and add --i
    counter = [0]
    def repl(m):
        counter[0] += 1
        return m.group(0).replace(
            '<article class="card reveal"',
            f'<article class="card reveal" style="--i: {counter[0]}"', 1)
    return re.sub(r'<article class="card reveal">', repl, html)

def stagger_timeline_steps(html):
    """Add data-state to timeline <li> elements inside <ol class="timeline">."""
    if 'data-state="active"' in html:
        return html
    # Find the timeline <ol> block and add data-state to each <li>
    def repl(m):
        block = m.group(0)
        lis = re.findall(r'<li([^>]*)>', block)
        new_block = block
        for i, attrs in enumerate(lis):
            if 'data-state' in attrs:
                continue
            state = 'active' if i == 0 else 'pending'
            new_attrs = attrs + f' data-state="{state}"'
            new_block = new_block.replace(f'<li{attrs}>', f'<li{new_attrs}>', 1)
        return new_block
    return re.sub(r'<ol class="timeline"[^>]*>.*?</ol>', repl, html, count=1, flags=re.S)

def add_favicon_to_header_icon(html):
    """Wrap the brand SVG icon in a span with icon-bg class."""
    if 'icon-bg' in html:
        return html
    return re.sub(
        r'(<a[^>]*class="brand"[^>]*>)\s*(<span[^>]*brand-mark[^>]*>)?\s*(<svg)',
        r'\1\n        <span class="icon-bg">\3',
        html, count=1)

def upgrade_page(path):
    if not os.path.exists(path):
        return False
    with open(path) as f:
        html = f.read()
    original = html
    html = add_scroll_progress(html)
    html = add_hero_orb(html)
    html = stagger_practice_cards(html)
    html = stagger_timeline_steps(html)
    if html != original:
        with open(path, 'w') as f:
            f.write(html)
        return True
    return False

if __name__ == '__main__':
    for p in PAGES:
        if upgrade_page(p):
            print(f"  ✓ {p}")
        else:
            print(f"  - {p} (no changes)")
