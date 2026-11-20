"""Home module showcase, and the shared look of the module pages."""
from mocks import mock
import products as PR

ORDER = ['app', 'pages', 'connect', 'compliance', 'reports']
CHIPS = {
    'app': ('The Good News, verse by verse', 'Runs in any browser'),
    'pages': ('QR code, tap or link', 'Your name, your colours'),
    'connect': ('Partner churches nearby', 'Consent travels with them'),
    'compliance': ('A check-up every quarter', 'State by state'),
    'reports': ('Totals only, never names', 'Written for you, monthly'),
}
TONE = {'app': 'peach', 'pages': 'peach', 'connect': 'sand', 'compliance': 'sage', 'reports': 'sage'}


def _tab(i, s):
    route, name, _, line, _ = PR.PRODUCTS[s]
    return (f'<button type="button" role="tab" class="msx-tab" id="msx-t-{s}" aria-controls="msx-p-{s}" aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}">'
            f'<span class="msx-ic">{PR._icon(s)}</span><span class="msx-tt"><span class="msx-verb">{PR.VERBS[s]}</span><b>{name}</b></span><i class="msx-bar" aria-hidden="true"></i></button>')


def _panel(i, s):
    route, name, _, line, _ = PR.PRODUCTS[s]
    a, b = CHIPS[s]
    return (f'<div class="msx-panel msx-{TONE[s]}" role="tabpanel" id="msx-p-{s}" aria-labelledby="msx-t-{s}"{"" if i == 0 else " hidden"}>'
            f'<div class="msx-art"><span class="msx-chip msx-c1">{a}</span>{mock(s, "mk-lg")}<span class="msx-chip msx-c2">{b}</span></div>'
            f'<div class="msx-cap"><p><b>{name}.</b> {line}</p><a href="#/{route}">Explore {name}</a></div></div>')


def home_showcase():
    return ('<div class="msx rv" data-msx>'
            f'<div class="msx-tabs" role="tablist" aria-label="Always Platform modules">{"".join(_tab(i, s) for i, s in enumerate(ORDER))}</div>'
            f'<div class="msx-stage">{"".join(_panel(i, s) for i, s in enumerate(ORDER))}</div></div>')


def stage(slug):
    a, b = CHIPS.get(slug, ('', ''))
    return f'<div class="pd-stage msx-{TONE.get(slug, "sage")}"><span class="msx-chip msx-c1">{a}</span>{mock(slug, "mk-lg")}<span class="msx-chip msx-c2">{b}</span></div>'


CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def feats(items):
    return '<div class="md-feats">' + ''.join(f'<div class="md-feat rv"><span class="md-ck">{CHECK}</span><h3>{t}</h3><p>{d}</p></div>' for t, d in items) + '</div>'


def works_with(slugs):
    return '<div class="md-with">' + ''.join(
        f'<a class="md-mod rv" href="#/{PR.PRODUCTS[s][0]}"><span class="msx-ic">{PR._icon(s)}</span><span><span class="msx-verb">{PR.VERBS[s]}</span><b>{PR.PRODUCTS[s][1]}</b><em>{PR.PRODUCTS[s][3]}</em></span></a>'
        for s in slugs) + '</div>'


def closing(slug):
    name = PR.PRODUCTS[slug][1]
    return (f'<section class="sec md-close"><div class="wrap"><div class="md-close-in rv">'
            f'<div><h2>Switch on {name}.</h2><p>Free for churches. One sign-in for your whole team, and your people’s details kept in Australia.</p></div>'
            f'<div class="pg-cta"><a class="btn btn-peach" href="#/join">Partner with Always</a><a class="btn btn-ghost" href="#/contact">Talk to us</a></div>'
            f'</div></div></section>')


