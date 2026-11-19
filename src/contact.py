"""The join form: as few fields as possible, a QR code for meeting in person, and a full-screen code to show."""
import json
import qr

# Preset: (role, topic shown above the form)
PRESETS = {'church': ['Church or ministry', ''], 'compliance': ['Church or ministry', 'Always Compliance'], 'reports': ['Church or ministry', 'Always Reports'],
           'pilot': ['Evangelist', 'The Always App pilot'], 'evangelist': ['Evangelist', ''], 'supporter': ['Supporter', ''],
           'developer': ['Developer or tech platform', ''], 'platform': ['Developer or tech platform', 'Always Compliance for platforms'], 'other': ['Something else', '']}

CHIPS = [
    ('Church or ministry', 'Church or ministry'),
    ('Evangelist', 'Evangelist'),
    ('Supporter', 'Supporter'),
    ('Developer or tech platform', 'Developer or tech platform'),
    ('Something else', 'Something else'),
]

FORM = f'''<form id="contact-form" class="rv cf" novalidate>
      <p class="cf-topic" id="cf-topic" hidden>About <b></b> <button type="button" aria-label="Remove topic">&times;</button></p>
      <input type="hidden" name="topic" value="">
      <fieldset class="cf-chips"><legend>I'm getting in touch as</legend>
        {''.join(f'<label><input type="radio" name="interest" value="{v}"{" checked" if i == 0 else ""}><span>{l}</span></label>' for i, (v, l) in enumerate(CHIPS))}
      </fieldset>
      <div class="row2">
        <label>First name<input name="name" autocomplete="given-name" autocapitalize="words" enterkeyhint="next" required></label>
        <label>Email or mobile<input name="contact" autocomplete="email" inputmode="email" autocapitalize="off" spellcheck="false" enterkeyhint="send" required></label>
      </div>
      <label class="cf-org"><span>Church or organisation <span class="cf-opt">optional</span></span><input name="organisation" autocomplete="organization"></label>
      <details class="cf-note"><summary>Add a note <span class="cf-opt">optional</span></summary><textarea name="message" rows="3" aria-label="Note"></textarea></details>
      <input class="cf-hp" name="company_site" tabindex="-1" autocomplete="off" aria-hidden="true">
      <button class="btn btn-peach" type="submit">Stay in touch</button>
      <p class="cf-fine">We'll only use this to get in touch. <a href="#/docs/privacy">Privacy</a></p>
      <p class="status" id="form-status" role="status" aria-live="polite"></p>
    </form>'''

QR_CARD = f'''<div class="cf-qr rv">
        <div class="cf-qr-code" aria-hidden="true">{qr.SVG}</div>
        <div><b>Meeting in person?</b><span>They scan this with their phone camera and fill it in themselves.</span>
        <div class="cf-qr-actions"><a href="#/hello">Show full screen</a><button type="button" id="cf-share">Share link</button></div></div>
      </div>'''

CONTACT = f'''<section class="sec join contact-sec"><div class="wrap">
    <div>
      <p class="pl-kick">Contact</p>
      <h1>Get in touch</h1>
      <p class="lead">Whether you're a church, a ministry, a supporter or a developer, we'd love to hear from you. Leave your details and we'll get back to you.</p>
      {QR_CARD}
      <a class="mail" href="mailto:hello@alwaysfoundation.org">hello@alwaysfoundation.org</a>
      <ul class="ct-more">
        <li><a href="#/join">Join Always</a></li>
        <li><a href="#/feedback">Report a problem or share an idea</a></li>
        <li><a href="#/faq">Read the FAQs</a></li>
      </ul>
    </div>
    {FORM}
</div></section>'''

HELLO = f'''<section class="hello"><div class="hello-card">
  <p class="hello-k">Always Foundation</p>
  <h1>Let's stay in touch</h1>
  <div class="hello-code" role="img" aria-label="QR code that opens the Always Foundation join form">{qr.SVG}</div>
  <p class="hello-how">Open your phone camera and point it here.</p>
  <p class="hello-url">alwaysfoundation.org</p>
  <a class="hello-back" href="#/contact">Or fill it in on this phone</a>
</div></section>'''

HELP_OPTIONS = [
    ("I'm from a church", '#/churches'),
    ('I run a ministry, event or tour', '#/ministries'),
    ('I need help with compliance', '#/compliance/check'),
    ("I'm a developer", '#/developers'),
    ("I'd like to talk to someone", '#/contact'),
]

