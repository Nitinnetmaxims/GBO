import os
import shutil

css_file = "fonts/local-fonts.css"
if os.path.exists(css_file):
    with open(css_file, "r") as f:
        content = f.read()
    
    # Remove Switzer-Variable @font-face block from local-fonts.css
    import re
    content = re.sub(r"@font-face\s*\{\s*font-family:\s*'Switzer-Variable';.*?\}", "", content, flags=re.DOTALL)
    
    with open(css_file, "w") as f:
        f.write(content.strip())

# Re-zip the fonts folder
shutil.make_archive('fonts', 'zip', 'fonts')
