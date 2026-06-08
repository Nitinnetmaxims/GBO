import re

with open('style.css', 'r') as f:
    css = f.read()

# Replace main .hero-form (first occurrence)
new_hero_form = """.hero-form {
  display: flex;
  align-items: center;
  gap: var(--space-3);
  max-width: 580px;
}"""
css = re.sub(r'\.hero-form\s*\{[^}]*\}', new_hero_form, css, count=1)

# Replace main .hero-form input (first occurrence)
new_input = """.hero-form input {
  flex-grow: 1;
  background-color: rgba(255, 255, 255, 0.07);
  border: 1px solid rgba(255, 255, 255, 0.15);
  color: var(--color-pure-white);
  height: 44px;
  padding: 0 1rem;
  box-sizing: border-box;
}"""
css = re.sub(r'\.hero-form\s+input\s*\{[^}]*\}', new_input, css, count=1)

# Add .hero-form .btn if not exists
btn_rule = """.hero-form .btn {
  white-space: nowrap;
  height: 44px;
  padding: 0 1.5rem;
  box-sizing: border-box;
}"""

if '.hero-form .btn' not in css:
    css = css.replace(new_input, new_input + "\n\n" + btn_rule, 1)

with open('style.css', 'w') as f:
    f.write(css)

print("Form styles updated successfully.")
