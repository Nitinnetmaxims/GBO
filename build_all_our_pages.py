import os
import re

out_dir = r'c:\Users\admin\Downloads\NITIN-GBO-Antigravity\GBO Antigravity_2\GBO Antigravity_2'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

# ==========================================
# SERVICE PAGES GENERATOR
# ==========================================
styles = """
<style>
  :root {
    --dark-charcoal: #222222;
    --dark-gray: #333333;
    --bright-red: #D91C24;
    --off-white: #F5F5F5;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: system-ui, -apple-system, sans-serif; color: #fff; background-color: var(--dark-charcoal); line-height: 1.6; }
  a { text-decoration: none; color: inherit; }
  .container { max-width: 1200px; margin: 0 auto; padding: 0 2rem; }
  section { padding: 80px 0; }
  .btn-primary { background-color: var(--bright-red); color: white; padding: 0.85rem 2rem; border-radius: 50px; font-weight: bold; display: inline-block; transition: background-color 0.2s; border: none; cursor: pointer; }
  .btn-primary:hover { background-color: #b5151e; }
  .btn-outline { background-color: transparent; color: white; padding: 0.85rem 2rem; border-radius: 50px; font-weight: bold; border: 2px solid white; display: inline-block; transition: background-color 0.2s; cursor: pointer; }
  .btn-outline:hover { background-color: rgba(255,255,255,0.1); }
  .section-title { font-size: 2.5rem; font-weight: bold; margin-bottom: 3rem; text-align: center; line-height: 1.2; }
  
  /* Layout components */
  .grid-3 { display: grid; grid-template-columns: repeat(3, 1fr); gap: 32px; }
  .grid-4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 32px; }
  .grid-2 { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; }
  .grid-custom-7 { display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 32px; }
  .grid-custom-5 { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 32px; }

  .card-dark { background-color: var(--dark-gray); padding: 32px; border-radius: 8px; border: 1px solid #444; color: white; }
  .card-light { background-color: white; padding: 32px; border-radius: 8px; border: 1px solid #e0e0e0; color: var(--dark-charcoal); }
  .card-red { background-color: var(--bright-red); padding: 32px; border-radius: 8px; color: white; border: none; }
  
  .card-num { display: inline-flex; align-items: center; justify-content: center; width: 36px; height: 36px; background: var(--bright-red); color: white; border-radius: 50%; font-size: 1.1rem; font-weight: bold; margin-bottom: 1.5rem; }
  .card-red .card-num { background: white; color: var(--bright-red); }

  .process-timeline { display: flex; flex-direction: column; gap: 2rem; max-width: 900px; margin: 0 auto; }
  .process-card { display: flex; gap: 2rem; padding: 32px; border-radius: 8px; }
  .process-card.dark { background-color: var(--dark-gray); border: 1px solid #444; color: white; }
  .process-card.red { background-color: var(--bright-red); color: white; }
  .process-num { width: 50px; height: 50px; border-radius: 50%; background-color: var(--bright-red); color: white; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; font-weight: bold; flex-shrink: 0; }
  .process-card.red .process-num { background-color: white; color: var(--bright-red); }
  
  .faq-item { background: white; border: 1px solid #ddd; border-radius: 8px; margin-bottom: 1rem; color: var(--dark-charcoal); overflow: hidden; }
  .faq-q { padding: 1.5rem; font-weight: bold; font-size: 1.1rem; display: flex; justify-content: space-between; align-items: center; cursor: pointer; user-select: none; }
  .faq-num { display: inline-flex; align-items: center; justify-content: center; width: 28px; height: 28px; background: var(--bright-red); color: white; border-radius: 50%; font-size: 0.9rem; font-weight: bold; margin-right: 1rem; flex-shrink: 0; }
  .faq-arrow { font-size: 1.2rem; transition: transform 0.2s; }
  .faq-a { padding: 0 1.5rem 1.5rem 3.5rem; color: #555; display: none; line-height: 1.7; }
  .faq-item.active .faq-a { display: block; }
  .faq-item.active .faq-arrow { transform: rotate(180deg); }
  
  .eyebrow-red { font-size: 0.9rem; font-weight: bold; color: var(--bright-red); text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.75rem; display: block; }
  .eyebrow-white { font-size: 0.9rem; font-weight: bold; color: white; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 0.75rem; display: block; }
  .section-h2 { font-size: 2.25rem; font-weight: bold; line-height: 1.2; margin-bottom: 2rem; }
  .list-checkmark { list-style: none; margin-top: 1rem; }
  .list-checkmark li { position: relative; padding-left: 1.75rem; margin-bottom: 0.75rem; }
  .list-checkmark li::before { content: '✓'; position: absolute; left: 0; top: 0; color: var(--bright-red); font-weight: bold; font-size: 1.1rem; }
  .card-red .list-checkmark li::before { color: white; }
</style>
<script>
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.faq-q').forEach(q => {
    q.addEventListener('click', () => {
      const item = q.parentElement;
      item.classList.toggle('active');
    });
  });
});
</script>
"""

dummy_header = "<header></header>"
dummy_footer = "<footer></footer>"

