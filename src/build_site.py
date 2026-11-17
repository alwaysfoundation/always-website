import os
ROOT = os.path.dirname(os.path.abspath(__file__))
"""Assemble the Always Foundation website: home, directory, about and docs in one page with hash routes."""
import json, html

css = open(os.path.join(ROOT, 'base.css')).read()
home = open(os.path.join(ROOT, 'main.html')).read()
import extras, pages as P, re as _re
def _swap(h, marker, new):
    i = h.find(marker); a = h.rfind('<section', 0, i); b = h.find('</section>', i) + 10
    return h[:a] + new + h[b:]
home = _swap(home, 'class="sec map"', extras.MAP_SECTION)
home = _swap(home, 'class="sec promise"', extras.FLOW_SECTION)
directory = open(os.path.join(ROOT, 'dir.json')).read()
COUNT = len(json.loads(directory))

# ---------------------------------------------------------------- Docs content
# Written as if the platform is live: this is the documentation people will read.
DOCS = [
 ("Getting started", [
  ("introduction", "Introduction", """
<p class="lead">Always connects the body of Christ in Australia, so everyone who responds to Jesus is offered their next best faith step, with a real person walking with them.</p>
<p>Every week people respond to Jesus at concerts, camps, services, film screenings and online. Always makes sure that moment becomes a next step. The person chooses what would help, sees exactly who will reach out before sharing anything, and a local church or ministry gets in touch. If no one can, our care team helps.</p>
<h2>Who Always is for</h2>
<ul>
<li><b>Churches</b> claim their page on the map, receive introductions and welcome people from their phone. Free, always.</li>
<li><b>Ministries and events</b> (tours, camps, youth events, campus and street outreach, media) give everyone who responds a safe next step, under their own brand if they like.</li>
<li><b>People who respond</b> get a clear choice, a real person, and control of their own story.</li>
<li><b>Builders</b> add Always to church and ministry apps with the Always API and SDK.</li>
</ul>
<div class="callout">New here? Read <a href="#/docs/how-it-works">How Always works</a>, then the guide for your role in the sidebar.</div>
"""),
  ("how-it-works", "How Always works", """
<p class="lead">Respond. Connect. Walk. Someone responds to Jesus, they're introduced to their next best faith step nearby, and a real person walks with them.</p>
<h2>1. Someone responds</h2>
<p>At an event, a service or online, the person opens a response card (a QR code, a link or a ministry's own app). They choose what would help: finding a church, exploring faith in a course, talking with someone, joining a youth group or starting to read the Bible. They give their first name, a mobile and their suburb, and agree to share them with a church or ministry nearby.</p>
<h2>2. They're connected</h2>
<p>Always offers them to the nearest verified church or ministry that offers that next step, has room this month and speaks their language. It accepts, or passes with a reason, and the next one nearby that fits is offered.</p>
<h2>3. A real person walks with them</h2>
<p>Once a church accepts, it sees the person's contact details and reaches out from its own phone. The person gets a text saying who will be in touch. The church logs that contact happened (never what was said) and keeps going: coffee, a seat together on Sunday, a course or a small group.</p>
<h2>The care team</h2>
<p>If no church or ministry can take someone, the Always care team helps, so everyone is offered a next step.</p>
<h2>Only the person says "connected"</h2>
<p>We count someone as connected only when they confirm it themselves, through the link in their text. That is the number we report, including the people we missed.</p>
"""),
  ("glossary", "Glossary", """
<dl class="gloss">
<dt>Response</dt><dd>Someone telling us they responded to Jesus and would like a next step, with their consent.</dd>
<dt>Next best faith step</dt><dd>What would help this person most right now: often a local church, sometimes a course to explore faith, a youth group, discipleship or care.</dd>
<dt>Introduction</dt><dd>An invitation to a church or ministry nearby to welcome a person. Their details are shared only once it accepts.</dd>

<dt>Care team</dt><dd>Trained Always staff and volunteers who say hello and walk with anyone no church could take.</dd>
<dt>Listed, claimed, verified</dt><dd>Every church starts as a listing on the map. A claimed page is managed by the church. A verified church has been checked with its denomination or network and can receive introductions. Verified youth partners can receive young people.</dd>
<dt>Consent receipt</dt><dd>The record that travels with a person: what they agreed to, who may receive their details, who agreed, and the exact words they saw.</dd>
<dt>Sender</dt><dd>A ministry, event or app that passes responses to the network.</dd>
</dl>
"""),
 ]),
 ("For churches", [
  ("claim", "Claim your church's page", """
<p class="lead">Every evangelical and Pentecostal church in Australia is on the map. Claiming your page is free and takes about ten minutes.</p>
<ol>
<li>Find your church in the <a href="#/directory">directory</a> and choose <b>Claim this page</b>.</li>
<li>Tell us your role (pastor, elder, administrator, connect lead) and how we can confirm it, such as your listing on your denomination's website.</li>
<li>We check with your denomination or network, usually within two working days.</li>
<li>Once confirmed, invite your team and set up your page, next steps and capacity.</li>
</ol>
<h2>Becoming verified</h2>
<p>To receive introductions, a church is verified: we confirm it affirms the Nicene Creed, is part of a denomination or network (or has two references from verified churches), and has a named connect lead who has completed the 20-minute welcoming course. To receive young people, a church is verified as a youth partner, which adds Working With Children Checks and a child-safe policy.</p>
"""),
  ("inbox", "Welcome from your phone", """
<p class="lead">The Always inbox works on any phone. It shows everyone you're walking with, what they asked for and what's due.</p>
<h2>When someone is waiting</h2>
<p>You get an email or notification that says someone near you has asked for a next step. It doesn't include their name or details. Open your inbox to see their first name, suburb, age band and what they asked for.</p>
<h2>Accept or pass</h2>
<ul>
<li><b>Accept</b> to see their mobile and welcome them.</li>
<li><b>Pass</b> if you can't help well: you're at capacity, there's a language need, it isn't the right fit, or there's a safeguarding concern. The next church is offered straight away. Passing is always OK.</li>
</ul>
<h2>Reach out your way</h2>
<p>Text or call from your own phone, then log what happened in one tap: a call, a text, a reply, a meeting. The conversation itself stays between you.</p>
<h2>Keep walking</h2>
<p>Your inbox reminds you of anyone waiting to hear back. When the person tells us they're connected, the introduction closes.</p>
"""),
  ("your-page", "Your church page", """
<p class="lead">Your page is how people meet you before they walk in. Make it yours.</p>
<ul>
<li><b>Welcome line and description</b> in your own words.</li>
<li><b>Style and colour:</b> choose classic, warm or bold, and your brand colour.</li>
<li><b>Sections in your order:</b> welcome, service times, what to expect, kids, youth, next steps, map and up to four custom sections.</li>
<li><b>Next steps you offer:</b> Sunday welcome, a course to explore faith, a conversation, youth group, small groups, practical help.</li>
</ul>
<p>Pages show a verified badge once you're verified. Your team's details stay private unless you choose to show them.</p>
"""),
  ("capacity", "Next steps and capacity", """
<p>Tell us what you can do well, and we'll only send you people you can welcome.</p>
<ul>
<li><b>Monthly limit:</b> how many introductions you can take each month (default 10).</li>
<li><b>Area:</b> how far from your church you'll welcome people (default 8 km).</li>
<li><b>Languages</b> your team can welcome people in.</li>
<li><b>Pause</b> introductions for a holiday or a busy season, and resume in one tap.</li>
</ul>
<p>Matching uses distance first, then how quickly churches usually respond, then how many introductions each church already holds, so welcomes are shared fairly.</p>
"""),
  ("welcoming", "Welcoming well", """
<p class="lead">The free 20-minute course every connect lead completes before their church is verified.</p>
<ol>
<li><b>Reply soon.</b> A short, warm text: who you are, that you're glad they reached out, and one simple invitation.</li>
<li><b>Offer a friend at the door.</b> People are far more likely to come back when someone they've met is waiting for them.</li>
<li><b>Go at their pace.</b> Coffee before church is fine. So is a course first.</li>
<li><b>Pray for them by name</b> with your team.</li>
<li><b>Keep it safe.</b> Two adults with young people, contact between 8am and 8pm, and safeguarding concerns go to a trained person straight away.</li>
</ol>
"""),
 ]),
 ("For ministries and events", [
  ("senders", "Response pages and QR codes", """
<p class="lead">Give everyone who responds at your event a safe next step, in seconds.</p>
<ol>
<li>Create a campaign for your event or tour in the Always console.</li>
<li>Add placements: a QR code for the screen, a short link, an armband card, or the response card inside your app.</li>
<li>People respond on their own phones. Volunteers can capture a conversation for someone too, with their consent.</li>
<li>Each person is offered to a verified church or ministry near where they live, anywhere in Australia.</li>
</ol>
<h2>What you see</h2>
<p>You see how many people responded and how many were received, accepted and connected. Their details stay with the church that welcomes them. If a person agrees, you'll also see that they connected.</p>
"""),
  ("branding", "Custom branding", """
<p class="lead">Run Always under your own brand. Same promise, your look and voice.</p>
<p>In the console, set your colours, fonts, logo, heading and button wording, and which next steps you offer. The consent wording, minors rules and privacy promises stay the same everywhere, so people are just as safe whichever ministry they meet.</p>
<pre><code>&lt;always-response
  endpoint="/api/always/respond"
  event="City worship night"
  theme="your-ministry"&gt;&lt;/always-response&gt;</code></pre>
<p>A youth ministry might use dark navy and electric blue with wide headlines. Every page still says the person's details stay in Australia and shows who will reach out.</p>
"""),
  ("events", "Events", """
<p class="lead">Christian events across Australia, in one place: worship nights, concerts, outreach, youth camps, courses and training.</p>
<h2>How events get in</h2>
<ol>
<li><b>Churches and ministries add their own</b> from Always for churches and ministries. Verified partners publish straight away.</li>
<li><b>Our team adds major events</b>, like tours and conferences.</li>
<li><b>Anyone can suggest an event.</b> Our team checks it before it shows.</li>
<li><b>Ticketing platforms.</b> Organisers can bring in events from their ticketing account, where the platform allows it. We're talking with platforms about doing this well.</li>
</ol>
<h2>Where events show</h2>
<p>On our Events page, in the Always app's Connect tab, and through the API so other apps can list them too.</p>
"""),
  ("online", "Online responses", """
<p class="lead">Sharing a testimony video, a sermon or a post? Give people a way to respond, wherever they watch.</p>
<ul>
<li><b>A link or QR</b> in a video description, a social bio or a post, opening a response page under your brand.</li>
<li><b>An embedded response card</b> on your website, right under the video.</li>
<li><b>A response button</b> in your own app, through the SDK.</li>
</ul>
<pre><code>&lt;always-response page="testimony-video"&gt;&lt;/always-response&gt;</code></pre>
<p>An invisible check stops spam without puzzles. The same consent and safeguards apply as at any event, and each person is introduced to a church near where they live.</p>
"""),
  ("results", "Results you can trust", """
<p>Every ministry measures the same things the same way: responses, received, accepted, first contact, and connected (confirmed by the person). We show totals only, and never a figure smaller than 10 adults or 20 young people, so no one can be identified.</p>
<p>The public <b>promise page</b> shows how the whole network is going each month, including the people we couldn't connect.</p>
"""),
 ]),
 ("For people", [
  ("your-choices", "Your choices and your privacy", """
<p class="lead">Your story is yours. Here's what happens when you respond.</p>
<ol>
<li>You choose your next step, and see who will reach out.</li>
<li>A church or ministry near you gets in touch.</li>
<li>You get a text with a private link to see who's in touch, tell us you're connected, or change your mind.</li>
</ol>
<p>Your details stay in Australia and are never sold. Under 15? We'll ask a parent or guardian to confirm first.</p>
"""),
 ]),
 ("The platform", [
  ("consent", "The consent primitive", """
<p class="lead">Consent travels with the person. This is the heart of Always.</p>
<p>Every person carries a consent receipt everywhere their details go. It records exactly what they agreed to, who may receive their details, who agreed (them or a parent), their age band, and the exact words they saw. Every system that touches the person checks it first and fails closed: anything not explicitly allowed is refused. Withdrawal is one tap and reaches everyone holding their details.</p>
<pre><code>{
  "purposes": ["connect.church", "notify.sender"],
  "recipients": [],
  "allowNextNearby": true,
  "party": "self",
  "ageBand": "18+",
  "wordingVersion": "v1"
}</code></pre>
<h2>Purposes</h2>
<table><tr><th>Purpose</th><th>What it allows</th></tr>
<tr><td><code>connect.church</code></td><td>Share first name and contact with the church or ministry that welcomes them. Required.</td></tr>
<tr><td><code>notify.sender</code></td><td>Tell the ministry that ran the event that the person connected. No details.</td></tr>
<tr><td><code>resources</code></td><td>Send a few helpful resources. Adults only.</td></tr>
<tr><td><code>stats.anonymous</code></td><td>Count the person in anonymous totals.</td></tr></table>
<p>The receipt follows ISO/IEC TS 27560 for consent records, so it can travel between any systems that implement the Always Handoff standard.</p>
"""),
  ("standard", "The Always Handoff standard", """
<p class="lead">An open specification for passing a person from one ministry to another, with consent attached.</p>
<p>Any church app, events tool or church management system can implement it. It defines:</p>
<ul>
<li>the <b>consent receipt</b> and its purposes</li>
<li>the <b>response</b>: next step, suburb, age band, language</li>
<li>the <b>offer</b> and its timers</li>
<li>the <b>handoff states</b>: awaiting parent, routing, offered, accepted, contacted, care team, closed, withdrawn</li>
<li>the <b>events</b> systems exchange, as CloudEvents 1.0</li>
</ul>
<p>The standard is published as JSON Schema under CC BY 4.0. Changes go through an open RFC process, approved by the Technology Steering Committee and, where people's safety is involved, the Safeguarding, Privacy and Ethics Committee.</p>
"""),
  ("api", "Always API", """
<p class="lead">A REST API (OpenAPI 3.1) for sending responses, receiving introductions, managing a page and reading the directory. Hosted in Sydney.</p>
<h2>Authentication</h2>
<p>Integrations use scoped API tokens (<code>alw_live_…</code>), shown once, hashed at rest and revocable. Staff sign in with passkeys or an authenticator app, and send the organisation they're acting for.</p>
<pre><code>curl https://api.alwaysfoundation.org/v1/responses \\
  -H "Authorization: Bearer $ALWAYS_TOKEN" \\
  -H "Content-Type: application/json" \\
  -d '{"firstName":"Sam","contact":{"kind":"mobile","value":"0400 000 000"},
       "suburb":"Parramatta","postcode":"2150","state":"NSW",
       "ageBand":"18+","step":"church",
       "consent":{"purposes":["connect.church"],"allowNextNearby":true,
                  "wordingVersion":"v1","party":"self"}}'</code></pre>
<h2>Endpoints</h2>
<table><tr><th>Endpoint</th><th>What it does</th></tr>
<tr><td><code>GET /v1/directory</code></td><td>Search churches and ministries (public)</td></tr>
<tr><td><code>GET /v1/orgs/{slug}</code></td><td>A church's public page</td></tr>
<tr><td><code>POST /v1/responses</code></td><td>Pass a consenting person to the network</td></tr>
<tr><td><code>GET /v1/inbox</code></td><td>Introductions for your organisation</td></tr>
<tr><td><code>POST /v1/handoffs/{id}/accept</code></td><td>Accept an introduction</td></tr>
<tr><td><code>POST /v1/handoffs/{id}/pass</code></td><td>Pass, with a reason</td></tr>
<tr><td><code>POST /v1/handoffs/{id}/activity</code></td><td>Log a call, text or meeting</td></tr>
<tr><td><code>PUT /v1/org/profile</code></td><td>Update your page, next steps and capacity</td></tr></table>
<p>Contact details appear only after acceptance. Errors use plain codes such as <code>no_pending_offer_for_org</code> and <code>under13_no_child_data</code>.</p>
"""),
  ("sdk", "Always SDK", """
<p class="lead">Add Always to any church or ministry app in about ten minutes.</p>
<pre><code>npm install @always/sdk</code></pre>
<h2>The response card</h2>
<p>A drop-in web component: accessible, brandable, no cookies or tracking. It posts to your own backend, so no secret ever reaches the browser.</p>
<pre><code>&lt;script type="module" src="https://cdn.alwaysfoundation.org/sdk/v0/widget.js"&gt;&lt;/script&gt;
&lt;always-response endpoint="/api/always/respond" accent="#1B4740"&gt;&lt;/always-response&gt;</code></pre>
<h2>The client</h2>
<pre><code>import { AlwaysClient, buildConsent } from '@always/sdk';

const always = new AlwaysClient({ token: process.env.ALWAYS_TOKEN });
await always.responses.create({
  firstName: 'Sam', contact: { kind: 'mobile', value: '0400 000 000' },
  suburb: 'Parramatta', postcode: '2150', state: 'NSW',
  ageBand: '18+', step: 'church',
  consent: buildConsent({ ageBand: '18+', connect: true, allowNextNearby: true }),
});</code></pre>
"""),
  ("webhooks", "Webhooks", """
<p>Subscribe to events such as <code>always.offer.created</code>, <code>always.handoff.accepted</code> and <code>always.handoff.withdrawn</code>. Events are CloudEvents 1.0, signed with HMAC-SHA256, and carry ids only, never personal details.</p>
<pre><code>import { verifyWebhook } from '@always/sdk';

const ok = await verifyWebhook({
  secret: process.env.ALWAYS_WEBHOOK_SECRET,
  body: rawBody,
  timestamp: req.headers['always-timestamp'],
  signature: req.headers['always-signature'],
});</code></pre>
<p>When you receive <code>always.handoff.withdrawn</code>, delete what you hold about that person.</p>
"""),
  ("youversion", "Scripture with YouVersion", """
<p class="lead">YouVersion opens the technology behind the Bible App to ministries. Always uses it in three places.</p>
<ol>
<li><b>Scripture from the first step.</b> Choosing "Start reading the Bible" opens a reading plan in the person's language, while a church gets in touch.</li>
<li><b>Sign in with YouVersion.</b> People can sign in with the account they already use. If they agree, Always links it to their home church, so their church stays with them across member apps.</li>
<li><b>Every member app starts with Scripture.</b> Apps built on the Always SDK can add the Bible reader in a few lines, free to use, with no paywall on Scripture and no ads.</li>
</ol>
<p>YouVersion confirms who someone is. Always holds which church they belong to and what they agreed to share. Neither holds the other's data.</p>
"""),
 ]),
 ("Trust and safety", [
  ("security", "Security", """
<p class="lead">People's stories are precious. We look after them carefully.</p>
<ul>
<li><b>Kept in Australia.</b> Everything is stored and processed in Sydney.</li>
<li><b>Encrypted.</b> Names and contact details are encrypted before they're stored.</li>
<li><b>Only the right church sees them.</b> A church sees someone's details only after it accepts their introduction.</li>
<li><b>Built to recognised standards.</b> The Essential Eight and OWASP ASVS, checked on every change.</li>
</ul>
<p>Found a security issue? Email <b>security@alwaysfoundation.org</b>.</p>
"""),
  ("privacy", "Privacy", """
<p class="lead">Your story is yours. You choose who hears it.</p>
<ul>
<li>We ask only for what a next step needs: a first name, a way to reach you, your suburb and what you'd like help with.</li>
<li>You see who will reach out before anything is shared, and it goes only to the church or ministry that welcomes you.</li>
<li>Change your mind whenever you like, and your details are deleted.</li>
<li>We don't sell information or use it for advertising.</li>
</ul>
<p>Questions, or want to see what we hold? <b>privacy@alwaysfoundation.org</b></p>
"""),
  ("young-people", "Children and young people", """
<p class="lead">Young people are welcome, and kept safe.</p>
<ul>
<li>Under 13s ask a parent or leader to help them take a next step.</li>
<li>For 13 and 14 year olds, a parent or guardian confirms first.</li>
<li>Young people are only introduced to verified youth partners, with Working With Children Checks and child-safe policies.</li>
</ul>
<p>We follow the National Principles for Child Safe Organisations. Questions: <b>safeguarding@alwaysfoundation.org</b></p>
"""),
  ("ai", "AI", """
<p class="lead">People welcome people. Technology helps them do it well.</p>
<p>Every welcome comes from a real person. Where we use AI, it's to save volunteers time, like turning a voice note into text on their own phone, and the person stays in charge of what happens next. We don't use anyone's information to train AI, and young people's information is kept out of it entirely.</p>
"""),
  ("policies", "Our policies", """
<p>Always is governed by six published policies, each with numbered rules:</p>
<table><tr><th>Policy</th><th>What it covers</th></tr>
<tr><td>Cybersecurity Policy</td><td>Access, encryption, secure development, incident response, business continuity</td></tr>
<tr><td>Privacy Policy</td><td>What we collect, why, who sees it, your rights</td></tr>
<tr><td>Data Governance Policy</td><td>Consent, sharing, retention, quality and minimum group sizes</td></tr>
<tr><td>Children and Young People's Information Policy</td><td>Age bands, parental confirmation, youth partners, safe contact</td></tr>
<tr><td>AI Policy</td><td>Where AI may and may not be used, human oversight, no training on people's data</td></tr>
<tr><td>Terms of Use</td><td>The agreement for churches, ministries, builders and people</td></tr></table>
<p>Full policies are published with the open-source repository and updated through the foundation's committees.</p>
"""),
 ]),
 ("The foundation", [
  ("governance", "Governance", """
<p>The Always Foundation is being established as an Australian not-for-profit company limited by guarantee, with Prolegis Lawyers, and will register as a charity with the ACNC.</p>
<ul>
<li><b>Members own it.</b> Churches and ministries that affirm the Nicene Creed are voting members: one member, one vote.</li>
<li><b>A skilled, independent board</b> of five to nine directors, a majority independent of any single organisation.</li>
<li><b>Committees:</b> Theology and Mission; Technology Steering; Safeguarding, Privacy and Ethics; Partnerships and Membership; Finance, Audit and Risk.</li>
<li><b>Builders on equal terms.</b> Anyone building on Always, including commercial builders, does so on the same terms as everyone else, with no special rights.</li>
</ul>
"""),
  ("open-source", "Open source and licences", """
<ul>
<li><b>Code</b> is Apache 2.0: permissive, widely trusted, with a patent grant.</li>
<li><b>Docs, the standard, policies and training</b> are CC BY 4.0.</li>
<li><b>Contributions</b> use the Developer Certificate of Origin. Contributors keep their copyright. AI-assisted work is disclosed.</li>
<li>Every change needs two human approvals, with code owners for consent, minors, security and routing.</li>
<li>People's information always stays private.</li>
</ul>
<p>Code lives at <b>github.com/alwaysfoundation</b>. Our focus is Australia, but anyone, anywhere, can use the technology for their own network.</p>
"""),
  ("brand", "Brand and trademark", """
<p>"Always", "Always Foundation" and the Always mark are trademarks held for the foundation's members. Anyone may say their app is "built on Always" or "connects to the Always Network". Please ask before using the mark, or anything that suggests the foundation endorses or verifies your product: <b>hello@alwaysfoundation.org</b>.</p>
"""),
  ("faq", "Questions", """
<p class="lead">Our full FAQs cover churches, ministries, people who respond, the Always app, privacy and supporters.</p>
<p><a href="#/faq">Read the FAQs</a></p>
"""),
 ]),
]

