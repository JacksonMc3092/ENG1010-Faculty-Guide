from pathlib import Path
from bs4 import BeautifulSoup, NavigableString
import re

ROOT = Path('.')
PAGES = [
    'index.html','getting-started.html','course-overview.html','corequisite-model.html',
    'module-guide.html','assignments.html','instructional-strategies.html','assessment.html',
    'syllabus-templates.html','policies.html','ai-policy.html','faculty-support.html'
]

def soup_file(path):
    return BeautifulSoup(Path(path).read_text(encoding='utf-8'), 'html.parser')

def save(path, soup):
    Path(path).write_text(str(soup), encoding='utf-8')

def replace_text(soup, pattern, replacement, flags=re.I):
    rx = re.compile(pattern, flags)
    for node in list(soup.find_all(string=rx)):
        if isinstance(node, NavigableString):
            node.replace_with(rx.sub(replacement, str(node)))

def ensure_review_css(soup):
    if not soup.find('link', href='assets/faculty-review.css'):
        base = soup.find('link', href='assets/faculty-guide.css')
        tag = soup.new_tag('link', rel='stylesheet', href='assets/faculty-review.css')
        if base: base.insert_after(tag)
        else: soup.head.append(tag)

def update_banner(soup):
    brand = soup.select_one('.fg-brand')
    if not brand: return
    mark = brand.select_one('.fg-mark')
    if mark:
        img = soup.new_tag('img', src='assets/site-mark.jpg', alt='', **{'class':'fg-mark-image','aria-hidden':'true'})
        mark.replace_with(img)
    elif not brand.select_one('.fg-mark-image'):
        img = soup.new_tag('img', src='assets/site-mark.jpg', alt='', **{'class':'fg-mark-image','aria-hidden':'true'})
        brand.insert(0, img)
    copy = brand.select_one('.fg-brand-copy')
    if copy:
        name = copy.select_one('.fg-site-name')
        subtitle = copy.select_one('.fg-site-subtitle, .fg-course-line')
        if subtitle:
            subtitle['class'] = ['fg-course-line']
            subtitle.string = 'ENG 1010: Composition | CT State - Three Rivers'
        else:
            subtitle = soup.new_tag('span', **{'class':'fg-course-line'})
            subtitle.string = 'ENG 1010: Composition | CT State - Three Rivers'
        if name: name.string = 'Faculty Guide'
        copy.clear()
        copy.append(subtitle)
        if name: copy.append(name)

def update_nav(soup, current_file):
    home = soup.select_one('.fg-nav-home')
    if home: home.string = 'Home'
    # Getting Started dropdown: insert Quick Start after Getting Started.
    for group in soup.select('.fg-nav-group'):
        button = group.find('button')
        if button and 'Getting Started' in button.get_text(' ', strip=True):
            dd = group.select_one('.fg-dropdown')
            if dd and not dd.find('a', href='quick-start.html'):
                first = dd.find('a', href='getting-started.html')
                q = soup.new_tag('a', href='quick-start.html')
                q.string = 'Quick Start'
                if first: first.insert_after(q)
                else: dd.insert(0, q)
    # Fix current-page marker in dropdowns.
    for a in soup.select('.fg-dropdown a, .fg-nav-home'):
        if a.get('href') == current_file: a['aria-current'] = 'page'
        elif a.has_attr('aria-current'): del a['aria-current']

def terminology(soup):
    replace_text(soup, r'(?:The\s+)?English\s*1010\s+curriculum\s+committee', 'The First-Year Writing Task Force')
    replace_text(soup, r'(?:The\s+)?ENG\s*1010\s+Curriculum\s+Committee', 'The First-Year Writing Task Force')
    replace_text(soup, r'English\s*1010\s+Curriculum\s+Committee', 'First-Year Writing Task Force')
    replace_text(soup, r'ENG\s*1010\s+curriculum\s+committee', 'First-Year Writing Task Force')