CSS = r'''
/* ---- Home hero ---- */
.hx2 { position: relative; overflow: hidden; isolation: isolate; padding-top: clamp(104px, 15vh, 170px) !important; padding-bottom: clamp(48px, 7vw, 96px) !important; }
.hx2-in { position: relative; display: grid; justify-items: center; text-align: center; padding-top: clamp(0px, 4vh, 60px); padding-bottom: clamp(0px, 3vh, 40px); }
.hx2 h1 { margin: 0; font-size: clamp(54px, 10.5vw, 172px); line-height: .92; letter-spacing: -.045em; max-width: 11ch; }
.hw { display: inline-block; white-space: nowrap; overflow: hidden; padding: .04em .015em .14em; margin: -.04em 0 -.14em; vertical-align: top; }
.hxc { display: inline-block; position: static; }
.hx2 .lede { max-width: 34ch; margin: 30px auto 0; font-size: clamp(18px, 1.6vw, 23px); line-height: 1.5; color: rgba(248,243,234,.82); }
.hx2 .ctas { justify-content: center; margin-top: 32px; }
.hx2-light { position: absolute; inset: 0; z-index: -1; pointer-events: none; }
.hx2-light i { position: absolute; left: 50%; top: -30%; width: min(1100px, 120vw); aspect-ratio: 1; border-radius: 50%; transform: translateX(-50%);
  background: radial-gradient(closest-side, rgba(248,243,234,.11), rgba(248,243,234,.04) 45%, rgba(248,243,234,0) 70%); }
.hx2-light i + i { top: auto; bottom: -55%; width: min(900px, 110vw); background: radial-gradient(closest-side, rgba(77,150,128,.35), rgba(77,150,128,0) 70%); }
@media (prefers-reduced-motion: no-preference) {
  .hxc { transform: translateY(105%) rotate(8deg); transform-origin: 0 100%; filter: blur(6px); opacity: 0; animation: hxChar 1s cubic-bezier(.16,.8,.2,1) forwards; animation-delay: calc(.25s + var(--c) * .04s); }
  .hx2 .lede, .hx2 .ctas { opacity: 0; animation: hxFade .9s ease forwards; }
  .hx2 .lede { animation-delay: 1s; } .hx2 .ctas { animation-delay: 1.2s; }
  .hx2-light i { opacity: 0; animation: hxLight 2.2s ease .1s forwards; } .hx2-light i + i { animation-delay: .6s; }
}
@keyframes hxChar { 60% { filter: blur(0); } to { transform: none; filter: none; opacity: 1; } }
@keyframes hxFade { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: none; } }
@keyframes hxLight { to { opacity: 1; } }
@media (max-width: 640px) { .hx2 { padding-top: 112px !important; padding-bottom: 40px !important; } .hx2-in { padding-top: 8px; padding-bottom: 0; } .hx2 .ctas { flex-wrap: wrap; } }

/* ---- Home module showcase ---- */
.ex { max-width: 760px; margin-top: 30px; padding: 26px 30px; border-radius: 24px; background: #FFFDF8; box-shadow: 0 1px 0 rgba(27,71,64,.06); }
.ex-k { font: 700 15px/1.2 var(--head); color: var(--peach-d, #B55A2E); margin-bottom: 10px; }
.ex p { font-size: 17px; line-height: 1.6; }
.ex .ex-f { margin-top: 14px; font-size: 15px; color: var(--muted); }
.ex .ex-f a { color: var(--green); font-weight: 600; text-underline-offset: 3px; }
.msx-cap .st { margin: 0 0 0 6px; vertical-align: 2px; }
@media (max-width: 640px) { .ex { padding: 22px; } }
.msx { display: grid; grid-template-columns: 330px minmax(0, 1fr); gap: 28px; margin-top: 48px; align-items: stretch; }
.msx-tabs { display: grid; gap: 6px; align-content: start; }
.msx-tab { position: relative; display: grid; grid-template-columns: 44px minmax(0, 1fr); gap: 14px; align-items: center; width: 100%; min-height: 76px; padding: 14px 16px; border: 0; border-radius: 20px; background: transparent; text-align: left; cursor: pointer; color: inherit; font: inherit; overflow: hidden; transition: background .3s ease; }
.msx-tab:hover { background: rgba(27,71,64,.05); }
.msx-tab[aria-selected="true"] { background: #FFFDF8; box-shadow: 0 1px 0 rgba(27,71,64,.06), 0 18px 36px -28px rgba(10,30,26,.45); }
.msx-tab:focus-visible { outline: 3px solid var(--green); outline-offset: 2px; }
.msx-ic .dd-ic { background: none !important; width: auto; height: auto; }
.msx-ic svg { width: 22px; height: 22px; }
.msx-tt { display: grid; gap: 2px; }
.msx-verb { font: 700 12.5px/1.2 var(--head); color: var(--clay); }
.msx-tt b { font: 800 19px/1.2 var(--head); color: var(--green); letter-spacing: -0.015em; }
.msx-bar { position: absolute; left: 16px; right: 16px; bottom: 8px; height: 2px; border-radius: 2px; background: rgba(27,71,64,.08); opacity: 0; }
.msx-bar::after { content: ''; position: absolute; inset: 0; border-radius: 2px; background: var(--peach); transform: scaleX(0); transform-origin: 0 50%; }
.msx.auto .msx-tab[aria-selected="true"] .msx-bar { opacity: 1; }
.msx.auto .msx-tab[aria-selected="true"] .msx-bar::after { animation: msxBar var(--msx-t, 7s) linear forwards; }
.msx.paused .msx-tab[aria-selected="true"] .msx-bar::after { animation-play-state: paused; }
@keyframes msxBar { to { transform: scaleX(1); } }
.msx-stage { position: relative; min-height: 560px; }
.msx-panel { position: absolute; inset: 0; display: grid; grid-template-rows: minmax(0, 1fr) auto; border-radius: 32px; overflow: hidden; }
.msx-panel[hidden] { display: none; }
.msx-panel:not([hidden]) { animation: msxIn .55s cubic-bezier(.2,.7,.2,1) both; }
@keyframes msxIn { from { opacity: 0; transform: translateY(10px) scale(.99); } }
.msx-peach { background: radial-gradient(120% 90% at 70% 10%, #FBE7D8 0%, #F3D9C4 55%, #EBC9AE 100%); }
.msx-sage { background: radial-gradient(120% 90% at 70% 10%, #E6F0EA 0%, #D3E4DA 55%, #C2D8CB 100%); }
.msx-sand { background: radial-gradient(120% 90% at 70% 10%, #F4EDE0 0%, #E9DFCC 55%, #DDD0B6 100%); }
.msx-art { position: relative; display: grid; place-items: center; padding: 56px 40px 24px; }
.msx-art .mk, .pd-stage .mk { background: transparent !important; box-shadow: none !important; padding: 0 !important; }
.msx-art .mk { transform: scale(1.25); transform-origin: center; }

.msx-ic .dd-ic, .md-mod .dd-ic { display: grid !important; place-items: center; color: inherit !important; }
.msx-ic svg * { stroke: currentColor; }
.msx-art .mk::before, .msx-art .mk::after, .pd-stage .mk::before, .pd-stage .mk::after { display: none !important; }
.msx-tab[aria-selected="true"] .msx-ic { color: var(--cream); }
.msx-art .mk-card, .pd-stage .mk-card { box-shadow: 0 1px 0 rgba(30,42,38,.04), 0 22px 36px -24px rgba(20,53,47,.32) !important; }
.msx-chip { position: absolute; z-index: 2; display: inline-flex; align-items: center; gap: 8px; padding: 9px 14px; border-radius: 999px; background: rgba(255,253,248,.92); backdrop-filter: blur(6px); box-shadow: 0 14px 30px -18px rgba(10,30,26,.45); font: 700 13.5px/1.2 var(--head); color: var(--green); white-space: nowrap; }
.msx-chip::before { content: ''; width: 8px; height: 8px; border-radius: 50%; background: var(--peach); }
.msx-c1 { left: 7%; top: 12%; animation: msxFloat 6s ease-in-out infinite; }
.msx-c2 { right: 7%; bottom: 10%; animation: msxFloat 6s ease-in-out 3s infinite; }
@keyframes msxFloat { 50% { transform: translateY(-6px); } }
.msx-cap { display: flex; align-items: center; justify-content: space-between; gap: 24px; margin: 0 16px 16px; padding: 18px 22px; border-radius: 20px; background: rgba(255,253,248,.82); backdrop-filter: blur(8px); }
.msx-cap p { margin: 0; font-size: 16.5px; line-height: 1.5; color: var(--ink); max-width: 60ch; }
.msx-cap b { color: var(--green); }
.msx-cap a { flex: none; display: inline-flex; align-items: center; min-height: 44px; padding: 0 18px; border-radius: 14px; background: var(--green); color: var(--cream); font: 700 15px/1 var(--head); text-decoration: none; transition: transform .2s ease; }
.msx-cap a:hover { transform: translateY(-1px); }
@media (max-width: 1000px) {
  .msx { grid-template-columns: minmax(0, 1fr); gap: 16px; }
  .msx-tabs { display: flex; overflow-x: auto; scroll-snap-type: x mandatory; gap: 8px; padding-bottom: 4px; scrollbar-width: none; margin: 0 -22px; padding-inline: 22px; }
  .msx-tabs::-webkit-scrollbar { display: none; }
  .msx-tab { flex: none; width: auto; min-height: 60px; grid-template-columns: 36px auto; padding: 10px 16px 10px 10px; scroll-snap-align: start; background: rgba(27,71,64,.05); }
  .msx-ic { width: 36px; height: 36px; border-radius: 11px; }
  .msx-tt b { font-size: 16px; }
  .msx-stage { min-height: 520px; }
}
@media (max-width: 640px) {
  .msx-stage { min-height: 500px; }
  .msx-art { padding: 64px 14px 14px; }
  .msx-art .mk { transform: scale(1); }
  .msx-chip { font-size: 12px; padding: 7px 11px; }
  .msx-c1 { left: 12px; top: 14px; } .msx-c2 { right: 12px; bottom: 6px; }
  .msx-cap { flex-direction: column; align-items: flex-start; gap: 12px; margin: 0 10px 10px; padding: 16px; }
}

/* ---- Module pages ---- */
.pd-stage { position: relative; display: grid; place-items: center; min-height: 440px; padding: 56px 36px; border-radius: 32px; box-shadow: 0 40px 80px -40px rgba(0,0,0,.45); }
.pd-stage .mk { transform: scale(1.15); }
.pd-hero .pd-stage .mk { animation: none; }
.md-feats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 16px; margin-top: 36px; }
.md-feat { position: relative; padding: 26px 24px 26px; border-radius: 24px; background: #FFFDF8; border: 1px solid var(--line); transition: transform .3s cubic-bezier(.2,.7,.2,1), box-shadow .3s ease, border-color .3s ease; }
.md-feat:hover { transform: translateY(-3px); border-color: rgba(27,71,64,.2); box-shadow: 0 24px 44px -30px rgba(10,30,26,.4); }
.md-ck { display: grid; place-items: center; width: 36px; height: 36px; border-radius: 50%; background: var(--sage); color: var(--green); margin-bottom: 18px; }
.md-ck svg { width: 18px; height: 18px; }
.md-feat h3 { margin: 0 0 8px; font-size: 20px; letter-spacing: -0.015em; color: var(--green); }
.md-feat p { margin: 0; font-size: 16px; line-height: 1.55; color: var(--soft); }
.md-with { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; margin-top: 28px; }
.md-mod { display: grid; grid-template-columns: 44px minmax(0, 1fr); gap: 14px; align-items: start; padding: 20px; border-radius: 22px; background: #FFFDF8; color: inherit; text-decoration: none; transition: transform .25s cubic-bezier(.2,.7,.2,1), box-shadow .25s ease; }
.md-mod:hover, .md-mod:focus-visible { transform: translateY(-2px); box-shadow: 0 20px 40px -28px rgba(10,30,26,.45); }
.md-mod b { display: block; margin-top: 2px; font: 800 18px/1.2 var(--head); color: var(--green); }
.md-mod em { display: block; margin-top: 6px; font-style: normal; font-size: 14.5px; line-height: 1.5; color: var(--soft); }
.md-close { padding-top: 0; }
.md-close-in { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 32px; align-items: center; padding: clamp(32px, 4vw, 52px); border-radius: 32px; background: var(--green); color: var(--cream); position: relative; overflow: hidden; }
.md-close-in::after { content: ''; position: absolute; right: -10%; top: -60%; width: 60%; height: 220%; background: radial-gradient(closest-side, rgba(232,165,119,.2), rgba(232,165,119,0)); pointer-events: none; }
.md-close-in h2 { margin: 0; font-size: clamp(30px, 3.4vw, 46px); letter-spacing: -0.035em; color: var(--cream); }
.md-close-in p { margin: 10px 0 0; font-size: 17px; color: var(--on-green); max-width: 50ch; }
.md-close-in .pg-cta { position: relative; z-index: 1; margin: 0; }
@media (max-width: 1000px) { .md-feats, .md-with { grid-template-columns: repeat(2, minmax(0, 1fr)); } .md-close-in { grid-template-columns: minmax(0, 1fr); } }
@media (max-width: 640px) { .md-feats, .md-with { grid-template-columns: minmax(0, 1fr); } .pd-stage { min-height: 360px; padding: 64px 14px 40px; } .pd-stage .mk { transform: scale(1); } }
@media (prefers-reduced-motion: reduce) {
  .msx-panel:not([hidden]), .msx-chip, .msx.auto .msx-tab[aria-selected="true"] .msx-bar::after { animation: none !important; }
  .md-feat, .md-mod, .msx-tab, .msx-cap a { transition: none; } .md-feat:hover, .md-mod:hover { transform: none; }
}
'''

