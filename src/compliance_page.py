"""Always Compliance: marketing page, free check-up (onboarding) and docs.

The register is copied from always-platform/spec/compliance/register.json, so the
check-up in the browser uses exactly the same rules as the platform. Nothing the
visitor enters is sent anywhere or saved.
"""
import json
import os
from html import escape

ROOT = os.path.dirname(os.path.abspath(__file__))
REGISTER = json.load(open(os.path.join(ROOT, 'compliance-register.json')))

AREAS = {
    'privacy': ('Privacy', 'The Privacy Act, data breaches, and the new Children\'s Online Privacy Code.'),
    'child_safety': ('Child safety', 'Working with children checks and the Child Safe Standards in your state.'),
    'charity': ('Charity', 'ACNC annual reporting, Governance Standards and record keeping.'),
    'messages': ('Emails and texts', 'Spam Act rules for newsletters, invitations and appeals.'),
}

STATES = [
    ('NSW', 'Working with Children Check'), ('VIC', 'Working with Children Check'), ('QLD', 'Blue Card'),
    ('WA', 'Working with Children Check'), ('SA', 'Working with Children Check'), ('TAS', 'Working with Vulnerable People'),
    ('ACT', 'Working with Vulnerable People'), ('NT', 'Ochre Card'),
]

PAGE = f'''<section class="page-hero cmx-hero"><div class="wrap pd-split">
  <div>
    <p class="pl-kick">Always Compliance</p>
    <h1>Compliance, made clear.</h1>
    <p class="pd-line">Know exactly what applies to your ministry, approve a simple check-up each quarter, and hear when the law changes.</p>
    <div class="pg-cta"><a class="btn btn-peach" href="#/compliance/check">Start your free check-up</a><a class="btn btn-ghost" href="#/compliance/problem">See the problem we solve</a></div>
    <p class="cm-fine">Free for churches. About ten minutes. A guide to common obligations, not legal advice.</p>
  </div>
  <div class="cmx-card" aria-hidden="true">
    <div class="cmx-card-top"><div><b>Quarterly check-up</b><span>Hope Church · NSW and VIC</span></div><span class="cmx-q">Q4</span></div>
    <div class="cmx-meter"><div class="cmx-meter-bar"><i style="width:75%"></i></div><span>9 of 12 in place</span></div>
    <ul>
      <li class="ok"><i></i><span>Privacy policy published</span></li>
      <li class="ok"><i></i><span>Consent recorded on every form</span></li>
      <li class="todo"><i></i><span>Working with Children Check register</span><em>To do</em></li>
      <li class="soon"><i></i><span>Children's Online Privacy Code</span><em>Coming</em></li>
    </ul>
    <div class="cmx-card-foot"><span>Ready for your board</span><b>Approve</b></div>
  </div>
</div></section>

<section class="sec cmx-problem" id="problem"><div class="wrap">
  <p class="cmx-big rv">Eight states and territories. Four areas of law. Rules that keep changing.</p>
  <div class="cmx-states rv" aria-label="The same kind of check has a different name in each state and territory">
    {''.join(f'<div><b>{st}</b><span>{nm}</span></div>' for st, nm in STATES)}
  </div>
  <p class="cmx-caption rv">One kind of check for people who work with children, with a different name and different rules in every state.</p>
  <div class="sl-rows cmx-why">
    <div class="sl-row rv"><h3>A patchwork</h3><p>Child safety, screening checks and privacy differ from state to state, and a ministry across borders has to meet them all.</p></div>
    <div class="sl-row rv"><h3>Always moving</h3><p>Privacy reforms, a new Children's Online Privacy Code, updated Child Safe Standards. What was right last year may not be now.</p></div>
    <div class="sl-row rv"><h3>Nobody's full-time job</h3><p>Most ministries run on small teams and volunteers, yet the board carries the responsibility.</p></div>
  </div>
</div></section>

<section class="sec pg-sec pg-sage cmx-value"><div class="wrap">
  <h2 class="pg-h rv">What Always Compliance does</h2>
  <div class="cmx-trio">
    <div class="cmx-tile rv"><div class="cmx-art"><div class="cmx-mini">
      <span class="cmx-mini-k">What applies to you</span>
      <div class="cmx-mini-row"><b>Privacy</b><span>4</span></div><div class="cmx-mini-row"><b>Child safety</b><span>3</span></div><div class="cmx-mini-row"><b>Charity</b><span>3</span></div><div class="cmx-mini-row"><b>Emails and texts</b><span>2</span></div>
    </div></div><h3>One clear picture</h3><p>Answer eleven questions and see every obligation that applies to you, in plain English, with what to do next.</p></div>
    <div class="cmx-tile rv"><div class="cmx-art"><div class="cmx-mini">
      <span class="cmx-mini-k">October to December</span>
      <p class="cmx-mini-h">Your check-up is ready</p>
      <span class="cmx-mini-s">Review, update and approve</span>
      <span class="cmx-mini-btn">Approve for the board</span>
    </div></div><h3>A check-up every quarter</h3><p>A short, clear record each quarter. Someone at your ministry reviews it and approves it for your board.</p></div>
    <div class="cmx-tile rv"><div class="cmx-art"><div class="cmx-mini cmx-alert">
      <span class="cmx-mini-k">Law change</span>
      <p class="cmx-mini-h">Child Safe Standards updated</p>
      <span class="cmx-mini-s">Affects 1 obligation for your ministry</span>
      <span class="cmx-mini-link">See what changed</span>
    </div></div><h3>Alerts when the law changes</h3><p>We watch official sources and tell you what changed, what it means for you, and what to do.</p></div>
  </div>
</div></section>

<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">How it works</h2>
  <div class="pg-steps">
    <div class="pg-step rv"><span>01</span><h3>Tell us about your ministry</h3><p>Where you meet, who you work with and how you keep in touch. Eleven quick questions.</p></div>
    <div class="pg-step rv"><span>02</span><h3>See where you stand</h3><p>What's in place, what needs attention, and what's coming. Always fills in what it already does for you.</p></div>
    <div class="pg-step rv"><span>03</span><h3>Approve each quarter</h3><p>A fresh check-up every quarter, plus an alert whenever a rule that applies to you changes.</p></div>
  </div>
</div></section>

<section class="sec pg-sec pg-sage"><div class="wrap">
  <h2 class="pg-h rv">What it covers</h2>
  <div class="pg-feats">{''.join(f'<div class="pg-feat rv"><h3>{t}</h3><p>{d}</p></div>' for t, d in AREAS.values())}</div>
</div></section>

<section class="sec pg-sec" id="check" aria-labelledby="check-h"><div class="wrap">
  <h2 class="pg-h rv" id="check-h">Try the free check-up</h2>
  <p class="pg-lead rv">About ten minutes. You don't need an account, and nothing you enter is sent or saved.</p>
  <div class="cw" id="cw">
    <ol class="cw-progress" aria-label="Check-up steps"><li data-step="1" class="on">Your ministry</li><li data-step="2">What you do</li><li data-step="3">Your results</li></ol>
    <form id="cw-profile" class="cw-step" data-step="1" novalidate></form>
    <form id="cw-evidence" class="cw-step" data-step="2" hidden novalidate></form>
    <div id="cw-report" class="cw-step" data-step="3" hidden tabindex="-1"></div>
  </div>
</div></section>

<section class="sec pg-sec solutions-home"><div class="wrap">
  <h2 class="pg-h rv">Why you can trust it</h2>
  <div class="sl-rows">
    <div class="sl-row rv"><h3>Checked by people</h3><p>A qualified reviewer approves every change to the rules before it reaches you.</p></div>
    <div class="sl-row rv"><h3>Linked to the law</h3><p>Every obligation links to its official source, so you can read it for yourself.</p></div>
    <div class="sl-row rv"><h3>Open to everyone</h3><p>The full list is open, so denominations and safe ministry teams can share one view of the rules. <a class="cm-link" href="#/docs/compliance-register">See every obligation</a></p></div>
  </div>
</div></section>

<section class="sec pg-sec pg-sage" id="infrastructure" aria-labelledby="infra-h"><div class="wrap">
  <div class="cm-infra-head"><div><p class="pl-kick cm-kick rv">For Christian tech platforms</p>
  <h2 class="pg-h rv" id="infra-h">Build it into your own product.</h2>
  <p class="pg-lead rv">Give your users the same clear view of the rules without leaving your app: the open register, change alerts and a check-up you can embed. Love is Our Weapon is our first user.</p>
  <div class="pg-cta rv"><a class="btn btn-peach" href="#/docs/compliance-platforms">Read the guide</a><a class="btn btn-ghost-dark" href="#/contact/compliance">Talk to us</a></div></div>
  <div class="cm-embed rv" aria-hidden="true"><span class="cm-embed-k">Add the check-up to any page</span><code>&lt;script type="module"
  src="…/sdk/v0/compliance-widget.js"&gt;&lt;/script&gt;
&lt;always-compliance-check&gt;
&lt;/always-compliance-check&gt;</code></div></div>
</div></section>

<section class="sec pd-statement cmx-end"><div class="wrap">
  <p class="rv">Free for churches.</p>
  <span class="cmx-end-sub rv">Larger ministries contribute according to their size. One sign-in for every Always module.</span>
  <div class="pg-cta rv"><a class="btn btn-peach" href="#/compliance/check">Start your free check-up</a><a class="btn btn-ghost-dark" href="#/contact/compliance">Talk to us</a></div>
</div></section>
'''

