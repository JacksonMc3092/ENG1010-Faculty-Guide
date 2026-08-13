from pathlib import Path

p = Path('assets/faculty-guide.css')
css = p.read_text(encoding='utf-8')
marker = '/* FACULTY GUIDE READING PRESENCE */'
block = '''

/* FACULTY GUIDE READING PRESENCE */
#main-content p,
#main-content li,
#main-content td,
#main-content th {
  font-family: 'Segoe UI Variable', 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
  font-size: 19px !important;
  line-height: 1.65 !important;
  font-weight: 500 !important;
}

/* Keep interface/support copy visually subordinate to the reading text. */
#main-content .fg-hub-group > p { font-size: 17px !important; font-weight: 400 !important; }
#main-content .fg-breadcrumb { font-size: 15px !important; font-weight: 400 !important; }
#main-content .fg-page-nav-label { font-size: 13px !important; font-weight: 800 !important; }
#main-content .fg-page-nav-title { font-weight: 700 !important; }
#main-content .fg-quick-reference li { font-size: 19px !important; font-weight: 500 !important; }

@media (max-width: 520px) {
  #main-content p,
  #main-content li,
  #main-content td,
  #main-content th {
    font-size: 19px !important;
    line-height: 1.65 !important;
    font-weight: 500 !important;
  }
}
'''

if marker in css:
    css = css[:css.index(marker)].rstrip() + block
else:
    css += block
p.write_text(css, encoding='utf-8')
