"""Home page: Australian horizon hero and the stories slider."""

HORIZON = '''<div class="oz-wrap">
<svg class="oz" viewBox="0 0 1440 440" preserveAspectRatio="xMidYMax slice" role="img" aria-label="Under the Southern Cross, two roads cross the Australian bush and meet at a small church with a lit door, as the sun rises">
  <defs>
    <linearGradient id="oz-sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1B4740" stop-opacity="0"/><stop offset=".5" stop-color="#2A5E52" stop-opacity=".55"/><stop offset="1" stop-color="#E8A577" stop-opacity=".5"/></linearGradient>
    <radialGradient id="oz-haze" cx=".66" cy=".7" r=".42"><stop offset="0" stop-color="#F3CFB3" stop-opacity=".6"/><stop offset="1" stop-color="#F3CFB3" stop-opacity="0"/></radialGradient>
    <symbol id="oz-star" viewBox="-10 -10 20 20"><path d="M0 -10 L2 -2 L10 0 L2 2 L0 10 L-2 2 L-10 0 L-2 -2Z" fill="#F8F3EA"/></symbol>
  </defs>
  <rect width="1440" height="440" fill="url(#oz-sky)"/>
  <rect width="1440" height="440" fill="url(#oz-haze)"/>
  <g class="oz-cross" transform="translate(330 40) scale(1.25)">
    <use class="oz-s s1" href="#oz-star" x="-7" y="-7" width="14" height="14"/>
    <use class="oz-s s2" href="#oz-star" x="-48" y="44" width="16" height="16"/>
    <use class="oz-s s3" href="#oz-star" x="47" y="34" width="12" height="12"/>
    <use class="oz-s s4" href="#oz-star" x="29" y="84" width="8" height="8"/>
    <use class="oz-s s5" href="#oz-star" x="2" y="118" width="18" height="18"/>
  </g>
  <circle class="oz-sun" cx="950" cy="262" r="96" fill="#E8A577"/>
  <path d="M0 292 C200 262 400 284 620 266 S1040 240 1440 262 V440 H0Z" fill="#8FB5A5" opacity=".5"/>
  <path class="oz-rock" d="M150 284 C160 262 186 254 230 252 C290 250 330 254 352 262 C364 268 372 278 378 286 Z" fill="#B9684A" opacity=".75"/>
  <path d="M0 326 C260 296 520 330 760 306 S1180 286 1440 308 V440 H0Z" fill="#2F6457"/>
  <path d="M0 376 C300 346 620 382 900 356 S1300 340 1440 350 V440 H0Z" fill="#1B4740"/>
  <g transform="translate(950 296)">
    <rect x="-40" y="0" width="80" height="62" fill="#F8F3EA"/>
    <path d="M-50 5 L0 -36 L50 5Z" fill="#14352F"/>
    <rect x="-9" y="-76" width="18" height="46" fill="#F8F3EA"/>
    <path d="M-15 -76 L0 -94 L15 -76Z" fill="#14352F"/>
    <rect x="-1.75" y="-120" width="3.5" height="26" fill="#F8F3EA"/><rect x="-9" y="-112" width="18" height="3.5" fill="#F8F3EA"/>
    <rect class="oz-door" x="-12" y="28" width="24" height="34" rx="12" fill="#E8A577"/>
  </g>
  <g fill="#14352F"><g transform="translate(1160 372) scale(1.15 1.15)"><path d="M-3 0 C-2 -22 -6 -40 -2 -58 C0 -66 -2 -74 2 -84 L6 -84 C4 -74 6 -66 4 -58 C2 -48 8 -30 5 0Z"/><path d="M0 -50 C-8 -60 -18 -66 -28 -70 L-27 -73 C-16 -70 -6 -64 2 -56Z"/><path d="M3 -64 C10 -72 18 -78 28 -80 L28 -77 C20 -74 12 -68 5 -60Z"/><ellipse cx="-32" cy="-78" rx="17" ry="9"/><ellipse cx="-20" cy="-86" rx="12" ry="7"/><ellipse cx="4" cy="-96" rx="18" ry="10"/><ellipse cx="20" cy="-90" rx="12" ry="7"/><ellipse cx="32" cy="-84" rx="15" ry="8"/></g><g transform="translate(1296 362) scale(-0.8 0.8)"><path d="M-3 0 C-2 -22 -6 -40 -2 -58 C0 -66 -2 -74 2 -84 L6 -84 C4 -74 6 -66 4 -58 C2 -48 8 -30 5 0Z"/><path d="M0 -50 C-8 -60 -18 -66 -28 -70 L-27 -73 C-16 -70 -6 -64 2 -56Z"/><path d="M3 -64 C10 -72 18 -78 28 -80 L28 -77 C20 -74 12 -68 5 -60Z"/><ellipse cx="-32" cy="-78" rx="17" ry="9"/><ellipse cx="-20" cy="-86" rx="12" ry="7"/><ellipse cx="4" cy="-96" rx="18" ry="10"/><ellipse cx="20" cy="-90" rx="12" ry="7"/><ellipse cx="32" cy="-84" rx="15" ry="8"/></g><g transform="translate(205 394) scale(-1.25 1.25)"><path d="M-3 0 C-2 -22 -6 -40 -2 -58 C0 -66 -2 -74 2 -84 L6 -84 C4 -74 6 -66 4 -58 C2 -48 8 -30 5 0Z"/><path d="M0 -50 C-8 -60 -18 -66 -28 -70 L-27 -73 C-16 -70 -6 -64 2 -56Z"/><path d="M3 -64 C10 -72 18 -78 28 -80 L28 -77 C20 -74 12 -68 5 -60Z"/><ellipse cx="-32" cy="-78" rx="17" ry="9"/><ellipse cx="-20" cy="-86" rx="12" ry="7"/><ellipse cx="4" cy="-96" rx="18" ry="10"/><ellipse cx="20" cy="-90" rx="12" ry="7"/><ellipse cx="32" cy="-84" rx="15" ry="8"/></g><g transform="translate(70 380) scale(0.7 0.7)"><path d="M-3 0 C-2 -22 -6 -40 -2 -58 C0 -66 -2 -74 2 -84 L6 -84 C4 -74 6 -66 4 -58 C2 -48 8 -30 5 0Z"/><path d="M0 -50 C-8 -60 -18 -66 -28 -70 L-27 -73 C-16 -70 -6 -64 2 -56Z"/><path d="M3 -64 C10 -72 18 -78 28 -80 L28 -77 C20 -74 12 -68 5 -60Z"/><ellipse cx="-32" cy="-78" rx="17" ry="9"/><ellipse cx="-20" cy="-86" rx="12" ry="7"/><ellipse cx="4" cy="-96" rx="18" ry="10"/><ellipse cx="20" cy="-90" rx="12" ry="7"/><ellipse cx="32" cy="-84" rx="15" ry="8"/></g></g>
  <path d="M0 418 C340 394 760 424 1080 404 S1380 394 1440 398 V440 H0Z" fill="#14352F"/>
  <path class="oz-road" d="M120 440 C290 404 510 380 710 374 S910 362 950 358" fill="none" stroke="#F8F3EA" stroke-width="9" stroke-linecap="round" opacity=".9"/>
  <path class="oz-road" d="M1380 440 C1250 414 1080 390 970 370" fill="none" stroke="#F8F3EA" stroke-width="9" stroke-linecap="round" opacity=".9"/>
</svg></div>'''

