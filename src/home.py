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

.case { background: var(--green); color: var(--cream); padding-top: clamp(80px, 9vw, 120px); padding-bottom: clamp(72px, 8vw, 110px); overflow: hidden; }
.case .tag { color: var(--peach); }
.case .sec-title { color: var(--cream); }
.case .cs-head .sv { color: var(--on-green); } .case .cs-head .sv cite { color: var(--peach); }
.case .cs-arrow { border-color: rgba(248,243,234,.35); color: var(--cream); }
.case .cs-arrow:hover, .case .cs-arrow:focus-visible { background: var(--cream); color: var(--green); }
.case .cs-arrow:disabled { background: transparent; color: var(--cream); }
.cs-track { grid-auto-columns: min(760px, 84vw); gap: 32px; margin-top: 48px; padding-top: 12px; padding-bottom: 12px; align-items: center; }
.cs-tile { position: relative; min-height: clamp(420px, 34vw, 470px); border-radius: 28px; overflow: hidden; background: var(--night); box-shadow: 0 40px 80px -40px rgba(0,0,0,.6);
  opacity: .42; transform: scale(.94); filter: saturate(.55); transition: opacity .6s cubic-bezier(.2,.7,.2,1), transform .6s cubic-bezier(.2,.7,.2,1), filter .6s ease; }
