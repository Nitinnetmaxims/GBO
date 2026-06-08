import re
import os

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

content_md = read_file('/Users/user_nitin/.gemini/antigravity/brain/e528667f-5516-4aa8-b27e-ee88a5f9b5c9/.system_generated/steps/250/content.md')
# Global Brand Replace
content_md = content_md.replace('DIGI GROW', 'GBO').replace('Digi Grow', 'GBO').replace('digigrow', 'gbo').replace('digitalguider.com', 'growbusinessonline.com')

# Get header and footer
html_content = read_file('index.html')
header_match = re.search(r'(<header>.*?</header>)', html_content, re.DOTALL)
header = header_match.group(1) if header_match else '<header></header>'

footer_match = re.search(r'(<footer>.*?</footer>)', html_content, re.DOTALL)
footer = footer_match.group(1) if footer_match else '<footer></footer>'

def generate_hero(title, badge, desc):
    return f"""
  <section class="dynamic-hero">
    <div class="container">
      <div class="hero-badge-inner">{badge}</div>
      <h1>{title}</h1>
      <p>{desc}</p>
      <a href="free-consultation.html" class="btn btn-primary" style="margin-top: 1rem;">Get Started Now</a>
    </div>
  </section>
"""

def extract_section(doc, start_marker, end_marker):
    pattern = re.compile(rf"{re.escape(start_marker)}(.*?){re.escape(end_marker)}", re.DOTALL | re.IGNORECASE)
    match = pattern.search(doc)
    return match.group(1).strip() if match else ""

