import re
import os

def read_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()

def write_file(filepath, content):
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Extract native parts from index.html
index_html = read_file('index.html')

# Extract header
header_match = re.search(r'(<header>.*?</header>)', index_html, re.DOTALL)
header_html = header_match.group(1) if header_match else ""

# Extract footer
footer_match = re.search(r'(<footer>.*?</footer>)', index_html, re.DOTALL)
footer_html = footer_match.group(1) if footer_match else ""

# Extract head contents (meta tags, css links)
head_match = re.search(r'<head>(.*?)</head>', index_html, re.DOTALL)
head_content = head_match.group(1) if head_match else ""
# Clean up title and description in head_content so we can replace them dynamically
head_content = re.sub(r'<title>.*?</title>', '', head_content)
head_content = re.sub(r'<meta name=\"description\" content=\".*?\">', '', head_content)

# Define universal head formatter
def make_head(title, description):
    return f"""<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - GBO</title>
  <meta name="description" content="{description}">
  {head_content.strip()}
</head>"""

# Define universal FAQ Script
faq_script = """
<script>
document.addEventListener('DOMContentLoaded', () => {
  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const btn = item.querySelector('.faq-question-btn');
    if (!btn) return;
    
    btn.addEventListener('click', () => {
      const isActive = item.classList.contains('active');
      
      // Close all FAQs
      faqItems.forEach(i => {
        i.classList.remove('active');
        const content = i.querySelector('.faq-answer');
        if(content) content.style.maxHeight = null;
      });

      // If it wasn't active, open it
      if (!isActive) {
        item.classList.add('active');
        const content = item.querySelector('.faq-answer');
        if(content) {
          content.style.maxHeight = content.scrollHeight + 'px';
        }
      }
    });
  });
});
</script>
"""

# Universal CTA Form template
def make_cta_banner(heading="Claim Your<br>Free Website Audit."):
    return f"""
  <section class="cta-banner" id="cta-banner">
    <div class="container">
      <div class="cta-left">
        <h2>{heading}</h2>
      </div>
      <div class="cta-right">
        <form id="cta-audit-form" action="free-consultation.html">
          <div class="cta-form-grid">
            <input type="text" placeholder="Full Name" required id="cta-name">
            <input type="email" placeholder="Email Address" required id="cta-email">
            <input type="url" placeholder="Website URL" required id="cta-website">
            <select required id="cta-budget">
              <option value="" disabled selected>Monthly Budget</option>
              <option value="under-1k">Under $1,000</option>
              <option value="1k-5k">$1,000 - $5,000</option>
              <option value="5k-10k">$5,000 - $10,000</option>
              <option value="above-10k">Above $10,000</option>
            </select>
          </div>
          <button type="submit" class="btn btn-dark cta-form-btn" id="cta-submit-btn">Get My Free Website Audit</button>
        </form>
      </div>
    </div>
  </section>
"""

def make_hero(badge, title, desc, cta_text="Get Started Now", cta_link="free-consultation.html"):
    return f"""
  <section class="hero" id="hero-section" style="padding-bottom: 4rem;">
    <div class="container" style="display: flex; justify-content: center; text-align: center;">
      <div class="hero-left" style="max-width: 800px; padding-right: 0;">
        <span class="hero-badge">{badge}</span>
        <h1 style="margin-bottom: 1.5rem;">{title}</h1>
        <p class="hero-desc">{desc}</p>
        <div class="hero-form-wrapper" style="justify-content: center; display: flex;">
          <a href="{cta_link}" class="btn btn-primary">{cta_text} &rarr;</a>
        </div>
      </div>
    </div>
  </section>
"""

def make_split_screen(title, p1, p2="", list_items=None, dark_bg=True):
    bg_style = "background: #111; color: white;" if dark_bg else "background: #fff; color: #1a1a1a;"
    text_color = "color: var(--color-cool-gray);" if dark_bg else "color: #555;"
    list_html = ""
    if list_items:
        list_html = f"<ul style='margin-top: 1.5rem; padding-left: 1.5rem; {text_color}'>"
        for item in list_items:
            list_html += f"<li style='margin-bottom: 0.5rem;'>{item}</li>"
        list_html += "</ul>"
        
    p2_html = f"<p style='margin-top: 1rem; {text_color}'>{p2}</p>" if p2 else ""

    return f"""
  <section class="marketing-revenue" style="padding: 6rem 0; {bg_style}">
    <div class="container">
      <div class="marketing-content-wrapper" style="display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center;">
        <div class="marketing-acc-content" style="display: block; opacity: 1; height: auto;">
          <h2 style="font-size: 2.5rem; margin-bottom: 1.5rem;">{title}</h2>
          <p style="line-height: 1.8; {text_color}">{p1}</p>
          {p2_html}
          {list_html}
        </div>
        <div class="marketing-image-panel">
          <img src="images/video_player.png" alt="Video Player Mockup" style="width: 100%; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.15);">
        </div>
      </div>
    </div>
  </section>
"""

def make_growth_engine(heading, cards):
    cards_html = ""
    for c in cards:
        cards_html += f"""
        <div class="growth-card" style="display: flex; flex-direction: column; justify-content: space-between;">
          <div>
            <h3>{c['title']}</h3>
            <p>{c['desc']}</p>
          </div>
          <div class="growth-card-graphic" style="margin-top: 1.5rem;">
            <img src="assets/growth-engine/search-intent.png" alt="Growth engine icon" style="height: 48px; width: auto; opacity: 0.85;">
          </div>
        </div>
        """
    return f"""
  <section class="growth-engine" id="growth-engine" style="padding: 6rem 0; background: var(--color-warm-white);">
    <div class="container">
      <h2 style="text-align: center; margin-bottom: 3.5rem;">{heading}</h2>
      <div class="growth-grid" id="growth-cards-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
        {cards_html}
      </div>
    </div>
  </section>
"""

def make_process_section(heading, steps):
    steps_html = ""
    for i, s in enumerate(steps):
        num = f"0{i+1}" if i+1 < 10 else str(i+1)
        steps_html += f"""
        <div class="process-step">
          <div class="step-icon"><img src="assets/Proven Process/step-{((i)%5)+1}.svg" alt="Step Icon"></div>
          <div class="step-number">{num}</div>
          <h4 class="step-title">{s['title']}</h4>
          <p class="step-desc">{s['desc']}</p>
        </div>
        """
    return f"""
  <section class="process-section" style="background: #111; color: white; padding: 6rem 0;">
    <div class="container">
      <div class="process-heading-wrapper" style="text-align: center; margin-bottom: 4rem;">
        <span class="process-label" style="color: var(--color-fire-engine-red);">OUR METHODOLOGY</span>
        <h2 style="margin-top: 1rem;">{heading}</h2>
      </div>
      <div class="process-timeline" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 2rem;">
        {steps_html}
      </div>
    </div>
  </section>
"""

def make_faq_section(heading, faqs):
    faq_html = ""
    for f in faqs:
        faq_html += f"""
        <div class="faq-item" style="border-bottom: 1px solid #eaeaea; padding: 1.5rem 0;">
          <button class="faq-question-btn" style="width: 100%; display: flex; justify-content: space-between; align-items: center; background: none; border: none; font-size: 1.2rem; font-weight: 600; text-align: left; cursor: pointer; color: #1a1a1a; padding: 0;">
            {f['q']}
            <span class="faq-icon" style="transition: transform var(--duration-base) var(--ease-standard); display: flex; align-items: center;">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>
            </span>
          </button>
          <div class="faq-answer" style="max-height: 0; overflow: hidden; transition: max-height var(--duration-base) var(--ease-standard);">
            <p style="color: var(--color-cool-gray); line-height: 1.8; margin-top: 1rem; font-size: 1rem; font-style: normal;">{f['a']}</p>
          </div>
        </div>
        """
    return f"""
  <section class="faq" id="faq" style="padding: 6rem 0; background: #fff;">
    <div class="container" style="max-width: 800px;">
      <div class="faq-header" style="text-align: center; margin-bottom: 3.5rem;">
        <h2>{heading}</h2>
      </div>
      <div class="faq-list" id="faq-accordions">
        {faq_html}
      </div>
    </div>
  </section>
"""

def make_stats_bar(stats):
    stats_html = ""
    for s in stats:
        stats_html += f"""
      <div class="stat-item" style="text-align: center;">
        <div class="stat-val" style="font-size: 3rem; font-weight: 700; color: var(--color-fire-engine-red);">{s['val']}</div>
        <div class="stat-label" style="font-size: 0.95rem; color: var(--color-cool-gray); margin-top: 0.5rem; text-transform: uppercase; letter-spacing: 1px;">{s['label']}</div>
      </div>
        """
    return f"""
  <section class="stats-bar" id="stats-section" style="padding: 3rem 0; background: #111; border-top: 1px solid #222; border-bottom: 1px solid #222;">
    <div class="container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 3rem;">
      {stats_html}
    </div>
  </section>
"""

# HTML Template Assembler
def build_html_page(filename, title, description, badge, hero_title, hero_desc, sections_html, scripts=""):
    head = make_head(title, description)
    html = f"""<!DOCTYPE html>
<html lang="en">
{head}
<body>
{header_html}
{make_hero(badge, hero_title, hero_desc)}
{sections_html}
{footer_html}
{faq_script}
{scripts}
</body>
</html>"""
    write_file(filename, html)
    print(f"Built page: {filename}")

# =========================================================================
# PAGES DATA DEFINITIONS
# =========================================================================