def build_service_page(filename, title, eyebrow, hero_desc, hero_bullets, what_is_desc, what_is_cards, benefits_cards, services_cards, process_steps, why_cards, faqs):
    bullets_html = "".join([f"<li style='position: relative; padding-left: 1.5rem; margin-bottom: 0.5rem; color: #e0e0e0;'><span style='position: absolute; left: 0; top: 8px; width: 6px; height: 6px; background-color: white; border-radius: 50%;'></span>{b}</li>" for b in hero_bullets])
    hero_section = f"""
    <section style="background-color: var(--dark-charcoal); padding: 6rem 0;">
      <div class="container" style="display: grid; grid-template-columns: 1.2fr 0.8fr; gap: 3rem; align-items: center;">
        <div>
          <div style="margin-bottom: 1.5rem; display: flex; align-items: center; gap: 1rem;">
            <span style="border: 1px solid var(--bright-red); background-color: rgba(217, 28, 36, 0.1); color: var(--bright-red); padding: 6px 16px; border-radius: 50px; font-size: 0.9rem; font-weight: 500;">{eyebrow}</span>
          </div>
          <h1 style="font-size: 3.5rem; font-weight: bold; line-height: 1.1; margin-bottom: 1.5rem; color: white;">{title}</h1>
          <p style="font-size: 1.25rem; color: #aaa; margin-bottom: 2rem; max-width: 650px;">{hero_desc}</p>
          <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem 1rem; margin-bottom: 3rem; max-width: 600px;">
            <ul style="list-style: none;">
              {bullets_html}
            </ul>
          </div>
          <div>
            <a href="free-consultation.html" class="btn-primary">GET YOUR FREE PROPOSAL</a>
          </div>
        </div>
        <div>
          <img src="images/video_player.png" alt="{title} Graphic" style="width: 100%; border-radius: 12px; opacity: 0.95; box-shadow: 0 10px 30px rgba(0,0,0,0.3);">
        </div>
      </div>
    </section>
    """

    what_is_cards_html = ""
    what_is_cards_html += f"""
      <div class="card-red">
        <h3 style="font-size: 1.5rem; margin-bottom: 1rem; color: white;">{what_is_cards[0][0]}</h3>
        <p style="color: white; line-height: 1.6;">{what_is_cards[0][1]}</p>
      </div>
    """
    for title_c, desc_c in what_is_cards[1:]:
        what_is_cards_html += f"""
          <div class="card-light">
            <h3 style="font-size: 1.25rem; margin-bottom: 1rem; color: var(--dark-charcoal);">{title_c}</h3>
            <p style="color: #555; line-height: 1.6;">{desc_c}</p>
          </div>
        """
    what_is_section = f"""
    <section style="background-color: var(--off-white); color: var(--dark-charcoal);">
      <div class="container">
        <div style="text-align: center; max-width: 800px; margin: 0 auto 3.5rem auto;">
          <span style="font-size: 0.85rem; color: #888; text-transform: uppercase; font-weight: bold; letter-spacing: 1px;">Overview</span>
          <h2 class="section-title" style="margin-top: 0.5rem; color: var(--dark-charcoal);">{what_is_desc}</h2>
        </div>
        <div class="grid-3">
          {what_is_cards_html}
        </div>
      </div>
    </section>
    """

    benefits_cards_html = ""
    benefits_cards_html += f"""
      <div class="card-red">
        <div class="card-num">1</div>
        <h3 style="font-size: 1.25rem; margin-bottom: 1rem; color: white;">{benefits_cards[0][0]}</h3>
        <p style="color: white; font-size: 0.95rem; line-height: 1.6;">{benefits_cards[0][1]}</p>
      </div>
    """
    for idx, (title_c, desc_c) in enumerate(benefits_cards[1:]):
        num = idx + 2
        benefits_cards_html += f"""
          <div class="card-dark">
            <div class="card-num">{num}</div>
            <h3 style="font-size: 1.25rem; margin-bottom: 1rem; color: white;">{title_c}</h3>
            <p style="color: #aaa; font-size: 0.95rem; line-height: 1.6;">{desc_c}</p>
          </div>
        """
    benefits_grid_class = "grid-3" if len(benefits_cards) == 6 else "grid-4"
    benefits_section = f"""
    <section style="background-color: var(--dark-charcoal); color: white;">
      <div class="container">
        <div style="text-align: center; max-width: 800px; margin: 0 auto 3.5rem auto;">
          <span style="font-size: 0.85rem; color: #aaa; text-transform: uppercase; font-weight: bold; letter-spacing: 1px;">Key Advantages</span>
          <h2 class="section-title" style="margin-top: 0.5rem; color: white;">Why Businesses Invest in these Services</h2>
        </div>
        <div class="{benefits_grid_class}">
          {benefits_cards_html}
        </div>
      </div>
    </section>
    """

    services_cards_html = ""
    services_cards_html += f"""
      <div class="card-red">
        <h3 style="font-size: 1.25rem; margin-bottom: 1rem; color: white;">{services_cards[0][0]}</h3>
        <p style="color: white; font-size: 0.95rem; line-height: 1.6;">{services_cards[0][1]}</p>
      </div>
    """
    for title_c, desc_c in services_cards[1:]:
        services_cards_html += f"""
          <div class="card-light">
            <h3 style="font-size: 1.25rem; margin-bottom: 1rem; color: var(--dark-charcoal);">{title_c}</h3>
            <p style="color: #555; font-size: 0.95rem; line-height: 1.6;">{desc_c}</p>
          </div>
        """
    services_grid_class = "grid-3" if len(services_cards) <= 6 else "grid-4"
    services_section = f"""
    <section style="background-color: var(--off-white); color: var(--dark-charcoal);">
      <div class="container">
        <div style="text-align: center; max-width: 800px; margin: 0 auto 3.5rem auto;">
          <span style="font-size: 0.85rem; color: #888; text-transform: uppercase; font-weight: bold; letter-spacing: 1px;">Core Offerings</span>
          <h2 class="section-title" style="margin-top: 0.5rem; color: var(--dark-charcoal);">Complete Deliverables & Capabilities</h2>
        </div>
        <div class="{services_grid_class}">
          {services_cards_html}
        </div>
      </div>
    </section>
    """

    process_steps_html = ""
    process_steps_html += f"""
      <div class="process-card red">
        <div class="process-num">1</div>
        <div>
          <h3 class="step-title" style="color: white; font-size: 1.35rem; margin-bottom: 0.5rem;">{process_steps[0][0]}</h3>
          <p style="color: white; line-height: 1.6;">{process_steps[0][1]}</p>
        </div>
      </div>
    """
    for idx, (title_c, desc_c) in enumerate(process_steps[1:]):
        num = idx + 2
        process_steps_html += f"""
          <div class="process-card dark">
            <div class="process-num">{num}</div>
            <div>
              <h3 class="step-title" style="color: white; font-size: 1.35rem; margin-bottom: 0.5rem;">{title_c}</h3>
              <p style="color: #aaa; line-height: 1.6;">{desc_c}</p>
            </div>
          </div>
        """
    process_section = f"""
    <section style="background-color: var(--dark-charcoal); color: white;">
      <div class="container">
        <div style="text-align: center; max-width: 800px; margin: 0 auto 3.5rem auto;">
          <span style="font-size: 0.85rem; color: #aaa; text-transform: uppercase; font-weight: bold; letter-spacing: 1px;">Our Workflow</span>
          <h2 class="section-title" style="margin-top: 0.5rem; color: white;">Our Proven Success Process</h2>
        </div>
        <div class="process-timeline">
          {process_steps_html}
        </div>
      </div>
    </section>
    """

    why_cards_html = ""
    why_cards_html += f"""
      <div class="card-red">
        <h3 style="font-size: 1.25rem; margin-bottom: 1rem; color: white;">{why_cards[0][0]}</h3>
        <p style="color: white; font-size: 0.95rem; line-height: 1.6;">{why_cards[0][1]}</p>
      </div>
    """
    for title_c, desc_c in why_cards[1:]:
        why_cards_html += f"""
          <div class="card-light">
            <h3 style="font-size: 1.25rem; margin-bottom: 1rem; color: var(--dark-charcoal);">{title_c}</h3>
            <p style="color: #555; font-size: 0.95rem; line-height: 1.6;">{desc_c}</p>
          </div>
        """
    why_grid_class = "grid-3" if len(why_cards) == 6 else "grid-4"
    why_section = f"""
    <section style="background-color: var(--off-white); color: var(--dark-charcoal);">
      <div class="container">
        <div style="text-align: center; max-width: 800px; margin: 0 auto 3.5rem auto;">
          <span style="font-size: 0.85rem; color: #888; text-transform: uppercase; font-weight: bold; letter-spacing: 1px;">Why Partner With Us</span>
          <h2 class="section-title" style="margin-top: 0.5rem; color: var(--dark-charcoal);">Why Businesses Trust GBO</h2>
        </div>
        <div class="{why_grid_class}">
          {why_cards_html}
        </div>
      </div>
    </section>
    """

    faqs_html = ""
    for idx, (q, a) in enumerate(faqs):
        num = idx + 1
        faqs_html += f"""
        <div class="faq-item">
          <div class="faq-q">
            <div style="display: flex; align-items: center;">
              <span class="faq-num">{num}</span>
              <span>{q}</span>
            </div>
            <span class="faq-arrow">&#9662;</span>
          </div>
          <div class="faq-a">
            <p>{a}</p>
          </div>
        </div>
        """
    faq_section = f"""
    <section style="background-color: var(--off-white); color: var(--dark-charcoal); border-top: 1px solid #e0e0e0;">
      <div class="container" style="max-width: 850px;">
        <div style="text-align: center; margin-bottom: 3.5rem;">
          <span style="font-size: 0.85rem; color: #888; text-transform: uppercase; font-weight: bold; letter-spacing: 1px;">Frequently Asked Questions</span>
          <h2 class="section-title" style="margin-top: 0.5rem; color: var(--dark-charcoal); margin-bottom: 0;">Got Questions? We Have Answers.</h2>
        </div>
        <div class="faq-list">
          {faqs_html}
        </div>
      </div>
    </section>
    """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - GBO</title>
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  {styles}
</head>
<body>
  {dummy_header}
  {hero_section}
  {what_is_section}
  {benefits_section}
  {services_section}
  {process_section}
  {why_section}
  {faq_section}
  {dummy_footer}