CSS = '''
/* ---- Always Compliance, productised ---- */
.cmx-hero h1 { font-size: clamp(48px, 6.2vw, 92px); }
.cmx-card { justify-self: end; width: min(400px, 100%); background: #FFFDF8; color: var(--ink); border-radius: 26px; padding: 22px; display: grid; gap: 16px; box-shadow: 0 40px 80px -40px rgba(0,0,0,.6); }
.cmx-card-top { display: flex; justify-content: space-between; align-items: start; gap: 12px; }
.cmx-card-top b { display: block; font: 800 18px/1.2 var(--head); color: var(--green); }
.cmx-card-top div span { font-size: 13px; color: var(--muted); }
.cmx-q { font: 400 26px/1 'Newsreader', Georgia, serif; color: var(--clay); }
.cmx-meter { display: grid; gap: 6px; } .cmx-meter span { font: 600 12.5px/1 var(--head); color: var(--soft); }
.cmx-meter-bar { height: 8px; border-radius: 99px; background: var(--sage-2); overflow: hidden; } .cmx-meter-bar i { display: block; height: 100%; border-radius: 99px; background: var(--green); }
.cmx-card ul { list-style: none; margin: 0; padding: 0; display: grid; gap: 4px; }
.cmx-card li { display: flex; align-items: center; gap: 10px; padding: 10px 0; border-top: 1px solid var(--line); font-size: 14px; color: var(--soft); }
.cmx-card li i { width: 18px; height: 18px; border-radius: 50%; flex: none; display: grid; place-items: center; }
.cmx-card li.ok i { background: var(--green); } .cmx-card li.ok i::after { content: ''; width: 7px; height: 3.5px; border-left: 1.8px solid #fff; border-bottom: 1.8px solid #fff; transform: rotate(-45deg) translate(1px, -1px); }
.cmx-card li.todo i { box-shadow: inset 0 0 0 2px var(--peach); } .cmx-card li.soon i { box-shadow: inset 0 0 0 2px var(--line); }
.cmx-card li em { margin-left: auto; font: 700 11px/1 var(--head); font-style: normal; color: var(--clay); }
.cmx-card li.soon em { color: var(--muted); }
.cmx-card-foot { display: flex; justify-content: space-between; align-items: center; padding-top: 4px; }
.cmx-card-foot span { font-size: 13px; color: var(--muted); } .cmx-card-foot b { padding: 10px 16px; border-radius: 999px; background: var(--green); color: var(--cream); font: 700 13px/1 var(--head); }

.cmx-problem { background: var(--cream); padding: 130px 0 110px; }
.cmx-big { margin: 0 auto; max-width: 20ch; text-align: center; font: 400 clamp(36px, 5vw, 68px)/1.1 'Newsreader', Georgia, serif; letter-spacing: -0.02em; color: var(--green); }
.cmx-states { display: grid; grid-template-columns: repeat(8, minmax(0, 1fr)); margin-top: 72px; border-top: 1px solid rgba(27,71,64,.16); }
.cmx-states div { padding: 22px 14px 0 0; display: grid; gap: 8px; align-content: start; }
.cmx-states b { font: 800 26px/1 var(--head); color: var(--green); letter-spacing: -0.02em; }
.cmx-states span { font-size: 13.5px; line-height: 1.35; color: var(--soft); }
.cmx-caption { margin: 22px 0 0; font: 400 18px/1.4 'Newsreader', Georgia, serif; font-style: italic; color: var(--clay); }
.cmx-why { margin-top: 64px; }

.cmx-trio { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px; margin-top: 44px; }
.cmx-tile { background: #FFFDF8; border-radius: 28px; padding: 10px 10px 28px; }
.cmx-tile h3 { margin: 24px 18px 8px; font: 800 24px/1.15 var(--head); letter-spacing: -0.02em; color: var(--green); }
.cmx-tile p { margin: 0 18px; font-size: 16px; line-height: 1.55; color: var(--soft); }
.cmx-art { height: 240px; border-radius: 22px; background: var(--peach-soft); display: grid; place-items: center; padding: 20px; }
.cmx-tile:nth-child(2) .cmx-art { background: var(--sage); } .cmx-tile:nth-child(3) .cmx-art { background: #EFE5D1; }
.cmx-mini { width: min(250px, 100%); background: #FFFDF8; border-radius: 18px; padding: 16px; display: grid; gap: 8px; box-shadow: 0 18px 34px -22px rgba(20,53,47,.45); }
.cmx-mini-k { font: 700 11.5px/1 var(--head); color: var(--clay); }
.cmx-mini-row { display: flex; justify-content: space-between; padding: 7px 0; border-top: 1px solid var(--line); font-size: 13px; }
.cmx-mini-row b { font-weight: 600; color: var(--ink); } .cmx-mini-row span { font: 700 13px/1 var(--head); color: var(--green); }
.cmx-mini-h { margin: 0; font: 800 17px/1.2 var(--head); color: var(--green); }
.cmx-mini-s { font-size: 12.5px; color: var(--muted); }
.cmx-mini-btn { margin-top: 6px; text-align: center; padding: 10px; border-radius: 999px; background: var(--green); color: var(--cream); font: 700 12.5px/1 var(--head); }
.cmx-alert { border-left: 4px solid var(--peach); }
.cmx-mini-link { margin-top: 4px; font: 700 12.5px/1 var(--head); color: var(--clay); text-decoration: underline; text-underline-offset: 3px; }

.cmx-end p { margin-bottom: 14px; }
.cmx-end-sub { display: block; text-align: center; color: var(--soft); font-size: 18px; }
.cmx-end .pg-cta { justify-content: center; margin-top: 30px; }
.solutions-home .sl-row .cm-link { color: var(--peach); }
@media (max-width: 1000px) { .cmx-states { grid-template-columns: repeat(4, minmax(0, 1fr)); row-gap: 26px; } .cmx-trio { grid-template-columns: minmax(0, 1fr); } .cmx-card { justify-self: start; } }
@media (max-width: 560px) { .cmx-states { grid-template-columns: repeat(2, minmax(0, 1fr)); } .cmx-problem { padding: 90px 0 80px; } }

.cm-infra-head { display: grid; grid-template-columns: minmax(0, 1.1fr) minmax(0, .9fr); gap: 56px; align-items: center; }
.cm-kick { color: var(--clay); }
.cm-embed { display: grid; gap: 12px; padding: 22px 24px; border-radius: 22px; background: #0F2925; color: #CFE0D7; box-shadow: 0 30px 50px -30px rgba(20,53,47,.6); min-width: 0; }
.cm-embed-k { font: 700 12.5px/1 var(--head); color: var(--peach); }
.cm-embed code { font: 500 13px/1.7 ui-monospace, 'SF Mono', Menlo, monospace; white-space: pre; overflow-x: auto; background: none; color: inherit; padding: 0; }
.cm-infra-rows { margin-top: 48px; }
#infrastructure .pg-cta { margin-top: 12px; }
@media (max-width: 900px) { .cm-infra-head { grid-template-columns: minmax(0, 1fr); gap: 32px; } }

.cm-hero h1 { max-width: 15ch; }
.cm-fine { margin-top: 18px; font-size: 14px; opacity: .8; }
.cm-sample { background: #FFFDF8; color: var(--ink, #1A1410); border-radius: 24px; padding: 24px; box-shadow: 0 30px 60px -30px rgba(0,0,0,.45); display: grid; gap: 10px; max-width: 420px; justify-self: end; width: 100%; }
.cm-sample-h { display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 6px; } .cm-sample-h b { color: var(--green); font: 700 18px/1.2 var(--head); } .cm-sample-h span { font-size: 13px; color: var(--muted); }
.cm-sample-row { display: flex; gap: 12px; align-items: center; padding: 12px 14px; border-radius: 12px; background: var(--paper, #F6F1E8); font-size: 15px; }
.cm-sample-row i { width: 12px; height: 12px; border-radius: 50%; flex: none; }
.cm-sample-row.met i { background: #3F7D5C; } .cm-sample-row.att i { background: #C4572E; } .cm-sample-row.up i { background: #C9A227; }
.cm-sample-f { display: flex; justify-content: space-between; align-items: center; margin-top: 6px; font-size: 14px; color: var(--muted); }
.cm-sample-f em { font-style: normal; font-weight: 700; padding: 8px 16px; border-radius: 999px; background: var(--green); color: var(--cream); }
.cm-steps { list-style: none; counter-reset: s; padding: 0; margin: 36px 0 0; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 18px; }
.cm-steps li { counter-increment: s; background: #FFFDF8; border-radius: 20px; padding: 26px; }
.cm-steps li::before { content: counter(s); display: grid; place-items: center; width: 36px; height: 36px; border-radius: 50%; background: var(--green); color: var(--cream); font: 700 16px/1 var(--head); margin-bottom: 16px; }
.cm-steps h3 { margin: 0; font-size: 19px; color: var(--green); } .cm-steps p { margin: 8px 0 0; color: var(--soft); font-size: 15.5px; line-height: 1.55; }
.cm-link { color: var(--peach); font-weight: 700; text-decoration: underline; text-underline-offset: 4px; }
.cm-end { text-align: center; } .cm-end .pg-lead { margin-left: auto; margin-right: auto; } .cm-end .pg-cta { justify-content: center; }
.btn-ghost-dark { border: 1.5px solid rgba(27,71,64,.35); color: var(--green); background: transparent; }
.btn-ghost-dark:hover, .btn-ghost-dark:focus-visible { background: var(--green); color: var(--cream); }
@media (max-width: 1000px) { .cm-steps { grid-template-columns: 1fr 1fr; } .cm-sample { justify-self: start; } }
@media (max-width: 620px) { .cm-steps { grid-template-columns: 1fr; } }

/* The check-up */
.cw form.cw-step { background: transparent; border-radius: 0; padding: 0; display: block; gap: 0; color: inherit; }
.cw .cw-step[hidden] { display: none !important; }
.cw form .btn { justify-self: auto; }
.cw label { color: inherit; font-size: inherit; display: inline; margin: 0; }
.cw { margin-top: 32px; background: #FFFDF8; border-radius: 28px; padding: clamp(22px, 4vw, 44px); box-shadow: 0 1px 0 rgba(27,71,64,.06); }
.cw-progress { list-style: none; display: flex; gap: 8px; padding: 0; margin: 0 0 28px; flex-wrap: wrap; }
.cw-progress li { font: 600 14px/1 var(--head); padding: 10px 14px; border-radius: 999px; background: var(--paper, #F1ECE2); color: var(--muted); }
.cw-progress li.on { background: var(--green); color: var(--cream); }
.cw-progress li.done { background: rgba(27,71,64,.12); color: var(--green); }
.cw fieldset { border: 0; padding: 18px 0; margin: 0; border-top: 1px solid rgba(27,71,64,.1); display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 8px 28px; align-items: center; }
.cw fieldset:first-of-type { border-top: 0; }
.cw legend { float: left; padding: 0; font: 600 17px/1.4 var(--head); color: var(--ink, #1A1410); }
.cw .cw-help { grid-column: 1; margin: 0; font-size: 14.5px; color: var(--muted); line-height: 1.5; }
.cw .cw-opts { grid-column: 2; grid-row: 1 / span 2; display: flex; gap: 8px; flex-wrap: wrap; justify-content: flex-end; }
.cw .cw-states { grid-column: 1 / -1; grid-row: auto; justify-content: flex-start; margin-top: 6px; }
.cw .cw-opt { position: relative; }
.cw .cw-opt input { position: absolute; opacity: 0; inset: 0; margin: 0; cursor: pointer; }
.cw .cw-opt span { display: inline-flex; align-items: center; justify-content: center; min-width: 64px; min-height: 44px; padding: 0 16px; border-radius: 999px; border: 1.5px solid rgba(27,71,64,.25); font: 600 15px/1 var(--head); color: var(--green); background: #fff; }
.cw .cw-opt input:checked + span { background: var(--green); border-color: var(--green); color: var(--cream); }
.cw .cw-opt input:focus-visible + span { outline: 3px solid var(--peach); outline-offset: 2px; }
.cw .cw-area { margin: 30px 0 4px; font-size: 13px; letter-spacing: .02em; color: var(--clay, #B5603A); font-weight: 700; }
.cw .cw-area:first-child { margin-top: 0; }
.cw .cw-ob { margin: 10px 0 2px; font: 700 18px/1.3 var(--head); color: var(--green); }
.cw .cw-nav { display: flex; justify-content: space-between; gap: 12px; margin-top: 28px; flex-wrap: wrap; }
.cw .cw-err { color: #A3381A; font-weight: 600; min-height: 1.4em; margin: 12px 0 0; }
.cw .cw-auto { font-size: 14px; color: var(--muted); margin: 4px 0 0; }
.cw-sum { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; margin: 8px 0 28px; }
.cw-sum div { border-radius: 18px; padding: 18px; background: var(--paper, #F6F1E8); }
.cw-sum b { display: block; font: 800 34px/1 var(--head); color: var(--green); } .cw-sum span { font-size: 14px; color: var(--soft); }
.cw-sum .att b { color: #A3381A; } .cw-sum .up b { color: #8A6D12; }
.cw-items { display: grid; gap: 12px; }
.cw-item { border: 1px solid rgba(27,71,64,.12); border-radius: 18px; padding: 18px 20px; }
.cw-item .cw-head { display: flex; gap: 10px; align-items: baseline; justify-content: space-between; flex-wrap: wrap; }
.cw-item h4 { margin: 0; font: 700 17px/1.35 var(--head); color: var(--ink, #1A1410); }
.cw-tag { font: 700 12.5px/1 var(--head); padding: 6px 10px; border-radius: 999px; white-space: nowrap; }
.cw-tag.met { background: #E3F0E7; color: #2D6146; } .cw-tag.attention { background: #F9E3DA; color: #8E3115; } .cw-tag.check { background: #EFEAE0; color: #5C5346; } .cw-tag.upcoming { background: #F6EDCB; color: #6E5610; }
.cw-item p { margin: 8px 0 0; font-size: 15px; line-height: 1.55; color: var(--soft); }
.cw-item ul { margin: 8px 0 0; padding-left: 20px; font-size: 15px; color: var(--soft); }
.cw-item .cw-law { font-size: 13.5px; } .cw-item .cw-law a { color: var(--green); }
.cw-item .cw-str { font-size: 13px; color: var(--muted); }
.cw-watch { margin-top: 24px; padding: 18px 20px; border-radius: 18px; background: var(--paper, #F6F1E8); font-size: 15px; }
.cw-notice { margin-top: 24px; font-size: 14px; color: var(--muted); }
@media (max-width: 720px) { .cw fieldset { grid-template-columns: 1fr; } .cw .cw-opts { grid-column: 1; grid-row: auto; justify-content: flex-start; } .cw-sum { grid-template-columns: 1fr 1fr; } }
@media print {
  body * { visibility: hidden !important; }
  #cw-report, #cw-report * { visibility: visible !important; }
  #cw-report { position: absolute; inset: 0 auto auto 0; width: 100%; }
  #cw-report .cw-nav { display: none !important; }
}
'''