# 1. services-digital-marketing.html
dm_sections = make_split_screen(
    "What is Digital Marketing?",
    "Digital marketing is the process of promoting businesses, products, and services through online platforms and digital channels. It helps brands connect directly with potential customers through the internet using powerful marketing techniques. By leveraging search engine optimization, paid advertising, and targeted content, we build sustainable, high-converting organic pipeline growth.",
    "Modern digital marketing includes multiple channels such as SEO, Google Ads, Social Media, Email, and Reputation Management. We align all channels specifically for search algorithms and modern AI generative search tools.",
    ["Search Engine Optimization (SEO)", "Google Ads & PPC Campaigns", "Social Media Marketing", "YouTube & Video Optimization", "Content Marketing Solutions", "Email Marketing & Lead Nurturing"]
) + make_growth_engine(
    "Why Your Business Needs Digital Marketing",
    [
        {"title": "Reach Targeted Audiences Globally", "desc": "Connect with prospects anywhere based on demography, search intent, and online behavior."},
        {"title": "Generate Quality Leads Consistently", "desc": "Build repeatable inbound pipelines of high-intent buyers looking for your solutions."},
        {"title": "Increase Online Visibility", "desc": "Rank at the top of search engine results pages and AI search engine recommendations."},
        {"title": "Build Brand Authority", "desc": "Establish credibility and position your business as a trusted industry leader."},
        {"title": "Improve Customer Trust", "desc": "Engage prospects transparently, build community, and manage online brand reputation."},
        {"title": "Maximize ROI & Sales", "desc": "Optimize campaign budget allocation to ensure every dollar spent returns maximum revenue."}
    ]
) + make_process_section(
    "Our Performance-Driven Process",
    [
        {"title": "Research & Analysis", "desc": "We analyze your business, target audience, and local competitor visibility gaps."},
        {"title": "Goal Definition & Strategy", "desc": "We define target goals and allocate marketing budgets to high-ROI channels."},
        {"title": "Setup & Optimization", "desc": "We set up tracking pixels, design clean landing pages, and optimize site UX."},
        {"title": "Campaign Launch", "desc": "We launch targeted search ads, organic SEO, and social marketing campaigns."},
        {"title": "Monitor & Scale", "desc": "We track performance, execute A/B split tests, and scale winning campaigns."}
    ]
) + make_faq_section(
    "Digital Marketing FAQs",
    [
        {"q": "What is digital marketing?", "a": "Digital marketing refers to any marketing campaign, promotion, or branding asset that runs on digital channels like search engines, social media platforms, email, and websites."},
        {"q": "How does digital marketing help my business?", "a": "It connects you with high-intent prospects, increases brand visibility, automates lead generation, and provides measurable data to optimize ROI."},
        {"q": "Which digital marketing channel is best for my brand?", "a": "It depends on your business type. B2B and SaaS brands typically see high ROI from SEO, LinkedIn, and PPC, while e-commerce brands excel with Meta ads, Google Shopping, and SEO."},
        {"q": "How long does it take to see results?", "a": "PPC and social media ads yield immediate traffic and leads, while organic search optimization (SEO) and content marketing usually show significant returns in 3 to 6 months."}
    ]
) + make_cta_banner("Start Growing Your<br>Brand Digitally Today.")

build_html_page(
    "services-digital-marketing.html",
    "Digital Marketing Services",
    "Accelerate your business growth with GBO's data-driven digital marketing solutions covering SEO, PPC, and Social Media.",
    "Full-Funnel Growth",
    "Digital Marketing Services That Drive Real Business Growth",
    "Leverage data-driven strategies across SEO, PPC, and Content to dominate your market, outrank competitors, and capture high-intent leads automatically.",
    dm_sections
)

# 2. services-local-seo.html
local_sections = make_split_screen(
    "What is Local SEO?",
    "Local SEO is the practice of optimizing your online presence to attract more business from relevant local searches on Google and other search engines. It ensures your business appears in local map packs and search queries at the exact moment local customers search for your services nearby.",
    "Over 80% of local mobile searches result in a purchase or store visit. By optimizing your Google Business Profile (GBP), building NAP citations, and targeting location keywords, we capture this high-intent traffic.",
    ["Rank for location-based and 'near me' searches", "Appear in the Google Maps Local 3-Pack", "Drive local foot traffic and phone calls", "Optimize Google Business Profile visibility"]
) + make_growth_engine(
    "Why Choose GBO for Local SEO",
    [
        {"title": "Google Maps Domination", "desc": "We position your business in the Local 3-Pack where 70% of local clicks happen."},
        {"title": "NAP Citation Consistency", "desc": "We align your business Name, Address, and Phone data across directories to build search trust."},
        {"title": "Review Loop Automation", "desc": "We optimize customer review collection to boost organic trust signals and local map rankings."},
        {"title": "Local Keyword Research", "desc": "We discover high-value keywords combined with location-specific search modifiers."},
        {"title": "Local Competitor Analysis", "desc": "We analyze local competitor citation density and outrank them systematically."},
        {"title": "Transparent Reporting", "desc": "Track your location visibility, call counts, and lead conversions with clear monthly reports."}
    ]
) + make_process_section(
    "Our Local SEO Strategic Process",
    [
        {"title": "Google Business Profile Audit", "desc": "Review GBP settings, classification tags, description text, and geo-coordinates."},
        {"title": "Directory NAP Cleanup", "desc": "Audit and build clean business directory citations, resolving duplicate or incorrect listings."},
        {"title": "On-Page Geo Optimization", "desc": "Integrate local city, county, and neighborhood keywords into website metadata and copy."},
        {"title": "Review Collection Setup", "desc": "Implement automated SMS/Email workflows to gather positive customer feedback on Google."},
        {"title": "Local Link Building", "desc": "Secure links from local business organizations, chambers of commerce, and local blogs."}
    ]
) + make_faq_section(
    "Local SEO FAQs",
    [
        {"q": "What is local SEO?", "a": "Local SEO is search engine optimization focused on improving your rankings in local search results and Google Maps listings."},
        {"q": "Why is local SEO important?", "a": "Local SEO is crucial for businesses with physical storefronts or service regions, helping nearby customers find your business when looking for local solutions."},
        {"q": "How long does local SEO take to show results?", "a": "Most local campaigns start seeing map pack and local keyword improvements within 3 to 6 months depending on local competition."},
        {"q": "What is Google Business Profile optimization?", "a": "It involves setting up and fully configuring your Google map listing with correct categories, descriptions, images, hours, and active review loops."}
    ]
) + make_cta_banner("Dominate Your Region.<br>Claim Your Maps Audit.")

build_html_page(
    "services-local-seo.html",
    "Best Local SEO Services",
    "Dominate local searches, rank in the Google Maps Local 3-Pack, and attract nearby customers with GBO's Local SEO services.",
    "Dominate Your Region",
    "Best Local SEO Services",
    "Capture high-intent local traffic, dominate Google Maps, and turn nearby searchers into loyal customers with our customized local search optimization.",
    local_sections
)

# 3. services-social-media.html
social_sections = make_split_screen(
    "What is Social Media Marketing?",
    "Social Media Marketing (SMM) helps brands promote their products and services across major social networks. With the right strategy, businesses can increase brand awareness, build organic trust, engage customers directly, and drive paid traffic to high-converting landing pages.",
    "We manage and grow your social media pages to help you reach more people and acquire new customers organically. We curate tailored creative calendars that translate followers into revenue.",
    ["Profile optimization across all platforms", "Custom high-quality graphic & video content calendars", "Organic follower growth & active community management", "High-performing paid social advertising campaigns"]
) + make_growth_engine(
    "Why Social Media Marketing Matters",
    [
        {"title": "Increase Brand Awareness", "desc": "Stay top-of-mind and build recognizable brand identity across social networks."},
        {"title": "Targeted Audience Reach", "desc": "Deliver customized messaging to the exact demographics interested in your services."},
        {"title": "Drive Organic Traffic", "desc": "Direct social followers to your website through strategic content links and promotions."},
        {"title": "Build Brand Credibility", "desc": "Keep profiles active, professional, and filled with social proof and case studies."},
        {"title": "Improve Customer Retention", "desc": "Communicate directly with customers, answering queries and resolving feedback in real-time."},
        {"title": "Boost Sales & ROI", "desc": "Convert social engagement into paid customer acquisition with conversion-focused ad funnels."}
    ]
) + make_process_section(
    "Our Social Media Management Process",
    [
        {"title": "Profile & Competitor Audit", "desc": "Analyze current profiles, branding consistency, and competitor engagement metrics."},
        {"title": "Content Strategy Development", "desc": "Design custom content pillars, posting schedules, and visual brand guidelines."},
        {"title": "Graphic & Video Asset Creation", "desc": "Write high-converting captions, design custom graphics, and edit engaging videos."},
        {"title": "Active Community Building", "desc": "Monitor comments, reply to direct messages, and engage with relevant target accounts."},
        {"title": "Performance Tracking & Scaling", "desc": "Track reach, follow metrics, CTR, and scale winning content formats."}
    ]
) + make_faq_section(
    "Social Media Marketing FAQs",
    [
        {"q": "Which social platforms should my business be on?", "a": "It depends on where your target audience spends their time. B2C brands typically excel on Instagram, Facebook, and TikTok, while B2B brands prioritize LinkedIn and YouTube."},
        {"q": "How often should my business post?", "a": "Consistency is key. We typically recommend posting 3 to 5 times per week to maintain active visibility without spamming your audience."},
        {"q": "Is organic social media enough?", "a": "Organic posts are crucial for brand credibility, but combining organic posting with targeted paid social ads yields faster lead generation and customer acquisition."},
        {"q": "How do you measure social media success?", "a": "We track reach, follower growth, engagement rates, click-through rates, and ultimately conversion leads generated from social campaigns."}
    ]
) + make_cta_banner("Ready to Grow Your Brand?<br>Book Your Social Audit.")

build_html_page(
    "services-social-media.html",
    "Social Media Marketing",
    "Build a loyal community and drive customer conversions across all major social networks with GBO's Social Media Marketing.",
    "Brand Engagement",
    "Social Media Marketing Services",
    "We manage and grow your social media pages to help you reach more people, build communities, and get new customers.",
    social_sections
)

# 4. services-seo.html
seo_sections = make_split_screen(
    "What are SEO Services?",
    "Search Engine Optimization (SEO) is the process of optimizing your website to improve its visibility in search engines. By aligning your site's structure, technical health, and content authority with search engine algorithms and user search intent, we build high-converting organic pipelines.",
    "Traditional search is evolving rapidly. We optimize your website not only for standard search engine rankings on Google but also for generative AI engine answers (GEO/AEO) to secure your brand's future visibility.",
    ["Comprehensive technical website audits", "In-depth keyword research and intent mapping", "On-page title, meta, and heading optimizations", "Authority-driven link building & digital PR"]
) + make_growth_engine(
    "Why Choose GBO for SEO",
    [
        {"title": "Rankings Dominance", "desc": "We rank your website at the top of Google search results for transactional search queries."},
        {"title": "AI Generative Engine Optimization", "desc": "Optimize your content to appear in AI recommendations on ChatGPT, Gemini, and Perplexity."},
        {"title": "Core Web Vitals Optimization", "desc": "Clean up technical page performance, mobile responsiveness, and load speeds."},
        {"title": "Topical Authority Mapping", "desc": "Create comprehensive semantic content hubs that establish your brand as an industry authority."},
        {"title": "Safe White-Hat Link Building", "desc": "Build backlink networks from high-authority websites using ethical, spam-free methodologies."},
        {"title": "Monthly Growth Reporting", "desc": "Track your rankings progress, organic traffic volume, and lead conversions transparently."}
    ]
) + make_process_section(
    "Our SEO Implementation Process",
    [
        {"title": "Technical SEO Audit", "desc": "Analyze site speed, crawlability, sitemaps, robots.txt, schema, and mobile compatibility."},
        {"title": "Keyword & Intent Mapping", "desc": "Find high-converting transactional keywords and map them to targeted landing pages."},
        {"title": "On-Page SEO Execution", "desc": "Optimize title tags, meta descriptions, image alt tags, H1-H3 structures, and internal links."},
        {"title": "Topical Content Creation", "desc": "Draft highly optimized blog posts and service content focused on search user intent."},
        {"title": "Authority Building (Link Building)", "desc": "Deploy outreach campaigns to acquire quality backlinks from industry-relevant sites."}
    ]
) + make_faq_section(
    "SEO Services FAQs",
    [
        {"q": "What is SEO?", "a": "SEO stands for Search Engine Optimization, which is the process of improving your website to increase its visibility in search engine results."},
        {"q": "How long does SEO take to show results?", "a": "Most organic SEO campaigns begin showing noticeable improvements in traffic and rankings within 3 to 6 months depending on competition and website condition."},
        {"q": "What is the difference between SEO and PPC?", "a": "PPC (Pay-Per-Click) is paid advertising where you pay for each click. SEO is organic search optimization where traffic is free, building long-term sustainable pipeline."},
        {"q": "Do you guarantee #1 rankings?", "a": "No ethical SEO agency guarantees specific ranking spots due to search algorithm updates, but we guarantee to apply industry-standard white hat optimization that drives traffic growth."}
    ]
) + make_cta_banner("Claim Your Technical<br>SEO Audit Report.")