def rename_planning_guide(soup):
    replace_text(soup, r'Module-by-Module\s+Guide', 'Course Planning Guide')
    replace_text(soup, r'Module-by-Module\s+Planning', 'Course Planning Guide')
    replace_text(soup, r'Module Guide', 'Course Planning Guide')
    if soup.title:
        soup.title.string = re.sub(r'MODULE GUIDE', 'COURSE PLANNING GUIDE', soup.title.get_text(), flags=re.I)

def external_links(soup):
    for a in soup.find_all('a', href=True):
        href = a['href'].strip()
        if href.startswith(('http://','https://')) and 'jacksonmc3092.github.io/ENG1010-Faculty-Guide' not in href:
            a['target'] = '_blank'
            rel = set(a.get('rel', []))
            rel.update(['noopener','noreferrer'])
            a['rel'] = sorted(rel)

def course_overview(soup):
    main = soup.select_one('#main-content')
    if not main: return
    # Give the final Best Practice in Reading Requirements extra space before the next major section.
    for p in main.find_all('p'):
        if 'Best Practice:' in p.get_text() and p.find_parent(class_='text-box'):
            classes = p.get('class', [])
            if 'fg-before-writing-requirements' not in classes:
                p['class'] = classes + ['fg-before-writing-requirements']
    # Restore the previously approved writing-requirements framing.
    target = next((s for s in main.find_all('section') if s.find('h2') and s.find('h2').get_text(' ',strip=True)=='Student Writing Requirements'), None)
    if target:
        firstp = target.find('p')
        if firstp:
            firstp.string = 'Students are required to complete at least 20 pages of finished formal writing over the course of the semester.'
        box = target.find(class_='highlight-box')
        if box:
            box.clear()
            h4 = soup.new_tag('h4'); h4.string = 'Required Formal Writing'; box.append(h4)
            p = soup.new_tag('p'); p.string = 'Students are required to complete at least 20 pages of finished formal writing over the course of the semester.'; box.append(p)
        imp = next((p for p in target.find_all('p') if 'In order to pass the course' in p.get_text()), None)
        if not imp:
            imp = soup.new_tag('p'); imp.append(BeautifulSoup('<strong>Important:</strong> In order to pass the course, <strong>students must submit ALL formal assignments</strong>.','html.parser')); target.append(imp)
    seq = next((s for s in main.find_all('section') if s.find('h2') and s.find('h2').get_text(' ',strip=True)=='Assignment Sequence'), None)
    if seq:
        p = seq.find('p')
        if p:
            p.string = ('The following three assignments are recommended for ENG 1010. Together, they provide one approach to moving students from close reading and critical analysis through synthesis and research-based argument. Instructors may adapt the sequence, topics, and assignment design based on their teaching approach and the needs of their students while ensuring that the official course learning outcomes are met.')

def corequisite(soup):
    for card in soup.select('.course-card'):
        if 'ENG 0910' in card.get_text(' ', strip=True):
            badge = card.select_one('.course-badge')
            if badge: badge.string = '3 Credits'
            for p in card.find_all('p'):
                if 'Satisfies:' in p.get_text():
                    p.clear()
                    strong=soup.new_tag('strong'); strong.string='Degree applicability:'; p.append(strong); p.append(' Credits do not apply toward degree requirements.')

def planning_guide(soup):
    for n in soup.select('.module-number'): n.decompose()
    replace_text(soup, r'The ENG 1010 Course Planning Guide offers one possible framework for organizing the semester\. The modules identify', 'The ENG 1010 Course Planning Guide offers one possible framework for organizing the semester. The sections identify')
    replace_text(soup, r'Essay #2: Synthesis paper \(5-6 pages\)', 'Essay #2: Synthesis paper (5-7 pages)')

def assessment(soup):
    gt = soup.select_one('.grade-table')
    if gt and gt.name != 'table':
        gt.name = 'table'
    if gt and not gt.find_parent(class_='fg-grade-table-wrap'):
        wrap = soup.new_tag('div', **{'class':'fg-grade-table-wrap'})
        gt.wrap(wrap)