def esc(s): return html.escape(s, quote=True)

nav_html = ''
pages_json = {}
order = []
for group, pages in DOCS:
    nav_html += f'<p class="dgroup">{esc(group)}</p><ul>'
    for slug, title, body in pages:
        nav_html += f'<li><a href="#/docs/{slug}" data-slug="{slug}">{esc(title)}</a></li>'
        pages_json[slug] = {'title': title, 'group': group, 'html': body.strip()}
        order.append(slug)
    nav_html += '</ul>'

extra_css = """
.brand svg.wm { width: auto; height: 34px; }
footer .brand svg.wm { height: 28px; }
@media (max-width: 480px) { header .brand svg.wm { height: 26px; } header .brand { font-size: 21px; } }
/* Multi-page */
.page[hidden] { display: none; }
.page-hero { background: var(--green); color: var(--cream); padding: 150px 0 72px; }
.page-hero h1 { font-size: clamp(44px, 6vw, 84px); letter-spacing: -0.045em; }
.page-hero p { margin-top: 18px; max-width: 680px; font-size: 20px; color: var(--on-green); }
nav a[aria-current="page"] { color: var(--cream); text-decoration: underline; text-decoration-color: var(--peach); text-underline-offset: 8px; text-decoration-thickness: 2px; }

/* Directory */
.dir-tools { display: grid; grid-template-columns: 1fr 200px 200px; gap: 14px; margin: -34px 0 28px; position: relative; z-index: 2; }
.dir-tools input, .dir-tools select { background: var(--paper); color: var(--ink); border: 1px solid var(--line); border-radius: 16px; height: 60px; padding: 0 20px; font-size: 17px; box-shadow: 0 20px 40px -30px rgba(30,42,38,.5); }
.dir-meta { display: flex; justify-content: space-between; align-items: center; margin-bottom: 18px; color: var(--muted); font-size: 15px; }
.dir-list { display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px; }
.org { background: var(--paper); border-radius: 24px; padding: 24px; display: flex; flex-direction: column; gap: 8px; min-height: 170px; }
.org h3 { font-size: 20px; letter-spacing: -0.02em; line-height: 1.2; }
.org .where { color: var(--soft); font-size: 15.5px; }
.org .den { color: var(--muted); font-size: 14px; }
.org .foot { margin-top: auto; display: flex; justify-content: space-between; align-items: center; gap: 10px; padding-top: 10px; }
.badge { font: 700 12px/1 var(--head); padding: 7px 10px; border-radius: 8px; background: var(--sage); color: var(--green); }
.badge.kind { background: var(--peach-soft); color: var(--clay); }
.org button { font: 600 14px var(--text); color: var(--green); background: none; border: 0; cursor: pointer; text-decoration: underline; text-underline-offset: 4px; padding: 6px 0; }
.dir-more { display: flex; justify-content: center; margin-top: 32px; }
.dir-empty { padding: 48px; text-align: center; color: var(--soft); background: var(--paper); border-radius: 24px; }
.claim-note { margin-top: 48px; background: var(--sage); border-radius: 28px; padding: 36px 40px; display: grid; grid-template-columns: 1fr auto; gap: 24px; align-items: center; }
.claim-note h3 { font-size: 28px; letter-spacing: -0.02em; }
.claim-note p { color: var(--soft); margin-top: 6px; }

/* About */
.about-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 72px; }
.about-grid h2 { font-size: clamp(32px, 3.6vw, 48px); color: var(--green); }
.about-grid p { margin-top: 18px; font-size: 18.5px; color: var(--soft); }
.mv { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; margin-top: 72px; }
.mv div { background: var(--paper); border-radius: 28px; padding: 34px; }
.mv h3 { font-size: 24px; color: var(--green); letter-spacing: -0.02em; }
.mv p { margin-top: 10px; color: var(--soft); font-size: 17px; }
.creed { margin-top: 72px; background: var(--green); color: var(--cream); border-radius: 36px; padding: 56px; display: grid; grid-template-columns: 1fr 1.2fr; gap: 48px; align-items: center; }
.creed h2 { font-size: clamp(30px, 3.4vw, 46px); color: var(--cream); }
.creed p { color: var(--on-green); font-size: 18px; }
.founders { display: flex; gap: 16px; margin-top: 28px; flex-wrap: wrap; }
.founders span { font: 800 26px/1 var(--head); padding: 22px 30px; border-radius: 20px; background: var(--paper); color: var(--green); letter-spacing: -0.02em; }

/* Docs */
.docs { display: grid; grid-template-columns: 270px minmax(0, 1fr); gap: 64px; padding-top: 64px; padding-bottom: 120px; }
.dpick { display: none; }
.dnav { position: sticky; top: 24px; align-self: start; max-height: calc(100vh - 48px); overflow: auto; padding-right: 8px; }
.dnav .dgroup { font: 700 13px/1 var(--head); color: var(--clay); margin: 26px 0 10px; }
.dnav .dgroup:first-child { margin-top: 0; }
.dnav ul { list-style: none; margin: 0; padding: 0; }
.dnav a { display: block; padding: 8px 12px; border-radius: 10px; color: var(--soft); text-decoration: none; font-size: 15.5px; }
.dnav a:hover { background: var(--paper); color: var(--ink); }
.dnav a.on { background: var(--green); color: var(--cream); font-weight: 600; }
.dsearch { width: 100%; height: 48px; border-radius: 12px; border: 1px solid var(--line); background: var(--paper); color: var(--ink); padding: 0 14px; font-size: 15px; margin-bottom: 8px; }
.prose { max-width: 760px; }
.prose .crumb { font: 700 13px/1 var(--head); color: var(--clay); }
.prose h1 { margin-top: 14px; font-size: clamp(38px, 4.6vw, 58px); color: var(--green); letter-spacing: -0.04em; }
.prose h2 { margin: 44px 0 12px; font-size: 28px; letter-spacing: -0.025em; color: var(--ink); line-height: 1.15; }
.prose h3 { margin: 30px 0 8px; font-size: 21px; letter-spacing: -0.02em; line-height: 1.2; }
.prose p, .prose li, .prose dd { font-size: 17.5px; color: var(--soft); line-height: 1.7; }
.prose p { margin-top: 14px; }
.prose .lead { margin-top: 18px; font-size: 21px; color: var(--ink); line-height: 1.55; }
.prose ul, .prose ol { margin: 14px 0 0; padding-left: 24px; display: grid; gap: 8px; }
.prose b { color: var(--ink); }
.prose a { color: var(--green); text-underline-offset: 3px; }
.prose code { font: 500 14.5px/1.5 ui-monospace, 'SF Mono', Menlo, monospace; background: var(--sage-2); color: var(--green); padding: 2px 6px; border-radius: 6px; }
.prose pre { margin: 20px 0 0; background: var(--night); color: #E4EEE7; border-radius: 18px; padding: 22px 24px; overflow-x: auto; }
.prose pre code { background: none; color: inherit; padding: 0; font-size: 14px; line-height: 1.7; }
.prose table { width: 100%; margin-top: 20px; border-collapse: collapse; font-size: 16px; }
.prose th { text-align: left; font: 700 14px/1.3 var(--head); color: var(--ink); padding: 12px 14px; border-bottom: 2px solid var(--line); }
.prose td { padding: 12px 14px; border-bottom: 1px solid var(--line); color: var(--soft); vertical-align: top; }
.prose .callout { margin-top: 28px; background: var(--peach-soft); border-radius: 18px; padding: 20px 24px; color: var(--ink); font-size: 17px; }
.prose .gloss dt { margin-top: 22px; font: 700 19px/1.3 var(--head); color: var(--ink); }
.prose .gloss dd { margin: 6px 0 0; }
.pager { display: flex; justify-content: space-between; gap: 16px; margin-top: 64px; padding-top: 28px; border-top: 1px solid var(--line); }
.pager a { display: grid; gap: 4px; text-decoration: none; padding: 16px 20px; border-radius: 16px; background: var(--paper); min-width: 220px; }
.pager a span { font-size: 13px; color: var(--muted); }
.pager a b { font: 700 17px/1.3 var(--head); color: var(--green); }
.pager a.next { text-align: right; margin-left: auto; }
@media (max-width: 1020px) {
  .dir-list { grid-template-columns: 1fr 1fr; }
  .docs { grid-template-columns: minmax(0, 1fr); gap: 24px; }
  .dnav { position: static; max-height: none; }
  .about-grid, .creed { grid-template-columns: 1fr; gap: 32px; }
  .mv { grid-template-columns: 1fr; }
}
@media (max-width: 860px) {
  .dnav { display: none; }
  .dpick { display: block; width: 100%; height: 54px; border-radius: 14px; border: 1px solid var(--line); background: var(--paper); color: var(--ink); padding: 0 14px; font-size: 16px; }
}
.menu-btn, .nav-foot { display: none; }
@media (max-width: 1020px) {
  header .bar { height: 80px; }
  header .bar > .btn { display: none; }
  .brand, .menu-btn { position: relative; z-index: 2; }
  .menu-btn { display: inline-flex; align-items: center; gap: 10px; height: 44px; padding: 0 16px 0 18px; border-radius: 999px; border: 1px solid rgba(248,243,234,.28); background: transparent; color: var(--cream); font: 600 15px var(--text); cursor: pointer; }
  .menu-btn i { width: 16px; height: 10px; border-top: 2px solid currentColor; border-bottom: 2px solid currentColor; transition: transform .2s, border-color .2s; }
  header.open .menu-btn i { display: none; }
  header nav { position: fixed; inset: 0; z-index: 1; display: flex; flex-direction: column; justify-content: space-between; gap: 32px; padding: 116px 28px 40px; background: var(--green-deep); overflow-y: auto; visibility: hidden; opacity: 0; transition: opacity .2s, visibility 0s .2s; }
  header.open nav { visibility: visible; opacity: 1; transition: opacity .2s; }
  header nav ul { display: grid !important; gap: 4px; }
  header nav ul a { display: block; padding: 10px 0; font: 800 34px/1.1 var(--head); letter-spacing: -0.02em; color: var(--cream); }
  header nav a[aria-current="page"] { color: var(--peach); text-decoration: none; }
  header nav .btn.nav-cta { display: inline-flex; align-self: stretch; justify-content: center; height: 56px; font-size: 17px; }
  header nav .nav-more { display: flex; flex-wrap: wrap; gap: 8px 22px; }
  header nav .nav-more a { font-size: 16px; color: var(--on-green); }
  header nav .nav-foot { display: grid; gap: 26px; }
  body.menu-open { overflow: hidden; }
}
@media (max-width: 640px) { header .bar { height: 72px; } }
@media (max-width: 640px) {
  .dir-tools { grid-template-columns: 1fr; }
  .dir-list { grid-template-columns: 1fr; }
  .claim-note { grid-template-columns: 1fr; }
  .creed { padding: 32px 26px; }
}
"""

