"""Assemble the Always Foundation website: home, directory, about and docs in one page with hash routes."""
import json, html, os
import os
ROOT = os.path.dirname(os.path.abspath(__file__))

css = open(os.path.join(ROOT,'base.css')).read()
home = open(os.path.join(ROOT,'main.html')).read()
import extras, pages as P, re as _re
import compliance_page as CP
import products as PR
import polish as PO
import developers as DV
import contact as CF
import join as JN
def _swap(h, marker, new):
    i = h.find(marker); a = h.rfind('<section', 0, i); b = h.find('</section>', i) + 10
    return h[:a] + new + h[b:]
home = _swap(home, 'class="sec map"', '')
home = home.replace('{{PILLARS}}', PR.product_bento()).replace('{{SOLUTIONS}}', PR.solutions_grid('hsx'))
import base64 as _b
import io as _io
from PIL import Image as _Im
def _photo(name, maxw=800, q=64):
  """Resize to WebP, write to /img beside index.html, return the relative URL (served by the Worker, cached)."""
  im = _Im.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', name)).convert('RGB')
  if im.width > maxw: im = im.resize((maxw, round(im.height * maxw / im.width)), _Im.LANCZOS)
  out = os.path.splitext(name)[0] + '.webp'
  os.makedirs(os.path.join(ROOT, '..', 'img'), exist_ok=True)
  im.save(os.path.join(ROOT, '..', 'img', out), 'WEBP', quality=q, method=6)
  return 'img/' + out
