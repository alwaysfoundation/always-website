"""Final visual layer, loaded last: quiet hairline rows instead of card grids, serif step numerals."""

JS = r'''
// Tiles come alive on hover or keyboard focus; on touch screens, when they scroll into view.
(() => {
  if (!matchMedia('(hover: none)').matches || !('IntersectionObserver' in window)) return;
  const io = new IntersectionObserver((es) => es.forEach((e) => e.target.classList.toggle('is-live', e.isIntersecting)), { threshold: 0.6 });
  document.querySelectorAll('.bt, .cmx-tile, .dg-mod').forEach((t) => io.observe(t));
})();
'''

CSS = '''
/* ---- Quiet rows in place of card grids ---- */
.pg-feats { column-gap: 48px; row-gap: 0; }
.pg-feats .pg-feat, .pg-sage .pg-feats .pg-feat { background: none; border-radius: 0; padding: 28px 0 32px; border-top: 1px solid rgba(27,71,64,.16); box-shadow: none; }
.pg-feats .pg-feat h3 { margin: 0 0 8px; font-size: 21px; color: var(--green); }
.pg-feats .pg-feat p { max-width: 38ch; }
.pg-night .pg-feats .pg-feat, .pg-green .pg-feats .pg-feat { border-top-color: rgba(248,243,234,.16); }
.pg-night .pg-feats .pg-feat h3, .pg-green .pg-feats .pg-feat h3 { color: var(--cream); }
.pg-night .pg-feats .pg-feat p, .pg-green .pg-feats .pg-feat p { color: var(--on-green); }

/* ---- Steps: a real sequence, so numbered, in serif ---- */
.pg-steps { column-gap: 48px; }
.pg-steps .pg-step { background: none; border-radius: 0; padding: 26px 0 0; border-top: 2px solid var(--green); }
.pg-steps .pg-step span { display: block; font: 400 44px/1 'Newsreader', Georgia, serif; color: var(--clay); margin-bottom: 18px; }
.pg-steps .pg-step h3 { margin-top: 0; }

/* ---- Compliance steps, same language ---- */
.cm-steps { column-gap: 40px; row-gap: 0; }
.cm-steps li { background: none; border-radius: 0; padding: 26px 0 0; border-top: 2px solid var(--green); }
.cm-steps li::before { content: counter(s, decimal-leading-zero); display: block; width: auto; height: auto; background: none; border-radius: 0; font: 400 44px/1 'Newsreader', Georgia, serif; color: var(--clay); margin-bottom: 18px; }

/* ---- About: vision, name, posture ---- */
.mv { column-gap: 48px; row-gap: 0; }
.mv div { background: none; border-radius: 0; padding: 28px 0 0; border-top: 1px solid rgba(27,71,64,.16); }

/* ---- Solution heroes with a product screen ---- */
.page-hero .pd-split .pg-cta { margin-top: 28px; }
.sl-end { text-align: center; }
.sl-end .pg-lead { margin-left: auto; margin-right: auto; }
.sl-end .pg-cta { justify-content: center; }

/* ---- Hero: one orchestrated moment ---- */
.hero { position: relative; overflow: hidden; }
.hero .wrap { position: relative; z-index: 1; }
.hero::before { content: ''; position: absolute; width: 70vw; height: 70vw; max-width: 1000px; max-height: 1000px; right: -18vw; top: -35%; border-radius: 50%; background: radial-gradient(closest-side, rgba(232,165,119,.16), rgba(232,165,119,0)); animation: glowDrift 18s ease-in-out infinite alternate; pointer-events: none; }
.hero::after { content: ''; position: absolute; width: 50vw; height: 50vw; left: -16vw; bottom: -40%; border-radius: 50%; background: radial-gradient(closest-side, rgba(207,224,214,.07), rgba(207,224,214,0)); pointer-events: none; }
@keyframes glowDrift { from { transform: translate(0, 0); } to { transform: translate(-6vw, 8%); } }
.hero h1 { animation: heroUp .9s cubic-bezier(.2,.8,.2,1) both; }
.hero-side > * { animation: heroUp .9s cubic-bezier(.2,.8,.2,1) both; }
.hero-side > *:nth-child(1) { animation-delay: .15s; } .hero-side > *:nth-child(2) { animation-delay: .28s; } .hero-side > *:nth-child(3) { animation-delay: .4s; }
@keyframes heroUp { from { opacity: 0; transform: translateY(18px); } to { opacity: 1; transform: none; } }

/* ---- Tiles that respond ---- */
.bt .mk-card, .bt .mk-conn { transition: transform .35s cubic-bezier(.2,.8,.2,1); }
.bt:hover .mk-card, .bt:focus-visible .mk-card, .bt.is-live .mk-card, .bt:hover .mk-conn, .bt.is-live .mk-conn { transform: translateY(-4px) scale(1.02); }
.bt .mk { transition: background-color .4s ease; }
/* App: pray, and the tabs move on */
.mk-app .mk-pill { transition: background-color .3s, color .3s; }
.bt:hover .mk-app .mk-pill:first-child, .bt:focus-visible .mk-app .mk-pill:first-child, .bt.is-live .mk-app .mk-pill:first-child { background: var(--peach); color: var(--night); }
.mk-tabs i { transition: background-color .3s; }
.bt:hover .mk-tabs i.on, .bt.is-live .mk-tabs i.on { background: var(--line); }
.bt:hover .mk-tabs i:nth-child(2), .bt.is-live .mk-tabs i:nth-child(2) { background: var(--peach); }
/* Pages: your brand, any colour */
@keyframes brandCycle { 0%, 100% { background: #6B4FA0; } 33% { background: #C2562E; } 66% { background: #1F6F78; } }
.bt:hover .mk-pages .mk-logo, .bt:hover .mk-pages .mk-btn, .bt:focus-visible .mk-pages .mk-logo, .bt:focus-visible .mk-pages .mk-btn, .bt.is-live .mk-pages .mk-logo, .bt.is-live .mk-pages .mk-btn { animation: brandCycle 3.6s ease-in-out infinite; }
/* Compliance: the last item gets done */
.mk-comp i.due, .mk-comp li em { transition: all .35s ease; }
.bt:hover .mk-comp i.due, .bt:focus-visible .mk-comp i.due, .bt.is-live .mk-comp i.due { background: var(--green); box-shadow: none; }
.bt:hover .mk-comp li em, .bt:focus-visible .mk-comp li em, .bt.is-live .mk-comp li em { opacity: 0; transform: translateX(6px); }
/* Reports: the month fills in */
@keyframes barGrow { from { width: 0; } }
.bt:hover .mk-bar::before, .bt:focus-visible .mk-bar::before, .bt.is-live .mk-bar::before { animation: barGrow .9s cubic-bezier(.2,.8,.2,1) both; }
.bt:hover .mk-bar:nth-child(3)::before, .bt.is-live .mk-bar:nth-child(3)::before { animation-delay: .08s; }
.bt:hover .mk-bar:nth-child(4)::before, .bt.is-live .mk-bar:nth-child(4)::before { animation-delay: .16s; }
.bt:hover .mk-bar:nth-child(5)::before, .bt.is-live .mk-bar:nth-child(5)::before { animation-delay: .24s; }
/* Connect: the hand-off happens */
@keyframes linkFlow { to { background-position: 0 16px; } }
.bt:hover .mk-link, .bt:focus-visible .mk-link, .bt.is-live .mk-link { animation: linkFlow .6s linear infinite; }
.mk-church .mk-pill:first-child { transition: box-shadow .3s; }
.bt:hover .mk-church .mk-pill:first-child, .bt.is-live .mk-church .mk-pill:first-child { box-shadow: 0 0 0 4px rgba(232,165,119,.45); }
/* Build: a blinking caret */
@keyframes caret { 50% { opacity: 0; } }
.mk-code code::after { content: ''; display: inline-block; width: 7px; height: 13px; margin-left: 2px; vertical-align: -2px; background: var(--peach); opacity: 0; }
.bt:hover .mk-code code::after, .dev-band:hover .mk-code code::after, .bt.is-live .mk-code code::after { opacity: 1; animation: caret 1s steps(1) infinite; }
/* Platform diagram: switches flick */
.dg-sw { transition: background-color .25s; } .dg-sw i { transition: right .25s cubic-bezier(.2,.8,.2,1); }
.dg-mod:hover .dg-sw, .dg-mod:focus-visible .dg-sw { background: var(--peach); }
.dg-mod:hover .dg-sw i, .dg-mod:focus-visible .dg-sw i { right: 17px; }
/* Compliance page tiles */
.cmx-mini { transition: transform .35s cubic-bezier(.2,.8,.2,1); }
.cmx-tile:hover .cmx-mini, .cmx-tile.is-live .cmx-mini { transform: translateY(-4px) scale(1.02); }
.cmx-card li.todo i { transition: all .35s; }
.cmx-card:hover li.todo i { background: var(--green); box-shadow: none; }
/* Solution rows */
.sl-row h3 { transition: transform .25s cubic-bezier(.2,.8,.2,1), color .2s; }
a.sl-row:hover h3, a.sl-row:focus-visible h3 { transform: translateX(4px); }
@media (prefers-reduced-motion: reduce) {
  .hero::before { animation: none; }
  .hero h1, .hero-side > * { animation: none; }
  .bt *, .bt *::before, .bt *::after, .dg-sw, .dg-sw i, .cmx-mini, .sl-row h3 { animation: none !important; transition: none !important; }
}
'''
