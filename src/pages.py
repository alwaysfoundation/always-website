"""Website pages: For churches, For ministries, Always App, FAQs."""
import json
import os
ROOT = os.path.dirname(os.path.abspath(__file__))
L = json.load(open(os.path.join(ROOT,'paths.json')))
def wm(c, h): return f'<svg width="{round(h*1328/366)}" height="{h}" viewBox="186 250 1328 366" role="img" aria-label="Always"><path fill="{c}" fill-rule="evenodd" d="{"".join(L["word"])}"/><path fill="#EE8B54" d="{"".join(L["cross"])}"/></svg>'

def steps(items):
    return '<div class="pg-steps">' + ''.join(f'<div class="pg-step rv"><span>0{i+1}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate(items)) + '</div>'
def feats(items):
    return '<div class="pg-feats">' + ''.join(f'<div class="pg-feat rv"><h3>{t}</h3><p>{d}</p></div>' for t, d in items) + '</div>'
def phone(inner, cls=''):
    return f'<div class="pg-phone {cls}"><div class="pg-screen">{inner}</div></div>'

church_desk = f'''<div class="pg-desk rv" aria-label="The church inbox on the web">
  <div class="pg-desk-nav">{wm('#F8F3EA', 20)}<span class="on">Inbox</span><span>Walking with</span><span>Our page</span><span>Next steps</span><span>Team</span></div>
  <div class="pg-desk-main">
    <div class="pg-row-h"><b>Inbox</b><span>Hope Church Parramatta</span></div>
    {''.join(f'<div class="pg-li{" sel" if i == 0 else ""}"><span><b>{n}</b> · {w}</span><em class="{c}">{s}</em></div>' for i, (n, w, s, c) in enumerate([('Sam', 'Parramatta · Find a church', 'New', 'new'), ('Priya', 'Westmead · Explore faith first', 'New', 'new'), ('Josh', 'Harris Park · Talk with someone', 'Accepted', 'ok'), ('Mia', 'Granville · Find a church', 'Texted', 'ok')]))}
    <div class="pg-detail"><b>Sam</b><span>Responded at City worship night</span><div class="pg-field">04•• ••• ••• · accept to see</div><div class="pg-btns"><span class="pg-b">Accept</span><span class="pg-b ln">Pass</span></div></div>
  </div>
</div>'''
church_phone = phone(f'''<p class="pg-cap">Always for churches · Inbox</p><div class="pg-card hl"><div class="pg-row-h"><b>Sam</b><em class="new">New</em></div><span class="pg-mut">Parramatta · Find a church</span><div class="pg-field">04•• ••• •••</div><div class="pg-btns"><span class="pg-b">Accept</span><span class="pg-b ln">Pass</span></div></div><div class="pg-card"><div class="pg-row-h"><b>Josh</b><em class="ok">Accepted</em></div><span class="pg-mut">Harris Park · Talk with someone</span></div>''')

CHURCHES = f'''<section class="page-hero"><div class="wrap"><h1>For churches</h1><p>Welcome people near you who have said yes to Jesus, and help them grow as disciples. Free, always.</p></div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">Three steps to welcoming people</h2>
  {steps([('Claim your page', 'Tell us about your church and who you are. It takes about ten minutes.'), ('Get verified', 'We check with your denomination or network, and your connect lead does a 20-minute course.'), ('Welcome people', 'When someone nearby asks for a next step you offer, accept or pass. Then call or text from your own phone.')])}
</div></section>
<section class="sec pg-sec pg-sage"><div class="wrap pg-split">
  <div><h2 class="pg-h rv">Always for churches, in any browser</h2><p class="pg-lead rv">A free web app for your team. Nothing to install, so your connect lead can say yes from their phone on a Sunday.</p>
  <ul class="pg-list rv"><li>See who nearby has asked for a next step, and what they asked for.</li><li>Accept to see their number, or pass so the next church nearby is asked.</li><li>Log that you got in touch. The conversation stays between you.</li></ul></div>
  <div class="pg-mocks">{church_desk}<div class="pg-phone-over rv">{church_phone}</div></div>
</div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">What your church gets</h2>
  {feats([('Your page on the map', 'Your welcome, service times, what to expect, and the next steps you offer, in your colours.'), ('Introductions near you', 'People who have already said yes to Jesus, within the area you choose.'), ('Next steps and capacity', 'Choose what you offer and how many people you can welcome each month. Pause any time.'), ('Your team', 'Invite your pastor, connect lead and youth leaders, each with the right access.'), ('Walking with', 'Keep track of everyone you are welcoming, and get a simple monthly report for your leaders.'), ('Your own tools', 'Use the free inbox, or connect your church management system through the API.')])}
  <div class="pg-cta rv"><a class="btn btn-peach" href="#/claim">Claim your church</a><a class="btn btn-green" href="#/docs/claim">How claiming works</a></div>
</div></section>'''

ministry_desk = f'''<div class="pg-desk rv" aria-label="The ministry dashboard on the web">
  <div class="pg-desk-nav"><b class="pg-mname">CITY EVENTS</b><span class="on">Results</span><span>Inbox</span><span>Response pages</span><span>Team</span></div>
  <div class="pg-desk-main">
    <div class="pg-row-h"><b>City worship night</b><em class="new">Live</em></div>
    <div class="pg-kpis">{''.join(f'<div><b{" class=pe" if i == 3 else ""}>{v}</b><span>{l}</span></div>' for i, (v, l) in enumerate([('128', 'Responded'), ('119', 'Introduced'), ('104', 'Accepted'), ('62', 'Connected')]))}</div>
    {''.join(f'<div class="pg-bar"><span>{l}</span><i><u style="width:{w}%"></u></i><b>{v}</b></div>' for l, w, v in [('Find a church', 100, 64), ('Explore faith', 44, 28), ('Youth group', 34, 22), ('Talk with someone', 22, 14)])}
    <p class="pg-mut">Example figures. Totals only.</p>
  </div>
</div>'''
ministry_phone = phone('<p class="pg-mbrand">YOUR MINISTRY</p><p class="pg-mh">Said yes tonight? Take your next step.</p><div class="pg-mo sel">Find a church near me</div><div class="pg-mo">Join a youth group</div><div class="pg-mo">Explore faith first</div><div class="pg-mbtn">Continue</div>', 'dark')

report_mock = '<div class="pg-desk pg-report rv" aria-label="An example monthly report"><div class="pg-desk-main"><div class="pg-row-h"><b>September report</b><em class="ok">Ready</em></div><span class="pg-mut">City worship tour · Prepared for our supporters</span><div class="pg-kpis">' + ''.join(f'<div><b{" class=pe" if i == 3 else ""}>{v}</b><span>{l}</span></div>' for i, (v, l) in enumerate([('310', 'Responded'), ('295', 'Introduced'), ('258', 'Accepted'), ('117', 'Connected')])) + '</div><div class="pg-btns"><span class="pg-b">Download PDF</span><span class="pg-b ln">Share a link</span></div><p class="pg-mut">Example figures. Totals only.</p></div></div>'

MINISTRIES = f'''<section class="page-hero"><div class="wrap"><h1>For ministries</h1><p>Tours, camps, youth events, outreach and online ministries: free tools to share the Gospel, less administration, and a next step near home for everyone who responds.</p></div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">From the altar call to a church family</h2>
  {steps([('Create a response page', 'Choose the next steps you offer and add your brand. Ready in minutes.'), ('Invite a response', 'Show the QR code on the big screen, hand out cards, or use the response card in your own app.'), ('See the fruit', 'Watch results live, and get a monthly report ready for your funders and board.')])}
</div></section>
<section class="sec pg-sec pg-night"><div class="wrap pg-split">
  <div><h2 class="pg-h rv">Your brand. Live results.</h2><p class="pg-lead rv">People respond on a page that looks like you. Your team sees totals live, and each person's details go only to the church that welcomes them.</p>
  <ul class="pg-list rv"><li>Results for every event, tour and campus.</li><li>An inbox for the steps you offer yourself, like a youth night or a course.</li><li>Street teams and evangelists use the Always App to show their own QR.</li></ul></div>
  <div class="pg-mocks">{ministry_desk}<div class="pg-phone-over rv">{ministry_phone}</div></div>
</div></section>
<section class="sec pg-sec"><div class="wrap pg-split">
  <div><h2 class="pg-h rv">Reporting your funders can trust</h2><p class="pg-lead rv">Answer to donors, a foundation or a denomination? Always Platform writes your report each month. Nothing extra to enter.</p>
  <ul class="pg-list rv"><li>Responded, introduced, contacted, and now part of a church family, month by month.</li><li>Download a PDF or spreadsheet, or send your funder a link you can switch off.</li><li>Your title, your funder's name, your words. Totals only, so no one can be identified.</li></ul>
  <div class="pg-cta rv" style="margin-top:24px"><a class="btn btn-green" href="#/docs/results">See what's in a report</a></div></div>
  <div class="pg-mocks">{report_mock}</div>
</div></section>
<section class="sec pg-sec pg-night"><div class="wrap">
  <h2 class="pg-h rv">Less administration, more ministry</h2>
  <p class="pg-lead rv">Shared tools for the everyday work behind every ministry, so your team can spend more time on people.</p>
  {feats([('Governance', 'Shared policies, templates and member records for boards and leaders.'), ('Compliance', 'Consent records and privacy requests, ready to export when you need them.'), ('Safeguarding', 'Child safety checklists and Working With Children Check reminders, kept in one place.'), ('Reporting', 'A monthly report for your board and funders, with totals only.')])}
</div></section>
<section class="sec pg-sec pg-sage"><div class="wrap pg-split">
  <div><h2 class="pg-h rv">Responses online, too</h2><p class="pg-lead rv">Sharing a testimony, sermon or post? Add a response link or QR code. Anyone in Australia can say yes and meet a church near them.</p></div>
  <pre class="pg-code rv"><code>&lt;always-response
  page="testimony-video"&gt;
&lt;/always-response&gt;

or link to
always.au/r/testimony-video</code></pre>
</div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">Built for events of every size</h2>
  {feats([('Response pages and QR codes', 'For the big screen, printed cards, video descriptions and short links.'), ('Leading the moment', 'Simple wording for the altar call: invite, pray, respond, welcome.'), ('Your team', 'Response team leads, evangelists and youth leaders, each with the right access.'), ('Safe for young people', 'Young people are introduced only to verified youth partners. Under 15s need a parent to confirm.'), ('Reports for funders', 'A monthly report with clear definitions, ready for donors, foundations and your board.'), ('Open API and SDK', 'Add the response card to your own app or website.')])}
  <div class="pg-cta rv"><a class="btn btn-peach" href="#/join">Book a catch-up call</a><a class="btn btn-green" href="#/docs/senders">Read the guide</a></div>
</div></section>'''

app_home = phone('<p class="pg-url">Always App · in your browser</p><p class="pg-serif">Who will you walk with today?</p><div class="pg-verse"><p>“For the Son of Man came to seek and to save the lost.”</p><span>Luke 19:10 (ESV)</span></div><p class="pg-small"><b>Pray for Sam, Priya and Josh</b></p><div class="pg-b pe">Start a response point</div>')
def mini(title, inner): return f'<div class="pg-mini rv"><div class="pg-mini-ph">{phone(inner)}</div><h3>{title}</h3></div>'
APP = f'''<section class="page-hero"><div class="wrap pg-split">
  <div><h1>For evangelists</h1><p>Infrastructure and tools for everyone who shares the Gospel: the Always App, your own branded response app, training and follow-up. All free, so every yes can grow into a disciple.</p><a class="btn btn-peach" href="#/join" style="margin-top:28px">Join the pilot</a></div>
  <div class="pg-hero-ph">{app_home}</div>
</div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">Always App</h2>
  <p class="pg-lead rv">A free web app with everything you need to share Jesus. Nothing to download: open it in your phone's browser and add it to your home screen.</p>
  <div class="pg-minis">
    {mini('Bible', '<p class="pg-cap">John 3 · ESV</p><span class="pg-big">3</span><p class="pg-read"><sup>16</sup> <mark>For God so loved the world, that he gave his only Son…</mark></p>')}
    {mini('Learn', '<p class="pg-cap">The Always path</p>' + ''.join(f'<div class="pg-path"><i class="s{i}"></i><b>0{i+1} / {s}</b></div>' for i, s in enumerate(['Understand', 'Live', 'Share', 'Walk'])))}
    {mini('Gather', '<p class="pg-serif sm">Someone said yes to Jesus. Give them a next step.</p><div class="pg-tile">Show a QR code</div><div class="pg-card">Connect someone now</div>')}
    {mini('Walk', '<p class="pg-cap">Walking with Sam</p>' + ''.join(f'<div class="pg-tick{" done" if d else ""}"><i></i>{t}</div>' for t, d in [('Send a welcome message', 1), ('Share John 3', 1), ('Coffee this week', 0), ('Church together', 0)]))}
    {mini('Connect', '<p class="pg-cap">Near you</p><div class="pg-mapbox"></div><div class="pg-card">Hope Church Parramatta</div><div class="pg-card">City worship night · Fri</div>')}
  </div>
  <p class="pg-built rv">Built on <a href="#/platform">Always Platform</a>: Connect uses the church feed and events, Gather uses response pages and the handoff, and the Bible comes through the YouVersion Platform.</p>
</div></section>
<section class="sec pg-sec pg-sage"><div class="wrap">
  <h2 class="pg-h rv">Made for evangelists, and for everyone</h2>
  {feats([('A beautiful Bible', 'KJV and WEB built in, more through YouVersion. Highlight, share verses as images, listen with soft music and a sleep timer.'), ('Conversation guides', 'How to share with someone with no faith, a Muslim friend, a Jehovah\'s Witness, a Buddhist and more.'), ('Altar calls and the street', 'Start a response point in seconds, coach the moment, and connect people with their yes.'), ('Prayer list and field notes', 'Pray for people by name and keep short notes after a conversation. They stay in your browser, on your own device.'), ('Church team inbox', 'Connect leads accept introductions in Always for churches, on the web.'), ('Private by design', 'Your prayer list, notes and plans stay on your own device. No ads.')])}
</div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">Training</h2>
  <p class="pg-lead rv">Short, free courses you can do in any browser, made with evangelists and churches.</p>
  {feats([('Sharing your story', 'Tell how Jesus changed your life, in three minutes, in your own words.'), ('Leading someone to Jesus', 'What to say, how to pray, and what to do next when someone says yes.'), ('Welcoming well', 'For church connect leads: the first call, the first coffee, the first Sunday.'), ('Safe ministry with young people', 'Child safe practice for youth leaders and events.'), ('Conversations across faiths', 'Listening well and sharing gently with friends of other beliefs.'), ('Walking with someone', 'The first months of following Jesus: Bible, prayer, church and friends.')])}
</div></section>
<section class="sec pg-sec pg-sage"><div class="wrap">
  <h2 class="pg-h rv">Infrastructure for your evangelism</h2>
  <p class="pg-lead rv">Running a street team, an outreach or a tour? Get your own branded response app on Always Platform, like Sydney Fire Evangelism's, and use the same open tools we use, free.</p>
  {feats([('Response pages and QR codes', 'People say yes on a page with your name on it, and get a next step near home.'), ('Find a church near me', 'Add our church finder to your website or app in one line.'), ('Church feed and API', 'Verified churches ready to welcome people, for your own tools.'), ('AI assistants', 'Use Always Platform from Claude and other assistants to find churches and events, with no personal data involved.'), ('Reports for funders', 'Monthly reports written for you, with totals only.'), ('Open source', 'Every tool is open, so you can check it, improve it or run it yourself.')])}
  <div class="pg-cta rv"><a class="btn btn-peach" href="#/join">Join the pilot</a><a class="btn btn-green" href="#/docs/feed">Build with the church feed</a></div>
</div></section>'''

FAQ_GROUPS = [
 ('About Always', [
  ('What is the Always Foundation?', 'An independent, member-based Christian nonprofit that brings churches and Christian ministries together. We equip them with free, open-source tools, support them with shared tools for governance, compliance, safeguarding and reporting, and connect them as one network.'),
  ('Who can become a member?', 'Churches and Christian ministries that affirm the Nicene Creed. Members help shape what we build and share in the benefits. Supporters can join us too, through prayer and giving.'),
  ('What is Always Platform?', 'The open-source technology behind everything we offer members: branded response pages, forms, reports, the directory and the Always App. Developers can build on it too.'),
  ('Who runs it?', 'The Always Foundation, a members-based not-for-profit being established in Australia. Churches and ministries that affirm the Nicene Creed are its members.'),
  ('Is it only for one denomination?', 'No. Evangelical and Pentecostal churches and ministries across denominations and networks take part, on the common ground of the Nicene Creed.'),
  ('Is Always Platform only in Australia?', 'Our focus is Australia. The technology is open source, so churches and ministries in other countries are welcome to use it.'),
  ('How do I sign in?', 'With one Always account, using Apple, Google, YouVersion or your email. The same account works across the Always App and every tool built on Always Platform.')]),
 ('For churches', [
  ('Does it cost anything?', 'No. Churches never pay. Larger ministries contribute according to their size.'),
  ('How do we join?', 'Claim your church\'s page, and we verify you with your denomination or network.'),
  ('What if we can\'t welcome someone?', 'Pass, with a reason. The next church or ministry nearby is asked. If none can, our care team helps.'),
  ('Do we have to change our church software?', 'No. Use the free inbox in Always for churches, in any browser, or connect your system through the API. Elvanto and Planning Center come first.'),
  ('What does welcoming now mean?', 'You\'re verified, trained, have room this month and usually reply on time. If you get busy, introductions simply pause.'),
  ('Who on our team can see people\'s details?', 'Only the people you add to your team, and only after your church accepts an introduction.')]),
 ('For ministries and events', [
  ('Can we use our own brand?', 'Yes. Response pages, QR codes and texts can use your colours, logo and wording.'),
  ('What results do we see?', 'Totals for each event: responded, introduced, accepted and connected. Each person\'s details go only to the church that welcomes them.'),
  ('Can Always Platform help us report to our funders?', 'Yes. It writes a monthly report for you: who responded, who was introduced, who was contacted, and who is now part of a church family. Download it as a PDF or spreadsheet, or send your funder a link.'),
  ('Will our funders see people\'s details?', 'No. Reports show totals only, and small numbers are hidden so no one can be identified.'),
  ('Can Always Platform help with privacy and child safety paperwork?', 'Yes. Your Compliance tab keeps your consent records, privacy requests, child safety checklists and Working With Children Check reminders, ready to export.'),
  ('Can we make the report our own?', 'Yes. Add your title, your funder\'s name and a short introduction. If a funder needs something specific, talk to us.'),
  ('Can we receive introductions ourselves?', 'Yes, for the steps you offer, like a youth night or a course.'),
  ('Can people respond online?', 'Yes. Add a response link or QR to a video description or post, or embed the response card on your website. An invisible check stops spam without puzzles.'),
  ('Can we list our events?', 'Yes. Add them from Always for churches and ministries, and they show on our Events page and in Always App.'),
  ('How do evangelists and street teams use it?', 'With Always App, a free web app: they start a response point, show their own QR, or connect someone in a conversation with their yes.')]),
 ('For people who respond', [
  ('What happens when I respond?', 'You choose a next step, see who will be in touch, and a church or ministry near you reaches out.'),
  ('What do you need from me?', 'Your first name, a mobile number and your suburb.'),
  ('Do I need to download an app?', 'No. You respond on a simple web page. Later, you\'re welcome to try Always App in your browser to read the Bible and grow.'),
  ('Can I change my mind?', 'Yes, any time, from the link in your text. Your details are then deleted.'),
  ('I\'m under 18. Can I still respond?', 'Yes. If you\'re under 15, a parent or guardian says yes with you. From 15 you can decide for yourself. Young people are introduced only to verified youth partners, and no AI ever touches your information.')]),
 ('Always App', [
  ('Who is it for?', 'Every Christian who wants to share Jesus and walk with people, and church teams who welcome them.'),
  ('How do I get it?', 'It\'s a web app, so there\'s nothing to download. It\'s in pilot: join through the form on our home page.'),
  ('Is there a mobile app?', 'Not for now. The Always App and our tools for churches and ministries run in the browser on your phone, tablet or computer, and you can add it to your home screen.'),
  ('Which Bible translations are included?', 'The King James Version and the World English Bible, with more through YouVersion.'),
  ('Where are my notes and prayer list kept?', 'In your browser, on your own device. They aren\'t sent to us.')]),
 ('Privacy and safety', [
  ('Where is information kept?', 'In Australia, encrypted, under Australian privacy law.'),
  ('Do you sell information or use it for advertising?', 'No.'),
  ('How do you use AI?', 'To save time on routine work, like writing your monthly report. Every welcome comes from a real person, and young people\'s information is kept out of AI entirely.'),
  ('How do I report a concern?', 'Email safeguarding@alwaysfoundation.org for safeguarding, privacy@ for privacy and security@ for security.')]),
 ('Supporters and builders', [
  ('How is the Always Foundation funded?', 'By supporters, and by larger ministries contributing according to their size. Churches never pay.'),
  ('How can I support the work?', 'Pray with us, and get in touch at hello@alwaysfoundation.org to book a catch-up call.'),
  ('Can developers build on Always Platform?', 'Yes. The API, SDK and open standard are open source under Apache 2.0, with docs under CC BY 4.0. An MCP server for AI assistants is coming, and it never sees a person\'s details.')])]

FAQ = '<section class="page-hero"><div class="wrap"><h1>FAQs</h1><p>Short answers to the questions we hear most.</p></div></section><section class="sec pg-sec"><div class="wrap pg-faq">' + \
  '<nav class="pg-faq-nav" aria-label="FAQ topics">' + ''.join(f'<a href="#faq-{i}" data-faq="{i}">{g}</a>' for i, (g, _) in enumerate(FAQ_GROUPS)) + '</nav><div>' + \
  ''.join(f'<div class="pg-faq-g" id="faq-{i}"><h2>{g}</h2>' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in qs) + '</div>' for i, (g, qs) in enumerate(FAQ_GROUPS)) + \
  '<div class="pg-faq-more"><h3>Still have a question?</h3><p>Email <b>hello@alwaysfoundation.org</b>. We\'d love to book a catch-up call.</p></div></div></div></section>'

