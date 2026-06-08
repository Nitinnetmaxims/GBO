import os

with open('style.css', 'a') as f:
    f.write("""
/* ==========================================================================
   Premium UI/UX Components
   ========================================================================== */

/* Inner Page Dynamic Hero */
.dynamic-hero {
  background-color: var(--color-charcoal-dark);
  color: var(--color-pure-white);
  padding: 8rem 0 6rem;
  text-align: center;
  position: relative;
  overflow: hidden;
}

.dynamic-hero::after {
  content: '';
  position: absolute;
  top: -50%; left: -50%; width: 200%; height: 200%;
  background: radial-gradient(circle at center, rgba(255, 62, 58, 0.05) 0%, transparent 60%);
  pointer-events: none;
}

.hero-badge-inner {
  display: inline-block;
  background-color: rgba(255, 62, 58, 0.1);
  color: var(--color-fire-engine-red);
  padding: 0.5rem 1rem;
  border-radius: 2rem;
  font-size: var(--fs-small);
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 1.5rem;
}

.dynamic-hero h1 {
  font-size: clamp(2.5rem, 5vw, 4rem);
  line-height: 1.1;
  margin-bottom: 1.5rem;
  font-weight: 800;
  letter-spacing: -0.02em;
}

.dynamic-hero p {
  font-size: var(--fs-p1);
  color: rgba(255, 255, 255, 0.7);
  max-width: 800px;
  margin: 0 auto 2rem;
  line-height: 1.6;
}

/* Bento Grid System */
.bento-section {
  padding: 6rem 0;
  background-color: var(--color-warm-white);
}

.bento-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 3rem;
}

.bento-card {
  background-color: var(--color-pure-white);
  border-radius: var(--border-radius-lg);
  padding: 2.5rem;
  box-shadow: 0 10px 30px rgba(0,0,0,0.03);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  border: 1px solid rgba(0,0,0,0.02);
  display: flex;
  flex-direction: column;
  height: 100%;
}

.bento-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 40px rgba(0,0,0,0.08);
}

.bento-icon {
  width: 50px;
  height: 50px;
  background-color: rgba(255, 62, 58, 0.1);
  color: var(--color-fire-engine-red);
  border-radius: var(--border-radius-sm);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: bold;
  margin-bottom: 1.5rem;
}

.bento-card h3 {
  font-size: var(--fs-h4);
  margin-bottom: 1rem;
  color: var(--color-charcoal);
}

.bento-card p {
  color: var(--color-cool-gray);
  line-height: 1.6;
  font-size: var(--fs-p2);
  margin-bottom: 0;
}

/* Split-Screen Layouts */
.split-section {
  padding: 6rem 0;
  background-color: var(--color-pure-white);
}

.split-section:nth-child(even) {
  background-color: var(--color-warm-white);
}

.split-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
}

.split-reverse .split-content {
  order: 2;
}

.split-reverse .split-visual {
  order: 1;
}

.split-content h2 {
  font-size: var(--fs-h2);
  margin-bottom: 1.5rem;
  color: var(--color-charcoal);
}

.split-content p {
  font-size: var(--fs-p1);
  color: var(--color-cool-gray);
  line-height: 1.7;
  margin-bottom: 2rem;
}

.split-list {
  list-style: none;
  padding: 0;
  margin: 0 0 2rem 0;
}

.split-list li {
  position: relative;
  padding-left: 2rem;
  margin-bottom: 1rem;
  font-size: var(--fs-p2);
  color: var(--color-charcoal);
  font-weight: 500;
}

.split-list li::before {
  content: '✓';
  position: absolute;
  left: 0;
  color: var(--color-fire-engine-red);
  font-weight: bold;
}

.split-visual {
  background-color: var(--color-warm-white);
  border-radius: var(--border-radius-lg);
  aspect-ratio: 4/3;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  box-shadow: 0 20px 50px rgba(0,0,0,0.05);
}

.split-visual img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.split-visual:hover img {
  transform: scale(1.05);
}

/* Premium Pricing Matrices */
.premium-pricing-section {
  padding: 6rem 0;
  background-color: var(--color-charcoal-dark);
  color: var(--color-pure-white);
}

.pricing-header {
  text-align: center;
  margin-bottom: 4rem;
}

.premium-pricing-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
  align-items: flex-start;
}

.premium-pricing-card {
  background-color: var(--color-charcoal);
  border-radius: var(--border-radius-lg);
  padding: 2.5rem;
  border: 1px solid rgba(255,255,255,0.05);
  position: relative;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.premium-pricing-card:hover {
  transform: translateY(-10px);
  box-shadow: 0 20px 40px rgba(0,0,0,0.2);
  border-color: rgba(255, 62, 58, 0.3);
}

.premium-pricing-card.popular {
  background-color: var(--color-pure-white);
  color: var(--color-charcoal);
  transform: scale(1.05);
  z-index: 10;
  border: 2px solid var(--color-fire-engine-red);
}

.premium-pricing-card.popular:hover {
  transform: scale(1.05) translateY(-10px);
}

.popular-badge {
  position: absolute;
  top: -15px;
  left: 50%;
  transform: translateX(-50%);
  background-color: var(--color-fire-engine-red);
  color: var(--color-pure-white);
  padding: 0.5rem 1.5rem;
  border-radius: 2rem;
  font-size: var(--fs-small);
  font-weight: bold;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  box-shadow: 0 5px 15px rgba(255, 62, 58, 0.4);
}

.pricing-title {
  font-size: var(--fs-h4);
  font-weight: 700;
  margin-bottom: 1rem;
}

.pricing-price {
  font-size: 3rem;
  font-weight: 900;
  margin-bottom: 1rem;
  line-height: 1;
}

.pricing-price span {
  font-size: var(--fs-p1);
  font-weight: 500;
  opacity: 0.7;
}

.pricing-features {
  list-style: none;
  padding: 0;
  margin: 2rem 0;
  border-top: 1px solid rgba(255,255,255,0.1);
  padding-top: 2rem;
}

.premium-pricing-card.popular .pricing-features {
  border-top-color: rgba(0,0,0,0.1);
}

.pricing-features li {
  margin-bottom: 1rem;
  font-size: var(--fs-p2);
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
}

.pricing-features li::before {
  content: '✓';
  color: var(--color-fire-engine-red);
  font-weight: bold;
}

/* Responsive adjustments */
@media (max-width: 992px) {
  .split-grid {
    grid-template-columns: 1fr;
    gap: 3rem;
  }
  .split-reverse .split-content {
    order: 1;
  }
  .split-reverse .split-visual {
    order: 2;
  }
  .premium-pricing-card.popular {
    transform: none;
  }
  .premium-pricing-card.popular:hover {
    transform: translateY(-5px);
  }
}
""")
print("Premium CSS added.")
