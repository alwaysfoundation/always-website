"""Website pages: For churches, For ministries, The Always app, FAQs."""
import json
L = json.load(open('/home/claude/logo/paths.json'))
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
church_phone = phone(f'''<p class="pg-cap">Always app · Team inbox</p><div class="pg-card hl"><div class="pg-row-h"><b>Sam</b><em class="new">New</em></div><span class="pg-mut">Parramatta · Find a church</span><div class="pg-field">04•• ••• •••</div><div class="pg-btns"><span class="pg-b">Accept</span><span class="pg-b ln">Pass</span></div></div><div class="pg-card"><div class="pg-row-h"><b>Josh</b><em class="ok">Accepted</em></div><span class="pg-mut">Harris Park · Talk with someone</span></div>''')

CHURCHES = f'''<section class="page-hero"><div class="wrap"><h1>For churches</h1><p>Welcome the people near you who have said yes to Jesus and asked for a next step. Free, always.</p></div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">Three steps to welcoming people</h2>
  {steps([('Claim your page', 'Find your church in the directory and claim its page. It takes about ten minutes.'), ('Get verified', 'We check with your denomination or network, and your connect lead completes a 20-minute welcoming course.'), ('Welcome people', 'When someone nearby asks for a next step you offer, you accept or pass. Accept, and you reach out from your own phone.')])}
</div></section>
<section class="sec pg-sec pg-sage"><div class="wrap pg-split">
  <div><h2 class="pg-h rv">On the web, or in your pocket</h2><p class="pg-lead rv">Always for churches and ministries runs in any browser. The same inbox is inside the Always app, so your connect lead can accept someone from their phone on a Sunday afternoon.</p>
  <ul class="pg-list rv"><li>See who nearby has asked for a next step, and what they asked for.</li><li>Accept to see their number, or pass so the next church nearby is asked.</li><li>Log that you got in touch. The conversation stays between you.</li></ul></div>
  <div class="pg-mocks">{church_desk}<div class="pg-phone-over rv">{church_phone}</div></div>
</div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">What your church gets</h2>
  {feats([('Your page on the map', 'Your welcome, service times, what to expect, and the next steps you offer, in your colours.'), ('Introductions near you', 'People who have already said yes to Jesus, within the area you choose.'), ('Next steps and capacity', 'Choose what you offer and how many people you can welcome each month. Pause any time.'), ('Your team', 'Invite your pastor, connect lead and youth leaders, each with the right access.'), ('Walking with', 'Keep track of everyone you are welcoming, and see when they tell us they are connected.'), ('Your own tools', 'Use the free inbox, or connect your church management system through the API.')])}
  <div class="pg-cta rv"><a class="btn btn-peach" href="#/directory">Find your church</a><a class="btn btn-green" href="#/docs/claim">How claiming works</a></div>
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

MINISTRIES = f'''<section class="page-hero"><div class="wrap"><h1>For ministries</h1><p>Tours, camps, youth events, campus and street outreach, and media ministries: give everyone who responds a next step near where they live.</p></div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">From the altar call to a church family</h2>
  {steps([('Create a response page', 'Choose the next steps you offer and add your brand. Ready in minutes.'), ('Invite a response', 'Show the QR code on the big screen, hand out cards, or use the response card in your own app.'), ('See the fruit', 'Watch results live: who responded, who was introduced to a church nearby, and who is connected.')])}
</div></section>
<section class="sec pg-sec pg-night"><div class="wrap pg-split">
  <div><h2 class="pg-h rv">Your brand. Live results.</h2><p class="pg-lead rv">People respond on a page that looks and sounds like you. Your team sees totals as they happen, and each person's details go only to the church that welcomes them.</p>
  <ul class="pg-list rv"><li>Results for every event, tour and campus.</li><li>An inbox for the steps you offer yourself, like a youth night or a course.</li><li>Street teams and evangelists use the Always app to show their own QR.</li></ul></div>
  <div class="pg-mocks">{ministry_desk}<div class="pg-phone-over rv">{ministry_phone}</div></div>
</div></section>
<section class="sec pg-sec pg-sage"><div class="wrap pg-split">
  <div><h2 class="pg-h rv">Responses online, too</h2><p class="pg-lead rv">Sharing a testimony video, a sermon or a post? Add a response link or QR in the description, or embed the response card on your website. People anywhere in Australia can say yes and be introduced to a church near them.</p></div>
  <pre class="pg-code rv"><code>&lt;always-response
  page="testimony-video"&gt;
&lt;/always-response&gt;

or link to
always.au/r/testimony-video</code></pre>
</div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">Built for events of every size</h2>
  {feats([('Response pages and QR codes', 'For the big screen, printed cards, video descriptions and short links.'), ('Leading the moment', 'Simple wording for the altar call: invite, pray, respond, welcome.'), ('Your team', 'Response team leads, evangelists and youth leaders, each with the right access.'), ('Safe for young people', 'Young people are introduced only to verified youth partners. Under 15s need a parent to confirm.'), ('Australia-wide', 'People are introduced to a church near where they live, anywhere in Australia.'), ('Open API and SDK', 'Add the response card to your own app or website.')])}
  <div class="pg-cta rv"><a class="btn btn-peach" href="#/join">Book a catch-up call</a><a class="btn btn-green" href="#/docs/senders">Read the guide</a></div>
