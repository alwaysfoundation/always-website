import os
ROOT = os.path.dirname(os.path.abspath(__file__))
"""Home page upgrades: the connected map and the auto-playing 'Watch it work' flow."""
import json, random

L = json.load(open(os.path.join(ROOT, 'paths.json')))
MAP = open(os.path.join(ROOT, 'map.json')).read()

def wm(color, h):
    return f'<svg width="{round(h*1328/366)}" height="{h}" viewBox="186 250 1328 366" role="img" aria-label="Always"><path fill="{color}" fill-rule="evenodd" d="{"".join(L["word"])}"/><path fill="#EE8B54" d="{"".join(L["cross"])}"/></svg>'

def qr(size=150):
    random.seed(7); n = 25; c = size / n
    out = f'<svg width="{size}" height="{size}" viewBox="0 0 {size} {size}" role="img" aria-label="QR code">'
    f = lambda x, y: f'<rect x="{x*c}" y="{y*c}" width="{7*c}" height="{7*c}" fill="#1E2A26"/><rect x="{(x+1)*c}" y="{(y+1)*c}" width="{5*c}" height="{5*c}" fill="#fff"/><rect x="{(x+2)*c}" y="{(y+2)*c}" width="{3*c}" height="{3*c}" fill="#1E2A26"/>'
    for i in range(n):
        for j in range(n):
            if (i < 8 and j < 8) or (i < 8 and j > n-9) or (i > n-9 and j < 8): continue
            if random.random() < .48: out += f'<rect x="{j*c:.1f}" y="{i*c:.1f}" width="{c:.1f}" height="{c:.1f}" fill="#1E2A26"/>'
    return out + f(0, 0) + f(n-7, 0) + f(0, n-7) + '</svg>'

states = [('NSW', 1406), ('VIC', 869), ('QLD', 597), ('WA', 382), ('SA', 285), ('TAS', 156), ('ACT', 63), ('NT', 39)]
bars = ''.join(f'<div class="sb"><span>{s}</span><span class="sb-t"><i data-w="{n/1406*100:.1f}%"></i></span><b>{n:,}</b></div>' for s, n in states)

MAP_SECTION = f'''<section class="sec live-map" id="map">
  <div class="wrap lm-grid">
    <div class="lm-copy">
      <p class="lm-k rv">We've mapped the churches</p>
      <p class="lm-n rv" id="lm-n">3,937</p>
      <p class="lm-lead rv">evangelical and Pentecostal churches and ministries, in every state and territory. When someone responds to Jesus, a church or ministry near them can welcome them.</p>
      <div class="lm-bars rv" id="lm-bars">{bars}</div>
      <a class="btn btn-peach rv" href="#/directory">Search the directory</a>
    </div>
    <div class="lm-mapwrap rv">
      <svg id="lm-map" viewBox="-20 -20 964 788" role="img" aria-label="Map of Australia: responses connecting to churches nearby"></svg>
      <div class="lm-count"><span><b id="lm-r">0</b> responses</span><span><b id="lm-c" class="pe">0</b> introduced nearby</span></div>
      <p class="lm-note">Illustration. The dots show where churches are.</p>
    </div>
  </div>
</section>'''

FLOW_SECTION = f'''<section class="sec watch" id="watch">
  <div class="wrap">
    <div class="w-head">
      <div><p class="lm-k rv">Watch it work</p><h2 class="sec-title rv" id="w-cap">Sam scans the QR at a concert.</h2></div>
      <div class="w-ctl rv"><button class="btn btn-peach" id="w-play" type="button">Pause</button><button class="btn w-ghost" id="w-again" type="button">Start again</button></div>
    </div>
    <div class="w-panes rv">
      <div class="w-pane"><p class="w-lab">Sam's phone</p><div class="w-phone" id="wp-a"><div class="w-screen" id="wa"></div></div></div>
      <div class="w-pane"><p class="w-lab">The church's inbox</p><div class="w-phone" id="wp-b"><div class="w-screen" id="wb"></div></div></div>
      <div class="w-pane w-pane-c"><p class="w-lab">The event ministry's results</p><div class="w-card" id="wc"></div></div>
    </div>
    <div class="w-steps" id="w-steps"></div>
    <p class="w-fine">Sam, Hope Church and City worship night are examples.</p>
  </div>
</section>'''

