"""Always Safety: results, the board summary, and the signed-in area (#/mycompliance)."""
import json
import os

# Sign-in and saving go live once Supabase Auth sends through SES Sydney and the API is deployed.
ACCOUNTS_ON = os.environ.get('ALWAYS_ACCOUNTS') == '1'
SUPABASE_URL = 'https://scoitzteqsvomsghtxfe.supabase.co'
SUPABASE_KEY = 'sb_publishable_Wcgql0VPiQ54KREb48X_Ew_dk1U5yy-'

PAGE = '''<section class="page-hero cmy-hero"><div class="wrap">
  <p class="cmy-kick">Always Safety</p>
  <h1 class="cmy-h" id="cmy-title">Your safety check-up</h1>
  <p class="cmy-lead" id="cmy-lead">Save your check-up, approve it each quarter, and hear when a rule that applies to you changes.</p>
</div></section>
<section class="sec pg-sec cmy-sec"><div class="wrap"><div class="cmy" id="cmy" aria-live="polite"></div></div></section>
'''

CSS = '''
.cw-next { margin: 28px 0 8px; }
.cw-next h4, .cw-more-h { font: 800 20px/1.2 var(--head); color: var(--ink, #1E2B27); margin: 0 0 6px; letter-spacing: -.01em; }
.cw-next > p { margin: 0 0 16px; color: #4B5B55; }
.cw-steps { list-style: none; counter-reset: s; margin: 0; padding: 0; display: grid; gap: 12px; }
.cw-steps > li { counter-increment: s; position: relative; padding: 18px 20px 18px 64px; background: #fff; border: 1px solid #E6E1D6; border-radius: 18px; }
.cw-steps > li::before { content: counter(s); position: absolute; left: 18px; top: 18px; width: 32px; height: 32px; border-radius: 50%; display: grid; place-items: center; font: 800 15px/1 var(--head); background: #E9F0EC; color: #1D4A42; }
.cw-steps > li.att::before { background: #FBE6D8; color: #A14E22; }
.cw-steps h5 { font: 700 16px/1.35 var(--head); margin: 2px 0 6px; color: #1E2B27; }
.cw-steps p { margin: 0 0 8px; color: #3E4C47; font-size: 15px; line-height: 1.55; }
.cw-steps ul { margin: 0 0 8px; padding-left: 18px; color: #3E4C47; font-size: 14.5px; }
.cw-steps .cw-law { font-size: 13.5px; margin: 0; }
.cw-steps .cw-law a { min-height: 44px; display: inline-flex; align-items: center; }
.cw-clear { padding: 18px 20px; border-radius: 18px; background: #E9F0EC; color: #1D4A42; font-weight: 600; }
.cw-more { margin: 22px 0 0; border-top: 1px solid #E6E1D6; padding-top: 6px; }
.cw-more summary { cursor: pointer; min-height: 44px; display: flex; align-items: center; font: 700 16px/1.3 var(--head); color: #1D4A42; }
.cw-more[open] summary { margin-bottom: 12px; }
.cw-then { display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin: 30px 0 8px; }
.cw-then > div { background: #fff; border: 1px solid #E6E1D6; border-radius: 20px; padding: 22px; display: flex; flex-direction: column; gap: 10px; }
.cw-then h5 { font: 800 17px/1.25 var(--head); margin: 0; color: #1E2B27; }
.cw-then p { margin: 0; color: #4B5B55; font-size: 14.5px; line-height: 1.55; flex: 1; }
.cw-then .btn { align-self: flex-start; }
.cw-then .cw-save { background: #1D4A42; border-color: #1D4A42; }
.cw-then .cw-save h5, .cw-then .cw-save p { color: #F4EFE6; }
.cw-name { display: grid; gap: 6px; margin: 0 0 6px; }
.cw-name label { font: 600 14px/1.3 var(--head); color: #1E2B27; }
.cw-name input, .cmy input[type=email], .cmy input[type=text], .cmy select { font: 500 16px/1.3 inherit; padding: 12px 14px; min-height: 48px; border: 1.5px solid #D5CFC2; border-radius: 12px; background: #fff; color: #1E2B27; width: 100%; max-width: 420px; box-sizing: border-box; }
.cw-name input:focus, .cmy input:focus, .cmy select:focus { outline: 3px solid #E8A477; outline-offset: 1px; border-color: #1D4A42; }
@media (max-width: 860px) { .cw-then { grid-template-columns: 1fr; } }
@media (max-width: 560px) { .cw-steps > li { padding: 16px 16px 16px 56px; } .cw-steps > li::before { left: 14px; top: 16px; } }

/* Signed-in area */
.cmy-hero { padding-bottom: 36px; }
.cmy-kick { font: 700 15px/1.2 var(--head); color: #E8A477; margin: 0 0 10px; }
.cmy-h { font: 800 clamp(36px, 6vw, 60px)/1.02 var(--head); letter-spacing: -.03em; margin: 0 0 14px; color: #F4EFE6; }
.cmy-lead { font-size: 18px; line-height: 1.55; color: #CFE0D7; max-width: 620px; margin: 0; }
.cmy { max-width: 760px; }
.cmy-card { background: #fff; border: 1px solid #E6E1D6; border-radius: 24px; padding: 28px; display: grid; gap: 14px; }
.cmy-card h2 { font: 800 24px/1.2 var(--head); margin: 0; color: #1E2B27; letter-spacing: -.01em; }
.cmy-card p { margin: 0; color: #4B5B55; line-height: 1.6; }
.cmy-card form { display: grid; gap: 14px; background: transparent; border-radius: 0; padding: 0; color: inherit; }
.cmy-card .btn-ghost-dark { color: #1D4A42; }
.cmy .cmy-opts { display: flex; gap: 8px; flex-wrap: wrap; }
.cmy .cw-opt { position: relative; }
.cmy .cw-opt input { position: absolute; opacity: 0; inset: 0; margin: 0; cursor: pointer; }
.cmy .cw-opt span { display: inline-flex; align-items: center; justify-content: center; min-height: 44px; padding: 0 18px; border-radius: 999px; border: 1.5px solid rgba(27,71,64,.25); font: 600 15px/1 var(--head); color: var(--green); background: #fff; }
.cmy .cw-opt input:checked + span { background: var(--green); border-color: var(--green); color: var(--cream); }
.cmy .cw-opt input:focus-visible + span { outline: 3px solid var(--peach); outline-offset: 2px; }
.cmy-field { display: grid; gap: 6px; }
.cmy-field label, .cmy-field legend { font: 600 14px/1.3 var(--head); color: #1E2B27; }
.cmy-row { display: flex; gap: 10px; flex-wrap: wrap; align-items: center; }
.cmy-code { letter-spacing: .3em; font-variant-numeric: tabular-nums; max-width: 220px !important; }
.cmy-err { color: #A14E22; font-weight: 600; min-height: 1.2em; margin: 0; }
.cmy-note { font-size: 14px; color: #6B7A74 !important; }
.cmy-steps { list-style: none; margin: 0; padding: 0; display: flex; gap: 8px; flex-wrap: wrap; }
.cmy-steps li { padding: 6px 12px; border-radius: 99px; background: #EFEBE3; font: 600 13px/1.3 var(--head); color: #6B7A74; }
.cmy-steps li.on { background: #1D4A42; color: #F4EFE6; }
.cmy-steps li.done { background: #E9F0EC; color: #1D4A42; }
.cmy-q { display: flex; justify-content: space-between; gap: 12px; align-items: center; flex-wrap: wrap; padding: 16px 0; border-top: 1px solid #EFEBE3; }
.cmy-q b { font: 700 16px/1.3 var(--head); color: #1E2B27; }
.cmy-q span { color: #6B7A74; font-size: 14px; }
.cmy-badge { font: 700 12.5px/1 var(--head); padding: 7px 10px; border-radius: 99px; background: #FBE6D8; color: #A14E22; }
.cmy-badge.ok { background: #E9F0EC; color: #1D4A42; }
.cmy-gap { height: 16px; }

/* Board summary: printed on its own */
#cw-board { display: none; }
@media print {
  body.printing-board > *:not(#cw-board) { display: none !important; }
  body.printing-board #cw-board, body.printing-board #cw-board * { visibility: visible !important; }
  body.printing-board #cw-board { display: block !important; color: #000; font: 11pt/1.45 Georgia, serif; }
  #cw-board h1 { font: 700 20pt/1.2 Georgia, serif; margin: 0 0 4pt; }
  #cw-board .b-sub { margin: 0 0 14pt; color: #333; }
  #cw-board .b-sum { display: flex; gap: 18pt; margin: 0 0 14pt; }
  #cw-board .b-sum div { border: 1pt solid #999; padding: 6pt 10pt; }
  #cw-board .b-sum b { font-size: 16pt; display: block; }
  #cw-board table { width: 100%; border-collapse: collapse; margin: 0 0 14pt; }
  #cw-board th, #cw-board td { text-align: left; border-bottom: .5pt solid #bbb; padding: 4pt 6pt 4pt 0; vertical-align: top; font-size: 10pt; }
  #cw-board td:nth-child(3) { white-space: nowrap; }
  #cw-board tr { break-inside: avoid; }
  #cw-board .b-sign { break-inside: avoid; display: flex; gap: 24pt; margin: 22pt 0 12pt; }
  #cw-board .b-sign div { flex: 1; border-top: 1pt solid #000; padding-top: 4pt; font-size: 9.5pt; }
  #cw-board .b-note { font-size: 8.5pt; color: #444; }
  @page { margin: 16mm; }
}
'''

