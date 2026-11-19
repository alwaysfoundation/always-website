"""'Wherever people respond' section for the Pages module: illustrated touchpoints."""

def _svg(body):
    return f'<svg viewBox="0 0 240 140" aria-hidden="true">{body}</svg>'

INK, GREEN, PEACH, CREAM, SAGE = '#1E2A26', '#1B4740', '#E8A577', '#FFFDF8', '#CFE0D6'

def _qr(x, y, s, c=GREEN):
    cells = '1110111 1010101 1110111 0001000 1101011 0110110 1011101'.split()
    k = s / 7
    out = ''.join(f'<rect x="{x + j*k:.1f}" y="{y + i*k:.1f}" width="{k:.1f}" height="{k:.1f}" fill="{c}"/>' for i, row in enumerate(cells) for j, b in enumerate(row) if b == '1')
    return out

ART = {
 'street': _svg(f'<rect x="38" y="30" width="78" height="92" rx="10" fill="{CREAM}" stroke="{GREEN}" stroke-width="2"/>{_qr(52,44,50)}<rect x="52" y="102" width="50" height="6" rx="3" fill="{PEACH}"/>'
                f'<g class="rs-phone"><rect x="134" y="20" width="62" height="108" rx="12" fill="{GREEN}"/><rect x="140" y="30" width="50" height="86" rx="6" fill="{SAGE}"/><rect class="rs-scan" x="142" y="40" width="46" height="3" rx="1.5" fill="{PEACH}"/></g>'),
 'altar': _svg(f'<rect x="30" y="16" width="180" height="84" rx="8" fill="{GREEN}"/><rect x="38" y="24" width="164" height="68" rx="4" fill="#2A5E52"/>{_qr(100,32,40,CREAM)}'
               + ''.join(f'<circle cx="{x}" cy="{y}" r="9" fill="{INK}" opacity=".85"/><rect x="{x-12}" y="{y+8}" width="24" height="20" rx="10" fill="{INK}" opacity=".85"/>' for x, y in [(52,112),(84,108),(116,112),(150,106),(184,112)])
               + f'<rect class="rs-hand" x="147" y="80" width="6" height="22" rx="3" fill="{INK}"/>'),
 'tap': _svg(f'<ellipse cx="88" cy="84" rx="54" ry="22" fill="none" stroke="{PEACH}" stroke-width="12"/><rect x="74" y="72" width="28" height="18" rx="5" fill="{GREEN}"/>'
             f'<g class="rs-waves" fill="none" stroke="{GREEN}" stroke-width="3" stroke-linecap="round"><path d="M128 52 q8 10 0 20"/><path d="M136 46 q13 16 0 32"/><path d="M144 40 q18 22 0 44"/></g>'
             f'<rect x="160" y="22" width="52" height="96" rx="11" fill="{GREEN}"/><rect x="165" y="31" width="42" height="76" rx="5" fill="{SAGE}"/><rect x="171" y="84" width="30" height="10" rx="5" fill="{PEACH}"/>'),
 'ticket': _svg(f'<path d="M30 34 h180 v24 a12 12 0 0 0 0 24 v24 h-180 v-24 a12 12 0 0 0 0 -24z" fill="{CREAM}" stroke="{GREEN}" stroke-width="2"/>'
                f'<line x1="150" y1="38" x2="150" y2="102" stroke="{GREEN}" stroke-width="2" stroke-dasharray="4 5"/>'
                f'<rect x="46" y="48" width="80" height="10" rx="5" fill="{GREEN}"/><rect x="46" y="66" width="56" height="7" rx="3.5" fill="{SAGE}"/><rect x="46" y="80" width="64" height="7" rx="3.5" fill="{SAGE}"/>{_qr(160,50,40)}'),
 'online': _svg(f'<rect x="28" y="18" width="184" height="106" rx="10" fill="{CREAM}" stroke="{GREEN}" stroke-width="2"/><rect x="28" y="18" width="184" height="16" rx="10" fill="{GREEN}"/>'
                f'<rect x="40" y="44" width="96" height="58" rx="6" fill="{GREEN}"/><path d="M80 62 l18 11 -18 11z" fill="{CREAM}"/>'
                f'<rect x="148" y="46" width="52" height="8" rx="4" fill="{SAGE}"/><rect x="148" y="60" width="40" height="8" rx="4" fill="{SAGE}"/><rect class="rs-btn" x="148" y="82" width="52" height="18" rx="9" fill="{PEACH}"/>'),
 'embed': _svg(f'<path d="M30 28 h120 a10 10 0 0 1 10 10 v40 a10 10 0 0 1 -10 10 h-84 l-20 16 v-16 h-16 a10 10 0 0 1 -10 -10 v-40 a10 10 0 0 1 10 -10z" fill="{GREEN}"/>'
               f'<rect x="44" y="44" width="80" height="8" rx="4" fill="{CREAM}" opacity=".85"/><rect x="44" y="60" width="54" height="8" rx="4" fill="{PEACH}"/>'
               f'<rect class="rs-form" x="118" y="58" width="94" height="66" rx="10" fill="{CREAM}" stroke="{GREEN}" stroke-width="2"/><rect x="128" y="70" width="74" height="9" rx="4.5" fill="{SAGE}"/><rect x="128" y="85" width="74" height="9" rx="4.5" fill="{SAGE}"/><rect x="128" y="102" width="44" height="12" rx="6" fill="{GREEN}"/>'),
}

