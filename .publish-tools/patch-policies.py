from pathlib import Path
from bs4 import BeautifulSoup

p = Path('policies.html')
s = p.read_text(encoding='utf-8')
soup = BeautifulSoup(s, 'html.parser')
content = soup.find('div', {'class': 'content', 'id': 'main-content'})
if content is None:
    raise SystemExit('main content container not found')

fragment = BeautifulSoup('''
<div class="intro-section">
  <h2>Policy Guidance for ENG 1010 Faculty</h2>
  <p>This page highlights policies and procedures that commonly affect ENG 1010 faculty at CT State - Three Rivers. It is intended as a practical starting point rather than a substitute for current CT State policy. Because institutional procedures and deadlines may change, faculty should use the linked CT State resources for the most current information.</p>
  <div class="info-box">
    <strong>Cancelling a Class Meeting:</strong>
    <p>If you need to cancel a class meeting during the semester, you must send an email to <a href="mailto:TR-AcademicDean@ctstate.edu">TR-AcademicDean@ctstate.edu</a>, <a href="mailto:Ronda.Charette@ctstate.edu">Ronda.Charette@ctstate.edu</a>, and <a href="mailto:joseph.selvaggio@ctstate.edu">joseph.selvaggio@ctstate.edu</a>.</p>
    <p>When possible, students should also be notified promptly by email and/or through Blackboard.</p>
  </div>
</div>

<div class="section">
  <h2>FERPA and Student Privacy</h2>
  <p>The Family Educational Rights and Privacy Act (FERPA) protects the privacy of student education records. Faculty routinely work with grades, student writing, attendance information, communications, and other records that may be protected.</p>
  <div class="policy-box">
    <h3>Practical Reminders</h3>
    <ul>
      <li>Discuss grades and other protected student information only with the student or with authorized college personnel who have a legitimate educational interest.</li>
      <li>Do not share a student's educational information with parents, family members, or other third parties unless appropriate authorization is in place.</li>
      <li>Protect identifiable student work, rosters, grades, and course records from public access.</li>
      <li>Use institution-approved systems when communicating or storing sensitive student information.</li>
    </ul>
  </div>
  <p>For current FERPA guidance and related institutional policy resources, consult the <a href="https://catalog.ctstate.edu/policy-resources/" target="_blank" rel="noopener">CT State Academic Catalog Policy Resources</a>.</p>
</div>

<div class="section">
  <h2>Academic Engagement</h2>
  <p>Faculty are responsible for documenting and reporting academic engagement according to current CT State guidance and the deadlines established for the specific course session. Because deadlines differ among full-term, late-start, and accelerated courses, consult the current Academic Calendar and the Guidance for Academic Engagement each semester.</p>
  <div class="alert-box">
    <strong>Important:</strong> Academic Engagement documentation reminders are emailed to faculty. Required Academic Engagement notations <strong>MUST be submitted by the established deadline</strong> for each course or session. Email the department chair if you have questions about Academic Engagement reporting or documentation.
  </div>
  <p><a href="https://ctstate.edu/for-you/faculty-staff" target="_blank" rel="noopener">CT State Faculty &amp; Staff Resources</a> provides the current Guidance for Academic Engagement. Use the <a href="https://ctstate.edu/academics/academic-calendar" target="_blank" rel="noopener">CT State Academic Calendar</a> for session-specific student and faculty deadlines.</p>
</div>

<div class="section">
  <h2>Grades and Incompletes</h2>
  <p>Final grades should be submitted by the deadline listed for the appropriate term or session in the CT State Academic Calendar. Because deadlines and administrative procedures may change, use current CT State resources rather than relying on older copied instructions.</p>
  <div class="policy-box">
    <h3>Incomplete Grades</h3>
    <p>An Incomplete is a temporary grade used when coursework is missing and the student agrees to complete the remaining requirements. Current CT State grading policy directs faculty to consider whether extenuating circumstances exist, whether the student has participated in and completed at least 61% of the course, and whether the remaining work can be completed no later than the tenth week of the next standard semester.</p>
    <p>Faculty assigning an Incomplete must document the temporary grade using the designated CT State process and communicate the remaining requirements and deadline to the student.</p>
  </div>
  <p>See the <a href="https://catalog.ctstate.edu/academic-policies-procedures/grades-grade-points-/" target="_blank" rel="noopener">current CT State Grading policy</a> and the <a href="https://ctstate.edu/academics/academic-calendar" target="_blank" rel="noopener">Academic Calendar</a>.</p>
</div>

<div class="section">
  <h2>Academic Integrity and Student Conduct</h2>
  <p>Academic integrity and classroom conduct concerns should be handled carefully, consistently, and in accordance with current CT State procedures.</p>
  <div class="policy-box">
    <h3>Responding to a Routine Concern</h3>
    <ol>
      <li><strong>Document the concern.</strong> Preserve relevant student work, communications, assignment instructions, or other information connected to the concern.</li>
      <li><strong>Meet with the student.</strong> Explain the concern, discuss what occurred, and give the student an opportunity to respond.</li>
      <li><strong>Consult when needed.</strong> Faculty may contact the department chair to discuss the concern, clarify next steps, or seek guidance before moving forward with a formal referral or academic misconduct process.</li>
      <li><strong>Follow the current CT State process.</strong> When appropriate, use the relevant academic misconduct or student conduct procedures and institutional referral process.</li>
    </ol>
  </div>
  <div class="alert-box">
    <strong>Immediate Safety Concerns:</strong> If behavior involves an immediate threat, safety issue, or a situation in which meeting privately with the student would not be appropriate, do not wait for a student conference before contacting the appropriate college office or emergency resource.
  </div>
  <p>The <a href="https://ctstate.edu/conduct" target="_blank" rel="noopener">CT State Conduct page</a> provides the Student Code of Conduct, Student Conduct Referral, and academic misconduct resources. The <a href="https://catalog.ctstate.edu/academic-policies-procedures/expectation-academic-integrity/" target="_blank" rel="noopener">Academic Catalog's Expectation of Academic Integrity</a> provides the current academic integrity policy.</p>
</div>

<div class="section">
  <h2>CARE Referrals and Student Support</h2>
  <p>Use a Student Conduct Referral when a potential Student Code of Conduct violation has occurred. Use a CARE Referral when the primary concern is a student's wellbeing, need for support, or behavior that may benefit from connection to campus resources.</p>
  <div class="info-box">
    <strong>Emergency situations:</strong> A CARE Referral does not provide an immediate emergency response. If a situation requires immediate medical, psychological, or police assistance, use the appropriate emergency resource.
  </div>
  <p>Current links for CARE referrals, conduct reports, disability services, tutoring, advising, and other student supports are available through <a href="https://ctstate.edu/for-you/faculty-staff" target="_blank" rel="noopener">CT State Faculty &amp; Staff Resources</a> and <a href="https://ctstate.edu/ss-links" target="_blank" rel="noopener">Student Services Quick Links</a>.</p>
</div>

<div class="section">
  <h2>Campus Closures and Emergencies</h2>
  <p>Faculty should follow official CT State notifications regarding campus closures, delayed openings, emergency conditions, and changes to college operations. Students should also be encouraged to use CT State's official alert system.</p>
  <p>See <a href="https://ctstate.edu/safety" target="_blank" rel="noopener">CT State Police and Public Safety</a> for current safety information and CT State Alerts.</p>
</div>

<div class="section">
  <h2>Current CT State Policy Resources</h2>
  <p>Institutional policies and procedures can change. The following resources should be treated as the current source of truth when questions arise:</p>
  <div class="checklist-box">
    <ul>
      <li><a href="https://ctstate.edu/for-you/faculty-staff" target="_blank" rel="noopener"><strong>Faculty &amp; Staff Resources</strong></a> - academic engagement guidance, faculty forms, student-support links, and other faculty resources.</li>
      <li><a href="https://ctstate.edu/academics/academic-calendar" target="_blank" rel="noopener"><strong>Academic Calendar</strong></a> - current session dates and reporting deadlines.</li>
      <li><a href="https://catalog.ctstate.edu/" target="_blank" rel="noopener"><strong>2026-2027 Academic Catalog</strong></a> - current academic policies, grading information, FERPA resources, and academic integrity standards.</li>
      <li><a href="https://ctstate.edu/conduct" target="_blank" rel="noopener"><strong>Conduct</strong></a> - Student Code of Conduct, conduct referrals, and academic misconduct resources.</li>
      <li><a href="https://ctstate.edu/safety" target="_blank" rel="noopener"><strong>Police and Public Safety</strong></a> - emergency information and CT State Alerts.</li>
    </ul>
  </div>
</div>
''', 'html.parser')