HELPER = f'''<div class="hp" id="hp">
  <div class="hp-panel" id="hp-panel" role="dialog" aria-label="Quick help" hidden>
    <div class="hp-head"><b>Hi there</b><button type="button" class="hp-x" aria-label="Close quick help">&times;</button></div>
    <p class="hp-msg">What brings you here today? Pick one and we'll take you to the right place.</p>
    <ul class="hp-opts">{''.join(f'<li><a href="{h}">{t}</a></li>' for t, h in HELP_OPTIONS)}</ul>
    <p class="hp-foot">Or email <a href="mailto:hello@alwaysfoundation.org">hello@alwaysfoundation.org</a></p>
  </div>
  <button type="button" class="hp-btn" aria-expanded="false" aria-controls="hp-panel"><span class="hp-dot" aria-hidden="true"></span>Need a hand?</button>
</div>'''

CSS = '''
/* ---- Join form ---- */
.cf { display: grid; gap: 16px; align-content: start; }
.cf-chips { border: 0; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 8px; }
.cf-chips legend { width: 100%; padding: 0; margin-bottom: 10px; font-weight: 600; font-size: 15px; }
.cf-chips label { position: relative; display: inline-flex; cursor: pointer; }
.cf-chips input { position: absolute; opacity: 0; inset: 0; margin: 0; cursor: pointer; }
.cf-chips span { display: inline-flex; align-items: center; min-height: 44px; padding: 0 16px; border-radius: 12px; border: 1px solid rgba(248,243,234,.28); font: 600 15px/1 var(--head); transition: background .15s, color .15s, border-color .15s; }
.cf-chips input:checked + span { background: var(--cream); color: var(--green); border-color: var(--cream); }
.cf-chips input:focus-visible + span { outline: 2px solid var(--peach); outline-offset: 2px; }
.cf-topic { margin: 0; display: inline-flex; align-items: center; gap: 8px; justify-self: start; padding: 8px 8px 8px 14px; border-radius: 12px; background: rgba(248,243,234,.1); font-size: 14.5px; }
.cf-topic[hidden] { display: none; } .cf-topic b { color: var(--cream); }
.cf-topic button { width: 28px; height: 28px; border: 0; border-radius: 50%; background: rgba(248,243,234,.14); color: var(--cream); font-size: 18px; line-height: 1; cursor: pointer; }
.cf-opt { font-weight: 400; opacity: .7; font-size: 13px; margin-left: 4px; }
.cf-org[hidden] { display: none; }
.cf-note summary { cursor: pointer; font-weight: 600; font-size: 15px; min-height: 32px; display: flex; align-items: center; gap: 4px; }
.cf-note textarea { margin-top: 8px; width: 100%; }
.cf-hp { position: absolute; left: -9999px; width: 1px; height: 1px; opacity: 0; }
.cf-fine { margin: 0; font-size: 13.5px; opacity: .8; } .cf-fine a { color: inherit; }
.cf-done { display: grid; gap: 10px; align-content: center; min-height: 280px; text-align: center; }
.cf-done h3 { margin: 0; font: 400 34px/1.15 'Newsreader', Georgia, serif; color: var(--cream); }
.cf-done p { margin: 0; opacity: .85; }
.cf-qr { display: grid; grid-template-columns: 112px minmax(0, 1fr); gap: 18px; align-items: center; margin-top: 28px; padding: 14px; border-radius: 20px; background: rgba(248,243,234,.08); }
.cf-qr-code { background: #FFFDF8; border-radius: 12px; padding: 10px; line-height: 0; }
.qr-svg { width: 100%; height: auto; display: block; shape-rendering: crispEdges; }
.cf-qr b { display: block; font: 700 16px/1.3 var(--head); color: var(--cream); }
.cf-qr span { display: block; margin-top: 4px; font-size: 14.5px; line-height: 1.45; opacity: .85; }
.cf-qr-actions { display: flex; gap: 14px; margin-top: 10px; flex-wrap: wrap; }
.cf-qr-actions a, .cf-qr-actions button { background: none; border: 0; padding: 0; min-height: 32px; font: 700 14px/1 var(--head); color: var(--peach); cursor: pointer; text-decoration: underline; text-underline-offset: 4px; }

/* ---- Home invitation ---- */
.join-paths { display: grid; gap: 0; align-content: start; }
.join-paths a { display: grid; gap: 4px; padding: 22px 0; border-top: 1px solid rgba(248,243,234,.16); color: var(--cream); text-decoration: none; }
.join-paths a:last-of-type { border-bottom: 1px solid rgba(248,243,234,.16); }
.join-paths b { font: 800 24px/1.15 var(--head); letter-spacing: -0.02em; }
.join-paths span { color: var(--on-green); font-size: 16px; }
.join-paths a:hover b, .join-paths a:focus-visible b { text-decoration: underline; text-decoration-color: var(--peach); text-underline-offset: 6px; }
.join-paths .sv { margin-top: 24px; }

/* ---- Contact page ---- */
.contact-sec { padding-top: 160px; }
.contact-sec h1 { margin: 10px 0 0; font: 800 clamp(44px, 6vw, 76px)/1.02 var(--head); letter-spacing: -0.04em; color: var(--cream); }
.contact-sec .pl-kick { color: var(--peach); }
.ct-more { list-style: none; padding: 0; margin: 28px 0 0; display: grid; gap: 10px; }
.ct-more a { color: var(--on-green); font-weight: 600; text-decoration: underline; text-decoration-color: rgba(248,243,234,.3); text-underline-offset: 5px; }
.ct-more a:hover { text-decoration-color: var(--peach); }
@media (max-width: 860px) { .contact-sec { padding-top: 120px; } }

/* ---- Quick help ---- */
.hp { position: fixed; right: 20px; bottom: 20px; z-index: 60; display: grid; justify-items: end; gap: 12px; font-family: var(--text); }
.hp-btn { display: inline-flex; align-items: center; gap: 10px; min-height: 48px; padding: 0 20px 0 16px; border: 0; border-radius: 999px; background: var(--cream); color: var(--green); font: 700 15px/1 var(--head); cursor: pointer; box-shadow: 0 14px 30px -12px rgba(20,53,47,.45), 0 0 0 1px rgba(27,71,64,.08); }
.hp-btn:focus-visible { outline: 3px solid var(--peach); outline-offset: 3px; }
.hp-dot { width: 10px; height: 10px; border-radius: 50%; background: var(--peach); box-shadow: 0 0 0 4px rgba(232,165,119,.25); }
.hp-btn[aria-expanded="true"] .hp-dot { background: var(--green); box-shadow: none; }
.hp-panel { width: min(340px, calc(100vw - 40px)); background: #FFFDF8; color: var(--ink); border-radius: 22px; padding: 18px 18px 14px; box-shadow: 0 30px 60px -24px rgba(20,53,47,.5), 0 0 0 1px rgba(27,71,64,.06); }
.hp-panel:not([hidden]) { animation: hpIn .22s cubic-bezier(.2,.8,.2,1); }
@keyframes hpIn { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: none; } }
.hp-head { display: flex; justify-content: space-between; align-items: center; }
.hp-head b { font: 800 18px/1 var(--head); color: var(--green); }
.hp-x { width: 36px; height: 36px; border: 0; border-radius: 50%; background: var(--sage-2); color: var(--green); font-size: 22px; line-height: 1; cursor: pointer; }
.hp-msg { margin: 10px 0 12px; padding: 12px 14px; border-radius: 16px 16px 16px 4px; background: var(--sage-2); font-size: 15px; line-height: 1.45; color: var(--soft); }
.hp-opts { list-style: none; margin: 0; padding: 0; display: grid; gap: 6px; }
.hp-opts a { display: flex; align-items: center; min-height: 44px; padding: 0 14px; border-radius: 12px; border: 1px solid rgba(27,71,64,.16); color: var(--green); font: 600 15px/1.2 var(--head); text-decoration: none; }
.hp-opts a:hover, .hp-opts a:focus-visible { background: var(--green); color: var(--cream); border-color: var(--green); }
.hp-foot { margin: 12px 2px 0; font-size: 13.5px; color: var(--muted); } .hp-foot a { color: var(--clay); }
body.on-hello .hp, body.menu-open .hp { display: none; }
@media (max-width: 640px) { .hp { right: 14px; bottom: 14px; } .hp-btn { min-height: 46px; padding: 0 16px 0 14px; } }
@media (prefers-reduced-motion: reduce) { .hp-panel:not([hidden]) { animation: none; } }

/* ---- Full-screen code ---- */
#page-hello ~ footer, body.on-hello footer { display: none; }
.hello { min-height: 100svh; display: grid; place-items: center; padding: 110px 20px 40px; background: var(--green); }
.hello-card { width: min(420px, 100%); text-align: center; color: var(--cream); }
.hello-k { margin: 0; font: 700 15px/1 var(--head); color: var(--peach); }
.hello h1 { margin: 12px 0 28px; font: 800 clamp(34px, 8vw, 48px)/1.05 var(--head); letter-spacing: -0.03em; }
.hello-code { background: #FFFDF8; border-radius: 28px; padding: 26px; line-height: 0; box-shadow: 0 30px 60px -30px rgba(0,0,0,.5); }
.hello-how { margin: 22px 0 4px; font-size: 18px; }
.hello-url { margin: 0; font: 400 22px/1.3 'Newsreader', Georgia, serif; opacity: .9; }
.hello-back { display: inline-block; margin-top: 22px; color: var(--peach); font: 700 15px/1 var(--head); }
@media (max-width: 640px) { .cf-qr { grid-template-columns: 88px minmax(0, 1fr); } }
'''