CARDS = [
    ('street', 'On the street', 'A QR card or link on an evangelist’s phone. Someone scans, and their details are saved safely in seconds.'),
    ('altar', 'At the altar call', 'A code on the big screen, so everyone who responds can say so, then and there.'),
    ('tap', 'Tap to respond', 'Armbands, tap discs and cards with an NFC chip open your page with a tap. No app needed.'),
    ('ticket', 'Tickets and passes', 'A code or chip on a concert ticket, event pass or lanyard, so the response travels home with them.'),
    ('online', 'Landing pages and video', 'A page for your event, campaign or video, with one clear way to respond.'),
    ('embed', 'Comments and embeds', 'A link for comments and posts, or a response card inside your own website or app.'),
]

SECTION = '''<section class="sec pg-sec rs-sec"><div class="wrap">
  <h2 class="pg-h rv">Wherever people respond</h2>
  <p class="pg-lead rv">One page, many ways in. Every scan, tap or click leads to the same simple next step, in your name.</p>
  <div class="rs-grid">''' + ''.join(
    f'<article class="rs-card rv"><div class="rs-art rs-{k}">{ART[k]}</div><h3>{t}</h3><p>{d}</p></article>' for k, t, d in CARDS) + '''</div>
  <ul class="rs-safe rv">
    <li><b>Age asked first</b><span>The rules for young people apply before anything else.</span></li>
    <li><b>Consent on every form</b><span>Nothing is shared without a clear yes.</span></li>
    <li><b>No names on screen</b><span>Live totals for your team, never a list of people.</span></li>
  </ul>
</div></section>'''

CSS = '''
.rs-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 20px; margin-top: 44px; }
.rs-card { padding: 14px 14px 26px; border-radius: 26px; background: #FFFDF8; border: 1px solid var(--line); transition: transform .35s cubic-bezier(.2,.7,.2,1), box-shadow .35s ease, border-color .35s ease; }
.rs-card:hover { transform: translateY(-4px); border-color: rgba(27,71,64,.2); box-shadow: 0 30px 60px -36px rgba(10,30,26,.4); }
.rs-art { border-radius: 18px; background: var(--sage); padding: 12px 8px; }
.rs-art svg { display: block; width: 100%; height: auto; }
.rs-card h3 { margin: 22px 12px 0; font-size: 22px; letter-spacing: -0.02em; color: var(--green); }
.rs-card p { margin: 8px 12px 0; font-size: 16.5px; line-height: 1.55; color: var(--soft); }
.rs-scan { animation: rsScan 2.4s ease-in-out infinite; }
@keyframes rsScan { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(66px); } }
.rs-waves path { animation: rsWave 2s ease-in-out infinite; }
.rs-waves path:nth-child(2) { animation-delay: .2s; } .rs-waves path:nth-child(3) { animation-delay: .4s; }
@keyframes rsWave { 0%, 100% { opacity: .25; } 50% { opacity: 1; } }
.rs-hand { transform-box: fill-box; transform-origin: 50% 100%; animation: rsHand 3s ease-in-out infinite; }
@keyframes rsHand { 0%, 100% { transform: scaleY(.4); } 40%, 70% { transform: scaleY(1); } }
.rs-btn, .rs-form { transform-box: fill-box; transform-origin: center; transition: transform .35s cubic-bezier(.2,.7,.2,1); }
.rs-card:hover .rs-btn { transform: scale(1.08); } .rs-card:hover .rs-form { transform: translateY(-4px); }
.rs-safe { list-style: none; margin: 40px 0 0; padding: 26px 28px; border-radius: 22px; background: var(--green); color: var(--cream); display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 24px; }
.rs-safe li { display: grid; gap: 4px; padding-left: 34px; position: relative; }
.rs-safe li::before { content: ''; position: absolute; left: 0; top: 1px; width: 22px; height: 22px; border-radius: 50%; background: var(--peach); -webkit-mask: radial-gradient(circle, #000 70%, transparent 71%); }
.rs-safe li::after { content: ''; position: absolute; left: 7px; top: 6px; width: 6px; height: 10px; border: solid var(--green); border-width: 0 2.5px 2.5px 0; transform: rotate(45deg); }
.rs-safe b { font: 700 17px/1.25 var(--head); } .rs-safe span { font-size: 15px; line-height: 1.5; color: var(--on-green); }
@media (max-width: 1000px) { .rs-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 640px) { .rs-grid, .rs-safe { grid-template-columns: minmax(0, 1fr); } }
@media (prefers-reduced-motion: reduce) { .rs-scan, .rs-waves path, .rs-hand { animation: none; } .rs-card, .rs-btn, .rs-form { transition: none; } .rs-card:hover { transform: none; } }
'''
