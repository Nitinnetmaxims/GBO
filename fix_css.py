with open('style.css', 'r') as f:
    content = f.read()

# The top of the file was corrupted by removing :root { ...
# Let's fix it by replacing the top part up to --color-maroon with the correct lines.

correct_top = """@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&display=swap');

:root {
  /* Color Palette */
  --color-fire-engine-red: #BB080B;
  --color-maroon: #A10709;"""

# Find --color-maroon and replace everything before it
import re
content = re.sub(r"^.*?--color-maroon: #A10709;", correct_top, content, flags=re.DOTALL)

with open('style.css', 'w') as f:
    f.write(content)