about = """
<section class="page-hero"><div class="wrap"><h1>About Always</h1><p>A gift to the Church in Australia, so no one who responds to Jesus walks alone.</p></div></section>
<section class="sec" style="padding-top:96px"><div class="wrap">
  <div class="about-grid">
    <div><h2>Why we exist</h2>
      <p>Jesus told us to make disciples, not just gather decisions (Matthew 28:19–20). Every week Australians respond to Jesus at concerts, camps, services, film screenings and online. Many of the ministries that see those responses aren't churches, and until now there has been no simple, safe way to connect each person with the right next step nearby.</p>
      <p>Too many people said yes to Jesus and then never heard from anyone again. Always exists to close that gap.</p></div>
    <div><h2>What we do</h2>
      <p>We map every evangelical and Pentecostal church and ministry in Australia, verify them with their denominations and networks, and run one shared network that offers everyone who responds their next best faith step, with a real person walking with them.</p>
      <p>Churches use it free. Ministries can run it under their own brand. Builders can add it to their apps. And people stay in control of their own story.</p>
      <p>Our focus is Australia. Because the technology is open source, the Church in other nations is free to use it too.</p></div>
  </div>
  <div class="mv">
    <div><h3>Our mission</h3><p>Equipping the saints to make disciples: connecting everyone who turns to the Lord Jesus Christ with a local church and their next step in following Him.</p></div>
    <div><h3>Our vision</h3><p>A connected body of Christ in Australia, where no one who responds to Jesus walks alone, and everyone is offered their next best faith step.</p></div>
    <div><h3>Our values</h3><p>Christ-centred. Shared, not owned. Freely given. People's stories stay theirs. Humble about what we measure.</p></div>
  </div>
  <div class="creed">
    <div><h2>Common ground: the Nicene Creed.</h2></div>
    <div><p>Members affirm the Nicene Creed (AD 381) as the minimum common ground for membership, so churches and ministries across denominations and traditions can serve together on the historic faith.</p>
    <p style="margin-top:16px">The foundation is members-based and is being established as an Australian not-for-profit company limited by guarantee, to register as a charity with the ACNC.</p></div>
  </div>
</div>
</div></section>
"""