_cfg = json.dumps({'on': ACCOUNTS_ON, 'url': SUPABASE_URL, 'key': SUPABASE_KEY})

JS = r'''
// ---------------------------------------------------------------- Always Safety: results, board summary, account
(() => {
  const CFG = __CFG__;
  const esc = (s) => String(s ?? '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  const LABEL = { met: 'Done', attention: 'Needs attention', check: 'To check', upcoming: 'Coming' };
  const AREA = { privacy: 'Privacy', child_safety: 'Child safety', charity: 'Charity', messages: 'Emails and texts' };
  const quarterOf = (d) => `${d.getFullYear()} Q${Math.floor(d.getMonth() / 3) + 1}`;
  const count = (items, s) => items.filter((i) => i.status === s).length;
  const lawLinks = (law) => (law || []).map((l) => `<a href="${esc(l.url)}" target="_blank" rel="noopener">${esc(l.name)}</a>`).join(', ');

  function card(it) {
    const when = it.status === 'upcoming' && it.commences ? ' ' + new Date(it.commences).toLocaleDateString('en-AU', { month: 'long', year: 'numeric' }) : '';
    return `<article class="cw-item"><div class="cw-head"><h4>${esc(it.title)}</h4><span class="cw-tag ${it.status}">${LABEL[it.status]}${when}</span></div>
      <p class="cw-str">${it.strength === 'required' ? 'Required for your ministry' : 'Good practice for your ministry'}</p>
      <p>${esc(it.summary)}</p>
      ${it.status !== 'met' && it.status !== 'upcoming' ? `<p><b>What to do:</b> ${esc(it.guidance)}</p>` : ''}
      <p class="cw-law">Source: ${lawLinks(it.law)}</p></article>`;
  }

  function nextSteps(items) {
    const todo = items.filter((i) => i.status === 'attention' || i.status === 'check');
    if (!todo.length) return '<div class="cw-clear">Nothing needs doing right now. Check again next quarter, or when a rule changes.</div>';
    return `<ol class="cw-steps">${todo.map((it) => `<li class="${it.status === 'attention' ? 'att' : ''}">
      <h5>${esc(it.title)}</h5>
      <p>${esc(it.guidance)}</p>
      ${it.missing.length ? `<ul>${it.missing.map((m) => `<li>Not yet: ${esc(m)}</li>`).join('')}</ul>` : ''}
      ${it.unanswered.length ? `<ul>${it.unanswered.map((m) => `<li>Check: ${esc(m)}</li>`).join('')}</ul>` : ''}
      <p class="cw-law">Read the rule: ${lawLinks(it.law)}</p></li>`).join('')}</ol>`;
  }

  /** The results view, shared by the free check-up and the signed-in area. */
  function report(a, opts = {}) {
    const items = a.items, todo = count(items, 'attention') + count(items, 'check');
    const saveCard = CFG.on
      ? `<div class="cw-save"><h5>Save it and check in each quarter</h5><p>We'll remind you each quarter and tell you when a rule that applies to you changes. Sign in with an email link, no password.</p><button class="btn btn-peach" type="button" data-save>Save my results</button></div>`
      : `<div class="cw-save"><h5>Get this every quarter</h5><p>Saving and quarterly reminders are opening soon. Tell us you're interested and we'll set you up first.</p><a class="btn btn-peach" href="#/contact/compliance">Tell me when it opens</a></div>`;
    return `<h3 class="pg-h" style="font-size:28px;margin:0 0 8px">Your check-up</h3>
      <p class="pg-lead" style="margin:0 0 20px">${items.length} obligations apply to your ministry. ${todo ? `${todo} ${todo === 1 ? 'needs' : 'need'} a look.` : 'You are on top of them.'}</p>
      <div class="cw-sum"><div class="att"><b>${count(items, 'attention')}</b><span>Need attention</span></div><div><b>${count(items, 'check')}</b><span>To check</span></div><div class="up"><b>${count(items, 'upcoming')}</b><span>Coming</span></div><div><b>${count(items, 'met')}</b><span>Done</span></div></div>
      <section class="cw-next" aria-labelledby="cw-next-h"><h4 id="cw-next-h">Your next steps</h4><p>Most important first. Each one links to the rule it comes from.</p>${nextSteps(items)}</section>
      <details class="cw-more"><summary>Everything that applies to you (${items.length})</summary><div class="cw-items">${items.map(card).join('')}</div>
        ${a.watching.length ? `<div class="cw-watch"><b>On the horizon.</b> ${a.watching.map((w) => esc(w.summary)).join(' ')}</div>` : ''}</details>
      ${opts.local ? `<div class="cw-then">
        <div><h5>A summary for your board</h5><div class="cw-name"><label for="cw-name">Ministry name</label><input id="cw-name" type="text" autocomplete="organization" maxlength="120" placeholder="Optional"></div><p>One page with where you stand and space to sign. It's made on your device.</p><button class="btn btn-ghost-dark" type="button" data-print>Download board summary</button></div>
        ${saveCard}
        <div><h5>Partner with Always</h5><p>Free for churches and ministries. One sign-in for every Always module, from safety to reports.</p><a class="btn btn-ghost-dark" href="#/join/church" data-join-interest="compliance">Partner with Always</a></div>
      </div>` : ''}
      <p class="cw-notice">Register ${esc(a.version)} (${esc(a.status)}). ${esc(a.notice)}${opts.local ? ' Nothing you entered has been sent or saved.' : ''}</p>
      ${opts.local ? '<div class="cw-nav"><button class="btn btn-ghost-dark" type="button" data-edit>Change my answers</button><span></span></div>' : ''}`;
  }

  /** One printable page, built on the device. Uses the browser's own Save as PDF. */
  function printBoard(a, name) {
    if (!a) return;
    let el = document.getElementById('cw-board');
    if (!el) { el = document.createElement('div'); el.id = 'cw-board'; document.body.appendChild(el); }
    const d = new Date(), items = a.items;
    el.innerHTML = `<h1>${esc(name || 'Our ministry')}: safety check-up</h1>
      <p class="b-sub">${esc(quarterOf(d))} · prepared ${d.toLocaleDateString('en-AU', { day: 'numeric', month: 'long', year: 'numeric' })} with Always Safety</p>
      <div class="b-sum"><div><b>${items.length}</b>apply</div><div><b>${count(items, 'met')}</b>done</div><div><b>${count(items, 'attention') + count(items, 'check')}</b>need a look</div><div><b>${count(items, 'upcoming')}</b>coming</div></div>
      <table><thead><tr><th>Area</th><th>Obligation</th><th>Status</th><th>Next step</th></tr></thead><tbody>
      ${items.map((i) => `<tr><td>${esc(AREA[i.area] || '')}</td><td>${esc(i.title)}</td><td>${esc(LABEL[i.status])}</td><td>${i.status === 'met' || i.status === 'upcoming' ? '' : esc(i.guidance)}</td></tr>`).join('')}
      </tbody></table>
      <div class="b-sign"><div>Reviewed by</div><div>Role</div><div>Date</div></div>
      <p class="b-note">Register ${esc(a.version)}. ${esc(a.notice)}</p>`;
    document.body.classList.add('printing-board');
    const done = () => { document.body.classList.remove('printing-board'); removeEventListener('afterprint', done); };
    addEventListener('afterprint', done);
    window.print();
    setTimeout(done, 1500);
  }

  // ---------------------------------------------------------------- Account (email link, Supabase Auth in Sydney)
  const KEY = 'always.session', PENDING = 'always.cw.pending', ORG = 'always.org';
  const store = {
    get: (k) => { try { return JSON.parse(sessionStorage.getItem(k) || 'null'); } catch { return null; } },
    set: (k, v) => { try { v == null ? sessionStorage.removeItem(k) : sessionStorage.setItem(k, JSON.stringify(v)); } catch {} },
  };
  const session = () => { const s = store.get(KEY); return s && s.expires_at * 1000 > Date.now() + 30_000 ? s : null; };

  async function auth(path, body) {
    const r = await fetch(`${CFG.url}/auth/v1/${path}`, { method: 'POST', headers: { apikey: CFG.key, 'content-type': 'application/json' }, body: JSON.stringify(body) });
    if (!r.ok) throw new Error(r.status === 429 ? 'Too many tries. Please wait a minute and try again.' : 'That didn’t work. Check the code and try again.');
    return r.status === 204 ? {} : r.json();
  }
  async function api(method, path, body) {
    const s = session(); if (!s) throw new Error('signed_out');
    const headers = { authorization: `Bearer ${s.access_token}`, 'content-type': 'application/json' };
    const org = store.get(ORG); if (org && !path.startsWith('/v1/account/')) headers['x-always-org'] = org.id;
    const r = await fetch(`/api${path}`, { method, headers, body: body ? JSON.stringify(body) : undefined });
    if (r.status === 401) { store.set(KEY, null); throw new Error('signed_out'); }
    if (!r.ok) { const e = new Error((await r.json().catch(() => ({}))).error || `http_${r.status}`); e.status = r.status; throw e; }
    return r.json();
  }

  function startSave(pending) {
    store.set(PENDING, pending);
    location.hash = '#/mycompliance';
  }

  // A magic link lands as #access_token=...&expires_at=...
  if (/^#access_token=/.test(location.hash)) {
    const q = new URLSearchParams(location.hash.slice(1));
    store.set(KEY, { access_token: q.get('access_token'), refresh_token: q.get('refresh_token'), expires_at: Number(q.get('expires_at')) || Math.floor(Date.now() / 1000) + 3600 });
    history.replaceState(null, '', '#/mycompliance');
  }

  const root = () => document.getElementById('cmy');
  const steps = (n) => `<ol class="cmy-steps" aria-label="Getting set up">${['Sign in', 'Your ministry', 'Your check-up'].map((t, i) => `<li class="${i + 1 === n ? 'on' : i + 1 < n ? 'done' : ''}"${i + 1 === n ? ' aria-current="step"' : ''}>${t}</li>`).join('')}</ol>`;

  function viewClosed() {
    root().innerHTML = `<div class="cmy-card"><h2>Opening soon</h2><p>Saving your check-up and quarterly reminders are nearly ready. You can use the free check-up now, and download a summary for your board.</p>
      <div class="cmy-row"><a class="btn btn-peach" href="#/compliance/check">Start the free check-up</a><a class="btn btn-ghost-dark" href="#/contact/compliance">Tell me when it opens</a></div></div>`;
  }

  function viewEmail(msg = '') {
    root().innerHTML = `<div class="cmy-card">${steps(1)}<h2>Sign in with your email</h2><p>We'll email you a link and a six-digit code. No password to remember.</p>
      <form id="cmy-email" novalidate><div class="cmy-field"><label for="cmy-e">Email address</label><input id="cmy-e" type="email" autocomplete="email" required></div>
      <p class="cmy-err" role="alert">${esc(msg)}</p><div class="cmy-row"><button class="btn btn-peach" type="submit">Email me a sign-in link</button></div>
      <p class="cmy-note">Your email is kept in Australia and used only for your account and safety reminders.</p></form></div>`;
    root().querySelector('#cmy-email').addEventListener('submit', async (e) => {
      e.preventDefault();
      const email = root().querySelector('#cmy-e').value.trim(), err = root().querySelector('.cmy-err');
      if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) { err.textContent = 'Please enter a valid email address.'; return; }
      e.submitter && (e.submitter.disabled = true);
      try { await auth('otp', { email, create_user: true }); viewCode(email); }
      catch (x) { err.textContent = x.message; e.submitter && (e.submitter.disabled = false); }
    });
    root().querySelector('#cmy-e').focus();
  }

  function viewCode(email) {
    root().innerHTML = `<div class="cmy-card">${steps(1)}<h2>Check your email</h2><p>We sent a link and a code to <b>${esc(email)}</b>. Open the link on this device, or type the code here.</p>
      <form id="cmy-code" novalidate><div class="cmy-field"><label for="cmy-c">Six-digit code</label><input id="cmy-c" class="cmy-code" type="text" inputmode="numeric" autocomplete="one-time-code" maxlength="6" pattern="[0-9]{6}" required></div>
      <p class="cmy-err" role="alert"></p><div class="cmy-row"><button class="btn btn-peach" type="submit">Sign in</button><button class="btn btn-ghost-dark" type="button" data-back>Use a different email</button></div></form></div>`;
    root().querySelector('[data-back]').addEventListener('click', () => viewEmail());
    root().querySelector('#cmy-code').addEventListener('submit', async (e) => {
      e.preventDefault();
      const token = root().querySelector('#cmy-c').value.replace(/\D/g, ''), err = root().querySelector('.cmy-err');
      if (token.length !== 6) { err.textContent = 'The code has six digits.'; return; }
      try {
        const s = await auth('verify', { type: 'email', email, token });
        store.set(KEY, { access_token: s.access_token, refresh_token: s.refresh_token, expires_at: s.expires_at || Math.floor(Date.now() / 1000) + (s.expires_in || 3600) });
        load();
      } catch (x) { err.textContent = x.message; }
    });
    root().querySelector('#cmy-c').focus();
  }

  function viewNewOrg(msg = '') {
    const pending = store.get(PENDING), st = pending?.profile?.states?.[0] || '';
    root().innerHTML = `<div class="cmy-card">${steps(2)}<h2>Tell us about your ministry</h2><p>This sets up your space on Always, with you as its admin.</p>
      <form id="cmy-org" novalidate>
        <div class="cmy-field"><label for="cmy-n">Church or ministry name</label><input id="cmy-n" type="text" autocomplete="organization" maxlength="120" required value="${esc(pending?.name || '')}"></div>
        <fieldset class="cmy-field" style="border:0;padding:0;margin:0"><legend>What kind of organisation is it?</legend><div class="cmy-opts"><label class="cw-opt"><input type="radio" name="kind" value="church" checked><span>A church</span></label><label class="cw-opt"><input type="radio" name="kind" value="ministry"><span>A ministry</span></label></div></fieldset>
        <div class="cmy-row"><div class="cmy-field"><label for="cmy-s">Main state or territory</label><select id="cmy-s" required>${['', 'NSW', 'VIC', 'QLD', 'WA', 'SA', 'TAS', 'ACT', 'NT'].map((s) => `<option value="${s}" ${s === st ? 'selected' : ''}>${s || 'Choose'}</option>`).join('')}</select></div>
        <div class="cmy-field"><label for="cmy-p">Postcode</label><input id="cmy-p" type="text" inputmode="numeric" maxlength="4" pattern="[0-9]{4}" style="max-width:140px"></div></div>
        <p class="cmy-err" role="alert">${esc(msg)}</p><div class="cmy-row"><button class="btn btn-peach" type="submit">Continue</button></div>
        <p class="cmy-note">This doesn't make you a partner church in Always Connect. That's a separate step, whenever you're ready.</p></form></div>`;
    root().querySelector('#cmy-org').addEventListener('submit', async (e) => {
      e.preventDefault();
      const f = e.target, err = root().querySelector('.cmy-err');
      const body = { displayName: f.querySelector('#cmy-n').value.trim(), kind: f.querySelector('input[name=kind]:checked').value, state: f.querySelector('#cmy-s').value };
      const pc = f.querySelector('#cmy-p').value.trim(); if (pc) body.postcode = pc;
      if (body.displayName.length < 2) { err.textContent = 'Please enter your church or ministry name.'; return; }
      if (!body.state) { err.textContent = 'Please choose a state or territory.'; return; }
      if (pc && !/^\d{4}$/.test(pc)) { err.textContent = 'A postcode has four digits.'; return; }
      try { const o = await api('POST', '/v1/account/orgs', body); store.set(ORG, o); load(); }
      catch (x) { err.textContent = x.message === 'email_linked_to_another_account' ? 'That email is already linked to another account. Please contact us.' : 'Something went wrong. Please try again.'; }
    });
  }

  async function savePending() {
    const p = store.get(PENDING); if (!p) return;
    await api('PUT', '/v1/compliance/profile', p.profile);
    const answers = Object.entries(p.answers || {}).filter(([, v]) => ['yes', 'no', 'unsure', 'not_applicable'].includes(v)).map(([evidenceId, answer]) => ({ evidenceId, answer }));
    if (answers.length) await api('PUT', '/v1/compliance/answers', { answers });
    store.set(PENDING, null);
  }

  async function viewDashboard(orgs) {
    const org = store.get(ORG);
    document.getElementById('cmy-title').textContent = org.name;
    document.getElementById('cmy-lead').textContent = 'Your safety check-up, kept up to date each quarter.';
    let a = null, history = [];
    try { a = await api('GET', '/v1/compliance/assessment'); } catch (x) { if (x.status !== 409) throw x; }
    if (!a) {
      root().innerHTML = `<div class="cmy-card">${steps(3)}<h2>Take your first check-up</h2><p>About ten minutes. When you finish, choose Save my results.</p><div class="cmy-row"><a class="btn btn-peach" href="#/compliance/check">Start the check-up</a></div></div>`;
      return;
    }
    try { history = (await api('GET', '/v1/compliance/assessments')).assessments; } catch {}
    const result = { items: a.items, watching: a.watching, version: a.registerVersion, status: a.registerStatus, notice: a.notice };
    const rows = history.map((h) => `<div class="cmy-q"><div><b>${esc(h.quarter)}</b><br><span>Register ${esc(h.register_version)}</span></div>
      ${h.approved_at ? `<span class="cmy-badge ok">Approved ${new Date(h.approved_at).toLocaleDateString('en-AU')}</span>` : `<button class="btn btn-peach" type="button" data-approve="${esc(h.id)}">Review and approve</button>`}</div>`).join('');
    root().innerHTML = `<div class="cmy-card"><h2>Where you stand today</h2>
      <div class="cmy-row"><button class="btn btn-ghost-dark" type="button" data-update>Update my answers</button><button class="btn btn-ghost-dark" type="button" data-board>Download board summary</button>${orgs.length > 1 ? '<button class="btn btn-ghost-dark" type="button" data-switch>Switch ministry</button>' : ''}<button class="btn btn-ghost-dark" type="button" data-out>Sign out</button></div></div>
      <div class="cmy-gap"></div><div class="cw">${report(result)}</div>
      <div class="cmy-gap"></div><div class="cmy-card"><h2>Each quarter</h2><p>At the start of every quarter we draft your check-up and email you. Someone at your ministry reviews and approves it for your board.</p>${rows || '<p class="cmy-note">Your first quarterly check-up will appear here at the start of next quarter.</p>'}</div>`;
    const c = root();
    c.querySelector('[data-update]').addEventListener('click', async () => {
      const st = await api('GET', '/v1/compliance/profile');
      sessionStorage.setItem('always.cw.prefill', JSON.stringify({ profile: st.profile, answers: st.answers }));
      store.set(PENDING, null); location.hash = '#/compliance/check'; location.reload();
    });
    c.querySelector('[data-board]').addEventListener('click', () => printBoard(result, org.name));
    c.querySelector('[data-out]').addEventListener('click', () => { store.set(KEY, null); store.set(ORG, null); load(); });
    c.querySelector('[data-switch]')?.addEventListener('click', () => { store.set(ORG, null); viewPick(orgs); });
    c.querySelectorAll('[data-approve]').forEach((b) => b.addEventListener('click', async () => {
      b.disabled = true;
      try { await api('POST', `/v1/compliance/assessments/${b.dataset.approve}/approve`); load(); } catch { b.disabled = false; }
    }));
  }

  function viewPick(orgs) {
    root().innerHTML = `<div class="cmy-card"><h2>Choose a ministry</h2>${orgs.map((o) => `<div class="cmy-q"><b>${esc(o.name)}</b><button class="btn btn-ghost-dark" type="button" data-org="${esc(o.id)}">Open</button></div>`).join('')}
      <div class="cmy-row"><button class="btn btn-ghost-dark" type="button" data-new>Add another ministry</button></div></div>`;
    root().querySelectorAll('[data-org]').forEach((b) => b.addEventListener('click', () => { store.set(ORG, orgs.find((o) => o.id === b.dataset.org)); load(); }));
    root().querySelector('[data-new]').addEventListener('click', () => viewNewOrg());
  }

  async function load() {
    if (!root()) return;
    if (!CFG.on) return viewClosed();
    if (!session()) return viewEmail();
    root().innerHTML = '<div class="cmy-card"><p>Loading…</p></div>';
    try {
      const { orgs } = await api('GET', '/v1/account/orgs');
      if (!orgs.length) return viewNewOrg();
      const current = store.get(ORG);
      if (!current || !orgs.some((o) => o.id === current.id)) {
        if (orgs.length === 1) store.set(ORG, orgs[0]); else return viewPick(orgs);
      }
      await savePending();
      await viewDashboard(orgs);
    } catch (x) {
      if (x.message === 'signed_out') return viewEmail('Your session ended. Please sign in again.');
      root().innerHTML = '<div class="cmy-card"><h2>We couldn’t load your safety check-up</h2><p>Please try again in a moment.</p><div class="cmy-row"><button class="btn btn-peach" type="button" onclick="location.reload()">Try again</button></div></div>';
    }
  }

  window.AlwaysCompliance = { report, printBoard, startSave };
  addEventListener('hashchange', () => { if (location.hash.startsWith('#/mycompliance')) load(); });
  if (location.hash.startsWith('#/mycompliance')) load();
})();
'''.replace('__CFG__', _cfg)