_slim = {
    'version': REGISTER['version'], 'status': REGISTER['status'], 'notice': REGISTER['notice'],
    'profileQuestions': REGISTER['profileQuestions'],
    'obligations': [{k: o[k] for k in ('id', 'area', 'jurisdiction', 'title', 'summary', 'law', 'status', 'commences', 'appliesWhen', 'requiredWhen', 'recommendedOnly', 'evidence', 'guidance') if k in o} for o in REGISTER['obligations']],
}

JS = '''
// ---------------------------------------------------------------- Always Compliance check-up
(() => {
  const R = __COMPLIANCE__;
  const root = document.getElementById('cw'); if (!root) return;
  const pf = document.getElementById('cw-profile'), ev = document.getElementById('cw-evidence'), rep = document.getElementById('cw-report');
  const STATES = ['NSW', 'VIC', 'QLD', 'WA', 'SA', 'TAS', 'ACT', 'NT'];
  const AREA = { privacy: 'Privacy', child_safety: 'Child safety', charity: 'Charity', messages: 'Emails and texts' };
  const LABEL = { met: 'Done', attention: 'Needs attention', check: 'To check', upcoming: 'Coming' };
  const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
  let profile = {}, answers = {};

  // Same logic as @always/core assess(): see always-platform/packages/core/src/compliance.ts
  const holds = (c, p) => {
    if (!c) return true;
    if (c.all) return c.all.every((x) => holds(x, p));
    if (c.any) return c.any.some((x) => holds(x, p));
    if (c.not) return !holds(c.not, p);
    if (c.includesAny) return c.field === 'states' && c.includesAny.some((s) => (p.states || []).includes(s));
    if ('is' in c) return p[c.field] === c.is;
    return false;
  };
  const strength = (o, p) => o.recommendedOnly ? 'recommended' : (holds(o.requiredWhen, p) ? 'required' : 'recommended');
  function assess(p, a, asOf) {
    const items = [], watching = [];
    for (const o of R.obligations) {
      if (!holds(o.appliesWhen, p)) continue;
      if (o.status === 'watch') { watching.push(o); continue; }
      const missing = [], unanswered = [];
      for (const e of o.evidence.filter((e) => holds(e.onlyWhen, p))) {
        if (e.kind === 'platform') continue; // Always does this when you use it
        const v = a[e.id];
        if (v === 'no') missing.push(e.prompt); else if (v !== 'yes' && v !== 'not_applicable') unanswered.push(e.prompt);
      }
      const notYet = o.status === 'upcoming' && (!o.commences || new Date(o.commences + 'T00:00:00+10:00') > asOf);
      const status = notYet ? 'upcoming' : missing.length ? 'attention' : unanswered.length ? 'check' : 'met';
      const law = o.jurisdiction === 'STATES' ? (o.law.filter((l) => !l.jurisdiction || p.states.includes(l.jurisdiction)).length ? o.law.filter((l) => !l.jurisdiction || p.states.includes(l.jurisdiction)) : o.law) : o.law;
      items.push({ o, status, strength: strength(o, p), missing, unanswered, law, platform: o.evidence.some((e) => e.kind === 'platform') });
    }
    const order = { attention: 0, check: 1, upcoming: 2, met: 3 };
    items.sort((x, y) => order[x.status] - order[y.status] || (x.strength === y.strength ? 0 : x.strength === 'required' ? -1 : 1));
    return { items, watching };
  }

  const yn = (name, value) => ['yes', 'no'].map((v) => `<label class="cw-opt"><input type="radio" name="${name}" value="${v}" ${value === v ? 'checked' : ''}><span>${v === 'yes' ? 'Yes' : 'No'}</span></label>`).join('');
  const ynu = (name, value) => [['yes', 'Yes'], ['no', 'No'], ['unsure', 'Not sure']].map(([v, t]) => `<label class="cw-opt"><input type="radio" name="${name}" value="${v}" ${value === v ? 'checked' : ''}><span>${t}</span></label>`).join('');

  function step(n) {
    root.querySelectorAll('.cw-step').forEach((s) => (s.hidden = s.dataset.step !== String(n)));
    root.querySelectorAll('.cw-progress li').forEach((li) => { const k = Number(li.dataset.step); li.className = k === n ? 'on' : k < n ? 'done' : ''; li.toggleAttribute('aria-current', k === n); });
    const target = n === 3 ? rep : root.querySelector(`.cw-step[data-step="${n}"]`);
    root.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
    const f = target.querySelector('input, button'); (n === 3 ? target : f)?.focus({ preventScroll: true });
  }

  function renderProfile() {
    pf.innerHTML = R.profileQuestions.map((q) => q.type === 'states'
      ? `<fieldset><legend>${esc(q.label)}</legend><p class="cw-help">${esc(q.help)}</p><div class="cw-opts cw-states">${STATES.map((s) => `<label class="cw-opt"><input type="checkbox" name="states" value="${s}" ${(profile.states || []).includes(s) ? 'checked' : ''}><span>${s}</span></label>`).join('')}</div></fieldset>`
      : `<fieldset><legend>${esc(q.label)}</legend><p class="cw-help">${esc(q.help)}</p><div class="cw-opts">${yn(q.id, profile[q.id] === undefined ? '' : profile[q.id] ? 'yes' : 'no')}</div></fieldset>`).join('') +
      '<p class="cw-err" id="cw-err1" role="alert"></p><div class="cw-nav"><span></span><button class="btn btn-peach" type="submit">Next: what you do</button></div>';
  }

  pf.addEventListener('submit', (e) => {
    e.preventDefault();
    const fd = new FormData(pf), p = { states: fd.getAll('states') };
    const missing = [];
    for (const q of R.profileQuestions) if (q.type === 'boolean') { const v = fd.get(q.id); if (!v) missing.push(q.label); p[q.id] = v === 'yes'; }
    if (!p.states.length) missing.unshift('Where do you run activities?');
    const err = document.getElementById('cw-err1');
    if (missing.length) { err.textContent = `Please answer ${missing.length === 1 ? 'one more question' : missing.length + ' more questions'}, starting with: ${missing[0]}`; return; }
    err.textContent = ''; profile = p; renderEvidence(); step(2);
  });

  function renderEvidence() {
    const { items } = assess(profile, {}, new Date());
    let html = '', lastArea = '';
    for (const it of items) {
      const qs = it.o.evidence.filter((e) => e.kind !== 'platform' && holds(e.onlyWhen, profile));
      if (!qs.length && !it.platform) continue;
      if (it.o.area !== lastArea) { html += `<p class="cw-area">${AREA[it.o.area]}</p>`; lastArea = it.o.area; }
      html += `<p class="cw-ob">${esc(it.o.title)}</p>`;
      if (it.platform) html += `<p class="cw-auto">Always does part of this for you when you use it.</p>`;
      html += qs.map((e) => `<fieldset><legend>${esc(e.prompt)}</legend><div class="cw-opts">${ynu(e.id, answers[e.id] || '')}</div></fieldset>`).join('');
    }
    ev.innerHTML = (html || '<p>Nothing to ask: no obligations in this check-up apply to what you told us.</p>') +
      '<div class="cw-nav"><button class="btn btn-ghost-dark" type="button" data-back>Back</button><button class="btn btn-peach" type="submit">See my results</button></div>';
  }
  ev.addEventListener('click', (e) => { if (e.target.closest('[data-back]')) step(1); });
  ev.addEventListener('submit', (e) => {
    e.preventDefault();
    const fd = new FormData(ev); answers = {};
    for (const [k, v] of fd.entries()) answers[k] = v;
    renderReport(); step(3);
  });

  function renderReport() {
    const { items, watching } = assess(profile, answers, new Date());
    const n = (s) => items.filter((i) => i.status === s).length;
    const card = (it) => `<article class="cw-item"><div class="cw-head"><h4>${esc(it.o.title)}</h4><span class="cw-tag ${it.status}">${LABEL[it.status]}${it.status === 'upcoming' && it.o.commences ? ' ' + new Date(it.o.commences).toLocaleDateString('en-AU', { month: 'long', year: 'numeric' }) : ''}</span></div>
      <p class="cw-str">${it.strength === 'required' ? 'Required for your ministry' : 'Good practice for your ministry'}</p>
      <p>${esc(it.o.summary)}</p>
      ${it.missing.length ? `<ul>${it.missing.map((m) => `<li>Not yet: ${esc(m)}</li>`).join('')}</ul>` : ''}
      ${it.unanswered.length && it.status !== 'upcoming' ? `<ul>${it.unanswered.map((m) => `<li>To check: ${esc(m)}</li>`).join('')}</ul>` : ''}
      ${it.status !== 'met' ? `<p><b>What to do:</b> ${esc(it.o.guidance)}</p>` : ''}
      <p class="cw-law">Source: ${it.law.map((l) => `<a href="${esc(l.url)}" target="_blank" rel="noopener">${esc(l.name)}</a>`).join(', ')}</p></article>`;
    rep.innerHTML = `<h3 class="pg-h" style="font-size:28px;margin:0 0 8px">Your check-up</h3>
      <p class="pg-lead" style="margin:0 0 20px">${items.length} obligations apply to your ministry. Here is where you stand today.</p>
      <div class="cw-sum"><div class="att"><b>${n('attention')}</b><span>Need attention</span></div><div><b>${n('check')}</b><span>To check</span></div><div class="up"><b>${n('upcoming')}</b><span>Coming</span></div><div><b>${n('met')}</b><span>Done</span></div></div>
      <div class="cw-items">${items.map(card).join('')}</div>
      ${watching.length ? `<div class="cw-watch"><b>On the horizon.</b> ${watching.map((w) => esc(w.summary)).join(' ')}</div>` : ''}
      <p class="cw-notice">Register ${esc(R.version)} (${esc(R.status)}). ${esc(R.notice)} Nothing you entered has been sent or saved.</p>
      <div class="cw-nav"><button class="btn btn-ghost-dark" type="button" data-edit>Change my answers</button><span style="display:flex;gap:10px;flex-wrap:wrap"><button class="btn btn-ghost-dark" type="button" data-print>Print or save as PDF</button><a class="btn btn-peach" href="#/contact/compliance">Get this every quarter</a></span></div>`;
  }
  rep.addEventListener('click', (e) => { if (e.target.closest('[data-edit]')) step(2); if (e.target.closest('[data-print]')) window.print(); });

  renderProfile();
})();

// Join links that set the interest
document.addEventListener('click', (e) => {
  const a = e.target.closest('[data-join-interest]'); if (!a) return;
  setTimeout(() => window.alwaysSetInterest?.(a.dataset.joinInterest), 50);
});
'''.replace('__COMPLIANCE__', json.dumps(_slim, ensure_ascii=False))

