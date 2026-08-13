from pathlib import Path
p=Path('instructional-strategies.html')
s=p.read_text(encoding='utf-8')

def r(a,b,n=1):
    global s
    if a not in s:
        raise SystemExit('Missing expected text: '+a[:100])
    s=s.replace(a,b,n)

# Looser spacing for long teaching pages.
r('</style>','''\n        /* Publication spacing */\n        .content > .intro-section, .content > .section { margin-bottom: 64px; }\n        .content > .section:last-child { margin-bottom: 0; }\n        .content > .intro-section p, .content > .section p { margin-bottom: 20px; }\n        .content > .section h2, .content > .intro-section h2 { margin-bottom: 26px; }\n        .content > .section h3 { margin-top: 42px; margin-bottom: 20px; }\n        .content > .section h4 { margin-top: 22px; margin-bottom: 12px; }\n        .strategy-grid, .highlight-box, .activity-box, .tip-box, table { margin-top: 24px; margin-bottom: 30px; }\n</style>''')

r('<h2>Teaching Philosophy</h2>','<h2>Teaching Approaches</h2>')
r('Effective writing instruction balances high expectations with supportive scaffolding. This page provides evidence-based strategies for teaching composition, with particular attention to the diverse needs of ENG 1010 students, including those in the corequisite ENG 0910 workshop. These approaches emphasize <strong>active learning, metacognition, and growth mindset</strong>—principles that help all students develop as writers and thinkers.','Effective writing instruction balances clear expectations with meaningful support and opportunities for practice. The strategies on this page offer practical approaches for teaching ENG 1010, including ideas for active learning, reflection, critical reading, revision, classroom community, and support for students with varied experiences and needs.')

r('<h2>🌱 Cultivating a Growth Mindset</h2>','<h2>Cultivating a Growth Mindset</h2>')
r('Many students enter ENG 1010 with fixed beliefs about their writing ability: "I\'m just not a good writer" or "I\'ve always been bad at English." Research by Carol Dweck and others shows that <strong>mindset matters</strong>. Students who believe writing ability can be developed through practice and feedback are more likely to persist through challenges, take intellectual risks, and improve over time.','Many students enter ENG 1010 with strong beliefs about their abilities as writers. Faculty can help students see writing as a set of practices and skills that develop through reading, drafting, feedback, revision, and reflection.')
r('<h3>How to Foster Growth Mindset in Your Classroom</h3>','<h3>Supporting Growth in the Writing Classroom</h3>')
r('<h4>✍️ Praise Process, Not Product</h4>','<h4>Focus on Process</h4>')
r('<h4>🔄 Normalize Revision</h4>','<h4>Normalize Revision</h4>')
r('<h4>📊 Make Progress Visible</h4>','<h4>Make Progress Visible</h4>')
r('<h4>💬 Use "Yet" Language</h4>','<h4>Use "Yet" Language</h4>')
r('<strong>💡 First-Day Activity:</strong>','<strong>First-Day Activity:</strong>')
r('''
                <div class="quote-box">
                    "The students who think they can't write are often the ones who simply haven't been taught strategies for invention, revision, and editing. Once they learn that writing is a <em>process with learnable skills</em>, they start to see themselves differently." — Composition pedagogy research
                </div>''','')

r('<h2>📖 Teaching Critical Reading</h2>','<h2>Teaching Critical Reading</h2>')
r("Students can't write effectively about texts they don't understand. Many students in ENG 1010—especially those placed into ENG 0910—need explicit instruction in <strong>active reading strategies</strong>. Don't assume they know how to annotate, summarize, or identify an author's argument.","Students need a working understanding of a text before they can analyze it effectively. Many students in ENG 1010, including students enrolled in ENG 0910, benefit from explicit instruction in active reading strategies. Instructors can model practices such as annotation, summary, identifying an author's argument, and tracing evidence and reasoning.")
r('<strong>Tweet-Length Summary:</strong>','<strong>280-Character Summary:</strong>')
r('<h5>🎯 Activity: Think-Pair-Share Protocol</h5>','<h5>Activity: Think-Pair-Share Protocol</h5>')
r('<strong>💡 For ENG 0910 Students:</strong>','<strong>For ENG 0910 Students:</strong>',1)