CSS = '''
/* live map */
.live-map { background: var(--night, #1E2A26); color: var(--cream); }
.lm-grid { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.25fr); gap: 56px; align-items: center; }
.lm-k { font: 700 18px/1.2 var(--head); color: var(--peach); margin: 0 0 14px; }
.lm-n { font: 800 clamp(84px, 11vw, 168px)/0.9 var(--head); letter-spacing: -0.06em; margin: 0; }
.lm-lead { margin-top: 18px; font-size: 19px; line-height: 1.55; color: var(--on-green, #CFE0D6); max-width: 520px; }
.lm-bars { margin: 28px 0 30px; display: grid; gap: 10px; max-width: 520px; }
.sb { display: grid; grid-template-columns: 52px 1fr 64px; gap: 14px; align-items: center; font: 700 15px var(--head); }
.sb b { text-align: right; }
.sb-t { height: 10px; border-radius: 999px; background: rgba(248,243,234,.12); overflow: hidden; }
.sb-t i { display: block; height: 100%; width: 0; border-radius: 999px; background: var(--peach); transition: width 1.4s cubic-bezier(.2,.7,.2,1); }
.lm-mapwrap { position: relative; }
#lm-map { width: 100%; height: auto; display: block; }
.lm-count { display: flex; gap: 28px; font-size: 15px; color: var(--on-green, #CFE0D6); margin-top: 6px; }
.lm-count b { font: 800 32px var(--head); color: var(--cream); margin-right: 6px; }
.lm-count b.pe { color: var(--peach); }
.lm-note { font-size: 12.5px; opacity: .6; margin-top: 8px; }
@keyframes lmfade { 0% { opacity: 0 } 15% { opacity: 1 } 70% { opacity: 1 } 100% { opacity: 0 } }
@keyframes lmpop { from { opacity: 0; transform: scale(.4) } to { opacity: 1; transform: none } }
/* watch it work */
.watch { background: var(--g, #1B4740); color: var(--cream); }
.w-head { display: flex; justify-content: space-between; align-items: flex-end; gap: 24px; flex-wrap: wrap; }
.w-head .sec-title { color: var(--cream); min-height: 2.1em; font-size: clamp(34px, 4.2vw, 56px); max-width: 820px; }
.w-ctl { display: flex; gap: 10px; }
.w-ghost { background: transparent; border: 2px solid rgba(248,243,234,.5); color: var(--cream); }
.w-panes { display: grid; grid-template-columns: 300px 300px minmax(0, 1fr); gap: 32px; margin-top: 36px; align-items: start; }
.w-lab { font: 700 14px var(--head); color: var(--on-green, #CFE0D6); margin: 0 0 10px; }
.w-phone { height: 540px; border-radius: 44px; background: #0d1412; padding: 10px; transition: box-shadow .4s; }
.w-phone.on, .w-card.on { box-shadow: 0 0 0 4px var(--peach); }
.w-screen { height: 100%; border-radius: 35px; background: var(--cream); color: var(--ink); padding: 34px 18px 18px; display: flex; flex-direction: column; gap: 10px; overflow: hidden; }
.w-card { min-height: 540px; background: var(--paper); color: var(--ink); border-radius: 26px; padding: 26px; display: flex; flex-direction: column; gap: 12px; transition: box-shadow .4s; }
.w-opt { display: flex; align-items: center; gap: 10px; min-height: 46px; padding: 0 14px; border-radius: 13px; border: 1px solid var(--line); background: var(--paper); font-size: 14.5px; font-weight: 500; }
.w-opt i { width: 16px; height: 16px; border-radius: 999px; border: 2px solid #CFC3AE; flex: none; }
.w-opt.sel { background: var(--g, #1B4740); color: var(--cream); border-color: var(--g, #1B4740); }
.w-opt.sel i { background: var(--peach); border-color: var(--peach); }
.w-field { min-height: 42px; border-radius: 11px; border: 1px solid var(--line); background: var(--paper); padding: 0 12px; display: flex; align-items: center; font-size: 14.5px; }
.w-btn { min-height: 46px; border-radius: 13px; display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 15px; background: var(--g, #1B4740); color: var(--cream); }
.w-btn.pe { background: var(--peach); color: var(--ink); }
.w-btn.ln { background: transparent; border: 2px solid var(--g, #1B4740); color: var(--g, #1B4740); }
.w-bub { max-width: 86%; padding: 10px 13px; border-radius: 18px; font-size: 13.5px; line-height: 1.45; animation: wpop .5s ease both; }
.w-bub.in { background: var(--paper); align-self: flex-start; border-bottom-left-radius: 6px; }
.w-bub.out { background: var(--g, #1B4740); color: var(--cream); align-self: flex-end; border-bottom-right-radius: 6px; }
.w-badge { font: 700 12px var(--head); padding: 5px 9px; border-radius: 8px; }
.w-kpi { background: var(--cream); border-radius: 14px; padding: 14px 16px; }
.w-kpi b { display: block; font: 800 30px var(--head); letter-spacing: -0.03em; }
.w-kpi span { font-size: 13px; color: var(--soft); }
.w-anim { animation: wpop .5s ease both; }
@keyframes wpop { from { opacity: 0; transform: translateY(10px) } to { opacity: 1; transform: none } }
.w-steps { display: grid; grid-template-columns: repeat(6, 1fr); gap: 12px; margin-top: 26px; }
.w-step { border: 0; background: none; color: inherit; text-align: left; padding: 0; opacity: .45; display: flex; flex-direction: column; gap: 8px; font: 700 14px/1.3 var(--head); cursor: pointer; }
.w-step .t { height: 5px; border-radius: 5px; background: rgba(248,243,234,.18); overflow: hidden; }
.w-step .t i { display: block; height: 100%; width: 0; background: var(--peach); }
.w-step.done { opacity: .8 } .w-step.done .t i { width: 100% }
.w-step.now { opacity: 1 } .w-step.now .t i { animation: wgrow 3.6s linear forwards }
@keyframes wgrow { from { width: 0 } to { width: 100% } }
.w-fine { margin-top: 18px; font-size: 12.5px; opacity: .6; }
@media (max-width: 1020px) {
  .lm-grid { grid-template-columns: 1fr; }
  .w-panes { grid-template-columns: 1fr 1fr; }
  .w-pane-c { grid-column: 1 / -1; }
  .w-card { min-height: 0; }
  .w-steps { grid-template-columns: repeat(3, 1fr); }
}
@media (max-width: 640px) {
  .w-panes { grid-template-columns: 1fr; }
  .w-pane:nth-child(2) { display: none; }
  .w-phone { height: 500px; max-width: 320px; }
  .w-steps { grid-template-columns: repeat(2, 1fr); }
  .lm-count { flex-direction: column; gap: 4px; }
}
@media (prefers-reduced-motion: reduce) { .w-step.now .t i { animation: none; width: 100%; } }
'''