build_html_page(
    "services-seo.html",
    "SEO Services",
    "Outrank competitors, scale organic search traffic, and capture high-intent leads automatically with GBO's advanced SEO services.",
    "Organic Dominance",
    "Advanced SEO Services",
    "We help your website rank higher on Google so more people can find your business. This brings you more visitors and better business growth.",
    seo_sections
)

# 5. services-video-seo.html
video_sections = make_split_screen(
    "What is Video SEO?",
    "Video SEO is the practice of optimizing video content to rank in search results on video platforms (like YouTube) and search engines (like Google). It ensures your target audience discovers your video tutorials, product reviews, and brand assets at the exact moment they search for answers.",
    "YouTube is the second largest search engine in the world. By optimizing video titles, description metadata, tags, and thumbnails, we maximize views, watch time, and subscriber conversions.",
    ["YouTube video & channel optimization", "Video-specific keyword research and search intent mapping", "High-CTR custom thumbnail design and testing", "SRT subtitle transcription file generation"]
) + make_growth_engine(
    "Why Video SEO Matters",
    [
        {"title": "YouTube Search Rankings", "desc": "Position your videos at the top of YouTube searches for relevant topic terms."},
        {"title": "Google Video Carousel Listings", "desc": "Optimize website videos to appear in Google search snippets and video tabs."},
        {"title": "Maximize Watch Time", "desc": "Structure video description timestamps and playlist layouts to increase session duration."},
        {"title": "Click-Through-Rate Optimization", "desc": "Test video titles and thumbnail visuals to maximize user click rates."},
        {"title": "Lead & Subscriber Conversion", "desc": "Include clear annotation calls and description link paths to drive website traffic."},
        {"title": "Video Schema Integration", "desc": "Implement structured video schema tags on site pages to assist search crawl bots."}
    ]
) + make_process_section(
    "Our Video SEO Optimization Process",
    [
        {"title": "Channel Audit & Setup", "desc": "Verify channel configuration, playlist arrangements, visual assets, and descriptions."},
        {"title": "Video Keyword Research", "desc": "Identify transactional keywords that display video results on Google and YouTube searches."},
        {"title": "Metadata Optimization", "desc": "Optimize video title tags, write informative descriptions, and input targeted search tags."},
        {"title": "Thumbnail Creation & Layout", "desc": "Design eye-catching custom thumbnails that increase user click interest."},
        {"title": "Schema & Subtitle Embedding", "desc": "Embed video files on your site, add VideoObject schema, and upload accurate SRT captions."}
    ]
) + make_faq_section(
    "Video SEO FAQs",
    [
        {"q": "What is Video SEO?", "a": "Video SEO is the process of optimizing your video content so that it ranks higher in search results on video platforms like YouTube and standard search engines like Google."},
        {"q": "Why is YouTube SEO important?", "a": "YouTube is the second largest search engine globally. Optimizing your video content helps you capture massive intent-driven audiences."},
        {"q": "Do you design custom thumbnails?", "a": "Yes, we help design high-CTR, brand-consistent custom thumbnails to increase click-through rates."},
        {"q": "How long does it take for video SEO to work?", "a": "YouTube search updates rankings very quickly, so optimized video metadata can show ranking increases in just a few days to weeks."}
    ]
) + make_cta_banner("Grow Your Video Views.<br>Get a Free Channel Audit.")

build_html_page(
    "services-video-seo.html",
    "Video SEO Services",
    "Boost video rankings, maximize watch time, and grow YouTube subscribers with GBO's expert Video SEO services.",
    "YouTube & Beyond",
    "Video SEO Services",
    "We improve your videos so they get more views, watch time, and rank better on YouTube and Google search.",
    video_sections
)

# 6. services-digital-advertising.html
adv_sections = make_split_screen(
    "What is Digital Advertising?",
    "Digital advertising allows businesses to target high-intent prospects across search engines, social media platforms, and website networks. By leveraging real-time bidding, interest targeting, and keyword intent, we put your brand in front of customers ready to buy.",
    "We run targeted ads on Google and social media to bring real and interested customers to your business, scaling your revenue footprint instantly.",
    ["Google Ads & Search PPC Campaigns", "Facebook & Instagram Social Advertising", "LinkedIn Lead Generation Management", "Dynamic Product Catalog Ads & Remarketing"]
) + make_growth_engine(
    "Why Choose GBO for Digital Ads",
    [
        {"title": "Instant Lead Generation", "desc": "Drive qualified traffic to your website from day one without waiting for SEO rankings."},
        {"title": "Precision Demographic Targeting", "desc": "Focus ad spend only on specific locations, demographics, interests, and keywords."},
        {"title": "Maximized Advertising ROI", "desc": "Continuously optimize bidding strategies and ad creatives to reduce cost-per-acquisition."},
        {"title": "Creative Ad Copywriting", "desc": "Write high-converting ad copy and design creative visual banner assets."},
        {"title": "Conversion Rate Optimization", "desc": "Optimize campaign landing pages to increase lead and purchase conversions."},
        {"title": "Dedicated PPC Specialist Support", "desc": "Certified account managers actively review, test, and scale your PPC campaigns."}
    ]
) + make_process_section(
    "Our Paid Advertising Process",
    [
        {"title": "Competitor & Market Analysis", "desc": "Analyze competitor keywords, ad copy hooks, and target landing page structures."},
        {"title": "Campaign Structure Configuration", "desc": "Design campaign architecture, allocate budgets, and set target audience parameters."},
        {"title": "Ad Writing & Asset Design", "desc": "Draft high-CTR copy variations and coordinate graphic/video creative designs."},
        {"title": "Tracking & Tag Implementation", "desc": "Install Google Tag Manager, Google Analytics, and conversion tracking pixels."},
        {"title": "A/B Testing & Daily Optimization", "desc": "Audit search terms, adjust bids, add negative keywords, and scale successful ads."}
    ]
) + make_faq_section(
    "Digital Advertising FAQs",
    [
        {"q": "What platforms do you advertise on?", "a": "We manage campaigns across Google Ads, Bing, Facebook, Instagram, LinkedIn, YouTube, and Pinterest."},
        {"q": "How much budget do I need for digital ads?", "a": "We manage ad budgets of all sizes, from local small business budgets ($1,000/mo) up to enterprise-scale budgets ($20,000+/mo)."},
        {"q": "What is the setup fee?", "a": "We charge a transparent setup fee based on campaign complexity and count, followed by a monthly management percentage."},
        {"q": "How quickly can campaigns start?", "a": "Typically, from audit and onboarding to ad launch takes 5 to 7 business days."}
    ]
) + make_cta_banner("Scale Your Lead Volume.<br>Request a PPC Proposal.")

build_html_page(
    "services-digital-advertising.html",
    "Digital Advertising",
    "Scale business revenue instantly with high-converting Google Ads, PPC, and social advertising managed by GBO.",
    "Paid Growth",
    "Digital Advertising Services",
    "We run targeted ads on Google and social media to bring real and interested customers to your business, scaling your revenue instantly.",
    adv_sections
)

# =========================================================================
# PRICING PAGES
# =========================================================================

