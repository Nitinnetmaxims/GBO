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

def extract_section(doc, start_marker, end_marker):
    pattern = re.compile(rf"{re.escape(start_marker)}(.*?){re.escape(end_marker)}", re.DOTALL | re.IGNORECASE)
    match = pattern.search(doc)
    return match.group(1).strip() if match else ""

def format_html(text):
    # Basic markdown-to-html converter for this specific format
    lines = text.split('\n')
    html = ""
    in_list = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        
        if line.startswith('SECTION') or line.startswith('[Hero Section]') or line.startswith('________________'):
            continue
            
        if line.startswith('1️⃣') or line.startswith('2️⃣') or line.startswith('3️⃣') or line.startswith('4️⃣') or line.startswith('5️⃣') or line.startswith('6️⃣'):
            html += f"<h3>{line}</h3>"
        elif line.startswith('1.') or line.startswith('2.') or line.startswith('3.'):
            html += f"<h2>{line}</h2>"
        elif line.startswith('*') or line.startswith('•'):
            if not in_list:
                html += "<ul style='margin-bottom: 1.5rem;'>"
                in_list = True
            html += f"<li style='margin-bottom: 0.5rem;'>{line[1:].strip()}</li>"
        else:
            if in_list:
                html += "</ul>"
                in_list = False
            html += f"<p style='margin-bottom: 1.5rem;'>{line}</p>"
            
    if in_list:
        html += "</ul>"
    
    return html

# 1. Digital Marketing Services
dm_text = extract_section(content_md, "SECTION 2 — WHAT IS DIGITAL MARKETING?", "digital-marketing-strategy")
if dm_text:
    html = read_file('services-digital-marketing.html')
    formatted = format_html(dm_text)
    html = re.sub(r'<div class="content-wrapper".*?>.*?</div>', f'<div class="content-wrapper" style="max-width: 900px; margin: 0 auto; color: var(--color-cool-gray); line-height: 1.8;">{formatted}</div>', html, flags=re.DOTALL)
    write_file('services-digital-marketing.html', html)

# 2. Local SEO
local_text = extract_section(content_md, "Local SEO Services", "Local SEO Services FAQs")
if local_text:
    html = read_file('services-local-seo.html')
    formatted = format_html(local_text)
    html = re.sub(r'<div class="content-wrapper".*?>.*?</div>', f'<div class="content-wrapper" style="max-width: 900px; margin: 0 auto; color: var(--color-cool-gray); line-height: 1.8;">{formatted}</div>', html, flags=re.DOTALL)
    write_file('services-local-seo.html', html)

# 3. SEO Packages
seo_pack = extract_section(content_md, "[Pricing Tier Comparison]", "smo package")
if seo_pack:
    html = read_file('pricing-seo.html')
    formatted = format_html(seo_pack)
    html = re.sub(r'<div class="content-wrapper".*?>.*?</div>', f'<div class="content-wrapper" style="max-width: 900px; margin: 0 auto; color: var(--color-cool-gray); line-height: 1.8;">{formatted}</div>', html, flags=re.DOTALL)
    write_file('pricing-seo.html', html)

# 4. SMO Setup
smo_setup = extract_section(content_md, "STRUCTURAL SET-UP", "maiNTANCE paCKAGE")
if smo_setup:
    html = read_file('pricing-smo-setup.html')
    formatted = format_html(smo_setup)
    html = re.sub(r'<div class="content-wrapper".*?>.*?</div>', f'<div class="content-wrapper" style="max-width: 900px; margin: 0 auto; color: var(--color-cool-gray); line-height: 1.8;">{formatted}</div>', html, flags=re.DOTALL)
    write_file('pricing-smo-setup.html', html)

# 5. E-Commerce PPC
ecom_ppc = extract_section(content_md, "ECOM. PAckage", "PPC")
if ecom_ppc:
    html = read_file('pricing-ecommerce-ppc.html')
    formatted = format_html(ecom_ppc)
    html = re.sub(r'<div class="content-wrapper".*?>.*?</div>', f'<div class="content-wrapper" style="max-width: 900px; margin: 0 auto; color: var(--color-cool-gray); line-height: 1.8;">{formatted}</div>', html, flags=re.DOTALL)
    write_file('pricing-ecommerce-ppc.html', html)

# 6. PPC
ppc = extract_section(content_md, "Our PPC Plans", "SERVICES")
if ppc:
    html = read_file('pricing-ppc.html')
    formatted = format_html(ppc)
    html = re.sub(r'<div class="content-wrapper".*?>.*?</div>', f'<div class="content-wrapper" style="max-width: 900px; margin: 0 auto; color: var(--color-cool-gray); line-height: 1.8;">{formatted}</div>', html, flags=re.DOTALL)
    write_file('pricing-ppc.html', html)

print("Content populated into HTML files.")
