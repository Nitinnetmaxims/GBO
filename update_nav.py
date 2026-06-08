import re

with open('index.html', 'r') as f:
    html = f.read()

new_nav = """      <nav id="main-navigation">
        <a href="index.html">Home</a>
        <div class="nav-item">
          <a href="#">Services</a>
          <div class="dropdown-menu">
            <a href="services-digital-marketing.html">digital-marketing</a>
            <a href="services-local-seo.html">Local SEO Services</a>
            <a href="services-social-media.html">Social Media Marketing</a>
            <a href="services-seo.html">SEO</a>
            <a href="services-video-seo.html">Video SEO</a>
            <a href="services-digital-advertising.html">Digital Advertising</a>
          </div>
        </div>
        <div class="nav-item">
          <a href="#">Pricing & Packages</a>
          <div class="dropdown-menu">
            <a href="pricing-seo.html">SEO Packages</a>
            <div class="dropdown-item-nested">
              <a href="#">SMO Packages</a>
              <div class="nested-dropdown-menu">
                <a href="pricing-smo-setup.html">Structural Set-Up</a>
                <a href="pricing-smo-maintenance.html">Maintenance Package</a>
              </div>
            </div>
            <a href="pricing-ecommerce-ppc.html">E-Commerce PPC Plans</a>
            <a href="pricing-ppc.html">PPC Packages</a>
          </div>
        </div>
        <a href="portfolio.html">Portfolio / Our Work</a>
        <a href="about.html">About Us</a>
        <a href="blog.html">Resources / Blog</a>
        <div class="nav-item">
          <a href="#">Utility Pages</a>
          <div class="dropdown-menu">
            <a href="contact.html">Contact Us</a>
            <a href="free-consultation.html">Free Consultation</a>
            <a href="privacy-terms.html">Privacy & Terms</a>
          </div>
        </div>
      </nav>"""

html = re.sub(r'<nav id="main-navigation">.*?</nav>', new_nav, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)

print("Nav updated.")
