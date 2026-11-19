"""Integrations: the tools churches and ministries already use, and how Always connects to them."""

LIVE, SOON, BUILDING, PLANNED = 'Live', 'Switching on', 'Building', 'Planned'

GROUPS = [
    ('chms', 'Church management', 'When a church accepts someone, they land in its own system: a person record, a follow-up task and a place in a pathway.', [
        ('Elvanto', 'Person, people flow and follow-up', BUILDING),
        ('Planning Center', 'Person, workflow card and assignee', BUILDING),
        ('Fluro', 'Person and follow-up process', PLANNED),
        ('ChurchSuite', 'Contact and flow', PLANNED),
        ('Breeze', 'Person, tags and follow-up', PLANNED),
    ]),
    ('msg', 'Messaging', 'Churches reach out personally. Always sends only the few messages a person needs to stay in control.', [
        ('Church’s own phone', 'Every welcome and conversation', LIVE),
        ('Email', 'Sent from Sydney through Amazon SES', BUILDING),
        ('SMS', 'An Australian SMS gateway', PLANNED),
        ('WhatsApp', 'Optional for churches, adults only, with consent', PLANNED),
    ]),
    ('events', 'Events, tickets and passes', 'Every ticket, pass and wristband becomes a way to respond, counted by placement with no names.', [
        ('NFC and QR', 'Armbands, tap discs, cards and screens', LIVE),
        ('Humanitix', 'Response links on events and confirmations', PLANNED),
        ('Eventbrite', 'Response links on events and confirmations', PLANNED),
        ('Ticketek, Oztix, Moshtix', 'A response code printed on tickets', PLANNED),
        ('Apple and Google Wallet', 'A response link on every event pass', PLANNED),
    ]),
    ('faith', 'Scripture and next steps', 'The Bible and the right next step, right where someone says yes.', [
        ('YouVersion', 'Scripture in Always Respond and Always Sent', SOON),
        ('Alpha', 'Explore faith at a course nearby', LIVE),
    ]),
    ('auto', 'Automation and AI', 'Connect anything else without custom code, with ids only, never people’s details.', [
        ('Zapier', 'Triggers for introductions and connections', PLANNED),
        ('Make', 'The same, for Make scenarios', PLANNED),
        ('n8n', 'Self-host in Australia to keep it onshore', PLANNED),
        ('AI assistants (MCP)', 'Public church and safety information', BUILDING),
    ]),
    ('platforms', 'For tech platforms', 'Build Always into your own product.', [
        ('Always Safety API', 'The open register and check-up, in your app', LIVE),
        ('Scripture component', '<always-scripture> in one line', SOON),
        ('Sign in with YouVersion', 'For adults, in Always Sent', PLANNED),
    ]),
]

ICONS = {
    'chms': '<circle cx="9" cy="8" r="3"/><path d="M3 19c0-3 3-5 6-5s6 2 6 5"/><circle cx="17" cy="9" r="2.4"/><path d="M15.5 14.2c2.7.2 5 1.9 5 4.8"/>',
    'msg': '<path d="M4 5h16v11H9l-5 4z"/>',
    'events': '<path d="M3 8h18v3a2 2 0 000 4v3H3v-3a2 2 0 000-4z"/><path d="M14 8v10" stroke-dasharray="2 2"/>',
    'faith': '<path d="M5 4h9a3 3 0 013 3v13H8a3 3 0 01-3-3z"/><path d="M11 8v6M8.5 10.5h5"/>',
    'auto': '<path d="M13 3L5 13h6l-1 8 8-10h-6z"/>',
    'platforms': '<path d="M8 7l-5 5 5 5M16 7l5 5-5 5"/>',
}

LOGOS = {
    'Planning Center': ['planningcenter.svg'], 'WhatsApp': ['whatsapp.svg'], 'Eventbrite': ['eventbrite.svg'],
    'Apple and Google Wallet': ['apple.svg', 'googlewallet.svg'], 'Alpha': ['../alpha-logo.png'], 'Zapier': ['zapier.svg'],
    'Make': ['make.svg'], 'n8n': ['n8n.svg'], 'AI assistants (MCP)': ['mcp.svg'], 'Email': ['aws.svg'],
}
INITIALS = {'Elvanto': 'E', 'Fluro': 'F', 'ChurchSuite': 'CS', 'Breeze': 'B', 'Humanitix': 'H', 'YouVersion': 'YV', 'Sign in with YouVersion': 'YV'}