CSS = '''
.pg-code { background: var(--night, #1E2A26); color: #E4EEE7; border-radius: 22px; padding: 26px 28px; font: 500 15.5px/1.7 ui-monospace, Menlo, monospace; margin: 0; overflow-x: auto; }
.pg-sec { padding: 96px 0; }
.pg-sage { background: var(--sage); }
.pg-night { background: var(--night, #1E2A26); color: var(--cream); }
.pg-night .pg-lead, .pg-night .pg-list li { color: var(--on-green); }
.pg-h { font: 800 clamp(32px, 4vw, 52px)/1.05 var(--head); letter-spacing: -0.035em; margin: 0; }
.pg-lead { font-size: 19px; line-height: 1.6; color: var(--soft); margin-top: 18px; max-width: 560px; }
.pg-list { margin: 22px 0 0; padding-left: 22px; display: grid; gap: 10px; font-size: 17px; line-height: 1.55; color: var(--soft); }
.pg-steps { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; margin-top: 44px; }
.pg-step { background: var(--paper); border-radius: 26px; padding: 30px; }
.pg-step span { font: 700 15px var(--head); color: var(--clay); }
.pg-step h3, .pg-feat h3 { font: 800 23px/1.2 var(--head); letter-spacing: -0.02em; margin: 10px 0 8px; }
.pg-step p, .pg-feat p { margin: 0; font-size: 16.5px; line-height: 1.55; color: var(--soft); }
.pg-feats { display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; margin-top: 44px; }
.pg-feat { background: var(--paper); border-radius: 24px; padding: 26px; }
.pg-sage .pg-feat { background: var(--paper); }
.pg-feat h3 { margin-top: 0; }
.pg-cta { display: flex; gap: 12px; flex-wrap: wrap; margin-top: 40px; }
.pg-split { display: grid; grid-template-columns: minmax(0, .9fr) minmax(0, 1.1fr); gap: 56px; align-items: center; }
.pg-mocks { position: relative; padding: 0 120px 40px 0; }
.page-hero .pg-screen p, .page-hero .pg-screen b { color: var(--ink); }
.page-hero .pg-verse p { color: var(--cream); }
.pg-desk { background: var(--paper); color: var(--ink); border-radius: 20px; display: grid; grid-template-columns: 150px 1fr; overflow: hidden; box-shadow: 0 40px 70px -40px rgba(0,0,0,.45); font-size: 13px; }
.pg-report { grid-template-columns: 1fr; max-width: 500px; margin: 0 auto; }
.pg-report .pg-desk-main { min-height: 0; gap: 10px; }
.pg-desk-nav { background: var(--green); color: var(--on-green); padding: 18px 12px; display: flex; flex-direction: column; gap: 4px; }
.pg-desk-nav svg { margin: 0 6px 14px; }
.pg-desk-nav span { padding: 8px 10px; border-radius: 9px; font: 600 12.5px var(--head); }
.pg-desk-nav span.on { background: rgba(248,243,234,.14); color: var(--cream); }
.pg-mname { font: 800 12px var(--head); letter-spacing: .08em; color: var(--cream); margin: 2px 8px 14px; }
.pg-desk-main { padding: 18px 20px 24px; display: flex; flex-direction: column; gap: 8px; min-height: 340px; }
.pg-row-h { display: flex; justify-content: space-between; align-items: center; gap: 8px; }
.pg-row-h b { font: 800 17px var(--head); }
.pg-row-h span { color: var(--soft); font-size: 12px; }
.pg-li { display: flex; justify-content: space-between; align-items: center; padding: 9px 10px; border-radius: 9px; border-top: 1px solid var(--line); color: var(--soft); }
.pg-li b { color: var(--ink); font-family: var(--head); }
.pg-li.sel { background: #F3EEE4; border-top-color: transparent; }
em.new, em.ok { font: 700 10.5px var(--head); font-style: normal; padding: 4px 7px; border-radius: 7px; }
em.new { background: #FDF0D9; color: #7A4B07; } em.ok { background: var(--sage); color: var(--green); }
.pg-detail { background: var(--cream); border-radius: 14px; padding: 14px; display: flex; flex-direction: column; gap: 8px; margin-top: 4px; }
.pg-detail > b { font: 800 17px var(--head); } .pg-detail > span { color: var(--soft); font-size: 12px; }
.pg-field { min-height: 34px; border-radius: 9px; border: 1px solid var(--line); background: var(--paper); padding: 0 10px; display: flex; align-items: center; font-size: 12.5px; color: var(--soft); }
.pg-btns { display: flex; gap: 8px; }
.pg-b { flex: 1; min-height: 36px; border-radius: 10px; background: var(--green); color: var(--cream); display: flex; align-items: center; justify-content: center; font-weight: 600; font-size: 13px; }
.pg-b.ln { background: transparent; border: 2px solid var(--green); color: var(--green); }
.pg-b.pe { background: var(--peach); color: var(--ink); margin-top: auto; flex: none; min-height: 42px; }
.pg-kpis { display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; }
.pg-kpis div { background: var(--cream); border-radius: 12px; padding: 10px 12px; }
.pg-kpis b { display: block; font: 800 22px var(--head); } .pg-kpis b.pe { color: var(--clay); }
.pg-kpis span { font-size: 11px; color: var(--soft); }
.pg-bar { display: grid; grid-template-columns: 110px 1fr 28px; gap: 10px; align-items: center; font-size: 12px; }
.pg-bar i { height: 8px; border-radius: 999px; background: #EFE7DA; overflow: hidden; } .pg-bar u { display: block; height: 100%; background: var(--green); border-radius: 999px; }
.pg-bar b { font-family: var(--head); text-align: right; }
.pg-mut { color: var(--soft); font-size: 12px; margin: 0; }
.pg-phone-over { position: absolute; right: -10px; bottom: -10px; width: 210px; }
.pg-phone { background: #0d1412; border-radius: 34px; padding: 8px; box-shadow: 0 40px 70px -35px rgba(0,0,0,.55); }
.pg-screen { background: var(--cream); color: var(--ink); border-radius: 27px; height: 400px; padding: 26px 13px 13px; display: flex; flex-direction: column; gap: 8px; overflow: hidden; font-size: 12px; }
.pg-phone.dark .pg-screen { background: #0B1026; color: #fff; }
.pg-cap { font: 700 11px var(--head); color: var(--clay); margin: 0; }
.pg-card { background: var(--paper); border-radius: 12px; padding: 10px; display: flex; flex-direction: column; gap: 6px; font-weight: 600; }
.pg-card.hl { border: 2px solid var(--peach); }
.pg-card .pg-row-h b { font-size: 14px; }
.pg-mbrand { font: 800 11px var(--head); letter-spacing: .12em; margin: 0; }
.pg-mh { font: 800 17px/1.15 var(--head); margin: 6px 0; }
.pg-mo { background: #151B3A; border: 1px solid #252C55; border-radius: 10px; padding: 10px; font-size: 12px; }
.pg-mo.sel { background: #5B6AD6; border-color: #5B6AD6; }
.pg-mbtn { margin-top: auto; background: #5B6AD6; border-radius: 10px; min-height: 38px; display: flex; align-items: center; justify-content: center; font-weight: 600; }
.pg-hero-peach { background: var(--peach); color: var(--ink); }
.pg-hero-peach h1 { color: var(--ink); } .pg-hero-peach p { color: #5A3A22; }
.pg-hero-ph { display: flex; justify-content: center; }
.pg-hero-ph .pg-phone { width: 260px; } .pg-hero-ph .pg-screen { height: 500px; font-size: 13px; padding: 30px 16px 16px; }
.pg-serif { font: 400 22px/1.15 var(--serif, Georgia), Georgia, serif; margin: 0; } .pg-serif.sm { font-size: 17px; }
.pg-verse { background: var(--green); color: var(--cream); border-radius: 14px; padding: 12px; }
.pg-verse p { margin: 0; font: 400 14px/1.4 var(--serif, Georgia), Georgia, serif; } .pg-verse span { font-size: 10.5px; color: var(--peach); }
.pg-small { margin: 0; font-size: 12px; }
.pg-minis { display: grid; grid-template-columns: repeat(5, 1fr); gap: 18px; margin-top: 44px; }
.pg-mini h3 { font: 800 20px var(--head); margin: 14px 0 0; text-align: center; }
.pg-mini .pg-screen { height: 340px; }
.pg-big { font: 400 40px/0.9 var(--serif, Georgia), Georgia, serif; color: var(--clay); }
.pg-read { margin: 0; font: 400 13px/1.6 var(--serif, Georgia), Georgia, serif; } .pg-read mark { background: #F6D9B8; }
.pg-path { display: flex; gap: 8px; align-items: center; padding: 4px 0; font-family: var(--head); }
.pg-path i { width: 16px; height: 16px; border-radius: 999px; background: var(--line); } .pg-path i.s0 { background: var(--green); } .pg-path i.s1 { background: var(--peach); }
.pg-tile { background: var(--green); color: var(--cream); border-radius: 12px; min-height: 90px; padding: 10px; display: flex; align-items: flex-end; font: 700 13px var(--head); }
.pg-tick { display: flex; gap: 8px; align-items: center; padding: 7px 0; border-bottom: 1px solid var(--line); }
.pg-tick i { width: 16px; height: 16px; border-radius: 999px; border: 2px solid #CFC3AE; flex: none; }
.pg-tick.done { color: var(--muted); text-decoration: line-through; } .pg-tick.done i { background: var(--green); border-color: var(--green); }
.pg-mapbox { height: 80px; border-radius: 12px; background: var(--sage); }
.pg-faq { display: grid; grid-template-columns: 240px minmax(0, 1fr); gap: 56px; }
.pg-faq-nav { position: sticky; top: 24px; align-self: start; display: flex; flex-direction: column; gap: 4px; }
.pg-faq-nav a { padding: 9px 12px; border-radius: 10px; color: var(--soft); text-decoration: none; font-size: 15.5px; }
.pg-faq-nav a:hover { background: var(--paper); color: var(--ink); }
.pg-faq-g { margin-bottom: 44px; scroll-margin-top: 24px; }
.pg-faq-g h2 { font: 800 30px var(--head); letter-spacing: -0.025em; color: var(--green); margin: 0 0 12px; }
.pg-faq details { border-top: 1px solid var(--line); }
.pg-faq summary { cursor: pointer; list-style: none; padding: 18px 40px 18px 0; position: relative; font: 700 18.5px/1.35 var(--head); }
.pg-faq summary::-webkit-details-marker { display: none; }
.pg-faq summary::after { content: '+'; position: absolute; right: 6px; top: 14px; font: 600 26px var(--head); color: var(--clay); transition: transform .2s; }
.pg-faq details[open] summary::after { transform: rotate(45deg); }
.pg-faq details p { margin: 0 0 20px; font-size: 17px; line-height: 1.6; color: var(--soft); max-width: 720px; }
.pg-faq-more { background: var(--sage); border-radius: 24px; padding: 28px 30px; }
.pg-faq-more h3 { font: 800 22px var(--head); margin: 0 0 6px; } .pg-faq-more p { margin: 0; color: var(--soft); }
@media (max-width: 1020px) {
  .pg-steps, .pg-feats { grid-template-columns: 1fr 1fr; }
  .pg-split { grid-template-columns: 1fr; }
  .pg-minis { grid-template-columns: repeat(3, 1fr); }
  .pg-faq { grid-template-columns: 1fr; gap: 24px; } .pg-faq-nav { position: static; flex-direction: row; flex-wrap: wrap; }
}
@media (max-width: 640px) {
  .pg-mocks { padding: 0 0 20px; }
  .pg-steps, .pg-feats { grid-template-columns: 1fr; }
  .pg-minis { grid-template-columns: 1fr 1fr; }
  .pg-desk { grid-template-columns: 1fr; } .pg-desk-nav { flex-direction: row; flex-wrap: wrap; } .pg-desk-nav svg { display: none; }
  .pg-phone-over { position: static; width: 220px; margin: 20px auto 0; }
  .pg-kpis { grid-template-columns: 1fr 1fr; }
}
'''

