from pathlib import Path
from bs4 import BeautifulSoup

p=Path('instructional-strategies.html')
soup=BeautifulSoup(p.read_text(encoding='utf-8'),'html.parser')
content=soup.select_one('.content')
if not content:
    raise SystemExit('Missing .content')
content['id']='main-content'
active=soup.find('a',href='instructional-strategies.html',class_='active')
if active:
    active['aria-current']='page'

style=soup.find('style')
spacing='''\n        /* Publication spacing */\n        .content > .intro-section, .content > .section { margin-bottom: 64px; }\n        .content > .section:last-child { margin-bottom: 0; }\n        .content > .intro-section p, .content > .section p { margin-bottom: 20px; }\n        .content > .section h2, .content > .intro-section h2 { margin-bottom: 26px; }\n        .content > .section h3 { margin-top: 42px; margin-bottom: 20px; }\n        .content > .section h4 { margin-top: 22px; margin-bottom: 12px; }\n        .strategy-grid, .highlight-box, .activity-box, .tip-box, table { margin-top: 24px; margin-bottom: 30px; }\n'''
if '/* Publication spacing */' not in style.get_text():
    style.string=(style.string or '')+spacing


def hfind(text, tag=None):
    tags=[tag] if tag else ['h2','h3','h4','h5']
    for h in content.find_all(tags):
        if text.lower() in h.get_text(' ',strip=True).lower():
            return h
    raise SystemExit('Missing heading: '+text)

def settext(tag,text):
    tag.clear(); tag.append(text)

# Opening
intro=content.select_one('.intro-section')
settext(intro.find('h2'),'Teaching Approaches')
intro.find('p').string='Effective writing instruction balances clear expectations with meaningful support and opportunities for practice. The strategies on this page offer practical approaches for teaching ENG 1010, including ideas for active learning, reflection, critical reading, revision, classroom community, and support for students with varied experiences and needs.'

# Growth and revision
growth=hfind('Cultivating a Growth Mindset','h2').find_parent('div',class_='section')
settext(growth.find('h2'),'Cultivating a Growth Mindset')
growth.find('p').string='Many students enter ENG 1010 with strong beliefs about their abilities as writers. Faculty can help students see writing as a set of practices and skills that develop through reading, drafting, feedback, revision, and reflection.'
settext(growth.find('h3'),'Supporting Growth in the Writing Classroom')
for old,new in [('Praise Process, Not Product','Focus on Process'),('Normalize Revision','Normalize Revision'),('Make Progress Visible','Make Progress Visible'),('Use "Yet" Language','Use "Yet" Language')]:
    settext(hfind(old,'h4'),new)
for q in growth.select('.quote-box'): q.decompose()
for tip in growth.select('.tip-box strong'):
    if 'First-Day Activity' in tip.get_text(): tip.string='First-Day Activity:'

# Critical reading
critical=hfind('Teaching Critical Reading','h2').find_parent('div',class_='section')
settext(critical.find('h2'),'Teaching Critical Reading')
critical.find('p').string="Students need a working understanding of a text before they can analyze it effectively. Many students in ENG 1010, including students enrolled in ENG 0910, benefit from explicit instruction in active reading strategies. Instructors can model practices such as annotation, summary, identifying an author's argument, and tracing evidence and reasoning."
for li in critical.find_all('li'):
    st=li.find('strong')
    if st and 'Tweet-Length Summary' in st.get_text(): st.string='280-Character Summary:'
for h5 in critical.find_all('h5'):
    if 'Think-Pair-Share' in h5.get_text(): settext(h5,'Activity: Think-Pair-Share Protocol')
for st in critical.select('.tip-box strong'):
    if 'For ENG 0910 Students' in st.get_text(): st.string='For ENG 0910 Students:'

# Active learning
active_sec=hfind('Active Learning Techniques','h2').find_parent('div',class_='section')
settext(active_sec.find('h2'),'Active Learning Techniques')
settext(active_sec.find('h3'),'Activities for Writing Classrooms')
for h4 in active_sec.find_all('h4'):
    t=h4.get_text(' ',strip=True)
    if 'Quick Writes' in t: settext(h4,'Quick Writes (5-10 min)')
    elif 'Peer Workshops' in t: settext(h4,'Peer Workshops')
    elif 'Sentence-Level Workshops' in t: settext(h4,'Sentence-Level Workshops')
    elif 'Think-Alouds' in t: settext(h4,'Think-Alouds')
