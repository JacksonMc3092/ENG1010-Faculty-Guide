from pathlib import Path
p=Path('assets/faculty-guide.css')
css=p.read_text(encoding='utf-8')
marker='/* SCHOLARS COMPASS READING SIZE FIX */'
block='''\n\n/* SCHOLARS COMPASS READING SIZE FIX */\nbody {\n  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;\n  font-size: 18px !important;\n  line-height: 1.6 !important;\n}\n#main-content p,\n#main-content li,\n#main-content td,\n#main-content th {\n  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;\n  font-size: 18px !important;\n  line-height: 1.6 !important;\n  font-weight: 400 !important;\n}\n#main-content .fg-hub-group > p { font-size: 16.5px !important; }\n#main-content .fg-breadcrumb { font-size: 15px !important; }\n#main-content .fg-page-nav-label { font-size: 13px !important; }\n#main-content .fg-quick-reference li { font-size: 18px !important; }\n@media (max-width: 520px) {\n  body { font-size: 18px !important; }\n  #main-content p,\n  #main-content li,\n  #main-content td,\n  #main-content th { font-size: 18px !important; }\n}\n'''
if marker in css:
    css=css[:css.index(marker)].rstrip()+block
else:
    css+=block
p.write_text(css,encoding='utf-8')