# ---------------- Events
EVENTS_DATA = [
 ('2026-11-21', 'City worship night', 'worship', 'Parramatta', 'NSW'),
 ('2026-11-22', 'Street outreach: Town Hall steps', 'outreach', 'Sydney', 'NSW'),
 ('2026-11-28', 'Carols with a gospel invitation', 'music', 'Liverpool', 'NSW'),
 ('2026-11-29', 'Evangelism training morning', 'training', 'Blacktown', 'NSW'),
 ('2026-12-05', 'Youth night', 'youth', 'Geelong', 'VIC'),
 ('2026-12-06', 'Prayer for the city', 'prayer', 'Brisbane', 'QLD'),
 ('2026-12-12', 'Summer worship gathering', 'worship', 'Perth', 'WA'),
 ('2027-01-12', 'Summer youth camp', 'youth', 'Adelaide Hills', 'SA'),
 ('2027-02-06', 'Exploring faith: a 6-week course', 'course', 'Hobart', 'TAS'),
]
KIND_LABEL = {'worship': 'Worship', 'music': 'Music', 'outreach': 'Outreach', 'training': 'Training', 'youth': 'Youth', 'prayer': 'Prayer', 'course': 'Course'}
import datetime as _dt
def _ev(d, t, k, s, st):
    dt = _dt.date.fromisoformat(d)
    return f'<article class="ev" data-k="{k}" data-s="{st}"><div class="ev-d"><b>{dt.day}</b><span>{dt.strftime("%b").upper()}</span></div><div class="ev-b"><h3>{t}</h3><p>{s}, {st}</p></div><span class="ev-k">{KIND_LABEL[k]}</span></article>'
