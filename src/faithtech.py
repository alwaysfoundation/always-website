"""Story: Always Platform as a free integration for FaithTech Australia and wider builders."""

PAGE = '''
<article class="ft">
<div class="ft-hero"><div class="wrap ft-hero-in">
  <p class="ft-kick"><a href="#/stories">Stories</a> <span aria-hidden="true">/</span> For builders and founders</p>
  <h1>Open to every builder: Always Platform and FaithTech Australia</h1>
  <p class="ft-dek">Always Platform is freely available to FaithTech Australia, and to Christian builders and founders everywhere, as an integration they can plug straight into.</p>
</div></div>

<figure class="ft-fig wrap">
  <img src="{{FAITHTECH_IMG}}" alt="FaithTech: a global tech community for Christ. Two young men talking at a FaithTech gathering." width="1731" height="909" loading="lazy">
  <figcaption>Image: FaithTech, used with permission.</figcaption>
</figure>

<div class="wrap ft-body">
  <div class="prose ft-prose">
    <p class="ft-lead">FaithTech is a global tech community for Christ: developers, designers and founders who build for the Kingdom. In Australia, that community is full of people with good ideas for helping someone take a next step with Jesus. Most of them run into the same hard parts before they get to the idea itself.</p>

    <h2>The parts every team rebuilds</h2>
    <p>Build anything that cares for a person who has responded to Jesus and you meet the same questions. How do you record their consent, and honour it when they change their mind? What happens if they're 14? Where is their data kept? Which local church is ready to welcome them, and how do you hand them on safely? Which privacy and child safety rules apply to your ministry?</p>
    <p>None of it is the reason anyone starts a project. All of it has to be right. Always Platform exists so that a weekend team or a first-time founder doesn't have to solve it alone.</p>

    <h2>What's open to builders</h2>
    <ul>
      <li><b>Always Compliance</b>, live now. A check-up for privacy, child safety, charity and messaging rules, as a hosted API and a drop-in widget. Nothing about the person using it is stored.</li>
      <li><b>Church feed and finder.</b> Verified churches near a postcode, and whether they are welcoming now, for your site, app or AI tool.</li>
      <li><b>Response pages and handoff.</b> Pass a consenting person to a local church through the API and SDK, with consent attached.</li>
      <li><b>MCP server.</b> Let an AI assistant find churches and explain Always Platform accurately, using public information only.</li>
      <li><b>Webhooks</b> for the moments that matter, carrying ids only, never personal details.</li>
    </ul>
    <p>Compliance is live today. The rest opens to builders as the Always API launches; the <a href="#/developers">Developers</a> page shows what's ready.</p>

    <blockquote class="ft-pull">Builders use Always Platform on the same terms as everyone else: free, open source, with no special rights for anyone.</blockquote>

    <h2>Free, and open</h2>
    <p>There is no fee to integrate. The code is open source under Apache 2.0 and the docs are CC BY 4.0, so you can read exactly how it works, improve it, or run it yourself. Commercial builders are welcome, on the same terms as everyone else.</p>

    <h2>What stays the same, whoever builds</h2>
    <p>The promises to people don't change from one app to the next. Consent travels with a person's details and is checked before anything is shared. The rules for young people are built in and can't be switched off, and no AI touches their information. Personal data stays in Australia. When you build on Always Platform, your users get those promises without you having to write them.</p>

    <h2>What it could look like</h2>
    <p>A few examples of how a team might use it:</p>
    <ul>
      <li>A prayer or Bible app adds "Find a church near me" in a line of code.</li>
      <li>A youth events tool checks its compliance before its first event.</li>
      <li>An outreach app hands every yes to a verified local church, with consent, instead of a spreadsheet.</li>
    </ul>

    <h2>Start building</h2>
    <p>Bring an idea to a FaithTech gathering, a hackathon, or your own weekend. Read the <a href="#/docs/compliance-api">Compliance API docs</a>, look through <a href="#/developers">Developers</a>, or register as a tech platform and we'll help you get set up.</p>
  </div>

  <aside class="ft-side" aria-label="At a glance">
    <div class="ft-card">
      <h2>At a glance</h2>
      <dl>
        <dt>For</dt><dd>FaithTech Australia, and Christian builders and founders everywhere</dd>
        <dt>Cost</dt><dd>Free</dd>
        <dt>Licence</dt><dd>Apache 2.0 code, CC BY 4.0 docs</dd>
        <dt>Live now</dt><dd>Always Compliance API and widget</dd>
        <dt>Data</dt><dd>Kept in Australia</dd>
      </dl>
      <a class="btn btn-peach" href="#/join/platform">Register as a tech platform</a>
      <a class="ft-link" href="#/developers">See the Developers page</a>
    </div>
  </aside>
</div>
</article>
'''