</div></section>'''

app_home = phone('<p class="pg-serif">Who will you walk with today?</p><div class="pg-verse"><p>“For the Son of man is come to seek and to save that which was lost.”</p><span>Luke 19:10</span></div><p class="pg-small"><b>Pray for Sam, Priya and Josh</b></p><div class="pg-b pe">Start a response point</div>')
def mini(title, inner): return f'<div class="pg-mini rv"><div class="pg-mini-ph">{phone(inner)}</div><h3>{title}</h3></div>'
APP = f'''<section class="page-hero"><div class="wrap pg-split">
  <div><h1>The Always app</h1><p>Every Christian can be someone's next step. A free app to understand the gospel, share it, and walk with people into a church family.</p><a class="btn btn-peach" href="#/join" style="margin-top:28px">Join the pilot</a></div>
  <div class="pg-hero-ph">{app_home}</div>
</div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">Everything you need to share Jesus</h2>
  <div class="pg-minis">
    {mini('Bible', '<p class="pg-cap">John 3 · KJV</p><span class="pg-big">3</span><p class="pg-read"><sup>16</sup> <mark>For God so loved the world, that he gave his only begotten Son…</mark></p>')}
    {mini('Learn', '<p class="pg-cap">The Always path</p>' + ''.join(f'<div class="pg-path"><i class="s{i}"></i><b>0{i+1} / {s}</b></div>' for i, s in enumerate(['Understand', 'Live', 'Share', 'Walk'])))}
    {mini('Gather', '<p class="pg-serif sm">Someone said yes to Jesus. Give them a next step.</p><div class="pg-tile">Show a QR code</div><div class="pg-card">Connect someone now</div>')}
    {mini('Walk', '<p class="pg-cap">Walking with Sam</p>' + ''.join(f'<div class="pg-tick{" done" if d else ""}"><i></i>{t}</div>' for t, d in [('Send a welcome message', 1), ('Share John 3', 1), ('Coffee this week', 0), ('Church together', 0)]))}
    {mini('Connect', '<p class="pg-cap">Near you</p><div class="pg-mapbox"></div><div class="pg-card">Hope Church Parramatta</div><div class="pg-card">City worship night · Fri</div>')}
  </div>
</div></section>
<section class="sec pg-sec pg-sage"><div class="wrap">
  <h2 class="pg-h rv">Made for evangelists, and for everyone</h2>
  {feats([('A beautiful Bible', 'KJV and WEB built in, more through YouVersion. Highlight, share verses as images, listen with soft music and a sleep timer.'), ('Conversation guides', 'How to share with someone with no faith, a Muslim friend, a Jehovah\'s Witness, a Buddhist and more.'), ('Altar calls and the street', 'Start a response point in seconds, coach the moment, and connect people with their yes.'), ('Prayer list and field notes', 'Pray for people by name. Talk through a conversation and it\'s turned into notes on your phone, offline. The audio never leaves it.'), ('Church team inbox', 'Connect leads accept introductions right in the app.'), ('Private by design', 'Your prayer list, notes and plans stay on your phone. No ads.')])}
  <div class="pg-cta rv"><a class="btn btn-peach" href="#/join">Join the pilot</a></div>