def syllabus(soup):
    main=soup.select_one('#main-content')
    if not main: return
    for section in list(main.find_all(class_='section', recursive=False)):
        h2=section.find('h2')
        if h2 and h2.get_text(' ',strip=True)=='Three Rivers ENG 1010 Course Expectations':
            section.decompose()
    target=None
    for section in main.find_all(class_='section', recursive=False):
        h2=section.find('h2')
        if h2 and h2.get_text(' ',strip=True)=='College-Wide Policies & Resources': target=section; break
    if target and not target.find('a', href='https://catalog.ctstate.edu/policy-resources/'):
        box=soup.new_tag('div', **{'class':'checklist-box'})
        h3=soup.new_tag('h3'); h3.string='Current CT State Resources'; box.append(h3)
        ul=soup.new_tag('ul')
        links=[
            ('https://ctstate.edu/for-you/faculty-staff','Faculty & Staff Resources','current faculty forms, guidance, syllabus resources, and support links'),
            ('https://catalog.ctstate.edu/policy-resources/','Academic Catalog Policy Resources','current institutional policy resources'),
            ('https://catalog.ctstate.edu/academic-policies-procedures/expectation-academic-integrity/','Academic Integrity','current expectations for academic integrity'),
            ('https://ctstate.edu/conduct','Student Conduct','Student Code of Conduct and referral resources'),
            ('https://ctstate.edu/ss-links','Student Services Quick Links','student support and referral resources')]
        for href,label,desc in links:
            li=soup.new_tag('li'); a=soup.new_tag('a',href=href); strong=soup.new_tag('strong'); strong.string=label; a.append(strong); li.append(a); li.append(f' - {desc}.'); ul.append(li)
        box.append(ul); target.append(box)

def policies(soup):
    main=soup.select_one('#main-content')
    if not main: return
    box=None
    for b in main.select('.policy-box'):
        h=b.find(['h3','h4'])
        if h and h.get_text(' ',strip=True)=='Incomplete Grades': box=b; break
    if not box: return
    h=box.find(['h3','h4'])
    box.clear(); box.append(h)
    paragraphs=[
        'An Incomplete is a temporary grade used when coursework is missing and the student agrees to complete the remaining requirements. A student may request an Incomplete, but faculty are not required to approve the request. Faculty should consider whether extenuating circumstances exist, whether the student has participated in and completed at least 61% of the course, and whether the remaining work can be completed no later than the tenth week of the next standard semester.',
        'After discussing the request with the instructor, the student initiates the Incomplete Grade Request through the MyCTState Student Online Forms area. The instructor then reviews the request, identifies the work that remains, establishes the completion deadline and default grade, provides the last date of attendance, and approves or denies the request. Approved requests are routed to the appropriate Dean and Registration and Academic History for processing.'
    ]
    for text in paragraphs:
        p=soup.new_tag('p'); p.string=text; box.append(p)
    info=soup.new_tag('div', **{'class':'info-box'})
    strong=soup.new_tag('strong'); strong.string='When submitting final grades:'; info.append(strong)
    info.append(' If the student has already discussed the Incomplete with you and the online Incomplete process has been started, leave that student’s grade blank on the roster and submit the remaining grades normally. The course may temporarily appear as “In Progress.” Once the approved Incomplete form is processed, the roster will be updated. Do not leave a grade blank unless the Incomplete process has already been initiated; otherwise, a final grade must be submitted.')
    box.append(info)
    note=soup.new_tag('div', **{'class':'alert-box'})
    strong=soup.new_tag('strong'); strong.string='Note for Part-Time Faculty:'; note.append(strong)
    note.append(' Part-time faculty who grant an Incomplete should notify the Department Chair and confirm whether they are willing to evaluate the student’s completed work if it is submitted while they are off contract. If the faculty member is not available or does not wish to assess the work while off contract, the Department Chair will make arrangements for the completed work to be evaluated based on a discussion with the faculty member about the remaining requirements and expectations.')
    box.append(note)

