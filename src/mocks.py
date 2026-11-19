"""Small drawn product screens, one per Always product. Pure HTML and CSS, decorative only."""

MOCKS = {
'app': '''<div class="mk-card mk-app"><span class="mk-k">Verse for today</span>
<p class="mk-verse">“I am with you always.”</p><span class="mk-cite">Matthew 28:20</span>
<div class="mk-row"><span class="mk-pill">Pray</span><span class="mk-pill mk-pill-o">Share</span></div>
<div class="mk-tabs"><i class="on"></i><i></i><i></i><i></i></div></div>''',
'pages': '''<div class="mk-card mk-pages"><div class="mk-brand"><span class="mk-logo"></span><b>Your ministry</b></div>
<p class="mk-h">Today I said yes to Jesus</p><span class="mk-in">First name</span><span class="mk-in">Suburb</span>
<span class="mk-btn">Take my next step</span><span class="mk-qr" aria-hidden="true"></span></div>''',
'compliance': '''<div class="mk-card mk-comp"><div class="mk-top"><b>Quarterly check-up</b><span class="mk-chip">Ready</span></div>
<ul><li><i class="ok"></i>Privacy</li><li><i class="ok"></i>Child safety</li><li><i class="ok"></i>Charity reporting</li><li><i class="due"></i>Messaging rules<em>Review</em></li></ul>
<span class="mk-foot">Approved by your board</span></div>''',
'reports': '''<div class="mk-card mk-rep"><div class="mk-top"><b>This month</b><span class="mk-chip">Totals only</span></div>
<div class="mk-bar" style="--w:94%"><span>Responded</span></div><div class="mk-bar" style="--w:72%"><span>Introduced</span></div>
<div class="mk-bar" style="--w:55%"><span>Contacted</span></div><div class="mk-bar mk-bar-p" style="--w:38%"><span>Part of a church family</span></div></div>''',
'connect': '''<div class="mk-conn"><div class="mk-card mk-person"><span class="mk-av">S</span><div><b>Sam</b><span>Wants a church nearby</span></div></div>
<span class="mk-link" aria-hidden="true"></span>
<div class="mk-card mk-church"><b>A local church</b><span>Partner church · 2 km away</span><div class="mk-row"><span class="mk-pill">Welcome Sam</span><span class="mk-pill mk-pill-o">Pass</span></div></div></div>''',
'agents': '''<div class="mk-card mk-agent"><span class="mk-k">Draft for your team</span>
<p class="mk-msg">Hi Sam, great to meet you on Friday. Youth night is Tuesday at 7. Would you like to come?</p>
<div class="mk-row"><span class="mk-pill">Approve</span><span class="mk-pill mk-pill-o">Edit</span></div>
<span class="mk-foot">A person approves every step</span></div>''',
'build': '''<div class="mk-card mk-code"><div class="mk-dots"><i></i><i></i><i></i></div>
<code><span class="c">// churches welcoming near 2150</span>
<span class="k">const</span> {{ items }} = <span class="k">await</span>
  always.feed.churches({{
    postcode: <span class="s">'2150'</span>,
    welcoming: <span class="k">true</span>,
  }});</code></div>''',
}


def mock(slug, size=''):
    return f'<div class="mk mk-{slug} {size}" aria-hidden="true">{MOCKS[slug]}</div>'