r('<h2>🎭 Active Learning Techniques</h2>','<h2>Active Learning Techniques</h2>')
r('<h3>High-Impact Activities for Writing Classrooms</h3>','<h3>Activities for Writing Classrooms</h3>')
for a,b in [('✏️ Quick Writes','Quick Writes'),('👥 Peer Workshops','Peer Workshops'),('🔍 Sentence-Level Workshops','Sentence-Level Workshops'),('💭 Think-Alouds','Think-Alouds')]: r(a,b)
r('Experts do much of this automatically; novices need to see the process made visible.','Experienced readers and writers often do much of this automatically; students benefit from seeing the process made visible.')
r('📘 Sample Activity: Thesis Statement Workshop','Sample Activity: Thesis Statement Workshop')

r('<h2>🎯 Differentiation & Support Strategies</h2>','<h2>Differentiation &amp; Support Strategies</h2>')
r('ENG 1010 classrooms include students with varied preparation, languages, learning styles, and needs. Effective differentiation means <strong>providing multiple pathways to success</strong> while maintaining high expectations for all students.','ENG 1010 classrooms include students with varied educational experiences, language backgrounds, strengths, responsibilities, and learning needs. Effective differentiation provides multiple pathways for students to engage with course material while maintaining the shared ENG 1010 learning outcomes.')
r('<h4>Multiple Means of Expression</h4>','<p>Faculty can provide different ways for students to explore, practice, or reflect on course concepts while still ensuring that required ENG 1010 writing outcomes are assessed through writing.</p>\n                    <h4>Multiple Means of Expression</h4>')
r('<h4>Best Practices for Multilingual/ESL Students</h4>','<h4>Best Practices for Multilingual Writers</h4>')
r('<strong>💡 Grammar Instruction That Works:</strong>','<strong>Grammar Instruction in Context:</strong>')

r('<h2>⏰ Classroom Time Management</h2>','<h2>Classroom Time Management</h2>')
r('<h3>Sample 75-Minute Class Structure</h3>','<h3>One Possible 75-Minute Class Structure</h3>')
r('<strong>💡 Online/Hybrid Adaptation:</strong>','<strong>Online/Hybrid Adaptation:</strong>')

r('<h2>🤝 Building Classroom Community</h2>','<h2>Building Classroom Community</h2>')
r('''
                <div class="quote-box">
                    "Students who feel they belong in a classroom are more likely to persist through challenges, seek help when needed, and engage deeply with course material. Community isn't a luxury—it's foundational to learning." — Educational research on belonging
                </div>''','')

r('<h2>💬 Effective Feedback Practices</h2>','<h2>Effective Feedback Practices</h2>')
r('Research shows students are overwhelmed by extensive feedback. Instead:','Extensive feedback can overwhelm students and make revision priorities difficult to identify. Instead:')
for a,b in [('📝 Comment Banks','Comment Banks'),('🎥 Video or Audio Feedback','Audio, Video, or Screen-Recorded Feedback'),('📋 Conferences','Conferences'),('🔄 Revision Plans','Revision Plans')]: r(a,b)
r('''<p>Record 3-5 minute video/audio comments instead of typing:</p>
                        <ul>
                            <li>Often faster than writing</li>
                            <li>More conversational tone</li>
                            <li>Students can hear your emphasis and tone</li>
                            <li>Tools: Screencast-O-Matic, Loom, or Blackboard's audio comment feature</li>
                        </ul>''','''<p>Use available audio, video, or screen-recording tools to provide brief conversational feedback when appropriate.</p>
                        <ul>
                            <li>Can be faster than extensive written feedback</li>
                            <li>Offers a conversational tone</li>
                            <li>Allows students to hear emphasis and priorities for revision</li>
                        </ul>''')
r('<strong>💡 For ENG 0910 Students:</strong>','<strong>For ENG 0910 Students:</strong>',1)

# Remove the decorative home icon on this revised page.
r('>🏠 Home<','>Home<')
# Current revision date.
r("Scholar's Compass Project | Last Updated: November 2024","Scholar's Compass Project | Revised for publication: August 2026")

p.write_text(s,encoding='utf-8')
