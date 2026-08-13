(() => {
  'use strict';

  // Match Scholar's Compass chapter typography at the rendered-text level.
  // This deliberately overrides older page-specific CSS that otherwise shrinks prose to 16px.
  const typography = document.createElement('style');
  typography.dataset.fgTypography = 'scholars-compass';
  typography.textContent = `
    body {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
      font-size: 18px !important;
      line-height: 1.6 !important;
    }
    #main-content p,
    #main-content li,
    #main-content td,
    #main-content th {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
      font-size: 18px !important;
      line-height: 1.6 !important;
      font-weight: 400 !important;
    }
    #main-content .fg-quick-reference li { font-size: 18px !important; }
    #main-content .fg-hub-group > p { font-size: 16.5px !important; }
    #main-content .fg-breadcrumb { font-size: 15px !important; }
    #main-content .fg-page-nav-label { font-size: 13px !important; }
    @media (max-width: 520px) {
      body,
      #main-content p,
      #main-content li,
      #main-content td,
      #main-content th { font-size: 18px !important; }
    }
  `;
  document.head.appendChild(typography);

  const pages = [
    { href: 'index.html', title: 'Faculty Guide Hub', section: 'Home', description: 'Overview, quick reference, and navigation for the ENG 1010 Faculty Guide.' },
    { href: 'getting-started.html', title: 'Getting Started', section: 'Getting Started', description: 'Orientation, mission, guiding principles, and first steps for ENG 1010 faculty.' },
    { href: 'course-overview.html', title: 'Course Overview', section: 'Getting Started', description: 'Official course description, student learning outcomes, required text, and course expectations.' },
    { href: 'corequisite-model.html', title: 'Corequisite Model', section: 'Getting Started', description: 'ENG 1010 and ENG 0910 structure, placement guidance, and workshop support.' },
    { href: 'module-guide.html', title: 'Module Guide', section: 'Planning & Teaching', description: 'A flexible sample framework for organizing the semester.' },
    { href: 'assignments.html', title: 'Assignments', section: 'Planning & Teaching', description: 'Recommended assignment sequence, sample prompts, scaffolding, and planning guidance.' },
    { href: 'instructional-strategies.html', title: 'Teaching Strategies', section: 'Planning & Teaching', description: 'Practical approaches for reading, writing, revision, active learning, and student support.' },
    { href: 'assessment.html', title: 'Assessment', section: 'Planning & Teaching', description: 'Sample rubrics, grading approaches, feedback, revision, and portfolio options.' },
    { href: 'syllabus-templates.html', title: 'Syllabus Guidance', section: 'Resources', description: 'ENG 1010 syllabus guidance and links to current CT State resources.' },
    { href: 'policies.html', title: 'Policies', section: 'Resources', description: 'Three Rivers procedures and current CT State policy guidance for ENG 1010 faculty.' },
    { href: 'ai-policy.html', title: 'Artificial Intelligence in ENG 1010', section: 'Resources', description: 'Guidance for course AI policies, teaching, student use, and academic integrity.' },
    { href: 'faculty-support.html', title: 'Faculty Support', section: 'Resources', description: 'ENG 1010 contacts, Three Rivers student support, and faculty resources.' }
  ];

  const current = location.pathname.split('/').pop() || 'index.html';
  const body = document.body;

  const menuButton = document.querySelector('[data-fg-menu]');
  if (menuButton) {
    menuButton.addEventListener('click', () => {
      const open = body.classList.toggle('fg-menu-open');
      menuButton.setAttribute('aria-expanded', String(open));
    });
  }

  document.querySelectorAll('[data-fg-group-toggle]').forEach((button) => {
    button.addEventListener('click', (event) => {
      event.preventDefault();
      const group = button.closest('.fg-nav-group');
      const wasOpen = group.classList.contains('is-open');
      document.querySelectorAll('.fg-nav-group.is-open').forEach((item) => {
        if (item !== group) {
          item.classList.remove('is-open');
          const b = item.querySelector('[data-fg-group-toggle]');
          if (b) b.setAttribute('aria-expanded', 'false');
        }
      });
      group.classList.toggle('is-open', !wasOpen);
      button.setAttribute('aria-expanded', String(!wasOpen));
    });
  });

  document.addEventListener('click', (event) => {
    if (!event.target.closest('.fg-nav-group') && window.innerWidth > 860) {
      document.querySelectorAll('.fg-nav-group.is-open').forEach((group) => {
        group.classList.remove('is-open');
        const button = group.querySelector('[data-fg-group-toggle]');
        if (button) button.setAttribute('aria-expanded', 'false');
      });
    }
  });

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      body.classList.remove('fg-menu-open');
      if (menuButton) menuButton.setAttribute('aria-expanded', 'false');
      document.querySelectorAll('.fg-nav-group.is-open').forEach((group) => {
        group.classList.remove('is-open');
        const button = group.querySelector('[data-fg-group-toggle]');
        if (button) button.setAttribute('aria-expanded', 'false');
      });
      closeSearch();
    }
    if (event.key === '/' && !/input|textarea|select/i.test(document.activeElement?.tagName || '')) {
      event.preventDefault();
      openSearch();
    }
  });

  const root = document.documentElement;
  const themeButton = document.querySelector('[data-fg-theme]');
  const savedTheme = localStorage.getItem('fg-theme');
  if (savedTheme === 'dark' || savedTheme === 'light') {
    root.dataset.theme = savedTheme;
  } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    root.dataset.theme = 'dark';
  }
  updateThemeButton();

  if (themeButton) {
    themeButton.addEventListener('click', () => {
      root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
      localStorage.setItem('fg-theme', root.dataset.theme);
      updateThemeButton();
    });
  }

  function updateThemeButton() {
    if (!themeButton) return;
    const dark = root.dataset.theme === 'dark';
    themeButton.setAttribute('aria-label', dark ? 'Use light theme' : 'Use dark theme');
    const icon = themeButton.querySelector('.fg-icon');
    if (icon) icon.textContent = dark ? '☀' : '◐';
  }

  const backdrop = document.querySelector('[data-fg-search-backdrop]');
  const input = document.querySelector('[data-fg-search-input]');
  const results = document.querySelector('[data-fg-search-results]');
  const searchButtons = document.querySelectorAll('[data-fg-search-open]');
  const closeButton = document.querySelector('[data-fg-search-close]');
  let previousFocus = null;

  searchButtons.forEach((button) => button.addEventListener('click', openSearch));
  if (closeButton) closeButton.addEventListener('click', closeSearch);
  if (backdrop) {
    backdrop.addEventListener('click', (event) => {
      if (event.target === backdrop) closeSearch();
    });
  }
  if (input) input.addEventListener('input', () => renderSearch(input.value));

  function openSearch() {
    if (!backdrop || !input) return;
    previousFocus = document.activeElement;
    backdrop.classList.add('is-open');
    backdrop.setAttribute('aria-hidden', 'false');
    input.value = '';
    renderSearch('');
    requestAnimationFrame(() => input.focus());
  }

  function closeSearch() {
    if (!backdrop) return;
    backdrop.classList.remove('is-open');
    backdrop.setAttribute('aria-hidden', 'true');
    if (previousFocus && typeof previousFocus.focus === 'function') previousFocus.focus();
  }

  function renderSearch(query) {
    if (!results) return;
    const q = query.trim().toLowerCase();
    const matches = pages.filter((page) => {
      const haystack = `${page.title} ${page.section} ${page.description}`.toLowerCase();
      return !q || haystack.includes(q);
    });
    results.replaceChildren();
    if (!matches.length) {
      const empty = document.createElement('div');
      empty.className = 'fg-search-empty';
      empty.textContent = 'No Faculty Guide pages match that search.';
      results.append(empty);
      return;
    }
    matches.forEach((page) => {
      const link = document.createElement('a');
      link.className = 'fg-search-result';
      link.href = page.href;
      const strong = document.createElement('strong');
      strong.textContent = page.title;
      const span = document.createElement('span');
      span.textContent = `${page.section} · ${page.description}`;
      link.append(strong, span);
      results.append(link);
    });
  }

  const backTop = document.querySelector('[data-fg-back-top]');
  if (backTop) {
    const toggleBackTop = () => backTop.classList.toggle('is-visible', window.scrollY > 650);
    window.addEventListener('scroll', toggleBackTop, { passive: true });
    toggleBackTop();
    backTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));
  }

  document.querySelectorAll('.fg-dropdown a, .fg-nav-home').forEach((link) => {
    const href = link.getAttribute('href');
    if (href === current || (current === '' && href === 'index.html')) link.setAttribute('aria-current', 'page');
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 860) {
      body.classList.remove('fg-menu-open');
      if (menuButton) menuButton.setAttribute('aria-expanded', 'false');
    }
  });
})();