JS = r'''
// ---------- live map
(() => {
  const MAP = __MAP__;
  const NS = 'http://www.w3.org/2000/svg';
  const mk = (t, a, p) => { const e = document.createElementNS(NS, t); for (const k in a) e.setAttribute(k, a[k]); p && p.appendChild(e); return e; };
  const svg = document.getElementById('lm-map'); if (!svg) return;
  mk('path', { d: MAP.outline, fill: '#26342F', stroke: '#3A4A44', 'stroke-width': 2 }, svg);
  const g = mk('g', {}, svg); MAP.churches.forEach(c => mk('circle', { cx: c[0], cy: c[1], r: 2.6, fill: '#DDE9E0', opacity: .5 }, g));
  const lay = mk('g', {}, svg);
  const R = document.getElementById('lm-r'), C = document.getElementById('lm-c');
  let timer = null, nr = 0;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  function tick() {
    const c = MAP.churches[Math.floor(Math.random() * MAP.churches.length)];
    const x = c[0] + (Math.random() * 36 - 18), y = c[1] + (Math.random() * 36 - 18);
    let best = c, bd = 1e9; for (const k of MAP.churches) { const d = (k[0] - x) ** 2 + (k[1] - y) ** 2; if (d < bd && d > 4) { bd = d; best = k; } }
    const p = mk('circle', { cx: x, cy: y, r: 5, fill: '#E8A577' }, lay); p.style.animation = 'lmpop .4s both'; p.style.transformOrigin = `${x}px ${y}px`;
    nr++; R.textContent = nr.toLocaleString('en-AU');
    setTimeout(() => {
      const l = mk('line', { x1: x, y1: y, x2: best[0], y2: best[1], stroke: '#E8A577', 'stroke-width': 2.5 }, lay);
      const h = mk('circle', { cx: best[0], cy: best[1], r: 6, fill: '#EE8B54' }, lay);
      C.textContent = nr.toLocaleString('en-AU');
      setTimeout(() => [p, l, h].forEach(e => { e.style.transition = 'opacity 1s'; e.style.opacity = .2; }), 1600);
      setTimeout(() => [p, l, h].forEach(e => e.remove()), 5000);
    }, 700);
  }
  const io = new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting) {
      document.querySelectorAll('#lm-bars i').forEach(i => i.style.width = i.dataset.w);
      if (!timer && !reduce) timer = setInterval(tick, 380);
    } else { clearInterval(timer); timer = null; }
  }), { threshold: .25 });
  io.observe(svg);
})();

// ---------- watch it work
(() => {
  const root = document.getElementById('watch'); if (!root) return;
  const QR = `__QR__`, WM = `__WM__`;
  const S = [
    { t: 'Sam scans the QR at a concert.', s: 'Sam scans the QR', on: 'a',
      a: `<p style="font:800 19px var(--head);text-align:center;margin-top:18px">Said yes to Jesus tonight?</p><p style="text-align:center;font-size:13.5px;color:var(--soft)">Scan to take your next step</p><div style="align-self:center;background:#fff;border-radius:18px;padding:12px;margin-top:6px">${QR}</div>`, b: 'idle', c: [127, 118, 61] },
    { t: 'He chooses a next step.', s: 'Chooses a next step', on: 'a',
      a: `<div>${WM}</div><p style="font:400 24px/1.12 var(--serif,Georgia)">We're so glad you said yes.</p><div class="w-opt sel w-anim"><i></i>Find a church near me</div><div class="w-opt"><i></i>Talk with someone</div><div class="w-opt"><i></i>Explore faith first</div>`, b: 'idle', c: [128, 118, 61] },
    { t: 'He says yes to sharing his details.', s: 'Says yes to sharing', on: 'a',
      a: `<div>${WM}</div><div style="display:flex;gap:8px;margin-top:6px"><div class="w-field" style="flex:1">Sam</div><div class="w-field" style="flex:1.3">Parramatta</div></div><div class="w-field">04•• ••• •••</div><div class="w-anim" style="display:flex;gap:10px;font-size:13px;line-height:1.45;background:var(--sage);padding:12px;border-radius:12px"><span style="width:20px;height:20px;border-radius:6px;background:#1B4740;color:#fff;display:flex;align-items:center;justify-content:center;font-size:12px;flex:none">✓</span>I'm happy for a church near me to get in touch.</div><div class="w-btn w-anim">Send</div>`, b: 'idle', c: [128, 118, 61] },
    { t: 'A church near Sam is introduced.', s: 'A church nearby is introduced', on: 'b',
      a: `<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:14px;background:#1B4740;color:#F8F3EA;margin:-34px -18px -18px;padding:26px"><div style="width:52px;height:52px;border-radius:999px;background:#E8A577;color:#1E2A26;display:flex;align-items:center;justify-content:center;font-size:24px">✓</div><p style="font:400 28px/1.1 var(--serif,Georgia)">You won't walk alone, Sam.</p><p style="font-size:14px;color:#CFE0D6">A church near Parramatta will be in touch.</p></div>`, b: 'alert', c: [128, 119, 61] },
    { t: 'The church accepts and texts Sam.', s: 'The church accepts and texts', on: 'b',
      a: `<p style="font:700 13px var(--head);color:var(--soft);text-align:center">Messages</p><div style="flex:1;display:flex;flex-direction:column;justify-content:flex-end;gap:10px"><div class="w-bub in">Hi Sam, it's Jo from Hope Church. So glad you reached out. Want to come along on Sunday? I'll meet you out the front.</div><div class="w-bub out" style="animation-delay:1s">That would be great, thanks Jo</div></div>`, b: 'accept', c: [128, 119, 61] },
    { t: 'Sam says he\'s connected. Everyone sees the fruit.', s: 'Sam says he\'s connected', on: 'c',
      a: `<p style="font:700 13px var(--head);color:var(--soft);text-align:center">Messages</p><div style="flex:1;display:flex;flex-direction:column;justify-content:flex-end;gap:10px"><div class="w-bub in">Always: Are you connected with Hope Church? Reply YES or tap the link.</div><div class="w-bub out" style="animation-delay:.8s">YES</div></div>`, b: 'done', c: [128, 119, 62] }];
  const B = {
    idle: `<p style="font:700 13px var(--head);color:var(--clay)">Inbox</p><div style="flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:10px;color:var(--soft)"><span style="width:50px;height:50px;border-radius:999px;background:var(--sage)"></span><p style="font-size:14.5px">No new introductions</p></div>`,
    alert: `<p style="font:700 13px var(--head);color:var(--clay)">Inbox</p><div class="w-anim" style="background:var(--paper);border:2px solid var(--peach);border-radius:18px;padding:16px;display:flex;flex-direction:column;gap:10px"><div style="display:flex;justify-content:space-between;align-items:center"><b style="font:800 19px var(--head)">Sam</b><span class="w-badge" style="background:#FDF0D9;color:#7A4B07">New</span></div><p style="font-size:14px;color:var(--soft)">Parramatta · Find a church</p><div class="w-field">04•• ••• •••</div><div style="display:flex;gap:8px"><div class="w-btn" style="flex:1">Accept</div><div class="w-btn ln" style="flex:1">Pass</div></div></div>`,
    accept: `<p style="font:700 13px var(--head);color:var(--clay)">Inbox</p><div style="background:var(--paper);border-radius:18px;padding:16px;display:flex;flex-direction:column;gap:10px"><div style="display:flex;justify-content:space-between;align-items:center"><b style="font:800 19px var(--head)">Sam</b><span class="w-badge" style="background:var(--sage);color:#1B4740">Accepted</span></div><p style="font-size:14px;color:var(--soft)">Parramatta · Find a church</p><div class="w-field w-anim" style="background:var(--sage);font-weight:600">0400 000 000</div><div class="w-btn pe w-anim" style="animation-delay:.7s">✓ Texted Sam</div></div>`,
    done: `<p style="font:700 13px var(--head);color:var(--clay)">Walking with</p><div class="w-anim" style="background:#1B4740;color:#F8F3EA;border-radius:18px;padding:20px;display:flex;flex-direction:column;gap:8px"><b style="font:800 20px var(--head)">Sam is connected</b><p style="font-size:14px;color:#CFE0D6">He confirmed it himself. Keep walking with him.</p></div>`};
  const C = c => `<div style="display:flex;justify-content:space-between;align-items:center"><b style="font:800 21px var(--head)">City worship night</b><span class="w-badge" style="background:#FDF0D9;color:#7A4B07">Live</span></div>${[['Responded tonight', c[0]], ['Introduced nearby', c[1]], ['Connected so far', c[2]]].map((k, i) => `<div class="w-kpi"><b style="${i === 2 ? 'color:#A4562A' : ''}">${k[1]}</b><span>${k[0]}</span></div>`).join('')}<p style="font-size:13px;color:var(--soft)">Totals only. A person's details go only to the church that welcomes them.</p>`;
  const steps = document.getElementById('w-steps');
  steps.innerHTML = S.map((s, i) => `<button class="w-step" type="button" data-i="${i}"><span class="t"><i></i></span>${i + 1}. ${s.s}</button>`).join('');
  let i = 0, t = null, play = true, started = false;
  const btn = document.getElementById('w-play');
  function show(n) {
    i = n; const s = S[n];
    document.getElementById('w-cap').textContent = s.t; document.getElementById('wa').innerHTML = s.a; document.getElementById('wb').innerHTML = B[s.b]; document.getElementById('wc').innerHTML = C(s.c);
    const st = [...steps.children]; st.forEach((b, k) => { b.classList.remove('now'); b.classList.toggle('done', k < n); }); void steps.offsetWidth; st[n].classList.add('now');
    document.getElementById('wp-a').classList.toggle('on', s.on === 'a'); document.getElementById('wp-b').classList.toggle('on', s.on === 'b'); document.getElementById('wc').classList.toggle('on', s.on === 'c');
  }
  function next() { clearTimeout(t); if (!play) return; t = setTimeout(() => { if (i < S.length - 1) { show(i + 1); next(); } else { play = false; btn.textContent = 'Play'; } }, 3600); }
  [...steps.children].forEach(b => b.onclick = () => { show(+b.dataset.i); next(); });
  btn.onclick = () => { play = !play; btn.textContent = play ? 'Pause' : 'Play'; if (play) { if (i === S.length - 1) show(0); next(); } else clearTimeout(t); };
  document.getElementById('w-again').onclick = () => { play = true; btn.textContent = 'Pause'; show(0); next(); };
  show(0);
  new IntersectionObserver(es => es.forEach(e => {
    if (e.isIntersecting && !started) { started = true; if (matchMedia('(prefers-reduced-motion: reduce)').matches) { play = false; btn.textContent = 'Play'; } else next(); }
    if (!e.isIntersecting) { clearTimeout(t); started = false; }
  }), { threshold: .35 }).observe(root);
})();
'''.replace('__MAP__', MAP).replace('__QR__', qr(150)).replace('__WM__', wm('#033D2B', 22))