</body>
</html>"""

    with open(os.path.join(out_dir, filename), "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Generated: {filename}")


# Rebuild 10 pages
# 1. youtube-optimization.html
build_service_page(
    filename="youtube-optimization.html",
    title="YouTube SEO & Optimization Services",
    eyebrow="YouTube Search Marketing",
    hero_desc="Boost your YouTube rankings, increase video visibility, and attract a highly engaged audience with GBO's advanced YouTube SEO Services.",
    hero_bullets=[
        "YouTube Channel Audits", "Competitor Channel Research", "SEO Video Titles & Descriptions", 
        "Tags & Category Metadata", "Custom High-CTR Thumbnails", "Watch Time & Session Optimization",
        "Subscriber Growth Roadmaps", "Video Embed & Schema Markup", "Interactive Cards & Endscreens", 
        "Advanced YouTube Analytics"
    ],
    what_is_desc="What Are YouTube SEO & Optimization Services?",
    what_is_cards=[
        ("YouTube SEO", "The process of optimizing your channel, playlists, metadata, and video files to rank higher in YouTube search results, recommendations, and Google Video tabs."),
        ("Target High-Intent Users", "Capture views from users searching for specific guides, tutorials, or product reviews at the exact moment they look for answers."),
        ("Drive Sustainable Leads", "Convert views into traffic and customers by placing clear calls-to-action in video descriptions, pins, cards, and endscreens.")
    ],
    benefits_cards=[
        ("Increase Video Views", "Grow your organic view count by ranking for high-volume, relevant transactional keywords and search terms."),
        ("Higher Subscriber Conversion", "Turn one-time video viewers into long-term channel subscribers by delivering highly relevant video experiences."),
        ("Maximize Watch Time", "Keep users watching longer by optimizing your video pacing, playlist configurations, and endscreeen cards."),
        ("Boost Click-Through Rate", "A/B test custom thumbnail designs and headlines to make your videos stand out and drive clicks."),
        ("Build Brand Authority", "Establish direct credibility and position your brand as a trusted authority on the world's second largest search platform."),
        ("Google Video Integration", "Ensure your videos rank in standard Google Search result pages in the video carousel snippets.")
    ],
    services_cards=[
        ("YouTube Channel Audit", "We perform a thorough review of your existing channel structure, playlists, meta tags, and overall visibility gaps."),
        ("Video Keyword Research", "Discover high-volume, low-competition keywords your ideal target audience uses on YouTube and Google."),
        ("Metadata Optimization", "Optimize video title tags, write informative descriptions, and input targeted search tags for maximum crawl bot trust."),
        ("Custom Thumbnail Design", "Design scroll-stopping, high-contrast thumbnails that capture attention and increase click rates."),
        ("Playlist & Card Setup", "Organize video assets into logical playlists and configure interactive links and endscreens to extend watch time."),
        ("Subtitle & Script Uploads", "Upload accurate SRT files and caption scripts to feed search engine indexes with readable text content.")
    ],
    process_steps=[
        ("Channel Audit & Setup", "We review channel configuration, playlist arrangements, layout branding, and indexing parameters."),
        ("Keyword & Topic Mapping", "Find high-value search queries with actual search volume matching your services."),
        ("Asset & Metadata Creation", "Draft SEO-optimized video titles, descriptions, tag parameters, and custom thumbnail options."),
        ("Caption & Schema Integration", "Configure VideoObject schema, embed video files, and sync accurate subtitle transcription files."),
        ("Campaign Launch", "Publish videos using optimized schedule patterns and early engagement hooks to trigger algorithms."),
        ("Performance Reporting", "Deliver monthly campaign reports tracking views, watch time, CTR, subscriber growth, and traffic outcomes.")
    ],
    why_cards=[
        ("YouTube Algorithm Experts", "We stay updated on the latest ranking factors and algorithm shifts governing video search."),
        ("Advanced Analytics Tools", "We use premium search tools to identify keyword opportunities and track position changes."),
        ("Multi-Platform Strategy", "We integrate your video assets with website content to maximize your overall digital marketing ROI."),
        ("Creative Design Support", "Our dedicated team of graphic designers and copywriters write and design high-performing assets."),
        ("Transparent Reporting", "Detailed reports tracking channel performance, website traffic, and customer leads."),
        ("Long-Term Value", "Build an organic search asset that keeps generating views, traffic, and sales for years.")
    ],
    faqs=[
        ("What is YouTube Optimization?", "It is the process of optimizing your channel, videos, and playlists to rank higher in YouTube search results and recommendations."),
        ("How long does it take to see results?", "YouTube's search algorithm updates very quickly, so optimized metadata changes can show ranking increases within days to weeks."),
        ("Do you design custom thumbnails?", "Yes. We design high-contrast custom thumbnails designed specifically to increase click-through rates."),
        ("Can YouTube SEO help my website rankings?", "Yes. Embedding optimized YouTube videos on your site increases dwell time, which is a key ranking factor for Google SEO."),
        ("Do you provide monthly reports?", "Absolutely. We provide clear monthly reports tracking video views, watch time, subscriber growth, and lead conversions.")
    ]
)

# 2. vlog-video-production.html
build_service_page(
    filename="vlog-video-production.html",
    title="Vlog & Video Production Services",
    eyebrow="Video Content Production",
    hero_desc="Create professional, engaging vlogs and high-quality video content that builds brand awareness, audience trust, and drives customer conversions.",
    hero_bullets=[
        "Professional Vlog Production", "AI Avatar Video Creation", "Corporate Video Production", 
        "Social Media Reels & Shorts", "Product Demo Video Creation", "Motion Graphics & Animation",
        "YouTube Video Production", "Video Editing & Optimization", "Scriptwriting & Storyboarding",
        "Multi-Platform Distribution"
    ],
    what_is_desc="What Are Vlog & Video Production Services?",
    what_is_cards=[
        ("Video Production Services", "The end-to-end process of planning, filming, editing, and optimizing high-quality video assets designed to capture attention and tell your brand's story."),
        ("Build Customer Trust", "Humanize your business by connecting directly with your target audience through engaging video content."),
        ("Increase Social Reach", "Generate more views and shares across platforms like YouTube, Instagram, Facebook, and TikTok.")
    ],
    benefits_cards=[
        ("Increase Audience Engagement", "Video captures user attention faster and keeps prospects engaged with your brand longer than plain text."),
        ("Build Stronger Brand Awareness", "Create memorable, brand-consistent visual experiences that strengthen recognition."),
        ("Improve Social Performance", "Generate more engagement, shares, and comments across all major social media channels."),
        ("Build Trust & Credibility", "Professional video production establishes your business as a trusted industry authority."),
        ("Support SEO & AI Search", "Video content improves discoverability across search engines and AI generative recommendation engines."),
        ("Generate More Leads", "Drive direct customer actions and sales conversions through strategic and engaging video content.")
    ],
    services_cards=[
        ("Vlog Video Production", "Create engaging, consistent vlogs that educate your audience, build loyalty, and showcase your expertise."),
        ("Corporate Video Production", "Showcase your company profile, team culture, office workspace, and B2B services professionally."),
        ("AI Avatar Video Production", "Scale content production quickly using advanced AI avatar technology without traditional filming limitations."),
        ("Promotional Videos", "Highlight new products, key services, and brand stories through compelling visual narratives."),
        ("Social Media Shorts", "Develop optimized vertical reels, shorts, and TikTok videos designed to capture quick scroll attention."),
        ("Product Demo Videos", "Showcase key product features, benefits, and user guides through clear and engaging video demonstrations.")
    ],
    process_steps=[
        ("Discovery & Strategy", "We understand your brand goals, target audience profiles, and video content requirements."),
        ("Script & Storyboard Development", "Create compelling scripts, hooks, and storyboards that capture your key messaging."),
        ("Production & Recording", "Film live-action video or utilize advanced AI-powered avatar video tools."),
        ("Editing & Motion Graphics", "Refine raw footage, add background audio, captions, motion graphics, and brand transitions."),
        ("SEO Optimization", "Optimize final files with tags, titles, captions, and sitemaps for maximum search indexing."),
        ("Publishing & Distribution", "Deploy video assets across your website, social networks, and targeted advertising channels.")
    ],
    why_cards=[
        ("AI-Powered Marketing Expertise", "We combine video production skills with advanced, data-driven digital marketing strategies."),
        ("Experienced Creative Team", "Work with skilled directors, editors, scriptwriters, and graphic designers."),
        ("End-to-End Solutions", "We handle everything from initial concept drafting to final SEO indexing and promotion."),
        ("AI Avatar Specialists", "Create scalable video training and marketing content quickly without filming delays."),
        ("Multi-Platform Optimization", "Ensure your videos render perfectly on mobile, tablet, and desktop screens."),
        ("Results-Focused Approach", "We focus on creating videos that generate actual views, leads, and customer sales.")
    ],
    faqs=[
        ("What types of videos do you produce?", "We produce vlogs, AI avatar videos, corporate overviews, product demos, explainer videos, and social media reels."),
        ("What are AI Avatar Videos?", "AI Avatar Videos use artificial intelligence to create realistic digital presenters, allowing you to scale video production quickly."),
        ("Can you edit existing video footage?", "Yes. We offer professional video editing, color grading, motion graphics, and audio sync services for existing raw clips."),
        ("Do you provide scriptwriting services?", "Yes, we handle script drafting, conceptual hooks, and storyboarding to ensure your message is clear and engaging."),
        ("How long does video production take?", "Timelines vary depending on project scope, but simple vlog edit runs take 3-5 days, while complex custom shoots can take 2-4 weeks.")
    ]
)

# 3. customer-testimonial-video.html
build_service_page(
    filename="customer-testimonial-video.html",
    title="Customer Testimonial Video Services",
    eyebrow="Social Proof Video Production",
    hero_desc="Turn happy customers into powerful brand advocates. Generate authentic testimonial videos that build instant credibility and boost your sales conversions.",
    hero_bullets=[
        "Customer Testimonial Videos", "Client Success Story Videos", "Case Study Video Production", 
        "Interview-Based Testimonials", "Video Editing & Enhancements", "Social Media Testimonial Videos",
        "Website Testimonial Videos", "Multi-Platform Video Optimization", "Scripting & Prep Support",
        "Professional Remote Filming"
    ],
    what_is_desc="What Are Customer Testimonial Video Services?",
    what_is_cards=[
        ("Testimonial Videos", "Authentic video interviews and case studies featuring real clients sharing their success stories and experiences working with your business."),
        ("Build Trust Instantly", "Establish immediate brand trust using direct social proof from real, satisfied clients."),
        ("Influence Buying Decisions", "Help prospects overcome purchasing hesitation by showing real-world results and benefits.")
    ],
    benefits_cards=[
        ("Build Instant Credibility", "Real customer stories create trust much faster than traditional marketing messages."),
        ("Increase Sales Conversions", "Prospects are more likely to convert into buyers after seeing proven client success stories."),
        ("Strengthen Brand Authority", "Showcase successful business outcomes, metrics, and high client satisfaction levels."),
        ("Reduce Purchase Hesitation", "Address common concerns, risks, and objections through authentic customer narratives."),
        ("Improve Engagement", "Video testimonials capture user attention and create stronger emotional connections than text reviews."),
        ("Support Ad Campaigns", "Utilize testimonial video snippets in retargeting ad campaigns to maximize conversion ROI.")
    ],
    services_cards=[
        ("Customer Testimonial Videos", "Capture honest, positive feedback from your key customers discussing their experiences."),
        ("Client Success Stories", "Highlight specific challenges, GBO solutions, and final metrics achieved for a client."),
        ("Case Study Videos", "Present detailed success stories through engaging video content."),
        ("Interview-Based Videos", "Conduct professional, guided interviews with key executives and happy users."),
        ("Product Review Testimonials", "Demonstrate actual product performance and customer happiness through review videos."),
        ("Social Media Testimonials", "Edit short, punchy vertical testimonial clips perfect for Instagram, LinkedIn, and TikTok.")
    ],
    process_steps=[
        ("Discovery & Planning", "Identify target customer candidates, key success metrics, and core messaging hooks."),
        ("Interview Prep", "Develop strategic, open-ended questions designed to elicit natural and compelling answers."),
        ("Remote or On-Site Recording", "Set up professional remote capture tools or capture on-site video footage of the client."),
        ("Editing & Enhancements", "Trim interview clips, add supporting b-roll, text metrics, background audio, and branding."),
        ("SEO & Embed Setup", "Optimize video files and embed testimonials strategically onto key conversion landing pages."),
        ("Launch & Promotion", "Distribute testimonial videos across websites, email campaigns, and targeted ads.")
    ],
    why_cards=[
        ("Professional Video Production", "High-quality, polished videos that protect and project your professional brand image."),
        ("Story-Driven Approach", "We focus on building a narrative: the problem, the solution, and the final positive results."),
        ("AI-Powered Marketing Solutions", "Integrate testimonial videos with advanced keyword research and search marketing."),
        ("Multi-Platform Optimization", "Format videos for seamless playback across mobile, tablet, and desktop channels."),
        ("Experienced Creative Team", "Work with interview specialists who help clients feel comfortable and express their stories naturally."),
        ("Conversion-Focused Strategy", "We design videos specifically to sit on product pages and increase checkout rates.")
    ],
    faqs=[
        ("What are customer testimonial videos?", "They are video reviews featuring real clients discussing how your products or services solved their problems and helped them succeed."),
        ("How long should testimonial videos be?", "For websites and ads, the most effective length is between 45 seconds and 3 minutes. Social media clips can be 15-30 seconds."),
        ("Do you help prepare the client?", "Yes. We provide question lists, staging advice, and support guides to help your clients feel comfortable and ready."),
        ("Can we use these videos in ads?", "Absolutely. Testimonial videos are highly effective when used in Facebook, Google, and LinkedIn retargeting ad campaigns."),
        ("How do remote testimonial captures work?", "We use premium, browser-based remote video recording tools that allow clients to capture high-definition video using their own devices without installing software.")
    ]
)

# 4. meta-ads.html
build_service_page(
    filename="meta-ads.html",
    title="Meta Ads & Facebook Advertising Services",
    eyebrow="Meta Ads Management",
    hero_desc="Connect with your target audience, generate quality leads, and scale your brand visibility across Facebook, Instagram, and Messenger with expert Meta Ads campaigns.",
    hero_bullets=[
        "Facebook Advertising Campaigns", "Facebook Lead Generation", "Advanced Demographic Targeting", 
        "Facebook Retargeting Ads", "Instagram Ads Management", "Creative Ad Graphic Design",
        "Meta Pixel Conversion Tracking", "Facebook Page Optimization", "Budget Allocation Strategy", 
        "Daily Bid Management"
    ],
    what_is_desc="What Are Meta Ads & Facebook Advertising Services?",
    what_is_cards=[
        ("Meta Ads", "Paid advertising campaigns run across Facebook, Instagram, Messenger, and the Audience Network using Meta's advanced targeting database."),
        ("Generate Quality Leads", "Capture name, email, and phone data directly in the social feed using optimized lead forms."),
        ("Increase Sales", "Drive traffic directly to your e-commerce store or landing pages to scale your business conversions.")
    ],
    benefits_cards=[
        ("Reach High-Intent Audiences", "Target users based on precise interests, demographics, location, and past buying behaviors."),
        ("Increase Brand Visibility", "Maintain consistent ad visibility across the world's most popular social networks."),
        ("Scale Lead Generation", "Generate a steady stream of B2B and B2C leads using native lead forms that increase conversion rates."),
        ("Optimize Marketing ROI", "Continuously test creatives, headlines, and bid parameters to maximize your Return on Ad Spend (ROAS)."),
        ("Re-Engage Hot Leads", "Run retargeting campaigns to capture users who visited your site but haven't purchased yet."),
        ("Detailed Analytics Insight", "Track cost-per-click, cost-per-lead, and sales metrics to optimize budgets.")
    ],
    services_cards=[
        ("Meta Ad Campaign Setup", "Build campaigns from scratch with custom audience segments, budgets, and bid configurations."),
        ("Lead Form Optimization", "Design and write high-converting custom instant forms to capture qualified business leads."),
        ("Creative Design & Copywriting", "Create scroll-stopping image banners, video scripts, and persuasive ad copy."),
        ("Instagram Ads Management", "Target younger demographic pools with custom reels, stories, and feed ad placements."),
        ("Retargeting Campaign Setup", "Re-target warm website visitors, cart abandoners, and page engagers to secure sales."),
        ("Pixel & API Tracking", "Install Meta Pixel and Conversions API to ensure accurate conversion tracking and data matching.")
    ],
    process_steps=[
        ("Business & Competitor Audit", "We audit your existing ad account, pixel health, past data, and analyze competitor ad strategies."),
        ("Audience & Targeting Research", "Identify your ideal customer demographics, interests, and build custom lookalike segments."),
        ("Ad Creative Production", "Write high-converting ad copy, design graphic banners, and build video ad components."),
        ("Campaign Configuration", "Set up campaign structures, target parameters, budget caps, and launch the ads."),
        ("A/B Testing", "Test multiple creative hooks, headlines, and landing page URLs to find the lowest CPA."),
        ("Scale & Report", "Scale winning ad sets weekly and deliver detailed reports showing spend, leads, and ROAS.")
    ],
    why_cards=[
        ("AI-Powered Campaign Insights", "We leverage advanced AI analytics to optimize targeting, bidding, and ad formats."),
        ("Certified Meta Ads Experts", "Work with experienced account managers who have managed thousands in ad spend."),
        ("Creative-First Strategy", "We design visually stunning, scroll-stopping ads that capture user attention instantly."),
        ("Data-Driven Decisions", "Every optimization is backed by conversion analytics, pixel tracking, and A/B test data."),
        ("Transparent reporting", "Detailed reports tracking reach, cost-per-lead, conversion volume, and advertising ROI."),
        ("Scalable Growth Models", "Flexible management structures built to scale as your business budget and lead volume grow.")
    ],
    faqs=[
        ("How much does Facebook advertising cost?", "Budgets vary. You can start with as little as $10/day, but we typically recommend a minimum ad budget of $1,000/month to see consistent lead volume."),
        ("How quickly will I see results?", "Meta Ads go live almost instantly. You can start seeing traffic, clicks, and leads within 24 to 48 hours of campaign launch."),
        ("Do you design the ad graphics?", "Yes. We handle the copywriting, graphic design, and video editing for all ad creatives in your campaign."),
        ("What is a lookalike audience?", "A lookalike audience is a custom targeting segment created by Meta that matches the characteristics of your existing customer list."),
        ("Do you provide monthly reports?", "Yes, we provide transparent monthly reports tracking ad spend, clicks, impressions, cost-per-lead, and ROAS.")
    ]
)

# 5. google-ads.html
build_service_page(
    filename="google-ads.html",
    title="Google Ads Management Services",
    eyebrow="Google PPC Management",
    hero_desc="Reach customers actively searching for your products and services on Google. Maximize clicks, generate qualified leads, and scale your sales ROI with expert PPC management.",
    hero_bullets=[
        "Google Search Ads", "Google Display Advertising", "Google Shopping Campaigns", 
        "YouTube Video Advertising", "Remarketing Campaigns", "Keyword Research & Mapping",
        "Google Tag Manager Setup", "Landing Page Optimization", "Bid & Budget Management", 
        "Negative Keyword Exclusions"
    ],
    what_is_desc="What Are Google Ads Management Services?",
    what_is_cards=[
        ("Google Ads", "Google's Pay-Per-Click (PPC) advertising platform that allows businesses to show ads on Google Search, Maps, YouTube, Shopping, and partner sites."),
        ("Capture Search Intent", "Show your business to users searching for specific services at the exact moment they want to buy."),
        ("Maximize PPC ROI", "Control ad spend, lower cost-per-click (CPC), and scale conversions through certified account optimization.")
    ],
    benefits_cards=[
        ("Reach Active Searchers", "Target customers with high intent who are actively searching for your products or services."),
        ("Generate Instant Traffic", "Skip the search engine queue and get qualified website traffic immediately from day one."),
        ("Flexible Ad Budgets", "Set daily budget caps, control bidding, and only pay when users click on your ads."),
        ("Advanced Search Targeting", "Filter ads by specific locations, languages, device types, and times of day."),
        ("Detailed Conversion Tracking", "Measure exactly which keywords, ads, and campaigns are generating customer phone calls and sales."),
        ("Brand Visibility Boost", "Dominate search result pages by appearing at the very top for competitive search terms.")
    ],
    services_cards=[
        ("Google Search Campaigns", "Write high-CTR text ads that rank at the top of Google search results for key target terms."),
        ("Google Shopping Ads", "Display product images, prices, and reviews in Google Shopping grids to drive direct product checkouts."),
        ("YouTube Advertising", "Target prospective buyers with engaging video ads before, during, and after YouTube videos."),
        ("Display Network Ads", "Run visual banner ads across millions of partner websites to increase brand recall."),
        ("Remarketing Campaign Setup", "Re-engage site visitors who left without completing a form or checkout purchase."),
        ("Conversion Setup (GTM)", "Integrate Google Tag Manager and GA4 to track calls, forms, and ecommerce purchases accurately.")
    ],
    process_steps=[
        ("Google Ads Account Audit", "We review your account settings, keyword quality, tracking pixels, and identify ad spend waste."),
        ("Competitor Research", "Analyze competitor ad copy hooks, keyword bids, and landing page layouts."),
        ("Keyword Intent Planning", "Find transactional, high-converting keywords while excluding negative search terms."),
        ("Ad Writing & Creative Design", "Write headlines, description copy variations, configure site extensions, and design display banners."),
        ("Tracking Pixel Setup", "Set up Google Tag Manager conversion events to track leads and e-commerce purchases."),
        ("Daily Optimization", "Manage bids, audit search terms, exclude poor queries, and scale high-performing campaigns weekly.")
    ],
    why_cards=[
        ("AI-Powered Bid Optimization", "We leverage Google's AI bidding models combined with manual bid monitoring to maximize conversions."),
        ("Certified Google Ads Experts", "Our account managers are certified in Google Search, Display, Video, and Shopping ads."),
        ("Negative Keyword Scrapes", "We clean up search queries daily to stop your budget from wasting on unrelated terms."),
        ("Conversion Rate Focus", "We analyze and optimize landing page layouts to turn ad clicks into actual phone calls and leads."),
        ("Transparent Campaign Data", "Access clear monthly reports tracking impressions, clicks, CTR, cost-per-lead, and ROAS."),
        ("Long-Term Paid Growth", "Configure scalable ad structures designed to maintain stable lead generation costs as budgets grow.")
    ],
    faqs=[
        ("How does Google Ads billing work?", "Google Ads is Pay-Per-Click. You pay Google directly for each click on your ads, setting a daily budget cap to control costs."),
        ("How quickly will my ads show?", "Once your campaign is set up and approved, your ads will start showing on Google Search almost instantly."),
        ("What is a negative keyword?", "A negative keyword is a search term you exclude from your campaign to prevent your ads from showing for irrelevant search queries."),
        ("Do you manage existing Google Ads accounts?", "Yes. We perform a thorough audit of your current ad account, fix tracking issues, optimize keywords, and take over ongoing management."),
        ("How do you measure PPC campaign success?", "We track conversions (form submissions, calls, checkouts), cost-per-conversion, click-through-rates, and return on ad spend (ROAS).")
    ]
)

# 6. ecommerce-ppc.html
build_service_page(
    filename="ecommerce-ppc.html",
    title="eCommerce PPC Advertising Services",
    eyebrow="eCommerce PPC Management",
    hero_desc="Scale your online sales and maximize your Return on Ad Spend (ROAS). Drive targeted shopping traffic directly to your product pages with expert eCommerce PPC.",
    hero_bullets=[
        "Google Shopping Ads", "eCommerce PPC Management", "Product Listing Ads (PLA)", 
        "Audience Retargeting Campaigns", "ROAS Optimization Strategies", "Keyword & Competitor Research",
        "Conversion Tracking (GTM)", "Performance Analytics", "Dynamic Remarketing Ads", 
        "Feed Optimization & Management"
    ],
    what_is_desc="What Are eCommerce PPC Advertising Services?",
    what_is_cards=[
        ("eCommerce PPC", "Paid search and shopping campaigns designed specifically to drive high-intent shoppers to online store product listings and secure direct checkouts."),
        ("Increase Store Sales", "Put your product images, prices, and reviews in front of shoppers actively ready to buy."),
        ("Maximize ROAS", "Optimize bidding, product feeds, and ad channels to ensure high revenue returns for your ad spend.")
    ],
    benefits_cards=[
        ("Reach Shoppers Instantly", "Target consumers actively looking for specific products on Google Shopping, Search, and Social feeds."),
        ("Increase Product Visibility", "Appear at the top of Google Shopping search grids with clear product details and pricing."),
        ("Boost Conversion Rates", "Deliver high-intent shoppers directly to conversion-optimized product detail pages."),
        ("Scale Revenue Faster", "Generate product sales, customers, and data from day one without waiting for SEO ranking growth."),
        ("Reduce Cost-Per-Acquisition", "Optimize bids and exclude poor keywords to lower your cost-per-sale over time."),
        ("Dynamic Ad Remarketing", "Automatically display viewed products to site visitors who left without completing checkouts.")
    ],
    services_cards=[
        ("Google Shopping Campaigns", "Configure and optimize product campaigns to display in Google Shopping results."),
        ("Dynamic Product Ads (DPA)", "Run dynamic ads across Meta showing the exact products users viewed on your site."),
        ("Merchant Center Feed Setup", "Optimize product catalog titles, descriptions, attributes, and image links in Google Merchant Center."),
        ("eCommerce Keyword Targeting", "Target transactional keyword strings like 'buy [product]' and 'best price for [product]'."),
        ("ROAS Bidding Optimization", "Utilize smart bidding strategies focused on generating maximum shopping cart revenue."),
        ("Cart Abandoner Retargeting", "Target users who added items to their shopping carts but abandoned checkout pages.")
    ],
    process_steps=[
        ("Account & Catalog Audit", "We review your e-commerce platform integration, merchant center feed quality, and past ad data."),
        ("Product Feed Optimization", "Optimize product titles, descriptions, attributes, and image links to increase search relevance."),
        ("Campaign Configuration", "Set up Google Shopping, Performance Max, search PPC, and dynamic social retargeting ads."),
        ("Tracking Pixel Integration", "Ensure purchase values, cart additions, and checkouts are tracked accurately using GTM."),
        ("Bidding & Budget Management", "Monitor cost-per-click, manage bid limits, and focus spend on top-selling products."),
        ("Scaling & Reporting", "Scale budget allocation on highly profitable products and deliver detailed ROAS monthly reports.")
    ],
    why_cards=[
        ("ROAS-Focused Optimization", "We focus strictly on the metrics that matter: sales revenue, cart value, and return on ad spend."),
        ("Merchant Feed Specialists", "We resolve feed errors, optimize titles, and configure taxonomies in Google Merchant Center."),
        ("Multi-Platform eCommerce Reach", "Manage shopping campaigns across Google, Meta, Instagram, Pinterest, and marketplaces."),
        ("Data-Driven Campaign Management", "Continuous budget shifts toward high-margin, top-selling product categories."),
        ("Transparent Performance Data", "Detailed reports tracking ad spend, clicks, product views, purchases, and final store ROAS."),
        ("Scalable eCommerce Scaling", "Strategies built to help new startups launch and established e-commerce brands scale sales volume.")
    ],
    faqs=[
        ("What is eCommerce PPC?", "It is paid advertising designed specifically to promote online store catalogs, utilizing shopping, search, and social ads to drive direct product purchases."),
        ("What is ROAS?", "ROAS stands for Return on Ad Spend. It measures the amount of revenue generated for every dollar spent on advertising (e.g. 5x ROAS means $5 generated for every $1 spent)."),
        ("Which platforms do you manage campaigns on?", "We manage e-commerce PPC across Google Shopping, Performance Max, Facebook & Instagram Dynamic Product Ads, and Pinterest Shopping."),
        ("Do you optimize our product feeds?", "Yes. We optimize your product catalog titles, descriptions, category links, and custom tags in Google Merchant Center to increase visibility."),
        ("How long does it take to see sales?", "Shopping and search ads generate immediate traffic, and store sales typically start rolling in within the first few days of campaign launch.")
    ]
)

# 7. yelp-ads.html
build_service_page(
    filename="yelp-ads.html",
    title="Yelp Ads Management Services",
    eyebrow="Yelp Advertising Management",
    hero_desc="Attract local customers actively searching for your services. Dominate local Yelp searches, optimize your profile, and drive more phone calls and bookings.",
    hero_bullets=[
        "Yelp Advertising Management", "Local Audience Targeting", "Yelp Profile Optimization", 
        "Lead Generation Campaigns", "Call & Conversion Tracking", "Competitor Profile Analysis",
        "Bid & Budget Optimization", "Performance Analytics & Reports", "Review Loop Configurations",
        "Yelp Page Customization"
    ],
    what_is_desc="What Are Yelp Ads Management Services?",
    what_is_cards=[
        ("Yelp Ads", "Paid advertising placements that position your local business at the very top of Yelp search results and competitor business listings."),
        ("Capture Local Searches", "Show your business to local users looking for services, contractors, restaurants, or salons nearby."),
        ("Drive Local Bookings", "Increase phone calls, click-to-map directions, and online quote requests from high-intent local buyers.")
    ],
    benefits_cards=[
        ("Reach Local Buyers Ready to Act", "Target users with high commercial intent actively looking for local business services."),
        ("Appear Above Competitors", "Ensure your ad placement appears at the top of Yelp searches and on competitor business pages."),
        ("Increase Call & Lead Volume", "Drive direct phone calls, map directions, website visits, and online call-to-action quote forms."),
        ("Build Trust and Credibility", "Yelp's reputation-driven platform makes highly rated profiles stand out to local shoppers."),
        ("Optimize Local Ad Spend", "Set custom monthly budgets, control bids, and only pay for targeted local clicks."),
        ("Detailed Lead Tracking", "Measure call clicks, form conversions, page views, and ad campaign performance.")
    ],
    services_cards=[
        ("Yelp Campaign Management", "Configure, launch, and manage targeted Yelp keyword ads to drive local customer acquisitions."),
        ("Yelp Profile Optimization", "Optimize business descriptions, photo portfolios, category tags, and list verified services."),
        ("Yelp Review Management", "Implement review loops and support guides to build positive customer feedback signaling."),
        ("Competitor Ad Block Exclusions", "Configure ads to block competitor placements on your own local business profile page."),
        ("Yelp Call Tracking Setup", "Set up phone tracking and form conversion goals to measure the exact ROI of your Yelp campaigns."),
        ("Call-To-Action Optimization", "Design high-converting custom Yelp CTA buttons like 'Request a Quote' or 'Book Online'.")
    ],
    process_steps=[
        ("Yelp Profile & Market Analysis", "We audit your business profile setup, current review count, and analyze local competitor Yelp visibility."),
        ("Profile Copy & Photo Overhaul", "Optimize business descriptions, upload high-quality portfolio images, and organize services."),
        ("Yelp Ad Campaign Setup", "Build campaigns with target location radius, set budget limits, and configure keyword bids."),
        ("CTA Button Configuration", "Add custom action buttons and forms to capture direct customer quotes and bookings."),
        ("Review Signals Build", "Implement automated email/SMS loops to gather positive customer feedback on Yelp."),
        ("Monitoring & Optimization", "Manage ad placement, analyze cost-per-click, track incoming calls, and deliver monthly reports.")
    ],
    why_cards=[
        ("Local Search Marketing Experts", "We understand the Yelp algorithm, local user behaviors, and profile optimization strategies."),
        ("Yelp Certified Setup Partners", "We configure accounts correctly to maximize Yelp credit programs and minimize ad waste."),
        ("Call & Lead Focus", "We track phone calls, map clicks, and quote forms to ensure you acquire real local customers."),
        ("Review Loop Automation", "We build systematic workflows to help your business build positive social proof naturally."),
        ("Transparent Local Reporting", "Access clean monthly reports showing clicks, calls, page views, and client lead conversions."),
        ("Flexible Local Scalability", "Bespoke plans built for small local service shops and multi-location franchise brands.")
    ],
    faqs=[
        ("What are Yelp Ads?", "Yelp Ads are paid listing promotions that place your business at the top of Yelp search results and on related local competitor profile pages."),
        ("Are Yelp Ads effective for small businesses?", "Yes. For local service providers (contractors, plumbers, salons, dental clinics), Yelp is one of the most effective local customer acquisition channels."),
        ("How much does Yelp advertising cost?", "Yelp ads are PPC. You set a daily/monthly budget (e.g. $300-$1000/mo) and pay Yelp for each click on your ad listing."),
        ("Do you handle our Yelp review responses?", "We help you set up professional response templates and review guidelines, but we recommend you reply directly to keep communication authentic."),
        ("How do you measure Yelp campaign success?", "We track ad impressions, listing clicks, website visits, map directions, customer phone calls, and quote requests.")
    ]
)

# 8. craigslist-ads.html
build_service_page(
    filename="craigslist-ads.html",
    title="Craigslist Ads Management Services",
    eyebrow="Craigslist Advertising Management",
    hero_desc="Reach high-intent local customers looking for your services. Post optimized, high-converting classified ads that drive phone calls and lead conversions.",
    hero_bullets=[
        "Craigslist Ad Creation", "Local Market Targeting", "Lead Generation Campaigns", 
        "Classified Copywriting", "Category Optimization", "Listing Performance Tracking",
        "Competitor Profile Analysis", "Ongoing Ad Posting Optimization", "Phone Call Tracking Setup",
        "Spam Filter Avoidance Strategies"
    ],
    what_is_desc="What Are Craigslist Ads Management Services?",
    what_is_cards=[
        ("Craigslist Ads", "Paid and organic classified listing promotions designed specifically to drive local calls, inquiries, and customer leads from Craigslist boards."),
        ("Generate Direct Calls", "Attract local buyers searching for home services, contracting, real estate, or jobs near them."),
        ("High ROI, Low Cost", "Maximize business leads using Craigslist's low platform listing fees and direct-response formats.")
    ],
    benefits_cards=[
        ("Reach Local Customers Fast", "Connect directly with local users looking for immediate home services, rentals, or sales in your area."),
        ("High Direct-Response Intent", "Yelp and Craigslist users typically have immediate purchase intent, driving faster phone call conversions."),
        ("Highly Cost-Effective", "Craigslist ads cost significantly less than Google Search click bids, delivering high lead ROI."),
        ("Target Specific Categories", "Optimize your ad placement in target classified boards (Services, Housing, Jobs, Sale)."),
        ("Local Radius Targeting", "Target individual cities, boroughs, suburbs, and neighborhoods matching your service area."),
        ("Avoid Spam & flagging Filters", "Our posting schedule, layout formatting, and unique IPs ensure your ads remain visible and active.")
    ],
    services_cards=[
        ("Craigslist Ad Creation", "Draft engaging, high-converting ad layouts with clear titles, features, and phone call hooks."),
        ("Local Post Management", "Manage posting schedules, renewals, and re-posts to ensure your ad stays near the top of lists."),
        ("Category Placement Optimization", "Analyze which service/product categories generate the highest call volume for your business."),
        ("Ad Graphic Styling", "Design visual banners and image headers to make your classified ad stand out in search grids."),
        ("Call Tracking Setup", "Set up unique trackable phone numbers to monitor Craigslist campaign ROI accurately."),
        ("Classified Competitor Tracking", "Track competitor posting frequencies, pricing tiers, and outrank their listings.")
    ],
    process_steps=[
        ("Classified Market Review", "We audit your service area demand, keyword searches, and analyze competitor classified ads on Craigslist."),
        ("Ad Copywriting & Image Design", "Write persuasive ad copy with bold headers, list features, and design high-contrast banner graphics."),
        ("Ad Account Setup & Verify", "Configure and verify your Craigslist business billing profiles and regional settings."),
        ("Campaign Posting & Launch", "Publish optimized classified listings in target categories during peak user traffic hours."),
        ("Lead Tracking & Renewal", "Track incoming calls, manage ad renewals, re-posts, and resolve listing flags."),
        ("Performance reporting", "Deliver monthly campaign reports tracking post count, renew intervals, calls, and CPA metrics.")
    ],
    why_cards=[
        ("Classified Marketing Experts", "We understand Craigslist posting guidelines, category rules, and listing structures."),
        ("Flagging & Spam Shielding", "We use white-hat posting methods to keep your listings active and avoid spam filters."),
        ("Call Generation Focus", "We write ads and headers designed specifically to make local customers pick up the phone and call."),
        ("Unique Regional Targeting", "Target multiple towns and neighborhoods matching your service crews' dispatch radius."),
        ("Transparent Local Reporting", "Detailed reports tracking Craigslist post visibility, phone calls, and cost-per-lead."),
        ("Affordable B2C Scaling", "Highly cost-effective classified strategy perfect for home services, moving, junk removal, and local trades.")
    ],
    faqs=[
        ("What is Craigslist advertising?", "It is the process of using Craigslist's classified directory to promote services, products, or job openings to local search audiences."),
        ("Are Craigslist ads good for lead generation?", "Yes, particularly for home services, local businesses, housing, and trades. Craigslist users are typically looking to book services immediately."),
        ("How much does it cost to post?", "Craigslist charges a small flat fee (usually $5) per listing in commercial categories. This makes it highly cost-effective compared to standard PPC bids."),
        ("How do you prevent ads from being flagged?", "We write unique copy, follow Craigslist guidelines, vary images, and schedule postings systematically to avoid automated spam filters."),
        ("Do you provide trackable phone numbers?", "Yes, we can set up unique, trackable phone lines to isolate and count the exact number of calls coming from your Craigslist ads.")
    ]
)

# 9. x-ads.html
build_service_page(
    filename="x-ads.html",
    title="X Ads Management Services",
    eyebrow="X Advertising Management",
    hero_desc="Reach targeted audiences, expand your brand visibility, and drive meaningful conversions with expert X (Twitter) advertising campaigns.",
    hero_bullets=[
        "X Ads Campaign Management", "Audience Targeting & Segmentation", "Promoted Posts & Video Ads", 
        "Lead Generation Campaigns", "Brand Awareness Advertising", "X Retargeting Campaign Setup",
        "Conversion Optimization", "X Analytics & Reporting", "Keyword & Interest Matching",
        "Trending Topic Ad Placements"
    ],
    what_is_desc="What Are X Ads Management Services?",
    what_is_cards=[
        ("X Ads (Twitter)", "Paid advertising campaigns run on the X platform, allowing brands to promote posts, videos, accounts, or trends to target users."),
        ("Connect with Trends", "Deliver your ads directly alongside trending topics, hashtags, and real-time news discussions."),
        ("Scale B2B & B2C Leads", "Target users based on industry conversations, follow graphs, interest groups, and demographics.")
    ],
    benefits_cards=[
        ("Target Active Conversations", "Connect with users actively discussing topics, news, and brand categories in real-time."),
        ("Expand Brand Visibility", "Promote your best content, product launches, or event invites to target audiences."),
        ("Generate Quality Leads", "Drive clicks, signups, app installs, and customer inquiries with conversion-focused ad formats."),
        ("Target Competitor Followers", "Target users who follow specific competitor profiles, industry influencers, or media outlets."),
        ("Support Real-Time Marketing", "Sync ads with live events, trending hashtags, conferences, and viral topics."),
        ("Track Performance Metrics", "Monitor ad reach, click-through-rates, followers gained, and cost-per-lead conversion ROI.")
    ],
    services_cards=[
        ("X Campaign Configuration", "Design, launch, and manage targeted campaigns using promoted posts, follow ads, or video cards."),
        ("Targeting & Segmentation", "Target audiences based on follower lookalikes, interest themes, search keywords, and location."),
        ("Ad Copywriting & Creative", "Write engaging, punchy copy and design eye-catching graphic headers and video ad clips."),
        ("App Install Campaigns", "Promote mobile app downloads directly in user timelines with click-to-install ad cards."),
        ("X Pixel & Conversion Tracking", "Install X Pixel on your website to track clicks, signups, leads, and store purchases."),
        ("Performance Analytics", "Monitor campaign metrics, run creative variations tests, and deliver monthly data reports.")
    ],
    process_steps=[
        ("Brand & Audience Analysis", "We audit your business profile, target demographics, and search for relevant conversations on X."),
        ("Ad Campaign Architecture", "Define campaign objectives (leads, views, clicks), budget limits, and configure targeting matrices."),
        ("Creative Asset Design", "Write clear, high-CTR copy variations, design graphic templates, and edit video ad components."),
        ("Tracking Pixel Setup", "Set up X Pixel events to track website conversions and map user landing page pathways."),
        ("Campaign Launch", "Publish promoted posts, bids, and targeting groups, pushing the campaign live during peak hours."),
        ("Weekly Optimization", "Review ad frequency, exclude low-performing target groups, optimize bids, and deliver reports.")
    ],
    why_cards=[
        ("Social Advertising Specialists", "We understand X's real-time ad platform, bid algorithms, and copy formatting guidelines."),
        ("Real-Time Conversation Mapping", "We target conversations, topics, and competitor profiles to capture high-interest leads."),
        ("Creative Design & Copywriting", "Our designers write scroll-stopping, concise copy and headers designed specifically to convert X users."),
        ("Conversion Rate Focus", "We configure landing pages and forms to ensure ad clicks translate into actual customer acquisitions."),
        ("Transparent reporting", "Detailed reports tracking campaign reach, cost-per-click, follow growth, and conversions."),
        ("Flexible Budget Scaling", "Advertising strategies built to scale from small testing budgets up to large corporate campaigns.")
    ],
    faqs=[
        ("What are X Ads?", "X Ads are paid advertising formats (promoted posts, videos, trends) that help brands reach targeted user groups on X (Twitter)."),
        ("How does X ad targeting work?", "X allows targeting by location, language, device, interests, search keywords, conversation topics, and follower lookalikes."),
        ("Can X ads generate B2B leads?", "Yes, X is a major platform for tech, finance, software, and marketing discussions, making it effective for targeting B2B decision-makers."),
        ("Do you design the ad graphics?", "Yes. We handle copy editing, graphic design, and video formatting for all ads in your campaign."),
        ("How quickly can we launch a campaign?", "From initial audit, copy design, and setup, we can launch your X ad campaign in 5 to 7 business days.")
    ]
)

# 10. linkedin-ads.html
build_service_page(
    filename="linkedin-ads.html",
    title="LinkedIn Ads Management Services",
    eyebrow="LinkedIn B2B Advertising",
    hero_desc="Reach key B2B decision-makers, generate high-quality B2B leads, and grow your sales pipeline with strategic LinkedIn Ads campaigns.",
    hero_bullets=[
        "B2B Lead Generation Campaigns", "LinkedIn Audience Targeting", "Sponsored Content Campaigns", 
        "LinkedIn Lead Gen Forms", "Brand Awareness Advertising", "Account-Based Marketing (ABM)",
        "Conversion Optimization", "LinkedIn Insight Tag Setup", "Message & Conversation Ads", 
        "Campaign Analytics & Reports"
    ],
    what_is_desc="What Are LinkedIn Ads Management Services?",
    what_is_cards=[
        ("LinkedIn Ads", "Paid advertising campaigns run on LinkedIn to target professional B2B audiences, executives, founders, and industry decision-makers."),
        ("Target B2B Decision-Makers", "Filter audiences by job title, company size, seniority, industry classification, and skills."),
        ("Generate High-Value Leads", "Capture professional leads in-feed using auto-filled LinkedIn Lead Gen Forms that maximize conversion rates.")
    ],
    benefits_cards=[
        ("Reach Key B2B Decision-Makers", "Target corporate directors, founders, CEOs, managers, and business professionals directly."),
        ("Generate High-Quality Leads", "Connect with prospective clients who are actively looking for B2B services and business software."),
        ("Build Trust and Brand Authority", "Build trust and credibility by displaying your B2B case studies and reviews in timelines."),
        ("Target Specific Companies (ABM)", "Upload target client lists to run customized Account-Based Marketing ad campaigns."),
        ("Support Long Sales Pipelines", "Maintain brand awareness and touchpoints for complex enterprise corporate sales."),
        ("Maximize B2B Ad Spend ROI", "Focus your budget strictly on high-value business profiles, avoiding consumer ad waste.")
    ],
    services_cards=[
        ("Sponsored Content Setup", "Launch and manage image, video, and carousel ads directly in the main LinkedIn feed."),
        ("Lead Gen Forms Setup", "Create custom forms that pre-fill with a user's professional profile data (name, company, email)."),
        ("Message & Conversation Ads", "Send direct, personalized B2B messages to target prospects' LinkedIn message inboxes."),
        ("Account-Based Marketing (ABM)", "Configure campaigns to target key decision-makers at specific target list companies."),
        ("Insight Tag Integration", "Install LinkedIn Insight Tag on your site to track conversions, page visits, and demographics."),
        ("B2B Copywriting & Design", "Write professional ad copy and design graphic templates aligned with B2B styles.")
    ],
    process_steps=[
        ("B2B Business & Competitor Audit", "We audit your service profiles, target client personas, and analyze competitor LinkedIn ad positioning."),
        ("Targeting Matrix Development", "Build custom target segments combining job seniority, industry tags, company size, and list uploads."),
        ("Creative Asset Design", "Write professional copy, draft video scripts, and design graphic banners aligned with corporate styles."),
        ("Insight Tag Setup", "Configure conversion tracking pixels and map out lead funnel pages on your website."),
        ("Campaign Launch", "Configure bidding parameters (CPC/CPM), schedule campaigns, and push the B2B ads live."),
        ("Optimization & Reporting", "Analyze lead cost, refine target parameters, test new ad copy hooks, and deliver monthly reports.")
    ],
    why_cards=[
        ("B2B Marketing Experts", "We understand the B2B sales pipeline, professional copy hooks, and LinkedIn ad platform logic."),
        ("Advanced Profile Targeting", "We combine job titles, member skills, and company parameters to reach the exact buyer profile."),
        ("Lead Gen Form Specialists", "We optimize lead capture forms to maximize response rates and capture clean professional data."),
        ("Conversion Rate Focus", "Integrate LinkedIn ad traffic with optimized landing pages to turn clicks into sales calls."),
        ("Transparent reporting", "Detailed monthly reports tracking ad spend, clicks, form completions, cost-per-lead, and pipeline value."),
        ("Scalable B2B Scaling", "Flexible ad management structures configured to scale as your enterprise sales goals expand.")
    ],
    faqs=[
        ("What are LinkedIn Ads?", "LinkedIn Ads are paid campaigns that help businesses reach professionals and decision-makers on LinkedIn."),
        ("Are LinkedIn Ads good for B2B marketing?", "Yes. LinkedIn is one of the most effective platforms for B2B lead generation and professional networking."),
        ("Can LinkedIn Ads generate qualified leads?", "Absolutely. LinkedIn's advanced targeting helps reach highly relevant B2B audiences."),
        ("What industries benefit from LinkedIn Ads?", "SaaS, technology, healthcare, education, finance, consulting, recruitment, and professional services."),
        ("Do you provide LinkedIn Lead Gen campaigns?", "Yes. We create and manage LinkedIn Lead Gen Form campaigns to capture quality leads."),
        ("How quickly can LinkedIn Ads generate results?", "Most campaigns start generating visibility and leads within days of launch."),
        ("Do you provide campaign reports?", "Yes. We provide detailed reporting covering leads, engagement, clicks, and conversions.")
    ]
)

# ==========================================
# NEW ABOUT US PAGE GENERATOR
# ==========================================

# 1. Hero Section (Dark Charcoal Background)
hero_html = """
<section style="background-color: var(--dark-charcoal); color: white; padding: 100px 0;">
  <div class="container" style="text-align: center; max-width: 900px;">
    <span class="eyebrow-red">AI-Powered Digital Marketing Agency</span>
    <h1 style="font-size: 3.5rem; font-weight: bold; line-height: 1.1; margin: 1.5rem 0 2rem 0; color: white;">Driving Business Growth Through AI, Innovation & Proven Marketing Expertise</h1>
    <p style="font-size: 1.25rem; color: #ccc; line-height: 1.6; max-width: 800px; margin: 0 auto;">GBO helps businesses grow faster with AI-powered marketing strategies, data-driven decisions, and proven digital growth frameworks designed for today's search landscape.</p>
  </div>