directory_page = f"""
<section class="page-hero"><div class="wrap"><h1>The directory</h1><p>{COUNT:,} evangelical and Pentecostal churches and ministries across Australia, and growing every week.</p></div></section>
<section style="padding-bottom:120px"><div class="wrap">
  <div class="dir-tools">
    <label class="skip" for="dq">Search the directory</label>
    <input id="dq" type="search" placeholder="Search by name, suburb or denomination" autocomplete="off">
    <label class="skip" for="ds">State</label>
    <select id="ds"><option value="">All states</option><option>NSW</option><option>VIC</option><option>QLD</option><option>WA</option><option>SA</option><option>TAS</option><option>ACT</option><option>NT</option></select>
    <label class="skip" for="dk">Type</label>
    <select id="dk"><option value="">Churches and ministries</option><option value="C">Churches</option><option value="M">Ministries</option></select>
  </div>
  <div class="dir-meta"><span id="dcount" aria-live="polite"></span><span>Listed from public denominational and network directories</span></div>
  <div class="dir-list" id="dlist"></div>
  <div class="dir-more"><button class="btn btn-green" id="dmore" type="button">Show more</button></div>
  <div class="claim-note">
    <div><h3>Is this your church?</h3><p>Claim your page to update your details, choose your next steps and start welcoming people. Free, always.</p></div>
    <a class="btn btn-peach" href="#/claim">Claim your church</a>
  </div>
</div></section>
"""

picker = ''.join(f'<optgroup label="{esc(g)}">' + ''.join(f'<option value="{sl}">{esc(t)}</option>' for sl,t,_ in ps) + '</optgroup>' for g, ps in DOCS)
docs_page = f"""
<section class="page-hero" style="padding-bottom:56px"><div class="wrap"><h1>Docs</h1><p>Everything about how Always works, for churches, ministries, people and builders.</p></div></section>
<div class="wrap docs">
  <aside class="dnav" aria-label="Docs">
    <label class="skip" for="dsq">Search the docs</label>
    <input class="dsearch" id="dsq" type="search" placeholder="Search the docs">
    <div id="dnavlist">{nav_html}</div>
  </aside>
  <div style="min-width:0"><label class="skip" for="dpick">Choose a page</label><select class="dpick" id="dpick">{picker}</select>
  <article class="prose" id="doc"></article></div>
</div>
"""