# 7. pricing-seo.html
seo_pricing_html = f"""
<section class="pricing-hero" style="padding: 8rem 0 4rem; text-align: center;">
  <div class="container" style="text-align: center;">
    <span class="process-label" style="display: inline-block; margin-bottom: 1rem; color: var(--color-fire-engine-red); font-weight: 700; letter-spacing: 2px;">PRICING</span>
    <h1>SEO Packages. <span class="highlight-red">Scale Your Rankings.</span></h1>
    <p style="font-size: 1.2rem; color: #666; max-width: 600px; margin: 0 auto 3rem;">Select the plan that suits you and start your journey.</p>
    
    <div class="new-pricing-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 2rem;">
      <div class="new-pricing-card">
        <div class="new-pricing-header"><h3>Basic Plan</h3><p>Essential SEO setup</p></div>
        <div class="new-pricing-price"><span class="new-currency">$</span><span class="new-amount">500</span><span class="new-interval">/Monthly</span></div>
        <a href="contact.html?plan=seo-basic" class="new-pricing-btn" style="text-align: center; text-decoration: none; line-height: 54px;">Select Plan</a>
        <div class="new-pricing-features">
          <ul>
            <li><i>&#10003;</i> 20 Keywords</li>
            <li><i>&#10003;</i> 40 Backlinks / month</li>
            <li><i>&#10003;</i> Up to 10 Pages Optimized</li>
            <li><i>&#10003;</i> GBP (GMB) - X</li>
            <li><i>&#10003;</i> AI Audit - 2 pages</li>
          </ul>
        </div>
      </div>
      <div class="new-pricing-card">
        <div class="new-pricing-header"><h3>Silver Plan</h3><p>Ideal for growing brands</p></div>
        <div class="new-pricing-price"><span class="new-currency">$</span><span class="new-amount">700</span><span class="new-interval">/Monthly</span></div>
        <a href="contact.html?plan=seo-silver" class="new-pricing-btn" style="text-align: center; text-decoration: none; line-height: 54px;">Select Plan</a>
        <div class="new-pricing-features">
          <ul>
            <li><i>&#10003;</i> 40 Keywords</li>
            <li><i>&#10003;</i> 60 Backlinks / month</li>
            <li><i>&#10003;</i> Up to 15 Pages Optimized</li>
            <li><i>&#10003;</i> GBP (GMB) - ✓</li>
            <li><i>&#10003;</i> AI Audit - 4 pages</li>
          </ul>
        </div>
      </div>
      <div class="new-pricing-card highlighted">
        <div class="new-pricing-header"><h3>Gold Plan</h3><p>Best Seller - Total SEO Domination</p></div>
        <div class="new-pricing-price"><span class="new-currency">$</span><span class="new-amount">900</span><span class="new-interval">/Monthly</span></div>
        <a href="contact.html?plan=seo-gold" class="new-pricing-btn featured-btn" style="text-align: center; text-decoration: none; line-height: 54px;">Select Plan</a>
        <div class="new-pricing-features featured-features">
          <ul>
            <li><i>&#10003;</i> 60 Keywords</li>
            <li><i>&#10003;</i> 100 Backlinks / month</li>
            <li><i>&#10003;</i> Up to 25 Pages Optimized</li>
            <li><i>&#10003;</i> GBP (GMB) - ✓</li>
            <li><i>&#10003;</i> Geotagging - ✓</li>
            <li><i>&#10003;</i> AI Audit - 6 pages</li>
          </ul>
        </div>
      </div>
      <div class="new-pricing-card">
        <div class="new-pricing-header"><h3>Premium Plan</h3><p>Full SEO & AI GEO Package</p></div>
        <div class="new-pricing-price"><span class="new-currency">$</span><span class="new-amount">1500</span><span class="new-interval">/Monthly</span></div>
        <a href="contact.html?plan=seo-premium" class="new-pricing-btn" style="text-align: center; text-decoration: none; line-height: 54px;">Select Plan</a>
        <div class="new-pricing-features">
          <ul>
            <li><i>&#10003;</i> 100 Keywords</li>
            <li><i>&#10003;</i> 200 Backlinks / month</li>
            <li><i>&#10003;</i> Up to 40 Pages Optimized</li>
            <li><i>&#10003;</i> GBP & Geotagging - ✓</li>
            <li><i>&#10003;</i> G.E.O & A.E.O - ✓</li>
            <li><i>&#10003;</i> AI Audit - 8 pages</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="comparison-table-section" style="padding: 4rem 0 6rem; background: #fff;">
  <div class="container">
    <div class="compare-heading-wrapper" style="text-align: center; margin-bottom: 3rem;">
      <h2 style="font-family: var(--font-heading); font-size: 2.2rem; font-weight: 600; color: #1a1a1a;">SEO Packages Comparison Matrix</h2>
      <p style="color: #666; margin-top: 0.5rem;">Detailed features and parameters of our search engine optimization plans.</p>
    </div>
    <div class="compare-table-container" style="border: 1px solid #eaeaea; border-radius: 12px; overflow: hidden; background: #fff; box-shadow: 0 4px 20px rgba(0,0,0,0.02);">
      <div style="overflow-x: auto;">
        <table style="width: 100%; border-collapse: collapse; text-align: center; min-width: 800px;">
          <thead>
            <tr style="background: #fafafa; border-bottom: 1px solid #eaeaea;">
              <th style="text-align: left; padding: 1.5rem 2rem; width: 28%; font-size: 1.05rem; color: #1a1a1a;">Features</th>
              <th style="padding: 1.5rem 1rem; width: 18%;">Basic</th>
              <th style="padding: 1.5rem 1rem; width: 18%;">Silver</th>
              <th style="padding: 1.5rem 1rem; width: 18%;">Gold</th>
              <th style="padding: 1.5rem 1rem; width: 18%;">Premium</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1.2rem 2rem; border-right: 1px solid #eaeaea; font-weight: 500;">Monthly Price</td>
              <td style="font-weight: 600; color: var(--color-fire-engine-red);">$500</td>
              <td style="font-weight: 600; color: var(--color-fire-engine-red);">$700</td>
              <td style="font-weight: 600; color: var(--color-fire-engine-red);">$900</td>
              <td style="font-weight: 600; color: var(--color-fire-engine-red);">$1500</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1.2rem 2rem; border-right: 1px solid #eaeaea; font-weight: 500;">Keywords</td>
              <td>20</td>
              <td>40</td>
              <td>60</td>
              <td>100</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1.2rem 2rem; border-right: 1px solid #eaeaea; font-weight: 500;">Backlinks</td>
              <td>40</td>
              <td>60</td>
              <td>100</td>
              <td>200</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1.2rem 2rem; border-right: 1px solid #eaeaea; font-weight: 500;">Optimized Pages</td>
              <td>Up to 10</td>
              <td>Up to 15</td>
              <td>Up to 25</td>
              <td>Up to 40</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1.2rem 2rem; border-right: 1px solid #eaeaea; font-weight: 500;">GBP (GMB)</td>
              <td style="color: #ccc;">X</td>
              <td style="color: green; font-weight: bold;">✓</td>
              <td style="color: green; font-weight: bold;">✓</td>
              <td style="color: green; font-weight: bold;">✓</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1.2rem 2rem; border-right: 1px solid #eaeaea; font-weight: 500;">Geotagging</td>
              <td style="color: #ccc;">X</td>
              <td style="color: #ccc;">X</td>
              <td style="color: green; font-weight: bold;">✓</td>
              <td style="color: green; font-weight: bold;">✓</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1.2rem 2rem; border-right: 1px solid #eaeaea; font-weight: 500;">GEO (Generative Search)</td>
              <td style="color: #ccc;">X</td>
              <td style="color: #ccc;">X</td>
              <td style="color: #ccc;">X</td>
              <td style="color: green; font-weight: bold;">✓</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1.2rem 2rem; border-right: 1px solid #eaeaea; font-weight: 500;">AEO (Answer Engine)</td>
              <td style="color: #ccc;">X</td>
              <td style="color: #ccc;">X</td>
              <td style="color: #ccc;">X</td>
              <td style="color: green; font-weight: bold;">✓</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1.2rem 2rem; border-right: 1px solid #eaeaea; font-weight: 500;">AI Audit</td>
              <td>2 pages</td>
              <td>4 pages</td>
              <td>6 pages</td>
              <td>8 pages</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</section>

<section class="growth-engine" style="padding: 6rem 0; background: var(--color-warm-white);">
  <div class="container">
    <h2 style="text-align: center; margin-bottom: 3.5rem;">Service Breakdown Modules</h2>
    <div class="growth-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem;">
      <div class="growth-card">
        <div>
          <h3>1. Hands-On SEO Analysis</h3>
          <p>Website Review Before Optimization, Competitor Research, Keyword Research, Current Ranking Check, Duplicate Content Review, Google Penalty Check, and Backlink Review (as needed).</p>
        </div>
      </div>
      <div class="growth-card">
        <div>
          <h3>2. AI Visibility Activities</h3>
          <p>AI Entity Optimization, Schema Check & Fix, Answer Engine Optimization (AEO), Featured Snippet Testing (A/B), Monthly AI Index Tracking, AI Image & Infographic Optimization, Website Structure for AI Understanding, Conversational AI Optimization, Voice Search Optimization, Zero-Click Optimization, AI-Based Landing Pages, AI-Optimized Blog Posts, Competitor AI Analysis, and Monthly AI Ranking Reports.</p>
        </div>
      </div>
      <div class="growth-card">
        <div>
          <h3>3. On-Page Optimization</h3>
          <p>Canonical Tag Checks, Title & Meta Tags Optimization, Headings & Image Alt Tags Optimization, Content Optimization, SEO-Friendly URL Setup, Website Navigation Review, 404 Page Setup, Broken Links Checks, Google Index Checks, Robots.txt & XML Sitemaps, GTM Setup, and Structured Data Setup.</p>
        </div>
      </div>
      <div class="growth-card">
        <div>
          <h3>4. Off-Page Optimization</h3>
          <p>Search Engine Submissions, Blog Writing & Link Building, Article Writing & Submissions, Image Sharing, Contextual Link Building, Social Media Sharing, Web 2.0 Profiles, Micro Blogging, Classified Submissions, Infographic Creation & Sharing, Google Business Listing Setup, and Local NAP Consistency Syndication.</p>
        </div>
      </div>
      <div class="growth-card">
        <div>
          <h3>5. Reports & Support</h3>
          <p>Comprehensive monthly reporting covering keyword rankings, website traffic, analytics conversion tracking, and link submissions. Direct support via email, phone, and live chat options.</p>
        </div>
      </div>
    </div>
  </div>
</section>
""" + make_cta_banner("Select Your Plan &<br>Start Ranking Today.")

build_html_page(
    "pricing-seo.html",
    "SEO Packages",
    "Choose from GBO's Basic, Silver, Gold, or Premium SEO Packages to grow your search visibility and organic traffic.",
    "SEO Pricing Plans",
    "SEO Packages",
    "Invest in long-term organic growth with plans designed for maximum search engine ROI.",
    seo_pricing_html
)