.cs-tile.active { opacity: 1; transform: none; filter: none; }
.cs-img { position: absolute; inset: 0; aspect-ratio: auto; }
.cs-img > img { width: 100%; height: 100%; object-fit: cover; transition: transform 1.2s cubic-bezier(.2,.7,.2,1); }
.cs-tile.active:hover .cs-img > img { transform: scale(1.03); }
.cs-img::after { content: ''; position: absolute; inset: 0; background: linear-gradient(90deg, rgba(16,44,40,.94) 0%, rgba(16,44,40,.78) 38%, rgba(16,44,40,.15) 75%, rgba(16,44,40,0) 100%), linear-gradient(0deg, rgba(16,44,40,.55), rgba(16,44,40,0) 45%); pointer-events: none; }
.cs-img.chai-tile { background: #fff; display: block; }
.cs-img.chai-tile > img { object-fit: contain; width: 46%; height: 100%; margin-left: 50%; }
.cs-text { position: relative; z-index: 2; display: flex; flex-direction: column; justify-content: center; align-items: flex-start; max-width: 460px; min-height: inherit; padding: clamp(28px, 4vw, 44px) !important; background: none; }
.cs-name { color: var(--peach) !important; font-size: 14px !important; }
.cs-name .cs-logo { border-radius: 6px; background: #fff; }
.cs-text h3 { margin-top: 12px !important; font-size: clamp(28px, 3vw, 40px) !important; line-height: 1.04 !important; letter-spacing: -0.03em !important; color: var(--cream) !important; text-wrap: balance; }
.cs-text > p:not(.cs-name) { margin-top: 16px !important; color: rgba(248,243,234,.85) !important; font-size: 16.5px !important; max-width: 40ch; }
.cs-more { margin-top: 26px !important; padding: 0 20px !important; min-height: 46px; display: inline-flex; align-items: center; gap: 10px; border-radius: 14px; background: var(--cream) !important; color: var(--green) !important; text-decoration: none !important; font: 700 15px/1 var(--head); transition: transform .2s ease, box-shadow .2s ease; }
.cs-more::after { content: ''; width: 14px; height: 14px; background: currentColor; -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M2 8h11M9 4l4 4-4 4' fill='none' stroke='black' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center / contain no-repeat; mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M2 8h11M9 4l4 4-4 4' fill='none' stroke='black' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center / contain no-repeat; transition: transform .2s ease; }
.cs-more:hover { transform: translateY(-1px); box-shadow: 0 10px 24px rgba(0,0,0,.25); } .cs-more:hover::after { transform: translateX(3px); }
.cs-polaroid { position: absolute; z-index: 3; right: 5%; bottom: 7%; width: 30%; margin: 0; padding: 8px 8px 0; background: #FFFDF8; border-radius: 10px; transform: rotate(4deg); box-shadow: 0 24px 40px -16px rgba(0,0,0,.55); transition: transform .5s cubic-bezier(.2,.7,.2,1); }
.cs-polaroid img { display: block; width: 100%; aspect-ratio: 4 / 3; object-fit: cover; border-radius: 6px; }
.cs-polaroid figcaption { padding: 8px 2px 10px; font-size: 12px; line-height: 1.3; color: var(--green); }
.cs-tile.active:hover .cs-polaroid { transform: rotate(1deg) translateY(-4px); }
.cs-foot { position: relative; display: flex; align-items: center; justify-content: space-between; gap: 24px; margin-top: 28px; }
.cs-bars { display: flex; gap: 8px; }
.cs-bars button { position: relative; width: 48px; height: 44px; padding: 0; border: 0; background: none; cursor: pointer; }
.cs-bars button::before { content: ''; position: absolute; left: 0; right: 0; top: 50%; height: 3px; margin-top: -1.5px; border-radius: 3px; background: rgba(248,243,234,.22); transition: background .3s ease; }
.cs-bars button[aria-current="true"]::before { background: var(--peach); }
.cs-count { position: absolute; left: 50%; transform: translateX(-50%); font: 700 14px/1 var(--head); letter-spacing: .04em; color: var(--cream); font-variant-numeric: tabular-nums; }
.cs-count span { color: rgba(248,243,234,.5); }
@media (max-width: 860px) { .cs-text { max-width: none; justify-content: flex-end; } .cs-img::after { background: linear-gradient(0deg, rgba(16,44,40,.95) 0%, rgba(16,44,40,.75) 50%, rgba(16,44,40,.1) 100%); } .cs-polaroid { width: 38%; top: 6%; bottom: auto; right: 6%; } .cs-img.chai-tile > img { width: 70%; height: 50%; margin: 0 auto; display: block; } .cs-count { position: static; transform: none; } }
@media (max-width: 640px) { .cs-bars { flex: 1; } .cs-bars button { flex: 1; width: auto; } .cs-count { display: none; } .cs-track { grid-auto-columns: 86vw; gap: 14px; } .cs-tile { min-height: 520px; } .cs-text h3 { font-size: 28px !important; } }

@media (prefers-reduced-motion: reduce) {
  .oz-road, .oz-sun, .oz-door, .oz-s, .hero .hero-kick { animation: none !important; }
  .cs-tile { transition: none; } .cs-img > img, .cs-polaroid { transition: none; }
  .cs-tile.active:hover .cs-img > img { transform: none; }
}
'''

JS = r'''
(function () {
  const track = document.querySelector('.cs-track');
  if (!track) return;
  const tiles = [...track.querySelectorAll('.cs-tile')];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const foot = document.createElement('div');
  foot.className = 'cs-foot';
  const bars = document.createElement('div'); bars.className = 'cs-bars';
  const count = document.createElement('p'); count.className = 'cs-count'; count.setAttribute('aria-live', 'polite');
  const pad = (n) => String(n).padStart(2, '0');
  const go = (i) => track.scrollTo({ left: tiles[i].offsetLeft - tiles[0].offsetLeft, behavior: reduce ? 'auto' : 'smooth' });
  tiles.forEach((t, i) => {
    const b = document.createElement('button');
    b.type = 'button'; b.setAttribute('aria-label', 'Story ' + (i + 1) + ' of ' + tiles.length);
    b.addEventListener('click', () => go(i));
    bars.appendChild(b);
    t.addEventListener('click', (e) => { if (!t.classList.contains('active') && !e.target.closest('a,button')) go(i); });
  });
  foot.append(bars, count);
  track.closest('.wrap') ? track.after(foot) : track.after(foot);
  const wrap = document.createElement('div'); wrap.className = 'wrap'; foot.replaceWith(wrap); wrap.appendChild(foot);
  function sync() {
    const x = track.scrollLeft, max = track.scrollWidth - track.clientWidth;
    const w = (tiles[1]?.offsetLeft || 1) - tiles[0].offsetLeft;
    const n = x >= max - 8 ? tiles.length - 1 : Math.round(x / w);
    tiles.forEach((t, i) => { t.classList.toggle('active', i === n); t.toggleAttribute('inert', false); });
    [...bars.children].forEach((d, i) => d.setAttribute('aria-current', i === n ? 'true' : 'false'));
    count.innerHTML = pad(n + 1) + ' <span>/ ' + pad(tiles.length) + '</span>';
  }
  track.addEventListener('scroll', () => requestAnimationFrame(sync), { passive: true });
  addEventListener('resize', sync); sync();
})();
'''

ABOUT_CSS = r'''
.ab-hero h1 { max-width: 14ch; }
.ab-hero { padding-bottom: 180px; }
.ab-photos { display: grid; grid-template-columns: 1.3fr 1fr 1fr; gap: 18px; margin-top: -120px; position: relative; z-index: 2; }
.ab-photos figure { margin: 0; border-radius: 24px; overflow: hidden; height: clamp(220px, 24vw, 320px); box-shadow: 0 30px 60px -30px rgba(10,30,26,.45); background: var(--night); }
.ab-photos figure:nth-child(2) { transform: translateY(28px); }
.ab-photos img { width: 100%; height: 100%; object-fit: cover; display: block; transition: transform 1s cubic-bezier(.2,.7,.2,1); }
.ab-photos figure:hover img { transform: scale(1.04); }
.ab-sec { padding-top: clamp(96px, 10vw, 140px); }
.ab-why { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(40px, 6vw, 96px); align-items: start; }
.ab-big { margin: 0; font: 400 clamp(30px, 3.4vw, 46px)/1.18 'Newsreader', Georgia, serif; color: var(--green); letter-spacing: -0.01em; }
.ab-why p:not(.ab-big):not(.tag) { margin: 0 0 18px; font-size: 18.5px; line-height: 1.65; color: var(--soft); }
.ab-help { display: grid; grid-template-columns: 1fr 1.1fr; gap: clamp(40px, 6vw, 96px); margin-top: clamp(80px, 9vw, 128px); padding-top: clamp(56px, 6vw, 80px); border-top: 1px solid var(--line); align-items: start; }
.ab-h { margin: 0; font-size: clamp(32px, 3.6vw, 48px); letter-spacing: -0.035em; color: var(--green); line-height: 1.05; }
.ab-lede { margin: 18px 0 28px; font-size: 18.5px; color: var(--soft); }
.ab-mods { list-style: none; margin: 0; padding: 0; }
.ab-mods a { display: grid; grid-template-columns: 1fr auto; grid-template-rows: auto auto; column-gap: 20px; align-items: center; padding: 22px 4px; border-bottom: 1px solid var(--line); color: inherit; text-decoration: none; transition: padding .3s cubic-bezier(.2,.7,.2,1), background .3s ease; }
.ab-mods li:first-child a { border-top: 1px solid var(--line); }
.ab-mods span { font: 700 13.5px/1.2 var(--head); color: var(--clay); }
.ab-mods b { grid-row: 2; font: 800 clamp(22px, 2.2vw, 28px)/1.15 var(--head); letter-spacing: -0.02em; color: var(--green); }
.ab-mods i { grid-row: 1 / 3; grid-column: 2; width: 40px; height: 40px; border-radius: 50%; border: 1.5px solid rgba(27,71,64,.22); position: relative; transition: background .25s ease, border-color .25s ease, transform .3s ease; }
.ab-mods i::after { content: ''; position: absolute; inset: 0; margin: auto; width: 14px; height: 14px; background: var(--green); -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M2 8h11M9 4l4 4-4 4' fill='none' stroke='black' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center / contain no-repeat; mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 16 16'%3E%3Cpath d='M2 8h11M9 4l4 4-4 4' fill='none' stroke='black' stroke-width='1.8' stroke-linecap='round' stroke-linejoin='round'/%3E%3C/svg%3E") center / contain no-repeat; }
.ab-mods a:hover, .ab-mods a:focus-visible { padding-left: 14px; }
.ab-mods a:hover i, .ab-mods a:focus-visible i { background: var(--green); border-color: var(--green); }
.ab-mods a:hover i::after, .ab-mods a:focus-visible i::after { background: var(--cream); }
.ab-band { background: var(--sage); }
.ab-three { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: clamp(28px, 4vw, 56px); }
.ab-three > div { padding-top: 22px; border-top: 2px solid var(--green); }
.ab-k { margin: 0 0 14px; font: 700 14px/1.2 var(--head); color: var(--clay); }
.ab-verse { margin: 0 0 12px !important; font: 400 clamp(26px, 2.6vw, 34px)/1.2 'Newsreader', Georgia, serif !important; color: var(--green) !important; }
.ab-three p:not(.ab-k) { margin: 0 0 12px; font-size: 17px; line-height: 1.6; color: var(--ink); }
@media (max-width: 900px) { .ab-why, .ab-help, .ab-three { grid-template-columns: minmax(0, 1fr); } .ab-photos { grid-template-columns: 1fr 1fr; } .ab-photos figure:first-child { grid-column: 1 / -1; } .ab-photos figure:nth-child(2) { transform: none; } }
@media (prefers-reduced-motion: reduce) { .ab-photos img, .ab-mods a, .ab-mods i { transition: none; } .ab-photos figure:hover img { transform: none; } }
'''

SEAM_CSS = r'''
#page-home .hero::after, .page .hero::after { left: 0; right: 0; bottom: 0; top: auto; width: auto; height: 160px; max-width: none; max-height: none; border-radius: 0; background: linear-gradient(180deg, rgba(27,71,64,0), var(--green)); z-index: 1; }
#page-home .hero > .wrap { position: relative; z-index: 3; }
.hero { padding-bottom: clamp(72px, 8vw, 112px) !important; }
.case { padding-top: clamp(40px, 5vw, 72px) !important; }
'''

MENU_CSS = r'''
@media (min-width: 861px) {
  .dd-sol { width: min(880px, 94vw); }
  .dd-sol-main { display: grid; gap: 10px; align-content: start; padding: 8px; }
  .dd-sol .dd-list { grid-template-columns: 1fr 1fr; gap: 10px; padding: 0; }
  .dd-sol .dd-list a { flex-direction: column; gap: 14px !important; min-height: 128px; padding: 18px !important; border-radius: 18px !important; background: var(--sage); transition: transform .25s cubic-bezier(.2,.7,.2,1), background .25s ease, box-shadow .25s ease; }
  .dd-sol .dd-list a:hover, .dd-sol .dd-list a:focus-visible { transform: translateY(-2px); background: #DCEBE2; box-shadow: 0 16px 30px -22px rgba(10,30,26,.45); }
  .dd-sol .dd-list .dd-ic { width: 40px; height: 40px; border-radius: 12px; background: #FFFDF8; }
  .dd-sol .dd-list .dd-tx b { font-size: 17px; }
  .dd-sol-foot { display: flex !important; justify-content: space-between; align-items: center; gap: 12px; padding: 12px 16px !important; margin: 0 !important; border-radius: 14px; font-size: 14.5px; color: var(--soft) !important; }
  .dd-sol-foot b { color: var(--green); font-weight: 700; }
  .dd-sol-foot b::after { content: ' \2192'; }
  .dd-sol-foot:hover { background: rgba(27,71,64,.05); }
  .dd-layout-sol { grid-template-columns: minmax(0, 1fr) 260px; }
  .dd-story .dd-story-img { display: block !important; height: 120px; margin: -8px -8px 6px; border-radius: 14px; background: url(img/sydneyfire-street.webp) center / cover; filter: grayscale(.2); transition: transform .5s cubic-bezier(.2,.7,.2,1); }
  .dd-story:hover .dd-story-img { transform: scale(1.02); }
}
@media (max-width: 860px) { .dd-sol-foot, .dd-story-img { display: none !important; } }
@media (prefers-reduced-motion: reduce) { .dd-sol .dd-list a { transition: none; } .dd-sol .dd-list a:hover { transform: none; } }
'''
