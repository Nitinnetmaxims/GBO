import re

# 1. Update index.html
with open('index.html', 'r') as f:
    html = f.read()

svg_icon = '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="6 9 12 15 18 9"></polyline></svg>'
html = html.replace('<span class="faq-icon">+</span>', f'<span class="faq-icon">{svg_icon}</span>')

with open('index.html', 'w') as f:
    f.write(html)

# 2. Update style.css
with open('style.css', 'r') as f:
    css = f.read()

# Replace .faq-list
new_faq_list = """.faq-list {
  max-width: 900px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
}"""
css = re.sub(r'\.faq-list\s*\{[^}]*\}', new_faq_list, css)

# Replace .faq-item
new_faq_item = """.faq-item {
  background-color: transparent;
  border-bottom: 1px dashed rgba(0,0,0,0.15);
  overflow: hidden;
  transition: all var(--duration-base) var(--ease-standard);
}

.faq-item:first-child {
  border-top: 1px dashed rgba(0,0,0,0.15);
}"""
css = re.sub(r'\.faq-item\s*\{[^}]*\}', new_faq_item, css)

# Replace .faq-question-btn
new_btn = """.faq-question-btn {
  width: 100%;
  background: none;
  border: none;
  padding: var(--space-6) 0;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: var(--font-body);
  font-size: 1.15rem;
  font-weight: 500;
  text-align: left;
  cursor: pointer;
  color: var(--color-charcoal);
  transition: color var(--duration-fast);
}"""
css = re.sub(r'\.faq-question-btn\s*\{[^}]*\}', new_btn, css)

# Replace .faq-icon
new_icon = """.faq-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  transition: transform 0.3s ease, color 0.3s ease;
  color: #888;
}"""
css = re.sub(r'\.faq-icon\s*\{[^}]*\}', new_icon, css)

# Replace active icon
new_active_icon = """.faq-item.active .faq-icon {
  transform: rotate(-180deg);
  color: var(--color-fire-engine-red);
}"""
css = re.sub(r'\.faq-item\.active\s*\.faq-icon\s*\{[^}]*\}', new_active_icon, css)

# Replace .faq-answer
new_answer = """.faq-answer {
  max-height: 0;
  overflow: hidden;
  transition: max-height var(--duration-base) var(--ease-standard), padding var(--duration-base);
  padding: 0 2rem 0 0;
  font-size: 1.05rem;
  color: var(--color-light-gray);
  line-height: 1.6;
}"""
css = re.sub(r'\.faq-answer\s*\{[^}]*\}', new_answer, css)

# Replace active answer
new_active_answer = """.faq-item.active .faq-answer {
  padding: 0 2rem var(--space-6) 0;
}"""
css = re.sub(r'\.faq-item\.active\s*\.faq-answer\s*\{[^}]*\}', new_active_answer, css)

with open('style.css', 'w') as f:
    f.write(css)

print("Updates complete.")