def build_quick_start():
    soup=soup_file('getting-started.html')
    update_nav(soup,'quick-start.html')
    if soup.title: soup.title.string='Quick Start | ENG 1010 Faculty Guide'
    main=soup.select_one('#main-content')
    if main:
        main.clear()
        frag=BeautifulSoup('''
        <div class="fg-breadcrumb" aria-label="Breadcrumb"><a href="index.html">Faculty Guide Hub</a><span class="fg-breadcrumb-sep" aria-hidden="true">/</span><span>Getting Started</span><span class="fg-breadcrumb-sep" aria-hidden="true">/</span><span>Quick Start</span></div>
        <section class="intro-section"><h2>Quick Start</h2><p>New to ENG 1010 or preparing a section on a short timeline? This page gathers the materials faculty most often request when they are getting started and points to the essential planning resources in the Faculty Guide.</p><div class="info-box"><strong>Sample downloads:</strong> Current sample syllabi and course calendars will be added here once the files are provided.</div></section>
        <section class="section"><h2>Sample Syllabi &amp; Course Calendars</h2><div class="fg-quickstart-grid"><div class="fg-quickstart-card"><h3>Sample Syllabi</h3><p>Downloadable ENG 1010 sample syllabi will be posted here for faculty to adapt to their own sections.</p><span class="fg-status">Samples forthcoming</span></div><div class="fg-quickstart-card"><h3>Course Calendars</h3><p>Downloadable sample course calendars will be posted here to provide starting points for semester pacing and planning.</p><span class="fg-status">Samples forthcoming</span></div></div></section>
        <section class="section"><h2>Build Your Course</h2><div class="checklist-box"><ul><li><a href="course-overview.html"><strong>Course Overview</strong></a> - official course information, learning outcomes, required text, and writing expectations.</li><li><a href="module-guide.html"><strong>Course Planning Guide</strong></a> - a flexible framework for organizing the semester.</li><li><a href="assignments.html"><strong>Assignments</strong></a> - recommended sequence, sample prompts, and scaffolding ideas.</li><li><a href="syllabus-templates.html"><strong>Syllabus Guidance</strong></a> - syllabus planning and current CT State resources.</li><li><a href="policies.html"><strong>Policies</strong></a> - practical Three Rivers procedures and links to current CT State policy resources.</li></ul></div></section>
        <div class="fg-page-nav" aria-label="Faculty Guide page navigation"><a class="fg-prev" href="getting-started.html"><span class="fg-page-nav-label">Previous</span><span class="fg-page-nav-title">Getting Started</span></a><a class="fg-hub-link" href="index.html"><span class="fg-page-nav-label">Faculty Guide</span><span class="fg-page-nav-title">Hub</span></a><a class="fg-next" href="course-overview.html"><span class="fg-page-nav-label">Next</span><span class="fg-page-nav-title">Course Overview</span></a></div>
        ''','html.parser')
        for child in list(frag.contents): main.append(child)
    return soup

# Apply common and page-specific changes.
for filename in PAGES:
    soup=soup_file(filename)
    ensure_review_css(soup)
    update_banner(soup)
    update_nav(soup,filename)
    terminology(soup)
    rename_planning_guide(soup)
    if filename=='course-overview.html': course_overview(soup)
    elif filename=='corequisite-model.html': corequisite(soup)
    elif filename=='module-guide.html': planning_guide(soup)
    elif filename=='assessment.html': assessment(soup)
    elif filename=='syllabus-templates.html': syllabus(soup)
    elif filename=='policies.html': policies(soup)
    external_links(soup)
    save(filename,soup)

# Add Quick Start to homepage hub.
soup=soup_file('index.html')
group=None
for section in soup.select('.fg-hub-group'):
    h=section.find('h3')
    if h and h.get_text(strip=True)=='Getting Started': group=section; break
if group:
    ul=group.find('ul')
    if ul and not ul.find('a',href='quick-start.html'):
        first=ul.find('li')
        li=soup.new_tag('li'); a=soup.new_tag('a',href='quick-start.html'); a.string='Quick Start'; li.append(a)
        if first: first.insert_after(li)
        else: ul.append(li)
external_links(soup); save('index.html',soup)

# Build the new page after the shared shell has been updated.
qs=build_quick_start(); ensure_review_css(qs); update_banner(qs); terminology(qs); rename_planning_guide(qs); external_links(qs); save('quick-start.html',qs)
