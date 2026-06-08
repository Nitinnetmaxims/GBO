with open('style.css', 'r') as f:
    css = f.read()

# We need to remove everything from "/* ==========================================================================\n   Premium UI/UX Components\n   ========================================================================== */"
# to the end of the file.

marker = "/* ==========================================================================\n   Premium UI/UX Components\n   ========================================================================== */"

if marker in css:
    css = css[:css.find(marker)].strip() + "\n"
    with open('style.css', 'w') as f:
        f.write(css)
    print("Reverted Premium CSS.")
else:
    print("Marker not found, assuming already clean.")
