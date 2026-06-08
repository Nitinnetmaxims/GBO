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

# Just reuse the pricing formatter for all pricing pages to maintain the elite design.
def pricing_formatter(title):
    return f"""
    <section class="premium-pricing-section">
      <div class="container">
        <div class="pricing-header">
          <h2 style="font-size: var(--fs-h2); margin-bottom: 1rem;">Select Your {title} Plan</h2>
          <p style="color: rgba(255,255,255,0.7); max-width: 600px; margin: 0 auto;">Transparent pricing tailored for every stage of your business evolution.</p>
        </div>
        <div class="premium-pricing-grid">
          
          <div class="premium-pricing-card">
            <div class="pricing-title">Starter Plan</div>
            <div class="pricing-price">$999<span>/mo</span></div>
            <p style="color: rgba(255,255,255,0.6); margin-bottom: 2rem;">Essential features for growing businesses.</p>
            <a href="contact.html" class="btn btn-outline" style="width: 100%; text-align: center;">Choose Starter</a>
            <ul class="pricing-features">
              <li>Comprehensive Audit</li>
              <li>Basic Optimization</li>
              <li>Monthly Report</li>
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
              <li>Advanced Keyword Mapping</li>
              <li>High-Quality Link Building</li>
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
              <li>Predictive AI Modeling</li>
            </ul>
          </div>

        </div>
      </div>
    </section>
    """

def placeholder_formatter():
    return """
    <section class="split-section" style="min-height: 50vh; display: flex; align-items: center;">
        <div class="container" style="text-align: center;">
            <h2>Coming Soon</h2>
            <p style="color: var(--color-cool-gray); margin-top: 1rem;">We are currently curating the ultimate digital experience for this page. Stay tuned.</p>
        </div>
    </section>
    """

pages = [
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
    
    if p['type'] == 'pricing':
        doc_html += pricing_formatter(p['title'])
    elif p['type'] == 'placeholder':
        doc_html += placeholder_formatter()

    doc_html += f"\n{footer}\n</body>\n</html>"
    write_file(p['file'], doc_html)

print("Remaining premium pages successfully built.")
