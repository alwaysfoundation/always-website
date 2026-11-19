"""Join Always: a short registration with four paths. The foundation team verifies each one."""
from products import ICON

STATES = ['NSW', 'VIC', 'QLD', 'WA', 'SA', 'TAS', 'ACT', 'NT']
MODULES = [('app', 'Always App'), ('pages', 'Always Respond'), ('compliance', 'Always Compliance'), ('reports', 'Always Reports'), ('connect', 'Always Connect')]
PATHS = [
    ('church', 'A church or ministry', 'Become a member and switch on the modules you need.', 'churches'),
    ('evangelist', 'An evangelist', 'Join the Always App pilot and share Jesus with confidence.', 'evangelists'),
    ('supporter', 'A supporter', 'Pray, give or volunteer with us.', 'youth'),
    ('platform', 'A tech platform', 'Build on Always Platform, starting with Always Compliance.', 'platforms'),
]


def _icon(k):
    return f'<span class="jn-ic" aria-hidden="true"><svg viewBox="0 0 24 24">{ICON[k]}</svg></span>'


def _checks(name, items):
    return '<div class="jn-checks">' + ''.join(f'<label><input type="checkbox" name="{name}" value="{v}"><span>{t}</span></label>' for v, t in items) + '</div>'


def _state_select(name, optional=True):
    opts = ''.join(f'<option>{s}</option>' for s in STATES)
    return f'<select name="{name}"><option value="">{"Choose" if not optional else "Choose (optional)"}</option>{opts}</select>'


PAGE = f'''<section class="page-hero jn-hero"><div class="wrap">
  <p class="pl-kick">Join Always</p>
  <h1>Be part of Always.</h1>
  <p>Register in a few minutes. We'll verify your details and switch on what you need. Free for churches.</p>
</div></section>
<section class="sec jn-sec"><div class="wrap jn-wrap">
  <form id="join-form" class="jn" novalidate>
    <fieldset class="jn-step">
      <legend><span class="jn-n">01</span>I'm joining as</legend>
      <div class="jn-paths">
        {''.join(f'<label class="jn-path"><input type="radio" name="path" value="{k}"{" checked" if i == 0 else ""}>{_icon(ic)}<b>{t}</b><span>{d}</span></label>' for i, (k, t, d, ic) in enumerate(PATHS))}
      </div>
    </fieldset>

    <fieldset class="jn-step">
      <legend><span class="jn-n">02</span>About you</legend>
      <div class="jn-grid">
        <label>Your name<input name="name" autocomplete="name" required></label>
        <label>Email<input name="email" type="email" autocomplete="email" required></label>
        <label>Mobile <em>optional</em><input name="mobile" type="tel" inputmode="tel" autocomplete="tel"></label>
        <label data-for="church platform">Your role<input name="role" autocomplete="organization-title" placeholder="For example pastor, administrator, CTO" data-required="church platform"></label>
      </div>
    </fieldset>

    <fieldset class="jn-step" data-for="church">
      <legend><span class="jn-n">03</span>Your church or ministry</legend>
      <div class="jn-grid">
        <label>Name<input name="organisation" autocomplete="organization" data-required="church"></label>
        <label>Type<select name="orgType" data-required="church"><option value="">Choose</option><option>Church</option><option>Ministry or charity</option><option>Denomination or network</option><option>Event or tour</option><option>Youth ministry</option></select></label>
        <label>Website <em>optional</em><input name="website" type="url" inputmode="url" placeholder="https://"></label>
        <label>Denomination or network <em>optional</em><input name="denomination"></label>
      </div>
      <p class="jn-q">Where do you serve?</p>
      {_checks('states', [(s, s) for s in STATES])}
      <p class="jn-q">Which modules would help? <em>optional</em></p>
      {_checks('modules', MODULES)}
    </fieldset>

    <fieldset class="jn-step" data-for="evangelist">
      <legend><span class="jn-n">03</span>Your ministry</legend>
      <div class="jn-grid">
        <label>State<span class="jn-sel">{_state_select('evState', optional=False).replace('<select ', '<select data-required="evangelist" ')}</span></label>
        <label>Your church <em>optional</em><input name="church"></label>
        <label>Street team or ministry <em>optional</em><input name="team"></label>
      </div>
    </fieldset>

    <fieldset class="jn-step" data-for="supporter">
      <legend><span class="jn-n">03</span>How you'd like to help</legend>
      {_checks('support', [('pray', 'Pray'), ('give', 'Give'), ('volunteer', 'Volunteer')])}
      <div class="jn-grid"><label>State <em>optional</em><span class="jn-sel">{_state_select('supState')}</span></label></div>
    </fieldset>

    <fieldset class="jn-step" data-for="platform">
      <legend><span class="jn-n">03</span>Your platform</legend>
      <div class="jn-grid">
        <label>Platform name<input name="platform" data-required="platform"></label>
        <label>Website<input name="platformSite" type="url" inputmode="url" placeholder="https://" data-required="platform"></label>
      </div>
      <p class="jn-q">What would you like to build with? <em>optional</em></p>
      {_checks('build', [('compliance', 'Always Compliance infrastructure'), ('feed', 'The church feed'), ('handoff', 'Handoff to local churches'), ('mcp', 'The MCP connector')])}
    </fieldset>

    <fieldset class="jn-step jn-agree">
      <legend><span class="jn-n jn-n-last">04</span>Agree and send</legend>
      <label class="jn-check" data-for="church"><input type="checkbox" name="creed" value="yes" data-required="church"><span>We affirm the <a href="#/docs/governance" target="_blank" rel="noopener">Nicene Creed</a>.</span></label>
      <label class="jn-check"><input type="checkbox" name="terms" value="yes" required><span>I agree to the <a href="#/docs/terms" target="_blank" rel="noopener">terms of use</a> and <a href="#/docs/privacy" target="_blank" rel="noopener">privacy policy</a>.</span></label>
      <input class="cf-hp" name="company_site" tabindex="-1" autocomplete="off" aria-hidden="true">
      <button class="btn btn-peach" type="submit">Register</button>
      <p class="jn-status" id="jn-status" role="status" aria-live="polite"></p>
    </fieldset>
  </form>
  <aside class="jn-aside">
    <h2>What happens next</h2>
    <ol>
      <li><span>01</span><b>We check your details</b><p>For churches and ministries, usually with your denomination or network.</p></li>
      <li><span>02</span><b>We switch on what you need</b><p>The modules you chose, with one sign-in for your team.</p></li>
      <li><span>03</span><b>You're part of Always</b><p>Free for churches. Larger ministries contribute according to their size.</p></li>
    </ol>
    <p class="jn-aside-q">Questions first? <a href="#/contact">Get in touch</a></p>
  </aside>
</div></section>'''