# ---------------------------------------------------------------- Wow moment: Australia lights up
WOW_SECTION = '''<section class="wow" id="wow" aria-labelledby="wow-h">
  <div class="wrap wow-in">
    <div class="wow-copy">
      <h2 id="wow-h" class="wow-h">Every yes,<br>connected.</h2>
      <p class="wow-lead">Across Australia, every person who says yes to Jesus can be connected with a church near them, and someone to walk with.</p>
      <p class="wow-stat"><b>3,937</b> churches and ministries mapped, in every state and territory.</p>
    </div>
    <div class="wow-map">
      <canvas id="wow-canvas" role="img" aria-label="An illustrated map of Australia. Sparks of light, each one a person saying yes to Jesus, connect to churches nearby until the map glows."></canvas>
      <p class="wow-note">Illustration. Each dot is a church.</p>
    </div>
  </div>
</section>'''

WOW_CSS = '''
.wow { position: relative; background: radial-gradient(120% 90% at 70% 40%, #1B4740 0%, #10302A 55%, #0B231F 100%); color: var(--cream); padding: clamp(80px, 10vw, 140px) 0; overflow: hidden; }
.wow-in { display: grid; grid-template-columns: minmax(0, .8fr) minmax(0, 1.7fr); gap: clamp(24px, 4vw, 64px); align-items: center; }
.wow-h { font: 800 clamp(48px, 7.4vw, 108px)/0.95 var(--head); letter-spacing: -0.045em; margin: 0; color: var(--cream); }
.wow-lead { margin: 26px 0 0; font-size: clamp(18px, 1.6vw, 21px); line-height: 1.55; color: #CFE0D6; max-width: 30ch; }
.wow-stat { margin: 28px 0 0; padding-top: 22px; border-top: 1px solid rgba(248,243,234,.15); font-size: 15px; color: #A9C2B8; max-width: 30ch; }
.wow-stat b { display: block; font: 800 clamp(40px, 4.4vw, 60px)/1 var(--head); letter-spacing: -0.04em; color: var(--peach); margin-bottom: 6px; }
.wow-map { position: relative; }
#wow-canvas { display: block; width: 100%; height: auto; aspect-ratio: 924 / 748; }
.wow-note { margin: 6px 0 0; font-size: 12px; color: #7F9A90; text-align: right; }
@media (max-width: 900px) { .wow-in { grid-template-columns: 1fr; } .wow-lead, .wow-stat { max-width: 40ch; } }
'''