def _mark(name, group):
    if name in LOGOS:
        return '<span class="ig-mark ig-logo" aria-hidden="true">' + ''.join(f'<img src="img/logos/{f}" alt="" loading="lazy">' for f in LOGOS[name]) + '</span>'
    if name in INITIALS:
        return f'<span class="ig-mark ig-ini" aria-hidden="true">{INITIALS[name]}</span>'
    icon = f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ICONS[group]}</svg>'
    return f'<span class="ig-mark" aria-hidden="true">{icon}</span>'

def _card(name, line, status, group='chms'):
    return f'<li class="ig-card rv">{_mark(name, group)}<span class="ig-tx"><b>{name}</b><span>{line}</span></span></li>'

PAGE = '''<section class="page-hero ig-hero"><div class="wrap">
  <p class="pl-kick">Integrations</p>
  <h1>Works with the tools you already use.</h1>
  <p>Always hands people on to your church management system, your messages and your events, with consent travelling the whole way. Your data stays yours, and personal data stays in Australia.</p>
</div></section>
<section class="sec pg-sec ig-sec"><div class="wrap">
''' + ''.join(f'''  <div class="ig-group" id="ig-{k}">
    <div class="ig-head rv"><h2>{t}</h2><p>{d}</p></div>
    <ul class="ig-grid">{''.join(_card(*c, group=k) for c in items)}</ul>
  </div>
''' for k, t, d, items in GROUPS) + '''</div></section>
<section class="sec pg-sec pg-green"><div class="wrap ig-rules">
  <h2 class="pg-h rv">The same rules, whatever we connect</h2>
  <div class="sl-rows sl-rows-4">
    <div class="sl-row rv"><h3>Consent travels</h3><p>Details go only where the person agreed, and a withdrawal reaches every system.</p></div>
    <div class="sl-row rv"><h3>Australia first</h3><p>Personal data stays in Australia. Offshore tools get only what a person agreed to send.</p></div>
    <div class="sl-row rv"><h3>Your system stays yours</h3><p>Pastoral notes never come back to Always, only the outcomes a person agreed to share.</p></div>
    <div class="sl-row rv"><h3>Young people first</h3><p>No one under 18 goes to a messaging or marketing tool, only to their youth partner.</p></div>
  </div>
  <div class="pg-cta rv"><a class="btn btn-peach" href="#/docs/integrations">Read the integration docs</a><a class="btn btn-ghost" href="#/contact">Suggest an integration</a></div>
</div></section>'''

