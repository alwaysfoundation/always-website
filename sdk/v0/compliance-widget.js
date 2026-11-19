/*
 * <always-compliance-check>: the free Always Compliance check-up, for any site or app.
 * Always Compliance is a module of Always Platform. https://alwaysfoundation.org/#/compliance
 *
 *   <script type="module" src="https://alwaysfoundation.org/sdk/v0/compliance-widget.js"></script>
 *   <always-compliance-check accent="#5B67D8"></always-compliance-check>
 *
 * Answers stay in the browser apart from the stateless check-up call, and nothing is stored.
 * No token, no cookies, no tracking. A guide to common obligations, not legal advice.
 * Licence: Apache-2.0.
 */
const STATES = ['NSW', 'VIC', 'QLD', 'WA', 'SA', 'TAS', 'ACT', 'NT'];
const AREAS = { privacy: 'Privacy', child_safety: 'Child safety', charity: 'Charity', messages: 'Emails and texts' };
const STATUS = { attention: 'Needs attention', check: 'To check', upcoming: 'Coming', met: 'In place' };
const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' })[c]);

class AlwaysComplianceCheck extends HTMLElement {
  get api() { return (this.getAttribute('api') || 'https://alwaysfoundation.org/api/compliance').replace(/\/$/, ''); }

  async connectedCallback() {
    if (this.shadowRoot) return;
    const a = this.getAttribute('accent') || '';
    const accent = /^#[0-9a-f]{6}$/i.test(a) ? a : '#1B4740';
    this.root = this.attachShadow({ mode: 'open' });
    this.root.innerHTML = `<style>
      :host { --a: ${accent}; display: block; font: 16px/1.5 Inter, system-ui, -apple-system, sans-serif; color: #1E2A26; }
      .card { max-width: 680px; padding: 28px; border-radius: 22px; background: var(--always-surface, #FFFDF8); box-shadow: 0 1px 0 rgba(30,42,38,.06), 0 18px 40px -30px rgba(30,42,38,.35); }
      h2 { margin: 0 0 4px; font: 800 24px/1.2 Manrope, system-ui, sans-serif; letter-spacing: -0.01em; color: var(--a); }
      .sub { margin: 0 0 8px; color: #4E5F58; font-size: 15px; }
      fieldset { border: 0; margin: 0; padding: 16px 0; border-top: 1px solid #E9DFCF; }
      legend { padding: 0; font-weight: 700; } .help { margin: 2px 0 10px; font-size: 14px; color: #4E5F58; }
      .opts { display: flex; flex-wrap: wrap; gap: 8px; }
      .opts label { position: relative; display: inline-flex; cursor: pointer; }
      .opts input { position: absolute; inset: 0; opacity: 0; margin: 0; cursor: pointer; }
      .opts span { display: inline-flex; align-items: center; min-height: 44px; padding: 0 16px; border: 1px solid #D9D2C4; border-radius: 12px; font-weight: 600; font-size: 15px; }
      .opts input:checked + span { background: var(--a); border-color: var(--a); color: #fff; }
      .opts input:focus-visible + span { outline: 3px solid var(--a); outline-offset: 2px; }
      button.go { min-height: 48px; margin-top: 12px; padding: 0 22px; border: 0; border-radius: 14px; background: var(--a); color: #fff; font: 700 16px Inter, system-ui, sans-serif; cursor: pointer; }
      button.go:focus-visible, a:focus-visible { outline: 3px solid var(--a); outline-offset: 2px; }
      .err { color: #A4562A; font-size: 14px; min-height: 1.4em; margin: 8px 0 0; }
      .sum { display: flex; flex-wrap: wrap; gap: 20px; margin: 14px 0 6px; }
      .sum div { display: grid; } .sum b { font: 800 28px/1 Manrope, system-ui, sans-serif; color: var(--a); } .sum span { font-size: 13px; color: #4E5F58; }
      h3 { margin: 22px 0 6px; font: 700 13px/1 Manrope, system-ui, sans-serif; color: #A4562A; }
      ol { list-style: none; margin: 0; padding: 0; }
      li { padding: 14px 0; border-top: 1px solid #E9DFCF; }
      li .t { display: flex; justify-content: space-between; gap: 12px; align-items: baseline; }
      li b { font-weight: 700; } li em { flex: none; font-style: normal; font-size: 12px; font-weight: 700; color: #4E5F58; }
      li em.attention { color: #A4562A; } li em.met { color: var(--a); }
      li p { margin: 4px 0 0; font-size: 14.5px; color: #3E4D47; }
      li .law { font-size: 13px; } li .law a { color: var(--a); }
      .tag { font-size: 12px; color: #4E5F58; }
      .foot { margin-top: 20px; padding-top: 14px; border-top: 1px solid #E9DFCF; font-size: 13px; color: #4E5F58; }
      .foot a { color: var(--a); font-weight: 600; }
      .again { background: none; border: 0; padding: 0; color: var(--a); font: 600 14px Inter, system-ui, sans-serif; text-decoration: underline; cursor: pointer; margin-top: 12px; }
    </style><div class="card" aria-live="polite"><p class="sub">Loading the check-up…</p></div>`;
    try {
      const r = await fetch(`${this.api}/register`);
      if (!r.ok) throw new Error();
      this.register = await r.json();
      this.form();
    } catch {
      this.card.innerHTML = '<p class="sub">The check-up could not load. Please try again later.</p>';
    }
  }