EVENTS = f'''<section class="page-hero"><div class="wrap"><h1>Events</h1><p>Christian events across Australia: worship nights, concerts, outreach, youth camps, courses and training. Go together, and bring someone.</p></div></section>
<section class="sec pg-sec"><div class="wrap">
  <div class="ev-tools">
    <label class="skip" for="ev-s">State</label><select id="ev-s"><option value="">All states</option>{"".join(f"<option>{s}</option>" for s in ["NSW","VIC","QLD","WA","SA","TAS","ACT","NT"])}</select>
    <label class="skip" for="ev-k">Type</label><select id="ev-k"><option value="">All types</option>{"".join(f'<option value="{k}">{v}</option>' for k, v in KIND_LABEL.items())}</select>
  </div>
  <div class="ev-list" id="ev-list">{"".join(_ev(*e) for e in EVENTS_DATA)}</div>
  <p class="ev-empty" id="ev-empty" hidden>No events match yet. Try another state or type.</p>
  <p class="pg-mut" style="margin-top:14px">Example events while the calendar is in pilot.</p>
  <div class="ev-add rv">
    <div><h3>Running an event?</h3><p>Churches and ministries add events from Always for churches and ministries. Anyone can suggest one, and our team checks every event before it shows.</p></div>
    <a class="btn btn-peach" href="#/join">Suggest an event</a>
  </div>
</div></section>'''
EVENTS_CSS = '''
.ev-tools { display: flex; gap: 12px; margin-bottom: 22px; flex-wrap: wrap; }
.ev-tools select { width: auto; height: 52px; border-radius: 14px; border: 1px solid var(--line); background: var(--paper); padding: 0 16px; font-size: 16px; color: var(--ink); min-width: 180px; }
.ev-list { display: grid; gap: 12px; }
.ev { display: grid; grid-template-columns: 72px 1fr auto; gap: 20px; align-items: center; background: var(--paper); border-radius: 22px; padding: 18px 22px; }
.ev-d { width: 64px; height: 68px; border-radius: 16px; background: var(--sage); display: flex; flex-direction: column; align-items: center; justify-content: center; color: var(--green); }
.ev-d b { font: 800 26px/1 var(--head); } .ev-d span { font: 700 12px var(--head); letter-spacing: .06em; }
.ev-b h3 { font: 800 20px/1.25 var(--head); margin: 0; letter-spacing: -0.01em; } .ev-b p { margin: 4px 0 0; color: var(--soft); font-size: 15.5px; }
.ev-k { font: 700 13px var(--head); color: var(--clay); }
.ev-empty { padding: 30px; text-align: center; color: var(--soft); background: var(--paper); border-radius: 22px; }
.ev-add { margin-top: 40px; background: var(--sage); border-radius: 26px; padding: 30px 34px; display: grid; grid-template-columns: 1fr auto; gap: 24px; align-items: center; }
.ev-add h3 { font: 800 24px var(--head); margin: 0; } .ev-add p { margin: 6px 0 0; color: var(--soft); max-width: 640px; }
@media (max-width: 640px) { .ev { grid-template-columns: 64px 1fr; } .ev-k { grid-column: 2; } .ev-add { grid-template-columns: 1fr; } }
'''