# ---------------------------------------------------------------- Docs

def _register_table():
    rows = []
    area_name = {k: v[0] for k, v in AREAS.items()}
    for o in REGISTER['obligations']:
        status = {'in_force': 'In force', 'upcoming': f"From {o.get('commences', '')}", 'watch': 'Watching'}[o['status']]
        where = 'Australia' if o['jurisdiction'] == 'CTH' else ('By state' if o['jurisdiction'] == 'STATES' else o['jurisdiction'])
        law = ', '.join(f'<a href="{escape(l["url"])}" target="_blank" rel="noopener">{escape(l["name"])}</a>' for l in o['law'][:2]) + (' and others' if len(o['law']) > 2 else '')
        rows.append(f'<tr><td><b>{escape(o["title"])}</b><br><span class="dt-sub">{escape(o["summary"])}</span></td><td>{area_name[o["area"]]}</td><td>{where}</td><td>{status}</td><td>{law}</td></tr>')
    return '<div class="dt-wrap"><table class="dt"><thead><tr><th>Obligation</th><th>Area</th><th>Where</th><th>Status</th><th>Source</th></tr></thead><tbody>' + ''.join(rows) + '</tbody></table></div>'

DOCS = ("Always Compliance", [
  ("compliance-overview", "Always Compliance", f"""
<p class="lead">Always Compliance helps churches and Christian ministries stay on top of privacy, child safety, charity and messaging rules, with a check-up every quarter and plain-English updates when the law changes.</p>
<div class="callout">Always Compliance is a guide to common obligations. It is not legal advice. For advice about your situation, talk to a lawyer.</div>
<h2>What you get</h2>
<ul>
<li><b>A clear picture.</b> Which rules apply to you, based on where you work and what you do.</li>
<li><b>A quarterly check-up.</b> Ready for you each quarter. A person at your ministry reviews and approves it, ready for your board.</li>
<li><b>Updates when the law changes.</b> We watch official sources every day. A qualified reviewer checks every change before it reaches you.</li>
<li><b>Help where it counts.</b> Each item says what to do next and links to the official source.</li>
</ul>
<h2>Get started</h2>
<ol>
<li>Try the <a href="#/compliance/check">free check-up</a>. It takes about ten minutes, and nothing is saved.</li>
<li><a href="#/join">Join Always</a> as a church or ministry.</li>
<li>Sign in to Always and open <b>Compliance</b>, answer the profile questions and save your answers.</li>
<li>Each quarter, review your check-up, update anything that has changed, and approve it.</li>
</ol>
<h2>What the results mean</h2>
<table class="dt"><thead><tr><th>Result</th><th>Meaning</th></tr></thead><tbody>
<tr><td>Done</td><td>Everything we asked about is in place.</td></tr>
<tr><td>Needs attention</td><td>You answered "no" to something. The item says what to do.</td></tr>
<tr><td>To check</td><td>Something is unanswered or you weren't sure.</td></tr>
<tr><td>Coming</td><td>A new rule that starts soon, so you can prepare.</td></tr>
</tbody></table>
<p>Each item is either <b>required</b> for your ministry or <b>good practice</b>. For example, many small churches aren't covered by the Privacy Act, but anyone can be sued for a serious invasion of privacy, so the privacy items still matter.</p>
<h2>What Always does for you</h2>
<p>If you use Always for response cards and contact details, some evidence is filled in automatically, because Always Platform enforces it in code: consent records, access controls, a deletion schedule, age rules for young people, and keeping details in Australia.</p>
<h2>Privacy</h2>
<p>Always Compliance stores facts about your organisation and your answers. It doesn't store anyone's personal details. Only your team can see your answers.</p>
"""),
  ("compliance-register", "Every obligation", f"""
<p class="lead">The list of obligations Always Compliance checks. It's open data under CC BY 4.0: anyone can use it.</p>
<p>Version <b>{escape(REGISTER['version'])}</b>, as of {escape(REGISTER['asOf'])}. Status: <b>{escape(REGISTER['status'])}</b>. {escape(REGISTER['notice'])}</p>
{_register_table()}
<p>Download the full register as JSON from the <a href="https://github.com/alwaysfoundation/always-platform/blob/main/spec/compliance/register.json">always-platform repository</a>, or call <code>GET /v1/compliance/register</code>.</p>
"""),
  ("compliance-review", "How we keep it right", """
<p class="lead">Every obligation is checked by a person before it reaches you.</p>
<ol>
<li><b>We watch official sources.</b> Every day, Always checks pages from the OAIC, ACNC, ACMA, legislation registers and state child safety regulators for changes.</li>
<li><b>We write it up.</b> When something changes, the foundation team writes a plain-English summary of what changed and what it means.</li>
<li><b>A person decides.</b> The foundation team reviews each change. A qualified reviewer approves every new version of the register, and their name is recorded.</li>
<li><b>You hear about it.</b> Your next check-up uses the new version, and the change feed explains what changed.</li>
</ol>
<div class="callout">Found something wrong or missing? <a href="#/feedback">Tell us</a>. We read every message.</div>
"""),
  ("compliance-api", "Compliance API", """
<p class="lead">Use the register and the check-up in your own tools. The register is public; member data needs sign-in.</p>
<h2>Public</h2>
<table class="dt"><thead><tr><th>Call</th><th>What it does</th></tr></thead><tbody>
<tr><td><code>GET /v1/compliance/register</code></td><td>The latest published register, with an ETag</td></tr>
<tr><td><code>GET /v1/compliance/register/versions</code></td><td>Every published version</td></tr>
<tr><td><code>GET /v1/compliance/register/{version}</code></td><td>One version. It never changes.</td></tr>
<tr><td><code>GET /v1/compliance/changes</code></td><td>What changed between versions, newest first</td></tr>
<tr><td><code>POST /v1/compliance/check</code></td><td>A check-up from a profile and answers. Nothing is stored.</td></tr>
</tbody></table>
<pre><code>curl -X POST https://api.alwaysfoundation.org/v1/compliance/check \\
  -H 'content-type: application/json' \\
  -d '{"profile":{"states":["NSW"],"collectsPersonalInfo":true,"turnoverOver3m":false,
       "providesHealthService":false,"usesOverseasServices":false,"worksWithChildren":true,
       "onlineServicesForChildren":false,"sendsEmailOrSms":true,"acncRegistered":true,
       "basicReligiousCharity":true,"acncMediumOrLarge":false},
       "answers":{"wwcc-register":"yes"}}'</code></pre>
<h2>Members</h2>
<p>Sign in as an admin, or use a token with the <code>compliance</code> scope.</p>
<table class="dt"><thead><tr><th>Call</th><th>What it does</th></tr></thead><tbody>
<tr><td><code>GET /v1/compliance/profile</code> and <code>PUT</code></td><td>Your organisation's profile and answers</td></tr>
<tr><td><code>PUT /v1/compliance/answers</code></td><td>Save answers to evidence questions</td></tr>
<tr><td><code>GET /v1/compliance/assessment</code></td><td>Your live assessment</td></tr>
<tr><td><code>GET /v1/compliance/assessments</code></td><td>Your quarterly assessments</td></tr>
<tr><td><code>POST /v1/compliance/assessments/{id}/approve</code></td><td>Approve a quarterly assessment. A signed-in person only.</td></tr>
</tbody></table>
<p>The engine is also in the open-source <code>@always/core</code> package as <code>assess()</code>.</p>
"""),
  ("compliance-platforms", "For platforms", """
<p class="lead">Build Always Compliance into your own product. The register, the check-up and the embed are free and need no sign-in. Change alerts need an Always account.</p>
<h2>Embed the check-up</h2>
<pre><code>&lt;script type="module" src="https://cdn.alwaysfoundation.org/sdk/v0/compliance-widget.js"&gt;&lt;/script&gt;
&lt;always-compliance-check accent="#5B67D8"&gt;&lt;/always-compliance-check&gt;</code></pre>
<p>Answers stay in the browser and nothing is stored. Listen for the <code>always-compliance-result</code> event to see the totals.</p>
<h2>Hear when the rules change</h2>
<p>Add a webhook endpoint as an admin, or with a token that has the <code>webhooks</code> scope. Keep the secret it returns: it is shown once.</p>
<pre><code>curl -X POST https://api.alwaysfoundation.org/v1/webhooks \\
  -H "authorization: Bearer $ALWAYS_TOKEN" -H "x-always-org: $ORG_ID" \\
  -H 'content-type: application/json' \\
  -d '{"url":"https://your-app.example/hooks/always",
       "events":["always.compliance.obligations.affected"]}'</code></pre>
<table class="dt"><thead><tr><th>Event</th><th>When</th></tr></thead><tbody>
<tr><td><code>always.compliance.register.published</code></td><td>A new version is published, with what changed</td></tr>
<tr><td><code>always.compliance.obligations.affected</code></td><td>A change affects obligations that apply to you</td></tr>
</tbody></table>
<p>Deliveries are signed CloudEvents. Check each one with <code>verifyWebhook</code> from <code>@always/sdk</code>. They carry register facts, never people's details.</p>
<h2>Compliant by default</h2>
<pre><code>import { ageGuard, requireConsent, personalDataProblems, spamActProblems } from '@always/sdk';

if (!ageGuard(person.ageBand).aiAllowed) skipAi();   // no AI for under-18s
requireConsent(person.consent, 'connect.church');    // throws without consent
personalDataProblems(notificationText);              // [] when there are no emails or phone numbers
spamActProblems({ consented, sender, unsubscribeUrl, body });</code></pre>
<p>These are the rules Always Platform itself runs on. They help with common obligations; they are not legal advice.</p>
"""),
])