CSS = '''
.ig-hero h1 { max-width: 16ch; }
.ig-legend { list-style: none; display: flex; flex-wrap: wrap; gap: 10px 22px; margin: 28px 0 0; padding: 0; color: var(--on-green); font-size: 14.5px; }
.ig-legend li { display: inline-flex; align-items: center; gap: 8px; }
.ig-legend i { width: 10px; height: 10px; border-radius: 50%; display: inline-block; }
i.ig-live, .ig-st.ig-live::before { background: #4FB286; } i.ig-soon, .ig-st.ig-soon::before { background: var(--peach); }
i.ig-building, .ig-st.ig-building::before { background: #8FB5D9; } i.ig-planned, .ig-st.ig-planned::before { background: #B9B3A8; }
.ig-group { padding: 8px 0 48px; border-bottom: 1px solid var(--line); margin-bottom: 48px; }
.ig-group:last-child { border-bottom: 0; margin-bottom: 0; }
.ig-head { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.3fr); gap: 32px; align-items: end; margin-bottom: 24px; }
.ig-head h2 { margin: 0; font-size: clamp(28px, 3vw, 38px); letter-spacing: -0.03em; color: var(--green); }
.ig-head p { margin: 0; font-size: 17px; line-height: 1.55; color: var(--soft); max-width: 52ch; }
.ig-grid { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; }
.ig-card { display: grid; grid-template-columns: 44px minmax(0, 1fr); grid-template-rows: auto auto; gap: 4px 14px; padding: 18px; border-radius: 20px; background: #FFFDF8; border: 1px solid var(--line); transition: transform .25s cubic-bezier(.2,.7,.2,1), box-shadow .25s ease, border-color .25s ease; }
.ig-card:hover { transform: translateY(-2px); border-color: rgba(27,71,64,.2); box-shadow: 0 18px 36px -26px rgba(10,30,26,.4); }
.ig-mark svg { width: 22px; height: 22px; }
.ig-mark.ig-logo { background: #fff; box-shadow: inset 0 0 0 1px rgba(27,71,64,.1); gap: 3px; grid-auto-flow: column; padding: 0 9px; width: auto; min-width: 44px; justify-self: start; }
.ig-mark.ig-logo img { width: 24px; height: 24px; object-fit: contain; display: block; }
.ig-mark.ig-ini { background: linear-gradient(155deg, #E6F0E9, #D3E4D9); box-shadow: inset 0 0 0 1px rgba(27,71,64,.07); }
.ig-mark { grid-row: 1 / 3; width: 44px; height: 44px; border-radius: 13px; display: grid; place-items: center; background: var(--sage); color: var(--green); font: 800 15px/1 var(--head); letter-spacing: -0.02em; }
.ig-tx b { display: block; font: 800 17px/1.25 var(--head); color: var(--green); }
.ig-tx span { display: block; margin-top: 3px; font-size: 14.5px; line-height: 1.45; color: var(--soft); }
.ig-st { grid-column: 2; justify-self: start; display: inline-flex; align-items: center; gap: 7px; margin-top: 8px; padding: 4px 10px 4px 8px; border-radius: 999px; background: rgba(27,71,64,.06); font: 700 12px/1.2 var(--head); color: var(--green); }
.ig-st::before { content: ''; width: 8px; height: 8px; border-radius: 50%; }
.pg-green .sl-row h3 { color: var(--cream); } .pg-green .sl-row p { color: var(--on-green); } .pg-green .sl-row { border-top-color: rgba(248,243,234,.18); }
.ig-rules .sl-rows-4 { grid-template-columns: repeat(4, minmax(0, 1fr)); }
@media (max-width: 1000px) { .ig-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); } .ig-head { grid-template-columns: minmax(0, 1fr); gap: 10px; } .pg-green .sl-row h3 { color: var(--cream); } .pg-green .sl-row p { color: var(--on-green); } .pg-green .sl-row { border-top-color: rgba(248,243,234,.18); }
.ig-rules .sl-rows-4 { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 640px) { .ig-grid { grid-template-columns: minmax(0, 1fr); } .pg-green .sl-row h3 { color: var(--cream); } .pg-green .sl-row p { color: var(--on-green); } .pg-green .sl-row { border-top-color: rgba(248,243,234,.18); }
.ig-rules .sl-rows-4 { grid-template-columns: minmax(0, 1fr); } }
@media (prefers-reduced-motion: reduce) { .ig-card { transition: none; } .ig-card:hover { transform: none; } }
'''

