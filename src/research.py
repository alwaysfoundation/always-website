"""Research case study: record linkage across ministries, designed and not used."""

SLUG = 'pprl'
TITLE = 'Why we don’t link people across ministries · Always Foundation'

STEPS = [
    ('Consent', 'A separate consent purpose, <code>share.journey</code>, checked on every read. Adults only.',
     'The person says yes to this on its own, apart from being introduced to a church. Anyone under 18 is never included.'),
    ('Scramble the number', 'The mobile is normalised to +61 format and run through HMAC-SHA256 with a secret key held in a key management service.',
     'Their phone number becomes a code, using a secret key. It works like one-way encryption: without the key, no one can turn the code back into the number.'),
    ('A different code for each ministry', 'A second key derives a separate pseudonym for each organisation, so two ministries&rsquo; exports cannot be joined.',
     'Each ministry sees a different code for the same person, so two ministries can&rsquo;t compare lists and find them.'),
    ('Only milestones, by month', 'Milestones only (responded, introduced, welcomed, first conversation, connected), under row-level security. Withdrawing consent unlinks the person through a database trigger.',
     'Ministries would see steps like &ldquo;welcomed by a church&rdquo;, with no names or notes. Saying stop removes the link straight away.'),
]

RISKS = [
    ('The key', 'Whoever holds the secret key can turn any phone number into its code. One leaked or misused key exposes everyone, past and future.'),
    ('Only 100 million numbers', 'Australian mobiles are 04 plus eight digits. With the key, a computer can try every number in minutes and reverse every code.'),
    ('Patterns give people away', 'Even without the key, &ldquo;youth event in March, course in May, church in Penrith in July&rdquo; can point to one person in a small community.'),
    ('A target worth attacking', 'The matched records are a list of people who responded to the Gospel, with places and dates. That list is valuable to the wrong people.'),
    ('Orders to hand it over', 'A court, regulator or foreign government could demand the linked records. Records that were never made can&rsquo;t be handed over.'),
    ('Requests grow', 'More ministries, longer histories, a funder dashboard. Each request seems reasonable, and together they add up to a register of religious participation.'),
    ('Trust', 'People agree to meet one church. Being recognised across several ministries is a different promise, and many wouldn&rsquo;t expect it even after ticking a box.'),
]

EVIDENCE = [
    ('Did people who responded at this event find a church?', 'The receiving church records each handoff step. Reports show totals for each event.'),
    ('Are they still connected months later?', 'The church the person chose asks them, and asks whether the answer can be counted. Only the total leaves the church.'),
    ('How is our ministry going over time?', 'Each ministry sees its own handoffs and outcomes, by month.'),
    ('What is happening across the network?', 'Totals across all partners, with small numbers held back so no one can be singled out.'),
]

CONDITIONS = [
    'Run by an independent university or accredited researcher, never by Always, a funder or a participating ministry.',
    'Approved by a human research ethics committee.',
    'Its own plain-language consent, which people can refuse without losing any help.',
    'Adults only.',
    'Identities held apart from the study data.',
    'A fixed end date, after which the linked data and keys are destroyed.',
    'Results published as totals, whatever they show.',
    'No linkage feature in Always, and no linking key held by Always.',
    'Decided in the open, with a new architecture decision, legal and independent privacy review, and board approval.',
]


def _steps():
    out = []
    for i, (h, tech, plain) in enumerate(STEPS, 1):
        out.append(f'''<li class="lk-step"><span class="lk-n" aria-hidden="true">{i}</span><div>
      <h3>{h}</h3><p class="lk-tech"><b>Technically:</b> {tech}</p><p><b>In plain words:</b> {plain}</p></div></li>''')
    return '\n'.join(out)


def _rows(items, cls):
    return '\n'.join(f'<div class="{cls}"><b>{a}</b><p>{b}</p></div>' for a, b in items)