# 8. pricing-smo-setup.html
smo_setup_html = f"""
<section class="pricing-hero" style="padding: 8rem 0 4rem; text-align: center;">
  <div class="container" style="max-width: 800px; text-align: center;">
    <span class="process-label" style="display: inline-block; margin-bottom: 1rem; color: var(--color-fire-engine-red); font-weight: 700; letter-spacing: 2px;">ONE TIME FEE</span>
    <h1>SMO Structural Set-Up</h1>
    <p style="font-size: 1.2rem; color: #666; margin-bottom: 3rem;">Lay a solid foundation for your brand across social media networks with GBO's setup configurations.</p>
    
    <div style="background: #fafafa; border: 1px solid #eaeaea; border-radius: 12px; padding: 3rem; text-align: center; max-width: 500px; margin: 0 auto; box-shadow: 0 10px 30px rgba(0,0,0,0.02);">
      <h3 style="font-size: 1.8rem; margin-bottom: 1rem; color: #1a1a1a;">Structural Setup Package</h3>
      <p style="color: #666; margin-bottom: 1.5rem;">Complete SMO & Paid Tracking Infrastructure</p>
      <div style="font-size: 3rem; font-weight: 700; color: var(--color-fire-engine-red); margin-bottom: 1.5rem;">
        $399<span style="font-size: 1rem; color: #666; font-weight: 500;"> One Time Setup Fee</span>
      </div>
      <p style="color: green; font-weight: 600; margin-bottom: 2rem;">✓ Save $101 (Regular price: $500)</p>
      <a href="contact.html?plan=smo-setup" class="btn btn-primary" style="display: block; width: 100%; text-align: center; line-height: 54px; height: 54px; padding: 0;">Get Started Now</a>
    </div>
  </div>
</section>

<section class="comparison-table-section" style="padding: 4rem 0 6rem; background: #fff;">
  <div class="container" style="max-width: 800px;">
    <div class="compare-heading-wrapper" style="text-align: center; margin-bottom: 3rem;">
      <h2 style="font-family: var(--font-heading); font-size: 2.2rem; font-weight: 600; color: #1a1a1a;">Setup Modules & Pricing Breakdown</h2>
    </div>
    <div class="compare-table-container" style="border: 1px solid #eaeaea; border-radius: 12px; overflow: hidden; background: #fff;">
      <table style="width: 100%; border-collapse: collapse; text-align: center;">
        <thead>
          <tr style="background: #fafafa; border-bottom: 1px solid #eaeaea;">
            <th style="text-align: left; padding: 1.5rem 2rem; font-size: 1.05rem; color: #1a1a1a; width: 70%;">Activity Category</th>
            <th style="padding: 1.5rem 2rem; font-size: 1.05rem; color: #1a1a1a; width: 30%;">Setup Cost</th>
          </tr>
        </thead>
        <tbody>
          <tr style="border-bottom: 1px solid #eaeaea;">
            <td style="text-align: left; padding: 1.2rem 2rem; border-right: 1px solid #eaeaea; font-weight: 500;">Organic Profiles Setup & Custom Creative Templates</td>
            <td style="font-weight: 600;">$250</td>
          </tr>
          <tr style="border-bottom: 1px solid #eaeaea;">
            <td style="text-align: left; padding: 1.2rem 2rem; border-right: 1px solid #eaeaea; font-weight: 500;">Paid Campaigns & Conversion Pixel Tracking Configurations</td>
            <td style="font-weight: 600;">$250</td>
          </tr>
          <tr style="border-bottom: 1px solid #eaeaea;">
            <td style="text-align: left; padding: 1.2rem 2rem; border-right: 1px solid #eaeaea; font-weight: 500;">Remarketing Setup (Audience Lists & Funnels)</td>
            <td style="font-weight: 600;">$150</td>
          </tr>
          <tr style="background: #fafafa; font-weight: bold; border-top: 2px solid #eaeaea;">
            <td style="text-align: left; padding: 1.5rem 2rem; border-right: 1px solid #eaeaea; font-size: 1.1rem; color: #1a1a1a;">Combined Package Cost (Special Offer)</td>
            <td style="font-size: 1.3rem; color: var(--color-fire-engine-red);">$399</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<section class="growth-engine" style="padding: 6rem 0; background: var(--color-warm-white);">
  <div class="container">
    <h2 style="text-align: center; margin-bottom: 3.5rem;">Setup Service Modules</h2>
    <div class="growth-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem;">
      <div class="growth-card">
        <div>
          <h3>1. Analysis & Strategy</h3>
          <p>Competitor SMO analysis, target audience selection, and customized organic posting strategy formation.</p>
        </div>
      </div>
      <div class="growth-card">
        <div>
          <h3>2. Organic Setup</h3>
          <p>Account creation & profile optimization, custom cover image design, bio writing, and 5 graphic design templates.</p>
        </div>
      </div>
      <div class="growth-card">
        <div>
          <h3>3. Tracking & Pixel Setup</h3>
          <p>Ad account verification, Facebook conversion pixel installation, standard event mapping (purchase, add to cart, checkout), and Google Analytics linking.</p>
        </div>
      </div>
      <div class="growth-card">
        <div>
          <h3>4. Remarketing Infrastructure</h3>
          <p>Setup custom and lookalike audiences, and configure retargeting funnels to re-engage previous site visitors.</p>
        </div>
      </div>
    </div>
  </div>
</section>
""" + make_cta_banner("Establish Your Brand<br>Social Foundation Today.")

build_html_page(
    "pricing-smo-setup.html",
    "SMO Structural Set-Up",
    "Establish your social media infrastructure with GBO's one-time SMO Structural Setup covering profiles, pixels, and tracking.",
    "One Time SMO Setup",
    "SMO Structural Set-Up",
    "Build a solid profile foundation and pixel tracking infrastructure across Facebook, Instagram, and LinkedIn.",
    smo_setup_html
)

# 9. pricing-smo-maintenance.html
smo_maint_html = f"""
<section class="pricing-hero" style="padding: 8rem 0 4rem; text-align: center;">
  <div class="container" style="text-align: center;">
    <span class="process-label" style="display: inline-block; margin-bottom: 1rem; color: var(--color-fire-engine-red); font-weight: 700; letter-spacing: 2px;">MONTHLY PLANS</span>
    <h1>SMO Maintenance Packages</h1>
    <p style="font-size: 1.2rem; color: #666; max-width: 600px; margin: 0 auto 3rem;">Ongoing organic social management and paid campaigns optimization to scale your brand footprint.</p>
    
    <div class="new-pricing-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; max-width: 1000px; margin: 0 auto;">
      <div class="new-pricing-card">
        <div class="new-pricing-header"><h3>Silver Package</h3><p>Standard profile maintenance</p></div>
        <div class="new-pricing-price"><span class="new-currency">$</span><span class="new-amount">350</span><span class="new-interval">/Monthly</span></div>
        <a href="contact.html?plan=smo-silver" class="new-pricing-btn" style="text-align: center; text-decoration: none; line-height: 54px;">Select Plan</a>
        <div class="new-pricing-features">
          <ul>
            <li><i>&#10003;</i> 5 Creative Graphics / month</li>
            <li><i>&#10003;</i> 5 Postings / month</li>
            <li><i>&#10003;</i> Organic Promotion & Hashtags</li>
            <li><i>&#10003;</i> Paid Campaigns - X</li>
            <li><i>&#10003;</i> Monthly Support & Reports</li>
          </ul>
        </div>
      </div>
      <div class="new-pricing-card highlighted">
        <div class="new-pricing-header"><h3>Gold Package</h3><p>Best Seller - Social Expansion</p></div>
        <div class="new-pricing-price"><span class="new-currency">$</span><span class="new-amount">550</span><span class="new-interval">/Monthly</span></div>
        <a href="contact.html?plan=smo-gold" class="new-pricing-btn featured-btn" style="text-align: center; text-decoration: none; line-height: 54px;">Select Plan</a>
        <div class="new-pricing-features featured-features">
          <ul>
            <li><i>&#10003;</i> 8 Creative Graphics / month</li>
            <li><i>&#10003;</i> 8 Postings / month</li>
            <li><i>&#10003;</i> Organic Promotion & Hashtags</li>
            <li><i>&#10003;</i> Paid Campaign Optimization - ✓</li>
            <li><i>&#10003;</i> Ad Creatives & Conversion Setup</li>
          </ul>
        </div>
      </div>
      <div class="new-pricing-card">
        <div class="new-pricing-header"><h3>Premium Package</h3><p>Enterprise Social Domination</p></div>
        <div class="new-pricing-price"><span class="new-currency">$</span><span class="new-amount">750</span><span class="new-interval">/Monthly</span></div>
        <a href="contact.html?plan=smo-premium" class="new-pricing-btn" style="text-align: center; text-decoration: none; line-height: 54px;">Select Plan</a>
        <div class="new-pricing-features">
          <ul>
            <li><i>&#10003;</i> 12 Creative Graphics / month</li>
            <li><i>&#10003;</i> 12 Postings / month</li>
            <li><i>&#10003;</i> Organic Promotion & Hashtags</li>
            <li><i>&#10003;</i> Paid Campaign Optimization - ✓</li>
            <li><i>&#10003;</i> Remarketing Campaigns - ✓</li>
            <li><i>&#10003;</i> Audience Lists & Target Mapping</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="comparison-table-section" style="padding: 4rem 0 6rem; background: #fff;">
  <div class="container">
    <div class="compare-heading-wrapper" style="text-align: center; margin-bottom: 3rem;">
      <h2 style="font-family: var(--font-heading); font-size: 2.2rem; font-weight: 600; color: #1a1a1a;">SMO Maintenance Comparison Table</h2>
    </div>
    <div class="compare-table-container" style="border: 1px solid #eaeaea; border-radius: 12px; overflow: hidden; background: #fff; box-shadow: 0 4px 20px rgba(0,0,0,0.02);">
      <div style="overflow-x: auto;">
        <table style="width: 100%; border-collapse: collapse; text-align: center; min-width: 800px;">
          <thead>
            <tr style="background: #fafafa; border-bottom: 1px solid #eaeaea;">
              <th style="text-align: left; padding: 1.5rem 2rem; width: 34%; font-size: 1.05rem; color: #1a1a1a;">Features & Activities</th>
              <th style="padding: 1.5rem 1rem; width: 22%;">Silver</th>
              <th style="padding: 1.5rem 1rem; width: 22%;">Gold</th>
              <th style="padding: 1.5rem 1rem; width: 22%;">Premium</th>
            </tr>
          </thead>
          <tbody>
            <tr style="background: #fdfdfd; font-weight: bold; border-bottom: 1px solid #eaeaea; text-align: left;">
              <td colspan="4" style="padding: 1rem 2rem; color: var(--color-fire-engine-red); letter-spacing: 1px;">ORGANIC PROMOTION</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea;">Competitor analysis & Strategy formation</td>
              <td style="color: green;">✓</td>
              <td style="color: green;">✓</td>
              <td style="color: green;">✓</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea;">Hashtag creation and promotion</td>
              <td style="color: green;">✓</td>
              <td style="color: green;">✓</td>
              <td style="color: green;">✓</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea;">Monthly creative graphic creation</td>
              <td>5</td>
              <td>8</td>
              <td>12</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea;">Monthly postings & Scheduling</td>
              <td>5</td>
              <td>8</td>
              <td>12</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea;">Engagement with active groups & third-party posts</td>
              <td style="color: green;">✓</td>
              <td style="color: green;">✓</td>
              <td style="color: green;">✓</td>
            </tr>
            <tr style="background: #fdfdfd; font-weight: bold; border-bottom: 1px solid #eaeaea; text-align: left;">
              <td colspan="4" style="padding: 1rem 2rem; color: var(--color-fire-engine-red); letter-spacing: 1px;">PAID PROMOTION</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea;">Setting up campaigns & Budget estimate</td>
              <td style="color: #ccc;">✗</td>
              <td style="color: green;">✓</td>
              <td style="color: green;">✓</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea;">Ad creative creation & Sales funnel configuration</td>
              <td style="color: #ccc;">✗</td>
              <td style="color: green;">✓</td>
              <td style="color: green;">✓</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea;">Daily account optimization & Tracking</td>
              <td style="color: #ccc;">✗</td>
              <td style="color: green;">✓</td>
              <td style="color: green;">✓</td>
            </tr>
            <tr style="background: #fdfdfd; font-weight: bold; border-bottom: 1px solid #eaeaea; text-align: left;">
              <td colspan="4" style="padding: 1rem 2rem; color: var(--color-fire-engine-red); letter-spacing: 1px;">REMARKETING</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea;">Remarketing Campaign Setup & Ad Creatives</td>
              <td style="color: #ccc;">✗</td>
              <td style="color: #ccc;">✗</td>
              <td style="color: green;">✓</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea;">Creation of custom & lookalike lists</td>
              <td style="color: #ccc;">✗</td>
              <td style="color: #ccc;">✗</td>
              <td style="color: green;">✓</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</section>
""" + make_cta_banner("Scale Your Social Reach.<br>Subscribe to a Plan.")