DOCS = ("Integrations", [
  ("integrations", "Integrations", """
<p class="lead">Always connects to the tools churches and ministries already use, with consent travelling the whole way and personal data kept in Australia.</p>
<table class="dt"><tr><th>Area</th><th>Live or switching on</th><th>Building and planned</th></tr>
<tr><td><a href="#/docs/int-chms">Church management</a></td><td>—</td><td>Elvanto, Planning Center (building); Fluro, ChurchSuite, Breeze</td></tr>
<tr><td><a href="#/docs/int-messaging">Messaging</a></td><td>The church's own phone</td><td>Email from Sydney (building); Australian SMS; WhatsApp</td></tr>
<tr><td><a href="#/docs/taps">Events, tickets and passes</a></td><td>NFC and QR</td><td>Humanitix, Eventbrite, Ticketek, Oztix, Moshtix, Apple and Google Wallet</td></tr>
<tr><td>Scripture and next steps</td><td><a href="#/docs/youversion">YouVersion</a> (switching on), <a href="#/alpha">Alpha</a></td><td>—</td></tr>
<tr><td><a href="#/docs/int-automation">Automation and AI</a></td><td>—</td><td>Zapier, Make, n8n; MCP server (building)</td></tr>
<tr><td>For tech platforms</td><td><a href="#/docs/compliance-api">Safety API</a>, <a href="#/docs/youversion">Scripture component</a></td><td>Sign in with YouVersion</td></tr></table>
<h2>The rules for every integration</h2>
<ul>
<li><b>Consent travels.</b> A person's details go only where they agreed, and a withdrawal reaches every system that holds them.</li>
<li><b>Australia first.</b> Offshore tools receive only what the person agreed to send there, or nothing personal.</li>
<li><b>Your system stays yours.</b> Pastoral notes never come back to Always.</li>
<li><b>Young people first.</b> No one under 18 is sent to a messaging or marketing tool.</li>
</ul>
<p>Want an integration that isn't here? <a href="#/contact">Tell us</a>.</p>
"""),
  ("int-chms", "Church management systems", """
<p class="lead">When a church accepts someone in Always Connect, they land in the church's own system. Elvanto and Planning Center come first.</p>
<h2>What lands</h2>
<ol>
<li><b>A person record:</b> first name, contact and suburb, with their consent receipt as a note.</li>
<li><b>A follow-up task</b> for the connect lead, with a due date.</li>
<li><b>A place in a pathway:</b> Newcomers, Alpha or Youth, chosen by the church.</li>
<li><b>"Connected" back to Always</b>, only if the person agrees, when they attend or join a group.</li>
</ol>
<h2>By system</h2>
<table class="dt"><tr><th>System</th><th>Pathway</th><th>Status</th></tr>
<tr><td>Elvanto</td><td>People flows</td><td>Building</td></tr>
<tr><td>Planning Center</td><td>Workflow cards</td><td>Building</td></tr>
<tr><td>Fluro</td><td>Follow-up processes</td><td>Planned</td></tr>
<tr><td>ChurchSuite</td><td>Flows</td><td>Planned</td></tr>
<tr><td>Breeze</td><td>Tags and follow-ups</td><td>Planned</td></tr></table>
<p>Each one is an adapter behind the open <a href="#/docs/standard">Always Handoff standard</a>. A church switches it on in its Always settings with its own API key or sign-in. Pastoral notes stay in the church's system and never come back to Always.</p>
"""),
  ("int-messaging", "Messaging", """
<p class="lead">Churches reach out personally, from their own phones. Always sends only the few messages a person needs to stay in control of their story.</p>
<table class="dt"><tr><th>Channel</th><th>Who sends it</th><th>What for</th><th>Status</th></tr>
<tr><td>The church's own phone</td><td>The church</td><td>Every welcome and conversation</td><td>Live</td></tr>
<tr><td>Email</td><td>Always, from Sydney</td><td>Who will be in touch, and the private link to say connected or change your mind</td><td>Building</td></tr>
<tr><td>SMS</td><td>Always, through an Australian gateway</td><td>The same, by text</td><td>Planned</td></tr>
<tr><td>WhatsApp</td><td>The church, if it chooses</td><td>Ongoing conversation</td><td>Planned, adults only, with consent</td></tr></table>
<p>No marketing messages, ever. Message previews never mention faith, and nothing goes to anyone under 18 except through their youth partner or a parent.</p>
"""),
  ("int-automation", "Automation and AI", """
<p class="lead">Connect Always to anything else without custom code. Every trigger carries ids only, never people's details.</p>
<ul>
<li><b>Zapier and Make.</b> Triggers when an introduction arrives, is accepted, or someone connects. Look up the details inside Always, with permission.</li>
<li><b>n8n.</b> The same triggers, and you can run n8n yourself in Australia to keep everything onshore.</li>
<li><b>Webhooks.</b> Signed CloudEvents for developers. See <a href="#/docs/webhooks">Webhooks</a>.</li>
<li><b>AI assistants.</b> The Always MCP server shares public church and safety information only. See <a href="#/docs/mcp">Always for AI assistants</a>.</li>
</ul>
"""),
])
