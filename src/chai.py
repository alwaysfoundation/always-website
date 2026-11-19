"""Story: Nathan Gaw's Christians in AI (CHAI) talk on Branches, now Always Connect."""

BRANCH = '''<svg class="chai-art" viewBox="0 0 400 250" aria-hidden="true"><rect width="400" height="250" fill="#1B4740"/>
<path class="chai-b" d="M40 210 C120 200 170 170 210 125 S300 60 360 50" fill="none" stroke="#E8A577" stroke-width="5" stroke-linecap="round"/>
<path class="chai-b" d="M150 182 C160 150 150 125 128 104" fill="none" stroke="#8FB5A5" stroke-width="4" stroke-linecap="round"/>
<path class="chai-b" d="M245 98 C262 120 290 128 318 124" fill="none" stroke="#8FB5A5" stroke-width="4" stroke-linecap="round"/>
<circle cx="128" cy="104" r="9" fill="#F8F3EA"/><circle cx="318" cy="124" r="9" fill="#F8F3EA"/><circle cx="360" cy="50" r="11" fill="#E8A577"/><circle cx="40" cy="210" r="7" fill="#F8F3EA"/>
<text x="36" y="58" fill="#F8F3EA" font-family="inherit" font-size="34" font-weight="800" letter-spacing="-1">CHAI</text>
<text x="36" y="84" fill="#CFE0D6" font-family="inherit" font-size="15">Christians in AI</text></svg>'''

BRANCH_WIDE = '''<svg class="chai-art" viewBox="0 0 800 350" aria-hidden="true"><rect width="800" height="350" fill="#1B4740"/>
<path class="chai-b" d="M300 300 C420 290 480 250 540 190 S650 90 740 70" fill="none" stroke="#E8A577" stroke-width="6" stroke-linecap="round"/>
<path class="chai-b" d="M440 272 C455 230 440 196 410 168" fill="none" stroke="#8FB5A5" stroke-width="5" stroke-linecap="round"/>
<path class="chai-b" d="M585 150 C605 180 645 192 685 186" fill="none" stroke="#8FB5A5" stroke-width="5" stroke-linecap="round"/>
<circle cx="410" cy="168" r="11" fill="#F8F3EA"/><circle cx="685" cy="186" r="11" fill="#F8F3EA"/><circle cx="740" cy="70" r="14" fill="#E8A577"/><circle cx="300" cy="300" r="9" fill="#F8F3EA"/>
<text x="60" y="110" fill="#F8F3EA" font-family="inherit" font-size="64" font-weight="800" letter-spacing="-2">CHAI</text>
<text x="62" y="150" fill="#CFE0D6" font-family="inherit" font-size="24">Christians in AI</text></svg>'''

PAGE = '''
<article class="ft">
<div class="ft-hero"><div class="wrap ft-hero-in">
  <p class="ft-kick"><a href="#/stories">Stories</a> <span aria-hidden="true">/</span> Christians in AI (CHAI)</p>
  <h1>Branches: walking with new believers from decision to discipleship</h1>
  <p class="ft-dek">At Christians in AI, Nathan Gaw shares the story of Branches, which evolved into Always Connect.</p>
</div></div>

<figure class="ft-fig wrap chai-fig">
  <img src="{{BRANCHES_IMG}}" alt="Branches: the global Gospel response network. Open source infrastructure for what happens after someone responds to the Gospel." width="1267" height="678" loading="lazy">
  <figcaption>Branches evolved into Always Connect.</figcaption>
</figure>

<div class="wrap ft-body">
  <div class="prose ft-prose">
    <p class="ft-lead">Every week people say yes to Jesus at events, online and in everyday conversations. Many never find their way into a local church. Branches was built for that moment.</p>

    <p>Christians in AI (CHAI) is a global community united by their interest in the intersection of Christianity and AI, stewarding its development and application for the glory of Jesus Christ. It is a fitting place to ask how AI can serve new believers well.</p>

    <h2>What Branches does</h2>
    <p>Branches meets people the moment they respond, with a simple QR code or link. It asks for their consent, then connects them to a church, a Bible reading plan or a mentor, and follows up so no one slips through the cracks.</p>

    <h2>From Branches to Always Connect</h2>
    <p>Branches evolved into <a href="#/connect">Always Connect</a>.</p>

    <blockquote class="ft-pull">AI can help ministries care for people. It should never replace the relationships that matter most.</blockquote>

    <h2>What we learned with ministry partners</h2>
    <p>Branches was built alongside ministry partners, and trialled at a youth event with UEN. Its agent checked each response and handed it to a person before anything was shared. That pattern, an agent doing the admin and a person making every decision, is how <a href="#/docs/always-agent">agents</a> work in Always Connect today.</p>

    <h2>How AI helps, and where it stops</h2>
    <ul>
      <li>Agents check new responses, remind teams who is waiting, and draft a first message for a person to edit and send.</li>
      <li>A person approves every action that affects someone who responded.</li>
      <li>No AI ever touches a young person's information.</li>
      <li>No one's information is used to train AI.</li>
    </ul>

    <h2>Find out more</h2>
    <p>Read about <a href="#/connect">Always Connect</a>, or <a href="#/join">join Always</a> to use it with your church or ministry.</p>
  </div>

  <aside class="ft-side" aria-label="At a glance">
    <div class="ft-card">
      <img class="chai-logo" src="{{CHAI_LOGO}}" alt="Christians in AI (ChAI) logo" width="240" height="180">
      <h2>At a glance</h2>
      <dl>
        <dt>Talk</dt><dd>Branches: Walking with New Believers from Decision to Discipleship</dd>
        <dt>Speaker</dt><dd>Nathan Gaw</dd>
        <dt>Community</dt><dd>Christians in AI (CHAI), a global community stewarding AI for the glory of Jesus Christ</dd>
        <dt>Today</dt><dd>Branches evolved into Always Connect</dd>
      </dl>
      <a class="btn btn-peach" href="#/connect">See Always Connect</a>
      <a class="ft-link" href="#/docs/always-agent">How agents work</a>
    </div>
  </aside>
</div>
</article>
'''