build_html_page(
    "pricing-smo-maintenance.html",
    "SMO Maintenance Packages",
    "Grow your social presence with GBO's SMO Maintenance Packages: Silver, Gold, and Premium monthly management.",
    "SMO Pricing Plans",
    "SMO Maintenance Packages",
    "Ongoing optimization and campaigns to keep your social channels active and growing.",
    smo_maint_html
)

# 10. pricing-ecommerce-ppc.html
ecom_pricing_html = f"""
<section class="pricing-hero" style="padding: 8rem 0 4rem; text-align: center;">
  <div class="container" style="text-align: center;">
    <span class="process-label" style="display: inline-block; margin-bottom: 1rem; color: var(--color-fire-engine-red); font-weight: 700; letter-spacing: 2px;">E-COMMERCE PLANS</span>
    <h1>E-Commerce PPC Plans</h1>
    <p style="font-size: 1.2rem; color: #666; max-width: 600px; margin: 0 auto 3rem;">Drive immediate checkout sales with GBO's targeted Shopping, Sponsored, and Display ad plans.</p>
    
    <div class="new-pricing-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.5rem;">
      <div class="new-pricing-card">
        <div class="new-pricing-header"><h3>Plan 1</h3><p>Budget up to $1,000</p></div>
        <div class="new-pricing-price"><span class="new-currency">$</span><span class="new-amount">350</span><span class="new-interval">/Monthly</span></div>
        <a href="contact.html?plan=ecom-plan1" class="new-pricing-btn" style="text-align: center; text-decoration: none; line-height: 54px;">Select Plan</a>
        <div class="new-pricing-features">
          <ul>
            <li><i>&#10003;</i> Setup Fee: Nil</li>
            <li><i>&#10003;</i> 1 Campaign</li>
            <li><i>&#10003;</i> Up to 30 Keywords</li>
            <li><i>&#10003;</i> Sponsored Products - Yes</li>
            <li><i>&#10003;</i> Sponsored Brands - No</li>
          </ul>
        </div>
      </div>
      <div class="new-pricing-card">
        <div class="new-pricing-header"><h3>Plan 2</h3><p>Budget up to $2,000</p></div>
        <div class="new-pricing-price"><span class="new-currency">$</span><span class="new-amount">550</span><span class="new-interval">/Monthly</span></div>
        <a href="contact.html?plan=ecom-plan2" class="new-pricing-btn" style="text-align: center; text-decoration: none; line-height: 54px;">Select Plan</a>
        <div class="new-pricing-features">
          <ul>
            <li><i>&#10003;</i> Setup Fee: Nil</li>
            <li><i>&#10003;</i> Up to 2 Campaigns</li>
            <li><i>&#10003;</i> Up to 50 Keywords</li>
            <li><i>&#10003;</i> Sponsored Products - Yes</li>
            <li><i>&#10003;</i> Sponsored Brands - Yes</li>
          </ul>
        </div>
      </div>
      <div class="new-pricing-card highlighted">
        <div class="new-pricing-header"><h3>Plan 3</h3><p>Budget up to $3,000</p></div>
        <div class="new-pricing-price"><span class="new-currency">$</span><span class="new-amount">750</span><span class="new-interval">/Monthly</span></div>
        <a href="contact.html?plan=ecom-plan3" class="new-pricing-btn featured-btn" style="text-align: center; text-decoration: none; line-height: 54px;">Select Plan</a>
        <div class="new-pricing-features featured-features">
          <ul>
            <li><i>&#10003;</i> Setup Fee: $350</li>
            <li><i>&#10003;</i> Up to 5 Campaigns</li>
            <li><i>&#10003;</i> Up to 100 Keywords</li>
            <li><i>&#10003;</i> Sponsored Brands/Display - Yes</li>
            <li><i>&#10003;</i> Product Listings: Up to 30</li>
          </ul>
        </div>
      </div>
      <div class="new-pricing-card">
        <div class="new-pricing-header"><h3>Plan 4</h3><p>Budget $3,000+</p></div>
        <div class="new-pricing-price"><span class="new-currency">$</span><span class="new-amount">1200</span><span class="new-interval">/Monthly</span></div>
        <a href="contact.html?plan=ecom-plan4" class="new-pricing-btn" style="text-align: center; text-decoration: none; line-height: 54px;">Select Plan</a>
        <div class="new-pricing-features">
          <ul>
            <li><i>&#10003;</i> Setup Fee: $350</li>
            <li><i>&#10003;</i> Up to 10 Campaigns</li>
            <li><i>&#10003;</i> Up to 200 Keywords</li>
            <li><i>&#10003;</i> Sponsored Brands/Display - Yes</li>
            <li><i>&#10003;</i> Product Listings: Up to 50</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="comparison-table-section" style="padding: 4rem 0 6rem; background: #fff;">
  <div class="container">
    <div class="compare-heading-wrapper" style="text-align: center; margin-bottom: 3rem;">
      <h2 style="font-family: var(--font-heading); font-size: 2.2rem; font-weight: 600; color: #1a1a1a;">E-Commerce PPC Comparison Table</h2>
    </div>
    <div class="compare-table-container" style="border: 1px solid #eaeaea; border-radius: 12px; overflow: hidden; background: #fff; box-shadow: 0 4px 20px rgba(0,0,0,0.02);">
      <div style="overflow-x: auto;">
        <table style="width: 100%; border-collapse: collapse; text-align: center; min-width: 800px;">
          <thead>
            <tr style="background: #fafafa; border-bottom: 1px solid #eaeaea;">
              <th style="text-align: left; padding: 1.5rem 2rem; width: 28%; font-size: 1.05rem; color: #1a1a1a;">Feature / Activity</th>
              <th style="padding: 1.5rem 1rem;">Plan 1</th>
              <th style="padding: 1.5rem 1rem;">Plan 2</th>
              <th style="padding: 1.5rem 1rem;">Plan 3</th>
              <th style="padding: 1.5rem 1rem;">Plan 4</th>
            </tr>
          </thead>
          <tbody>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea; font-weight: 500;">Monthly Budget Limit</td>
              <td>Up to $1000</td>
              <td>Up to $2000</td>
              <td>Up to $3000</td>
              <td>$3000+</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea; font-weight: 500;">Setup Fee (One Time)</td>
              <td>Nil</td>
              <td>Nil</td>
              <td>$350</td>
              <td>$350</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea; font-weight: 500;">Number of Campaigns</td>
              <td>1</td>
              <td>Up to 2</td>
              <td>Up to 5</td>
              <td>Up to 10</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea; font-weight: 500;">Keyword Research</td>
              <td>Up to 30</td>
              <td>Up to 50</td>
              <td>Up to 100</td>
              <td>Up to 200</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea; font-weight: 500;">Sponsored Products</td>
              <td style="color: green; font-weight: bold;">✓</td>
              <td style="color: green; font-weight: bold;">✓</td>
              <td style="color: green; font-weight: bold;">✓</td>
              <td style="color: green; font-weight: bold;">✓</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea; font-weight: 500;">Sponsored Brands</td>
              <td style="color: #ccc;">X</td>
              <td style="color: green; font-weight: bold;">✓</td>
              <td style="color: green; font-weight: bold;">✓</td>
              <td style="color: green; font-weight: bold;">✓</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea; font-weight: 500;">Sponsored Display</td>
              <td style="color: #ccc;">X</td>
              <td style="color: #ccc;">X</td>
              <td>Up to 5</td>
              <td>Up to 10</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea; font-weight: 500;">Product Listings</td>
              <td>Up to 10</td>
              <td>Up to 20</td>
              <td>Up to 30</td>
              <td>Up to 50</td>
            </tr>
            <tr style="background: #fafafa; font-weight: bold; border-top: 1px solid #eaeaea; text-align: left;">
              <td colspan="5" style="padding: 1rem 2rem; color: var(--color-fire-engine-red); letter-spacing: 1px;">CAMPAIGN MANAGEMENT ACTIVITIES</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea;">Competitor Analysis</td>
              <td style="color: #ccc;">✗</td>
              <td style="color: #ccc;">✗</td>
              <td style="color: green; font-weight: bold;">✓</td>
              <td style="color: green; font-weight: bold;">✓</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea;">CTR Optimization & ACoS Reduction</td>
              <td style="color: green; font-weight: bold;">✓</td>
              <td style="color: green; font-weight: bold;">✓</td>
              <td style="color: green; font-weight: bold;">✓</td>
              <td style="color: green; font-weight: bold;">✓</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea;">Filter Negative Search Terms</td>
              <td style="color: #ccc;">✗</td>
              <td style="color: #ccc;">✗</td>
              <td style="color: green; font-weight: bold;">✓</td>
              <td style="color: green; font-weight: bold;">✓</td>
            </tr>
            <tr style="border-bottom: 1px solid #eaeaea;">
              <td style="text-align: left; padding: 1rem 2rem; border-right: 1px solid #eaeaea;">Weekly Bid & Budget Check</td>
              <td style="color: green; font-weight: bold;">✓</td>
              <td style="color: green; font-weight: bold;">✓</td>
              <td style="color: green; font-weight: bold;">✓</td>
              <td style="color: green; font-weight: bold;">✓</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</section>
""" + make_cta_banner("Scale Your E-Commerce ROI.<br>Choose an Ad Plan.")

build_html_page(
    "pricing-ecommerce-ppc.html",
    "E-Commerce PPC Plans",
    "Drive sales and scale purchase volume with GBO's dedicated E-Commerce PPC advertising plans.",
    "E-Commerce PPC Pricing",
    "E-Commerce PPC Plans",
    "Drive instant product sales with highly targeted shopping, brand, and search ads.",
    ecom_pricing_html
)