PAGE = f'''
<article class="lk">
<div class="lk-top"><div class="wrap lk-in">
  <p class="lk-kick">Research case study</p>
  <h1>Why we don&rsquo;t link people across ministries</h1>
  <p class="lk-lede">We explored a way to recognise the same person across the churches and ministries that help them, using privacy-preserving record linkage. We designed it, tested it, and decided it should not be used. This is what we learned.</p>
</div></div>

<div class="wrap lk-in lk-body">
  <aside class="lk-status" role="note"><b>Not in use.</b> Always does not link people across organisations. Nothing described here runs on the Always Platform, and it never ran with real people. Published 21 November 2026.</aside>

  <h2>The question we explored</h2>
  <p>Someone might hear the Gospel at a youth event, do a course run by another ministry a few months later, and then join a local church. Each organisation sees only its own part of that story. The event team never learns the person found a church, and the course can&rsquo;t tell whether people stay.</p>
  <p>We asked ourselves whether ministries could learn how the story ended without anyone handing over their contact lists. Health research in Australia has the same problem with hospital and GP records, and has used privacy-preserving record linkage to work on it for years. We wanted to know whether the same approach could serve churches.</p>

  <h2>How it would have worked</h2>
  <p>Four steps, each described the way an engineer would and then in everyday words.</p>
  <ol class="lk-steps">
{_steps()}
  </ol>
  <p>We built it and tested it, including database security tests that try to read across organisations. It was never switched on, and we have since removed it from the platform.</p>

  <h2>Where it breaks down</h2>
  <p>The cryptography holds up. The trouble is what the system creates around it, and who might want that.</p>
  <div class="lk-grid">
{_rows(RISKS, 'lk-risk')}
  </div>

  <h2>Why a small pilot doesn&rsquo;t fix it</h2>
  <p>It is tempting to allow linkage only for a few high-impact programmes, under tight rules. That reduces how many people are exposed, but the core risks stay.</p>
  <ul>
    <li><b>Small groups are easier to identify.</b> In a few hundred people across three ministries, a handful of dates and places can be enough to name someone.</li>
    <li><b>The key is just as valuable.</b> A small pilot still needs a secret key and someone trusted to hold it.</li>
    <li><b>Exceptions become the norm.</b> Once one funder has it, the next will ask, and saying no gets harder each time.</li>
  </ul>
  <p>In health, the linking is done by separate accredited units that keep identities apart from research data, under ethics approval and their own legislation. A ministry network has none of that, and Always shouldn&rsquo;t try to become it.</p>

  <h2>The law sets a high bar</h2>
  <p>Australian law doesn&rsquo;t ban record linkage, but it treats a person&rsquo;s religious beliefs as sensitive information. Under the Privacy Act 1988, organisations generally need consent to collect it, and can use or share it only for the purpose it was collected for, or a closely related one the person would reasonably expect. A Children&rsquo;s Online Privacy Code must be registered by 10 December 2026, adding stricter rules for children&rsquo;s information online.</p>
  <p>Meeting that bar for cross-ministry linkage would be hard. On top of what the law requires, we have chosen not to do it at all.</p>
  <p class="lk-small">This is a general summary of the law, not legal advice.</p>

  <h2>The strength of the local church</h2>
  <p>The church has always been many local congregations, each knowing and caring for its own people. That is a strength for privacy as well as for care. When each church holds its own records, there is no single list to steal, sell or seize, and a breach at one church doesn&rsquo;t expose another. Care happens where people are known by name.</p>
  <p>Always is built the same way. It connects churches and ministries and leaves their people with them. Someone who asks to be introduced goes to one church, with their permission, and that church cares for them. The network introduces people and then steps back.</p>

  <h2>What we do instead</h2>
  <p>Most of what ministries and funders want to know can be answered without recognising anyone across organisations.</p>
  <div class="lk-ev">
{_rows(EVIDENCE, 'lk-evr')}
  </div>
  <p>The one question this can&rsquo;t answer is whether a particular programme <i>caused</i> someone to join a church, compared with everything else in their life. That is a research question, and it needs a different approach.</p>

  <h2>If that question ever needs an answer</h2>
  <p>It would have to be a one-off study, run outside Always. These are the least we would expect before even discussing one:</p>
  <ol class="lk-cond">
    {''.join(f'<li>{c}</li>' for c in CONDITIONS)}
  </ol>
  <p>If a proposal can&rsquo;t meet all of them, the answer is no.</p>

  <h2>Our position</h2>
  <p>Always does not link people across organisations, at any scale or under any name. That decision is recorded in our open-source architecture decisions and applies to our code, our partners and our funders. We publish this case study to show how we weigh risk: we did the design work properly, and the design work told us not to build it.</p>
  <p class="lk-contact">Questions or a different view? Email <a href="mailto:hello@alwaysfoundation.org">hello@alwaysfoundation.org</a>.</p>
  <p class="lk-links"><a href="#/docs/privacy">How we look after information</a> <a href="#/">Home</a></p>
</div>
</article>
'''