</section>
"""

# 2. Our Story Section (Off-White Background)
story_html = """
<section style="background-color: var(--off-white); color: var(--dark-charcoal);">
  <div class="container" style="max-width: 900px;">
    <span class="eyebrow-red">Who We Are</span>
    <h2 class="section-h2" style="color: var(--dark-charcoal);">Built for the Future of Digital Marketing</h2>
    <div style="font-size: 1.1rem; line-height: 1.8; color: #333; display: flex; flex-direction: column; gap: 1.5rem;">
      <p>GBO was created to help businesses navigate a rapidly changing digital world where traditional marketing alone is no longer enough.</p>
      <p>With 5+ years of hands-on expertise in digital marketing, SEO, paid advertising, content strategy, social media marketing, and AI-driven growth solutions, we help businesses increase visibility, generate qualified leads, and achieve measurable growth.</p>
      <p>Today, search is evolving beyond Google. Customers are finding businesses through ChatGPT, Google AI Overviews, Gemini, Perplexity, voice assistants, social media platforms, and traditional search engines. That's why we combine Artificial Intelligence, human expertise, and performance marketing to help businesses stay ahead of competitors and remain visible wherever customers search.</p>
    </div>
  </div>
</section>
"""

# 3. Competitive Advantage Grid (Dark Charcoal Background)
comp_cards = [
    ("AI-Driven Marketing Approach", "We leverage Artificial Intelligence to uncover insights, identify opportunities, and improve marketing performance faster than traditional agencies."),
    ("Future-Ready Search Expertise", "Most agencies focus only on Google rankings. We optimize visibility across Google, AI Search, ChatGPT, Gemini, Perplexity, voice search, and emerging search platforms."),
    ("Results Over Vanity Metrics", "We focus on leads, conversions, revenue growth, and business impact—not just impressions and traffic."),
    ("Customized Growth Strategies", "Every business is unique. We build personalized marketing strategies based on your goals, industry, audience, and competition."),
    ("Full-Funnel Growth Thinking", "From awareness and visibility to conversion and customer retention, we optimize every stage of the customer journey."),
    ("Data-Driven Decision Making", "Every strategy is backed by analytics, user behavior, competitive intelligence, and performance data."),
    ("Transparent Communication", "No hidden processes. No confusing reports. Just clear insights, measurable progress, and honest communication.")
]

comp_cards_html = ""
# Top-left card (Card 1) is solid red
comp_cards_html += f"""
<div class="card-red">
  <h3 style="font-size: 1.35rem; font-weight: bold; margin-bottom: 1rem; color: white;">{comp_cards[0][0]}</h3>
  <p style="color: white; font-size: 0.95rem; line-height: 1.6;">{comp_cards[0][1]}</p>