</div></section>'''

FAQ_GROUPS = [
 ('About Always', [
  ('What is Always?', 'A shared network that connects everyone who responds to Jesus in Australia with their next best faith step, usually a local church near where they live.'),
  ('Who runs it?', 'The Always Foundation, a members-based not-for-profit being established in Australia. Churches and ministries that affirm the Nicene Creed are its members.'),
  ('Is it only for one denomination?', 'No. Evangelical and Pentecostal churches and ministries across denominations and networks take part, on the common ground of the Nicene Creed.'),
  ('Is Always only in Australia?', 'Our focus is Australia. The technology is open source, so churches and ministries in other countries are welcome to use it.'),
  ('How do I sign in?', 'With one Always account, using Apple, Google, YouVersion or your email. The same account works in the Always app and on the web.')]),
 ('For churches', [
  ('Does it cost anything?', 'No. Always is free for every church.'),
  ('How do we join?', 'Find your church in the directory, claim its page, and we verify you with your denomination or network.'),
  ('What if we can\'t welcome someone?', 'Pass, with a reason. The next church or ministry nearby is asked. If none can, our care team helps.'),
  ('Do we have to change our church software?', 'No. Use the free inbox on the web or in the Always app, or connect your system through the API.'),
  ('Who on our team can see people\'s details?', 'Only the people you add to your team, and only after your church accepts an introduction.')]),
 ('For ministries and events', [
  ('Can we use our own brand?', 'Yes. Response pages, QR codes and texts can use your colours, logo and wording.'),
  ('What results do we see?', 'Totals for each event: responded, introduced, accepted and connected. Each person\'s details go only to the church that welcomes them.'),
  ('Can we receive introductions ourselves?', 'Yes, for the steps you offer, like a youth night or a course.'),
  ('Can people respond online?', 'Yes. Add a response link or QR to a video description or post, or embed the response card on your website. An invisible check stops spam without puzzles.'),
  ('Can we list our events?', 'Yes. Add them from Always for churches and ministries, and they show on our Events page and in the Always app.'),
  ('How do evangelists and street teams use it?', 'With the Always app: they start a response point, show their own QR, or connect someone in a conversation with their yes.')]),
 ('For people who respond', [
  ('What happens when I respond?', 'You choose a next step, see who will be in touch, and a church or ministry near you reaches out.'),
  ('What do you need from me?', 'Your first name, a mobile number and your suburb.'),
  ('Do I need to download an app?', 'No. You respond on a simple web page. Later, you\'re welcome to try the Always app to read the Bible and grow.'),
  ('Can I change my mind?', 'Yes, any time, from the link in your text. Your details are then deleted.'),
  ('I\'m under 18. Can I still respond?', 'Yes. Under 15s need a parent or guardian to confirm, and young people are introduced only to verified youth partners.')]),
 ('The Always app', [
  ('Who is the app for?', 'Every Christian who wants to share Jesus and walk with people, and church teams who welcome them.'),
  ('How do I get it?', 'The app is in pilot. Join the pilot through the form on our home page.'),
  ('Which Bible translations are included?', 'The King James Version and the World English Bible, with more through YouVersion.'),
  ('Where are my notes and prayer list kept?', 'On your phone. Voice notes are turned into text on your phone too, using NVIDIA Parakeet, an open speech model. The audio never leaves your phone.')]),
 ('Privacy and safety', [
  ('Where is information kept?', 'In Australia, encrypted, under Australian privacy law.'),
  ('Do you sell information or use it for advertising?', 'No.'),
  ('How do you use AI?', 'To save people time, like turning a voice note into text on your own phone with NVIDIA Parakeet, an open model that works offline. Every welcome comes from a real person, and young people\'s information is kept out of AI entirely.'),
  ('How do I report a concern?', 'Email safeguarding@alwaysfoundation.org for safeguarding, privacy@ for privacy and security@ for security.')]),
 ('Supporters and builders', [
  ('How is Always funded?', 'By supporters, and by larger ministries contributing to upkeep according to their size. Churches never pay.'),
  ('How can I support the work?', 'Pray with us, and get in touch at hello@alwaysfoundation.org to book a catch-up call.'),
  ('Can developers build on Always?', 'Yes. The API, SDK and open standard are open source under Apache 2.0, with docs under CC BY 4.0.')])]

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
    <div class="cl-org" id="cl-org"><p class="pg-cap">Your church</p><h2 id="cl-name">Choose your church</h2><p id="cl-where" class="pg-mut"></p></div>
    <form class="cl-form" id="claim-form" novalidate>
      <label>Search for your church<input id="cl-q" type="search" placeholder="Church name or suburb" autocomplete="off"></label>
      <div id="cl-results" class="cl-results"></div>
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
    <p class="pg-mut">Can't find your church? <a href="#/feedback/missing">Tell us about it</a>.</p>
  </aside>
</div></section>'''
FEEDBACK = '''<section class="page-hero"><div class="wrap"><h1>Ideas and problems</h1><p>Help us make Always better. Share an idea, report something that isn't working, or tell us about a church we've missed.</p></div></section>
<section class="sec pg-sec"><div class="wrap cl-grid">
  <form class="cl-form" id="fb-form" novalidate>
    <div class="fb-kinds" role="radiogroup" aria-label="What would you like to share?">
      <label class="fb-kind"><input type="radio" name="kind" value="idea" checked><span><b>An idea</b>Something that would help</span></label>
      <label class="fb-kind"><input type="radio" name="kind" value="bug"><span><b>A problem</b>Something isn't working</span></label>
      <label class="fb-kind"><input type="radio" name="kind" value="missing"><span><b>A missing church</b>Add a church or ministry</span></label>
    </div>
    <label>Where<select name="area"><option>The website</option><option>The Always app</option><option>Always for churches and ministries</option><option>A response page</option><option>The directory</option><option>Somewhere else</option></select></label>
    <label id="fb-msg-l">Tell us more<textarea name="message" rows="6" required></textarea></label>
    <label>Your email <span>Optional, if you'd like a reply</span><input name="email" type="email" autocomplete="email"></label>
    <button class="btn btn-green" type="submit">Send</button>
    <p class="cl-status" id="fb-status" role="status" aria-live="polite"></p>
    <div class="cl-done" id="fb-done" hidden><h2>Thank you.</h2><p>We read every message. If you left your email, we'll be in touch.</p></div>
  </form>
  <aside class="cl-side">
    <h3>For developers</h3>
    <p class="pg-mut">Always is open source. You can also open an issue or suggest a change on GitHub.</p>
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