# ---------------- Claim a church, and ideas and problems
ROLES = ['Senior pastor or minister', 'Pastor or staff member', 'Elder or board member', 'Administrator or office manager', 'Connect or welcome lead', 'Youth leader']
CLAIM = '''<section class="page-hero"><div class="wrap"><h1>Claim your church</h1><p>Manage your page, choose the next steps you offer, and start welcoming people near you. Free, always.</p></div></section>
<section class="sec pg-sec"><div class="wrap cl-grid">
  <div>
    <form class="cl-form" id="claim-form" novalidate>
      <label>Your church<input name="church" required autocomplete="organization" placeholder="Church or ministry name"></label>
      <label>Suburb<input name="suburb" required placeholder="Suburb and state, like Parramatta NSW"></label>
      <label>Your name<input name="name" required autocomplete="name"></label>
      <label>Your role<select name="role" required><option value="">Choose your role</option>''' + ''.join(f'<option>{r}</option>' for r in ROLES) + '''</select></label>
      <label>Work email<input name="email" type="email" required autocomplete="email" placeholder="you@yourchurch.org.au"></label>
      <label>How can we confirm your role? <span>Optional</span><input name="evidence" placeholder="A link to your church or denomination website"></label>
      <label class="cl-check"><input type="checkbox" name="creed" required> Our church affirms the Nicene Creed, and I can act for it.</label>
      <button class="btn btn-green" type="submit">Send claim</button>
      <p class="cl-status" id="cl-status" role="status" aria-live="polite"></p>
    </form>
    <div class="cl-done" id="cl-done" hidden><h2>Thanks. We've got your claim.</h2><p>Our team will check with your denomination or network and email you when your page is ready.</p><a class="btn btn-peach" href="#/docs/welcoming">Read about welcoming well</a></div>
  </div>
  <aside class="cl-side">
    <h3>What happens next</h3>
    <ol><li><b>We check your role</b> with your denomination or network.</li><li><b>You set up your page</b>: welcome, service times and next steps.</li><li><b>Your connect lead</b> completes the 20-minute welcoming course.</li><li><b>You're verified</b>, and people nearby can be introduced to you.</li></ol>
      </aside>
</div></section>'''
FEEDBACK = '''<section class="page-hero"><div class="wrap"><h1>Ideas and problems</h1><p>Help us make Always Platform better. Share an idea, report something that isn't working, or tell us about a church we've missed.</p></div></section>
<section class="sec pg-sec"><div class="wrap cl-grid">
  <form class="cl-form" id="fb-form" novalidate>
    <div class="fb-kinds" role="radiogroup" aria-label="What would you like to share?">
      <label class="fb-kind"><input type="radio" name="kind" value="idea" checked><span><b>An idea</b>Something that would help</span></label>
      <label class="fb-kind"><input type="radio" name="kind" value="bug"><span><b>A problem</b>Something isn't working</span></label>
      <label class="fb-kind"><input type="radio" name="kind" value="missing"><span><b>A missing church</b>Add a church or ministry</span></label>
    </div>
    <label>Where<select name="area"><option>The website</option><option>Always App</option><option>Always for churches and ministries</option><option>A response page</option><option>Somewhere else</option></select></label>
    <label id="fb-msg-l">Tell us more<textarea name="message" rows="6" required></textarea></label>
    <label>Your email <span>Optional, if you'd like a reply</span><input name="email" type="email" autocomplete="email"></label>
    <button class="btn btn-green" type="submit">Send</button>
    <p class="cl-status" id="fb-status" role="status" aria-live="polite"></p>
    <div class="cl-done" id="fb-done" hidden><h2>Thank you.</h2><p>We read every message. If you left your email, we'll be in touch.</p></div>
  </form>
  <aside class="cl-side">
    <h3>For developers</h3>
    <p class="pg-mut">Always Platform is open source. You can also open an issue or suggest a change on GitHub.</p>
    <a class="btn btn-peach" href="https://github.com/alwaysfoundation">Always on GitHub</a>
    <h3 style="margin-top:28px">Something urgent?</h3>
    <p class="pg-mut">Safeguarding: safeguarding@alwaysfoundation.org<br>Security: security@alwaysfoundation.org</p>
  </aside>
</div></section>'''
CLAIM_CSS = '''
.cl-form[hidden], .cl-done[hidden], .cl-form [hidden] { display: none !important; }
.cl-form label > span { font-size: 14px; margin-top: -4px; }
.cl-grid { display: grid; grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr); gap: 56px; align-items: start; }
.cl-org { background: var(--sage); border-radius: 24px; padding: 24px 26px; margin-bottom: 22px; }
.cl-org h2 { font: 800 28px/1.15 var(--head); margin: 6px 0 4px; letter-spacing: -0.02em; }
form.cl-form { display: grid; gap: 16px; background: none; padding: 0; border-radius: 0; }
.cl-form label { display: grid; gap: 7px; font: 600 15px var(--text); color: var(--ink); }
.cl-form label span { font-weight: 400; color: var(--soft); }
.cl-form input:not([type=checkbox]):not([type=radio]), .cl-form select, .cl-form textarea { width: 100%; min-height: 52px; border-radius: 14px; border: 1px solid var(--line); background: var(--paper); padding: 12px 16px; font: 16px var(--text); color: var(--ink); box-sizing: border-box; }
.cl-form textarea { resize: vertical; }
.cl-check { display: flex !important; grid-template-columns: none; align-items: flex-start; gap: 12px !important; font-weight: 500 !important; line-height: 1.45; }
.cl-check input { width: 22px; height: 22px; accent-color: var(--green); margin-top: 1px; flex: none; }
.cl-form .btn { justify-self: start; }
.cl-status { margin: 0; color: var(--clay); font-weight: 600; min-height: 1.4em; }
.cl-results { display: grid; gap: 6px; margin-top: -6px; }
.cl-results button { text-align: left; border: 1px solid var(--line); background: var(--paper); border-radius: 12px; padding: 12px 14px; font: 15px var(--text); color: var(--ink); cursor: pointer; }
.cl-results button b { font-family: var(--head); }
.cl-results button span { color: var(--soft); }
.cl-results button:hover, .cl-results button:focus-visible { border-color: var(--green); }
.cl-side { background: var(--paper); border-radius: 26px; padding: 30px; }
.cl-side h3 { font: 800 22px var(--head); margin: 0 0 12px; }
.cl-side ol { margin: 0 0 18px; padding-left: 22px; display: grid; gap: 10px; color: var(--soft); line-height: 1.5; }
.cl-side ol b { color: var(--ink); }
.cl-done { background: var(--sage); border-radius: 24px; padding: 30px; }
.cl-done h2 { font: 800 30px var(--head); margin: 0 0 8px; letter-spacing: -0.02em; }
.cl-done p { color: var(--soft); margin: 0 0 18px; }
.fb-kinds { display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }
.fb-kind { position: relative; }
.fb-kind input { position: absolute; opacity: 0; }
.fb-kind span { display: grid; gap: 3px; border: 1px solid var(--line); background: var(--paper); border-radius: 16px; padding: 16px; font: 400 14px var(--text); color: var(--soft); cursor: pointer; min-height: 76px; }
.fb-kind span b { font: 800 17px var(--head); color: var(--ink); }
.fb-kind input:checked + span { background: var(--green); border-color: var(--green); color: var(--on-green); }
.fb-kind input:checked + span b { color: var(--cream); }
.fb-kind input:focus-visible + span { outline: 3px solid var(--peach); outline-offset: 2px; }
@media (max-width: 860px) { .cl-grid { grid-template-columns: 1fr; } .fb-kinds { grid-template-columns: 1fr; } }
'''