CSS = '''
/* ---- Product screens ---- */
.mk { --tint: var(--peach-soft); position: relative; display: grid; place-items: center; padding: 28px 24px; background: var(--tint); border-radius: 22px; min-height: 230px; overflow: hidden; isolation: isolate; }
.mk::before { content: ''; position: absolute; inset: auto -20% -55% -20%; height: 90%; background: radial-gradient(closest-side, rgba(255,253,248,.7), transparent); z-index: -1; }
.mk-compliance, .mk-reports { --tint: var(--sage); }
.mk-connect { --tint: #EFE5D1; }
.mk-agents { --tint: #E9E4F1; }
.mk-build { --tint: var(--green-deep); }
.mk-build::before { background: radial-gradient(closest-side, rgba(232,165,119,.16), transparent); }
.mk-code { box-shadow: inset 0 0 0 1px rgba(228,238,231,.08), 0 24px 40px -24px rgba(0,0,0,.6); }
.mk-card { width: min(270px, 100%); background: var(--paper); border-radius: 18px; padding: 16px 16px 15px; box-shadow: 0 1px 0 rgba(30,42,38,.04), 0 18px 34px -22px rgba(20,53,47,.45); display: grid; gap: 9px; font-family: var(--text); color: var(--ink); text-align: left; }
.mk-k { font: 700 11.5px/1 var(--head); color: var(--clay); }
.mk-row { display: flex; gap: 6px; flex-wrap: wrap; }
.mk-pill { font: 700 11.5px/1 var(--head); padding: 8px 12px; border-radius: 999px; background: var(--green); color: var(--cream); }
.mk-pill-o { background: transparent; color: var(--green); box-shadow: inset 0 0 0 1.5px rgba(27,71,64,.25); }
.mk-chip { font: 700 10.5px/1 var(--head); padding: 5px 8px; border-radius: 999px; background: var(--sage); color: var(--green); }
.mk-top { display: flex; justify-content: space-between; align-items: center; gap: 8px; } .mk-top b { font: 800 14px/1.2 var(--head); color: var(--green); }
.mk-foot { font-size: 11px; color: var(--muted); }
.mk .mk-verse { margin: 2px 0 0; font: 400 21px/1.2 'Newsreader', Georgia, serif; color: var(--green); }
.mk-cite { font: 600 11px/1 var(--head); color: var(--muted); }
.mk-tabs { display: flex; justify-content: space-around; padding-top: 10px; border-top: 1px solid var(--line); }
.mk-tabs i { width: 16px; height: 4px; border-radius: 4px; background: var(--line); } .mk-tabs i.on { background: var(--peach); }
.mk-pages { --brand: #6B4FA0; position: relative; }
.mk-brand { display: flex; align-items: center; gap: 8px; } .mk-brand b { font: 700 12.5px/1 var(--head); color: #3A2A5C; }
.mk-logo { width: 22px; height: 22px; border-radius: 7px; background: var(--brand); }
.mk .mk-h { margin: 2px 0; font: 800 18px/1.15 var(--head); color: #3A2A5C; letter-spacing: -0.01em; max-width: 13ch; }
.mk-in { font-size: 11px; color: #8C82A3; padding: 9px 10px; border-radius: 10px; border: 1.5px solid #E5DFEE; }
.mk-btn { margin-top: 2px; text-align: center; padding: 11px; border-radius: 999px; background: var(--brand); color: #fff; font: 700 12px/1 var(--head); }
.mk-qr { position: absolute; top: 14px; right: 14px; width: 34px; height: 34px; border-radius: 6px; background:
  conic-gradient(from 90deg at 30% 30%, #3A2A5C 25%, transparent 0) 0 0/11px 11px, #F3EFF8; opacity: .85; }
.mk-comp ul { list-style: none; margin: 2px 0; padding: 0; display: grid; gap: 7px; }
.mk-comp li { display: flex; align-items: center; gap: 8px; font-size: 12.5px; color: var(--soft); }
.mk-comp li em { margin-left: auto; font: 700 10.5px/1 var(--head); font-style: normal; color: var(--clay); background: var(--peach-soft); padding: 4px 7px; border-radius: 999px; }
.mk-comp i { width: 16px; height: 16px; border-radius: 50%; flex: none; display: grid; place-items: center; }
.mk-comp i.ok { background: var(--green); } .mk-comp i.ok::after { content: ''; width: 6px; height: 3px; border-left: 1.6px solid var(--cream); border-bottom: 1.6px solid var(--cream); transform: rotate(-45deg) translate(1px, -1px); }
.mk-comp i.due { box-shadow: inset 0 0 0 1.6px var(--peach); }
.mk-bar { position: relative; height: 26px; border-radius: 8px; background: var(--sage-2); overflow: hidden; }
.mk-bar::before { content: ''; position: absolute; inset: 0 auto 0 0; width: var(--w); background: rgba(27,71,64,.16); border-radius: 8px; }
.mk-bar-p::before { background: var(--peach); }
.mk-bar span { position: relative; display: block; padding: 7px 10px; font: 600 11px/1 var(--head); color: var(--green); }
.mk-conn { display: grid; justify-items: center; gap: 0; width: min(270px, 100%); }
.mk-person { display: flex; align-items: center; gap: 10px; width: 82%; justify-self: start; }
.mk-person b, .mk-church b { font: 800 13.5px/1.2 var(--head); color: var(--green); display: block; }
.mk-person span:not(.mk-av), .mk-church > span { font-size: 11.5px; color: var(--muted); }
.mk-av { width: 30px; height: 30px; border-radius: 50%; background: var(--peach); color: var(--night); display: grid; place-items: center; font: 800 13px/1 var(--head); flex: none; }
.mk-link { width: 2px; height: 22px; background: repeating-linear-gradient(var(--clay) 0 4px, transparent 4px 8px); }
.mk-church { width: 86%; justify-self: end; gap: 5px; }
.mk .mk-msg { margin: 0; padding: 11px 12px; border-radius: 14px 14px 14px 4px; background: #F1EDF7; font-size: 12.5px; line-height: 1.45; color: #3A2A5C; }
.mk-code { background: #0F2925; color: #CFE0D7; gap: 12px; }
.mk-dots { display: flex; gap: 5px; } .mk-dots i { width: 8px; height: 8px; border-radius: 50%; background: rgba(228,238,231,.22); }
.mk-code code { font: 500 11.5px/1.65 ui-monospace, 'SF Mono', Menlo, monospace; white-space: pre; overflow: hidden; }
.mk-code .c { color: #7E9C91; } .mk-code .k { color: var(--peach); } .mk-code .s { color: #B8D8A8; }
/* page heroes style every p; reset inside screens */
.page-hero .mk p { max-width: none; }
.page-hero .mk .mk-h { margin: 2px 0; font-size: 18px; line-height: 1.15; color: #3A2A5C; }
.page-hero .mk .mk-verse { margin: 2px 0 0; font-size: 21px; line-height: 1.2; color: var(--green); }
.page-hero .mk .mk-msg { margin: 0; font-size: 12.5px; line-height: 1.45; color: #3A2A5C; }
.mk-lg { min-height: 380px; border-radius: 30px; padding: 40px; }
.mk-lg .mk-card, .mk-lg .mk-conn { width: min(320px, 100%); transform: scale(1.06); }
.page-hero .mk-lg { background: rgba(248,243,234,.08); box-shadow: inset 0 0 0 1px rgba(248,243,234,.1); }
.page-hero .mk-lg::before { background: radial-gradient(closest-side, rgba(232,165,119,.22), transparent); }
@media (max-width: 860px) { .mk-lg { min-height: 300px; padding: 28px 20px; } .mk-lg .mk-card, .mk-lg .mk-conn { transform: none; } }
'''