</div>
"""
# Remaining 6 cards are dark gray
for title, text in comp_cards[1:]:
    comp_cards_html += f"""
    <div class="card-dark">
      <h3 style="font-size: 1.35rem; font-weight: bold; margin-bottom: 1rem; color: white;">{title}</h3>
      <p style="color: #aaa; font-size: 0.95rem; line-height: 1.6;">{text}</p>
    </div>
    """

comp_html = f"""
<section style="background-color: var(--dark-charcoal); color: white;">
  <div class="container">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 3.5rem auto;">
      <span class="eyebrow-red">Our Competitive Advantage</span>
      <h2 class="section-h2" style="color: white; margin-top: 0.5rem;">Why Businesses Choose GBO</h2>
    </div>
    <div class="grid-custom-7">
      {comp_cards_html}
    </div>
  </div>
</section>
"""

# 4. Our Expertise Grid (Off-White Background)
exp_cards = [
    ("5+ Years of Digital Marketing Experience", "Helping businesses grow through strategic digital marketing solutions."),
    ("Multi-Industry Expertise", "Experience working with healthcare, real estate, legal, eCommerce, home services, education, SaaS, technology, hospitality, and professional service businesses."),
    ("AI Search & SEO Specialists", "Expertise in SEO, GEO, AEO, Voice Search Optimization, Video SEO, and AI-powered search visibility."),
    ("Performance Marketing Experts", "Managing advertising campaigns across Google Ads, Meta Ads, LinkedIn Ads, YouTube Ads, Yelp Ads, and local advertising platforms."),
    ("Content & Brand Growth Specialists", "Creating content strategies designed to build authority, engagement, and long-term visibility.")
]

exp_cards_html = ""
# Top-left card (Card 1) is solid red
exp_cards_html += f"""
<div class="card-red">
  <h3 style="font-size: 1.35rem; font-weight: bold; margin-bottom: 1rem; color: white;">{exp_cards[0][0]}</h3>
  <p style="color: white; font-size: 0.95rem; line-height: 1.6;">{exp_cards[0][1]}</p>