JS = r'''
(function () {
  document.querySelectorAll('[data-msx]').forEach((root) => {
    const tabs = [...root.querySelectorAll('.msx-tab')];
    const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
    let i = 0, timer = null, inView = false, hold = false;
    const T = 7000;
    function show(n, focus) {
      i = (n + tabs.length) % tabs.length;
      tabs.forEach((t, k) => {
        const on = k === i;
        t.setAttribute('aria-selected', on); t.tabIndex = on ? 0 : -1;
        document.getElementById(t.getAttribute('aria-controls')).hidden = !on;
        if (on) { const bar = t.querySelector('.msx-bar'); bar.replaceWith(bar.cloneNode(true)); }
      });
      if (focus) tabs[i].focus();
      schedule();
    }
    function schedule() {
      clearTimeout(timer);
      const auto = !reduce && inView && !hold;
      root.classList.toggle('auto', !reduce);
      root.classList.toggle('paused', !auto);
      if (auto) timer = setTimeout(() => show(i + 1), T);
    }
    tabs.forEach((t, k) => {
      t.addEventListener('click', () => { hold = true; show(k); });
      t.addEventListener('keydown', (e) => {
        if (['ArrowDown', 'ArrowRight'].includes(e.key)) { e.preventDefault(); hold = true; show(i + 1, true); }
        if (['ArrowUp', 'ArrowLeft'].includes(e.key)) { e.preventDefault(); hold = true; show(i - 1, true); }
      });
    });
    root.addEventListener('mouseenter', () => { hold = true; schedule(); });
    root.addEventListener('mouseleave', () => { hold = false; schedule(); });
    root.addEventListener('focusin', () => { hold = true; schedule(); });
    if ('IntersectionObserver' in window) new IntersectionObserver((es) => { inView = es[0].isIntersecting; schedule(); }, { threshold: 0.35 }).observe(root);
    root.style.setProperty('--msx-t', T + 'ms');
    schedule();
  });
})();
'''