CSS = '''
.ft-hero { background: var(--green); color: var(--cream); padding: 168px 0 132px; }
.ft-hero-in { max-width: 920px; }
.ft-kick { margin: 0 0 22px; font: 700 15px/1.3 var(--head); color: var(--peach); }
.ft-kick a { color: inherit; text-decoration: none; } .ft-kick a:hover { text-decoration: underline; } .ft-kick span { margin: 0 6px; opacity: .6; }
.ft-hero h1 { font-size: clamp(38px, 5vw, 68px); letter-spacing: -0.04em; line-height: 1.02; color: var(--cream); }
.ft-dek { margin: 24px 0 0; max-width: 640px; font: 400 clamp(20px, 2vw, 24px)/1.45 'Newsreader', Georgia, serif; color: var(--on-green); }
.ft-fig { margin: -84px auto 0; position: relative; }
.ft-fig img { display: block; width: 100%; height: auto; border-radius: 26px; box-shadow: 0 40px 80px -40px rgba(10,30,26,.45); background: #fff; }
.ft-fig figcaption { margin-top: 12px; font-size: 13px; color: var(--muted); }
.ft-body { display: grid; grid-template-columns: minmax(0, 1fr) 300px; gap: 72px; padding-top: 64px; padding-bottom: 120px; align-items: start; }
.ft-prose { max-width: 680px; }
.ft-prose .ft-lead { font: 400 22px/1.55 'Newsreader', Georgia, serif; color: var(--ink); }
.ft-prose h2 { font-size: 27px; margin-top: 52px; color: var(--green); }
.ft-prose p, .ft-prose li { font-size: 18px; line-height: 1.7; }
.ft-pull { margin: 52px 0; padding: 0 0 0 24px; border-left: 3px solid var(--peach); font: 400 clamp(24px, 2.4vw, 30px)/1.35 'Newsreader', Georgia, serif; color: var(--green); }
.ft-side { position: sticky; top: 104px; }
.ft-card { padding: 28px 26px; border-radius: 26px; background: var(--sage); }
.ft-card h2 { margin: 0 0 16px; font: 800 20px/1.2 var(--head); color: var(--green); }
.ft-card dl { margin: 0 0 22px; display: grid; gap: 12px; }
.ft-card dt { font: 700 13.5px/1.2 var(--head); color: var(--clay); }
.ft-card dd { margin: 2px 0 0; font-size: 15px; line-height: 1.45; color: var(--ink); }
.ft-card .btn { display: flex; justify-content: center; width: 100%; }
.ft-link { display: block; margin-top: 14px; text-align: center; font-weight: 600; color: var(--green); }
@media (max-width: 1000px) { .ft-body { grid-template-columns: minmax(0, 1fr); gap: 40px; } .ft-side { position: static; } }
@media (max-width: 640px) { .ft-hero { padding: 128px 0 96px; } .ft-fig { margin-top: -60px; } .ft-fig img { border-radius: 18px; } }
'''

TILE = '''      <li class="cs-tile">
        <div class="cs-img"><img src="{{FAITHTECH_IMG}}" alt="FaithTech: a global tech community for Christ" loading="lazy" style="object-position:0 50%"></div>
        <div class="cs-text">
          <p class="cs-name">FaithTech Australia</p>
          <h3>Open to every builder.</h3>
          <p>Always Platform is freely available to FaithTech Australia and wider builders and founders, as an integration.</p>
          <a class="cs-more" href="#/faithtech">Read the story</a>
        </div>
      </li>
'''