home = home.replace('{{UEN_STUDIO}}', _photo('uen-studio.jpg'))
home = home.replace('{{CXMMXNS_IMG}}', _photo('cxmmxns-tour.jpg'))
home = home.replace('{{ALPHA_IMG}}', _photo('alpha-photo.jpg'))
import shutil as _sh; os.makedirs(os.path.join(ROOT, '..', 'img'), exist_ok=True); _sh.copyfile(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', 'alpha-logo.png'), os.path.join(ROOT, '..', 'img', 'alpha-logo.png'))
home = home.replace('{{ALPHA_LOGO}}', 'img/alpha-logo.png')
home = home.replace('{{SYDNEYFIRE_IMG}}', _photo('sydneyfire-street.jpg'))
home = home.replace('{{REJOICE_IMG}}', _photo('rejoice-team.jpg'))
home = home.replace('{{UEN_IMG}}', _photo('uen-event.jpg'))
FAITHTECH_IMG = _photo('faithtech.png', maxw=1600, q=84)
home = _swap(home, 'class="sec promise"', '')
  # 'Watch it work' removed
directory = open(os.path.join(ROOT,'dir.json')).read()
COUNT = len(json.loads(directory))

# ---------------------------------------------------------------- Docs content
# Written as if the platform is live: this is the documentation people will read.
DOCS = [
 ("Getting started", [
  ("introduction", "Introduction", """
<p class="lead">Always Platform connects churches and ministries across Australia, so everyone who says yes to Jesus has a next step and a real person to walk with.</p>
<p>Every week people respond to Jesus at concerts, camps, services, film screenings and online. Always Platform makes sure that moment becomes a next step. The person chooses what would help and sees who will reach out. Then a local church gets in touch. If no one can, our care team helps.</p>
<h2>Who Always Platform is for</h2>
<ul>
<li><b>Churches</b> claim their page on the map, receive introductions and welcome people from their phone. Free, always.</li>
<li><b>Ministries and events</b> (tours, camps, youth events, campus and street outreach, media) give everyone who says yes a safe next step, under their own name if they like.</li>
<li><b>People who respond</b> get a clear choice, a real person, and control of their own story.</li>
<li><b>Builders</b> add Always Platform to church and ministry apps with its API and SDK.</li>
</ul>
<div class="callout">New here? Read <a href="#/docs/how-it-works">How Always Platform works</a>, then the guide for your role in the sidebar.</div>
"""),
  ("how-it-works", "How Always Platform works", """
<p class="lead">Respond. Connect. Walk. Someone responds to Jesus, they're introduced to their next best faith step nearby, and a real person walks with them.</p>
<h2>1. Someone responds</h2>
<p>At an event, a service or online, the person opens a response card (a QR code, a link or a ministry's own app). They choose what would help: a church, a course, someone to talk to, a youth group or reading the Bible. They give their first name, a mobile and their suburb, and agree to share them with a church or ministry nearby.</p>
<h2>2. They're connected</h2>
<p>Always Platform offers them to the nearest verified church or ministry that offers that next step, has room this month and speaks their language. It accepts, or passes with a reason, and the next one nearby that fits is offered.</p>
<h2>3. A real person walks with them</h2>
<p>Once a church accepts, it sees the person's contact details and reaches out from its own phone. The person gets a text saying who will be in touch. The church notes that they've been in touch (never what was said) and keeps going: coffee, Sunday together, a small group.</p>
<h2>The care team</h2>
<p>If no church or ministry can take someone, the Always care team helps, so everyone is offered a next step.</p>
<h2>Only the person says "connected"</h2>
<p>We count someone as connected only when they confirm it themselves, through the link in their text. That is the number we report, including the people we missed.</p>
"""),
  ("glossary", "Glossary", """
<dl class="gloss">
<dt>Response</dt><dd>Someone telling us they responded to Jesus and would like a next step, with their consent.</dd>
<dt>Next best faith step</dt><dd>What would help most right now: usually a local church, sometimes a course, a youth group or care.</dd>
<dt>Introduction</dt><dd>An invitation to a church or ministry nearby to welcome a person. Their details are shared only once it accepts.</dd>

<dt>Care team</dt><dd>Trained Always staff and volunteers who say hello and walk with anyone no church could take.</dd>
<dt>Listed, claimed, verified</dt><dd>Every church starts as a listing on the map. A claimed page is managed by the church. A verified church has been checked with its denomination or network and can receive introductions. Verified youth partners can receive young people.</dd>
<dt>Consent receipt</dt><dd>A record of what the person agreed to, who may see their details, and the exact words they saw.</dd>
<dt>Sender</dt><dd>A ministry, event or app that passes responses to the network.</dd>
<dt>Always Network</dt><dd>The churches and ministries connected through Always Platform. It grew out of an earlier project called Branches.</dd>
<dt>Welcoming now</dt><dd>A church or ministry that is verified, trained, has room this month and answers introductions on time.</dd>
<dt>Always Agent</dt><dd>An assistant that helps teams with the admin around a welcome, with a person deciding every step.</dd>
</dl>
"""),
 ]),
 ("For churches", [
  ("claim", "Claim your church's page", """
<p class="lead">Every evangelical and Pentecostal church in Australia is on the map. Claiming your page is free and takes about ten minutes.</p>
<ol>
<li>Go to <a href="#/claim">Claim your church</a>.</li>
<li>Tell us your role (pastor, elder, administrator, connect lead) and how we can confirm it, such as your listing on your denomination's website.</li>
<li>We check with your denomination or network and email you when your page is ready.</li>
<li>Once confirmed, invite your team and set up your page, next steps and capacity.</li>
</ol>
<h2>Becoming verified</h2>
<p>Before receiving introductions, a church is verified. It affirms the Nicene Creed, belongs to a denomination or network (or has two references from verified churches), and has a connect lead who has done the 20-minute welcoming course. To receive young people, a church is verified as a youth partner, which adds Working With Children Checks and a child-safe policy.</p>
"""),
  ("inbox", "Welcome from your phone", """
<p class="lead">The Always Connect inbox works in any phone's browser. It shows everyone you're walking with, what they asked for and what's due.</p>
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
  ("ready", "Ready to welcome", """
<p class="lead">Churches marked <b>welcoming now</b> are ready to receive people this month.</p>
<p>A church or ministry is welcoming now when:</p>
<ol>
<li>It's verified with its denomination or network.</li>
<li>Its connect lead has done the short welcoming course.</li>
<li>It offers at least one next step and has room this month.</li>
<li>It has checked its details in the last 90 days.</li>
<li>It usually accepts or passes introductions on time.</li>
</ol>
<p>If things get busy, introductions pause until you're ready again. Nothing is removed, and only your own team sees your response times.</p>
<h2>Welcoming young people</h2>
<p>You'll also need a child safe policy, a named child safety contact, and current Working With Children Checks for your youth leaders. We remind you before a check expires.</p>
<h2>Who sees what</h2>
<p>Everyone sees your name, suburb, the next steps you offer and the badge. Partner ministries can check readiness through the API so they can offer people a church nearby. Capacity and response times stay private.</p>
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
<li>Create a campaign for your event or tour in Always for ministries.</li>
<li>Add placements: a QR code for the screen, a short link, an armband card, or the response card inside your app.</li>
<li>People respond on their own phones. Volunteers can capture a conversation for someone too, with their consent.</li>
<li>Each person is offered to a verified church or ministry near where they live, anywhere in Australia.</li>
</ol>
<h2>What you see</h2>
<p>You see how many people responded and how many were received, accepted and connected. Their details stay with the church that welcomes them. If a person agrees, you'll also see that they connected.</p>
"""),
  ("branding", "Custom branding", """
<p class="lead">Run Always Platform under your own brand. Same promise, your look and voice.</p>
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
<li><b>Churches and ministries add their own</b> when they sign in to Always. Verified partners publish straight away.</li>
<li><b>Our team adds major events</b>, like tours and conferences.</li>
<li><b>Anyone can suggest an event.</b> Our team checks it before it shows.</li>
<li><b>Ticketing platforms.</b> Organisers can bring in events from their ticketing account, where the platform allows it. We're talking with platforms about doing this well.</li>
</ol>
<h2>Where events show</h2>
<p>On our Events page, in the Connect tab of Always App, and through the API so other apps can list them too.</p>
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
  ("results", "Reports for your funders", """
<p class="lead">If donors, a foundation or your denomination fund your ministry, Always Platform writes your report for you, every month.</p>
<p>Always Platform already knows each step a person takes after they respond, so there is nothing extra to enter. Pick a month, a quarter or the financial year, and your report is ready.</p>
<h2>What's in a report</h2>
<ol>
<li>The journey: how many people responded, were introduced, were accepted, were contacted and are connected.</li>
<li>What people asked for, like finding a church or exploring faith.</li>
<li>Where they live, by state.</li>
<li>Month by month, so you can show the trend.</li>
<li>A short story, only when the person has agreed to share it.</li>
<li>Plain definitions of every number, so your funder knows exactly what each one means.</li>
</ol>
<h2>An example</h2>
<table class="doc-table"><thead><tr><th scope="col">City worship tour, July to September</th><th scope="col">People</th></tr></thead><tbody>
<tr><th scope="row">Responded</th><td>1,240</td></tr>
<tr><th scope="row">Introduced to a church nearby</th><td>1,188</td></tr>
<tr><th scope="row">Accepted by that church</th><td>1,046</td></tr>
<tr><th scope="row">Contacted</th><td>962</td></tr>
<tr><th scope="row">Told us they are connected</th><td>418</td></tr>
</tbody></table>
<p><small>Every figure here is made up.</small></p>
<h2>Sharing it</h2>
<p>Download it as a PDF or a spreadsheet, or send your funder a link. A link shows the report exactly as it was when you made it, and you can switch it off any time. Add your own title, your funder's name and a short introduction.</p>
<h2>Keeping people safe</h2>
<p>Reports show totals only. Any figure under 10 people, or 20 where young people are included, is shown as "too few to show", so no one can be identified. No funder ever sees a person's name or details.</p>
<h2>Fair credit</h2>
<p>Each ministry sees what happened to the people it introduced, and each church sees the people it welcomed. Every number is counted once, using the same definitions across the whole network, so reports from different ministries can be compared fairly.</p>
"""),
  ("compliance", "Compliance made simple", """
<p class="lead">The privacy and child safety paperwork, kept for you as you go.</p>
<p>Each church and ministry gets a Compliance tab with records you can export when your board, denomination or insurer asks.</p>
<ul>
<li><b>Consent register</b>: every permission, what it covered, the wording shown, and any withdrawal.</li>
<li><b>Privacy requests</b>: people see, download, correct or delete their details from their own link.</li>
<li><b>Data breaches</b>: a register, the 30-day assessment checklist, and draft notices if one is ever needed.</li>
<li><b>Child safety</b>: a checklist against the National Principles for Child Safe Organisations, Working With Children Check reminders, and your child safety contact.</li>
<li><b>Retention</b>: proof that details were deleted on schedule.</li>
<li><b>Audit trail</b>: a tamper-evident log of who opened what, and why.</li>
<li><b>Annual reporting</b>: activity totals ready for your ACNC return.</li>
</ul>
<p>The Compliance tab shows records and dates, never people's details. Child safety incidents stay in your own safeguarding system, kept for at least 45 years as the Royal Commission recommended.</p>
<p><small>Always Platform helps you keep good records. It isn't legal advice; check your obligations with your own adviser.</small></p>
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
  ("consent", "How consent works", """
<p class="lead">Consent travels with the person. Every system checks it before it acts.</p>
<p>Every person carries a consent receipt everywhere their details go. It records what they agreed to, who may see their details, who agreed (them or a parent), their age group and the words they saw. Every system that touches the person checks it first and fails closed: anything not explicitly allowed is refused. Withdrawal is one tap and reaches everyone holding their details.</p>
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
  ("journey", "One journey, with consent", """
<p class="lead">Help people take the next step without starting from scratch each time, and only with their permission.</p>
<p>When someone responds at a second event, the ministry can see they're already connected with a church, so nobody asks the same questions twice or loses track of them.</p>
<ul>
<li>Shared only if the person agrees, and only the steps (which church, which step, when), never notes.</li>
<li>No one can search for people or browse a list. It's not a mailing list or a CRM.</li>
<li>Withdraw once and it stops everywhere: every church and ministry is told straight away.</li>
<li>Never for anyone under 18. Each young person's response stands alone.</li>
</ul>
<p>Moving between church systems uses the open Always Handoff standard, starting with Elvanto and Planning Center.</p>
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
  ("api", "Always Platform API", """
<p class="lead">A REST API (OpenAPI 3.1) for sending responses, receiving introductions, managing a page and reading the church feed. Hosted in Sydney.</p>
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
  ("sdk", "Always Platform SDK", """
<p class="lead">Add Always Platform to any church or ministry app in about ten minutes.</p>
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
  ("feed", "Church feed and finder", """
<p class="lead">Point people to verified churches near them, from your own website, app or AI tool. Free.</p>
<p>The church feed lists churches that chose to be included: name, suburb, denomination, service times, the next steps they offer, and whether they're <b>welcoming now</b>. It never includes anyone's personal details.</p>
<h2>Add "Find a church near me" to your site</h2>
<pre><code>&lt;script type="module" src="https://cdn.alwaysfoundation.org/sdk/v0/finder.js"&gt;&lt;/script&gt;
&lt;always-church-finder accent="#1B4740"&gt;&lt;/always-church-finder&gt;</code></pre>
<p>Add <code>step="youth"</code> to show youth groups, or <code>youth</code> to show only verified youth partners.</p>
<h2>Use the feed in your code</h2>
<pre><code>import { AlwaysClient } from '@always/sdk';

const always = new AlwaysClient();
const { items } = await always.feed.churches({ postcode: '2150', welcoming: true });
const check = await always.feed.verify('hope-parramatta');</code></pre>
<h2>Or call it directly</h2>
<pre><code>GET https://api.alwaysfoundation.org/v1/feed/churches?postcode=2150&amp;welcoming=true
GET https://api.alwaysfoundation.org/v1/feed/churches.jsonl
GET https://api.alwaysfoundation.org/v1/verify/hope-parramatta</code></pre>
<p>No key is needed to start. For an app or a daily download, ask for a free developer key at <b>hello@alwaysfoundation.org</b>, so we can let you know about changes.</p>
<h2>Fair use</h2>
<ul>
<li>Show churches as they are, and link to their Always page.</li>
<li>Credit "Always church feed".</li>
<li>Don't use the feed to contact churches with marketing.</li>
</ul>
"""),
  ("mcp", "Always for AI assistants", """
<p class="lead">Use Always Platform from Claude and other AI assistants, safely.</p>
<p>The Always MCP server gives an assistant four tools. All of them read public church information only, so no one's personal details are ever involved.</p>
<ul>
<li><b>find_churches</b>: churches near a postcode, with filters for welcoming now, youth partners and next steps.</li>
<li><b>verify_church</b>: whether a church is verified, and whether it welcomes young people.</li>
<li><b>list_events</b>: upcoming Christian events.</li>
<li><b>how_always_works</b>: a short guide, so the assistant explains Always Platform accurately.</li>
</ul>
<h2>Connect it</h2>
<pre><code>https://api.alwaysfoundation.org/mcp</code></pre>
<p>Add it as a custom connector in your assistant. Agents can also read <code>https://api.alwaysfoundation.org/llms.txt</code>.</p>
<h2>What it never does</h2>
<ul>
<li>Touch any young person's information.</li>
<li>See anyone who has responded, or any church's inbox.</li>
<li>Act on its own. Future tools that help a team with adults who agreed to AI help will always need a person to press send.</li>
</ul>
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
<p class="lead">YouVersion opens the technology behind the Bible App to ministries. Always Platform uses it in three places.</p>
<ol>
<li><b>Scripture from the first step.</b> Choosing "Start reading the Bible" opens a reading plan in the person's language, while a church gets in touch.</li>
<li><b>Sign in with YouVersion.</b> People can sign in with the account they already use. If they agree, Always Platform links it to their home church, so their church stays with them across member apps.</li>
<li><b>Every member app starts with Scripture.</b> Apps built on Always Platform can add the Bible reader in a few lines. Free, with no ads.</li>
</ol>
<p>YouVersion confirms who someone is. Always Platform holds which church they belong to and what they agreed to share. Neither holds the other's data.</p>
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
<li>Saying yes to Jesus is about your faith, which Australian privacy law treats as sensitive. So nothing is shared without your clear permission.</li>
<li>You see who will reach out before anything is shared, and it goes only to the church or ministry that welcomes you.</li>
<li>Your information stays in Australia, encrypted.</li>
<li>See, download or delete what we hold at any time, from the link in your text. Change your mind and your details are deleted within a week.</li>
<li>We keep details only as long as your next step needs them, then delete them. Reports only ever show totals.</li>
<li>We don't sell information or use it for advertising.</li>
</ul>
<p>Questions, or want to see what we hold? <b>privacy@alwaysfoundation.org</b></p>
"""),
  ("young-people", "Children and young people", """
<p class="lead">Young people are welcome, and kept safe. The rules below are built into Always Platform and can't be switched off.</p>
<table class="doc-table age-table"><thead><tr><th scope="col"><span class="sr-only">Rule</span></th><th scope="col">Under 13</th><th scope="col">13 and 14</th><th scope="col">15 to 17</th></tr></thead><tbody><tr><th scope="row">Who says yes to sharing</th><td data-label="Under 13">A parent or guardian</td><td data-label="13 and 14">A parent or guardian</td><td data-label="15 to 17">The young person</td></tr><tr><th scope="row">The young person's own agreement</th><td data-label="Under 13">Asked, in plain words</td><td data-label="13 and 14">Asked</td><td data-label="15 to 17">They decide</td></tr><tr><th scope="row">Their own details</th><td data-label="Under 13">None. A parent responds</td><td data-label="13 and 14">First name and contact only</td><td data-label="15 to 17">First name and contact only</td></tr><tr><th scope="row">Who they meet</th><td colspan="3" data-label="Everyone under 18">Only verified youth partners</td></tr></tbody></table>
<h2>What every young person can count on</h2>
<ul>
<li>Only youth leaders with a current Working With Children Check can see a young person's details, and only at the church that welcomes them.</li>
<li>No AI ever touches a young person's information.</li>
<li>No bulk lists or exports, and no sharing between ministries.</li>
<li>No profiles, feeds or messaging. Always Platform isn't social media.</li>
<li>Permission lasts 12 months, then we ask again. Details are deleted on a short schedule.</li>
<li>If we're unsure of someone's age, the younger rules apply.</li>
</ul>
<h2>Youth partners</h2>
<p>To welcome young people, a church or ministry needs a child safe policy, a named child safety contact, and current Working With Children Checks for its youth leaders. Leaders meet young people in line with their own child safe policy, and mandatory reporting duties always come first.</p>
<p>We follow the National Principles for Child Safe Organisations and are designing to Australia's Children's Online Privacy Code. Questions: <b>safeguarding@alwaysfoundation.org</b></p>
"""),
  ("always-agent", "Always Agent", """
<p class="lead">The Always Agent helps people do the admin around a welcome, so they have more time for the welcome itself.</p>
<p>It works alongside the foundation team, churches and ministries, and a person always decides what happens next. It never contacts someone who responded to Jesus on its own.</p>
<h2>What it does</h2>
<ul>
<li><b>Checks new responses</b> for missing details and anything a trained person should see first, before an introduction is offered.</li>
<li><b>Helps the foundation team</b> work through church claims and suggested events, gathering what's needed to confirm them.</li>
<li><b>Reminds teams</b> of anyone waiting to hear back, and drafts a friendly first text for a person to edit and send.</li>
<li><b>Answers questions</b> from churches, ministries and builders, using these docs.</li>
</ul>
<h2>Guardrails</h2>
<ul>
<li>A person approves every action that affects someone who responded.</li>
<li>It sees only what its task needs, and every action is logged.</li>
<li>Young people's information is kept out of it entirely.</li>
<li>No one's information is used to train AI.</li>
</ul>
<p>The Always Agent grew from our earlier work on agents with a human in the loop. Read the field notes in <a href="#/research">Research</a>. It is in pilot with the foundation team.</p>
"""),
  ("ai", "AI", """
<p class="lead">People welcome people. Technology helps them do it well.</p>
<p>Every welcome comes from a real person. Where we use AI, it's to save volunteers time, like turning a voice note into text on their own phone, and the person stays in charge of what happens next. The <a href="#/docs/always-agent">Always Agent</a> helps teams with admin, with a person deciding every step. We don't use anyone's information to train AI, and young people's information is kept out of it entirely.</p>
"""),
  ("policies", "Our policies", """
<p>Always Platform is governed by six published policies, each with numbered rules:</p>
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
<li><b>Builders on equal terms.</b> Anyone building on Always Platform, including commercial builders, does so on the same terms as everyone else, with no special rights.</li>
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
 ]),
]

def esc(s): return html.escape(s, quote=True)

DOCS.insert(1, CP.DOCS)
import docs_update as DU
import faithtech as FT
PR.NEW_PAGES['faithtech'] = FT.PAGE
PR.TITLES['faithtech'] = 'FaithTech Australia · Always Foundation'
import motion as MO
DU.apply(DOCS)
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
.dt-wrap { overflow-x: auto; margin: 20px 0; }
.dt { width: 100%; border-collapse: collapse; font-size: 15px; margin: 18px 0; }
.dt th, .dt td { text-align: left; vertical-align: top; padding: 12px 14px; border-bottom: 1px solid rgba(27,71,64,.12); }
.dt th { font: 700 13.5px/1.3 var(--head); color: var(--green); background: rgba(27,71,64,.05); }
.dt .dt-sub { color: var(--muted); font-size: 14px; }
.dt a { color: var(--green); }

.brand svg.wm { width: auto; height: 34px; }
footer .brand svg.wm { height: 28px; }
@media (max-width: 480px) { header .brand svg.wm { height: 26px; } header .brand { font-size: 21px; } }
/* Multi-page */
.page[hidden] { display: none; }
.page-hero { background: var(--green); color: var(--cream); padding: 176px 0 104px; }
@media (max-width: 860px) { .page-hero { padding: 128px 0 64px; } }
.page-hero h1 { font-size: clamp(44px, 6vw, 84px); letter-spacing: -0.045em; }
.page-hero p { margin-top: 22px; max-width: 700px; font-size: 22px; line-height: 1.5; color: var(--on-green); }
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
.prose .dt code { overflow-wrap: anywhere; word-break: break-word; }
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
@media (max-width: 640px) { .pager { flex-direction: column; } .pager a { min-width: 0; } .pager a.next { margin-left: 0; } }
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
<section class="page-hero"><div class="wrap"><h1>About the Always Foundation</h1><p>Together for the Gospel. We bring churches and Christian ministries together, providing the tools, resources and connections they need to serve Christ and their communities.</p></div></section>
<section class="sec" style="padding-top:96px"><div class="wrap">
  <div class="about-grid">
    <div><h2>Why we exist</h2>
      <p>Always Foundation is a new initiative. We are being established now, and we are testing our first tools with churches and ministries.</p>
      <p>Across Australia, churches and ministries are sharing the Gospel, making disciples and serving their communities. Jesus sent His Church to “go therefore and make disciples of all nations” (Matthew 28:19, ESV), and no single church or ministry carries that alone.</p>
      <p>Yet many ministries each build and pay for the same tools, carry heavy administration, and struggle to pass people on to one another safely. Too many people respond to Jesus and never find a church family. We exist to support their work, so ministries can devote more of their time and resources to what matters most.</p></div>
    <div><h2>How we help</h2>
      <p><b>Equip.</b> Free, open-source technology and practical tools for churches and Christian organisations, including the Always App for every Christian who shares the Gospel.</p>
      <p><b>Support.</b> Shared tools for governance, compliance, safeguarding and reporting that make everyday operations simpler.</p>
      <p><b>Connect.</b> Common standards and a connected network that help ministries work together, share resources and connect people with local churches.</p>
      <p>All of it runs on Always Platform, our open-source technology. Our focus is Australia, and the Church in other nations is free to use it too.</p></div>
  </div>
  <div class="mv">
    <div><h3>Our vision</h3><p>One faith. Many ministries. A shared mission: the Gospel going further across Australia, and more people worshipping Jesus.</p><p style="margin-top:12px">Our values: Christ-centred. Gospel first. Built together, shared freely. People's details stay theirs.</p></div>
    <div><h3>Our name</h3><p>From Jesus' promise in the Great Commission: “I am with you always” (Matthew 28:20, ESV).</p></div>
    <div><h3>Our posture</h3><p>A ministry that serves ministries. Like those appointed in Acts 6 to carry the practical work, we serve quietly in the background, so churches and ministries can give themselves to the Gospel. We are not on the frontline. We stand behind it.</p></div>
  </div>
  <div class="creed">
    <div><h2>Built together. Shared freely.</h2></div>
    <div><p>Always Foundation is an independent, member-based Christian nonprofit. Our members help shape what we build, contribute to common standards and share in the benefits. Churches use it free, and larger ministries contribute according to their size.</p>
    <p style="margin-top:16px">Members affirm the Nicene Creed (AD 381), so churches across denominations can serve together on the historic faith. The foundation is being established as an Australian not-for-profit company limited by guarantee, to register as a charity with the ACNC.</p></div>
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
<section class="page-hero" style="padding-bottom:56px"><div class="wrap"><h1>Docs</h1><p>How Always Platform and its five modules work, for churches, ministries, people and developers.</p>
  <nav class="dq" aria-label="Start here">
    <a href="#/docs/joining"><b>Joining</b><span>Register and get verified</span></a>
    <a href="#/docs/inbox"><b>Churches</b><span>Welcome people from your phone</span></a>
    <a href="#/docs/senders"><b>Ministries</b><span>Response pages and reports</span></a>
    <a href="#/docs/api"><b>Developers</b><span>API, SDK, MCP, webhooks</span></a>
    <a href="#/docs/privacy"><b>Privacy</b><span>Your story is yours</span></a>
  </nav></div></section>
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

DECK_CSS = '''
/* ---- Aligned with the interactive deck ---- */
.case { background: var(--cream); }
.case .sec-title { max-width: 18ch; }
.case-photo { margin: 56px 0 0; border-radius: 26px; overflow: hidden; aspect-ratio: 16 / 9; background: var(--night); }
.case-photo img { width: 100%; height: 100%; object-fit: cover; display: block; }
.case-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 56px; margin-top: 56px; }
.case-grid h3 { font-size: 27px; color: var(--green); }
.case-grid p { margin-top: 14px; color: var(--soft); font-size: 18px; }
.case-quote { margin: 64px 0 0; max-width: 30ch; font: 400 clamp(26px, 3vw, 38px)/1.3 'Newsreader', Georgia, serif; color: var(--green); }
.case-fine { margin-top: 28px; font-size: 13px; color: var(--muted); }
@media (max-width: 860px) { .case-grid { grid-template-columns: 1fr; gap: 36px; } .case-photo { aspect-ratio: 4 / 3; } }

/* Docs: calm and compact */
#page-docs .page-hero { padding: 150px 0 56px; }
#page-docs .page-hero h1 { font-size: clamp(40px, 4.4vw, 60px); }
#page-docs .page-hero p { font-size: 19px; }
.prose h1 { font-size: clamp(34px, 3.6vw, 48px); letter-spacing: -0.035em; }
.prose h2 { font-size: 25px; letter-spacing: -0.02em; margin-top: 44px; }
.prose .lead { font-size: 20px; color: var(--muted); }
.prose p, .prose li { font-size: 17px; }
.doc-meta { margin-top: 56px; padding-top: 20px; border-top: 1px solid var(--line); display: flex; justify-content: space-between; gap: 16px; flex-wrap: wrap; font-size: 14px; color: var(--muted); }
.doc-meta a { color: var(--clay); }
.doc-table { width: 100%; border-collapse: collapse; margin: 16px 0 8px; font-size: 16px; }
.doc-table th, .doc-table td { text-align: left; padding: 12px 0; border-bottom: 1px solid var(--line); }
.doc-table thead th { font-weight: 700; color: var(--green); }
.doc-table thead th:last-child { text-align: right; }
.doc-table td { text-align: right; font-variant-numeric: tabular-nums; font-weight: 700; }
.doc-table tbody th { font-weight: 400; }
.age-table td { text-align: left; font-weight: 400; padding-right: 12px; } .age-table th[scope=row] { padding-right: 16px; } .age-table thead th:last-child { text-align: left; }
.sr-only { position: absolute; width: 1px; height: 1px; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }
@media (max-width: 640px) { .age-table thead { display: none; } .age-table, .age-table tbody, .age-table tr, .age-table th, .age-table td { display: block; width: 100%; } .age-table tr { border-bottom: 1px solid var(--line); padding: 12px 0; } .age-table th[scope=row] { border: 0; padding: 0 0 6px; font-weight: 700; color: var(--green); } .age-table td { border: 0; padding: 3px 0; display: flex; gap: 12px; } .age-table td::before { content: attr(data-label); flex: 0 0 120px; color: var(--muted); font-size: 14px; } }
@media (max-width: 860px) { #page-docs .page-hero { padding: 120px 0 40px; } }
.rv { transform: none; transition: opacity .6s ease; }
.word .verse { font-family: 'Newsreader', Georgia, serif; font-weight: 400; letter-spacing: -0.01em; line-height: 1.2; color: var(--green); }
.word .verse::before { content: '\\201C'; display: inline; font-size: inherit; line-height: inherit; margin: 0; color: inherit; }
.word .verse::after { content: '\\201D'; }
.word .cite { font: 700 17px var(--head); color: var(--clay); }
.btn { border-radius: 16px; }
.sec-title, .page-hero h1 { letter-spacing: -0.035em; }
.tag, .lm-k { display: block; font: 700 17px/1.2 var(--head); color: var(--clay); margin-bottom: 18px; }
.sec-lede { color: var(--muted); }
.churches { background: var(--sage); color: var(--ink); }
.churches .sec-title { color: var(--green); }
.churches .sec-lede { color: var(--muted); }
.gift { background: var(--paper); }
.gift h3 { color: var(--ink); }
.gift p { color: var(--muted); }
.story { background: var(--cream); }
.app-band { background: var(--peach); color: var(--night); padding: 0; overflow: hidden; }
.app-band-grid { display: grid; grid-template-columns: minmax(0, 1fr) 380px; gap: 80px; align-items: stretch; }
.app-band-grid > div:first-child { padding: 140px 0; }
.app-band .tag { color: var(--night); }
.app-band .sec-title { color: var(--night); max-width: 14ch; }
.app-band .sec-lede { color: #3B2A1F; }
.app-band .ctas { margin-top: 36px; }
.app-band-mark { background: transparent; display: flex; align-items: center; justify-content: center; }
.app-band-mark svg { width: 96px; }

/* home platform section: green band, deck style */
.plat { background: var(--green); color: var(--on-green, #F8F3EA); }
.plat .tag { color: var(--peach); }
.plat .sec-title { color: #F8F3EA; }
.plat .sec-lede { color: #CFE0D6; }
.plat-ways { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 18px; margin: 56px 0 44px; }
.plat-way { background: #14352F; border-radius: 26px; padding: 18px 18px 26px; display: grid; gap: 10px; align-content: start; }
.plat-way h3 { margin: 10px 6px 0; font: 800 24px/1.15 var(--head); color: #F8F3EA; letter-spacing: -0.02em; }
.plat-way p { margin: 0 6px; color: #CFE0D6; font-size: 16px; line-height: 1.5; }
.pw-art { height: 168px; border-radius: 18px; background: #1B4740; display: grid; place-items: center; overflow: hidden; }
.pw-phone .pw-screen { width: 132px; height: 190px; margin-top: 46px; background: #F8F3EA; border-radius: 22px 22px 0 0; box-shadow: 0 0 0 6px #0F2924; padding: 14px 12px; display: grid; gap: 6px; align-content: start; color: #1E2A26; font-size: 10px; }
.pw-brand { font-weight: 700; color: #7A4BD8; font-size: 9px; }
.pw-screen b { font: 800 13px/1.15 var(--head); }
.pw-opt { background: #fff; border-radius: 8px; padding: 6px 7px; box-shadow: inset 0 0 0 1px #E9DFCF; }
.pw-go { background: #7A4BD8; color: #fff; border-radius: 8px; padding: 6px; text-align: center; font-weight: 700; }
.pw-code { place-items: start; align-content: center; padding: 0 20px; font: 13.5px/1.75 ui-monospace, SFMono-Regular, Menlo, monospace; color: #E3ECE6; }
.pw-code .k { color: #E8A577; } .pw-code .d { color: #8FB5A5; }
.pw-chat { align-content: center; gap: 8px; padding: 0 16px; place-items: stretch; }
.pw-chat span { font-size: 13px; line-height: 1.4; padding: 9px 12px; border-radius: 14px; max-width: 88%; }
.pw-chat .me { justify-self: end; background: #E8A577; color: #1E2A26; border-bottom-right-radius: 4px; }
.pw-chat .ai { justify-self: start; background: #F8F3EA; color: #1E2A26; border-bottom-left-radius: 4px; }
.plat-does { list-style: none; margin: 0 0 40px; padding: 28px 0 0; border-top: 1px solid rgba(207,224,214,.18); display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 18px 24px; }
.plat-does li { color: #CFE0D6; font-size: 16px; line-height: 1.5; }
.plat-does b { display: block; font: 800 18px/1.3 var(--head); color: #F8F3EA; margin-bottom: 2px; }
.btn-line { border: 1.5px solid #1B4740; color: #1B4740; background: transparent; }
@media (max-width: 1080px) { .plat-ways, .plat-does { grid-template-columns: 1fr 1fr; } }
@media (max-width: 640px) { .plat-ways, .plat-does { grid-template-columns: 1fr; } }

/* Case studies */
.case-item { display: grid; grid-template-columns: 5fr 7fr; gap: 56px; align-items: start; margin-top: 64px; }
.case-item + .case-item { margin-top: 72px; padding-top: 72px; border-top: 1px solid rgba(27,71,64,.12); }
.case .case-photo { margin: 0; aspect-ratio: 4 / 3; border-radius: 20px; }
.case-title { font-size: clamp(26px, 2.6vw, 34px); line-height: 1.15; letter-spacing: -0.02em; color: var(--green); max-width: 22ch; }
.case-part { margin-top: 20px; }
.case-part h3 { font-size: 18px; color: var(--green); }
.case-part p { margin-top: 6px; color: var(--soft); font-size: 17px; max-width: 58ch; }
.case .case-quote { margin-top: 28px; font-size: clamp(20px, 1.8vw, 24px); max-width: 40ch; padding-left: 22px; }
.case .case-fine { margin-top: 18px; }
/* Case study slider */
#stories { padding-top: clamp(72px, 9vw, 112px); padding-bottom: clamp(72px, 9vw, 112px); }
.cs-head { display: flex; align-items: flex-end; justify-content: space-between; gap: 24px; }
.cs-head .sec-title { max-width: 18ch; }
.cs-arrows { display: flex; gap: 10px; flex: none; }
.cs-arrow { width: 48px; height: 48px; border-radius: 50%; border: 1.5px solid rgba(27,71,64,.25); background: transparent; color: var(--green); font-size: 20px; cursor: pointer; transition: background .2s, color .2s; }
.cs-arrow:hover, .cs-arrow:focus-visible { background: var(--green); color: var(--cream); }
.cs-arrow:disabled { opacity: .35; cursor: default; background: transparent; color: var(--green); }
.cs-track { list-style: none; margin: 40px 0 0; padding: 4px max(22px, calc((100vw - 1240px) / 2 + 40px)) 18px; display: grid; grid-auto-flow: column; grid-auto-columns: clamp(280px, 30vw, 380px); gap: 20px; overflow-x: auto; scroll-snap-type: x mandatory; scroll-padding-inline: max(22px, calc((100vw - 1240px) / 2 + 40px)); scrollbar-width: none; overscroll-behavior-x: contain; }
.cs-track::-webkit-scrollbar { display: none; }
.cs-tile { scroll-snap-align: start; background: #FFFDF8; border-radius: 22px; overflow: hidden; display: flex; flex-direction: column; box-shadow: 0 1px 0 rgba(27,71,64,.06); }
.cs-img { position: relative; aspect-ratio: 4 / 3; background: var(--night); }
.cs-img img { width: 100%; height: 100%; object-fit: cover; display: block; }
.cs-soon { position: absolute; left: 14px; top: 14px; padding: 6px 12px; border-radius: 999px; background: var(--cream); color: #9A4F22; font: 700 12.5px/1 var(--head); }
.cs-text { padding: 22px 22px 22px; display: flex; flex-direction: column; flex: 1; }
.cs-name { display: flex; align-items: center; gap: 8px; margin: 0; font: 700 13.5px/1.2 var(--head); color: var(--clay); }
.cs-logo { width: 28px; height: 28px; }
.cs-text h3 { margin: 10px 0 0; font-size: 21px; line-height: 1.2; letter-spacing: -0.01em; color: var(--green); }
.cs-text > p:not(.cs-name) { margin: 8px 0 0; color: var(--soft); font-size: 15.5px; line-height: 1.5; }
.cs-more { margin-top: auto; align-self: flex-start; padding: 16px 0 0; min-height: 44px; background: none; border: 0; color: var(--green); font: 700 15px/1 var(--head); cursor: pointer; text-decoration: underline; text-underline-offset: 4px; text-decoration-color: rgba(27,71,64,.35); }
.cs-more:hover, .cs-more:focus-visible { text-decoration-color: currentColor; }
.cs-dialog { border: 0; padding: 0; border-radius: 24px; width: min(720px, calc(100vw - 32px)); max-height: calc(100dvh - 48px); background: #FFFDF8; color: var(--night); box-shadow: 0 30px 80px rgba(0,0,0,.35); }
.cs-dialog::backdrop { background: rgba(20,53,47,.6); backdrop-filter: blur(2px); }
.cs-dlg-in { position: relative; padding: 28px clamp(22px, 4vw, 40px) 32px; }
.cs-close { position: absolute; right: 14px; top: 14px; width: 44px; height: 44px; border-radius: 50%; border: 0; background: rgba(27,71,64,.08); color: var(--green); font-size: 26px; line-height: 1; cursor: pointer; }
.cs-dialog h3 { margin: 10px 0 18px; font-size: clamp(24px, 3vw, 30px); line-height: 1.15; color: var(--green); padding-right: 48px; }
.cs-dialog h4 { margin: 22px 0 6px; font: 700 16px/1.3 var(--head); color: var(--green); }
.cs-dialog p { margin: 0; color: var(--soft); font-size: 16.5px; line-height: 1.6; }
.cs-dialog a { color: var(--clay); }
.cs-hero { width: 100%; aspect-ratio: 16 / 9; object-fit: cover; border-radius: 16px; display: block; }
.cs-two { margin-top: 10px; } .cs-two img { width: 48%; aspect-ratio: 4 / 3; object-fit: cover; border-radius: 12px; display: block; }
.cs-dialog blockquote { margin: 22px 0 0; padding-left: 18px; border-left: 3px solid var(--clay); }
.cs-dialog blockquote p { font-family: var(--serif, Georgia, serif); font-size: 19px; color: var(--night); }
.cs-dialog cite { display: block; margin-top: 10px; font: normal 700 14px/1.3 var(--head); color: var(--clay); }
.cs-fine { margin-top: 20px !important; font-size: 13px !important; color: var(--muted, #7a827e) !important; }
@media (max-width: 640px) { .cs-arrows { display: none; } .cs-track { grid-auto-columns: 82vw; gap: 14px; } }
.hero { padding-bottom: clamp(56px, 7vw, 96px); }
.hero-grid { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.15fr); gap: clamp(24px, 4vw, 56px); align-items: center; }
.hero-grid .hero-copy > * { max-width: 620px; }
.hero h1 { font-size: clamp(48px, 7vw, 104px); }
.hero .hero-split { display: grid; grid-template-columns: 1.15fr 1fr; gap: clamp(32px, 6vw, 96px); align-items: end; max-width: none; }
.hero .hero-split > * { max-width: none; }
.hero .hero-split h1 { margin: 0; }
.hero .hero-side .lede { margin-top: 0; max-width: 40ch; }
@media (max-width: 900px) { .hero .hero-split { grid-template-columns: 1fr; gap: 24px; } }
.hero h1 .nw { white-space: nowrap; }
.hero h1 .u { text-decoration: underline; text-decoration-color: var(--peach); text-decoration-thickness: .075em; text-underline-offset: .12em; text-decoration-skip-ink: none; }
.sv { margin: 18px 0 0; font-family: 'Newsreader', Georgia, serif; font-style: italic; font-size: 17px; line-height: 1.45; color: inherit; opacity: .78; }
.sv cite, .heart-fine cite { font: 700 12.5px/1 var(--head); font-style: normal; letter-spacing: .01em; color: var(--clay, #B5603A); margin-left: .35em; white-space: nowrap; }
.sc { font-variant: small-caps; }
.heart-item .sv { margin-top: 16px; padding-top: 14px; border-top: 1px solid rgba(27,71,64,.1); font-size: 16px; }
.cs-head .sv { margin-top: 14px; font-size: 19px; }
.app-band .sv { font-size: 19px; margin: 22px 0 0; opacity: .85; }
.app-band .sv cite { color: var(--night); }
.plat .sv, .join .sv { font-size: 19px; }
.join .wrap > * { min-width: 0; }
/* ---- Together for the Gospel ---- */
.hero-line { margin: 22px 0 0; font: 700 17px/1.4 var(--head); color: var(--peach); }
.word .wrap { align-items: start; }
.word .sec-title { font-size: clamp(30px, 3.4vw, 46px); line-height: 1.12; max-width: 20ch; margin-top: 14px; }
.word .side p b { color: var(--green); font-weight: 700; }
.heart-item .hk { margin-top: 6px; color: var(--green); font: 700 17px/1.35 var(--head); }
.heart-item .hk + p { margin-top: 10px; }
.hl { list-style: none; margin: 18px 0 0; padding: 0; display: grid; gap: 4px; }
.hl a { display: inline-flex; align-items: center; min-height: 32px; color: var(--green); font: 600 15.5px/1.3 var(--head); text-decoration: underline; text-decoration-color: rgba(27,71,64,.25); text-underline-offset: 4px; }
.hl a:hover, .hl a:focus-visible { text-decoration-color: var(--peach); }
.shared { background: var(--sage); }
.shared-grid { display: grid; grid-template-columns: 1.1fr 1fr; gap: 80px; align-items: start; }
.shared .sec-lede { max-width: 34ch; }
.shared-p { margin-top: 18px; font-size: 17px; line-height: 1.6; color: var(--soft); max-width: 46ch; }
.shared-list { list-style: none; margin: 0; padding: 0; display: grid; gap: 14px; }
.shared-list li { padding: 24px 26px; border-radius: 20px; background: #FFFDF8; }
.shared-list h3 { margin: 0; font-size: 21px; color: var(--green); }
.shared-list p { margin: 6px 0 0; color: var(--soft); font-size: 16px; line-height: 1.55; }
.join-fine { margin-top: 16px; font-size: 15px; line-height: 1.55; color: var(--on-green); opacity: .85; max-width: 44ch; }
.join-fine a { color: var(--cream); text-decoration: underline; text-underline-offset: 3px; }
.join-ctas { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 28px; }
.join-ctas .btn { min-height: 48px; cursor: pointer; font: inherit; font-weight: 600; }
.join-ctas .btn-ghost { background: transparent; color: var(--cream); border: 1.5px solid rgba(248,243,234,.55); }
.join-ctas .btn-ghost:hover, .join-ctas .btn-ghost:focus-visible { background: var(--cream); color: var(--green); }

.pw-form, .pw-bars, .pw-list { align-items: stretch; text-align: left; place-items: stretch; display: flex; flex-direction: column; justify-content: center; gap: 7px; padding: 18px 20px; font: 600 12px/1.2 var(--head); color: var(--on-green); }
.pf-l { opacity: .75; }
.pf-i { height: 22px; border-radius: 7px; background: rgba(248,243,234,.12); border: 1px solid rgba(248,243,234,.18); }
.pf-c { display: flex; align-items: center; gap: 8px; margin-top: 4px; color: var(--cream); }
.pf-c i { width: 14px; height: 14px; border-radius: 4px; background: var(--peach); flex: none; }
.pb-t { opacity: .75; margin-bottom: 2px; }
.pw-form > *, .pw-bars > *, .pw-list > * { width: 100%; box-sizing: border-box; }
.pb { position: relative; height: 24px; border-radius: 7px; background: rgba(248,243,234,.08); overflow: hidden; }
.pb::before { content: ''; position: absolute; inset: 0 auto 0 0; width: var(--w); background: rgba(232,165,119,.85); border-radius: 7px; }
.pb em { position: relative; font-style: normal; padding-left: 9px; line-height: 24px; color: #1A1410; }
.pl { display: flex; justify-content: space-between; gap: 10px; padding: 8px 11px; border-radius: 9px; background: rgba(248,243,234,.1); }
.pl b { color: var(--cream); font-weight: 700; } .pl em { font-style: normal; opacity: .7; }
.pw-agent { display: flex; flex-direction: column; justify-content: center; gap: 8px; padding: 18px 20px; text-align: left; font: 600 12px/1.35 var(--head); color: var(--on-green); }
.pa-t { opacity: .75; }
.pa-m { padding: 10px 12px; border-radius: 10px 10px 10px 3px; background: rgba(248,243,234,.12); color: var(--cream); font-weight: 500; }
.pa-b { display: flex; gap: 6px; }
.pa-b i { font-style: normal; padding: 5px 10px; border-radius: 999px; border: 1px solid rgba(248,243,234,.3); }
.pa-b i:first-child { background: var(--peach); border-color: var(--peach); color: #1A1410; }
.plat-dev { margin-top: 22px; font-size: 15.5px; color: var(--on-green); opacity: .85; }
.plat-dev a { color: var(--cream); text-decoration: underline; text-underline-offset: 3px; }
@media (max-width: 860px) { .shared-grid { grid-template-columns: 1fr; gap: 40px; } }

.join .mail { overflow-wrap: anywhere; }
.plat .sv cite, .join .sv cite { color: var(--peach); }
.hero-cite { margin: 26px 0 0; font: 700 15px/1 var(--head); color: var(--peach); }
.hero .hero-cite + .lede { margin-top: 26px; }
.hero-map { position: relative; }
.hero-stat { margin: 4px 0 0; font-size: 14.5px; color: #A9C2B8; text-align: right; }
.hero-stat b { color: var(--peach); font: 800 18px/1 var(--head); }
.hero-stat span { display: block; font-size: 12px; color: #7F9A90; margin-top: 4px; }
@media (max-width: 900px) { .hero-grid { grid-template-columns: 1fr; } .hero-stat { text-align: left; } }
.heart-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 20px; margin-top: 48px; }
.heart-item { padding: 30px 28px; border-radius: 22px; background: #FFFDF8; border-top: 4px solid var(--peach); }
.heart-item h3 { margin: 0; font-size: 23px; color: var(--green); }
.heart-item p { margin: 10px 0 0; color: var(--soft); font-size: 16.5px; line-height: 1.55; }
.heart-fine { margin-top: 28px; color: var(--soft); font-size: 16px; font-style: italic; }
@media (max-width: 860px) { .heart-grid { grid-template-columns: 1fr; } }
.case-media { position: relative; padding-bottom: 22%; }
.case .case-media .case-photo:first-child { width: 88%; }
.case .case-inset { position: absolute; right: 0; bottom: 0; width: 52%; border: 6px solid var(--cream); box-shadow: 0 18px 40px rgba(20,53,47,.18); border-radius: 18px; }
.case-soon { display: inline-block; margin: 0 0 14px; padding: 6px 12px; border-radius: 999px; background: rgba(232,165,119,.2); color: #9A4F22; font: 700 13px/1 var(--head); }
@media (max-width: 860px) { .case-media { padding-bottom: 18%; } .case .case-media .case-photo:first-child { width: 90%; } .case .case-inset { width: 48%; border-width: 4px; } }
.case-logo { display: block; width: 52px; height: 52px; margin: 0 0 14px; }
.case-quote cite { display: block; margin-top: 12px; font: normal 700 14px/1.3 var(--head); color: var(--clay); }
/* calmer home on small screens */
.plat .ctas { margin-top: 48px; }
.ctas { display: flex; flex-wrap: wrap; gap: 12px; }
.pl-hero > *, .pl-hero .wrap > * { min-width: 0; }
@media (max-width: 640px) {
  .step { padding: 28px 24px 30px; }
  .plat-ways { grid-template-columns: 1fr 1fr !important; gap: 12px; }
  .plat-way .pw-art { display: none; }
  .plat-way { padding: 20px 18px; }
  .plat-way h3 { font-size: 19px; }
  .plat-way p { font-size: 14.5px; }
  .app-band-mark { height: auto !important; padding: 36px 22px 44px !important; }
}
@media (max-width: 860px) { .case-item { grid-template-columns: 1fr; gap: 24px; margin-top: 40px; } .case-item + .case-item { margin-top: 48px; padding-top: 48px; } }
/* footer */
footer { background: var(--night); color: #B8CCC1; padding: 88px 0 40px; font-size: 15px; }
footer { padding-bottom: 0; overflow: hidden; }
footer .wrap { display: grid; grid-template-columns: minmax(240px, 1fr) 2.2fr; gap: 28px 64px; align-items: start; }
.foot-brand { display: grid; gap: 18px; align-content: start; }
.foot-mail { color: #E8A577 !important; font-weight: 600; text-decoration: none; }
.foot-mail:hover { text-decoration: underline; }
footer .brand svg.wm { height: 34px; width: auto; }
.foot-line { margin: 0; max-width: 30ch; color: #CFE0D6; font-size: 17px; line-height: 1.55; }
.foot-cols { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 32px; }
.foot-cols h2 { font: 700 14px/1.2 var(--head); color: #E8A577; margin: 0 0 14px; letter-spacing: 0; }
.foot-cols a { display: block; color: #E3ECE6; text-decoration: none; padding: 7px 0; min-height: 0; overflow-wrap: anywhere; }
.foot-cols a:hover, .foot-cols a:focus-visible { color: #fff; text-decoration: underline; text-underline-offset: 3px; }
.foot-base a { color: #9FB3A9; }
.foot-base { grid-column: 1 / -1; display: flex; flex-wrap: wrap; justify-content: space-between; gap: 12px; margin-top: 48px; padding-top: 24px; border-top: 1px solid rgba(207,224,214,.14); font-size: 14px; color: #9FB3A9; }
footer .photo-credit { grid-column: 1 / -1; padding: 0 !important; max-width: none; margin: 40px 0 0; font-size: 12.5px; color: #7F958B; }
.foot-base { margin-top: 14px !important; }
.foot-mark { margin-top: 40px; padding: 0 max(22px, calc((100vw - 1240px) / 2 + 40px)); line-height: 0; }
.foot-mark-svg { width: 100%; height: auto; display: block; margin-bottom: -3.2%; opacity: .95; }
.foot-mark-svg path:first-child { fill: #F8F3EA; opacity: .1; }
.foot-mark-svg path:last-child { fill: #EE8B54; opacity: .9; }
@media (max-width: 900px) {
  footer { padding: 64px 0 32px; }
  footer .wrap { grid-template-columns: 1fr; }
  .foot-cols { grid-template-columns: 1fr 1fr; gap: 28px 24px; margin-top: 12px; }
}

/* polish: steps, app phone, case quote */
.step { min-height: 0; padding: 36px 34px 40px; gap: 14px; }
.step .art { margin: 0 0 10px; height: 56px; width: auto; align-self: flex-start; }
.step .tag { margin: 0; }
.app-band-mark { padding: 56px 24px; }
.app-phone { width: min(300px, 100%); background: var(--cream); border-radius: 36px; padding: 26px 18px 30px; box-shadow: 0 0 0 10px #12302B, 0 30px 60px rgba(0,0,0,.25); display: grid; gap: 10px; }
.ap-day { font: 700 13px/1 var(--head); color: var(--muted); margin: 0 4px 4px; }
.ap-card { display: flex; gap: 12px; align-items: flex-start; background: var(--paper); border-radius: 16px; padding: 14px; text-align: left; }
.ap-card b { display: block; font: 700 15px/1.25 var(--head); color: var(--green); }
.ap-card em { display: block; font-style: normal; font-size: 13px; color: var(--muted); margin-top: 3px; }
.ap-card.soft { background: #E9EFEA; }
.ap-dot { flex: 0 0 10px; height: 10px; border-radius: 50%; background: var(--green); margin-top: 4px; }
.ap-dot.pe { background: var(--peach); }
.case-quote { max-width: 34ch; padding-left: 28px; border-left: 3px solid var(--peach); }
.case-quote p { margin: 0; }
@media (max-width: 900px) { .app-band-mark { height: auto; padding: 40px 22px; } }

@media (max-width: 860px) {
  .app-band-grid { grid-template-columns: 1fr; gap: 0; }
  .app-band-grid > div:first-child { padding: 96px 0 56px; }
  .app-band-mark { margin: 0; height: auto; padding: 0 0 72px !important; }
}
'''

header = """
<header>
  <div class="wrap bar">
    <a class="brand" href="#/">
      <svg class="wm" viewBox="186 250 1328 366" role="img" aria-label="Always Foundation"><path fill="#F8F3EA" fill-rule="evenodd" d="M1030.8,608.4C1046.2,605.2 1061.0,596.1 1069.8,584.4C1077.9,573.6 1081.9,564.7 1101.5,514.5C1111.9,488.1 1128.3,446.2 1138.0,421.5C1147.8,396.8 1157.6,371.4 1160.0,365.2C1166.0,349.0 1167.7,350.0 1134.5,350.0C1109.8,350.0 1108.2,350.1 1106.6,351.9C1105.6,353.0 1101.7,362.3 1097.9,372.7C1094.1,383.0 1084.8,408.5 1077.3,429.2C1069.7,450.0 1063.2,467.0 1062.9,467.0C1062.5,467.0 1059.3,459.7 1055.7,450.8C1050.1,437.0 1029.3,386.6 1018.0,359.7C1016.3,355.5 1014.0,351.5 1013.0,351.0C1010.4,349.6 958.5,349.7 955.9,351.0C954.9,351.6 954.0,352.9 954.0,353.8C954.0,354.8 957.1,362.3 960.8,370.5C964.6,378.8 970.4,391.6 973.7,399.0C977.1,406.4 984.1,421.9 989.3,433.5C994.5,445.1 1006.2,470.9 1015.3,491.0C1024.3,511.1 1032.8,529.9 1034.0,532.8L1036.3,538.1L1033.5,544.6C1030.1,552.5 1024.9,557.3 1017.8,559.0C1011.6,560.5 1006.1,559.8 997.5,556.4C992.7,554.5 990.3,554.0 989.2,554.7C987.3,555.8 972.0,589.2 971.3,593.7C970.8,596.5 971.2,597.1 974.1,598.9C979.3,602.1 993.4,606.9 1001.9,608.4C1012.2,610.3 1021.6,610.3 1030.8,608.4ZM290.8,550.7C302.4,547.4 313.4,541.1 323.4,531.9L329.0,526.8L329.0,535.7C329.0,549.8 327.2,549.0 357.1,549.0C380.7,549.0 382.1,548.9 384.0,547.0C386.0,545.0 386.0,543.7 386.0,483.1C386.0,444.5 385.6,418.2 384.9,413.3C383.4,401.9 378.4,387.9 373.0,379.6C358.9,358.1 334.9,346.8 299.9,345.3C277.1,344.3 257.2,348.0 239.4,356.4C226.2,362.7 215.0,370.6 215.0,373.6C215.0,375.3 233.4,404.2 235.2,405.3C236.3,406.0 239.8,404.8 248.1,400.7C261.5,394.2 269.0,392.1 282.1,391.3C303.0,390.0 319.1,396.4 325.2,408.4C327.2,412.2 329.2,428.0 327.7,428.0C327.4,428.0 322.5,426.5 316.8,424.6C295.5,417.5 273.2,416.4 252.2,421.5C224.5,428.2 206.5,443.5 198.5,467.1C196.0,474.4 195.6,477.0 195.6,487.5C195.5,497.4 195.9,500.8 197.9,507.0C204.9,529.9 224.5,546.4 251.1,552.0C257.5,553.3 284.5,552.4 290.8,550.7ZM861.0,550.9C872.2,548.3 882.3,543.1 892.6,534.8C897.2,531.0 901.1,528.0 901.2,528.0C901.4,528.0 901.5,532.1 901.5,537.1C901.5,544.9 901.8,546.4 903.4,547.6C905.0,548.7 910.3,549.0 930.1,549.0C954.6,549.0 954.9,549.0 956.4,546.8C957.8,544.8 958.0,537.0 958.0,482.3C958.0,443.7 957.6,417.2 956.9,412.3C953.3,385.7 940.3,366.7 917.8,355.4C898.3,345.6 866.7,342.3 840.2,347.5C824.4,350.5 804.6,358.9 792.8,367.6C786.6,372.0 786.6,374.0 792.8,383.3C795.5,387.3 799.8,394.0 802.4,398.2C805.1,402.5 807.8,406.0 808.6,406.0C809.4,406.0 813.9,404.0 818.7,401.6C837.7,392.0 856.9,388.8 874.3,392.5C891.6,396.1 901.0,406.8 901.0,422.7C901.0,425.6 900.9,428.0 900.7,428.0C900.5,428.0 896.4,426.6 891.5,425.0C877.3,420.2 867.3,418.6 851.0,418.6C829.0,418.7 812.5,423.2 797.0,433.5C785.0,441.5 775.9,453.5 771.3,467.4C769.1,474.3 768.7,477.3 768.7,488.0C768.6,499.1 768.9,501.4 771.4,508.5C772.9,512.9 775.7,519.0 777.5,522.0C781.3,528.2 790.3,537.2 796.6,541.2C802.7,545.1 814.3,549.8 821.8,551.4C832.1,553.6 850.8,553.4 861.0,550.9ZM1262.7,550.6C1300.7,542.3 1323.0,511.4 1316.6,476.0C1314.6,464.6 1309.4,454.4 1302.1,447.1C1291.7,436.8 1278.0,430.6 1246.5,422.0C1221.5,415.1 1216.0,411.8 1216.0,403.5C1216.0,396.2 1221.1,392.0 1232.5,389.9C1243.3,387.9 1260.8,392.6 1275.7,401.7C1279.6,404.0 1283.8,406.0 1284.9,406.0C1286.2,406.0 1287.9,404.6 1289.4,402.2C1299.6,386.1 1307.0,373.7 1307.0,372.5C1307.0,369.2 1289.4,357.6 1276.7,352.6C1250.2,342.1 1217.5,342.8 1194.5,354.3C1173.0,365.0 1160.8,382.2 1159.4,403.8C1158.2,420.7 1162.9,434.0 1173.9,445.0C1184.4,455.4 1195.2,460.2 1237.6,473.0C1256.3,478.7 1263.4,486.5 1258.6,495.8C1254.9,503.0 1247.9,506.0 1235.0,506.0C1219.7,506.0 1204.7,500.8 1187.4,489.5C1182.2,486.1 1177.9,484.0 1176.6,484.2C1175.2,484.4 1171.1,489.3 1163.8,499.5C1149.3,519.8 1149.9,518.3 1154.1,522.6C1158.9,527.6 1172.1,536.3 1182.1,540.9C1192.1,545.6 1208.7,550.6 1218.5,551.9C1228.5,553.3 1254.1,552.5 1262.7,550.6ZM460.6,547.6C462.5,546.2 462.5,543.5 462.8,411.9C463.0,292.7 462.9,277.4 461.5,275.3L460.0,273.0L434.1,273.0C411.9,273.0 408.1,273.2 407.0,274.6C405.9,275.8 405.7,292.4 405.8,357.3C406.0,558.6 405.9,545.7 407.6,547.4C409.8,549.7 457.5,549.8 460.6,547.6ZM585.3,547.8C586.2,547.1 590.1,538.0 593.9,527.5C618.9,459.0 626.2,439.4 627.0,438.6C627.6,438.0 628.0,437.9 628.0,438.2C628.0,438.5 633.7,454.5 640.6,473.7C647.5,492.8 656.1,516.8 659.7,527.0C663.5,537.7 667.1,546.2 668.2,547.2C670.0,548.8 672.8,549.0 693.5,549.0C715.1,549.0 716.8,548.9 718.4,547.1C719.4,546.0 726.9,525.4 735.0,501.3C743.2,477.2 757.7,434.3 767.4,405.9C783.6,358.1 784.8,354.1 783.4,352.1C781.9,350.1 781.3,350.0 756.1,350.0C732.9,350.0 730.0,350.2 728.1,351.8C726.7,353.0 722.8,363.7 715.1,388.0C709.1,407.0 701.4,431.2 698.0,441.9C694.6,452.5 691.5,460.8 691.1,460.4C690.6,459.9 687.5,451.4 684.0,441.5C675.5,417.0 657.5,366.0 654.4,357.8C653.0,354.2 651.2,350.9 650.4,350.6C649.5,350.3 639.4,350.0 627.9,350.0C609.1,350.0 606.8,350.2 605.2,351.8C604.2,352.8 600.8,361.0 597.6,370.1C594.4,379.1 587.2,399.3 581.5,415.0C575.9,430.7 569.8,447.7 568.0,452.8C566.2,457.9 564.5,461.9 564.3,461.7C564.1,461.4 562.1,455.2 559.9,447.9C557.6,440.5 554.1,429.1 552.1,422.5C550.0,415.9 544.4,397.7 539.5,382.0C534.7,366.3 530.0,352.7 529.2,351.8C527.8,350.2 525.2,350.0 500.9,350.0C477.9,350.0 473.9,350.2 472.6,351.6C471.7,352.4 471.0,353.5 471.0,353.8C471.0,354.2 475.5,368.0 481.0,384.5C489.8,410.8 510.4,474.5 527.4,528.0C530.5,537.7 533.8,546.4 534.7,547.3C536.2,548.8 539.1,549.0 560.0,549.0C577.3,549.0 584.1,548.7 585.3,547.8ZM276.4,509.0C266.5,507.0 258.1,501.8 254.2,495.1C252.0,491.4 251.5,489.3 251.5,484.0C251.5,476.0 254.8,469.6 261.7,464.6C269.8,458.7 274.8,457.5 290.5,457.5C305.4,457.5 311.7,458.9 323.2,464.7L328.0,467.0L328.0,474.4C328.0,480.5 327.5,482.6 324.9,487.8C317.1,503.5 295.8,512.8 276.4,509.0ZM848.3,509.0C825.1,504.1 816.4,482.6 831.5,467.5C838.7,460.2 845.3,457.9 860.1,457.2C873.5,456.7 882.8,458.5 894.4,464.1L901.2,467.4L900.8,474.9C899.9,489.9 890.4,501.5 874.6,507.0C867.8,509.3 854.5,510.3 848.3,509.0Z"/><path fill="#EE8B54" d="M1434.5,553.6C1436.3,552.3 1436.4,549.1 1436.4,463.1L1436.5,374.0L1468.9,374.0C1497.7,374.0 1501.5,373.8 1503.2,372.3C1504.8,370.9 1505.0,368.9 1505.0,352.8C1505.0,342.3 1504.6,334.1 1504.0,332.9C1503.0,331.1 1501.5,331.0 1470.0,331.0L1437.0,331.0L1437.0,296.4C1437.0,274.5 1436.6,261.2 1436.0,259.9C1435.0,258.1 1433.7,258.0 1413.4,258.0L1392.0,258.0L1391.0,260.6C1390.4,262.0 1390.0,277.4 1390.0,297.1L1390.0,331.0L1357.7,331.0C1333.9,331.0 1325.1,331.3 1324.2,332.2C1323.3,333.1 1323.0,339.0 1323.0,352.7C1323.0,370.7 1323.1,372.0 1324.9,373.0C1326.2,373.6 1338.6,374.0 1358.4,374.0L1390.0,374.0L1390.0,462.5C1390.0,549.7 1390.0,551.0 1392.0,553.0C1393.9,554.9 1395.3,555.0 1413.3,555.0C1428.1,555.0 1433.1,554.7 1434.5,553.6Z"/></svg>
    </a>
    <nav aria-label="Main" id="main-nav"><ul>
      """ + PR.menu_html() + """
    </ul><div class="nav-foot"><div class="nav-more"><a href="#/faq">FAQs</a><a href="#/events">Events</a><a href="#/research">Research</a><a href="#/brand">Brand</a><a href="#/claim">Claim your church</a><a href="#/contact">Contact</a></div><a class="btn btn-peach nav-cta" href="#/join">Join Always</a></div></nav>
    <a class="btn btn-peach" href="#/join">Join Always</a>
    <button class="menu-btn" type="button" aria-expanded="false" aria-controls="main-nav" onclick="toggleMenu()"><span>Menu</span><i aria-hidden="true"></i></button>
  </div>
</header>
"""

# Home: rewrite in-page links to routes
home = home.replace('href="#join"', 'href="#/join"').replace('href="#stories"', 'href="#/stories"')
home = home.replace('<a class="btn btn-peach" href="#/join">Join as a church or ministry</a>', '<a class="btn btn-peach" href="#/join">Join as a church or ministry</a>')
home = home.replace('<p class="note">Evangelical and Pentecostal, in every state and territory, and growing every week. Every one can claim its page, and is verified before anyone is introduced to it.</p>',
 '<p class="note">Evangelical and Pentecostal, in every state and territory, and growing every week. Every one can claim its page, and is verified before anyone is introduced to it.</p><a class="btn btn-green" href="#/directory" style="margin-top:28px">Search the directory</a>')

script = """

const DOCS = __DOCS__;
const ORDER = __ORDER__;
document.body.classList.remove('no-js');

// Reveal on scroll
const io = 'IntersectionObserver' in window ? new IntersectionObserver((es) => es.forEach((e) => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: 0.12 }) : null;
function watch(root) { root.querySelectorAll('.rv:not(.in)').forEach((el, i) => { el.style.transitionDelay = (i % 4) * 80 + 'ms'; io ? io.observe(el) : el.classList.add('in'); }); }

// Router
const pages = { home: 'page-home', about: 'page-about', docs: 'page-docs', churches: 'page-churches', ministries: 'page-ministries', app: 'page-app', faq: 'page-faq', events: 'page-events', claim: 'page-claim', feedback: 'page-feedback', research: 'page-research', brand: 'page-brand', platform: 'page-platform', compliance: 'page-compliance', developers: 'page-developers', hello: 'page-hello', contact: 'page-contact', join: 'page-join'""" + ''.join(f", {k}: 'page-{k}'" for k in PR.NEW_PAGES) + """ };
const anchors = { how: 'heart', stories: 'stories' };
function route() {
  const h = location.hash.replace(/^#\\/?/, '');
  const [first, second] = h.split('/');
  const aliases = """ + json.dumps(PR.ALIASES) + """;
  if (aliases[first]) { location.replace('#/' + aliases[first]); return; }
  let page = 'home';
  if (pages[first] && first !== 'home') page = first;
  for (const [k, id] of Object.entries(pages)) document.getElementById(id).hidden = k !== page;
  document.querySelectorAll('nav a[data-route]').forEach((a) => a.toggleAttribute('aria-current', a.dataset.route === page) || a.setAttribute('aria-current', a.dataset.route === page ? 'page' : ''));
  document.querySelectorAll('nav a[data-route]').forEach((a) => { if (a.dataset.route === page) a.setAttribute('aria-current', 'page'); else a.removeAttribute('aria-current'); });
  if (page === 'docs') showDoc(second || 'introduction');
  if (page === 'feedback' && second === 'missing') { document.querySelector('#fb-form input[value=missing]').checked = true; fbKind(); }
  if (page === 'compliance' && ['check', 'problem', 'infrastructure'].includes(second)) { requestAnimationFrame(() => document.getElementById(second).scrollIntoView({ behavior: 'smooth' })); watch(document.getElementById(pages[page])); document.title = second === 'check' ? 'Free compliance check-up · Always Foundation' : 'Always Compliance · Always Foundation'; return; }
  if (page === 'home' && anchors[first]) { requestAnimationFrame(() => document.getElementById(anchors[first]).scrollIntoView({ behavior: 'smooth' })); }
  else window.scrollTo(0, 0);
  const titles = { home: 'Always Foundation · Together for the Gospel', compliance: 'Always Compliance · Always Foundation', directory: 'Directory · Always Foundation', about: 'About · Always Foundation', churches: 'For churches · Always Foundation', ministries: 'For events, tours and ministries · Always Foundation', app: 'Always App · Always Foundation', faq: 'FAQs · Always Foundation', events: 'Events · Always Foundation', claim: 'Claim your church · Always Foundation', feedback: 'Ideas and problems · Always Foundation', research: 'Research · Always Foundation', brand: 'Brand · Always Foundation', platform: 'Always Platform · Always Foundation', ...""" + json.dumps(PR.TITLES, ensure_ascii=False) + """ };
  document.body.classList.toggle('on-hello', page === 'hello');
  if (page !== 'docs') document.title = titles[page] || 'Always Foundation';
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
    (next ? `<a class="next" href="#/docs/${next}"><span>Next</span><b>${DOCS[next].title}</b></a>` : '') + `</nav>` +
    `<div class="doc-meta"><span>Updated November 2026 · CC BY 4.0</span><span><a href="#/feedback">Suggest a change</a> · <a href="https://github.com/alwaysfoundation/always-website">Edit on GitHub</a></span></div>`;
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

const esc = (s) => String(s || '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

const LIVE = /(^|\\.)alwaysfoundation\\.org$/.test(location.hostname);
function evf(){const s=document.getElementById('ev-s').value,k=document.getElementById('ev-k').value;let n=0;document.querySelectorAll('#ev-list .ev').forEach((e)=>{const on=(!s||e.dataset.s===s)&&(!k||e.dataset.k===k);e.hidden=!on;if(on)n++;});document.getElementById('ev-empty').hidden=n>0;}
['ev-s','ev-k'].forEach((id)=>document.getElementById(id).addEventListener('change',evf));

// ---------- claim a church
const API_BASE = LIVE ? '/api/forms' : ''; // Claims and feedback go to the foundation inbox until the Always API is live.
async function sendJSON(path, body) {
  if (!API_BASE) return true; // prototype: no API connected yet
  const r = await fetch(API_BASE + path, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body) });
  return r.ok;
}
document.getElementById('claim-form').addEventListener('submit', async (e) => {
  e.preventDefault(); const f = e.target, st = document.getElementById('cl-status');
  if (!f.checkValidity()) { st.textContent = 'Please add your church, your name, role and work email, and tick the box.'; return; }
  const d = Object.fromEntries(new FormData(f));
  st.textContent = 'Sending…';
  const ok = await sendJSON('/v1/orgs/new/claims', { email: d.email, role: d.role, evidence: [d.church, d.suburb, d.name, d.evidence].filter(Boolean).join(' · ') }).catch(() => false);
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

(() => {
  const track = document.querySelector('.cs-track');
  if (!track) return;
  const arrows = document.querySelectorAll('.cs-arrow');
  const step = () => (track.querySelector('.cs-tile')?.getBoundingClientRect().width || 300) + 20;
  arrows.forEach((a) => a.addEventListener('click', () => track.scrollBy({ left: step() * Number(a.dataset.dir), behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' })));
  const sync = () => { const max = track.scrollWidth - track.clientWidth - 4; arrows[0].disabled = track.scrollLeft <= 4; arrows[1].disabled = track.scrollLeft >= max; };
  track.addEventListener('scroll', sync, { passive: true }); addEventListener('resize', sync); sync();
  document.querySelectorAll('.cs-more').forEach((btn) => btn.addEventListener('click', () => {
    const d = document.getElementById('cs-' + btn.dataset.cs);
    if (!d || !d.showModal) return;
    d.querySelectorAll('img[data-from]').forEach((im) => { if (!im.src) { const src = document.querySelector('img[data-key="' + im.dataset.from + '"]'); if (src) im.src = src.src; } });
    d.showModal(); d.querySelector('.cs-close').focus();
  }));
  document.querySelectorAll('.cs-dialog').forEach((d) => {
    d.querySelector('.cs-close').addEventListener('click', () => d.close());
    d.addEventListener('click', (e) => { if (e.target === d) d.close(); });
  });
})();


document.querySelectorAll('[data-interest]').forEach((b) => b.addEventListener('click', () => {
  const f = document.getElementById('contact-form'); if (!f) return;
  window.alwaysSetInterest?.(b.dataset.interest);
  f.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'center' });
  const n = f.querySelector('input[name="name"]'); if (n) setTimeout(() => n.focus({ preventScroll: true }), 400);
}));
""" + CP.JS + extras.JS + PR.MENU_JS + CF.JS + JN.JS + PO.JS + MO.JS
script = script.replace('__DIR__', directory).replace('__DOCS__', json.dumps(pages_json, ensure_ascii=False)).replace('__ORDER__', json.dumps(order))

footer = """
<footer>
  <div class="wrap">
    <div class="foot-brand"><a class="brand" href="#/"><svg class="wm" viewBox="186 250 1328 366" role="img" aria-label="Always Foundation"><path fill="#F8F3EA" fill-rule="evenodd" d="M1030.8,608.4C1046.2,605.2 1061.0,596.1 1069.8,584.4C1077.9,573.6 1081.9,564.7 1101.5,514.5C1111.9,488.1 1128.3,446.2 1138.0,421.5C1147.8,396.8 1157.6,371.4 1160.0,365.2C1166.0,349.0 1167.7,350.0 1134.5,350.0C1109.8,350.0 1108.2,350.1 1106.6,351.9C1105.6,353.0 1101.7,362.3 1097.9,372.7C1094.1,383.0 1084.8,408.5 1077.3,429.2C1069.7,450.0 1063.2,467.0 1062.9,467.0C1062.5,467.0 1059.3,459.7 1055.7,450.8C1050.1,437.0 1029.3,386.6 1018.0,359.7C1016.3,355.5 1014.0,351.5 1013.0,351.0C1010.4,349.6 958.5,349.7 955.9,351.0C954.9,351.6 954.0,352.9 954.0,353.8C954.0,354.8 957.1,362.3 960.8,370.5C964.6,378.8 970.4,391.6 973.7,399.0C977.1,406.4 984.1,421.9 989.3,433.5C994.5,445.1 1006.2,470.9 1015.3,491.0C1024.3,511.1 1032.8,529.9 1034.0,532.8L1036.3,538.1L1033.5,544.6C1030.1,552.5 1024.9,557.3 1017.8,559.0C1011.6,560.5 1006.1,559.8 997.5,556.4C992.7,554.5 990.3,554.0 989.2,554.7C987.3,555.8 972.0,589.2 971.3,593.7C970.8,596.5 971.2,597.1 974.1,598.9C979.3,602.1 993.4,606.9 1001.9,608.4C1012.2,610.3 1021.6,610.3 1030.8,608.4ZM290.8,550.7C302.4,547.4 313.4,541.1 323.4,531.9L329.0,526.8L329.0,535.7C329.0,549.8 327.2,549.0 357.1,549.0C380.7,549.0 382.1,548.9 384.0,547.0C386.0,545.0 386.0,543.7 386.0,483.1C386.0,444.5 385.6,418.2 384.9,413.3C383.4,401.9 378.4,387.9 373.0,379.6C358.9,358.1 334.9,346.8 299.9,345.3C277.1,344.3 257.2,348.0 239.4,356.4C226.2,362.7 215.0,370.6 215.0,373.6C215.0,375.3 233.4,404.2 235.2,405.3C236.3,406.0 239.8,404.8 248.1,400.7C261.5,394.2 269.0,392.1 282.1,391.3C303.0,390.0 319.1,396.4 325.2,408.4C327.2,412.2 329.2,428.0 327.7,428.0C327.4,428.0 322.5,426.5 316.8,424.6C295.5,417.5 273.2,416.4 252.2,421.5C224.5,428.2 206.5,443.5 198.5,467.1C196.0,474.4 195.6,477.0 195.6,487.5C195.5,497.4 195.9,500.8 197.9,507.0C204.9,529.9 224.5,546.4 251.1,552.0C257.5,553.3 284.5,552.4 290.8,550.7ZM861.0,550.9C872.2,548.3 882.3,543.1 892.6,534.8C897.2,531.0 901.1,528.0 901.2,528.0C901.4,528.0 901.5,532.1 901.5,537.1C901.5,544.9 901.8,546.4 903.4,547.6C905.0,548.7 910.3,549.0 930.1,549.0C954.6,549.0 954.9,549.0 956.4,546.8C957.8,544.8 958.0,537.0 958.0,482.3C958.0,443.7 957.6,417.2 956.9,412.3C953.3,385.7 940.3,366.7 917.8,355.4C898.3,345.6 866.7,342.3 840.2,347.5C824.4,350.5 804.6,358.9 792.8,367.6C786.6,372.0 786.6,374.0 792.8,383.3C795.5,387.3 799.8,394.0 802.4,398.2C805.1,402.5 807.8,406.0 808.6,406.0C809.4,406.0 813.9,404.0 818.7,401.6C837.7,392.0 856.9,388.8 874.3,392.5C891.6,396.1 901.0,406.8 901.0,422.7C901.0,425.6 900.9,428.0 900.7,428.0C900.5,428.0 896.4,426.6 891.5,425.0C877.3,420.2 867.3,418.6 851.0,418.6C829.0,418.7 812.5,423.2 797.0,433.5C785.0,441.5 775.9,453.5 771.3,467.4C769.1,474.3 768.7,477.3 768.7,488.0C768.6,499.1 768.9,501.4 771.4,508.5C772.9,512.9 775.7,519.0 777.5,522.0C781.3,528.2 790.3,537.2 796.6,541.2C802.7,545.1 814.3,549.8 821.8,551.4C832.1,553.6 850.8,553.4 861.0,550.9ZM1262.7,550.6C1300.7,542.3 1323.0,511.4 1316.6,476.0C1314.6,464.6 1309.4,454.4 1302.1,447.1C1291.7,436.8 1278.0,430.6 1246.5,422.0C1221.5,415.1 1216.0,411.8 1216.0,403.5C1216.0,396.2 1221.1,392.0 1232.5,389.9C1243.3,387.9 1260.8,392.6 1275.7,401.7C1279.6,404.0 1283.8,406.0 1284.9,406.0C1286.2,406.0 1287.9,404.6 1289.4,402.2C1299.6,386.1 1307.0,373.7 1307.0,372.5C1307.0,369.2 1289.4,357.6 1276.7,352.6C1250.2,342.1 1217.5,342.8 1194.5,354.3C1173.0,365.0 1160.8,382.2 1159.4,403.8C1158.2,420.7 1162.9,434.0 1173.9,445.0C1184.4,455.4 1195.2,460.2 1237.6,473.0C1256.3,478.7 1263.4,486.5 1258.6,495.8C1254.9,503.0 1247.9,506.0 1235.0,506.0C1219.7,506.0 1204.7,500.8 1187.4,489.5C1182.2,486.1 1177.9,484.0 1176.6,484.2C1175.2,484.4 1171.1,489.3 1163.8,499.5C1149.3,519.8 1149.9,518.3 1154.1,522.6C1158.9,527.6 1172.1,536.3 1182.1,540.9C1192.1,545.6 1208.7,550.6 1218.5,551.9C1228.5,553.3 1254.1,552.5 1262.7,550.6ZM460.6,547.6C462.5,546.2 462.5,543.5 462.8,411.9C463.0,292.7 462.9,277.4 461.5,275.3L460.0,273.0L434.1,273.0C411.9,273.0 408.1,273.2 407.0,274.6C405.9,275.8 405.7,292.4 405.8,357.3C406.0,558.6 405.9,545.7 407.6,547.4C409.8,549.7 457.5,549.8 460.6,547.6ZM585.3,547.8C586.2,547.1 590.1,538.0 593.9,527.5C618.9,459.0 626.2,439.4 627.0,438.6C627.6,438.0 628.0,437.9 628.0,438.2C628.0,438.5 633.7,454.5 640.6,473.7C647.5,492.8 656.1,516.8 659.7,527.0C663.5,537.7 667.1,546.2 668.2,547.2C670.0,548.8 672.8,549.0 693.5,549.0C715.1,549.0 716.8,548.9 718.4,547.1C719.4,546.0 726.9,525.4 735.0,501.3C743.2,477.2 757.7,434.3 767.4,405.9C783.6,358.1 784.8,354.1 783.4,352.1C781.9,350.1 781.3,350.0 756.1,350.0C732.9,350.0 730.0,350.2 728.1,351.8C726.7,353.0 722.8,363.7 715.1,388.0C709.1,407.0 701.4,431.2 698.0,441.9C694.6,452.5 691.5,460.8 691.1,460.4C690.6,459.9 687.5,451.4 684.0,441.5C675.5,417.0 657.5,366.0 654.4,357.8C653.0,354.2 651.2,350.9 650.4,350.6C649.5,350.3 639.4,350.0 627.9,350.0C609.1,350.0 606.8,350.2 605.2,351.8C604.2,352.8 600.8,361.0 597.6,370.1C594.4,379.1 587.2,399.3 581.5,415.0C575.9,430.7 569.8,447.7 568.0,452.8C566.2,457.9 564.5,461.9 564.3,461.7C564.1,461.4 562.1,455.2 559.9,447.9C557.6,440.5 554.1,429.1 552.1,422.5C550.0,415.9 544.4,397.7 539.5,382.0C534.7,366.3 530.0,352.7 529.2,351.8C527.8,350.2 525.2,350.0 500.9,350.0C477.9,350.0 473.9,350.2 472.6,351.6C471.7,352.4 471.0,353.5 471.0,353.8C471.0,354.2 475.5,368.0 481.0,384.5C489.8,410.8 510.4,474.5 527.4,528.0C530.5,537.7 533.8,546.4 534.7,547.3C536.2,548.8 539.1,549.0 560.0,549.0C577.3,549.0 584.1,548.7 585.3,547.8ZM276.4,509.0C266.5,507.0 258.1,501.8 254.2,495.1C252.0,491.4 251.5,489.3 251.5,484.0C251.5,476.0 254.8,469.6 261.7,464.6C269.8,458.7 274.8,457.5 290.5,457.5C305.4,457.5 311.7,458.9 323.2,464.7L328.0,467.0L328.0,474.4C328.0,480.5 327.5,482.6 324.9,487.8C317.1,503.5 295.8,512.8 276.4,509.0ZM848.3,509.0C825.1,504.1 816.4,482.6 831.5,467.5C838.7,460.2 845.3,457.9 860.1,457.2C873.5,456.7 882.8,458.5 894.4,464.1L901.2,467.4L900.8,474.9C899.9,489.9 890.4,501.5 874.6,507.0C867.8,509.3 854.5,510.3 848.3,509.0Z"/><path fill="#EE8B54" d="M1434.5,553.6C1436.3,552.3 1436.4,549.1 1436.4,463.1L1436.5,374.0L1468.9,374.0C1497.7,374.0 1501.5,373.8 1503.2,372.3C1504.8,370.9 1505.0,368.9 1505.0,352.8C1505.0,342.3 1504.6,334.1 1504.0,332.9C1503.0,331.1 1501.5,331.0 1470.0,331.0L1437.0,331.0L1437.0,296.4C1437.0,274.5 1436.6,261.2 1436.0,259.9C1435.0,258.1 1433.7,258.0 1413.4,258.0L1392.0,258.0L1391.0,260.6C1390.4,262.0 1390.0,277.4 1390.0,297.1L1390.0,331.0L1357.7,331.0C1333.9,331.0 1325.1,331.3 1324.2,332.2C1323.3,333.1 1323.0,339.0 1323.0,352.7C1323.0,370.7 1323.1,372.0 1324.9,373.0C1326.2,373.6 1338.6,374.0 1358.4,374.0L1390.0,374.0L1390.0,462.5C1390.0,549.7 1390.0,551.0 1392.0,553.0C1393.9,554.9 1395.3,555.0 1413.3,555.0C1428.1,555.0 1433.1,554.7 1434.5,553.6Z"/></svg></a>
    <p class="foot-line">Together for the Gospel. Bringing churches and Christian ministries together across Australia.</p>
    <a class="foot-mail" href="mailto:hello@alwaysfoundation.org">hello@alwaysfoundation.org</a></div>
    <nav class="foot-cols" aria-label="Footer">
      """ + PR.footer_cols() + """
    </nav>
    <p class="photo-credit">{{CREDIT}}</p>
    <div class="foot-base"><span>© Always Foundation</span><a href="#/docs/privacy">Privacy</a><a href="#/docs/terms">Terms</a></div>
  </div>
  <div class="foot-mark"><svg class="foot-mark-svg" viewBox="186 250 1328 366" aria-hidden="true" focusable="false"><path fill="#F8F3EA" fill-rule="evenodd" d="M1030.8,608.4C1046.2,605.2 1061.0,596.1 1069.8,584.4C1077.9,573.6 1081.9,564.7 1101.5,514.5C1111.9,488.1 1128.3,446.2 1138.0,421.5C1147.8,396.8 1157.6,371.4 1160.0,365.2C1166.0,349.0 1167.7,350.0 1134.5,350.0C1109.8,350.0 1108.2,350.1 1106.6,351.9C1105.6,353.0 1101.7,362.3 1097.9,372.7C1094.1,383.0 1084.8,408.5 1077.3,429.2C1069.7,450.0 1063.2,467.0 1062.9,467.0C1062.5,467.0 1059.3,459.7 1055.7,450.8C1050.1,437.0 1029.3,386.6 1018.0,359.7C1016.3,355.5 1014.0,351.5 1013.0,351.0C1010.4,349.6 958.5,349.7 955.9,351.0C954.9,351.6 954.0,352.9 954.0,353.8C954.0,354.8 957.1,362.3 960.8,370.5C964.6,378.8 970.4,391.6 973.7,399.0C977.1,406.4 984.1,421.9 989.3,433.5C994.5,445.1 1006.2,470.9 1015.3,491.0C1024.3,511.1 1032.8,529.9 1034.0,532.8L1036.3,538.1L1033.5,544.6C1030.1,552.5 1024.9,557.3 1017.8,559.0C1011.6,560.5 1006.1,559.8 997.5,556.4C992.7,554.5 990.3,554.0 989.2,554.7C987.3,555.8 972.0,589.2 971.3,593.7C970.8,596.5 971.2,597.1 974.1,598.9C979.3,602.1 993.4,606.9 1001.9,608.4C1012.2,610.3 1021.6,610.3 1030.8,608.4ZM290.8,550.7C302.4,547.4 313.4,541.1 323.4,531.9L329.0,526.8L329.0,535.7C329.0,549.8 327.2,549.0 357.1,549.0C380.7,549.0 382.1,548.9 384.0,547.0C386.0,545.0 386.0,543.7 386.0,483.1C386.0,444.5 385.6,418.2 384.9,413.3C383.4,401.9 378.4,387.9 373.0,379.6C358.9,358.1 334.9,346.8 299.9,345.3C277.1,344.3 257.2,348.0 239.4,356.4C226.2,362.7 215.0,370.6 215.0,373.6C215.0,375.3 233.4,404.2 235.2,405.3C236.3,406.0 239.8,404.8 248.1,400.7C261.5,394.2 269.0,392.1 282.1,391.3C303.0,390.0 319.1,396.4 325.2,408.4C327.2,412.2 329.2,428.0 327.7,428.0C327.4,428.0 322.5,426.5 316.8,424.6C295.5,417.5 273.2,416.4 252.2,421.5C224.5,428.2 206.5,443.5 198.5,467.1C196.0,474.4 195.6,477.0 195.6,487.5C195.5,497.4 195.9,500.8 197.9,507.0C204.9,529.9 224.5,546.4 251.1,552.0C257.5,553.3 284.5,552.4 290.8,550.7ZM861.0,550.9C872.2,548.3 882.3,543.1 892.6,534.8C897.2,531.0 901.1,528.0 901.2,528.0C901.4,528.0 901.5,532.1 901.5,537.1C901.5,544.9 901.8,546.4 903.4,547.6C905.0,548.7 910.3,549.0 930.1,549.0C954.6,549.0 954.9,549.0 956.4,546.8C957.8,544.8 958.0,537.0 958.0,482.3C958.0,443.7 957.6,417.2 956.9,412.3C953.3,385.7 940.3,366.7 917.8,355.4C898.3,345.6 866.7,342.3 840.2,347.5C824.4,350.5 804.6,358.9 792.8,367.6C786.6,372.0 786.6,374.0 792.8,383.3C795.5,387.3 799.8,394.0 802.4,398.2C805.1,402.5 807.8,406.0 808.6,406.0C809.4,406.0 813.9,404.0 818.7,401.6C837.7,392.0 856.9,388.8 874.3,392.5C891.6,396.1 901.0,406.8 901.0,422.7C901.0,425.6 900.9,428.0 900.7,428.0C900.5,428.0 896.4,426.6 891.5,425.0C877.3,420.2 867.3,418.6 851.0,418.6C829.0,418.7 812.5,423.2 797.0,433.5C785.0,441.5 775.9,453.5 771.3,467.4C769.1,474.3 768.7,477.3 768.7,488.0C768.6,499.1 768.9,501.4 771.4,508.5C772.9,512.9 775.7,519.0 777.5,522.0C781.3,528.2 790.3,537.2 796.6,541.2C802.7,545.1 814.3,549.8 821.8,551.4C832.1,553.6 850.8,553.4 861.0,550.9ZM1262.7,550.6C1300.7,542.3 1323.0,511.4 1316.6,476.0C1314.6,464.6 1309.4,454.4 1302.1,447.1C1291.7,436.8 1278.0,430.6 1246.5,422.0C1221.5,415.1 1216.0,411.8 1216.0,403.5C1216.0,396.2 1221.1,392.0 1232.5,389.9C1243.3,387.9 1260.8,392.6 1275.7,401.7C1279.6,404.0 1283.8,406.0 1284.9,406.0C1286.2,406.0 1287.9,404.6 1289.4,402.2C1299.6,386.1 1307.0,373.7 1307.0,372.5C1307.0,369.2 1289.4,357.6 1276.7,352.6C1250.2,342.1 1217.5,342.8 1194.5,354.3C1173.0,365.0 1160.8,382.2 1159.4,403.8C1158.2,420.7 1162.9,434.0 1173.9,445.0C1184.4,455.4 1195.2,460.2 1237.6,473.0C1256.3,478.7 1263.4,486.5 1258.6,495.8C1254.9,503.0 1247.9,506.0 1235.0,506.0C1219.7,506.0 1204.7,500.8 1187.4,489.5C1182.2,486.1 1177.9,484.0 1176.6,484.2C1175.2,484.4 1171.1,489.3 1163.8,499.5C1149.3,519.8 1149.9,518.3 1154.1,522.6C1158.9,527.6 1172.1,536.3 1182.1,540.9C1192.1,545.6 1208.7,550.6 1218.5,551.9C1228.5,553.3 1254.1,552.5 1262.7,550.6ZM460.6,547.6C462.5,546.2 462.5,543.5 462.8,411.9C463.0,292.7 462.9,277.4 461.5,275.3L460.0,273.0L434.1,273.0C411.9,273.0 408.1,273.2 407.0,274.6C405.9,275.8 405.7,292.4 405.8,357.3C406.0,558.6 405.9,545.7 407.6,547.4C409.8,549.7 457.5,549.8 460.6,547.6ZM585.3,547.8C586.2,547.1 590.1,538.0 593.9,527.5C618.9,459.0 626.2,439.4 627.0,438.6C627.6,438.0 628.0,437.9 628.0,438.2C628.0,438.5 633.7,454.5 640.6,473.7C647.5,492.8 656.1,516.8 659.7,527.0C663.5,537.7 667.1,546.2 668.2,547.2C670.0,548.8 672.8,549.0 693.5,549.0C715.1,549.0 716.8,548.9 718.4,547.1C719.4,546.0 726.9,525.4 735.0,501.3C743.2,477.2 757.7,434.3 767.4,405.9C783.6,358.1 784.8,354.1 783.4,352.1C781.9,350.1 781.3,350.0 756.1,350.0C732.9,350.0 730.0,350.2 728.1,351.8C726.7,353.0 722.8,363.7 715.1,388.0C709.1,407.0 701.4,431.2 698.0,441.9C694.6,452.5 691.5,460.8 691.1,460.4C690.6,459.9 687.5,451.4 684.0,441.5C675.5,417.0 657.5,366.0 654.4,357.8C653.0,354.2 651.2,350.9 650.4,350.6C649.5,350.3 639.4,350.0 627.9,350.0C609.1,350.0 606.8,350.2 605.2,351.8C604.2,352.8 600.8,361.0 597.6,370.1C594.4,379.1 587.2,399.3 581.5,415.0C575.9,430.7 569.8,447.7 568.0,452.8C566.2,457.9 564.5,461.9 564.3,461.7C564.1,461.4 562.1,455.2 559.9,447.9C557.6,440.5 554.1,429.1 552.1,422.5C550.0,415.9 544.4,397.7 539.5,382.0C534.7,366.3 530.0,352.7 529.2,351.8C527.8,350.2 525.2,350.0 500.9,350.0C477.9,350.0 473.9,350.2 472.6,351.6C471.7,352.4 471.0,353.5 471.0,353.8C471.0,354.2 475.5,368.0 481.0,384.5C489.8,410.8 510.4,474.5 527.4,528.0C530.5,537.7 533.8,546.4 534.7,547.3C536.2,548.8 539.1,549.0 560.0,549.0C577.3,549.0 584.1,548.7 585.3,547.8ZM276.4,509.0C266.5,507.0 258.1,501.8 254.2,495.1C252.0,491.4 251.5,489.3 251.5,484.0C251.5,476.0 254.8,469.6 261.7,464.6C269.8,458.7 274.8,457.5 290.5,457.5C305.4,457.5 311.7,458.9 323.2,464.7L328.0,467.0L328.0,474.4C328.0,480.5 327.5,482.6 324.9,487.8C317.1,503.5 295.8,512.8 276.4,509.0ZM848.3,509.0C825.1,504.1 816.4,482.6 831.5,467.5C838.7,460.2 845.3,457.9 860.1,457.2C873.5,456.7 882.8,458.5 894.4,464.1L901.2,467.4L900.8,474.9C899.9,489.9 890.4,501.5 874.6,507.0C867.8,509.3 854.5,510.3 848.3,509.0Z"/><path fill="#EE8B54" d="M1434.5,553.6C1436.3,552.3 1436.4,549.1 1436.4,463.1L1436.5,374.0L1468.9,374.0C1497.7,374.0 1501.5,373.8 1503.2,372.3C1504.8,370.9 1505.0,368.9 1505.0,352.8C1505.0,342.3 1504.6,334.1 1504.0,332.9C1503.0,331.1 1501.5,331.0 1470.0,331.0L1437.0,331.0L1437.0,296.4C1437.0,274.5 1436.6,261.2 1436.0,259.9C1435.0,258.1 1433.7,258.0 1413.4,258.0L1392.0,258.0L1391.0,260.6C1390.4,262.0 1390.0,277.4 1390.0,297.1L1390.0,331.0L1357.7,331.0C1333.9,331.0 1325.1,331.3 1324.2,332.2C1323.3,333.1 1323.0,339.0 1323.0,352.7C1323.0,370.7 1323.1,372.0 1324.9,373.0C1326.2,373.6 1338.6,374.0 1358.4,374.0L1390.0,374.0L1390.0,462.5C1390.0,549.7 1390.0,551.0 1392.0,553.0C1393.9,554.9 1395.3,555.0 1413.3,555.0C1428.1,555.0 1433.1,554.7 1434.5,553.6Z"/></svg></div>
</footer>
"""

doc = f"""<!DOCTYPE html>
<html lang="en-AU">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'><rect width='64' height='64' rx='14' fill='%23033D2B'/><path fill='%23EE8B54' d='M29 10h6v12h12v6H35v26h-6V28H17v-6h12z'/></svg>">
<title>Always Foundation · Together for the Gospel</title>
<meta name="description" content="Together for the Gospel. Always Foundation brings churches and Christian ministries across Australia together, with free, open-source tools, shared resources and connections to serve Christ and their communities.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&family=Inter:wght@400;500;600&family=Newsreader:opsz,wght@6..72,400&display=swap" rel="stylesheet">
<style>{css}{extra_css}{extras.CSS}{P.CSS}{P.EVENTS_CSS}{P.CLAIM_CSS}{P.RESEARCH_CSS}{P.BRAND_CSS}{P.PLATFORM_CSS}{CP.CSS}{PR.CSS}{DECK_CSS}{DV.CSS}{CF.CSS}{JN.CSS}{DU.CSS}{FT.CSS}{PO.CSS}{MO.CSS}</style>
</head>
<body class="no-js">
<a class="skip" href="#main">Skip to content</a>
{header}
<main id="main">
<div class="page" id="page-home">{home}</div>
<div class="page" id="page-about" hidden>{about}</div>
<div class="page" id="page-docs" hidden>{docs_page}</div>
<div class="page" id="page-churches" hidden>{P.CHURCHES}</div>
<div class="page" id="page-ministries" hidden>{P.MINISTRIES}</div>
<div class="page" id="page-app" hidden>{P.APP}</div>
<div class="page" id="page-faq" hidden>{P.FAQ}</div>
<div class="page" id="page-events" hidden>{P.EVENTS}</div>
<div class="page" id="page-claim" hidden>{P.CLAIM}</div>
<div class="page" id="page-feedback" hidden>{P.FEEDBACK}</div>
<div class="page" id="page-research" hidden>{P.RESEARCH}</div>
<div class="page" id="page-brand" hidden>{P.BRAND}</div>
<div class="page" id="page-platform" hidden>{PR.PLATFORM_OVERVIEW}</div>
<div class="page" id="page-developers" hidden>{DV.PAGE}</div>
<div class="page" id="page-hello" hidden>{CF.HELLO}</div>
<div class="page" id="page-contact" hidden>{CF.CONTACT}</div>
<div class="page" id="page-join" hidden>{JN.PAGE}</div>
{''.join(f'<div class="page" id="page-{k}" hidden>{v}</div>' for k, v in PR.NEW_PAGES.items())}
<div class="page" id="page-compliance" hidden>{CP.PAGE}</div>
</main>
{footer}
{CF.HELPER}
<script>{script}</script>
</body>
</html>
"""

# ---------- photos (Unsplash, hotlinked as the Unsplash guidelines ask; hidden if they can't load)
U = 'https://images.unsplash.com/'
PHOTOS = [  # (photo id, where: (page id, anchor inside it))
  ('photo-1790805370091-2c237d73bf16', ('page-churches', '<section class="sec pg-sec')),
  ('photo-1663162550932-f67b561e656f', ('page-ministries', '<section class="sec pg-sec')),
  ('photo-1775400713633-e4b2b3577fb7', ('page-app', '<section class="sec pg-sec')),
]
for _pid, (_page, _anchor) in PHOTOS:
    _p = doc.index(f'id="{_page}"'); _i = doc.find(_anchor, _p)
    if _i < 0: continue
    _fig = (f'<figure class="photo-band"><img src="{U}{_pid}?w=1800&q=75&auto=format&fit=crop" '
            f'srcset="{U}{_pid}?w=900&q=75&auto=format&fit=crop 900w, {U}{_pid}?w=1800&q=75&auto=format&fit=crop 1800w" '
            f'sizes="100vw" alt="" loading="lazy" onerror="this.parentNode.remove()"></figure>\n')
    doc = doc[:_i] + _fig + doc[_i:]
import re as _re2
doc = _re2.sub(r'(<form\b[^>]*>)', r'\1<input type="text" name="company_site" tabindex="-1" autocomplete="off" aria-hidden="true" style="position:absolute;left:-9999px;width:1px;height:1px">', doc)
doc = doc.replace('{{FAITHTECH_IMG}}', FAITHTECH_IMG)
doc = doc.replace('{{CREDIT}}', 'Scripture quotations marked ESV are from the ESV® Bible (The Holy Bible, English Standard Version®), © 2001 by Crossway, a publishing ministry of Good News Publishers. Used by permission. All rights reserved. Scripture quotations are not covered by our Creative Commons licence. Photos: UEN, Rejoice, Sydney Fire Evangelism, Alpha Australia, CXMMXNS and FaithTech, used with permission; some photos from Unsplash under the Unsplash License.', 1)
doc = doc.replace('</style>', '.photo-band{margin:0;height:min(52vh,480px);overflow:hidden;background:var(--sage)}.photo-band img{width:100%;height:100%;object-fit:cover;display:block}@media (max-width:860px){.photo-band{height:300px}}.photo-credit{font-size:12px;opacity:.65;max-width:1240px;margin:22px auto 0;padding:0 40px;box-sizing:border-box}@media (max-width:640px){.photo-credit{padding:0 22px}}</style>', 1)
_svg = lambda n: 'data:image/svg+xml;base64,' + _b.b64encode(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'img', n), 'rb').read()).decode()
doc = doc.replace('{{LOGO}}', _svg('always-foundation-logo.svg')).replace('{{LOGO_REV}}', _svg('always-foundation-logo-reverse.svg'))
doc = _re2.sub(r'<img (?![^>]*loading=)([^>]*src="img/)', r'<img loading="lazy" decoding="async" \1', doc)
open(os.path.join(ROOT, '..', 'index.html'), 'w').write(doc)
print('pages', len(order), 'bytes', len(doc))
