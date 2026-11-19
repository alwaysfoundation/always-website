"""The Developers area: the API, SDK, MCP connector, feeds and webhooks under every Always module."""
from html import escape
import products as PR

# Console examples: a request and a synthetic response. Names and numbers are invented.
CONSOLE = [
    ('find', 'Find a church', 'GET', '/v1/directory?q=parramatta&kind=church',
     '{\n  "items": [\n    {\n      "slug": "example-church-parramatta",\n      "name": "Example Church",\n      "suburb": "Parramatta",\n      "partner": true,\n      "steps": ["visit", "talk", "course"]\n    }\n  ],\n  "next": null\n}', 'docs/feed'),
    ('handoff', 'Hand someone on', 'POST', '/v1/responses',
     '{\n  "ageBand": "18_plus",\n  "step": "talk",\n  "suburb": "Harris Park",\n  "consent": {\n    "purposes": ["connect"],\n    "allowNextNearby": true,\n    "party": "self"\n  }\n}\n\n201 Created\n{ "id": "rsp_7Hq2", "status": "offered" }', 'docs/standard'),
    ('guard', 'Fail closed', 'SDK', "canShare(consent, 'connect')",
     "// A 14-year-old, without a parent's okay\n{\n  \"ok\": false,\n  \"reason\": \"parent_confirmation_required\"\n}\n\n// Nothing moves until it passes.", 'docs/consent'),
    ('mcp', 'Ask an assistant', 'MCP', 'find_churches',
     '// "Which partner churches near Penrith\n//  run a course for new Christians?"\n{\n  "tool": "find_churches",\n  "input": { "near": "Penrith", "step": "course" }\n}\n\n// Public information only. No people.', 'docs/mcp'),
]


FLOW = [
    ('A person responds', 'POST /v1/responses', 'Age band first, then the step they chose and what they agreed to share.'),
    ('One church is offered', 'handoff.offered', 'The nearest partner church that fits. Webhooks carry ids, never names.'),
    ('The church accepts', 'POST /v1/handoffs/:id/accept', 'Their details open to that church only, and the clock for first contact starts.'),
    ('Someone gets in touch', 'POST /v1/handoffs/:id/contacted', 'First contact is logged. If it never comes, the person moves on to the next church.'),
]

GUARDS = [
    ('Consent comes first', 'Every share, sync and export checks it. If someone changes their mind, nothing moves.', 'share(id)', 'refused: withdrawn'),
    ('Young people are protected', 'Age is asked before anything else. A parent says yes for under 15s, and young people never reach AI.', 'canShare(consent)', 'refused: parent_confirmation_required'),
    ('Messages carry ids, not people', 'Webhooks, logs and alerts never hold a name or a number.', 'handoff.accepted', '{ "id": "hnd_8Fa2" }'),
]

WAYS = [
    ('api', 'The API', 'Send responses, receive introductions, manage a church page and read the church feed. Scoped tokens, shown once, revocable.', 'docs/api', 'API reference'),
    ('sdk', 'The SDK', 'A TypeScript client, a drop-in response card, the safety check-up and guardrails that fail closed.', 'docs/sdk', 'SDK guide'),
    ('mcp', 'The MCP connector', 'Let AI assistants find churches, see which are partner churches and list events, using public information only.', 'docs/mcp', 'Connect an assistant'),
]

WAY_ICON = {
    'api': '<path d="M8 7l-5 5 5 5M16 7l5 5-5 5M13.5 5l-3 14"/>',
    'sdk': '<path d="M4 7.5L12 3l8 4.5v9L12 21l-8-4.5z"/><path d="M4 7.5l8 4.5 8-4.5M12 12v9"/>',
    'mcp': '<circle cx="6" cy="12" r="2.5"/><circle cx="18" cy="6" r="2.5"/><circle cx="18" cy="18" r="2.5"/><path d="M8.3 11l7.4-3.8M8.3 13l7.4 3.8"/>',
}