</div>
"""
# Remaining 4 cards are white
for title, text in exp_cards[1:]:
    exp_cards_html += f"""
    <div class="card-light">
      <h3 style="font-size: 1.35rem; font-weight: bold; margin-bottom: 1rem; color: var(--dark-charcoal);">{title}</h3>
      <p style="color: #555; font-size: 0.95rem; line-height: 1.6;">{text}</p>
    </div>
    """

exp_html = f"""
<section style="background-color: var(--off-white); color: var(--dark-charcoal);">
  <div class="container">
    <div style="text-align: center; max-width: 800px; margin: 0 auto 3.5rem auto;">
      <span class="eyebrow-red">Experience That Delivers Results</span>
      <h2 class="section-h2" style="color: var(--dark-charcoal); margin-top: 0.5rem;">Proven Digital Marketing Expertise</h2>
    </div>
    <div class="grid-custom-5">
      {exp_cards_html}
    </div>
  </div>
</section>
"""

# 5. USP, Mission & Vision (Dark Charcoal Background)
usp_list = [
    "Google Search", "Google AI Overviews", "ChatGPT", "Gemini", 
    "Perplexity", "Voice Search", "YouTube Search", "Social Search Platforms"
]
usp_list_html = "".join([f"<li style='position: relative; padding-left: 1.75rem; margin-bottom: 0.5rem; color: #fff;'>✓ {item}</li>" for item in usp_list])

usp_mission_vision_html = f"""
<section style="background-color: var(--dark-charcoal); color: white;">
  <div class="container">
    <div class="grid-3">
      
      <!-- Column 1 (The USP) -->
      <div style="display: flex; flex-direction: column; justify-content: space-between;">
        <div>
          <span class="eyebrow-red">Why We're Different</span>
          <h3 style="font-size: 1.75rem; font-weight: bold; margin-bottom: 1rem; color: white;">The GBO Advantage</h3>
          <p style="color: #ccc; font-size: 0.95rem; margin-bottom: 1.5rem; line-height: 1.6;">Traditional Agencies Optimize for Rankings. GBO Optimizes for Visibility Everywhere. We help businesses get discovered across:</p>
          <ul style="list-style: none; padding: 0; margin-bottom: 1.5rem; display: grid; grid-template-columns: 1fr 1fr; gap: 0.5rem; font-size: 0.9rem;">
            {usp_list_html}
          </ul>
        </div>
        <p style="color: #aaa; font-size: 0.9rem; line-height: 1.6; border-top: 1px solid #444; padding-top: 1rem;">By combining AI-powered marketing, advanced SEO, paid advertising, content strategy, and conversion optimization, we help businesses build sustainable digital growth systems—not just marketing campaigns.</p>
      </div>
      
      <!-- Column 2 (Mission Card) -->
      <div class="card-dark" style="display: flex; flex-direction: column; justify-content: flex-start;">
        <span class="eyebrow-red">Our Purpose</span>
        <h3 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 1rem; color: white;">Helping Businesses Grow Smarter</h3>
        <p style="color: #ccc; line-height: 1.7;">Our mission is to empower businesses with innovative, AI-driven marketing strategies that increase visibility, generate opportunities, and create sustainable long-term growth.</p>
      </div>
      
      <!-- Column 3 (Vision Card) -->
      <div class="card-dark" style="display: flex; flex-direction: column; justify-content: flex-start;">
        <span class="eyebrow-red">Where We're Going</span>
        <h3 style="font-size: 1.5rem; font-weight: bold; margin-bottom: 1rem; color: white;">Building the Future of Search & Marketing</h3>
        <p style="color: #ccc; line-height: 1.7;">Our vision is to become the most trusted AI-powered digital marketing agency helping businesses succeed across traditional search engines, AI platforms, social media, and emerging digital channels.</p>
      </div>
      
    </div>
  </div>