CSS = '''
.chai-fig img { border-radius: 26px; }
.ft-card .chai-logo { display: block; width: 140px; height: auto; margin: -6px 0 12px -10px; mix-blend-mode: multiply; }
.cs-img.ptr-tile { display: flex; flex-direction: column; justify-content: flex-end; gap: 6px; padding: 28px; background: linear-gradient(150deg, #E7F0EA, #CFE2D6); color: var(--green); }
.cs-img.ptr-tile-night { background: linear-gradient(150deg, #22302B, #34463F); color: #F8F3EA; }
.ptr-tile-mono { display: grid; place-items: center; width: 72px; height: 72px; margin-bottom: auto; border-radius: 22px; background: var(--green); color: var(--cream); font: 800 24px/1 var(--head); }
.ptr-tile-night .ptr-tile-mono { background: #F8D486; color: #1E2A26; }
.ptr-tile-k { font: 600 14px/1 var(--head); color: var(--clay, #B55A2E); } .ptr-tile-night .ptr-tile-k { color: #F2B98E; }
.ptr-tile-n { font: 800 clamp(26px, 2.6vw, 34px)/1.05 var(--head); letter-spacing: -.02em; }
.cs-img.jn-tile { background: radial-gradient(70% 60% at 85% 0%, rgba(232,165,119,.25), rgba(232,165,119,0) 60%), linear-gradient(160deg, #1D4C43, #12302A); display: grid; place-items: center; }
.cs-img .jn-art { position: absolute; top: 7%; right: 5%; width: min(48%, 360px); height: auto; transition: transform 1.2s cubic-bezier(.2,.7,.2,1); }
.cs-tile:hover .cs-img .jn-art { transform: scale(1.04); }
@media (max-width: 700px) { .cs-img .jn-art { width: 78%; right: 11%; top: 5%; } }
.cs-img.chai-tile { background: #fff; display: grid; place-items: center; }
.cs-img.chai-tile img { width: 70%; height: auto; object-fit: contain; }
.cs-tile:hover .cs-img.chai-tile img { transform: scale(1.03); }
.chai-fig .chai-art { display: block; width: 100%; height: auto; aspect-ratio: 800 / 350; border-radius: 26px; box-shadow: 0 40px 80px -40px rgba(10,30,26,.45); }
.cs-img .chai-art { width: 100%; height: 100%; display: block; }
.chai-b { stroke-dasharray: 1000; animation: chaiGrow 2.2s cubic-bezier(.3,.6,.2,1) .3s both; }
@keyframes chaiGrow { from { stroke-dashoffset: 1000; } }
@media (prefers-reduced-motion: reduce) { .chai-b { animation: none; } }
'''

TILE = '''      <li class="cs-tile">
        <div class="cs-img chai-tile"><img src="{{CHAI_LOGO}}" alt="Christians in AI (ChAI) logo" loading="lazy"></div>
        <div class="cs-text">
          <p class="cs-name">Christians in AI (CHAI)</p>
          <h3>From decision to discipleship.</h3>
          <p>Nathan Gaw on Branches, which evolved into Always Connect.</p>
          <a class="cs-more" href="#/chai">Read the story</a>
        </div>
      </li>
'''