for ptag in active_sec.find_all('p'):
    if 'Experts do much of this automatically' in ptag.get_text(): ptag.string='Experienced readers and writers often do much of this automatically; students benefit from seeing the process made visible.'
for h5 in active_sec.find_all('h5'):
    if 'Thesis Statement Workshop' in h5.get_text(): settext(h5,'Sample Activity: Thesis Statement Workshop')

# Differentiation and support
diff=hfind('Differentiation','h2').find_parent('div',class_='section')
settext(diff.find('h2'),'Differentiation & Support Strategies')
diff.find('p').string='ENG 1010 classrooms include students with varied educational experiences, language backgrounds, strengths, responsibilities, and learning needs. Effective differentiation provides multiple pathways for students to engage with course material while maintaining the shared ENG 1010 learning outcomes.'
expr=hfind('Multiple Means of Expression','h4')
prev=expr.find_previous_sibling('p')
clar='Faculty can provide different ways for students to explore, practice, or reflect on course concepts while still ensuring that required ENG 1010 writing outcomes are assessed through writing.'
if not prev or clar not in prev.get_text(' ',strip=True):
    tag=soup.new_tag('p'); tag.string=clar; expr.insert_before(tag)
settext(hfind('Best Practices for Multilingual/ESL Students','h4'),'Best Practices for Multilingual Writers')
for st in diff.select('.tip-box strong'):
    if 'Grammar Instruction That Works' in st.get_text(): st.string='Grammar Instruction in Context:'

# Time management
time=hfind('Classroom Time Management','h2').find_parent('div',class_='section')
settext(time.find('h2'),'Classroom Time Management')
settext(time.find('h3'),'One Possible 75-Minute Class Structure')
for st in time.select('.tip-box strong'):
    if 'Online/Hybrid Adaptation' in st.get_text(): st.string='Online/Hybrid Adaptation:'

# Community
community=hfind('Building Classroom Community','h2').find_parent('div',class_='section')
settext(community.find('h2'),'Building Classroom Community')
for q in community.select('.quote-box'): q.decompose()

# Feedback
feedback=hfind('Effective Feedback Practices','h2').find_parent('div',class_='section')
settext(feedback.find('h2'),'Effective Feedback Practices')
limit=hfind('2. Limit Your Comments','h4').find_parent('div',class_='highlight-box')
limit.find('p').string='Extensive feedback can overwhelm students and make revision priorities difficult to identify. Instead:'
for h4 in feedback.find_all('h4'):
    t=h4.get_text(' ',strip=True)
    if 'Comment Banks' in t: settext(h4,'Comment Banks')
    elif 'Video or Audio Feedback' in t: settext(h4,'Audio, Video, or Screen-Recorded Feedback')
    elif 'Conferences' in t: settext(h4,'Conferences')
    elif 'Revision Plans' in t: settext(h4,'Revision Plans')
video=hfind('Audio, Video, or Screen-Recorded Feedback','h4').find_parent('div',class_='strategy-card')
video.find('p').string='Use available audio, video, or screen-recording tools to provide brief conversational feedback when appropriate.'
ul=video.find('ul'); ul.clear()
for text in ['Can be faster than extensive written feedback','Offers a conversational tone','Allows students to hear emphasis and priorities for revision']:
    li=soup.new_tag('li'); li.string=text; ul.append(li)
for st in feedback.select('.tip-box strong'):
    if 'For ENG 0910 Students' in st.get_text(): st.string='For ENG 0910 Students:'

# Remove decorative icons in the page content while keeping words and warning/callout structure.
emojis='🌱✍️🔄📊💬💡📖🎯🎭✏️👥🔍💭📘⏰🤝📝🎥📋'
for tag in content.find_all(['h2','h3','h4','h5','strong']):
    if tag.string:
        t=tag.string
        for e in emojis: t=t.replace(e,'')
        tag.string=' '.join(t.split())

text=str(soup)
if not text.lstrip().lower().startswith('<!doctype'):
    text='<!DOCTYPE html>\n'+text
p.write_text(text,encoding='utf-8')