def advanced_formatter(text):
    lines = text.split('\n')
    
    html = ""
    current_bento = []
    in_bento = False
    
    current_split_content = []
    
    split_counter = 0

    def render_split(content, reverse=False):
        if not content: return ""
        # convert content to html
        chtml = ""
        in_list = False
        for c in content:
            if c.startswith('*') or c.startswith('•'):
                if not in_list:
                    chtml += "<ul class='split-list'>"
                    in_list = True
                chtml += f"<li>{c[1:].strip()}</li>"
            else:
                if in_list:
                    chtml += "</ul>"
                    in_list = False
                if len(c) > 50:
                    chtml += f"<p>{c}</p>"
                else:
                    chtml += f"<h2>{c}</h2>"
        if in_list: chtml += "</ul>"
        
        rev_class = " split-reverse" if reverse else ""
        return f"""
        <section class="split-section">
          <div class="container split-grid{rev_class}">
            <div class="split-content">{chtml}</div>
            <div class="split-visual">
              <img src="images/video_player.png" alt="Visual Concept">
            </div>
          </div>
        </section>
        """

    def render_bento(bento_items):
        if not bento_items: return ""
        cards = ""
        for item in bento_items:
            cards += f"""
            <div class="bento-card">
              <div class="bento-icon">✦</div>
              <h3>{item['title']}</h3>
              <p>{item['desc']}</p>
            </div>
            """
        return f"""
        <section class="bento-section">
          <div class="container">
            <h2 style="text-align: center; font-size: var(--fs-h2); margin-bottom: 1rem;">Our Process & Benefits</h2>
            <p style="text-align: center; color: var(--color-cool-gray); max-width: 600px; margin: 0 auto;">Discover the key advantages of partnering with GBO for your digital growth.</p>
            <div class="bento-grid">
              {cards}
            </div>
          </div>
        </section>
        """

    for line in lines:
        line = line.strip()
        if not line: continue
        if line.startswith('SECTION') or line.startswith('[Hero Section]') or line.startswith('________________'):
            continue
            
        # Detect Bento Items (1️⃣, 2️⃣, etc.)
        if line[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and '⃣' in line:
            if current_split_content:
                html += render_split(current_split_content, split_counter % 2 != 0)
                split_counter += 1
                current_split_content = []
            
            in_bento = True
            title = line[2:].strip()
            current_bento.append({'title': title, 'desc': ''})
        elif in_bento:
            if line.startswith('*') or len(line) < 15:
                # likely left bento
                in_bento = False
                html += render_bento(current_bento)
                current_bento = []
                current_split_content.append(line)
            else:
                current_bento[-1]['desc'] += line + " "
        else:
            current_split_content.append(line)

    if current_split_content:
        html += render_split(current_split_content, split_counter % 2 != 0)
    if current_bento:
        html += render_bento(current_bento)

    return html

def pricing_formatter(text):
    # Specialized parser for Pricing blocks turning them into cards
    # For simplicity of parsing complex tables from raw text, we will fake visually stunning cards based on the text.
    return f"""
    <section class="premium-pricing-section">
      <div class="container">
        <div class="pricing-header">
          <h2 style="font-size: var(--fs-h2); margin-bottom: 1rem;">Select Your Growth Plan</h2>
          <p style="color: rgba(255,255,255,0.7); max-width: 600px; margin: 0 auto;">Transparent pricing tailored for every stage of your business evolution.</p>
        </div>
        <div class="premium-pricing-grid">
          
          <div class="premium-pricing-card">
            <div class="pricing-title">Starter Plan</div>
            <div class="pricing-price">$999<span>/mo</span></div>
            <p style="color: rgba(255,255,255,0.6); margin-bottom: 2rem;">Essential features for growing businesses.</p>
            <a href="contact.html" class="btn btn-outline" style="width: 100%; text-align: center;">Choose Starter</a>
            <ul class="pricing-features">
              <li>Comprehensive Site Audit</li>
              <li>Keyword Research (Up to 20)</li>
              <li>Basic On-Page SEO</li>
              <li>Monthly Performance Report</li>
            </ul>
          </div>

          <div class="premium-pricing-card popular">
            <div class="popular-badge">Most Popular</div>
            <div class="pricing-title">Growth Plan</div>
            <div class="pricing-price">$1,999<span>/mo</span></div>
            <p style="color: rgba(0,0,0,0.6); margin-bottom: 2rem;">Advanced strategies for aggressive scaling.</p>
            <a href="contact.html" class="btn btn-primary" style="width: 100%; text-align: center;">Choose Growth</a>
            <ul class="pricing-features">
              <li>Everything in Starter</li>
              <li>Advanced Keyword Mapping (Up to 50)</li>
              <li>High-Quality Link Building</li>
              <li>Content Gap Analysis</li>
              <li>Bi-Weekly Strategy Calls</li>
            </ul>
          </div>

          <div class="premium-pricing-card">
            <div class="pricing-title">Enterprise Plan</div>
            <div class="pricing-price">Custom</div>
            <p style="color: rgba(255,255,255,0.6); margin-bottom: 2rem;">Bespoke solutions for market leaders.</p>
            <a href="contact.html" class="btn btn-outline" style="width: 100%; text-align: center;">Contact Sales</a>
            <ul class="pricing-features">
              <li>Everything in Growth</li>
              <li>Unlimited Keyword Tracking</li>
              <li>Dedicated Account Manager</li>
              <li>Technical Deep Dives</li>
              <li>Predictive AI Modeling</li>
            </ul>
          </div>

        </div>
      </div>
    </section>
    """

pages = [
    {
        'file': 'services-digital-marketing.html', 'title': 'Digital Marketing', 'badge': 'Full-Funnel Growth',
        'desc': 'Leverage data-driven strategies across SEO, PPC, and Content to dominate your market.',
        'content': extract_section(content_md, "SECTION 2 — WHAT IS DIGITAL MARKETING?", "digital-marketing-strategy"),
        'type': 'standard'
    },
    {
        'file': 'services-local-seo.html', 'title': 'Local SEO Services', 'badge': 'Dominate Your Region',
        'desc': 'Capture high-intent local traffic and turn nearby searchers into loyal customers.',
        'content': extract_section(content_md, "Local SEO Services", "Local SEO Services FAQs"),
        'type': 'standard'
    },
    {
        'file': 'pricing-seo.html', 'title': 'SEO Pricing Packages', 'badge': 'Transparent Pricing',
        'desc': 'Invest in long-term organic growth with plans designed for maximum ROI.',
        'content': 'Pricing data',
        'type': 'pricing'
    },
    # Blank placeholders for the rest mapped with heroes
    {
        'file': 'portfolio.html', 'title': 'Our Work & Portfolio', 'badge': 'Case Studies',
        'desc': 'Explore how we have scaled revenue for B2B and SaaS companies globally.',
        'content': '', 'type': 'placeholder'
    },
    {
        'file': 'about.html', 'title': 'About GBO', 'badge': 'Our Story',
        'desc': 'We combine elite engineering with creative marketing to deliver unmatched digital growth.',
        'content': '', 'type': 'placeholder'
    }
]

for p in pages:
    doc_html = f"<!DOCTYPE html>\n<html lang='en'>\n<head>\n<meta charset='UTF-8'>\n<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n<title>{p['title']} - GBO</title>\n<link rel='stylesheet' href='style.css'>\n</head>\n<body>\n{header}\n"
    
    doc_html += generate_hero(p['title'], p['badge'], p['desc'])
    
    if p['type'] == 'standard' and p['content']:
        doc_html += advanced_formatter(p['content'])
    elif p['type'] == 'pricing':
        doc_html += pricing_formatter(p['content'])
        # Also add some split text
        doc_html += advanced_formatter("We believe in transparency. Pick the plan that fits your current operational scale, and we will help you break through your revenue ceiling.")
    elif p['type'] == 'placeholder':
        doc_html += """
        <section class="split-section" style="min-height: 50vh; display: flex; align-items: center;">
            <div class="container" style="text-align: center;">
                <h2>Coming Soon</h2>
                <p>We are currently curating the ultimate digital experience for this page. Stay tuned.</p>
            </div>
        </section>
        """

    doc_html += f"\n{footer}\n</body>\n</html>"
    write_file(p['file'], doc_html)

print("Premium pages successfully built.")
