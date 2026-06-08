import os
import re
import urllib.request
import zipfile
import shutil
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

fonts_dir = "fonts"
os.makedirs(fonts_dir, exist_ok=True)

# Move existing font
if os.path.exists("Font/Switzer-Variable.ttf"):
    shutil.copy("Font/Switzer-Variable.ttf", os.path.join(fonts_dir, "Switzer-Variable.ttf"))

# Download DM Sans (woff2) by mocking a modern Chrome User-Agent
url = "https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,100..1000;1,9..40,100..1000&display=swap"
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
}
req = urllib.request.Request(url, headers=headers)
try:
    with urllib.request.urlopen(req) as response:
        css = response.read().decode('utf-8')

    urls = re.findall(r'url\((.*?)\)', css)
    # The CSS will likely have .woff2
    for i, font_url in enumerate(set(urls)):
        ext = font_url.split('.')[-1]
        filename = f"dm-sans-{i}.{ext}"
        filepath = os.path.join(fonts_dir, filename)
        urllib.request.urlretrieve(font_url, filepath)
        css = css.replace(font_url, f"{filename}") # the css is local, so paths are relative to fonts/

    # append Switzer-Variable to the sample css
    switzer_css = """
@font-face {
  font-family: 'Switzer-Variable';
  src: url('Switzer-Variable.ttf') format('truetype');
  font-weight: 100 900;
  font-style: normal;
  font-display: swap;
}
"""
    with open(os.path.join(fonts_dir, "local-fonts.css"), "w") as f:
        f.write(css + "\n" + switzer_css)

    # Zip the folder
    shutil.make_archive('fonts', 'zip', fonts_dir)
    print("Success: Fonts downloaded and packaged in fonts.zip")
except Exception as e:
    print("Error:", e)
