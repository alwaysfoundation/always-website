"""Header scroll state and site-wide motion. Loaded after polish so it wins. Everything stops under reduced motion."""

CSS = r'''
header { position: fixed; inset: 0 0 auto 0; z-index: 30; transition: transform .35s cubic-bezier(.2,.7,.2,1); }
header::before { content: ''; position: absolute; inset: 0; z-index: -1; background: rgba(20,54,49,.82); backdrop-filter: blur(14px) saturate(140%); -webkit-backdrop-filter: blur(14px) saturate(140%); box-shadow: 0 1px 0 rgba(248,243,234,.08), 0 12px 32px rgba(10,30,27,.22); opacity: 0; transition: opacity .3s ease; pointer-events: none; }
header .bar { transition: height .3s cubic-bezier(.2,.7,.2,1); }
header .brand svg.wm { transition: height .3s cubic-bezier(.2,.7,.2,1); }
header.scrolled::before { opacity: 1; }
header.scrolled .bar { height: 72px; }
header.scrolled .brand svg.wm { height: 28px; }
header.tuck:not(.open):not(.dd-open) { transform: translateY(-100%); }
header .hd-progress { position: absolute; left: 0; bottom: 0; height: 2px; width: 100%; background: var(--peach); transform-origin: 0 50%; transform: scaleX(var(--p, 0)); opacity: 0; transition: opacity .3s ease; }
header.scrolled .hd-progress { opacity: .9; }

@media (min-width: 861px) {
  header nav > ul > li > a, header nav > ul > li > .dd-btn { position: relative; }
  header nav > ul > li > a::after, header nav > ul > li > .dd-btn::after { content: ''; position: absolute; left: 0; right: 0; bottom: -8px; height: 2px; border-radius: 2px; background: var(--peach); transform: scaleX(0); transform-origin: 0 50%; transition: transform .28s cubic-bezier(.2,.7,.2,1); }
  header nav > ul > li > a:hover::after, header nav > ul > li > .dd-btn:hover::after, header nav > ul > li > a[aria-current="page"]::after, header nav > ul > li > .dd-btn[aria-expanded="true"]::after { transform: scaleX(1); }
  header nav > ul > li > a[aria-current="page"] { text-decoration: none; }
}
@media (max-width: 860px) { header.scrolled .bar { height: 68px; } }

.bar > .btn-peach { position: relative; overflow: hidden; transition: transform .2s ease, box-shadow .2s ease, background .2s ease; }
.bar > .btn-peach::after { content: ''; position: absolute; inset: 0; background: linear-gradient(110deg, transparent 30%, rgba(255,255,255,.35) 50%, transparent 70%); transform: translateX(-120%); }
.bar > .btn-peach:hover { transform: translateY(-1px); box-shadow: 0 8px 22px rgba(232,160,112,.32); }
.bar > .btn-peach:hover::after { transform: translateX(120%); transition: transform .7s ease; }

.page:not([hidden]) { animation: pageIn .45s cubic-bezier(.2,.7,.2,1) both; }
@keyframes pageIn { from { opacity: 0; transform: translateY(8px); } }

.rv { opacity: 0; transform: translateY(18px); transition: opacity .7s cubic-bezier(.2,.7,.2,1), transform .7s cubic-bezier(.2,.7,.2,1); }
.rv.in { opacity: 1; transform: none; }

.btn { transition: transform .2s ease, box-shadow .2s ease, background .2s ease, color .2s ease; }
.btn:hover { transform: translateY(-1px); }
.btn:active { transform: translateY(0) scale(.98); }

.page-hero .mk { animation: mkFloat 7s ease-in-out infinite; }
@keyframes mkFloat { 50% { transform: translateY(-6px); } }

.prose h2 { scroll-margin-top: 96px; }
.prose a { background-image: linear-gradient(currentColor, currentColor); background-size: 0 1px; background-repeat: no-repeat; background-position: 0 100%; transition: background-size .25s ease; }
.prose a:hover { background-size: 100% 1px; }

[data-count] { font-variant-numeric: tabular-nums; }

@media (prefers-reduced-motion: reduce) {
  header, header::before, header .bar, header .brand svg.wm, .bar > .btn-peach, .btn, .rv, .prose a { transition: none !important; }
  header.tuck:not(.open) { transform: none; }
  header .hd-progress { display: none; }
  .page:not([hidden]), .page-hero .mk { animation: none !important; }
  .rv { opacity: 1; transform: none; }
  .bar > .btn-peach::after { display: none; }
  .btn:hover, .btn:active { transform: none; }
}
'''

JS = r'''
(function () {
  const h = document.querySelector('header');
  if (!h) return;
  const bar = document.createElement('i');
  bar.className = 'hd-progress'; bar.setAttribute('aria-hidden', 'true');
  h.appendChild(bar);
  let last = scrollY, ticking = false;
  function update() {
    const y = scrollY, max = document.documentElement.scrollHeight - innerHeight;
    h.classList.toggle('scrolled', y > 24);
    h.classList.toggle('dd-open', !!h.querySelector('.dd-btn[aria-expanded="true"]'));
    if (y > 480 && y > last + 4) h.classList.add('tuck');
    else if (y < last - 4 || y < 480) h.classList.remove('tuck');
    h.style.setProperty('--p', max > 0 ? Math.min(1, y / max).toFixed(4) : 0);
    last = y; ticking = false;
  }
  addEventListener('scroll', () => { if (!ticking) { ticking = true; requestAnimationFrame(update); } }, { passive: true });
  addEventListener('hashchange', () => { h.classList.remove('tuck'); requestAnimationFrame(update); });
  h.addEventListener('focusin', () => h.classList.remove('tuck'));
  update();

  if (matchMedia('(prefers-reduced-motion: reduce)').matches || !('IntersectionObserver' in window)) return;
  const fmt = new Intl.NumberFormat('en-AU');
  const io = new IntersectionObserver((es) => es.forEach((e) => {
    if (!e.isIntersecting) return;
    io.unobserve(e.target);
    const el = e.target, end = +el.dataset.count, t0 = performance.now(), d = 1100;
    (function step(t) {
      const k = Math.min(1, (t - t0) / d), v = Math.round(end * (1 - Math.pow(1 - k, 3)));
      el.textContent = fmt.format(v);
      if (k < 1) requestAnimationFrame(step);
    })(t0);
  }), { threshold: 0.6 });
  function arm(root) {
    root.querySelectorAll('.doc-table td, [data-count]').forEach((el) => {
      if (el.dataset.armed) return;
      const n = el.dataset.count || el.textContent.trim().replace(/,/g, '');
      if (!/^\d{2,7}$/.test(n)) return;
      el.dataset.armed = '1'; el.dataset.count = n; el.textContent = '0'; io.observe(el);
    });
  }
  arm(document);
  new MutationObserver(() => arm(document.getElementById('doc') || document)).observe(document.getElementById('doc') || document.body, { childList: true });
})();
'''