header = """
<header>
  <div class="wrap bar">
    <a class="brand" href="#/">
      <svg class="wm" viewBox="186 250 1328 366" role="img" aria-label="Always Foundation"><path fill="#F8F3EA" fill-rule="evenodd" d="M1030.8,608.4C1046.2,605.2 1061.0,596.1 1069.8,584.4C1077.9,573.6 1081.9,564.7 1101.5,514.5C1111.9,488.1 1128.3,446.2 1138.0,421.5C1147.8,396.8 1157.6,371.4 1160.0,365.2C1166.0,349.0 1167.7,350.0 1134.5,350.0C1109.8,350.0 1108.2,350.1 1106.6,351.9C1105.6,353.0 1101.7,362.3 1097.9,372.7C1094.1,383.0 1084.8,408.5 1077.3,429.2C1069.7,450.0 1063.2,467.0 1062.9,467.0C1062.5,467.0 1059.3,459.7 1055.7,450.8C1050.1,437.0 1029.3,386.6 1018.0,359.7C1016.3,355.5 1014.0,351.5 1013.0,351.0C1010.4,349.6 958.5,349.7 955.9,351.0C954.9,351.6 954.0,352.9 954.0,353.8C954.0,354.8 957.1,362.3 960.8,370.5C964.6,378.8 970.4,391.6 973.7,399.0C977.1,406.4 984.1,421.9 989.3,433.5C994.5,445.1 1006.2,470.9 1015.3,491.0C1024.3,511.1 1032.8,529.9 1034.0,532.8L1036.3,538.1L1033.5,544.6C1030.1,552.5 1024.9,557.3 1017.8,559.0C1011.6,560.5 1006.1,559.8 997.5,556.4C992.7,554.5 990.3,554.0 989.2,554.7C987.3,555.8 972.0,589.2 971.3,593.7C970.8,596.5 971.2,597.1 974.1,598.9C979.3,602.1 993.4,606.9 1001.9,608.4C1012.2,610.3 1021.6,610.3 1030.8,608.4ZM290.8,550.7C302.4,547.4 313.4,541.1 323.4,531.9L329.0,526.8L329.0,535.7C329.0,549.8 327.2,549.0 357.1,549.0C380.7,549.0 382.1,548.9 384.0,547.0C386.0,545.0 386.0,543.7 386.0,483.1C386.0,444.5 385.6,418.2 384.9,413.3C383.4,401.9 378.4,387.9 373.0,379.6C358.9,358.1 334.9,346.8 299.9,345.3C277.1,344.3 257.2,348.0 239.4,356.4C226.2,362.7 215.0,370.6 215.0,373.6C215.0,375.3 233.4,404.2 235.2,405.3C236.3,406.0 239.8,404.8 248.1,400.7C261.5,394.2 269.0,392.1 282.1,391.3C303.0,390.0 319.1,396.4 325.2,408.4C327.2,412.2 329.2,428.0 327.7,428.0C327.4,428.0 322.5,426.5 316.8,424.6C295.5,417.5 273.2,416.4 252.2,421.5C224.5,428.2 206.5,443.5 198.5,467.1C196.0,474.4 195.6,477.0 195.6,487.5C195.5,497.4 195.9,500.8 197.9,507.0C204.9,529.9 224.5,546.4 251.1,552.0C257.5,553.3 284.5,552.4 290.8,550.7ZM861.0,550.9C872.2,548.3 882.3,543.1 892.6,534.8C897.2,531.0 901.1,528.0 901.2,528.0C901.4,528.0 901.5,532.1 901.5,537.1C901.5,544.9 901.8,546.4 903.4,547.6C905.0,548.7 910.3,549.0 930.1,549.0C954.6,549.0 954.9,549.0 956.4,546.8C957.8,544.8 958.0,537.0 958.0,482.3C958.0,443.7 957.6,417.2 956.9,412.3C953.3,385.7 940.3,366.7 917.8,355.4C898.3,345.6 866.7,342.3 840.2,347.5C824.4,350.5 804.6,358.9 792.8,367.6C786.6,372.0 786.6,374.0 792.8,383.3C795.5,387.3 799.8,394.0 802.4,398.2C805.1,402.5 807.8,406.0 808.6,406.0C809.4,406.0 813.9,404.0 818.7,401.6C837.7,392.0 856.9,388.8 874.3,392.5C891.6,396.1 901.0,406.8 901.0,422.7C901.0,425.6 900.9,428.0 900.7,428.0C900.5,428.0 896.4,426.6 891.5,425.0C877.3,420.2 867.3,418.6 851.0,418.6C829.0,418.7 812.5,423.2 797.0,433.5C785.0,441.5 775.9,453.5 771.3,467.4C769.1,474.3 768.7,477.3 768.7,488.0C768.6,499.1 768.9,501.4 771.4,508.5C772.9,512.9 775.7,519.0 777.5,522.0C781.3,528.2 790.3,537.2 796.6,541.2C802.7,545.1 814.3,549.8 821.8,551.4C832.1,553.6 850.8,553.4 861.0,550.9ZM1262.7,550.6C1300.7,542.3 1323.0,511.4 1316.6,476.0C1314.6,464.6 1309.4,454.4 1302.1,447.1C1291.7,436.8 1278.0,430.6 1246.5,422.0C1221.5,415.1 1216.0,411.8 1216.0,403.5C1216.0,396.2 1221.1,392.0 1232.5,389.9C1243.3,387.9 1260.8,392.6 1275.7,401.7C1279.6,404.0 1283.8,406.0 1284.9,406.0C1286.2,406.0 1287.9,404.6 1289.4,402.2C1299.6,386.1 1307.0,373.7 1307.0,372.5C1307.0,369.2 1289.4,357.6 1276.7,352.6C1250.2,342.1 1217.5,342.8 1194.5,354.3C1173.0,365.0 1160.8,382.2 1159.4,403.8C1158.2,420.7 1162.9,434.0 1173.9,445.0C1184.4,455.4 1195.2,460.2 1237.6,473.0C1256.3,478.7 1263.4,486.5 1258.6,495.8C1254.9,503.0 1247.9,506.0 1235.0,506.0C1219.7,506.0 1204.7,500.8 1187.4,489.5C1182.2,486.1 1177.9,484.0 1176.6,484.2C1175.2,484.4 1171.1,489.3 1163.8,499.5C1149.3,519.8 1149.9,518.3 1154.1,522.6C1158.9,527.6 1172.1,536.3 1182.1,540.9C1192.1,545.6 1208.7,550.6 1218.5,551.9C1228.5,553.3 1254.1,552.5 1262.7,550.6ZM460.6,547.6C462.5,546.2 462.5,543.5 462.8,411.9C463.0,292.7 462.9,277.4 461.5,275.3L460.0,273.0L434.1,273.0C411.9,273.0 408.1,273.2 407.0,274.6C405.9,275.8 405.7,292.4 405.8,357.3C406.0,558.6 405.9,545.7 407.6,547.4C409.8,549.7 457.5,549.8 460.6,547.6ZM585.3,547.8C586.2,547.1 590.1,538.0 593.9,527.5C618.9,459.0 626.2,439.4 627.0,438.6C627.6,438.0 628.0,437.9 628.0,438.2C628.0,438.5 633.7,454.5 640.6,473.7C647.5,492.8 656.1,516.8 659.7,527.0C663.5,537.7 667.1,546.2 668.2,547.2C670.0,548.8 672.8,549.0 693.5,549.0C715.1,549.0 716.8,548.9 718.4,547.1C719.4,546.0 726.9,525.4 735.0,501.3C743.2,477.2 757.7,434.3 767.4,405.9C783.6,358.1 784.8,354.1 783.4,352.1C781.9,350.1 781.3,350.0 756.1,350.0C732.9,350.0 730.0,350.2 728.1,351.8C726.7,353.0 722.8,363.7 715.1,388.0C709.1,407.0 701.4,431.2 698.0,441.9C694.6,452.5 691.5,460.8 691.1,460.4C690.6,459.9 687.5,451.4 684.0,441.5C675.5,417.0 657.5,366.0 654.4,357.8C653.0,354.2 651.2,350.9 650.4,350.6C649.5,350.3 639.4,350.0 627.9,350.0C609.1,350.0 606.8,350.2 605.2,351.8C604.2,352.8 600.8,361.0 597.6,370.1C594.4,379.1 587.2,399.3 581.5,415.0C575.9,430.7 569.8,447.7 568.0,452.8C566.2,457.9 564.5,461.9 564.3,461.7C564.1,461.4 562.1,455.2 559.9,447.9C557.6,440.5 554.1,429.1 552.1,422.5C550.0,415.9 544.4,397.7 539.5,382.0C534.7,366.3 530.0,352.7 529.2,351.8C527.8,350.2 525.2,350.0 500.9,350.0C477.9,350.0 473.9,350.2 472.6,351.6C471.7,352.4 471.0,353.5 471.0,353.8C471.0,354.2 475.5,368.0 481.0,384.5C489.8,410.8 510.4,474.5 527.4,528.0C530.5,537.7 533.8,546.4 534.7,547.3C536.2,548.8 539.1,549.0 560.0,549.0C577.3,549.0 584.1,548.7 585.3,547.8ZM276.4,509.0C266.5,507.0 258.1,501.8 254.2,495.1C252.0,491.4 251.5,489.3 251.5,484.0C251.5,476.0 254.8,469.6 261.7,464.6C269.8,458.7 274.8,457.5 290.5,457.5C305.4,457.5 311.7,458.9 323.2,464.7L328.0,467.0L328.0,474.4C328.0,480.5 327.5,482.6 324.9,487.8C317.1,503.5 295.8,512.8 276.4,509.0ZM848.3,509.0C825.1,504.1 816.4,482.6 831.5,467.5C838.7,460.2 845.3,457.9 860.1,457.2C873.5,456.7 882.8,458.5 894.4,464.1L901.2,467.4L900.8,474.9C899.9,489.9 890.4,501.5 874.6,507.0C867.8,509.3 854.5,510.3 848.3,509.0Z"/><path fill="#EE8B54" d="M1434.5,553.6C1436.3,552.3 1436.4,549.1 1436.4,463.1L1436.5,374.0L1468.9,374.0C1497.7,374.0 1501.5,373.8 1503.2,372.3C1504.8,370.9 1505.0,368.9 1505.0,352.8C1505.0,342.3 1504.6,334.1 1504.0,332.9C1503.0,331.1 1501.5,331.0 1470.0,331.0L1437.0,331.0L1437.0,296.4C1437.0,274.5 1436.6,261.2 1436.0,259.9C1435.0,258.1 1433.7,258.0 1413.4,258.0L1392.0,258.0L1391.0,260.6C1390.4,262.0 1390.0,277.4 1390.0,297.1L1390.0,331.0L1357.7,331.0C1333.9,331.0 1325.1,331.3 1324.2,332.2C1323.3,333.1 1323.0,339.0 1323.0,352.7C1323.0,370.7 1323.1,372.0 1324.9,373.0C1326.2,373.6 1338.6,374.0 1358.4,374.0L1390.0,374.0L1390.0,462.5C1390.0,549.7 1390.0,551.0 1392.0,553.0C1393.9,554.9 1395.3,555.0 1413.3,555.0C1428.1,555.0 1433.1,554.7 1434.5,553.6Z"/></svg>
    </a>
    <nav aria-label="Main" id="main-nav"><ul>
      <li><a href="#/churches" data-route="churches">Churches</a></li>
      <li><a href="#/ministries" data-route="ministries">Ministries</a></li>
      <li><a href="#/app" data-route="app">The app</a></li>
      <li><a href="#/events" data-route="events">Events</a></li>
      <li><a href="#/directory" data-route="directory">Directory</a></li>
      <li><a href="#/faq" data-route="faq">FAQs</a></li>
    </ul><div class="nav-foot"><div class="nav-more"><a href="#/about">About</a><a href="#/docs/introduction">Docs</a><a href="#/claim">Claim your church</a><a href="#/feedback">Ideas and problems</a></div><a class="btn btn-peach nav-cta" href="#/join">Get involved</a></div></nav>
    <a class="btn btn-peach" href="#/join">Get involved</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="main-nav" onclick="toggleMenu()"><span>Menu</span><i aria-hidden="true"></i></button>
  </div>
</header>
"""

