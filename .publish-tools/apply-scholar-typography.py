from pathlib import Path

path = Path('assets/faculty-guide.css')
css = path.read_text(encoding='utf-8')
marker = '/* SCHOLARS COMPASS TYPOGRAPHY ALIGNMENT */'
block = r'''

/* SCHOLARS COMPASS TYPOGRAPHY ALIGNMENT */
body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
  font-size: 18px !important;
  line-height: 1.6 !important;
}

/* Neutralize legacy page-level type sizing so reading text stays consistent. */
#main-content p,
#main-content li,
#main-content td,
#main-content th {
  font-size: 1rem !important;
  line-height: 1.6 !important;
}

/* Preserve intentionally compact interface/support text. */
#main-content .fg-hub-group > p { font-size: .92rem !important; }
#main-content .fg-breadcrumb { font-size: .84rem !important; }
#main-content .fg-page-nav-label { font-size: .74rem !important; }
#main-content .fg-quick-reference li { font-size: 1rem !important; }

/* Headings use the same clean system family and a readable hierarchy. */
#main-content h2,
#main-content h3,
#main-content h4,
#main-content h5 {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
  line-height: 1.25 !important;
}

@media (max-width: 520px) {
  body { font-size: 17px !important; }
  #main-content p,
  #main-content li,
  #main-content td,
  #main-content th { font-size: 1rem !important; }
}
'''
if marker not in css:
    css += block
else:
    start = css.index(marker)
    css = css[:start].rstrip() + block
path.write_text(css, encoding='utf-8')