BUILD = [
    ('feed', 'Church feed and finder', 'Partner churches near any postcode, for your website, app or map.', 'docs/feed'),
    ('connect', 'Responses and handoff', 'Pass people to a local partner church, with consent that travels with them.', 'docs/standard'),
    ('compliance', 'Safety infrastructure', 'The open register, change alerts and an embeddable check-up.', 'docs/compliance-platforms'),
    ('webhooks', 'Webhooks', 'Hear about introductions, handoffs and rule changes as they happen.', 'docs/webhooks'),
    ('pages', 'Response pages and embeds', 'Branded response cards and pages you drop into your own site.', 'docs/senders'),
    ('app', 'Scripture', 'The Bible in your app through YouVersion.', 'docs/youversion'),
    ('platforms', 'AI assistants', 'Let assistants find partner churches through the MCP connector, using public information only.', 'docs/mcp'),
    ('consent', 'Consent receipts', 'A record of what each person agreed to, the words they saw and who may see their details.', 'docs/consent'),
    ('journeys', 'Journeys across ministries', 'Link one person&rsquo;s steps across ministries, only with their yes.', 'docs/journeys'),
]


def _way_icon(k):
    return f'<span class="mi" aria-hidden="true"><svg viewBox="0 0 24 24">{WAY_ICON[k]}</svg></span>'


def _console():
    tabs = ''.join(
        f'<button type="button" role="tab" class="sw-tab" id="dv-t-{k}" aria-controls="dv-p-{k}" aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}">{n}</button>'
        for i, (k, n, _, _, _, _) in enumerate(CONSOLE))
    panels = ''.join(
        f'<div class="sw-panel dvc-panel" role="tabpanel" id="dv-p-{k}" aria-labelledby="dv-t-{k}"{"" if i == 0 else " hidden"}>'
        f'<p class="dvc-req"><span class="dvc-m dvc-m-{m.lower()}">{m}</span><code>{escape(path)}</code></p>'
        f'<pre class="dvc-out"><code>{"".join(f"<span>{escape(line) or " "}</span>" for line in out.split(chr(10)))}</code></pre>'
        f'<a class="dvc-doc" href="#/{doc}">Read the docs</a></div>'
        for i, (k, n, m, path, out, doc) in enumerate(CONSOLE))
    return (f'<div class="sw dvc" data-dvc><div class="dvc-bar"><span class="dvc-dots" aria-hidden="true"><i></i><i></i><i></i></span>'
            f'<span class="dvc-host">api.alwaysfoundation.org</span></div>'
            f'<div class="sw-tabs" role="tablist" aria-label="Examples">{tabs}</div>{panels}'
            f'<p class="dvc-note">Example data. Names are invented.</p></div>')


PAGE = f'''<section class="page-hero dv-hero"><div class="wrap dv-split">
  <div class="dv-copy"><p class="pl-kick">Developers</p>
  <h1>Build with the Body.</h1>
  <p>The same open-source API, SDK and AI connector every Always module runs on. Help people who say yes to Jesus find a local church, from your own website, app or event. Free for churches and ministries.</p>
  <div class="pg-cta"><a class="btn btn-peach" href="#/docs/api">Read the docs</a><a class="btn btn-ghost" href="#/join/platform">Ask for a key</a></div></div>
  {_console()}
</div></section>
<section class="sec pg-sec dv-flow-sec"><div class="wrap">
  <h2 class="pg-h rv">A handoff, end to end.</h2>
  <p class="pg-lead rv">Four calls take someone from a moment of decision to a real person at a church near home.</p>
  <ol class="dv-flow">{''.join(f'<li class="rv"><span class="dv-n" aria-hidden="true">{i}</span><h3>{t}</h3><code>{escape(c)}</code><p>{p}</p></li>' for i, (t, c, p) in enumerate(FLOW, 1))}</ol>
</div></section>
<section class="sec pg-sec dv-guard-sec"><div class="wrap">
  <h2 class="pg-h rv">Care, built in.</h2>
  <p class="pg-lead rv">Every integration inherits the same promises to the people it serves.</p>
  <div class="dv-cards">{''.join(f'<div class="dv-card rv"><h3>{t}</h3><p>{p}</p><code><span>{escape(c)}</span><b>{escape(r)}</b></code></div>' for t, p, c, r in GUARDS)}</div>
</div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">Three ways in.</h2>
  <div class="dv-ways">{''.join(f'<a class="dv-way rv" href="#/{d}">{_way_icon(k)}<h3>{t}</h3><p>{p}</p><span class="dv-go">{l}</span></a>' for k, t, p, d, l in WAYS)}</div>
</div></section>
<section class="sec pg-sec pg-sage"><div class="wrap">
  <h2 class="pg-h rv">What you can build.</h2>
  <div class="dv-build">{''.join(f'<a class="pd-link rv" href="#/{d}">{PR.mod_icon(s)}<b>{t}</b><span>{p}</span></a>' for s, t, p, d in BUILD)}</div>
</div></section>
<section class="sec pg-sec"><div class="wrap sl-end">
  <h2 class="pg-h rv">Building for churches or ministries?</h2>
  <p class="pg-lead rv">Tell us what you&rsquo;re making. We&rsquo;ll help you get started and keep it safe for the people it serves.</p>
  <div class="pg-cta rv"><a class="btn btn-peach" href="#/contact/developer">Talk to us</a><a class="btn btn-green" href="#/docs/introduction">Browse the docs</a></div>
</div></section>'''

