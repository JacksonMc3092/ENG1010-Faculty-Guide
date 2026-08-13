from pathlib import Path
from bs4 import BeautifulSoup

css_path = Path('assets/faculty-guide.css')
css = css_path.read_text(encoding='utf-8')
marker = '/* FINAL PUBLICATION POLISH */'
if marker not in css:
    css += '''

/* FINAL PUBLICATION POLISH */
#main-content .fg-hub-hero h2 { color: #fff !important; }
#main-content a { color: #08796f; }
html[data-theme="dark"] #main-content a { color: #75ddd4; }
html[data-theme="dark"] .fg-nav-home[aria-current="page"] { color: #f3f5fb !important; }
html[data-theme="dark"] .fg-dropdown a[aria-current="page"],
html[data-theme="dark"] .fg-dropdown a:hover,
html[data-theme="dark"] .fg-dropdown a:focus-visible {
  color: #f3f5fb !important;
  background: #2a3150 !important;
}
#main-content .resource-box,
#main-content .contact-card {
  background: var(--fg-surface) !important;
  border: 1px solid var(--fg-border) !important;
  border-radius: var(--fg-radius) !important;
  padding: 22px !important;
  margin: 18px 0 !important;
}
#main-content .requirement-grid {
  display: grid !important;
  grid-template-columns: repeat(3, minmax(0, 1fr)) !important;
  gap: 18px !important;
  margin: 26px 0 !important;
}
#main-content .requirement-card {
  background: var(--fg-surface) !important;
  border: 1px solid var(--fg-border) !important;
  border-radius: var(--fg-radius) !important;
  padding: 22px !important;
  text-align: center !important;
  box-shadow: none !important;
}
#main-content .requirement-card h3 { margin: 0 0 10px !important; }
#main-content .requirement-card .page-count {
  font-size: 2rem !important;
  line-height: 1.1 !important;
  color: var(--fg-purple) !important;
  font-weight: 850 !important;
}
html[data-theme="dark"] #main-content .requirement-card .page-count { color: #c6c9ff !important; }
#main-content .requirement-card p { margin: 4px 0 !important; }
@media (max-width: 860px) {
  .fg-site-subtitle { font-size: 0 !important; margin-top: 3px !important; }
  .fg-site-subtitle::after { content: "ENG 1010: Composition"; font-size: .82rem; }
  #main-content .requirement-grid { grid-template-columns: 1fr !important; gap: 12px !important; }
  #main-content .requirement-card { padding: 18px !important; }
}
'''
    css_path.write_text(css, encoding='utf-8')

ap = Path('assignments.html')
soup = BeautifulSoup(ap.read_text(encoding='utf-8'), 'html.parser')
for h3 in soup.find_all('h3'):
    if h3.get_text(' ', strip=True) == 'Source Requirements & Evaluation':
        table = h3.find_next_sibling('table')
        if table:
            table.decompose()
        h3.decompose()
        break
ap.write_text(str(soup), encoding='utf-8')