# ---------------- Research
RESEARCH_ITEMS = [
  ('Brief', 'In progress', 'What happens after a yes', 'Every week people respond to Jesus at events, services and online. We\'re studying what happens after someone says yes: where people get lost, and what helps them take a next step.', None),
  ('Standard', 'Published', 'Consent that travels with the person', 'How a consent receipt can move between ministries and systems, what it records, and why every system checks it before it acts. Built on ISO/IEC TS 27560 for consent records.', '#/docs/consent'),
  ('Field notes', 'Published', 'Agents with a human in the loop', 'The Always Network grew out of an earlier project called Branches. Its agent checked each response and handed it to a person before anything was shared. Trialled at a youth event with UEN, it shaped how the Always Agent works today.', '#/docs/always-agent'),
  ('Brief', 'In progress', 'Measuring humbly', 'What we count, what we don’t, and why a person is only counted as connected when they say so themselves. Totals only, with minimum group sizes so no one can be identified.', '#/docs/results'),
]
RESEARCH = '''<section class="page-hero"><div class="wrap"><h1>Research</h1><p>We learn in the open: briefs and field notes from building Always Platform with churches and ministries.</p></div></section>
<section class="sec pg-sec"><div class="wrap"><div class="rs-list">''' + ''.join(
  f'<article class="rs-item"><p class="rs-meta">{k} · <span class="{"rs-live" if s == "Published" else "rs-soon"}">{s}</span></p><h2>{t}</h2><p>{d}</p>' + (f'<a href="{l}">Read more</a>' if l else '') + '</article>'
  for k, s, t, d, l in RESEARCH_ITEMS) + '''</div>
<div class="rs-note"><h3>Research with us</h3><p>Working on discipleship, follow-up or faith and technology in Australia? We'd love to collaborate and share what we learn. Email <a href="mailto:hello@alwaysfoundation.org">hello@alwaysfoundation.org</a>.</p></div>
</div></section>'''
RESEARCH_CSS = '''
.rs-list { display: grid; gap: 18px; }
.rs-item { background: var(--paper); border-radius: 26px; padding: 32px 36px; display: grid; gap: 10px; }
.rs-item h2 { font-size: 27px; letter-spacing: -0.02em; color: var(--green); }
.rs-item p { margin: 0; color: var(--soft); max-width: 70ch; }
.rs-item a { color: var(--clay); font-weight: 600; justify-self: start; }
.rs-meta { font: 700 15px var(--head); color: var(--muted) !important; }
.rs-live { color: var(--green); } .rs-soon { color: var(--clay); }
.rs-note { margin-top: 56px; background: var(--sage); border-radius: 26px; padding: 36px; }
.rs-note h3 { font-size: 27px; color: var(--green); } .rs-note p { margin: 10px 0 0; color: var(--soft); }
@media (max-width: 640px) { .rs-item, .rs-note { padding: 26px 22px; } }
'''


def _swatch(name, hexv, use, dark=False):
    return f'<div class="br-sw"><span class="br-chip" style="background:{hexv}"></span><b>{name}</b><code>{hexv}</code><span>{use}</span></div>'

