import re
import os

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

html_content = read_file('index.html')

# Extract header
header_match = re.search(r'(<header>.*?</header>)', html_content, re.DOTALL)
header = header_match.group(1) if header_match else '<header></header>'

# Extract footer
footer_match = re.search(r'(<footer>.*?</footer>)', html_content, re.DOTALL)
footer = footer_match.group(1) if footer_match else '<footer></footer>'

template = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{{{{TITLE}}}} - GBO</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  {header}

  <section class="hero" id="hero-section">
    <div class="container" style="text-align: center;">
      <span class="hero-badge">{{{{BADGE}}}}</span>
      <h1 style="margin-bottom: 1rem;">{{{{HERO_TITLE}}}}</h1>
      <p class="hero-desc" style="max-width: 800px; margin: 0 auto;">{{{{HERO_DESC}}}}</p>
    </div>
  </section>

  <section style="padding: 5rem 0;">
    <div class="container">
      <div class="content-wrapper" style="max-width: 900px; margin: 0 auto; color: var(--color-cool-gray); line-height: 1.8;">
        {{{{CONTENT}}}}
      </div>
    </div>
  </section>

  {footer}
</body>
</html>"""

pages_to_create = [
    ('services-digital-marketing.html', 'Digital Marketing Services', 'Services', 'Digital Marketing Services That Drive Real Business Growth', 'Increase Traffic. Generate Leads. Boost Revenue.'),
    ('services-local-seo.html', 'Local SEO Services', 'Services', 'Best Local SEO Services', 'Improve local search visibility, attract nearby customers, and increase leads with result-driven local SEO services.'),
    ('services-social-media.html', 'Social Media Marketing', 'Services', 'Social Media Marketing', 'Engage your audience and build your brand.'),
    ('services-seo.html', 'SEO Services', 'Services', 'Search Engine Optimization', 'Rank higher and drive targeted traffic.'),
    ('services-video-seo.html', 'Video SEO Services', 'Services', 'Video SEO', 'Optimize your video content for maximum visibility.'),
    ('services-digital-advertising.html', 'Digital Advertising Services', 'Services', 'Digital Advertising', 'Targeted campaigns for immediate ROI.'),
    ('pricing-seo.html', 'SEO Packages', 'Pricing', 'SEO Packages That Help You Grow Your Revenue', 'Simple, clear SEO pricing with custom plans for startups, growing businesses, and large companies.'),
    ('pricing-smo-setup.html', 'SMO Structural Set-Up', 'Pricing', 'One Time Structural Set-UP', 'Complete social media foundation for your brand.'),
    ('pricing-smo-maintenance.html', 'SMO Maintenance Package', 'Pricing', 'SMO Maintenance Packages', 'Ongoing social media optimization and growth.'),
    ('pricing-ecommerce-ppc.html', 'E-Commerce PPC Plans', 'Pricing', 'E-Commerce PPC Plans', 'Drive online sales with targeted advertising.'),
    ('pricing-ppc.html', 'PPC Packages', 'Pricing', 'PPC Packages', 'Google Ads and Pay-Per-Click management.'),
    ('portfolio.html', 'Our Work & Portfolio', 'Portfolio', 'Our Work & Portfolio', 'See how we have helped brands scale.'),
    ('about.html', 'About Us', 'Company', 'About GBO', 'We combine deep machine learning algorithm simulations with rigorous keyword research.'),
    ('blog.html', 'Resources & Blog', 'Resources', 'Resources & Blog', 'Latest insights in AI SEO and Digital Marketing.'),
    ('contact.html', 'Contact Us', 'Contact', 'Get In Touch', 'Start your growth journey today.'),
    ('free-consultation.html', 'Free Consultation', 'Consultation', 'Get Your Free Proposal', 'Let GBO analyze your digital footprint.'),
    ('privacy-terms.html', 'Privacy Policy & Terms', 'Legal', 'Privacy & Terms', 'Our commitment to your privacy.')
]

import sys

for filename, title, badge, hero_title, hero_desc in pages_to_create:
    page_html = template.replace('{{TITLE}}', title)\
                        .replace('{{BADGE}}', badge)\
                        .replace('{{HERO_TITLE}}', hero_title)\
                        .replace('{{HERO_DESC}}', hero_desc)\
                        .replace('{{CONTENT}}', f'<h2>{title}</h2><p>Content for {title} goes here. This will be replaced with the full copy.</p>')
    write_file(filename, page_html)

print("Generated templates for all pages.")