  get card() { return this.root.querySelector('.card'); }

  form() {
    const qs = this.register.profileQuestions;
    const f = (q) => `<fieldset><legend>${esc(q.label)}</legend>${q.help ? `<p class="help">${esc(q.help)}</p>` : ''}<div class="opts">${
      q.type === 'states'
        ? STATES.map((s) => `<label><input type="checkbox" name="${esc(q.id)}" value="${s}"><span>${s}</span></label>`).join('')
        : `<label><input type="radio" name="${esc(q.id)}" value="yes"><span>Yes</span></label><label><input type="radio" name="${esc(q.id)}" value="no"><span>No</span></label>`
    }</div></fieldset>`;
    this.card.innerHTML = `<h2>Free compliance check-up</h2><p class="sub">About five minutes. Nothing is saved.</p><form novalidate>${qs.map(f).join('')}<button class="go" type="submit">See what applies to us</button><p class="err" role="alert"></p></form>`;
    const form = this.root.querySelector('form');
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const d = new FormData(form), profile = {}, missing = [];
      for (const q of qs) {
        if (q.type === 'states') { profile[q.id] = d.getAll(q.id).map(String); if (!profile[q.id].length) missing.push(q.label); }
        else { const v = d.get(q.id); if (!v) missing.push(q.label); profile[q.id] = v === 'yes'; }
      }
      const err = form.querySelector('.err');
      if (missing.length) { err.textContent = `Please answer every question. First unanswered: ${missing[0]}`; return; }
      err.textContent = 'Checking…';
      try {
        const r = await fetch(`${this.api}/check`, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify({ profile }) });
        if (!r.ok) throw new Error();
        this.result(await r.json());
      } catch { err.textContent = 'Something went wrong. Please try again.'; }
    });
  }

  result(r) {
    const groups = Object.keys(AREAS).map((k) => [k, r.items.filter((i) => i.area === k)]).filter(([, l]) => l.length);
    const item = (i) => `<li><div class="t"><b>${esc(i.title)}</b><em class="${i.status}">${STATUS[i.status]}</em></div>
      <p>${esc(i.summary)}</p><p class="tag">${i.strength === 'required' ? 'Required' : 'Recommended'}${i.commences ? ` · from ${esc(i.commences)}` : ''}</p>
      ${i.law?.length ? `<p class="law">${i.law.map((l) => `<a href="${esc(l.url)}" target="_blank" rel="noopener">${esc(l.name)}</a>`).join(' · ')}</p>` : ''}</li>`;
    this.card.innerHTML = `<h2>${r.summary.required} required for your ministry</h2>
      <p class="sub">${r.items.length} obligations apply in total. Work through each one with your team.</p>
      <div class="sum"><div><b>${r.summary.required}</b><span>Required</span></div><div><b>${r.items.length - r.summary.required}</b><span>Recommended</span></div><div><b>${r.summary.upcoming}</b><span>Coming</span></div></div>
      ${groups.map(([k, l]) => `<h3>${AREAS[k]}</h3><ol>${l.map(item).join('')}</ol>`).join('')}
      <button type="button" class="again">Start again</button>
      <p class="foot">${esc(r.notice)} Register version ${esc(r.registerVersion)}. <a href="https://alwaysfoundation.org/#/compliance" target="_blank" rel="noopener">Always Compliance</a>, a module of Always Platform.</p>`;
    this.root.querySelector('.again').addEventListener('click', () => this.form());
    this.dispatchEvent(new CustomEvent('always-compliance-result', { detail: { summary: r.summary, registerVersion: r.registerVersion }, bubbles: true, composed: true }));
  }
}

if (!customElements.get('always-compliance-check')) customElements.define('always-compliance-check', AlwaysComplianceCheck);
