import re

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
  <!-- Native Hero Component -->
  <section class="hero" id="hero-section" style="padding-bottom: 4rem;">
    <div class="container" style="display: flex; justify-content: center; text-align: center;">
      <div class="hero-left" style="max-width: 800px; padding-right: 0;">
        <span class="hero-badge">{badge}</span>
        <h1 style="margin-bottom: 1.5rem;">{title}</h1>
        <p class="hero-desc">{desc}</p>
        <div class="hero-form-wrapper" style="justify-content: center; display: flex;">
          <a href="free-consultation.html" class="btn btn-primary">Get Started Now</a>
        </div>
      </div>
    </div>
  </section>
"""

def extract_section(doc, start_marker, end_marker):
    pattern = re.compile(rf"{re.escape(start_marker)}(.*?){re.escape(end_marker)}", re.DOTALL | re.IGNORECASE)
    match = pattern.search(doc)
    return match.group(1).strip() if match else ""

def native_formatter(text):
    lines = text.split('\n')
    
    html = ""
    current_bento = []
    in_bento = False
    
    current_split_content = []
    
    def render_split(content):
        if not content: return ""
        chtml = ""
        in_list = False
        for c in content:
            if c.startswith('*') or c.startswith('•'):
                if not in_list:
                    chtml += "<ul style='color: var(--color-cool-gray); margin-bottom: 1.5rem; padding-left: 1.5rem;'>"
                    in_list = True
                chtml += f"<li style='margin-bottom: 0.5rem;'>{c[1:].strip()}</li>"
            else:
                if in_list:
                    chtml += "</ul>"
                    in_list = False
                if len(c) > 50:
                    chtml += f"<p style='color: var(--color-cool-gray); line-height: 1.8; margin-bottom: 1rem;'>{c}</p>"
                else:
                    chtml += f"<h3 style='margin-bottom: 1rem; margin-top: 1.5rem;'>{c}</h3>"
        if in_list: chtml += "</ul>"
        
        return f"""
        <section class="marketing-revenue" style="padding: 4rem 0; border-top: 1px solid rgba(0,0,0,0.05);">
          <div class="container">
            <div class="marketing-content-wrapper" style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">
              <div class="marketing-acc-content" style="display: block; opacity: 1; height: auto;">
                {chtml}
              </div>
              <div class="marketing-image-panel">
                <img src="images/video_player.png" alt="Concept Visual" style="width: 100%; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
              </div>
            </div>
          </div>
        </section>
        """

    def render_bento(bento_items):
        if not bento_items: return ""
        cards = ""
        for item in bento_items:
            cards += f"""
            <div class="testimonial-card" style="display: flex; flex-direction: column; justify-content: flex-start; text-align: left;">
              <div class="stars" style="color: var(--color-fire-engine-red); margin-bottom: 1rem;">✦✦✦</div>
              <h3 style="margin-bottom: 0.5rem;">{item['title']}</h3>
              <p class="testimonial-text" style="font-style: normal;">"{item['desc']}"</p>
            </div>
            """
        return f"""
        <section class="testimonials" style="padding: 4rem 0; background-color: var(--color-warm-white);">
          <div class="container">
            <h2 style="text-align: center; margin-bottom: 3rem;">Core <span>Features</span></h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
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
            
        if line[0] in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] and '⃣' in line:
            if current_split_content:
                html += render_split(current_split_content)
                current_split_content = []
            
            in_bento = True
            title = line[2:].strip()
            current_bento.append({'title': title, 'desc': ''})
        elif in_bento:
            if line.startswith('*') or len(line) < 15:
                in_bento = False
                html += render_bento(current_bento)
                current_bento = []
                current_split_content.append(line)
            else:
                current_bento[-1]['desc'] += line + " "
        else:
            current_split_content.append(line)

    if current_split_content:
        html += render_split(current_split_content)
    if current_bento:
        html += render_bento(current_bento)

    return html

def pricing_formatter(title):
    return f"""
    <section class="pricing" style="padding: 6rem 0;">
      <div class="container">
        <div class="text-center" style="margin-bottom: 3rem;">
          <span class="process-label" style="color: var(--color-fire-engine-red); font-weight: 700; letter-spacing: 2px;">PRICING</span>
          <h2>Select Your <span class="highlight-red">{title} Plan</span></h2>
          <p class="pricing-sub">Transparent pricing tailored for every stage of your business evolution.</p>
        </div>
        <div class="new-pricing-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
          
          <div class="new-pricing-card">
            <div class="new-pricing-header">
              <h3>Starter</h3>
              <p>Ideal For Individual</p>
            </div>
            <div class="new-pricing-price">
              <span class="new-currency">$</span><span class="new-amount">999</span><span class="new-interval">/Monthly</span>
            </div>
            <button class="new-pricing-btn">Select Plan</button>
            <div class="new-pricing-features">
              <ul>
                <li><i>&#10003;</i> Comprehensive Audit</li>
                <li><i>&#10003;</i> Basic Optimization</li>
                <li><i>&#10003;</i> Monthly Report</li>
              </ul>
            </div>
          </div>

          <div class="new-pricing-card" style="border: 2px solid var(--color-fire-engine-red); transform: scale(1.05);">
            <div class="new-pricing-header">
              <h3>Growth</h3>
              <p>Most Popular</p>
            </div>
            <div class="new-pricing-price">
              <span class="new-currency">$</span><span class="new-amount">1999</span><span class="new-interval">/Monthly</span>
            </div>
            <button class="new-pricing-btn" style="background-color: var(--color-fire-engine-red); color: white;">Select Plan</button>
            <div class="new-pricing-features">
              <ul>
                <li><i>&#10003;</i> Everything in Starter</li>
                <li><i>&#10003;</i> Advanced Keyword Mapping</li>
                <li><i>&#10003;</i> High-Quality Link Building</li>
                <li><i>&#10003;</i> Bi-Weekly Strategy Calls</li>
              </ul>
            </div>
          </div>

          <div class="new-pricing-card">
            <div class="new-pricing-header">
              <h3>Enterprise</h3>
              <p>Custom Solutions</p>
            </div>
            <div class="new-pricing-price">
              <span class="new-amount">Custom</span>
            </div>
            <button class="new-pricing-btn">Contact Sales</button>
            <div class="new-pricing-features">
              <ul>
                <li><i>&#10003;</i> Everything in Growth</li>
                <li><i>&#10003;</i> Unlimited Keyword Tracking</li>
                <li><i>&#10003;</i> Dedicated Account Manager</li>
                <li><i>&#10003;</i> Predictive AI Modeling</li>
              </ul>
            </div>
          </div>

        </div>
      </div>
    </section>
    """

