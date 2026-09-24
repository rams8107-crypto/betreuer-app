(() => {
  const STORAGE_KEY = "gbb-lernen-progress-v1";
  const AUTH_KEY = "gbb-lernen-auth-v1";
  const EXPECTED_USER = "ramazan";
  const EXPECTED_PASS = "GBBprivat26";

  const gate = document.getElementById("gate");
  const appShell = document.getElementById("appShell");
  const app = document.getElementById("app");
  const tabbar = document.getElementById("tabbar");
  const loginForm = document.getElementById("loginForm");
  const gateError = document.getElementById("gateError");

  const state = {
    route: "home",
    modules: [],
    meta: null,
    module: null,
    quiz: null,
    quizIndex: 0,
    selections: {},
    review: null,
    loading: true,
    error: null,
  };

  function isAuthed() {
    try {
      return sessionStorage.getItem(AUTH_KEY) === "ok";
    } catch {
      return false;
    }
  }

  function setAuthed() {
    sessionStorage.setItem(AUTH_KEY, "ok");
  }

  function loadProgress() {
    try {
      return JSON.parse(localStorage.getItem(STORAGE_KEY) || "{}");
    } catch {
      return {};
    }
  }

  function saveProgress(data) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(data));
  }

  function moduleProgress(id) {
    const p = loadProgress()[String(id)] || {};
    return {
      cardsDone: !!p.cardsDone,
      bestPercent: p.bestPercent || 0,
      passed: !!p.passed,
      attempts: p.attempts || 0,
    };
  }

  function markCardsDone(id) {
    const all = loadProgress();
    const cur = all[String(id)] || {};
    cur.cardsDone = true;
    all[String(id)] = cur;
    saveProgress(all);
  }

  function markQuizResult(id, percent, passed) {
    const all = loadProgress();
    const cur = all[String(id)] || {};
    cur.attempts = (cur.attempts || 0) + 1;
    cur.bestPercent = Math.max(cur.bestPercent || 0, percent);
    cur.passed = cur.passed || passed;
    all[String(id)] = cur;
    saveProgress(all);
  }

  function overallProgress() {
    if (!state.modules.length) return { done: 0, total: 0, percent: 0 };
    const total = state.modules.length;
    const done = state.modules.filter((m) => moduleProgress(m.id).passed).length;
    return { done, total, percent: Math.round((done / total) * 100) };
  }

  function continueModuleId() {
    const unfinished = state.modules.find((m) => !moduleProgress(m.id).passed);
    return unfinished ? unfinished.id : state.modules[0]?.id || 1;
  }

  function getFullModule(id) {
    return state.fullModules.find((m) => m.id === id) || null;
  }

  function listSummary() {
    return state.fullModules.map((m) => ({
      id: m.id,
      title: m.title,
      hours: m.hours,
      area: m.area,
      summary: m.summary,
      topic_count: m.topics.length,
      card_count: m.cards.length,
      quiz_count: m.quiz.length,
    }));
  }

  async function boot() {
    try {
      const res = await fetch("static/data.json", { cache: "no-store" });
      if (!res.ok) throw new Error("Lerninhalt konnte nicht geladen werden.");
      const data = await res.json();
      state.fullModules = data.modules;
      state.meta = data.meta;
      state.modules = listSummary();
      state.loading = false;
      render();
    } catch (err) {
      state.loading = false;
      state.error = err.message;
      render();
    }
  }

  function setRoute(route) {
    state.route = route;
    state.error = null;
    if (route !== "quiz" && route !== "result") {
      state.quiz = null;
      state.review = null;
      state.selections = {};
      state.quizIndex = 0;
    }
    render();
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  function updateTabs() {
    const active =
      state.route === "home"
        ? "home"
        : state.route === "progress"
          ? "progress"
          : "modules";
    tabbar.querySelectorAll(".tab").forEach((btn) => {
      btn.classList.toggle("is-active", btn.dataset.route === active);
    });
  }

  function escapeHtml(str) {
    return String(str)
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;");
  }

  function renderHome() {
    const prog = overallProgress();
    const nextId = continueModuleId();
    return `
      <section class="screen">
        <div class="hero">
          <h1 class="brand">GBB Lernen</h1>
          <p class="hero-line">Sachkunde für gesetzliche Berufsbetreuung</p>
          <p class="hero-sub">Alle Unterrichtsinhalte der BtRegV-Anlage – Originalpunkte mit Lerntext und Quiz.</p>
          <div class="cta-row">
            <button class="btn btn-primary" data-action="open-module" data-id="${nextId}">Weiterlernen</button>
            <button class="btn btn-ghost" data-action="go" data-route="modules">Alle Module</button>
          </div>
        </div>
        <div class="panel after-hero">
          <div class="stat-line">
            <div class="stat"><strong>${prog.percent}%</strong><span>Module bestanden</span></div>
            <div class="stat"><strong>${state.meta?.total_hours || 270}</strong><span>Zeitstunden (Lehrgang)</span></div>
            <div class="stat"><strong>${state.meta?.total_official_topics || state.meta?.total_questions || 0}</strong><span>Original-Inhalte</span></div>
            <div class="stat"><strong>${state.meta?.total_questions || 0}</strong><span>Quizfragen</span></div>
          </div>
          <p class="disclaimer">${escapeHtml(state.meta?.disclaimer || "")}</p>
          ${state.meta?.source ? `<p class="disclaimer"><a href="${state.meta.source.pdf_url}" target="_blank" rel="noopener">Original-PDF BtRegV (gesetze-im-internet.de)</a> · ${escapeHtml(state.meta.source.citation || "")}</p>` : ""}
        </div>
      </section>
    `;
  }

  function renderModules() {
    const rows = state.modules
      .map((m) => {
        const p = moduleProgress(m.id);
        const badge = p.passed
          ? `<span class="badge">Bestanden ${p.bestPercent}%</span>`
          : p.bestPercent
            ? `<span class="badge warn">Bestwert ${p.bestPercent}%</span>`
            : "";
        return `
          <button class="module-row" data-action="open-module" data-id="${m.id}">
            <div class="mod-num">${m.id}</div>
            <div class="mod-body">
              <h3>${escapeHtml(m.title)}</h3>
              <p>${escapeHtml(m.area)} · ${m.quiz_count} Fragen</p>
              ${badge}
            </div>
            <div class="mod-meta">${m.hours} Std.</div>
          </button>
        `;
      })
      .join("");

    return `
      <section class="screen panel">
        <h2 class="section-title">Module</h2>
        <p class="lede">Inhaltliche Anforderungen an die Sachkunde – Anlage zu § 3 Abs. 4 BtRegV.</p>
        <div class="module-list">${rows}</div>
      </section>
    `;
  }

  function renderProgress() {
    const prog = overallProgress();
    const rows = state.modules
      .map((m) => {
        const p = moduleProgress(m.id);
        return `
          <div class="learn-card">
            <strong>Modul ${m.id}: ${escapeHtml(m.title)}</strong>
            <div class="progress-bar"><span style="width:${p.bestPercent}%"></span></div>
            <p>${p.passed ? "Bestanden" : "Offen"} · ${p.attempts} Versuch${p.attempts === 1 ? "" : "e"} · Bestwert ${p.bestPercent}%</p>
          </div>
        `;
      })
      .join("");

    return `
      <section class="screen panel">
        <h2 class="section-title">Fortschritt</h2>
        <p class="lede">${prog.done} von ${prog.total} Modulen mit mindestens 60 % bestanden.</p>
        <div class="progress-bar" style="height:14px;margin-bottom:18px"><span style="width:${prog.percent}%"></span></div>
        <div class="card-stack">${rows}</div>
        <button class="btn btn-soft" data-action="reset-progress" style="width:100%;margin-top:8px">Fortschritt zurücksetzen</button>
      </section>
    `;
  }

function renderModuleDetail() {
    const m = state.module;
    if (!m) {
      return `
        <section class="screen">
          <div class="topbar">
            <button class="back" data-action="go" data-route="modules" aria-label="Zurück">←</button>
            <h2>Modul</h2>
          </div>
          <div class="panel"><p class="lede">Modul wird geladen…</p></div>
        </section>`;
    }
    const p = moduleProgress(m.id);
    const lessons = (m.lessons || (m.topics || []).map((t) => ({ title: t, body: "" })))
      .map(
        (lesson, idx) => `
        <article class="learn-card">
          <strong>${idx + 1}. ${escapeHtml(lesson.title || lesson)}</strong>
          ${lesson.body ? `<p>${escapeHtml(lesson.body)}</p>` : ""}
        </article>`
      )
      .join("");

    return `
      <section class="screen">
        <div class="topbar">
          <button class="back" data-action="go" data-route="modules" aria-label="Zurück">←</button>
          <h2>Modul ${m.id}</h2>
        </div>
        <div class="panel">
          <h2 class="section-title">${escapeHtml(m.title)}</h2>
          <p class="lede">${escapeHtml(m.summary)} · ${m.hours} Zeitstunden${m.legal_ref ? ` · ${escapeHtml(m.legal_ref)}` : ""}</p>
          ${p.passed ? `<span class="badge">Quiz bestanden (${p.bestPercent}%)</span>` : ""}
          <h3 class="section-title" style="font-size:1.15rem;margin-top:20px">Unterrichtsinhalte (BtRegV-Anlage, Original)</h3>
          <p class="lede">Alle Punkte aus der amtlichen Anlage – mit Lerntext zur Wiederholung.</p>
          <div class="card-stack">${lessons}</div>
          <div class="cta-row" style="margin-top:8px">
            <button class="btn btn-ink" data-action="start-quiz" data-id="${m.id}">Quiz starten (${(m.quiz || []).length || m.quiz_count || 0} Fragen)</button>
          </div>
        </div>
      </section>
    `;
  }

  function renderQuiz() {
    const q = state.quiz.questions[state.quizIndex];
    const total = state.quiz.questions.length;
    const pct = Math.round((state.quizIndex / total) * 100);
    const selected = state.selections[q.id];
    const options = q.options
      .map(
        (opt, idx) => `
        <button class="option ${selected === idx ? "is-selected" : ""}" data-action="select-option" data-idx="${idx}">
          ${escapeHtml(opt)}
        </button>`
      )
      .join("");

    return `
      <section class="screen">
        <div class="topbar">
          <button class="back" data-action="open-module" data-id="${state.quiz.module_id}" aria-label="Zurück">←</button>
          <h2>Quiz · ${state.quizIndex + 1}/${total}</h2>
        </div>
        <div class="panel">
          <div class="quiz-progress"><i style="width:${pct}%"></i></div>
          <p class="q-text">${escapeHtml(q.question)}</p>
          <div class="options">${options}</div>
          <div class="cta-row" style="margin-top:18px">
            <button class="btn btn-ink" data-action="next-question" ${selected == null ? "disabled" : ""}>
              ${state.quizIndex + 1 === total ? "Auswerten" : "Weiter"}
            </button>
          </div>
        </div>
      </section>
    `;
  }

  function renderResult() {
    const r = state.review;
    const cls = r.passed ? "pass" : "fail";
    const details = r.results
      .map((item, i) => {
        const q = state.quiz.questions.find((x) => x.id === item.question_id);
        return `
          <article class="learn-card">
            <strong>${i + 1}. ${escapeHtml(q?.question || "")}</strong>
            <p>${item.is_correct ? "Richtig" : "Falsch"} · ${escapeHtml(item.explain)}</p>
          </article>`;
      })
      .join("");

    return `
      <section class="screen">
        <div class="result-hero">
          <p>Modul ${r.module_id}</p>
          <div class="score ${cls}">${r.percent}%</div>
          <p class="${cls}">${r.correct} von ${r.total} richtig · ${r.passed ? "Bestanden" : "Noch nicht bestanden (60 % nötig)"}</p>
        </div>
        <div class="panel">
          <div class="card-stack">${details}</div>
          <div class="cta-row" style="margin-top:12px;display:grid">
            <button class="btn btn-ink" data-action="start-quiz" data-id="${r.module_id}">Nochmal üben</button>
            <button class="btn btn-soft" data-action="go" data-route="modules">Zur Modulübersicht</button>
          </div>
        </div>
      </section>
    `;
  }

  function render() {
    updateTabs();
    if (state.loading) {
      app.innerHTML = `<section class="screen panel"><p>Laden…</p></section>`;
      return;
    }
    if (state.error) {
      app.innerHTML = `<section class="screen panel"><p>${escapeHtml(state.error)}</p></section>`;
      return;
    }

    let html = "";
    switch (state.route) {
      case "home":
        html = renderHome();
        break;
      case "modules":
        html = renderModules();
        break;
      case "progress":
        html = renderProgress();
        break;
      case "module":
        html = renderModuleDetail();
        break;
      case "quiz":
        html = renderQuiz();
        break;
      case "result":
        html = renderResult();
        break;
      default:
        html = renderHome();
    }
    app.innerHTML = html;
  }

  function openModule(id) {
    state.route = "module";
    state.module = getFullModule(id);
    markCardsDone(id);
    render();
  }

  function startQuiz(id) {
    const module = getFullModule(id);
    if (!module) return;
    state.quiz = {
      module_id: id,
      title: module.title,
      questions: module.quiz.map((q) => ({
        id: q.id,
        question: q.question,
        options: q.options,
        correct: q.correct,
        explain: q.explain,
      })),
    };
    state.quizIndex = 0;
    state.selections = {};
    state.review = null;
    state.route = "quiz";
    render();
  }

  function submitQuiz() {
    const questions = state.quiz.questions;
    let correctCount = 0;
    const results = questions.map((q) => {
      const selected = state.selections[q.id];
      const isCorrect = selected === q.correct;
      if (isCorrect) correctCount += 1;
      return {
        question_id: q.id,
        selected,
        correct_index: q.correct,
        is_correct: isCorrect,
        explain: q.explain,
      };
    });
    const total = questions.length;
    const percent = total ? Math.round((correctCount / total) * 100) : 0;
    const passed = percent >= 60;
    markQuizResult(state.quiz.module_id, percent, passed);
    state.review = {
      module_id: state.quiz.module_id,
      correct: correctCount,
      total,
      percent,
      passed,
      results,
    };
    state.route = "result";
    render();
  }

  function showApp() {
    gate.classList.add("hidden");
    appShell.classList.remove("hidden");
    boot();
  }

  loginForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const user = document.getElementById("user").value.trim();
    const pass = document.getElementById("pass").value;
    if (user === EXPECTED_USER && pass === EXPECTED_PASS) {
      setAuthed();
      gateError.textContent = "";
      showApp();
    } else {
      gateError.textContent = "Benutzer oder Passwort falsch.";
    }
  });

  tabbar.addEventListener("click", (e) => {
    const btn = e.target.closest("[data-route]");
    if (!btn) return;
    setRoute(btn.dataset.route);
  });

  app.addEventListener("click", (e) => {
    const el = e.target.closest("[data-action]");
    if (!el) return;
    const action = el.dataset.action;

    if (action === "go") setRoute(el.dataset.route);
    if (action === "open-module") openModule(Number(el.dataset.id));
    if (action === "start-quiz") startQuiz(Number(el.dataset.id));
    if (action === "select-option") {
      const q = state.quiz.questions[state.quizIndex];
      state.selections[q.id] = Number(el.dataset.idx);
      render();
    }
    if (action === "next-question") {
      const q = state.quiz.questions[state.quizIndex];
      if (state.selections[q.id] == null) return;
      if (state.quizIndex + 1 >= state.quiz.questions.length) {
        submitQuiz();
      } else {
        state.quizIndex += 1;
        render();
      }
    }
    if (action === "reset-progress") {
      if (confirm("Gesamten Lernfortschritt wirklich löschen?")) {
        localStorage.removeItem(STORAGE_KEY);
        render();
      }
    }
  });

  if (isAuthed()) showApp();
})();
