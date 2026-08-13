(() => {
  'use strict';

  const pages = [
    { href: 'index.html', title: 'Home', section: 'Home', description: 'Overview, quick reference, and navigation for the ENG 1010 Faculty Guide.' },
    { href: 'getting-started.html', title: 'Getting Started', section: 'Getting Started', description: 'Orientation, mission, guiding principles, and first steps for ENG 1010 faculty.' },
    { href: 'quick-start.html', title: 'Quick Start', section: 'Getting Started', description: 'Fast-start planning resources, sample syllabi and course calendars, and essential course links.' },
    { href: 'course-overview.html', title: 'Course Overview', section: 'Getting Started', description: 'Official course description, student learning outcomes, required text, and course expectations.' },
    { href: 'corequisite-model.html', title: 'Corequisite Model', section: 'Getting Started', description: 'ENG 1010 and ENG 0910 structure, placement guidance, grading scenarios, and workshop support.' },
    { href: 'module-guide.html', title: 'Course Planning Guide', section: 'Planning & Teaching', description: 'A flexible sample framework for organizing the semester.' },
    { href: 'assignments.html', title: 'Assignments', section: 'Planning & Teaching', description: 'Recommended assignment sequence, sample prompts, scaffolding, and planning guidance.' },
    { href: 'instructional-strategies.html', title: 'Teaching Strategies', section: 'Planning & Teaching', description: 'Practical approaches for reading, writing, revision, active learning, and student support.' },
    { href: 'assessment.html', title: 'Assessment', section: 'Planning & Teaching', description: 'Sample rubrics, grading approaches, feedback, revision, and portfolio options.' },
    { href: 'syllabus-templates.html', title: 'Syllabus Guidance', section: 'Resources', description: 'ENG 1010 syllabus guidance and links to current CT State resources.' },
    { href: 'policies.html', title: 'Policies', section: 'Resources', description: 'Class cancellation, incomplete grades, academic engagement, integrity, and current CT State policy guidance.' },
    { href: 'ai-policy.html', title: 'Artificial Intelligence in ENG 1010', section: 'Resources', description: 'Guidance for course AI policies, teaching, student use, and academic integrity.' },
    { href: 'faculty-support.html', title: 'Faculty Support', section: 'Resources', description: 'ENG 1010 contacts, Three Rivers student support, and faculty resources.' }
  ];

  const current = location.pathname.split('/').pop() || 'index.html';
  const body = document.body;
  let searchIndexPromise = null;

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
          item.querySelector('[data-fg-group-toggle]')?.setAttribute('aria-expanded', 'false');
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
        group.querySelector('[data-fg-group-toggle]')?.setAttribute('aria-expanded', 'false');
      });
    }
  });

  const root = document.documentElement;
  const themeButton = document.querySelector('[data-fg-theme]');
  const savedTheme = localStorage.getItem('fg-theme');
  if (savedTheme === 'dark' || savedTheme === 'light') root.dataset.theme = savedTheme;
  else if (window.matchMedia?.('(prefers-color-scheme: dark)').matches) root.dataset.theme = 'dark';
  updateThemeButton();

  themeButton?.addEventListener('click', () => {
    root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    localStorage.setItem('fg-theme', root.dataset.theme);
    updateThemeButton();
  });

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
  let previousFocus = null;

  document.querySelectorAll('[data-fg-search-open]').forEach((button) => button.addEventListener('click', openSearch));
  document.querySelector('[data-fg-search-close]')?.addEventListener('click', closeSearch);
  backdrop?.addEventListener('click', (event) => { if (event.target === backdrop) closeSearch(); });
  input?.addEventListener('input', () => renderSearch(input.value));

  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape') {
      body.classList.remove('fg-menu-open');
      menuButton?.setAttribute('aria-expanded', 'false');
      document.querySelectorAll('.fg-nav-group.is-open').forEach((group) => {
        group.classList.remove('is-open');
        group.querySelector('[data-fg-group-toggle]')?.setAttribute('aria-expanded', 'false');
      });
      closeSearch();
    }
    if (event.key === '/' && !/input|textarea|select/i.test(document.activeElement?.tagName || '')) {
      event.preventDefault();
      openSearch();
    }
  });

  function openSearch() {
    if (!backdrop || !input) return;
    previousFocus = document.activeElement;
    backdrop.classList.add('is-open');
    backdrop.setAttribute('aria-hidden', 'false');
    input.value = '';
    renderSearch('');
    buildSearchIndex();
    requestAnimationFrame(() => input.focus());
  }

  function closeSearch() {
    if (!backdrop) return;
    backdrop.classList.remove('is-open');
    backdrop.setAttribute('aria-hidden', 'true');
    if (previousFocus?.focus) previousFocus.focus();
  }

  function stem(word) {
    let w = word.toLowerCase().replace(/[^a-z0-9]/g, '');
    if (/^cancel(l)?(ing|ed|ation|ations)?$/.test(w) || w === 'cancellation' || w === 'cancellations') return 'cancel';
    if (w === 'classes') return 'class';
    if (w === 'syllabi') return 'syllabus';
    if (w === 'policies') return 'policy';
    if (w.length > 5 && w.endsWith('ing')) w = w.slice(0, -3);
    else if (w.length > 4 && w.endsWith('ed')) w = w.slice(0, -2);
    else if (w.length > 4 && w.endsWith('es')) w = w.slice(0, -2);
    else if (w.length > 3 && w.endsWith('s')) w = w.slice(0, -1);
    return w;
  }

  function tokens(text) {
    return (text.toLowerCase().match(/[a-z0-9]+/g) || []).map(stem).filter(Boolean);
  }

  function normalize(text) { return tokens(text).join(' '); }

  function buildSearchIndex() {
    if (searchIndexPromise) return searchIndexPromise;
    searchIndexPromise = Promise.all(pages.map(async (page) => {
      try {
        const response = await fetch(page.href, { cache: 'no-cache' });
        if (!response.ok) throw new Error(String(response.status));
        const html = await response.text();
        const doc = new DOMParser().parseFromString(html, 'text/html');
        const main = doc.querySelector('#main-content');
        const headings = [...(main?.querySelectorAll('h2,h3,h4,h5') || [])].map(el => el.textContent.trim()).filter(Boolean);
        const text = (main?.innerText || main?.textContent || '').replace(/\s+/g, ' ').trim();
        return { ...page, headings, text, normalized: normalize(`${page.title} ${page.section} ${page.description} ${headings.join(' ')} ${text}`) };
      } catch (error) {
        return { ...page, headings: [], text: page.description, normalized: normalize(`${page.title} ${page.section} ${page.description}`) };
      }
    }));
    return searchIndexPromise;
  }

  function excerptFor(page, queryTokens) {
    const text = page.text || page.description;
    const lower = text.toLowerCase();
    let best = -1;
    for (const raw of queryTokens) {
      const candidates = raw === 'cancel' ? ['cancel', 'cancell'] : [raw];
      for (const candidate of candidates) {
        const at = lower.indexOf(candidate);
        if (at >= 0 && (best < 0 || at < best)) best = at;
      }
    }
    if (best < 0) return page.description;
    const start = Math.max(0, best - 85);
    const end = Math.min(text.length, best + 180);
    return `${start ? '…' : ''}${text.slice(start, end).trim()}${end < text.length ? '…' : ''}`;
  }

  async function renderSearch(query) {
    if (!results) return;
    const q = query.trim();
    const index = await buildSearchIndex();
    const qTokens = tokens(q);

    let matches;
    if (!qTokens.length) {
      matches = index.slice(0, 8).map(page => ({ page, score: 0 }));
    } else {
      matches = index.map((page) => {
        const titleN = normalize(page.title);
        const headingN = normalize(page.headings.join(' '));
        const descN = normalize(page.description);
        const allTerms = qTokens.every(term => page.normalized.includes(term));
        if (!allTerms) return null;
        let score = 1;
        qTokens.forEach(term => {
          if (titleN.includes(term)) score += 12;
          if (headingN.includes(term)) score += 7;
          if (descN.includes(term)) score += 4;
          score += Math.min(5, page.normalized.split(term).length - 1);
        });
        return { page, score };
      }).filter(Boolean).sort((a,b) => b.score - a.score);
    }

    results.replaceChildren();
    if (!matches.length) {
      const empty = document.createElement('div');
      empty.className = 'fg-search-empty';
      empty.textContent = 'No Faculty Guide pages match that search. Try fewer or broader terms.';
      results.append(empty);
      return;
    }

    matches.slice(0, 10).forEach(({ page }) => {
      const link = document.createElement('a');
      link.className = 'fg-search-result';
      link.href = page.href;
      const strong = document.createElement('strong');
      strong.textContent = page.title;
      const meta = document.createElement('span');
      meta.className = 'fg-search-meta';
      meta.textContent = page.section;
      const excerpt = document.createElement('span');
      excerpt.className = 'fg-search-excerpt';
      excerpt.textContent = excerptFor(page, qTokens);
      link.append(strong, meta, excerpt);
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
      menuButton?.setAttribute('aria-expanded', 'false');
    }
  });
})();