</section>
"""

# 6. Client Success & Trust (Off-White Background)
trust_list = [
    "Increased Online Visibility", "Better Search Rankings", "Stronger Brand Presence", 
    "Higher Quality Leads", "Improved Conversion Rates", "Sustainable Business Growth"
]
trust_list_html = "".join([f"<li style='position: relative; padding-left: 1.75rem; margin-bottom: 0.75rem; color: var(--dark-charcoal); font-weight: 500;'>✓ {item}</li>" for item in trust_list])

trust_html = f"""
<section style="background-color: var(--off-white); color: var(--dark-charcoal);">
  <div class="container grid-2">
    <div>
      <span class="eyebrow-red">What Our Clients Say</span>
      <h2 class="section-h2" style="color: var(--dark-charcoal); margin-top: 0.5rem;">Trusted by Businesses Across Industries</h2>
      <p style="color: #555; margin-bottom: 2rem; font-size: 1.05rem;">Businesses choose GBO because we focus on outcomes that matter:</p>
      <ul style="list-style: none; padding: 0;">
        {trust_list_html}
      </ul>
    </div>
    <div style="display: flex; flex-direction: column; gap: 1.5rem; justify-content: center;">
      <div class="card-light" style="border-left: 4px solid var(--bright-red); box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
        <p style="font-style: italic; font-size: 1.1rem; color: var(--dark-charcoal); line-height: 1.6;">"GBO helped us improve our visibility, generate more qualified leads, and create a clear digital growth strategy that delivered measurable results."</p>
      </div>
      <div class="card-light" style="border-left: 4px solid var(--bright-red); box-shadow: 0 4px 6px rgba(0,0,0,0.02);">
        <p style="font-style: italic; font-size: 1.1rem; color: var(--dark-charcoal); line-height: 1.6;">"Their AI-driven approach and commitment to transparency made them feel like an extension of our team rather than just another agency."</p>
      </div>
    </div>
  </div>