CSS = '''
/* ---- Join Always ---- */
.jn-hero { padding-bottom: 72px; }
.jn-sec { background: var(--cream); padding-top: 64px; }
.jn-wrap { display: grid; grid-template-columns: minmax(0, 1fr) 300px; gap: 40px; align-items: start; }
#join-form.jn { max-width: none; display: grid; gap: 18px; padding: 0; margin: 0; background: transparent; border-radius: 0; color: var(--ink); box-shadow: none; }
.jn-aside { position: sticky; top: 110px; padding: 28px 26px; border-radius: 26px; background: var(--green); color: var(--on-green); }
.jn-aside h2 { margin: 0 0 18px; font: 800 22px/1.2 var(--head); color: var(--cream); }
.jn-aside ol { list-style: none; margin: 0; padding: 0; display: grid; gap: 18px; }
.jn-aside li { display: grid; gap: 4px; padding-top: 14px; border-top: 1px solid rgba(248,243,234,.16); }
.jn-aside li span { font: 400 22px/1 'Newsreader', Georgia, serif; color: var(--peach); }
.jn-aside li b { color: var(--cream); font: 700 16px/1.3 var(--head); } .jn-aside li p { margin: 0; font-size: 14.5px; line-height: 1.5; }
.jn-aside-q { margin: 22px 0 0; font-size: 14.5px; } .jn-aside-q a { color: var(--peach); font-weight: 600; }
@media (max-width: 1000px) { .jn-wrap { grid-template-columns: minmax(0, 1fr); } .jn-aside { position: static; } }
.jn-step { margin: 0; padding: 30px 30px 32px; border: 0; border-radius: 26px; background: #FFFDF8; box-shadow: 0 1px 0 rgba(30,42,38,.05); min-width: 0; }
.jn-step[hidden] { display: none; }
.jn-step legend { float: left; width: 100%; display: flex; align-items: baseline; gap: 14px; margin-bottom: 20px; padding: 0; font: 800 24px/1.2 var(--head); letter-spacing: -0.02em; color: var(--green); }
.jn-step legend + * { clear: both; }
.jn-n { font: 400 26px/1 'Newsreader', Georgia, serif; color: var(--clay); }
.jn-paths { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; }
.jn-path { position: relative; display: grid; grid-template-columns: 44px minmax(0, 1fr); column-gap: 14px; row-gap: 2px; align-items: start; padding: 18px; border-radius: 18px; border: 1.5px solid var(--line); cursor: pointer; transition: border-color .2s, background-color .2s, transform .2s cubic-bezier(.2,.8,.2,1); }
.jn-path input { position: absolute; opacity: 0; inset: 0; margin: 0; cursor: pointer; }
.jn-path .jn-ic { grid-row: span 2; }
.jn-path b { font: 800 17px/1.25 var(--head); color: var(--green); } .jn-path span:not(.jn-ic) { font-size: 14.5px; line-height: 1.45; color: var(--soft); }
.jn-path:hover { transform: translateY(-2px); }
.jn-path:has(input:checked) { border-color: var(--green); background: var(--sage-2); }
.jn-path:has(input:focus-visible) { outline: 3px solid var(--peach); outline-offset: 2px; }
.jn-ic { display: grid; place-items: center; width: 44px; height: 44px; border-radius: 13px; background: var(--peach-soft); color: var(--clay); }
.jn-path:has(input:checked) .jn-ic { background: var(--green); color: var(--cream); }
.jn-ic svg { width: 22px; height: 22px; fill: none; stroke: currentColor; stroke-width: 1.7; stroke-linecap: round; stroke-linejoin: round; }
.jn-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 14px 16px; }
.jn-grid label { display: flex; flex-wrap: wrap; align-items: baseline; gap: 6px; font-weight: 600; font-size: 14.5px; color: var(--ink); }
.jn-grid label > input, .jn-grid label > select, .jn-grid label > .jn-sel { flex-basis: 100%; }
.jn-grid label[hidden] { display: none; }
.jn em { font-style: normal; font-weight: 400; color: var(--muted); font-size: 13px; }
.jn input:not([type=checkbox]):not([type=radio]), .jn select { width: 100%; min-height: 48px; padding: 0 14px; border-radius: 12px; border: 1.5px solid var(--line); background: #fff; font: 400 16px var(--text); color: var(--ink); }
.jn input:focus-visible, .jn select:focus-visible { outline: 3px solid var(--peach); outline-offset: 1px; border-color: var(--green); }
.jn-sel { display: block; }
.jn-q { margin: 22px 0 10px; font-weight: 600; font-size: 14.5px; }
.jn-checks { display: flex; flex-wrap: wrap; gap: 8px; }
.jn-checks label { position: relative; display: inline-flex; cursor: pointer; }
.jn-checks input { position: absolute; inset: 0; opacity: 0; margin: 0; cursor: pointer; }
.jn-checks span { display: inline-flex; align-items: center; min-height: 44px; padding: 0 16px; border-radius: 12px; border: 1.5px solid var(--line); font: 600 14.5px/1 var(--head); color: var(--green); transition: background-color .15s, color .15s, border-color .15s; }
.jn-checks input:checked + span { background: var(--green); color: var(--cream); border-color: var(--green); }
.jn-checks input:focus-visible + span { outline: 3px solid var(--peach); outline-offset: 2px; }
.jn-check { display: flex; gap: 12px; align-items: flex-start; margin-bottom: 14px; font-size: 15.5px; line-height: 1.5; cursor: pointer; color: var(--ink); font-weight: 400; }
.jn-check[hidden] { display: none; }
.jn-check input { width: 22px; height: 22px; margin-top: 1px; accent-color: var(--green); flex: none; }
.jn-check a { color: var(--green); }
.jn-agree .btn { margin-top: 8px; }
.jn-status { margin: 12px 0 0; color: var(--clay); font-size: 14.5px; min-height: 1.4em; }
.jn-done { padding: 56px 32px; border-radius: 26px; background: #FFFDF8; text-align: center; display: grid; gap: 10px; }
.jn-done h2 { margin: 0; font: 400 clamp(32px, 4vw, 46px)/1.15 'Newsreader', Georgia, serif; color: var(--green); }
.jn-done p { margin: 0 auto; max-width: 46ch; color: var(--soft); font-size: 17px; }
@media (max-width: 720px) { .jn-paths, .jn-grid { grid-template-columns: minmax(0, 1fr); } .jn-step { padding: 24px 20px; } }
'''