CSS = '''
/* ---- Developers ---- */
.dv-hero { padding-bottom: 72px; }
.dv-split { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.05fr); gap: 56px; align-items: center; }
.dv-copy h1 { font-size: clamp(48px, 6.4vw, 92px); line-height: .95; letter-spacing: -.035em; }
.dv-copy > p:not(.pl-kick):not(.dv-pilot) { max-width: 46ch; margin-top: 22px; font-size: 19px; line-height: 1.55; color: rgba(248,243,234,.82); }
.page-hero p.dv-pilot, .page-hero p.dvc-note { max-width: none; }
.page-hero p.dv-pilot { font-size: 14px; }
.page-hero p.dvc-note { font-size: 12.5px; margin: 0; }
.dv-pilot { display: inline-flex; align-items: center; gap: 10px; margin-top: 22px; padding: 9px 14px; border-radius: 999px; background: rgba(248,243,234,.08); font: 600 14px/1.3 var(--head); color: var(--cream); }
.dv-pilot i { width: 8px; height: 8px; border-radius: 50%; background: var(--peach); box-shadow: 0 0 0 4px rgba(232,165,122,.25); }
.dvc { padding: 0; border-radius: 26px; background: #102A25; box-shadow: inset 0 0 0 1px rgba(248,243,234,.08), 0 40px 80px -40px rgba(0,0,0,.7); overflow: hidden; }
.dvc-bar { display: flex; align-items: center; gap: 12px; padding: 14px 18px; border-bottom: 1px solid rgba(248,243,234,.07); font: 500 13px/1 var(--head); color: rgba(248,243,234,.6); }
.dvc-dots { display: flex; gap: 6px; } .dvc-dots i { width: 10px; height: 10px; border-radius: 50%; background: rgba(248,243,234,.16); }
.dvc-host { flex: 1; }
.dvc-au { padding: 5px 10px; border-radius: 999px; background: rgba(232,165,122,.14); color: var(--peach); font-weight: 600; }
.dvc .sw-tabs { margin: 14px 16px 0; }
.dvc .dvc-panel p.dvc-req { margin: 0; font-size: inherit; max-width: none; }
.dvc-panel { padding: 20px 22px 18px; }
.dvc-req { display: flex; align-items: center; gap: 10px; min-width: 0; }
.dvc-req code { font: 500 14px/1.4 ui-monospace, 'SF Mono', Menlo, monospace; color: var(--cream); overflow-wrap: anywhere; }
.dvc-m { flex: none; padding: 4px 8px; border-radius: 7px; font: 700 12px/1 var(--head); background: rgba(248,243,234,.1); color: var(--cream); }
.dvc-m-post { background: rgba(232,165,122,.2); color: var(--peach); }
.dvc-m-get { background: rgba(167,207,186,.18); color: #A7CFBA; }
.dvc-out { margin: 16px 0 0; padding: 18px; min-height: 270px; border-radius: 16px; background: rgba(0,0,0,.22); overflow-x: auto; }
.dvc-out code { display: block; font: 500 13px/1.7 ui-monospace, 'SF Mono', Menlo, monospace; color: #DCE7DF; white-space: pre; }
.dvc-out span { display: block; }
.dvc.go .dvc-panel:not([hidden]) .dvc-out span { animation: dvLine .35s ease both; }
''' + ''.join(f'.dvc.go .dvc-out span:nth-child({i}) {{ animation-delay: {i * 0.05:.2f}s; }}\n' for i in range(1, 16)) + '''
@keyframes dvLine { from { opacity: 0; transform: translateY(4px); } to { opacity: 1; transform: none; } }
.dvc-doc { display: inline-block; margin-top: 14px; color: var(--peach); font: 600 14px/1 var(--head); text-underline-offset: 3px; }
.dvc-note { padding: 0 22px 18px; font-size: 12.5px; color: rgba(248,243,234,.45); }
.dv-flow { list-style: none; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 16px; margin: 40px 0 0; padding: 0; counter-reset: none; position: relative; }
.dv-flow::before { content: ''; position: absolute; top: 22px; left: 22px; right: 22px; height: 2px; background: linear-gradient(90deg, var(--peach), rgba(232,165,122,.15)); }
.dv-flow li { position: relative; }
.dv-n { position: relative; display: grid; place-items: center; width: 44px; height: 44px; border-radius: 50%; background: var(--green); color: var(--cream); font: 800 17px/1 var(--head); box-shadow: 0 0 0 6px var(--cream-bg, #F6F1E8); }
.dv-flow h3 { margin-top: 20px; font: 800 20px/1.2 var(--head); color: var(--green); }
.dv-flow code { display: inline-block; margin-top: 10px; padding: 6px 9px; border-radius: 8px; background: #E9EFE9; color: var(--green); font: 600 12.5px/1.3 ui-monospace, 'SF Mono', Menlo, monospace; overflow-wrap: anywhere; }
.dv-flow p { margin-top: 10px; font-size: 15.5px; line-height: 1.55; color: var(--soft); }
.dv-guard-sec { background: #14352F; color: var(--cream); }
.dv-guard-sec .pg-h { color: var(--cream); } .dv-guard-sec .pg-lead { color: rgba(248,243,234,.75); }
.dv-cards { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px; margin-top: 40px; }
.dv-card { display: flex; flex-direction: column; gap: 12px; padding: 30px 28px 26px; border-radius: 26px; background: linear-gradient(165deg, rgba(248,243,234,.07), rgba(248,243,234,.02)); box-shadow: inset 0 0 0 1px rgba(248,243,234,.09); }
.dv-card h3 { font: 800 24px/1.2 var(--head); letter-spacing: -.015em; color: var(--cream); }
.dv-card p { font-size: 16px; line-height: 1.55; color: rgba(248,243,234,.72); }
.dv-card code { margin-top: auto; display: grid; gap: 6px; padding: 16px 18px; border-radius: 16px; background: #0D241F; font: 500 13px/1.5 ui-monospace, 'SF Mono', Menlo, monospace; overflow-wrap: anywhere; }
.dv-card code span { color: rgba(220,231,223,.6); } .dv-card code b { color: var(--peach); font-weight: 600; }
.dv-ways { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; margin-top: 32px; }
.dv-way { display: grid; align-content: start; gap: 10px; padding: 28px; border-radius: 24px; background: #FFFDF8; color: inherit; text-decoration: none; box-shadow: 0 1px 0 rgba(27,71,64,.06); transition: transform .2s ease, box-shadow .2s ease; }
.dv-way:hover, .dv-way:focus-visible { transform: translateY(-3px); box-shadow: 0 24px 44px -30px rgba(10,30,26,.45); }
.dv-way h3 { margin-top: 8px; font: 800 22px/1.2 var(--head); color: var(--green); }
.dv-way p { font-size: 15.5px; line-height: 1.55; color: var(--soft); }
.dv-go { margin-top: 6px; font: 600 15px/1 var(--head); color: var(--clay, #B55A2E); }
.dv-build { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; margin-top: 32px; }
@media (max-width: 1000px) {
  .dv-split { grid-template-columns: 1fr; gap: 40px; }
  .dv-cards { grid-template-columns: 1fr; }
  .dv-flow { grid-template-columns: 1fr 1fr; row-gap: 36px; } .dv-flow::before { display: none; }
  .dv-ways, .dv-build { grid-template-columns: 1fr; }
}
@media (max-width: 640px) {
  .dv-flow { grid-template-columns: 1fr; }
  .dvc .sw-tabs { flex-wrap: wrap; overflow: visible; } .dvc-req { flex-wrap: wrap; } .dvc-panel { padding: 16px; }
  .dvc-out { min-height: 0; } .dvc-out code { font-size: 12px; }
  }
@media (prefers-reduced-motion: reduce) { .dvc.go .dvc-out span { animation: none !important; } .dv-way { transition: none; } }
'''

JS = r'''
// Developer console: lines arrive once when it comes into view, and again on each tab change.
(() => {
  const c = document.querySelector('[data-dvc]'); if (!c) return;
  const replay = () => { c.classList.remove('go'); void c.offsetWidth; c.classList.add('go'); };
  new IntersectionObserver((es, o) => { if (es[0].isIntersecting) { replay(); o.disconnect(); } }).observe(c);
  c.querySelectorAll('.sw-tab').forEach((t) => t.addEventListener('click', replay));
})();
'''
