from pathlib import Path
from bs4 import BeautifulSoup

path = Path('syllabus-templates.html')
html = path.read_text(encoding='utf-8')
soup = BeautifulSoup(html, 'html.parser')
main = soup.find('div', id='main-content')
if main is None:
    raise SystemExit('Missing #main-content')

fragment = '''
<div class="intro-section">
  <h2>Syllabus Guidance</h2>
  <p>A clear syllabus gives students a roadmap for the course by explaining expectations, learning outcomes, assignments, grading, course policies, and important resources. This page highlights ENG 1010-specific information and Three Rivers syllabus expectations while directing faculty to current CT State resources for college-wide policies and statements.</p>
  <div class="info-box">
    <strong>Important:</strong> Email your syllabus to the department chair and the dean's office within two weeks of the start of the semester.
  </div>
</div>

<div class="section">
  <h2>Using Current CT State Syllabus Resources</h2>
  <p>CT State maintains syllabus guidance, institutional policies, academic engagement information, student resources, and other materials that may change over time. Faculty should consult current CT State materials when preparing each semester's syllabus rather than relying on older copied policy language.</p>
  <div class="checklist-box">
    <h3>Current CT State Syllabus &amp; Policy Resources</h3>
    <ul>
      <li><a href="https://ctstate.edu/for-you/faculty-staff" target="_blank" rel="noopener"><strong>CT State Faculty &amp; Staff Resources</strong></a> - current faculty links, including the sample CT State course syllabus, academic engagement guidance, disability support information, tutoring, and other resources.</li>
      <li><a href="https://ctstate.edu/curriculum-links/" target="_blank" rel="noopener"><strong>CT State Curriculum / Faculty Resources</strong></a> - approved course outlines and the sample CT State course syllabus template.</li>
      <li><a href="https://catalog.ctstate.edu/" target="_blank" rel="noopener"><strong>CT State Academic Catalog</strong></a> - current course descriptions, academic policies, grading information, programs, and college requirements.</li>
      <li><a href="https://ctstate.edu/academic-calendar" target="_blank" rel="noopener"><strong>CT State Academic Calendar</strong></a> - current semester dates, holidays, deadlines, and other calendar information.</li>
    </ul>
  </div>
</div>

<div class="section">
  <h2>Building Your ENG 1010 Syllabus</h2>
  <p>Instructors have flexibility in the organization and design of their syllabi. The syllabus should clearly communicate how the course will operate while keeping the approved ENG 1010 course information and current CT State expectations in view.</p>

  <div class="checklist-box">
    <h3>Course and Instructor Information</h3>
    <ul>
      <li>ENG 1010: Composition, 3 credits</li>
      <li>Semester, CRN, section, meeting information, location, and course modality</li>
      <li><strong>Prerequisite:</strong> Placement as determined by placement process</li>
      <li>Instructor name, CT State email, office or meeting information, and preferred contact method</li>
      <li>Course communication expectations and Blackboard information</li>
    </ul>
  </div>

  <div class="checklist-box">
    <h3>Course Design Information</h3>
    <ul>
      <li>Official course description and approved student learning outcomes</li>
      <li>Required text and any supplemental readings or materials</li>
      <li>Major assignments and other graded work</li>
      <li>Grading criteria or grade distribution</li>
      <li>Course schedule, readings, major due dates, and important semester dates</li>
      <li>Instructor policies for attendance or engagement, late work, revision, communication, and use of generative AI</li>
    </ul>
  </div>
</div>

<div class="section">
  <h2>Official ENG 1010 Information</h2>

  <h3>Official Course Description</h3>
  <div class="policy-text" style="background: white; border-left: 4px solid #667eea; padding: 24px;">
    <strong>ENG 1010: Composition (3 credits)</strong><br/><br/>
    Composition focuses on the study and practice of effective written communication across a variety of rhetorical situations. The course develops skills in applying language conventions, engaging with and using authoritative sources, and crafting logical arguments.
  </div>

  <h3>Student Learning Outcomes</h3>
  <p>All ENG 1010 syllabi should include the complete approved student learning outcomes. The outcomes are organized into four areas:</p>
  <ol style="padding-left: 36px; margin: 20px 0 28px 0;">
    <li><strong>Respond to Rhetorical Situations</strong></li>
    <li><strong>Engage with and Use Authoritative Sources</strong></li>
    <li><strong>Craft Logical Arguments</strong></li>
    <li><strong>Apply Language Conventions</strong></li>
  </ol>
  <p>See the <a href="course-overview.html">Course Overview</a> for the complete approved wording.</p>

  <h3>Required Text</h3>
  <p><em>They Say / I Say with Readings</em>, 6th edition (Norton, 2024), plus supplemental readings selected by the instructor. Instructors may not require a different text or handbook without permission of the Curriculum Leader or Department Chair.</p>
</div>

<div class="section">
  <h2>Three Rivers ENG 1010 Course Expectations</h2>
  <p>The following local expectations should be reflected clearly in the syllabus while leaving instructors flexibility in assignment sequence, topics, and course design.</p>
  <div class="checklist-box">
    <ul>
      <li>Students are required to complete <strong>at least 20 pages of finished formal writing</strong> over the course of the semester.</li>
      <li>In order to pass the course, <strong>students must submit all formal assignments</strong>.</li>
      <li>Throughout the semester, students should encounter around <strong>6 to 8 substantive readings of varying complexity</strong> from the required text and/or supplemental readings.</li>
      <li>The Faculty Guide presents a <strong>recommended three-assignment sequence</strong>, not a required template: Essay 1 (3-5 pages), Essay 2 (5-7 pages), and Essay 3 (6-8 pages).</li>
      <li>By the end of the semester, students must complete at least one thesis-driven, text-based essay of approximately 1500 words that demonstrates competent argumentation using complex texts.</li>
    </ul>
  </div>
  <p>See <a href="assignments.html">Assignments</a> and <a href="assessment.html">Assessment</a> for sample prompts, sequencing options, and rubrics that can be adapted to individual sections.</p>
</div>

<div class="section">
  <h2>College-Wide Policies &amp; Resources</h2>
  <p>Use current CT State syllabus and faculty resources for college-wide information such as academic engagement, academic integrity, withdrawal, disability and accessibility services, student support, communication processes, and other institutional statements. Linking to and consulting the current institutional sources helps prevent outdated policy language from remaining in a syllabus after CT State guidance changes.</p>
  <div class="info-box">
    <strong>Good practice:</strong> Review the current CT State syllabus resources before each semester begins, especially if you are reusing a syllabus from an earlier term.
  </div>
</div>

<div class="section">
  <h2>Final Syllabus Checklist</h2>
  <p>Before distributing the syllabus and emailing the required copy, confirm that it includes:</p>
  <div class="checklist-box">
    <ul>
      <li>Current course and instructor information</li>
      <li>The official ENG 1010 course description</li>
      <li>The complete approved ENG 1010 student learning outcomes</li>
      <li>The required text and any additional course materials</li>
      <li>Clear assignment, grading, and revision expectations</li>
      <li>A course calendar or schedule with major due dates</li>
      <li>Your attendance or engagement, communication, late-work, and AI expectations</li>
      <li>Current CT State policy and student-resource information drawn from current institutional sources</li>
      <li>Accessible formatting and working links</li>
    </ul>
  </div>
  <p><strong>Submission:</strong> Email the syllabus to the department chair and the dean's office within two weeks of the start of the semester.</p>
</div>
'''

new_nodes = BeautifulSoup(fragment, 'html.parser')
main.clear()
for node in list(new_nodes.contents):
    main.append(node)

style = soup.find('style')
if style is None:
    raise SystemExit('Missing style block')
spacing_css = '''

        /* Publication spacing for syllabus page */
        #main-content > .intro-section,
        #main-content > .section { margin-bottom: 68px; }
        #main-content > .section:last-child { margin-bottom: 0; }
        #main-content p { margin-bottom: 22px; }
        #main-content h2 { margin-bottom: 28px; }
        #main-content h3 { margin-top: 42px; margin-bottom: 20px; }
        #main-content .checklist-box,
        #main-content .info-box,
        #main-content .policy-text { margin-top: 28px; margin-bottom: 34px; }
        #main-content .checklist-box li { margin-bottom: 12px; line-height: 1.7; }
        #main-content .checklist-box li:last-child { margin-bottom: 0; }
        #main-content a { overflow-wrap: anywhere; }
'''
style.append(spacing_css)

out = str(soup)
out = out.replace('>🏠 Home<', '>Home<')
path.write_text(out, encoding='utf-8')