# Home: rewrite in-page links to routes
home = home.replace('href="#join"', 'href="#/join"').replace('href="#how"', 'href="#/how"')
home = home.replace('<a class="btn btn-peach" href="#/join">Join as a church or ministry</a>', '<a class="btn btn-peach" href="#/join">Join as a church or ministry</a>')
home = home.replace('<p class="note">Evangelical and Pentecostal, in every state and territory, and growing every week. Every one can claim its page, and is verified before anyone is introduced to it.</p>',
 '<p class="note">Evangelical and Pentecostal, in every state and territory, and growing every week. Every one can claim its page, and is verified before anyone is introduced to it.</p><a class="btn btn-green" href="#/directory" style="margin-top:28px">Search the directory</a>')

script = """
const DIR = __DIR__;
const DOCS = __DOCS__;
const ORDER = __ORDER__;
document.body.classList.remove('no-js');

// Reveal on scroll
const io = 'IntersectionObserver' in window ? new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: 0.12 }) : null;
function watch(root) { root.querySelectorAll('.rv:not(.in)').forEach((el, i) => { el.style.transitionDelay = (i % 4) * 80 + 'ms'; io ? io.observe(el) : el.classList.add('in'); }); }

// Router
const pages = { home: 'page-home', directory: 'page-directory', about: 'page-about', docs: 'page-docs', churches: 'page-churches', ministries: 'page-ministries', app: 'page-app', faq: 'page-faq', events: 'page-events', claim: 'page-claim', feedback: 'page-feedback' };
const anchors = { join: 'join', how: 'how' };
function route() {
  const h = location.hash.replace(/^#\\/?/, '');
  const [first, second] = h.split('/');
  let page = 'home';
  if (pages[first] && first !== 'home') page = first;
  for (const [k, id] of Object.entries(pages)) document.getElementById(id).hidden = k !== page;
  document.querySelectorAll('nav a[data-route]').forEach((a) => a.toggleAttribute('aria-current', a.dataset.route === page) || a.setAttribute('aria-current', a.dataset.route === page ? 'page' : ''));
  document.querySelectorAll('nav a[data-route]').forEach((a) => { if (a.dataset.route === page) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current'); });
  if (page === 'docs') showDoc(second || 'introduction');
  if (page === 'directory') renderDir(true);
  if (page === 'claim') claimPick(second);
  if (page === 'feedback' && second === 'missing') { document.querySelector('#fb-form input[value=missing]').checked = true; fbKind(); }
  if (page === 'home' && anchors[first]) { requestAnimationFrame(() => document.getElementById(anchors[first]).scrollIntoView({ behavior: 'smooth' })); }
  else window.scrollTo(0, 0);
  const titles = { home: 'Always Foundation · Every response deserves a next step', directory: 'Directory · Always Foundation', about: 'About · Always Foundation', churches: 'For churches · Always Foundation', ministries: 'For ministries · Always Foundation', app: 'The Always app · Always Foundation', faq: 'FAQs · Always Foundation', events: 'Events · Always Foundation', claim: 'Claim your church · Always Foundation', feedback: 'Ideas and problems · Always Foundation' };
  if (page !== 'docs') document.title = titles[page];
  watch(document.getElementById(pages[page]));
}
window.addEventListener('hashchange', route);

// Docs
function showDoc(slug) {
  const d = DOCS[slug] || DOCS.introduction;
  const i = ORDER.indexOf(slug in DOCS ? slug : 'introduction');
  const prev = ORDER[i - 1], next = ORDER[i + 1];
  document.getElementById('doc').innerHTML =
    `<p class="crumb">${d.group}</p><h1>${d.title}</h1>${d.html}` +
    `<nav class="pager" aria-label="Next and previous">` +
    (prev ? `<a href="#/docs/${prev}"><span>Previous</span><b>${DOCS[prev].title}</b></a>` : '') +
    (next ? `<a class="next" href="#/docs/${next}"><span>Next</span><b>${DOCS[next].title}</b></a>` : '') + `</nav>`;
  document.querySelectorAll('.dnav a').forEach((a) => a.classList.toggle('on', a.dataset.slug === slug));
  document.getElementById('dpick').value = slug in DOCS ? slug : 'introduction';
  document.title = d.title + ' · Always docs';
}
document.getElementById('dsq').addEventListener('input', (e) => {
  const q = e.target.value.trim().toLowerCase();
  document.querySelectorAll('.dnav li').forEach((li) => {
    const slug = li.querySelector('a').dataset.slug;
    const hit = !q || DOCS[slug].title.toLowerCase().includes(q) || DOCS[slug].html.toLowerCase().includes(q);
    li.hidden = !hit;
  });
});

document.getElementById('dpick').addEventListener('change', (e) => { location.hash = '#/docs/' + e.target.value; });

// Directory
const STATUS = { Unverified: 'Listed', Claimed: 'Claimed', Verified: 'Verified', 'Verified youth': 'Verified youth' };
let shown = 0, matches = [];
const esc = (s) => String(s || '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));
function filterDir() {
  const q = document.getElementById('dq').value.trim().toLowerCase();
  const st = document.getElementById('ds').value, k = document.getElementById('dk').value;
  matches = DIR.filter((r) => (!st || r[4] === st) && (!k || r[1] === k) && (!q || (r[0] + ' ' + r[2] + ' ' + r[3]).toLowerCase().includes(q)));
}
function renderDir(reset) {
  if (reset) { filterDir(); shown = 0; document.getElementById('dlist').innerHTML = ''; }
  const list = document.getElementById('dlist');
  const slice = matches.slice(shown, shown + 30);
  if (!matches.length) list.innerHTML = '<div class="dir-empty" style="grid-column:1/-1">No churches or ministries match yet. Try a nearby suburb, or tell us about a church we\\'ve missed at hello@alwaysfoundation.org.</div>';
  list.insertAdjacentHTML('beforeend', slice.map((r) => `<article class="org"><h3>${esc(r[0])}</h3><p class="where">${esc([r[3], r[4]].filter(Boolean).join(', '))}</p><p class="den">${esc(r[2])}</p><div class="foot"><span class="badge ${r[1] === 'M' ? 'kind' : ''}">${r[1] === 'M' ? 'Ministry' : STATUS[r[5]] || 'Listed'}</span><button type="button" onclick="location.hash='#/claim/${DIR.indexOf(r)}'">Claim this page</button></div></article>`).join(''));
  shown += slice.length;
  document.getElementById('dcount').textContent = `${matches.length.toLocaleString('en-AU')} ${matches.length === 1 ? 'result' : 'results'}`;
  document.getElementById('dmore').hidden = shown >= matches.length;
}
let t;
['dq', 'ds', 'dk'].forEach((id) => document.getElementById(id).addEventListener('input', () => { clearTimeout(t); t = setTimeout(() => renderDir(true), 120); }));
document.getElementById('dmore').addEventListener('click', () => renderDir(false));

// Contact form
const FORM_ENDPOINT = ''; // Set to your form service URL when live. Messages go to hello@alwaysfoundation.org.
const form = document.getElementById('contact-form');
const status = document.getElementById('form-status');
form.addEventListener('submit', async (e) => {
  e.preventDefault();
  if (!form.checkValidity()) { status.textContent = 'Please add your name, a valid email address and a message.'; return; }
  if (!FORM_ENDPOINT) { status.textContent = 'The form is not connected yet. Please email hello@alwaysfoundation.org for now.'; return; }
  const b = form.querySelector('button'); b.disabled = true; b.textContent = 'Sending…';
  try { const r = await fetch(FORM_ENDPOINT, { method: 'POST', headers: { Accept: 'application/json' }, body: new FormData(form) }); if (!r.ok) throw 0; form.reset(); status.textContent = 'Message sent. We will be in touch soon.'; }
  catch { status.textContent = 'Your message could not be sent. Please email hello@alwaysfoundation.org.'; }
  finally { b.disabled = false; b.textContent = 'Send message'; }
});
function evf(){const s=document.getElementById('ev-s').value,k=document.getElementById('ev-k').value;let n=0;document.querySelectorAll('#ev-list .ev').forEach((e)=>{const on=(!s||e.dataset.s===s)&&(!k||e.dataset.k===k);e.hidden=!on;if(on)n++;});document.getElementById('ev-empty').hidden=n>0;}
['ev-s','ev-k'].forEach((id)=>document.getElementById(id).addEventListener('change',evf));

// ---------- claim a church
const API_BASE = ''; // Set to the Always API, e.g. https://api.alwaysfoundation.org, when live.
let claimRow = null;
function claimPick(i) {
  const r = DIR[+i];
  claimRow = Number.isInteger(+i) && r ? r : null;
  document.getElementById('cl-name').textContent = claimRow ? claimRow[0] : 'Choose your church';
  document.getElementById('cl-where').textContent = claimRow ? [claimRow[3], claimRow[4]].filter(Boolean).join(', ') + ' · ' + claimRow[2] : 'Search below, or pick it from the directory.';
  document.getElementById('cl-results').innerHTML = '';
  document.getElementById('claim-form').hidden = false; document.getElementById('cl-done').hidden = true;
}
document.getElementById('cl-q').addEventListener('input', (e) => {
  const q = e.target.value.trim().toLowerCase();
  const m = q.length < 2 ? [] : DIR.map((r, i) => [r, i]).filter(([r]) => (r[0] + ' ' + r[3]).toLowerCase().includes(q)).slice(0, 6);
  const box = document.getElementById('cl-results');
  box.innerHTML = m.map(([r, i]) => `<button type="button" data-i="${i}"><b>${esc(r[0])}</b> <span>· ${esc([r[3], r[4]].filter(Boolean).join(', '))}</span></button>`).join('');
  box.querySelectorAll('button').forEach((b) => b.onclick = () => { location.hash = '#/claim/' + b.dataset.i; e.target.value = ''; });
});
async function sendJSON(path, body) {
  if (!API_BASE) return true; // prototype: no API connected yet
  const r = await fetch(API_BASE + path, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body) });
  return r.ok;
}
document.getElementById('claim-form').addEventListener('submit', async (e) => {
  e.preventDefault(); const f = e.target, st = document.getElementById('cl-status');
  if (!claimRow) { st.textContent = 'Search for your church first.'; return; }
  if (!f.checkValidity()) { st.textContent = 'Please add your name, role and work email, and tick the box.'; return; }
  const d = Object.fromEntries(new FormData(f));
  st.textContent = 'Sending…';
  const ok = await sendJSON(`/v1/orgs/${encodeURIComponent(claimRow[0])}/claims`, { email: d.email, role: d.role, evidence: [d.name, d.evidence].filter(Boolean).join(' · ') }).catch(() => false);
  if (!ok) { st.textContent = 'Your claim could not be sent. Please email hello@alwaysfoundation.org.'; return; }
  st.textContent = ''; f.reset(); f.hidden = true; document.getElementById('cl-done').hidden = false;
});
// ---------- ideas and problems
function fbKind() {
  const k = document.querySelector('#fb-form input[name=kind]:checked').value;
  document.getElementById('fb-msg-l').firstChild.textContent = k === 'bug' ? 'What happened, and what did you expect?' : k === 'missing' ? 'The church or ministry: name, suburb and website' : 'Tell us more';
}
document.querySelectorAll('#fb-form input[name=kind]').forEach((r) => r.addEventListener('change', fbKind));
document.getElementById('fb-form').addEventListener('submit', async (e) => {
  e.preventDefault(); const f = e.target, st = document.getElementById('fb-status');
  if (!f.checkValidity()) { st.textContent = 'Please tell us a little more.'; return; }
  const d = Object.fromEntries(new FormData(f)); st.textContent = 'Sending…';
  const ok = await sendJSON('/v1/feedback', d).catch(() => false);
  if (!ok) { st.textContent = 'Your message could not be sent. Please email hello@alwaysfoundation.org.'; return; }
  st.textContent = ''; [...f.querySelectorAll('label, .fb-kinds, button')].forEach((x) => x.hidden = true); document.getElementById('fb-done').hidden = false;
});


function toggleMenu(force) {
  const h = document.querySelector('header'), open = force ?? !h.classList.contains('open');
  h.classList.toggle('open', open); document.body.classList.toggle('menu-open', open);
  const b = h.querySelector('.menu-btn'); b.setAttribute('aria-expanded', open); b.querySelector('span').textContent = open ? 'Close' : 'Menu';
}
addEventListener('hashchange', () => toggleMenu(false));
addEventListener('keydown', (e) => { if (e.key === 'Escape') toggleMenu(false); });
document.querySelectorAll('.pg-faq-nav a').forEach((a) => a.addEventListener('click', (e) => { e.preventDefault(); document.getElementById(a.getAttribute('href').slice(1)).scrollIntoView({ behavior: 'smooth' }); }));
route();
""" + extras.JS
script = script.replace('__DIR__', directory).replace('__DOCS__', json.dumps(pages_json, ensure_ascii=False)).replace('__ORDER__', json.dumps(order))