# 11. pricing-ppc.html
ppc_pricing_html = f"""
<section class="pricing-hero" style="padding: 8rem 0 4rem; text-align: center;">
  <div class="container" style="text-align: center;">
    <span class="process-label" style="display: inline-block; margin-bottom: 1rem; color: var(--color-fire-engine-red); font-weight: 700; letter-spacing: 2px;">PPC PACKAGES</span>
    <h1>PPC Packages. <span class="highlight-red">Maximize Ad Spend.</span></h1>
    <p style="font-size: 1.2rem; color: #666; max-width: 600px; margin: 0 auto 3rem;">Certified Google Ads & PPC campaign management packages configured for conversion growth.</p>
    
    <div class="new-pricing-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 1.5rem;">
      <div class="new-pricing-card">
        <div class="new-pricing-header"><h3>Basic PPC</h3><p>Budget up to $1,000/mo</p></div>
        <div class="new-pricing-price"><span class="new-currency">$</span><span class="new-amount">250</span><span class="new-interval">/Monthly</span></div>
        <a href="contact.html?plan=ppc-basic" class="new-pricing-btn" style="text-align: center; text-decoration: none; line-height: 54px;">Select Plan</a>
        <div class="new-pricing-features">
          <ul>
            <li><i>&#10003;</i> Setup Fee: Nil</li>
            <li><i>&#10003;</i> Up to 2 Campaigns</li>
            <li><i>&#10003;</i> Up to 50 Keywords</li>
            <li><i>&#10003;</i> Ad Groups: 2</li>
            <li><i>&#10003;</i> Conversion Tracking: Basic</li>
          </ul>
        </div>
      </div>
      <div class="new-pricing-card">
        <div class="new-pricing-header"><h3>Standard PPC</h3><p>Budget up to $2,500/mo</p></div>
        <div class="new-pricing-price"><span class="new-currency">$</span><span class="new-amount">450</span><span class="new-interval">/Monthly</span></div>
        <a href="contact.html?plan=ppc-standard" class="new-pricing-btn" style="text-align: center; text-decoration: none; line-height: 54px;">Select Plan</a>
        <div class="new-pricing-features">
          <ul>
            <li><i>&#10003;</i> Setup Fee: Nil</li>
            <li><i>&#10003;</i> Up to 4 Campaigns</li>
            <li><i>&#10003;</i> Up to 100 Keywords</li>
            <li><i>&#10003;</i> Ad Groups: 4</li>
            <li><i>&#10003;</i> Remarketing Setup: ✓</li>
          </ul>
        </div>
      </div>
      <div class="new-pricing-card highlighted">
        <div class="new-pricing-header"><h3>Professional PPC</h3><p>Budget up to $5,000/mo</p></div>
        <div class="new-pricing-price"><span class="new-currency">$</span><span class="new-amount">650</span><span class="new-interval">/Monthly</span></div>
        <a href="contact.html?plan=ppc-pro" class="new-pricing-btn featured-btn" style="text-align: center; text-decoration: none; line-height: 54px;">Select Plan</a>
        <div class="new-pricing-features featured-features">
          <ul>
            <li><i>&#10003;</i> Setup Fee: Nil</li>
            <li><i>&#10003;</i> Up to 8 Campaigns</li>
            <li><i>&#10003;</i> Up to 200 Keywords</li>
            <li><i>&#10003;</i> Ad Groups: 8</li>
            <li><i>&#10003;</i> GTM & Conversion Funnel: ✓</li>
          </ul>
        </div>
      </div>
      <div class="new-pricing-card">
        <div class="new-pricing-header"><h3>Enterprise PPC</h3><p>Budget $5,000+/mo</p></div>
        <div class="new-pricing-price"><span class="new-currency">$</span><span class="new-amount">950</span><span class="new-interval">/Monthly</span></div>
        <a href="contact.html?plan=ppc-enterprise" class="new-pricing-btn" style="text-align: center; text-decoration: none; line-height: 54px;">Select Plan</a>
        <div class="new-pricing-features">
          <ul>
            <li><i>&#10003;</i> Setup Fee: Nil</li>
            <li><i>&#10003;</i> Campaigns: Unlimited</li>
            <li><i>&#10003;</i> Keywords: Unlimited</li>
            <li><i>&#10003;</i> Ad Groups: Unlimited</li>
            <li><i>&#10003;</i> Landing Page Audit & A/B: ✓</li>
          </ul>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="growth-engine" style="padding: 6rem 0; background: var(--color-warm-white);">
  <div class="container">
    <h2 style="text-align: center; margin-bottom: 3.5rem;">PPC Management Activities</h2>
    <div class="growth-grid" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 2rem;">
      <div class="growth-card">
        <div>
          <h3>1. Setup Activities</h3>
          <p>Ad Account Setup, Competitor Analysis, Keyword Research & Mapping, Campaign Structuring, Ad Copywriting, Ad Extension Configuration, and Conversion Tracking Code (Google Analytics & GTM) installation.</p>
        </div>
      </div>
      <div class="growth-card">
        <div>
          <h3>2. Optimization & Monitoring</h3>
          <p>Bid Adjustments, Keyword Bid Management, Search Term Report Audits, Negative Keyword Exclusions, Ad Copy Testing (A/B), and Landing Page UX Review.</p>
        </div>
      </div>
      <div class="growth-card">
        <div>
          <h3>3. Remarketing campaigns</h3>
          <p>Configure custom remarketing lists and run targeted banner/display ad campaigns to re-engage prospective buyers.</p>
        </div>
      </div>
      <div class="growth-card">
        <div>
          <h3>4. Support & Reports</h3>
          <p>Monthly campaign reports showing Impressions, Click-Through-Rate (CTR), Cost-Per-Click (CPC), Conversions, and Acquisition Costs. Email and phone consulting support.</p>
        </div>
      </div>
    </div>
  </div>
</section>
""" + make_cta_banner("Scale Your Lead Flow.<br>Select a PPC Package.")

build_html_page(
    "pricing-ppc.html",
    "PPC Packages",
    "Maximize your return on ad spend with GBO's Professional Google Ads and PPC management packages.",
    "PPC Pricing Packages",
    "PPC Packages",
    "Partner with certified Google Ads experts to maximize your advertising return on investment.",
    ppc_pricing_html
)

# =========================================================================
# UTILITY / CORPORATE PAGES
# =========================================================================

# 12. portfolio.html
portfolio_content = make_stats_bar([
    {"val": "500+", "label": "Projects Delivered"},
    {"val": "40+", "label": "Industries Served"},
    {"val": "98%", "label": "Client Satisfaction"},
    {"val": "3+", "label": "Years Experience"}
]) + make_growth_engine(
    "Proven Growth Case Studies",
    [
        {"title": "E-Commerce Revenue Growth", "desc": "Boosted organic search traffic by 250% and direct checkout sales by 180% for a fashion retailer in 6 months."},
        {"title": "SaaS Lead Generation", "desc": "Optimized search intent mapping to scale monthly organic demo signups by 320% for an enterprise CRM platform."},
        {"title": "Local Business Domination", "desc": "Positioned a local home service provider in the Google Maps Local 3-Pack across 15 target zip codes, driving a 400% call volume increase."},
        {"title": "Enterprise SEO Scaling", "desc": "Cleaned up technical site structure, schema markup, and internal link routing to boost page indexing for a 100k+ page directories site."},
        {"title": "Content Marketing ROI", "desc": "Created a topical authority map and high-quality SEO content hub that scaled monthly blog traffic from zero to 50k visitors."},
        {"title": "PPC Campaign Optimization", "desc": "Restructured Google Ads ad groups and refined negative keywords to reduce cost-per-acquisition (CPA) by 42% while doubling lead volume."}
    ]
) + make_split_screen(
    "Our Custom Application Case Studies",
    " Sarah Brayton, Owner of RI Elite Skating Academy, highlighted GBO's thoroughness and transparency during the creation of their custom sports training app. She was particularly impressed by the accessibility of the team and their continued responsiveness for technical fixes long after the official launch.",
    "We build not only search marketing plans but also structural lead capture assets, customized scripts, and integrations to ensure your operations scale alongside traffic growth.",
    ["Confidentiality and technical compliance", "Response readiness and emergency support hooks", "Seamless CRM and email marketing integrations"],
    dark_bg=True
) + make_cta_banner("Let Us Scale Your Brand.<br>Schedule a Case Review.")

build_html_page(
    "portfolio.html",
    "Our Work & Portfolio",
    "Explore how GBO has scaled organic traffic and generated revenue for SaaS, E-Commerce, and local service brands.",
    "Case Studies",
    "Our Work & Portfolio",
    "Proven results and digital marketing case studies showing how we help businesses Grow Business Online.",
    portfolio_content
)

# 13. about.html
about_content = make_split_screen(
    "Who We Are",
    "GBO (Grow Business Online) is a premier digital marketing agency built on the foundation of performance, transparency, and data-driven marketing. Our team of certified SEO experts, PPC specialists, content strategists, and creative designers work together to build sustainable, high-converting organic pipeline growth.",
    "Search is changing very fast. With AI tools like ChatGPT, Gemini, and Perplexity, traditional keyword stuffing is not enough. We merge tech engineering with copywriting to keep your brand visible and recommended across all search networks.",
    ["Experienced team of SEO, SMO & PPC strategists", "Topical authority and NLP semantic specialists", "Data-driven and conversion-focused campaign methodologies"]
) + make_stats_bar([
    {"val": "1000+", "label": "Satisfied Clients"},
    {"val": "20+", "label": "Industries Served"},
    {"val": "10+", "label": "Years Experience"},
    {"val": "95%", "label": "Client Retention"}
]) + make_growth_engine(
    "Our Core Values",
    [
        {"title": "Results-First", "desc": "We prioritize marketing activities that deliver actual business revenue, leads, and search ROI."},
        {"title": "Complete Transparency", "desc": "We provide clear, honest performance reports without vanity metrics, hidden fees, or jargon."},
        {"title": "Data-Driven Insights", "desc": "We optimize campaigns based on real-time search intent data and behavior analytics."},
        {"title": "Continuous Innovation", "desc": "We stay ahead of changing search algorithms and generative AI search (GEO/AEO) trends."},
        {"title": "Client Partnership", "desc": "We act as a direct extension of your team, aligned with your business goals and operational capabilities."},
        {"title": "Operational Excellence", "desc": "We maintain high standards of code hygiene, design aesthetics, and responsive customer support."}
    ]
) + make_process_section(
    "How We Work",
    [
        {"title": "Discover", "desc": "We audit your digital presence, index state, and analyze competitor visibility gaps."},
        {"title": "Strategize", "desc": "We build a tailored roadmap across organic search, social media, and paid ads."},
        {"title": "Execute", "desc": "We launch optimized search campaigns, write copy, and configure tracking pixels."},
        {"title": "Optimize", "desc": "We track conversions, run A/B tests, and refine user experience pathways."},
        {"title": "Scale", "desc": "We scale what works to maximize your digital footprint and business revenue."}
    ]
) + make_cta_banner("Let GBO Build Your<br>Digital Success Story.")