CSS = r'''
.lk-top { background: var(--green); color: var(--cream); padding: 168px 0 56px; }
.lk-in { max-width: 760px; }
.lk-kick { font: 600 14px/1 var(--head); color: rgba(255,253,248,.72); margin: 0 0 18px; }
.lk h1 { font-size: clamp(36px, 5.4vw, 60px); letter-spacing: -0.035em; line-height: 1.03; margin: 0 0 22px; color: var(--cream); }
.lk-lede { font-size: 20px; line-height: 1.55; margin: 0; color: rgba(255,253,248,.88); max-width: 640px; }
.lk-body { padding-top: 40px; padding-bottom: 104px; }
.lk-body > p, .lk-body li { font-size: 18px; line-height: 1.65; }
.lk-body > p { margin: 0 0 18px; }
.lk-body h2 { font-size: clamp(26px, 3.2vw, 34px); letter-spacing: -0.025em; line-height: 1.15; margin: 56px 0 16px; }
.lk-status { margin: 0 0 8px; padding: 18px 20px; border-left: 4px solid var(--peach); background: #FFFDF8; border-radius: 0 14px 14px 0; font-size: 16.5px; line-height: 1.55; }
.lk-steps { list-style: none; padding: 0; margin: 24px 0; display: grid; gap: 14px; }
.lk-step { display: grid; grid-template-columns: 44px 1fr; gap: 16px; padding: 20px; background: #FFFDF8; border-radius: 18px; box-shadow: 0 1px 0 rgba(27,71,64,.08); }
.lk-n { width: 44px; height: 44px; border-radius: 999px; background: var(--green); color: var(--cream); display: flex; align-items: center; justify-content: center; font: 700 18px/1 var(--head); }
.lk-step h3 { font-size: 19px; margin: 8px 0 8px; }
.lk-step p { margin: 0 0 8px; font-size: 16.5px; line-height: 1.6; }
.lk-step p:last-child { margin-bottom: 0; }
.lk-tech { color: var(--soft); }
.lk-tech code { font-size: 14px; }
.lk-grid { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px; margin: 22px 0 8px; }
.lk-risk { padding: 18px; border: 1px solid var(--line); border-radius: 16px; }
.lk-risk b, .lk-evr b { display: block; font: 700 16.5px/1.3 var(--head); color: var(--green); margin-bottom: 6px; }
.lk-risk p, .lk-evr p { margin: 0; font-size: 15.5px; line-height: 1.55; }
.lk-ev { display: grid; margin: 20px 0 18px; border-top: 1px solid var(--line); }
.lk-evr { display: grid; grid-template-columns: 1fr 1.2fr; gap: 20px; padding: 16px 0; border-bottom: 1px solid var(--line); }
.lk-evr b { margin: 0; }
.lk-cond li { margin-bottom: 8px; }
.lk-body > p.lk-small { font-size: 15px; color: var(--soft); }
.lk-risk:last-child:nth-child(odd) { grid-column: 1 / -1; }
.lk-contact { margin-top: 40px !important; }
.lk-links { display: flex; gap: 24px; flex-wrap: wrap; }
.lk-links a { display: inline-flex; align-items: center; min-height: 44px; font-weight: 600; }
@media (max-width: 700px) {
  .lk-top { padding: 124px 0 40px; }
  .lk-grid { grid-template-columns: 1fr; }
  .lk-evr { grid-template-columns: 1fr; gap: 6px; }
  .lk-step { grid-template-columns: 1fr; }
}
'''

TILE = '''
      <li class="cs-tile cs-tile-rs">
        <div class="cs-img lk-tile-art" aria-hidden="true"><svg viewBox="0 0 400 260"><g fill="none" stroke="rgba(255,253,248,.28)" stroke-width="2"><circle cx="90" cy="120" r="46"/><circle cx="200" cy="120" r="46"/><circle cx="310" cy="120" r="46"/></g><g fill="#E8A577"><circle cx="78" cy="110" r="6"/><circle cx="100" cy="128" r="6"/><circle cx="190" cy="104" r="6"/><circle cx="212" cy="122" r="6"/><circle cx="196" cy="140" r="6"/><circle cx="300" cy="114" r="6"/><circle cx="322" cy="132" r="6"/></g><text x="200" y="216" text-anchor="middle" fill="rgba(255,253,248,.78)" font-family="Inter, sans-serif" font-weight="600" font-size="17">Each church keeps its own people</text></svg></div>
        <div class="cs-text">
          <p class="cs-name">Research case study</p>
          <h3>Why we don&rsquo;t link people across ministries.</h3>
          <p>A system we designed, tested and chose not to use, and what it taught us about privacy and the local church.</p>
          <a class="cs-more" href="#/pprl">Read the case study</a>
        </div>
      </li>'''

TILE_CSS = '''
.lk-tile-art { background: radial-gradient(120% 90% at 85% 10%, rgba(232,165,119,.22), transparent 60%), #14352F; display: flex; align-items: center; justify-content: center; }
.lk-tile-art svg { width: 100%; height: 100%; }
'''

JS = ''