JS = r'''
// Join Always: show the fields for the chosen path; only those are required and sent.
(() => {
  const form = document.getElementById('join-form');
  if (!form) return;
  const status = document.getElementById('jn-status');
  const path = () => form.querySelector('input[name=path]:checked').value;
  const sync = () => {
    const p = path();
    form.querySelectorAll('[data-for]').forEach((el) => { el.hidden = !el.dataset.for.split(' ').includes(p); });
  };
  form.querySelectorAll('input[name=path]').forEach((r) => r.addEventListener('change', sync));
  const preset = () => { const m = location.hash.match(/^#\/join\/(church|evangelist|supporter|platform)/); if (m) { form.querySelector(`input[name=path][value=${m[1]}]`).checked = true; } sync(); };
  window.addEventListener('hashchange', preset); preset();
  const LABEL = { church: 'Church or ministry', evangelist: 'Evangelist', supporter: 'Supporter', platform: 'Tech platform' };
  form.addEventListener('submit', async (e) => {
    e.preventDefault();
    const p = path();
    const need = [...form.querySelectorAll('[required], [data-required]')].filter((el) => !el.closest('[hidden]') && (!el.dataset.required || el.dataset.required.split(' ').includes(p)));
    const empty = need.find((el) => (el.type === 'checkbox' ? !el.checked : !String(el.value).trim()));
    const email = form.elements.email.value.trim();
    if (empty) { status.textContent = 'Please complete the highlighted details and tick the agreement.'; empty.focus(); return; }
    if (!/^[^\s@<>]+@[^\s@<>]+\.[^\s@<>]+$/.test(email)) { status.textContent = 'Please check your email address.'; form.elements.email.focus(); return; }
    if (p === 'church' && !form.querySelector('input[name=states]:checked')) { status.textContent = 'Please choose where you serve.'; form.querySelector('input[name=states]').focus(); return; }
    const data = { path: LABEL[p] };
    const fd = new FormData(form);
    for (const [k, v] of fd) {
      const el = form.elements[k]; const node = el instanceof RadioNodeList ? el[0] : el;
      if (k === 'path' || (node && node.closest && node.closest('[hidden]'))) continue;
      if (!String(v).trim()) continue;
      data[k] = data[k] ? data[k] + ', ' + v : v;
    }
    const LIVE = /(^|\.)alwaysfoundation\.org$/.test(location.hostname);
    if (!LIVE) { status.textContent = 'Registration is not connected on this preview. Please email hello@alwaysfoundation.org.'; return; }
    const b = form.querySelector('button[type=submit]'); b.disabled = true; b.textContent = 'Sending…';
    try {
      const r = await fetch('/api/forms/register', { method: 'POST', headers: { 'content-type': 'application/json', accept: 'application/json' }, body: JSON.stringify(data) });
      if (!r.ok) throw 0;
      const first = String(data.name).trim().split(/\s+/)[0].replace(/[<>&"]/g, '');
      const done = document.createElement('div'); done.className = 'jn-done'; done.tabIndex = -1;
      done.innerHTML = `<h2>Thank you, ${first}.</h2><p>We've received your registration. We'll verify your details and be in touch.</p>`;
      form.replaceWith(done); done.focus();
    } catch {
      status.textContent = 'That didn\'t send. Please try again, or email hello@alwaysfoundation.org.';
      b.disabled = false; b.textContent = 'Register';
    }
  });
})();
'''
