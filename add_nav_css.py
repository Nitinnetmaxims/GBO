with open('style.css', 'r') as f:
    css = f.read()

# CSS for Dropdown navigation
dropdown_css = """
/* Dropdown Navigation */
.nav-item {
  position: relative;
}

.nav-item > a {
  display: flex;
  align-items: center;
  gap: 0.25rem;
}

.nav-item > a::after {
  content: "▾";
  font-size: 0.8rem;
  transition: transform 0.2s ease;
}

.nav-item:hover > a::after {
  transform: rotate(180deg);
}

.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  background-color: var(--color-pure-white);
  min-width: 240px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  border-radius: var(--border-radius-sm);
  padding: 0.5rem 0;
  opacity: 0;
  visibility: hidden;
  transform: translateY(10px);
  transition: all 0.2s ease;
  z-index: 200;
  display: flex;
  flex-direction: column;
}

.nav-item:hover > .dropdown-menu {
  opacity: 1;
  visibility: visible;
  transform: translateY(0);
}

.dropdown-menu a {
  color: var(--color-charcoal);
  padding: 0.75rem 1.5rem;
  font-size: var(--fs-p3);
  font-weight: 500;
  transition: background-color 0.2s ease, color 0.2s ease;
  text-decoration: none;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.dropdown-menu a:hover {
  background-color: rgba(255, 62, 58, 0.05); /* very light red */
  color: var(--color-fire-engine-red);
}

/* Nested Dropdowns (e.g. SMO Packages) */
.dropdown-item-nested {
  position: relative;
}

.dropdown-item-nested > a::after {
  content: "▸";
  font-size: 0.8rem;
}

.nested-dropdown-menu {
  position: absolute;
  top: 0;
  left: 100%;
  background-color: var(--color-pure-white);
  min-width: 220px;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
  border-radius: var(--border-radius-sm);
  padding: 0.5rem 0;
  opacity: 0;
  visibility: hidden;
  transform: translateX(10px);
  transition: all 0.2s ease;
  z-index: 201;
}

.dropdown-item-nested:hover > .nested-dropdown-menu {
  opacity: 1;
  visibility: visible;
  transform: translateX(0);
}
"""

if "/* Dropdown Navigation */" not in css:
    # insert before /* Hero Section */
    css = css.replace("/* Hero Section */", dropdown_css + "\n/* Hero Section */")
    with open('style.css', 'w') as f:
        f.write(css)
    print("Dropdown CSS added.")
else:
    print("Dropdown CSS already exists.")