WOW_JS = '''
(() => {
  const cv = document.getElementById('wow-canvas'); if (!cv) return;
  const M = __MAP__;
  const ctx = cv.getContext('2d');
  const W = M.w, H = M.h, pad = 10;
  const outline = new Path2D(M.outline);
  const ch = M.churches.map(([x, y]) => ({ x, y, glow: 0 }));
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  let scale = 1, sparks = [], embers = [], running = false, last = 0, made = 0;
  function size() {
    const r = cv.getBoundingClientRect(), dpr = Math.min(devicePixelRatio || 1, 2);
    cv.width = Math.round(r.width * dpr); cv.height = Math.round(r.width * (H / W) * dpr);
    scale = cv.width / (W + pad * 2);
  }
  function nearest(x, y) { let b = ch[0], d = 1e9; for (const c of ch) { const e = (c.x - x) ** 2 + (c.y - y) ** 2; if (e < d) { d = e; b = c; } } return b; }
  function spawn() {
    const base = ch[(Math.random() * ch.length) | 0];
    const a = Math.random() * Math.PI * 2, r = 14 + Math.random() * 30;
    const x = base.x + Math.cos(a) * r, y = base.y + Math.sin(a) * r;
    sparks.push({ x, y, to: nearest(x, y), t: 0, seed: Math.random() * 10 });
    for (let k = 0; k < 6; k++) embers.push({ x: x + (Math.random() - .5) * 6, y, vx: (Math.random() - .5) * 0.012, vy: -(0.018 + Math.random() * 0.03), life: 0, max: 700 + Math.random() * 700, r: 0.8 + Math.random() * 1.4 });
    made++;
  }
  function draw(dt) {
    ctx.globalCompositeOperation = 'source-over';
    ctx.setTransform(scale, 0, 0, scale, pad * scale, pad * scale);
    ctx.clearRect(-pad, -pad, W + pad * 2, H + pad * 2);
    ctx.fillStyle = 'rgba(248,243,234,0.05)'; ctx.fill(outline);
    ctx.strokeStyle = 'rgba(207,224,214,0.32)'; ctx.lineWidth = 1.2 / scale * 1.4; ctx.stroke(outline);
    ctx.globalCompositeOperation = 'lighter';
    for (const c of ch) {
      c.glow = Math.max(0.2, c.glow - dt * 0.00004);
      ctx.fillStyle = c.glow > 0.4 ? `rgba(255,${Math.round(214 + 30 * (1 - c.glow))},${Math.round(150 + 80 * (1 - c.glow))},${0.3 + c.glow * 0.7})` : `rgba(248,243,234,${0.22 + c.glow * 0.7})`;
      ctx.beginPath(); ctx.arc(c.x, c.y, 2.8 + c.glow * 2.4, 0, 7); ctx.fill();
      if (c.glow > 0.4) { ctx.fillStyle = `rgba(238,120,60,${(c.glow - 0.4) * 0.5})`; ctx.beginPath(); ctx.arc(c.x, c.y, 9 + c.glow * 12, 0, 7); ctx.fill(); }
    }
    sparks = sparks.filter((s) => s.t < 1.6);
    for (const s of sparks) {
      s.t += dt / 1400;
      const p = Math.min(1, Math.max(0, (s.t - 0.25) / 0.75));
      const ease = 1 - (1 - p) ** 3;
      if (s.t < 0.25 || p < 1) {
        const pr = Math.min(1, s.t / 0.25);
        const fl = 1 + Math.sin((s.t * 40) + s.seed) * 0.18 + Math.sin((s.t * 23) + s.seed * 2) * 0.12;
        const fade = s.t > 1 ? Math.max(0, 1 - (s.t - 1) * 1.5) : 1;
        ctx.fillStyle = `rgba(238,96,40,${0.22 * fade})`; ctx.beginPath(); ctx.arc(s.x, s.y, (6 + pr * 14) * fl, 0, 7); ctx.fill();
        ctx.fillStyle = `rgba(255,150,60,${0.85 * fade})`; ctx.beginPath(); ctx.arc(s.x, s.y, (3 + pr * 2.5) * fl, 0, 7); ctx.fill();
        ctx.fillStyle = `rgba(255,236,170,${0.95 * fade})`; ctx.beginPath(); ctx.arc(s.x, s.y, (1.4 + pr) * fl, 0, 7); ctx.fill();
      }
      if (p > 0) {
        const x = s.x + (s.to.x - s.x) * ease, y = s.y + (s.to.y - s.y) * ease;
        const g = ctx.createLinearGradient(s.x, s.y, x, y);
        g.addColorStop(0, 'rgba(238,96,40,0)'); g.addColorStop(1, `rgba(255,210,140,${s.t > 1 ? Math.max(0, 1 - (s.t - 1) * 1.7) : 0.95})`);
        ctx.strokeStyle = g; ctx.lineWidth = 2.4; ctx.beginPath(); ctx.moveTo(s.x, s.y); ctx.lineTo(x, y); ctx.stroke();
        if (p >= 1 && !s.done) { s.done = true; s.to.glow = 1; }
      }
    }
  }
  function drawEmbers(dt) {
    embers = embers.filter((e) => e.life < e.max);
    for (const e of embers) {
      e.life += dt; e.x += e.vx * dt + Math.sin(e.life / 120) * 0.04; e.y += e.vy * dt;
      const a = 1 - e.life / e.max;
      ctx.fillStyle = `rgba(255,${Math.round(140 + 90 * a)},${Math.round(60 + 60 * a)},${a * 0.9})`;
      ctx.beginPath(); ctx.arc(e.x, e.y, e.r * (0.5 + a * 0.5), 0, 7); ctx.fill();
    }
  }
  function frame(now) {
    if (!running) return;
    const dt = Math.min(64, now - (last || now)); last = now;
    const rate = made < 60 ? 70 : 160; // a quick burst, then a steady rhythm
    if (Math.random() < dt / rate) spawn();
    draw(dt); drawEmbers(dt); requestAnimationFrame(frame);
  }
  size(); addEventListener('resize', () => { size(); if (reduce || !running) draw(0); });
  if (reduce) { ch.forEach((c, i) => { c.glow = i % 3 ? 0.35 : 0.9; }); draw(0); return; }
  draw(0);
  new IntersectionObserver((es) => es.forEach((e) => {
    if (e.isIntersecting && !running) { running = true; last = 0; requestAnimationFrame(frame); }
    else if (!e.isIntersecting) running = false;
  }), { threshold: 0.2 }).observe(cv);
})();
'''.replace('__MAP__', MAP)