</section>
"""

# 7. Final CTA Banner (Solid Bright Red Background)
cta_html = """
<section style="background-color: var(--bright-red); color: white; text-align: center; padding: 100px 0;">
  <div class="container" style="max-width: 800px;">
    <span class="eyebrow-white" style="font-size: 1rem; margin-bottom: 1rem;">Ready to Grow?</span>
    <h2 style="font-size: 2.75rem; font-weight: bold; line-height: 1.2; margin-bottom: 1.5rem; color: white;">Partner with an AI-Powered Marketing Agency Built for the Future</h2>
    <p style="font-size: 1.2rem; opacity: 0.9; margin-bottom: 2.5rem; line-height: 1.6;">Whether you're looking to improve visibility, generate more leads, or stay ahead in the age of AI search, GBO is ready to help.</p>
    <a href="free-consultation.html" class="btn-primary" style="background-color: white; color: var(--dark-charcoal); font-size: 1.05rem; padding: 1rem 2.5rem;">GET YOUR FREE GROWTH STRATEGY CONSULTATION TODAY</a>
  </div>
</section>
"""

# 8. FAQ Section (Off-White Background)
faqs = [
    ("What makes GBO different from other digital marketing agencies?", "GBO combines AI-powered marketing, future-ready search optimization, and data-driven growth strategies to help businesses stay ahead of evolving customer behavior."),
    ("How much experience does GBO have?", "Our team brings 5+ years of experience across SEO, paid advertising, content marketing, social media, AI search optimization, and performance marketing."),
    ("Does GBO work with businesses in different industries?", "Yes. We work with healthcare, legal, real estate, eCommerce, SaaS, education, home services, hospitality, and many other industries."),
    ("What is AI-powered marketing?", "AI-powered marketing uses artificial intelligence, automation, and data insights to improve targeting, content strategies, customer engagement, and campaign performance."),
    ("Does GBO only focus on Google rankings?", "No. We help businesses improve visibility across Google Search, Google AI Overviews, ChatGPT, Gemini, Perplexity, voice search, YouTube, and social platforms."),
    ("Is GBO suitable for small businesses and startups?", "Absolutely. We create scalable strategies designed for startups, local businesses, growing brands, and enterprise organizations."),
    ("How does GBO measure success?", "We focus on visibility, qualified leads, conversions, customer acquisition, and measurable business growth."),
    ("How can I get started with GBO?", "Simply schedule a free consultation, and we'll create a customized growth strategy tailored to your business goals.")
]

faqs_html = ""
for idx, (q, a) in enumerate(faqs):
    num = idx + 1
    faqs_html += f"""
    <div class="faq-item">
      <div class="faq-q">
        <div style="display: flex; align-items: center;">
          <span class="faq-num">{num}</span>
          <span>{q}</span>
        </div>
        <span class="faq-arrow">&#9662;</span>
      </div>
      <div class="faq-a">
        <p>{a}</p>
      </div>
    </div>
    """

faq_html = f"""
<section style="background-color: var(--off-white); color: var(--dark-charcoal); border-top: 1px solid #e0e0e0;">
  <div class="container" style="max-width: 850px;">
    <div style="text-align: center; margin-bottom: 3.5rem;">
      <span class="eyebrow-red">Frequently Asked Questions</span>
      <h2 class="section-title" style="margin-top: 0.5rem; color: var(--dark-charcoal); margin-bottom: 0;">Common Questions About GBO</h2>
    </div>
    <div class="faq-list">
      {faqs_html}
    </div>
  </div>
</section>
"""

# Combine into full page HTML for about-us.html
about_us_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>About Us - GBO</title>
  <link rel="stylesheet" href="style.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
  {styles}
</head>
<body>
  {dummy_header}
  {hero_html}
  {story_html}
  {comp_html}
  {exp_html}
  {usp_mission_vision_html}
  {trust_html}
  {cta_html}
  {faq_html}
  {dummy_footer}
</body>
</html>"""

with open(os.path.join(out_dir, 'about-us.html'), 'w', encoding='utf-8') as f:
    f.write(about_us_html)
print("about-us.html generated successfully.")

# Map this new page in index.html navbar
index_path = os.path.join(out_dir, 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    index_html = f.read()

index_html = index_html.replace('href="about.html"', 'href="about-us.html"')
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(index_html)
print("Mapped about-us.html inside index.html")