build_html_page(
    "about.html",
    "About Us",
    "Learn about GBO's story, core values, and our expert digital growth and SEO team.",
    "Our Story",
    "About GBO",
    "We combine elite engineering with creative marketing to deliver unmatched search engine visibility and revenue growth.",
    about_content
)

# 14. blog.html
blog_content = f"""
<section class="insights" id="insights" style="padding: 6rem 0; background: #111; color: white;">
  <div class="container">
    <div style="text-align: center; margin-bottom: 3.5rem;">
      <span class="process-label" style="color: var(--color-fire-engine-red);">MARKETING INSIGHTS</span>
      <h2 style="margin-top: 1rem; color: white;">Latest Digital Growth Articles</h2>
    </div>
    
    <div class="insights-grid" id="insights-grid-container" style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 2rem;">
      <div class="insight-card" style="background: #1a1a1a; border: 1px solid #222; border-radius: 12px; overflow: hidden; display: flex; flex-direction: column;">
        <div class="insight-img" style="background: linear-gradient(135deg, var(--color-fire-engine-red), var(--color-maroon)); height: 200px;"></div>
        <div class="insight-body" style="padding: 1.5rem; display: flex; flex-direction: column; justify-content: space-between; flex-grow: 1;">
          <div>
            <span class="insight-meta" style="color: var(--color-fire-engine-red); font-size: 0.8rem; font-weight: 700; text-transform: uppercase;">SEO & AI</span>
            <h4 class="insight-title" style="font-size: 1.25rem; font-weight: 600; margin: 0.5rem 0 1rem; color: white;">How AI is Transforming SEO in 2026</h4>
            <p class="insight-desc" style="color: #999; font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;">A comprehensive guide to optimizing your brand visibility for ChatGPT Search, Google Gemini, and Perplexity recommendations.</p>
          </div>
          <div class="insight-author" style="display: flex; align-items: center; gap: 1rem; border-top: 1px solid #222; padding-top: 1rem;">
            <div class="author-avatar" style="background-color: var(--color-fire-engine-red); width: 40px; height: 40px; border-radius: 50%;"></div>
            <div>
              <div class="author-name" style="font-weight: 600; font-size: 0.9rem; color: white;">Sarah Jenkins</div>
              <div class="insight-date" style="color: #666; font-size: 0.8rem;">May 19, 2026 · 4 min read</div>
            </div>
          </div>
        </div>
      </div>
      <div class="insight-card" style="background: #1a1a1a; border: 1px solid #222; border-radius: 12px; overflow: hidden; display: flex; flex-direction: column;">
        <div class="insight-img" style="background: linear-gradient(135deg, #FF4B2B, #FF416C); height: 200px;"></div>
        <div class="insight-body" style="padding: 1.5rem; display: flex; flex-direction: column; justify-content: space-between; flex-grow: 1;">
          <div>
            <span class="insight-meta" style="color: var(--color-fire-engine-red); font-size: 0.8rem; font-weight: 700; text-transform: uppercase;">LOCAL SEARCH</span>
            <h4 class="insight-title" style="font-size: 1.25rem; font-weight: 600; margin: 0.5rem 0 1rem; color: white;">The Complete Guide to Local SEO & Google Maps</h4>
            <p class="insight-desc" style="color: #999; font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;">Learn the exact steps to rank in the Local 3-Pack, manage customer reviews, and build directory citations that search engines trust.</p>
          </div>
          <div class="insight-author" style="display: flex; align-items: center; gap: 1rem; border-top: 1px solid #222; padding-top: 1rem;">
            <div class="author-avatar" style="background-color: #FF4B2B; width: 40px; height: 40px; border-radius: 50%;"></div>
            <div>
              <div class="author-name" style="font-weight: 600; font-size: 0.9rem; color: white;">David Chen</div>
              <div class="insight-date" style="color: #666; font-size: 0.8rem;">May 22, 2026 · 6 min read</div>
            </div>
          </div>
        </div>
      </div>
      <div class="insight-card" style="background: #1a1a1a; border: 1px solid #222; border-radius: 12px; overflow: hidden; display: flex; flex-direction: column;">
        <div class="insight-img" style="background: linear-gradient(135deg, #1f4068, #162447); height: 200px;"></div>
        <div class="insight-body" style="padding: 1.5rem; display: flex; flex-direction: column; justify-content: space-between; flex-grow: 1;">
          <div>
            <span class="insight-meta" style="color: var(--color-fire-engine-red); font-size: 0.8rem; font-weight: 700; text-transform: uppercase;">PPC STRATEGY</span>
            <h4 class="insight-title" style="font-size: 1.25rem; font-weight: 600; margin: 0.5rem 0 1rem; color: white;">SEO vs PPC: Which Strategy Wins?</h4>
            <p class="insight-desc" style="color: #999; font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;">We break down the costs, traffic speeds, conversion rates, and ROI parameters of paid PPC advertising versus organic search optimization.</p>
          </div>
          <div class="insight-author" style="display: flex; align-items: center; gap: 1rem; border-top: 1px solid #222; padding-top: 1rem;">
            <div class="author-avatar" style="background-color: #1f4068; width: 40px; height: 40px; border-radius: 50%;"></div>
            <div>
              <div class="author-name" style="font-weight: 600; font-size: 0.9rem; color: white;">Elena Rodriguez</div>
              <div class="insight-date" style="color: #666; font-size: 0.8rem;">June 01, 2026 · 5 min read</div>
            </div>
          </div>
        </div>
      </div>
      <div class="insight-card" style="background: #1a1a1a; border: 1px solid #222; border-radius: 12px; overflow: hidden; display: flex; flex-direction: column;">
        <div class="insight-img" style="background: linear-gradient(135deg, #111, #444); height: 200px;"></div>
        <div class="insight-body" style="padding: 1.5rem; display: flex; flex-direction: column; justify-content: space-between; flex-grow: 1;">
          <div>
            <span class="insight-meta" style="color: var(--color-fire-engine-red); font-size: 0.8rem; font-weight: 700; text-transform: uppercase;">CONTENT</span>
            <h4 class="insight-title" style="font-size: 1.25rem; font-weight: 600; margin: 0.5rem 0 1rem; color: white;">Creating Content That Converts</h4>
            <p class="insight-desc" style="color: #999; font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.5rem;">Avoid vanity traffic metrics. Learn how to write SEO blog posts and landing pages targeted at high-intent transactional search queries.</p>
          </div>
          <div class="insight-author" style="display: flex; align-items: center; gap: 1rem; border-top: 1px solid #222; padding-top: 1rem;">
            <div class="author-avatar" style="background-color: #444; width: 40px; height: 40px; border-radius: 50%;"></div>
            <div>
              <div class="author-name" style="font-weight: 600; font-size: 0.9rem; color: white;">Marcus Thorne</div>
              <div class="insight-date" style="color: #666; font-size: 0.8rem;">June 04, 2026 · 7 min read</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
""" + make_cta_banner("Learn Growth Strategies.<br>Join Our Newsletter.")

build_html_page(
    "blog.html",
    "Resources & Blog",
    "Read GBO's latest digital marketing insights, search engine algorithm guides, and organic scaling tactics.",
    "Insights",
    "Resources & Blog",
    "The latest strategies, search algorithm updates, and digital marketing insights from our growth engineers.",
    blog_content
)

# 15. contact.html
contact_content = make_stats_bar([
    {"val": " Sheridan, WY", "label": "30 N. Gould St, Suite 6573"},
    {"val": "Support Line", "label": "+1-307-209-3608"},
    {"val": "Email Address", "label": "info@growbusinessonline.com"},
    {"val": "Hours", "label": "Mon-Fri 9AM-6PM EST"}
]) + make_cta_banner("Send Us A Message Now.")

build_html_page(
    "contact.html",
    "Contact Us",
    "Get in touch with GBO's digital marketing specialists to request an audit or discuss pricing packages.",
    "Get In Touch",
    "Contact Our Team",
    "Ready to dominate search engine results, optimize advertising spend, and lead your market? Contact us today.",
    contact_content
)

# 16. free-consultation.html
consultation_content = make_split_screen(
    "What Your Consultation Includes",
    "Our senior growth strategists will perform a manual review of your website performance, SEO structure, competitor visibility gaps, and ad campaign efficiency. You will receive a clear, actionable roadmap with zero obligations.",
    "Get a comprehensive analysis of your digital footprint, completely free. Our experts will identify opportunities to boost your traffic, rankings, and revenue.",
    ["Deep technical SEO index error review", "Keyword rankings & search visibility analysis", "Competitor backlink and content gap mapping", "Page load speed & mobile responsive checks", "Paid ad campaign spend waste discovery"],
    dark_bg=True
) + make_cta_banner("Schedule Your Consultation.")

build_html_page(
    "free-consultation.html",
    "Free Consultation",
    "Request a free comprehensive digital marketing and SEO consultation from GBO's senior growth engineers.",
    "Free Audit",
    "Get Your Free Consultation",
    "Get a comprehensive analysis of your digital footprint, completely free. Our experts will identify opportunities to boost your traffic, rankings, and revenue.",
    consultation_content
)

# 17. privacy-terms.html
privacy_content = make_split_screen(
    "Privacy Policy & Terms",
    "At GBO (growbusinessonline.com), we prioritize the security and confidentiality of our clients' and visitors' data. We collect minimal analytics cookies to improve our services and never sell your personal information. Our terms of service govern your use of our website, consulting reports, and marketing deliverables.",
    "By submitting an audit request, you agree to receive communications from our strategy team regarding your report.",
    ["GDPR & CCPA compliant data handling", "Secure SSL-encrypted request forms", "Opt-out links in all marketing emails", "Clear intellectual property guidelines for deliverables", "Transparent cancellation and refund policies for packages"],
    dark_bg=False
) + make_cta_banner("Read GBO Operations Compliance.")

build_html_page(
    "privacy-terms.html",
    "Privacy & Terms",
    "Read GBO's privacy policy commitments, CCPA/GDPR compliance statements, and terms of service guidelines.",
    "Legal",
    "Privacy Policy & Terms",
    "Read GBO's commitment to data security, privacy compliance, and operational terms of service.",
    privacy_content
)

print("ALL 17 PAGES SUCCESSFULLY COMPILED!")