# ---------------------------------------------------------------- Pentecost flame moments
FIRE_SECTION = '''<section class="fire" id="fire" aria-labelledby="fire-h">
  <canvas class="fire-canvas" id="fire-canvas" aria-hidden="true"></canvas>
  <div class="wrap fire-in">
    <p class="fire-v" id="fire-h">“And divided tongues as of fire appeared to them and rested on each one of them.”</p>
    <p class="fire-c">Acts 2:3 (ESV)</p>
    <p class="fire-l">We're praying for that fire again: on every church, in every city, across Australia.</p>
  </div>
</section>'''

FLAME_SVG = '<svg class="flame" viewBox="0 0 40 56" aria-hidden="true"><defs><linearGradient id="fg" x1="0" y1="1" x2="0" y2="0"><stop offset="0" stop-color="#E25822"/><stop offset=".55" stop-color="#EE8B54"/><stop offset="1" stop-color="#FFD58A"/></linearGradient></defs><path class="fo" d="M20 2C24 14 36 20 36 34c0 10-7 19-16 19S4 44 4 34c0-8 5-12 8-18 1 6 4 9 7 10C17 18 17 10 20 2z" fill="url(#fg)"/><path class="fi" d="M20 26c3 6 8 9 8 15 0 5-4 9-8 9s-8-4-8-9c0-4 3-6 4-9 1 3 2 4 3 5 0-4 0-7 1-11z" fill="#FFE7B0"/></svg>'