BRAND = f'''<section class="page-hero"><div class="wrap">
  <h1>Brand</h1><p>How Always looks and sounds. Use it freely when you talk about Always.</p>
</div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">Logo</h2>
  <p class="pg-lead rv">The word "always", ending in a cross: Jesus at the end of every always.</p>
  <div class="br-logos">
    <figure class="br-logo"><img src="{{{{LOGO}}}}" alt="Always Foundation logo"><figcaption>For light backgrounds</figcaption><div class="br-dl"><a class="btn btn-green" href="/brand/always-foundation-logo.png?download">Download PNG</a><a class="br-alt" href="/brand/always-foundation-logo.svg?download">SVG</a></div></figure>
    <figure class="br-logo dark"><img src="{{{{LOGO_REV}}}}" alt="Always Foundation logo on green"><figcaption>On green</figcaption><div class="br-dl"><a class="btn btn-peach" href="/brand/always-foundation-logo-on-green.png?download">Download PNG</a><a class="br-alt" href="/brand/always-foundation-logo-on-green.svg?download">SVG</a></div></figure>
  </div>
  <p class="br-fine rv">Designers: a <a href="/brand/always-foundation-logo-reverse.svg?download">light logo with no background</a> is there for placing on your own green.</p>
  <ul class="br-list rv"><li>Use the dark logo on light backgrounds, and the light one on green.</li><li>Leave space around it. Don't recolour, stretch or add effects.</li><li>Put it on a solid band, never straight on a photo.</li></ul>
</div></section>
<section class="sec pg-sec pg-sage"><div class="wrap">
  <h2 class="pg-h rv">Colour</h2>
  <p class="pg-lead rv">Deep green and warm cream, with peach for the one thing to press.</p>
  <div class="br-sws rv">
    {_swatch('Green', '#1B4740', 'The brand colour')}
    {_swatch('Cream', '#F8F3EA', 'Pages and space')}
    {_swatch('Sage', '#DDE9E0', 'Scripture and calm')}
    {_swatch('Night', '#1E2A26', 'Text and footers')}
    {_swatch('Peach', '#E8A577', 'One main button')}
    {_swatch('Orange', '#EE8B54', 'The cross only')}
    {_swatch('Clay', '#A4562A', 'Links on cream')}
  </div>
</div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">Type</h2>
  <div class="br-type rv">
    <div><p class="br-cap">Manrope, for headlines</p><p class="br-display">Every yes deserves a next step.</p></div>
    <div><p class="br-cap">Inter, for everything else</p><p class="br-body">Free for every church. Kept in Australia. Nothing shared without permission.</p></div>
    <div><p class="br-cap">Newsreader, for Scripture</p><p class="br-verse">“Lo, I am with you alway.”</p><p class="br-ref">Matthew 28:20</p></div>
  </div>
</div></section>
<section class="sec pg-sec pg-sage"><div class="wrap">
  <h2 class="pg-h rv">Voice</h2>
  <p class="pg-lead rv">Warm and plain, like a pastor at the door.</p>
  <ul class="br-list rv">
    <li>Start with people and with Jesus, never with the software.</li>
    <li>One idea at a time, in short sentences a twelve-year-old could read aloud.</li>
    <li>Say what happens. No hype, and no promises about time.</li>
    <li>Capitalise He, Him and His for God. Australian spelling.</li>
  </ul>
  <table class="doc-table br-say rv"><thead><tr><th scope="col">Say</th><th scope="col">Not</th></tr></thead><tbody>
    <tr><td>welcome, introduce, walk with</td><td>route, dispatch, funnel</td></tr>
    <tr><td>people who said yes to Jesus</td><td>leads, contacts, records</td></tr>
    <tr><td>next step</td><td>conversion</td></tr>
    <tr><td>free for every church</td><td>free tier</td></tr>
  </tbody></table>
</div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">Photos</h2>
  <ul class="br-list rv">
    <li>Real people and churches in natural light, with written permission and first names only.</li>
    <li>No identifiable children or young people under 18.</li>
    <li>Credit every photo.</li>
  </ul>
  <p class="br-more rv">Need something else, like slides or social templates? <b>hello@alwaysfoundation.org</b></p>
</div></section>'''

BRAND_CSS = """
.br-logos { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 36px; }
.br-logo { margin: 0; background: var(--paper, #FFFDF8); border-radius: 26px; padding: 48px 32px 28px; display: grid; gap: 28px; justify-items: center; }
.br-logo.dark { background: #1B4740; }
.br-logo img { width: min(280px, 80%); height: auto; }
.br-logo figcaption { font-size: 14px; color: var(--muted); margin-top: -12px; }
.br-logo.dark figcaption { color: #CFE0D6; }
.br-dl { display: flex; gap: 16px; align-items: center; }
.br-alt { font-weight: 600; color: #A4562A; min-height: 44px; display: inline-flex; align-items: center; }
.br-logo.dark .br-alt { color: #E8A577; }
.br-fine { margin-top: 16px; font-size: 15px; color: var(--muted); }
.br-fine a { color: #A4562A; }
.br-list { margin: 28px 0 0; padding-left: 20px; display: grid; gap: 8px; font-size: 18px; max-width: 62ch; }
.br-sws { display: grid; grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); gap: 16px; margin-top: 36px; }
.br-sw { display: grid; gap: 4px; background: var(--paper, #FFFDF8); border-radius: 20px; padding: 14px 14px 16px; }
.br-chip { height: 84px; border-radius: 14px; box-shadow: inset 0 0 0 1px rgba(0,0,0,.06); margin-bottom: 8px; }
.br-sw b { font: 700 16px/1.2 var(--head); color: var(--green); }
.br-sw code { font-size: 14px; color: var(--muted); background: none; padding: 0; }
.br-sw span:last-child { font-size: 14px; color: var(--soft); }
.br-type { display: grid; gap: 36px; margin-top: 36px; max-width: 900px; }
.br-cap { font-size: 14px; color: var(--muted); margin: 0 0 6px; }
.br-display { font: 800 clamp(36px, 5vw, 62px)/1.05 'Manrope', sans-serif; letter-spacing: -0.035em; color: var(--green); margin: 0; }
.br-body { font: 400 21px/1.6 'Inter', sans-serif; margin: 0; max-width: 46ch; }
.br-verse { font: 400 clamp(28px, 3.4vw, 44px)/1.3 'Newsreader', Georgia, serif; color: var(--green); margin: 0; }
.br-ref { font: 700 16px/1 var(--head); color: #A4562A; margin: 10px 0 0; }
.br-say { max-width: 620px; margin-top: 28px; }
.doc-table.br-say td, .doc-table.br-say th { text-align: left; font-weight: 400; }
.doc-table.br-say thead th, .doc-table.br-say thead th:last-child { font-weight: 700; text-align: left; }

.br-more { margin-top: 36px; color: var(--muted); }
@media (max-width: 700px) { .br-logos { grid-template-columns: 1fr; } }
"""


PLAT_BLOCKS = [
  ('Find a church', 'Verified churches near any postcode, ready to welcome.', 'Church feed'),
  ('Introduce someone', 'Pass on someone who said yes, with their permission.', 'Handoff'),
  ('Welcome them', 'Churches say yes, reach out, and keep walking with them.', 'Church inbox'),
  ('Trust', 'Know a church is verified and safe for young people.', 'Verification'),
  ('Gather', 'Christian events across Australia, in one place.', 'Events'),
  ('See the fruit', 'Show supporters what God is doing, without sharing a single name.', 'Reports'),
]

PLAT_WAYS = [
  ('Your own brand', 'Give people a next step with your name and colours on it: response pages, QR codes, event screens, and pieces for your own app.',
   '<div class="pw-art pw-phone" aria-hidden="true"><div class="pw-screen"><span class="pw-brand">Your ministry</span><b>Said yes tonight?</b><span class="pw-opt">Find a church near me</span><span class="pw-opt">Join a youth group</span><span class="pw-go">Continue</span></div></div>'),
  ('API', 'Plug Always Platform into the church and ministry tools you already use. Plain, well-documented and open.',
   '<div class="pw-art pw-code" aria-hidden="true"><span class="k">GET</span> /v1/feed/churches<br><span class="d">?postcode=2150</span><br><span class="d">&amp;welcoming=true</span></div>'),
  ('SDK', 'Ready-made pieces for websites and apps, like "Find a church near me", so you can build in minutes.',
   '<div class="pw-art pw-code" aria-hidden="true"><span class="d">$</span> npm install @always/sdk<br><br><span class="k">&lt;always-church-finder&gt;</span></div>'),
  ('AI connector', 'Ask Claude and other assistants to find a church or an event nearby. No one\'s personal details are ever involved.',
   '<div class="pw-art pw-chat" aria-hidden="true"><span class="me">Find a church near Parramatta for Sam</span><span class="ai">Hope Church is 1 km away and welcoming now.</span></div>'),
]


PRODUCTS = [
  ('Always App', 'Share Jesus, start a response point and walk with people.', '#/app',
   [('Connect', 'Church feed and Events'), ('Gather', 'Response pages and Handoff'), ('Bible', 'YouVersion Platform'), ('Walk', 'Kept in your browser')]),
  ('Always for churches', 'Accept or pass introductions, welcome people and keep walking with them.', '#/churches',
   [('Inbox', 'Handoff'), ('Your page', 'Church feed and Verification'), ('Leaders\' report', 'Reports')]),
  ('Always for ministries', 'Branded response pages, live results, funder reports and compliance.', '#/ministries',
   [('Response pages', 'Your own brand'), ('Live results', 'Handoff'), ('Funder reports', 'Reports'), ('Compliance', 'Consent records')]),
]
def _prod(name, line, href, uses):
    rows = ''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in uses)
    return f'<a class="pl-prod rv" href="{href}"><p class="pl-prod-k">Web app</p><h3>{name}</h3><p>{line}</p><ul>{rows}</ul></a>'
BUILT_ON = f'''<section class="sec pg-sec pg-sage"><div class="wrap">
  <p class="pl-kick rv">Built on Always Platform</p>
  <h2 class="pg-h rv">We build our own apps on it too.</h2>
  <p class="pg-lead rv">The Always App, and our tools for churches and ministries, are free web apps that run in any browser, with nothing to download. Each one talks to the platform through the same public API and SDK that are open to you. There's no private back door: if we can build it, so can you.</p>
  <div class="pl-prods">{''.join(_prod(*p) for p in PRODUCTS)}</div>
</div></section>'''