def placeholder_formatter():
    return """
    <section class="marketing-revenue" style="min-height: 50vh; display: flex; align-items: center; justify-content: center;">
        <div class="container" style="text-align: center;">
            <h2>Coming <span>Soon</span></h2>
            <p style="color: var(--color-cool-gray); margin-top: 1rem;">We are currently curating the ultimate digital experience for this page. Stay tuned.</p>
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
        'file': 'services-social-media.html', 'title': 'Social Media Marketing', 'badge': 'Brand Engagement',
        'desc': 'Build a loyal community and drive conversions across all major social platforms.',
        'type': 'placeholder'
    },
    {
        'file': 'services-seo.html', 'title': 'SEO Services', 'badge': 'Organic Dominance',
        'desc': 'Outrank your competitors with AI-driven, highly technical search engine optimization.',
        'type': 'placeholder'
    },
    {
        'file': 'services-video-seo.html', 'title': 'Video SEO', 'badge': 'YouTube & Beyond',
        'desc': 'Maximize views, watch time, and subscriber growth with strategic video optimization.',
        'type': 'placeholder'
    },
    {
        'file': 'services-digital-advertising.html', 'title': 'Digital Advertising', 'badge': 'Paid Growth',
        'desc': 'Scale revenue instantly with high-converting, data-backed PPC and display campaigns.',
        'type': 'placeholder'
    },
    {
        'file': 'pricing-seo.html', 'title': 'SEO Packages', 'badge': 'Pricing',
        'desc': 'Invest in long-term organic growth with plans designed for maximum ROI.',
        'content': 'Pricing data',
        'type': 'pricing'
    },
    {
        'file': 'pricing-smo-setup.html', 'title': 'SMO Structural Set-Up', 'badge': 'Pricing',
        'desc': 'Lay the foundation for your social media empire.',
        'type': 'pricing'
    },
    {
        'file': 'pricing-smo-maintenance.html', 'title': 'SMO Maintenance Package', 'badge': 'Pricing',
        'desc': 'Ongoing optimization to keep your social channels growing.',
        'type': 'pricing'
    },
    {
        'file': 'pricing-ecommerce-ppc.html', 'title': 'E-Commerce PPC Plans', 'badge': 'Pricing',
        'desc': 'Drive instant product sales with highly targeted shopping ads.',
        'type': 'pricing'
    },
    {
        'file': 'pricing-ppc.html', 'title': 'PPC Packages', 'badge': 'Pricing',
        'desc': 'Maximize your ad spend with expert Google Ads management.',
        'type': 'pricing'
    },
    {
        'file': 'portfolio.html', 'title': 'Our Work & Portfolio', 'badge': 'Case Studies',
        'desc': 'Explore how we have scaled revenue for B2B and SaaS companies globally.',
        'type': 'placeholder'
    },
    {
        'file': 'about.html', 'title': 'About GBO', 'badge': 'Our Story',
        'desc': 'We combine elite engineering with creative marketing to deliver unmatched digital growth.',
        'type': 'placeholder'
    },
    {
        'file': 'blog.html', 'title': 'Resources & Blog', 'badge': 'Insights',
        'desc': 'The latest strategies, algorithms updates, and marketing news from GBO experts.',
        'type': 'placeholder'
    },
    {
        'file': 'contact.html', 'title': 'Contact Us', 'badge': 'Get in Touch',
        'desc': 'Ready to dominate your market? Reach out to our strategy team today.',
        'type': 'placeholder'
    },
    {
        'file': 'free-consultation.html', 'title': 'Free Consultation', 'badge': 'Free Audit',
        'desc': 'Get a comprehensive analysis of your digital footprint, completely free.',
        'type': 'placeholder'
    },
    {
        'file': 'privacy-terms.html', 'title': 'Privacy & Terms', 'badge': 'Legal',
        'desc': 'Read our commitment to your data privacy and operational terms.',
        'type': 'placeholder'
    }
]

for p in pages:
    doc_html = f"<!DOCTYPE html>\n<html lang='en'>\n<head>\n<meta charset='UTF-8'>\n<meta name='viewport' content='width=device-width, initial-scale=1.0'>\n<title>{p['title']} - GBO</title>\n<link rel='stylesheet' href='style.css'>\n</head>\n<body>\n{header}\n"
    
    doc_html += generate_hero(p['title'], p['badge'], p['desc'])
    
    if p['type'] == 'standard' and p.get('content'):
        doc_html += native_formatter(p['content'])
    elif p['type'] == 'pricing':
        doc_html += pricing_formatter(p['title'])
    elif p['type'] == 'placeholder':
        doc_html += placeholder_formatter()

    doc_html += f"\n{footer}\n</body>\n</html>"
    write_file(p['file'], doc_html)

print("Synchronized native pages successfully built.")