FIRE_CSS = '''
.fire { position: relative; overflow: hidden; background: radial-gradient(90% 70% at 50% 100%, #3A1A0E 0%, #1A1410 45%, #0E1412 100%); color: var(--cream); padding: clamp(110px, 14vw, 200px) 0 clamp(130px, 16vw, 230px); text-align: center; isolation: isolate; }
.fire-canvas { position: absolute; inset: 0; width: 100%; height: 100%; z-index: -1; }
.fire-in { position: relative; max-width: 980px; }
.fire-v { margin: 0 auto; font-family: var(--serif, Georgia, serif); font-size: clamp(32px, 4.6vw, 62px); line-height: 1.18; letter-spacing: -0.01em; color: #FFF6E8; text-shadow: 0 2px 30px rgba(226,88,34,.35); max-width: 22ch; text-wrap: balance; }
.fire-c { margin: 22px 0 0; font: 700 15px/1 var(--head); color: #FFB37A; }
.fire-l { margin: 34px auto 0; font-size: clamp(18px, 1.7vw, 22px); line-height: 1.55; color: #E9D9C6; max-width: 34ch; text-wrap: balance; }
.heart-item { position: relative; }
.heart-item .flame { width: 30px; height: 42px; display: block; margin-bottom: 14px; transform-origin: 50% 100%; animation: flick 2.4s ease-in-out infinite; filter: drop-shadow(0 4px 10px rgba(226,88,34,.35)); }
.heart-item:nth-child(2) .flame { animation-delay: -.8s; } .heart-item:nth-child(3) .flame { animation-delay: -1.6s; }
.heart-item .flame .fi { transform-origin: 50% 100%; animation: flick2 1.3s ease-in-out infinite; }
@keyframes flick { 0%,100% { transform: scale(1, 1) skewX(0deg); } 25% { transform: scale(.96, 1.06) skewX(-2deg); } 50% { transform: scale(1.03, .97) skewX(1.5deg); } 75% { transform: scale(.98, 1.04) skewX(-1deg); } }
@keyframes flick2 { 0%,100% { transform: scale(1, 1); } 50% { transform: scale(.9, 1.12); } }
.join { position: relative; isolation: isolate; }
.join-embers { position: absolute; inset: 0; width: 100%; height: 100%; z-index: -1; pointer-events: none; }
@media (prefers-reduced-motion: reduce) { .heart-item .flame, .heart-item .flame .fi { animation: none; } }
'''