content.clear()
for node in list(fragment.contents):
    content.append(node)

# Remove decorative Home icon on this revised page.
for a in soup.find_all('a'):
    if a.get_text(strip=True) == '🏠 Home':
        a.string = 'Home'

# Add page-specific breathing room without disturbing existing responsive layout.
style = soup.find('style')
if style is None:
    raise SystemExit('style element not found')
spacing = '''

        /* Publication spacing for policy page */
        .content > .intro-section,
        .content > .section { margin-bottom: 68px; }
        .content > .section:last-child { margin-bottom: 0; }
        .content p { margin-bottom: 22px; }
        .content h2 { margin-bottom: 28px; }
        .content h3 { margin-top: 34px; margin-bottom: 18px; }
        .content .info-box,
        .content .policy-box,
        .content .alert-box,
        .content .checklist-box { margin-top: 28px; margin-bottom: 34px; }
        .content ul,
        .content ol { margin-top: 16px; margin-bottom: 20px; padding-left: 34px; }
        .content li { margin-bottom: 10px; line-height: 1.65; }
'''
style.append(spacing)

# Refresh the footer revision label if the old one is present.
text = str(soup)
text = text.replace("Scholar's Compass Project | Last Updated: November 2024", "Scholar's Compass Project | Revised for publication: August 2026")
p.write_text(text, encoding='utf-8')