PLATFORM = f'''<section class="page-hero"><div class="wrap pg-split">
  <div><p class="pl-badge">Always Platform</p><h1>One platform for the Great Commission.</h1><p>Open infrastructure for the Gospel, behind the Always App and every tool we make. Use it to build your own app, plug in our API, or ask an AI assistant.</p>
  <div class="pl-ctas"><a class="btn btn-peach" href="#/docs/feed">Start building</a><a class="btn btn-ghost" href="#/join">Talk to us</a></div></div>
  <pre class="pl-code" aria-label="Example code"><code><span class="c">// Find churches welcoming people near 2150</span>
<span class="k">import</span> {{ AlwaysClient }} <span class="k">from</span> <span class="s">'@always/sdk'</span>;

<span class="k">const</span> always = <span class="k">new</span> AlwaysClient();
<span class="k">const</span> {{ items }} = <span class="k">await</span> always.feed.churches({{
  postcode: <span class="s">'2150'</span>, welcoming: <span class="k">true</span>,
}});</code></pre>
</div></section>
<section class="sec pg-sec"><div class="wrap">
  <p class="pl-kick rv">Four ways to build</p>
  <h2 class="pg-h rv">Start wherever you are.</h2>
  <div class="plat-ways pl-ways4">{''.join(f'<article class="plat-way rv">{art}<h3>{t}</h3><p>{d}</p></article>' for t, d, art in PLAT_WAYS)}</div>
</div></section>
{BUILT_ON}
<section class="sec pg-sec"><div class="wrap">
  <p class="pl-kick rv">What it does</p>
  <h2 class="pg-h rv">From the first yes to a church family.</h2>
  <div class="pl-grid">{''.join(f'<div class="pl-block rv"><span class="pl-tag">{c}</span><h3>{t}</h3><p>{d}</p></div>' for t, d, c in PLAT_BLOCKS)}</div>
</div></section>
<section class="sec pg-sec pg-sage"><div class="wrap">
  <p class="pl-kick rv">How it fits together</p>
  <h2 class="pg-h rv">Your tools, one network.</h2>
  <div class="pl-stack rv" role="list">
    <div class="pl-layer" role="listitem"><b>Web apps</b><span>The Always App, Always for churches and ministries, your own apps and websites, and AI assistants</span></div>
    <div class="pl-layer mid" role="listitem"><b>Always Platform</b><span>Find a church, introduce someone, welcome them, trust, gather, see the fruit</span></div>
    <div class="pl-layer base" role="listitem"><b>Network</b><span>Verified churches, permission that travels with people, and a care team when no one else can</span></div>
  </div>
</div></section>
<section class="sec pg-sec pg-green"><div class="wrap">
  <p class="pl-kick rv">What never changes</p>
  <h2 class="pg-h rv">A gift to the Church.</h2>
  <div class="pl-never">{''.join(f'<div class="rv"><b>{t}</b><span>{d}</span></div>' for t, d in [('Free', 'For every church, ministry and developer.'), ('Open', 'Every line is public, to check and build on.'), ('Permission first', 'Nothing about a person moves without their yes.'), ('Kept in Australia', 'People\'s details stay here.'), ('Safe for young people', 'No AI and no sharing for anyone under 18.'), ('People decide', 'AI helps with the work. People make the calls.')])}</div>
  <div class="pg-cta rv"><a class="btn btn-peach" href="#/docs/feed">Start building</a><a class="btn btn-ghost" href="#/join">Talk to us</a></div>
</div></section>'''

PLATFORM_CSS = """
.pl-prods { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px; margin-top: 48px; }
.pl-prod { display: flex; flex-direction: column; background: var(--paper); border-radius: 22px; padding: 30px 28px 26px; color: inherit; text-decoration: none; transition: transform .2s ease, box-shadow .2s ease; }
.pl-prod:hover, .pl-prod:focus-visible { transform: translateY(-3px); box-shadow: 0 18px 40px rgba(20,53,47,.10); }
.pl-prod-k { margin: 0 0 10px; font: 700 13px/1 var(--head); color: var(--clay); }
.pl-prod h3 { font-size: 23px; color: var(--green); }
.pl-prod > p:not(.pl-prod-k) { margin-top: 8px; color: var(--soft); font-size: 16px; }
.pl-prod ul { list-style: none; margin: 22px 0 0; padding: 18px 0 0; border-top: 1px solid rgba(27,71,64,.12); display: grid; gap: 10px; }
.pl-prod li { display: flex; justify-content: space-between; gap: 12px; font-size: 14.5px; }
.pl-prod li b { font: 700 14.5px/1.35 var(--head); color: var(--green); }
.pl-prod li span { color: var(--muted); text-align: right; }
.pg-built { margin-top: 36px; max-width: 64ch; font-size: 15.5px; color: var(--soft); }
.pg-built a { color: var(--clay); font-weight: 600; }
.pg-screen p.pg-url { margin: -4px auto 12px; max-width: none; line-height: 1 !important; letter-spacing: 0; width: fit-content; padding: 5px 12px; border-radius: 999px; background: #E9EFEA; font: 600 10.5px/1 var(--head) !important; color: var(--muted) !important; white-space: nowrap; }
@media (max-width: 960px) { .pl-prods { grid-template-columns: 1fr; } }

.pl-badge { display: inline-block; margin: 0 0 18px; padding: 6px 14px; border-radius: 999px; background: rgba(232,165,119,.16); color: #E8A577; font: 700 15px/1 var(--head); }
.pl-ctas { display: flex; flex-wrap: wrap; gap: 12px; margin-top: 28px; }
.pl-code { margin: 0; background: #14352F; color: #E3ECE6; border-radius: 24px; padding: 28px 30px; font: 14.5px/1.7 ui-monospace, SFMono-Regular, Menlo, monospace; overflow-x: auto; box-shadow: 0 30px 60px rgba(0,0,0,.2); }
.pl-code .c { color: #8FB5A5; } .pl-code .k { color: #E8A577; } .pl-code .s { color: #CFE0D6; }
.pl-kick { font: 700 17px/1.2 var(--head); color: #A4562A; margin: 0 0 12px; }
.pl-ways4 { margin-top: 44px; }
.pg-sec .plat-way { background: #1B4740; }
.pg-sec .plat-way .pw-art { background: #14352F; }
.pl-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px; margin-top: 44px; }
.pl-block { background: var(--paper, #FFFDF8); border-radius: 26px; padding: 28px 26px 30px; display: grid; gap: 8px; align-content: start; box-shadow: 0 1px 0 rgba(20,53,47,.04); }
.pl-tag { justify-self: start; font-size: 13px; font-weight: 600; color: #1B4740; background: #DDE9E0; padding: 4px 10px; border-radius: 999px; }
.pl-block h3 { margin: 8px 0 0; font: 800 24px/1.15 var(--head); color: var(--green); letter-spacing: -0.02em; }
.pl-block p { margin: 0; color: var(--soft); font-size: 17px; line-height: 1.55; }
.pl-stack { display: grid; gap: 12px; margin-top: 44px; max-width: 920px; }
.pl-layer { display: grid; grid-template-columns: 170px 1fr; gap: 18px; align-items: center; padding: 26px 28px; border-radius: 22px; background: var(--paper, #FFFDF8); }
.pl-layer b { font: 800 20px/1 var(--head); color: var(--green); }
.pl-layer span { color: var(--soft); font-size: 17px; }
.pl-layer.mid { background: #1B4740; box-shadow: 0 30px 60px rgba(20,53,47,.18); } .pl-layer.mid b { color: #E8A577; } .pl-layer.mid span { color: #E3ECE6; }
.pl-layer.base { background: #DDE9E0; }
.pg-green { background: #1B4740; }
.pg-green .pg-h { color: #F8F3EA; }
.pg-green .pl-kick { color: #E8A577; }
.pl-never { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 30px 40px; margin-top: 44px; }
.pl-never div { border-top: 1px solid rgba(207,224,214,.2); padding-top: 18px; }
.pl-never b { display: block; font: 800 21px/1.2 var(--head); color: #F8F3EA; margin-bottom: 6px; }
.pl-never span { color: #CFE0D6; font-size: 16.5px; line-height: 1.5; }
.pg-green .btn-ghost { color: #F8F3EA; border-color: rgba(248,243,234,.5); }
@media (max-width: 900px) { .pl-grid, .pl-never { grid-template-columns: 1fr; } .pl-layer { grid-template-columns: 1fr; gap: 6px; } }
"""