FIRE_JS = '''
(() => {
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  // Flame field: many soft particles rising from the base, additive blending, stronger while in view.
  function flameField(cv, opts) {
    const ctx = cv.getContext('2d'); let W = 0, H = 0, dpr = 1, parts = [], on = false, last = 0, power = 0, target = 0;
    function size() { const r = cv.getBoundingClientRect(); dpr = Math.min(devicePixelRatio || 1, 2); W = r.width; H = r.height; cv.width = W * dpr; cv.height = H * dpr; ctx.setTransform(dpr, 0, 0, dpr, 0, 0); }
    function spawn() {
      const x = Math.random() * W; const big = Math.random() < opts.tongues;
      parts.push({ x, y: H + 10, vx: (Math.random() - .5) * 0.02, vy: -(opts.speed * (0.6 + Math.random() * 0.8)), r: big ? 26 + Math.random() * 30 : 6 + Math.random() * 14, life: 0, max: opts.life * (0.6 + Math.random() * 0.7), seed: Math.random() * 6 });
    }
    function frame(now) {
      if (!on) return; const dt = Math.min(48, now - (last || now)); last = now;
      power += (target - power) * 0.04;
      const n = opts.rate * power * dt / 16; for (let i = 0; i < n; i++) spawn();
      ctx.globalCompositeOperation = 'source-over'; ctx.clearRect(0, 0, W, H);
      ctx.globalCompositeOperation = 'lighter';
      parts = parts.filter((p) => p.life < p.max);
      for (const p of parts) {
        p.life += dt; const k = p.life / p.max;
        p.x += (p.vx + Math.sin(p.life / 180 + p.seed) * 0.03) * dt; p.y += p.vy * dt;
        const r = p.r * (1 - k * 0.7);
        const g = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, r);
        const a = (1 - k) * opts.alpha;
        g.addColorStop(0, `rgba(255,${Math.round(220 - k * 120)},${Math.round(150 - k * 120)},${a})`);
        g.addColorStop(.45, `rgba(238,${Math.round(120 - k * 60)},40,${a * 0.55})`);
        g.addColorStop(1, 'rgba(120,30,10,0)');
        ctx.fillStyle = g; ctx.beginPath(); ctx.arc(p.x, p.y, r, 0, 7); ctx.fill();
      }
      requestAnimationFrame(frame);
    }
    size(); addEventListener('resize', size);
    if (reduce) { target = power = 1; for (let i = 0; i < 220; i++) { spawn(); const p = parts[parts.length - 1]; p.life = Math.random() * p.max * .8; p.y = H - Math.random() * H * opts.reach; } on = true; frame(performance.now()); on = false; return; }
    new IntersectionObserver((es) => es.forEach((e) => {
      target = Math.min(1, e.intersectionRatio * 1.6);
      if (e.isIntersecting && !on) { on = true; last = 0; requestAnimationFrame(frame); }
      else if (!e.isIntersecting) { on = false; parts = []; power = 0; }
    }), { threshold: [0, .15, .3, .45, .6, .75] }).observe(cv);
  }
  window.__flameField = flameField;
  const f = document.getElementById('fire-canvas');
  if (f) flameField(f, { rate: 3.2, speed: 0.16, life: 2600, alpha: 0.5, tongues: 0.18, reach: .6 });
  const j = document.querySelector('.join-embers');
  if (j) flameField(j, { rate: 0.35, speed: 0.07, life: 5200, alpha: 0.28, tongues: 0, reach: 1 });
})();
'''

# ---------------------------------------------------------------- Opening: Matthew 28 over flame, every visit