footer = """
<footer>
  <div class="wrap">
    <a class="brand" href="#/"><svg class="wm" viewBox="186 250 1328 366" role="img" aria-label="Always Foundation"><path fill="#F8F3EA" fill-rule="evenodd" d="M1030.8,608.4C1046.2,605.2 1061.0,596.1 1069.8,584.4C1077.9,573.6 1081.9,564.7 1101.5,514.5C1111.9,488.1 1128.3,446.2 1138.0,421.5C1147.8,396.8 1157.6,371.4 1160.0,365.2C1166.0,349.0 1167.7,350.0 1134.5,350.0C1109.8,350.0 1108.2,350.1 1106.6,351.9C1105.6,353.0 1101.7,362.3 1097.9,372.7C1094.1,383.0 1084.8,408.5 1077.3,429.2C1069.7,450.0 1063.2,467.0 1062.9,467.0C1062.5,467.0 1059.3,459.7 1055.7,450.8C1050.1,437.0 1029.3,386.6 1018.0,359.7C1016.3,355.5 1014.0,351.5 1013.0,351.0C1010.4,349.6 958.5,349.7 955.9,351.0C954.9,351.6 954.0,352.9 954.0,353.8C954.0,354.8 957.1,362.3 960.8,370.5C964.6,378.8 970.4,391.6 973.7,399.0C977.1,406.4 984.1,421.9 989.3,433.5C994.5,445.1 1006.2,470.9 1015.3,491.0C1024.3,511.1 1032.8,529.9 1034.0,532.8L1036.3,538.1L1033.5,544.6C1030.1,552.5 1024.9,557.3 1017.8,559.0C1011.6,560.5 1006.1,559.8 997.5,556.4C992.7,554.5 990.3,554.0 989.2,554.7C987.3,555.8 972.0,589.2 971.3,593.7C970.8,596.5 971.2,597.1 974.1,598.9C979.3,602.1 993.4,606.9 1001.9,608.4C1012.2,610.3 1021.6,610.3 1030.8,608.4ZM290.8,550.7C302.4,547.4 313.4,541.1 323.4,531.9L329.0,526.8L329.0,535.7C329.0,549.8 327.2,549.0 357.1,549.0C380.7,549.0 382.1,548.9 384.0,547.0C386.0,545.0 386.0,543.7 386.0,483.1C386.0,444.5 385.6,418.2 384.9,413.3C383.4,401.9 378.4,387.9 373.0,379.6C358.9,358.1 334.9,346.8 299.9,345.3C277.1,344.3 257.2,348.0 239.4,356.4C226.2,362.7 215.0,370.6 215.0,373.6C215.0,375.3 233.4,404.2 235.2,405.3C236.3,406.0 239.8,404.8 248.1,400.7C261.5,394.2 269.0,392.1 282.1,391.3C303.0,390.0 319.1,396.4 325.2,408.4C327.2,412.2 329.2,428.0 327.7,428.0C327.4,428.0 322.5,426.5 316.8,424.6C295.5,417.5 273.2,416.4 252.2,421.5C224.5,428.2 206.5,443.5 198.5,467.1C196.0,474.4 195.6,477.0 195.6,487.5C195.5,497.4 195.9,500.8 197.9,507.0C204.9,529.9 224.5,546.4 251.1,552.0C257.5,553.3 284.5,552.4 290.8,550.7ZM861.0,550.9C872.2,548.3 882.3,543.1 892.6,534.8C897.2,531.0 901.1,528.0 901.2,528.0C901.4,528.0 901.5,532.1 901.5,537.1C901.5,544.9 901.8,546.4 903.4,547.6C905.0,548.7 910.3,549.0 930.1,549.0C954.6,549.0 954.9,549.0 956.4,546.8C957.8,544.8 958.0,537.0 958.0,482.3C958.0,443.7 957.6,417.2 956.9,412.3C953.3,385.7 940.3,366.7 917.8,355.4C898.3,345.6 866.7,342.3 840.2,347.5C824.4,350.5 804.6,358.9 792.8,367.6C786.6,372.0 786.6,374.0 792.8,383.3C795.5,387.3 799.8,394.0 802.4,398.2C805.1,402.5 807.8,406.0 808.6,406.0C809.4,406.0 813.9,404.0 818.7,401.6C837.7,392.0 856.9,388.8 874.3,392.5C891.6,396.1 901.0,406.8 901.0,422.7C901.0,425.6 900.9,428.0 900.7,428.0C900.5,428.0 896.4,426.6 891.5,425.0C877.3,420.2 867.3,418.6 851.0,418.6C829.0,418.7 812.5,423.2 797.0,433.5C785.0,441.5 775.9,453.5 771.3,467.4C769.1,474.3 768.7,477.3 768.7,488.0C768.6,499.1 768.9,501.4 771.4,508.5C772.9,512.9 775.7,519.0 777.5,522.0C781.3,528.2 790.3,537.2 796.6,541.2C802.7,545.1 814.3,549.8 821.8,551.4C832.1,553.6 850.8,553.4 861.0,550.9ZM1262.7,550.6C1300.7,542.3 1323.0,511.4 1316.6,476.0C1314.6,464.6 1309.4,454.4 1302.1,447.1C1291.7,436.8 1278.0,430.6 1246.5,422.0C1221.5,415.1 1216.0,411.8 1216.0,403.5C1216.0,396.2 1221.1,392.0 1232.5,389.9C1243.3,387.9 1260.8,392.6 1275.7,401.7C1279.6,404.0 1283.8,406.0 1284.9,406.0C1286.2,406.0 1287.9,404.6 1289.4,402.2C1299.6,386.1 1307.0,373.7 1307.0,372.5C1307.0,369.2 1289.4,357.6 1276.7,352.6C1250.2,342.1 1217.5,342.8 1194.5,354.3C1173.0,365.0 1160.8,382.2 1159.4,403.8C1158.2,420.7 1162.9,434.0 1173.9,445.0C1184.4,455.4 1195.2,460.2 1237.6,473.0C1256.3,478.7 1263.4,486.5 1258.6,495.8C1254.9,503.0 1247.9,506.0 1235.0,506.0C1219.7,506.0 1204.7,500.8 1187.4,489.5C1182.2,486.1 1177.9,484.0 1176.6,484.2C1175.2,484.4 1171.1,489.3 1163.8,499.5C1149.3,519.8 1149.9,518.3 1154.1,522.6C1158.9,527.6 1172.1,536.3 1182.1,540.9C1192.1,545.6 1208.7,550.6 1218.5,551.9C1228.5,553.3 1254.1,552.5 1262.7,550.6ZM460.6,547.6C462.5,546.2 462.5,543.5 462.8,411.9C463.0,292.7 462.9,277.4 461.5,275.3L460.0,273.0L434.1,273.0C411.9,273.0 408.1,273.2 407.0,274.6C405.9,275.8 405.7,292.4 405.8,357.3C406.0,558.6 405.9,545.7 407.6,547.4C409.8,549.7 457.5,549.8 460.6,547.6ZM585.3,547.8C586.2,547.1 590.1,538.0 593.9,527.5C618.9,459.0 626.2,439.4 627.0,438.6C627.6,438.0 628.0,437.9 628.0,438.2C628.0,438.5 633.7,454.5 640.6,473.7C647.5,492.8 656.1,516.8 659.7,527.0C663.5,537.7 667.1,546.2 668.2,547.2C670.0,548.8 672.8,549.0 693.5,549.0C715.1,549.0 716.8,548.9 718.4,547.1C719.4,546.0 726.9,525.4 735.0,501.3C743.2,477.2 757.7,434.3 767.4,405.9C783.6,358.1 784.8,354.1 783.4,352.1C781.9,350.1 781.3,350.0 756.1,350.0C732.9,350.0 730.0,350.2 728.1,351.8C726.7,353.0 722.8,363.7 715.1,388.0C709.1,407.0 701.4,431.2 698.0,441.9C694.6,452.5 691.5,460.8 691.1,460.4C690.6,459.9 687.5,451.4 684.0,441.5C675.5,417.0 657.5,366.0 654.4,357.8C653.0,354.2 651.2,350.9 650.4,350.6C649.5,350.3 639.4,350.0 627.9,350.0C609.1,350.0 606.8,350.2 605.2,351.8C604.2,352.8 600.8,361.0 597.6,370.1C594.4,379.1 587.2,399.3 581.5,415.0C575.9,430.7 569.8,447.7 568.0,452.8C566.2,457.9 564.5,461.9 564.3,461.7C564.1,461.4 562.1,455.2 559.9,447.9C557.6,440.5 554.1,429.1 552.1,422.5C550.0,415.9 544.4,397.7 539.5,382.0C534.7,366.3 530.0,352.7 529.2,351.8C527.8,350.2 525.2,350.0 500.9,350.0C477.9,350.0 473.9,350.2 472.6,351.6C471.7,352.4 471.0,353.5 471.0,353.8C471.0,354.2 475.5,368.0 481.0,384.5C489.8,410.8 510.4,474.5 527.4,528.0C530.5,537.7 533.8,546.4 534.7,547.3C536.2,548.8 539.1,549.0 560.0,549.0C577.3,549.0 584.1,548.7 585.3,547.8ZM276.4,509.0C266.5,507.0 258.1,501.8 254.2,495.1C252.0,491.4 251.5,489.3 251.5,484.0C251.5,476.0 254.8,469.6 261.7,464.6C269.8,458.7 274.8,457.5 290.5,457.5C305.4,457.5 311.7,458.9 323.2,464.7L328.0,467.0L328.0,474.4C328.0,480.5 327.5,482.6 324.9,487.8C317.1,503.5 295.8,512.8 276.4,509.0ZM848.3,509.0C825.1,504.1 816.4,482.6 831.5,467.5C838.7,460.2 845.3,457.9 860.1,457.2C873.5,456.7 882.8,458.5 894.4,464.1L901.2,467.4L900.8,474.9C899.9,489.9 890.4,501.5 874.6,507.0C867.8,509.3 854.5,510.3 848.3,509.0Z"/><path fill="#EE8B54" d="M1434.5,553.6C1436.3,552.3 1436.4,549.1 1436.4,463.1L1436.5,374.0L1468.9,374.0C1497.7,374.0 1501.5,373.8 1503.2,372.3C1504.8,370.9 1505.0,368.9 1505.0,352.8C1505.0,342.3 1504.6,334.1 1504.0,332.9C1503.0,331.1 1501.5,331.0 1470.0,331.0L1437.0,331.0L1437.0,296.4C1437.0,274.5 1436.6,261.2 1436.0,259.9C1435.0,258.1 1433.7,258.0 1413.4,258.0L1392.0,258.0L1391.0,260.6C1390.4,262.0 1390.0,277.4 1390.0,297.1L1390.0,331.0L1357.7,331.0C1333.9,331.0 1325.1,331.3 1324.2,332.2C1323.3,333.1 1323.0,339.0 1323.0,352.7C1323.0,370.7 1323.1,372.0 1324.9,373.0C1326.2,373.6 1338.6,374.0 1358.4,374.0L1390.0,374.0L1390.0,462.5C1390.0,549.7 1390.0,551.0 1392.0,553.0C1393.9,554.9 1395.3,555.0 1413.3,555.0C1428.1,555.0 1433.1,554.7 1434.5,553.6Z"/></svg></a>
    <span><a href="#/churches">For churches</a> · <a href="#/ministries">For ministries</a> · <a href="#/app">The app</a> · <a href="#/about">About</a> · <a href="#/docs/introduction">Docs</a> · <a href="#/faq">FAQs</a> · <a href="#/feedback">Ideas and problems</a> · <a href="#/docs/privacy">Privacy</a></span>
    <span><a href="mailto:hello@alwaysfoundation.org">hello@alwaysfoundation.org</a> · <a href="https://github.com/alwaysfoundation">Open source</a></span>
  </div>
</footer>
"""

