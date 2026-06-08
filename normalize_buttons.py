with open('style.css', 'r') as f:
    css = f.read()

# The standard .btn padding is 0.75rem top/bottom, 1rem font-size, normal line-height. This computes to roughly 52px.
# We will append a normalizing rule at the end of the file.

normalization_rule = """
/* ==========================================================================
   GLOBAL BUTTON HEIGHT NORMALIZATION
   ========================================================================== */
.btn,
.hero-form .btn,
.cta-form-btn,
.new-pricing-btn,
.featured-btn,
.pricing-card .btn {
  height: 54px !important;
  padding-top: 0 !important;
  padding-bottom: 0 !important;
  display: inline-flex !important;
  align-items: center !important;
  justify-content: center !important;
  box-sizing: border-box !important;
}

.hero-form input {
  height: 54px !important; /* Keep input in sync with the new global button height */
}
"""

if "GLOBAL BUTTON HEIGHT NORMALIZATION" not in css:
    with open('style.css', 'a') as f:
        f.write(normalization_rule)

print("Button heights normalized globally.")
