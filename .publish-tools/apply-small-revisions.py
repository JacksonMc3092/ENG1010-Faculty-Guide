from pathlib import Path
from bs4 import BeautifulSoup
import re

ROOT = Path('.')

def load(name):
    return BeautifulSoup(Path(name).read_text(encoding='utf-8'), 'html.parser')

def save(name, soup):
    Path(name).write_text(str(soup), encoding='utf-8')

# 1. Corequisite scenario 3 wording
name = 'corequisite-model.html'
soup = load(name)
scenario = None
for h in soup.find_all(['h4','h5']):
    text = h.get_text(' ', strip=True)
    if 'Pass ENG 1010' in text and 'Do Not Participate in ENG 0910' in text and text.lstrip().startswith('3'):
        scenario = h.find_parent(class_='scenario-box') or h.parent
        h.string = '3 Pass ENG 1010 + Do Not Participate in ENG 0910'
        break
if scenario:
    result_p = next((p for p in scenario.find_all('p', recursive=False) if p.get_text(' ', strip=True).startswith('Result:')), None)
    if not result_p:
        result_p = scenario.find('p')
    if result_p:
        result_p.clear()
        strong = soup.new_tag('strong'); strong.string = 'Result:'; result_p.append(strong)
        result_p.append(' Students receive an ')
        strong2 = soup.new_tag('strong'); strong2.string = '"F"'; result_p.append(strong2)
        result_p.append(' in ENG 0910. Ideally these students have been dropped for NP (Non-Participation) or encouraged to withdraw.')
save(name, soup)

# 2. Assessment Revision Options
name = 'assessment.html'
soup = load(name)
heading = next((h for h in soup.find_all(['h3','h4']) if h.get_text(' ', strip=True) == 'Revision Options'), None)
if heading:
    # Find the first paragraph/list before the next same-or-higher-level heading.
    p = heading.find_next_sibling('p')
    if p:
        p.string = 'Consider allowing:'
    ul = heading.find_next_sibling('ul')
    if not ul:
        node = heading.find_next_sibling()
        while node and node.name not in ['h2','h3']:
            if getattr(node, 'name', None) == 'ul':
                ul = node; break
            node = node.find_next_sibling()
    if ul:
        ul.clear()
        items = [
            'At least one major revision per semester',
            'Grade averaging (average original + revision) or grade replacement',
            'Requiring a revision memo explaining changes that the student made in the revision',
        ]
        for text in items:
            li = soup.new_tag('li'); li.string = text; ul.append(li)
save(name, soup)

# 3. Shared spacing refinements
css_path = Path('assets/faculty-review.css')
css = css_path.read_text(encoding='utf-8')
marker = '/* August 13 small revision pass */'
if marker not in css:
    css += r'''

/* August 13 small revision pass */
/* Course Planning Guide: stronger separation between headings, descriptions, timelines, and sections */
#main-content .content-section > .section-title {
  margin-bottom: 2rem !important;
}
#main-content .intro-box h4 {
  margin-bottom: 1.35rem !important;
}
#main-content .module-card {
  margin-top: 3.75rem !important;
  margin-bottom: 4rem !important;
}
#main-content .module-header {
  margin-bottom: 1.8rem !important;
}
#main-content .module-title-section .module-weeks {
  margin-top: .8rem !important;
  margin-bottom: 0 !important;
}
#main-content .module-description {
  margin-top: 1.45rem !important;
  margin-bottom: 2rem !important;
}
#main-content .outcomes-section,
#main-content .activities-section {
  margin-top: 2.2rem !important;
}
#main-content .timeline-box {
  margin-top: 2.4rem !important;
  margin-bottom: 2.8rem !important;
}
#main-content .timeline-box h5 {
  margin-bottom: 1.55rem !important;
}
#main-content .timeline-item + .timeline-item {
  margin-top: 1rem !important;
}

/* Assignments: separate prompt text from the Why this works explanation */
#main-content .prompt-box .prompt-text + p {
  margin-top: 1.45rem !important;
}
'''
    css_path.write_text(css, encoding='utf-8')

print('Small Faculty Guide revisions applied')