doc = f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='14' fill='%23033D2B'/><path fill='%23EE8B54' d='M29 10h6v12h12v6H35v26h-6V28H17v-6h12z'/></svg>">
<title>Always Foundation · Every response deserves a next step</title>
<meta name="description" content="No one who responds to Jesus should walk alone. Always connects the body of Christ in Australia, so everyone who responds is offered their next best faith step.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=Inter:wght@400;500;600&family=Newsreader:opsz,wght@6..72,400&display=swap" rel="stylesheet">
<style>{css}{extra_css}{extras.CSS}{P.CSS}{P.EVENTS_CSS}{P.CLAIM_CSS}</style>
</head>
<body class="no-js">
<a class="skip" href="#main">Skip to content</a>
{header}
<main id="main">
<div class="page" id="page-home">{home}</div>
<div class="page" id="page-directory" hidden>{directory_page}</div>
<div class="page" id="page-about" hidden>{about}</div>
<div class="page" id="page-docs" hidden>{docs_page}</div>
<div class="page" id="page-churches" hidden>{P.CHURCHES}</div>
<div class="page" id="page-ministries" hidden>{P.MINISTRIES}</div>
<div class="page" id="page-app" hidden>{P.APP}</div>
<div class="page" id="page-faq" hidden>{P.FAQ}</div>
<div class="page" id="page-events" hidden>{P.EVENTS}</div>
<div class="page" id="page-claim" hidden>{P.CLAIM}</div>
<div class="page" id="page-feedback" hidden>{P.FEEDBACK}</div>
</main>
{footer}
<script>{script}</script>
</body>
</html>
"""

# ---------- optional photos: drop files into af-web/img/ and rebuild
import base64 as _b64, glob as _glob
PHOTOS = {  # name: (anchor to insert before, alt text, credit)
  'friends': ('<section class="sec story" id="stories">', 'Friends talking together outdoors', 'Nathan Mullet'),
  'baptism': ('<section class="sec pg-sec"', 'A baptism in the ocean', 'Vitaly Gariev'),
}
_credits = []
for _n, (_anchor, _alt, _by) in PHOTOS.items():
    _f = sorted(_glob.glob(os.path.join(ROOT, 'img', f'{_n}.*')))
    if not _f or _anchor not in doc: continue
    _ext = _f[0].rsplit('.', 1)[1].lower().replace('jpg', 'jpeg')
    _uri = f'data:image/{_ext};base64,' + _b64.b64encode(open(_f[0], 'rb').read()).decode()
    _fig = f'<figure class="photo-band"><img src="{_uri}" alt="{_alt}" loading="lazy"></figure>\n'
    _i = doc.index(_anchor) if _n == 'friends' else doc.index(_anchor, doc.index('id="page-churches"'))
    doc = doc[:_i] + _fig + doc[_i:]
    _credits.append(_by)
if _credits:
    doc = doc.replace('</footer>', f'<p class="photo-credit">Photos from Unsplash under the Unsplash License: {", ".join(_credits)}.</p></footer>', 1)
    doc = doc.replace('</style>', '.photo-band{margin:0;height:min(62vh,560px);overflow:hidden}.photo-band img{width:100%;height:100%;object-fit:cover;display:block}.photo-credit{font-size:12px;opacity:.65;text-align:center;margin:18px 0 0}</style>', 1)
print('photos', _credits)
open(os.path.join(ROOT, '..', 'index.html'), 'w').write(doc)
print('pages', len(order), 'bytes', len(doc))