CSS = r'''
.hero .oz { display: block; width: 100%; height: clamp(240px, 30vw, 440px); margin-top: clamp(-40px, -2vw, 0px); }
.oz-wrap { overflow: hidden; }
@media (max-width: 640px) { .hero .oz { width: 170vw; height: auto; aspect-ratio: 1440 / 440; margin-left: -32vw; margin-top: 8px; } }
.oz-road { stroke-dasharray: 1300; stroke-dashoffset: 0; animation: ozRoad 2.4s cubic-bezier(.3,.6,.2,1) .4s both; }
.oz-sun { transform-box: fill-box; transform-origin: center; animation: ozSun 2s cubic-bezier(.2,.7,.2,1) both; }
.oz-door { animation: ozDoor 1.2s ease 2.4s both, ozGlow 4s ease-in-out 3.6s infinite; }
.oz-s { transform-box: fill-box; transform-origin: center; animation: ozIn .8s ease both, ozTwinkle 5s ease-in-out infinite; }
.oz-s.s1 { animation-delay: 1.2s, 2s; } .oz-s.s2 { animation-delay: 1.35s, 3.1s; } .oz-s.s3 { animation-delay: 1.5s, 2.6s; } .oz-s.s4 { animation-delay: 1.65s, 4s; } .oz-s.s5 { animation-delay: 1.8s, 2.3s; }
@keyframes ozRoad { from { stroke-dashoffset: 1300; } }
@keyframes ozSun { from { transform: translateY(70px); opacity: 0; } }
@keyframes ozDoor { from { opacity: 0; } }
@keyframes ozGlow { 50% { fill: #F3CFB3; } }
@keyframes ozIn { from { opacity: 0; transform: scale(.3); } }
@keyframes ozTwinkle { 0%, 100% { opacity: 1; } 50% { opacity: .55; } }
.hero .hero-split { align-items: start; }
.hero .hero-kick { display: inline-flex; align-items: center; gap: 10px; margin: 0 0 22px; font: 700 15px/1.2 var(--head); color: var(--peach); animation: heroUp .9s cubic-bezier(.2,.8,.2,1) both; }
.hero .hero-kick i { width: 8px; height: 8px; border-radius: 50%; background: var(--peach); box-shadow: 0 0 0 5px rgba(232,165,119,.18); }

.case { padding-top: clamp(72px, 8vw, 112px); }
.cs-track { grid-auto-columns: clamp(300px, 40vw, 540px); gap: 24px; margin-top: 44px; padding-bottom: 28px;
  -webkit-mask-image: linear-gradient(90deg, #000 0, #000 calc(100% - 140px), transparent);
          mask-image: linear-gradient(90deg, #000 0, #000 calc(100% - 140px), transparent); }
.cs-track.scrolled { -webkit-mask-image: linear-gradient(90deg, transparent, #000 140px, #000 calc(100% - 140px), transparent); mask-image: linear-gradient(90deg, transparent, #000 140px, #000 calc(100% - 140px), transparent); }
.cs-track.at-end { -webkit-mask-image: linear-gradient(90deg, transparent, #000 140px); mask-image: linear-gradient(90deg, transparent, #000 140px); }
.cs-tile { border-radius: 26px; box-shadow: 0 1px 0 rgba(27,71,64,.06), 0 24px 48px -32px rgba(10,30,26,.35); transition: transform .35s cubic-bezier(.2,.7,.2,1), box-shadow .35s ease; opacity: 0; transform: translateX(48px); }
.cs-tile.in { opacity: 1; transform: none; transition: opacity .8s cubic-bezier(.2,.7,.2,1), transform .8s cubic-bezier(.2,.7,.2,1), box-shadow .35s ease; }
.cs-tile.in:hover { transform: translateY(-4px); box-shadow: 0 1px 0 rgba(27,71,64,.06), 0 32px 60px -30px rgba(10,30,26,.45); }
.cs-img { aspect-ratio: 16 / 10; overflow: hidden; }
.cs-img img { transition: transform .8s cubic-bezier(.2,.7,.2,1); }
.cs-tile:hover .cs-img img { transform: scale(1.04); }
.cs-text { padding: 26px 28px 28px !important; }
.cs-text h3 { font-size: clamp(22px, 1.9vw, 27px) !important; line-height: 1.15; }
.cs-text p:not(.cs-name) { font-size: 16.5px; }
.cs-dots { display: flex; justify-content: center; gap: 8px; margin-top: 8px; }
.cs-dots button { width: 8px; height: 8px; min-width: 8px; padding: 0; border: 0; border-radius: 99px; background: rgba(27,71,64,.22); cursor: pointer; transition: width .3s ease, background .3s ease; }
.cs-dots button[aria-current="true"] { width: 26px; background: var(--green); }
.cs-dots button::after { content: ''; display: block; margin: -18px; width: 44px; height: 44px; }
@media (max-width: 640px) { .cs-track { grid-auto-columns: 84vw; -webkit-mask-image: none; mask-image: none; } }

@media (prefers-reduced-motion: reduce) {
  .oz-road, .oz-sun, .oz-door, .oz-s, .hero .hero-kick { animation: none !important; }
  .cs-tile, .cs-tile.in { opacity: 1; transform: none; transition: none; }
  .cs-img img { transition: none; } .cs-tile:hover .cs-img img { transform: none; }
}
'''