JS = r'''
// Quick help: guided choices, no AI. Escape or a choice closes it.
(() => {
  const btn = document.querySelector('.hp-btn'), panel = document.getElementById('hp-panel');
  if (!btn) return;
  const set = (open, focus) => { btn.setAttribute('aria-expanded', String(open)); panel.hidden = !open; if (open) panel.querySelector('.hp-opts a').focus(); else if (focus) btn.focus(); };
  btn.addEventListener('click', () => set(panel.hidden));
  panel.querySelector('.hp-x').addEventListener('click', () => set(false, true));
  panel.querySelectorAll('.hp-opts a').forEach((a) => a.addEventListener('click', () => set(false)));
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !panel.hidden) set(false, true); });
  document.addEventListener('click', (e) => { if (!panel.hidden && !e.target.closest('.hp')) set(false); });
})();

// Join form: one box for email or mobile, chips for who they are, the note optional
(() => {
  const form = document.getElementById('contact-form');
  if (!form) return;
  const status = document.getElementById('form-status');
  const LIVE = /(^|\.)alwaysfoundation\.org$/.test(location.hostname);
  const org = form.querySelector('.cf-org');
  const ORG = ['Church or ministry', 'Developer or tech platform'];
  const sync = () => { const v = form.querySelector('input[name=interest]:checked')?.value; org.hidden = !ORG.includes(v); };
  form.querySelectorAll('input[name=interest]').forEach((r) => r.addEventListener('change', sync)); sync();
  window.alwaysSetInterest = (v) => { const r = [...form.querySelectorAll('input[name=interest]')].find((x) => x.value === v); if (r) { r.checked = true; sync(); } };
  const EMAIL = /^[^\s@<>]+@[^\s@<>]+\.[^\s@<>]+$/;
  const MOBILE = /^(\+?61|0)4\d{8}$/;
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const d = Object.fromEntries(new FormData(form));
    const contact = String(d.contact || '').trim(), digits = contact.replace(/[\s()-]/g, '');
    const isEmail = EMAIL.test(contact), isMobile = MOBILE.test(digits);
    if (!String(d.name || '').trim() || !(isEmail || isMobile)) { status.textContent = 'Please add your first name and an email address or Australian mobile number.'; return; }
    const body = { interest: d.interest, topic: d.topic, name: d.name, ...(isEmail ? { email: contact } : { mobile: digits }), organisation: org.hidden ? '' : d.organisation, message: d.message, company_site: d.company_site };
    if (!LIVE) { status.textContent = 'The form is not connected on this preview. Please email hello@alwaysfoundation.org.'; return; }
    const b = form.querySelector('button[type=submit]'); b.disabled = true; b.textContent = 'Sending…';
    try {
      const r = await fetch('/api/forms/join', { method: 'POST', headers: { 'content-type': 'application/json', accept: 'application/json' }, body: JSON.stringify(body) });
      if (!r.ok) throw 0;
      const first = String(d.name).trim().split(/\s+/)[0].replace(/[<>&"]/g, '');
      form.innerHTML = `<div class="cf-done" tabindex="-1"><h3>Thank you, ${first}.</h3><p>We've got your details and will be in touch soon.</p></div>`;
      form.querySelector('.cf-done').focus();
    } catch {
      status.textContent = 'That didn\'t send. Please try again, or email hello@alwaysfoundation.org.';
      b.disabled = false; b.textContent = 'Stay in touch';
    }
  });
  const PRESETS = __PRESETS__;
  const topicEl = document.getElementById('cf-topic');
  const setTopic = (t) => { form.elements.topic.value = t; topicEl.hidden = !t; topicEl.querySelector('b').textContent = t; };
  topicEl.querySelector('button').addEventListener('click', () => setTopic(''));
  const preset = () => { const m = location.hash.match(/^#\/contact\/([a-z]+)/); if (m && PRESETS[m[1]]) { window.alwaysSetInterest(PRESETS[m[1]][0]); setTopic(PRESETS[m[1]][1]); } };
  window.addEventListener('hashchange', preset); preset();
  const share = document.getElementById('cf-share');
  share?.addEventListener('click', async () => {
    const url = 'https://alwaysfoundation.org/#/contact';
    try { if (navigator.share) await navigator.share({ title: 'Always Foundation', text: "Let's stay in touch", url }); else { await navigator.clipboard.writeText(url); share.textContent = 'Link copied'; } } catch {}
  });
})();
'''

JS = JS.replace('__PRESETS__', json.dumps(PRESETS))