JS = r'''
(function () {
  const track = document.querySelector('.cs-track');
  if (!track) return;
  const tiles = [...track.querySelectorAll('.cs-tile')];
  const dots = document.createElement('div');
  dots.className = 'cs-dots';
  tiles.forEach((t, i) => {
    const b = document.createElement('button');
    b.type = 'button';
    b.setAttribute('aria-label', 'Story ' + (i + 1) + ' of ' + tiles.length);
    b.addEventListener('click', () => track.scrollTo({ left: t.offsetLeft - tiles[0].offsetLeft, behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' }));
    dots.appendChild(b);
  });
  track.after(dots);
  function sync() {
    const x = track.scrollLeft, max = track.scrollWidth - track.clientWidth;
    track.classList.toggle('scrolled', x > 8 && x < max - 8);
    track.classList.toggle('at-end', x >= max - 8 && max > 0);
    const w = (tiles[1]?.offsetLeft || 1) - tiles[0].offsetLeft;
    const n = x >= max - 8 ? tiles.length - 1 : Math.round(x / w);
    [...dots.children].forEach((d, i) => d.setAttribute('aria-current', i === n ? 'true' : 'false'));
  }
  track.addEventListener('scroll', () => requestAnimationFrame(sync), { passive: true });
  addEventListener('resize', sync); sync();
  if (!('IntersectionObserver' in window) || matchMedia('(prefers-reduced-motion: reduce)').matches) { tiles.forEach((t) => t.classList.add('in')); return; }
  const io = new IntersectionObserver((es) => es.forEach((e) => {
    if (!e.isIntersecting) return;
    io.unobserve(e.target);
    setTimeout(() => e.target.classList.add('in'), (tiles.indexOf(e.target) % 4) * 110);
  }), { threshold: 0.15 });
  tiles.forEach((t) => io.observe(t));
})();
'''
