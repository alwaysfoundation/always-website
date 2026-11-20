"""Website pages: For churches, For ministries, Always Sent, FAQs."""
import json
import products as PR
from mocks import mock
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
church_phone = phone(f'''<p class="pg-cap">Always Connect · Inbox</p><div class="pg-card hl"><div class="pg-row-h"><b>Sam</b><em class="new">New</em></div><span class="pg-mut">Parramatta · Find a church</span><div class="pg-field">04•• ••• •••</div><div class="pg-btns"><span class="pg-b">Accept</span><span class="pg-b ln">Pass</span></div></div><div class="pg-card"><div class="pg-row-h"><b>Josh</b><em class="ok">Accepted</em></div><span class="pg-mut">Harris Park · Talk with someone</span></div>''')

CHURCHES = f'''<section class="page-hero pd-hero"><div class="wrap pd-split"><div><p class="pl-kick">Solutions</p><h1>For churches</h1><p>Welcome people near you who have said yes to Jesus, and help them grow as disciples. Free, always.</p><div class="pg-cta"><a class="btn btn-peach" href="#/join/church">Join as a church</a></div></div>{mock('connect', 'mk-lg')}</div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">Three steps to welcoming people</h2>
  {steps([('Partner with Always', 'Register your church and tell us who you are. It takes a few minutes.'), ('Get ready at your pace', 'We check with your denomination or network, and your connect lead does a 20-minute course. Then you\'re a partner church.'), ('Welcome people', 'When someone nearby asks for a next step you offer, accept or pass. Then call or text from your own phone.')])}
</div></section>
<section class="sec pg-sec pg-sage"><div class="wrap pg-split">
  <div><h2 class="pg-h rv">Always Connect, in any browser</h2><p class="pg-lead rv">A free web app for your team. Nothing to install, so your connect lead can say yes from their phone on a Sunday.</p>
  <ul class="pg-list rv"><li>See who nearby has asked for a next step, and what they asked for.</li><li>Accept to see their number, or pass so the next church nearby is asked.</li><li>Log that you got in touch. The conversation stays between you.</li></ul></div>
  <div class="pg-mocks">{church_desk}<div class="pg-phone-over rv">{church_phone}</div></div>
</div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">What your church gets</h2>
  {feats([('Your page on the map', 'Your welcome, service times, what to expect, and the next steps you offer, in your colours.'), ('Introductions near you', 'People who have already said yes to Jesus, within the area you choose.'), ('Next steps and capacity', 'Choose what you offer and how many people you can welcome each month. Pause any time.'), ('Your team', 'Invite your pastor, connect lead and youth leaders, each with the right access.'), ('Walking with', 'Keep track of everyone you are welcoming, and get a simple monthly report for your leaders.'), ('Your own tools', 'Use the free inbox, or connect your church management system through the API.')])}
  <div class="pg-cta rv"><a class="btn btn-peach" href="#/join/church">Join as a church</a><a class="btn btn-green" href="#/docs/joining">How joining works</a></div>
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

MINISTRIES = f'''<section class="page-hero pd-hero"><div class="wrap pd-split"><div><p class="pl-kick">Solutions</p><h1>For ministries</h1><p>Events, tours, camps, evangelists and street teams: free tools to share the Gospel, less administration, and a next step near home for everyone who responds.</p><div class="pg-cta"><a class="btn btn-peach" href="#/join">Partner with Always</a></div></div>{mock('pages', 'mk-lg')}</div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">From the altar call to a church family</h2>
  {steps([('Create a response page', 'Choose the next steps you offer and add your brand. Ready in minutes.'), ('Invite a response', 'Show the QR code on the big screen, hand out cards, or use the response card in your own app.'), ('See the fruit', 'Watch results live, and get a monthly report ready for your funders and board.')])}
</div></section>
<section class="sec pg-sec pg-night"><div class="wrap pg-split">
  <div><h2 class="pg-h rv">Your brand. Live results.</h2><p class="pg-lead rv">People respond on a page that looks like you. Your team sees totals live, and each person's details go only to the church that welcomes them.</p>
  <ul class="pg-list rv"><li>Results for every event, tour and campus.</li><li>An inbox for the steps you offer yourself, like a youth night or a course.</li><li>Street teams and evangelists use Always Sent to show their own QR.</li></ul></div>
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
  <p class="pg-lead rv">Shared tools for the everyday work behind every ministry, with agents to help with follow-up and admin, so your team can spend more time on people.</p>
  {feats([('Governance', 'Shared policies, templates and partner records for boards and leaders.'), ('Consent and privacy', 'Consent records and privacy requests, ready to export when you need them.'), ('Safeguarding', 'Child safety checklists and Working With Children Check reminders, kept in one place.'), ('Reporting', 'A monthly report for your board and funders, with totals only.')])}
  <div class="pg-cta rv"><a class="btn btn-peach" href="#/compliance/check">Try the free safety check-up</a><a class="btn btn-ghost" href="#/compliance">About Always Safety</a></div>
</div></section>
<section class="sec pg-sec pg-sage"><div class="wrap pg-split">
  <div><h2 class="pg-h rv">Responses online, too</h2><p class="pg-lead rv">Sharing a testimony, sermon or post? Add a response link or QR code. Anyone in Australia can say yes and meet a church near them.</p></div>
  <div class="pg-link-card rv" aria-hidden="true"><span class="plc-k">Your response link</span><b>always.au/r/testimony</b><span class="plc-qr"></span><span class="plc-f">Add it under a video, in a post, or as a QR code on screen.</span></div>
</div></section>
<section class="sec pg-sec"><div class="wrap sl-end">
  <h2 class="pg-h rv">Planning an event or a tour?</h2>
  <p class="pg-lead rv">We'd love to hear about it, and help everyone who responds find a next step near home.</p>
  <div class="pg-cta rv"><a class="btn btn-peach" href="#/contact">Book a catch-up call</a><a class="btn btn-green" href="#/docs/senders">Read the guide</a></div>
</div></section>'''

app_home = phone('<p class="pg-url">Always Sent · in your browser</p><p class="pg-serif">Who will you walk with today?</p><div class="pg-verse"><p>“For the Son of Man came to seek and to save the lost.”</p><span>Luke 19:10 (ESV)</span></div><p class="pg-small"><b>Pray for Sam, Priya and Josh</b></p><div class="pg-b pe">Start a response point</div>')
def mini(title, inner): return f'<div class="pg-mini rv"><div class="pg-mini-ph">{phone(inner)}</div><h3>{title}</h3></div>'
import os as _os
from PIL import Image as _Img
def _shot(name):
    src = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'img', 'app', name + '.png')
    out_dir = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'img')
    im = _Img.open(src).convert('RGB'); im = im.resize((520, round(im.height * 520 / im.width)), _Img.LANCZOS)
    im.save(_os.path.join(out_dir, 'app-' + name + '.webp'), 'WEBP', quality=80, method=6)
    return 'img/app-' + name + '.webp'
def ph(name, alt, cls=''):
    return f'<figure class="ap-ph {cls}"><img src="{_shot(name)}" alt="{alt}" loading="lazy" width="390" height="844"></figure>'
AP_QR = """<svg class="ap-qr-svg" role="img" aria-label="QR code for app.alwaysfoundation.org" viewBox="0 0 33 33" xmlns="http://www.w3.org/2000/svg"><rect width="33" height="33" fill="#fff"/><path d="M2 2h1v1h-1zM3 2h1v1h-1zM4 2h1v1h-1zM5 2h1v1h-1zM6 2h1v1h-1zM7 2h1v1h-1zM8 2h1v1h-1zM10 2h1v1h-1zM11 2h1v1h-1zM13 2h1v1h-1zM17 2h1v1h-1zM18 2h1v1h-1zM19 2h1v1h-1zM20 2h1v1h-1zM24 2h1v1h-1zM25 2h1v1h-1zM26 2h1v1h-1zM27 2h1v1h-1zM28 2h1v1h-1zM29 2h1v1h-1zM30 2h1v1h-1zM2 3h1v1h-1zM8 3h1v1h-1zM10 3h1v1h-1zM12 3h1v1h-1zM18 3h1v1h-1zM21 3h1v1h-1zM22 3h1v1h-1zM24 3h1v1h-1zM30 3h1v1h-1zM2 4h1v1h-1zM4 4h1v1h-1zM5 4h1v1h-1zM6 4h1v1h-1zM8 4h1v1h-1zM10 4h1v1h-1zM11 4h1v1h-1zM14 4h1v1h-1zM17 4h1v1h-1zM18 4h1v1h-1zM20 4h1v1h-1zM22 4h1v1h-1zM24 4h1v1h-1zM26 4h1v1h-1zM27 4h1v1h-1zM28 4h1v1h-1zM30 4h1v1h-1zM2 5h1v1h-1zM4 5h1v1h-1zM5 5h1v1h-1zM6 5h1v1h-1zM8 5h1v1h-1zM11 5h1v1h-1zM13 5h1v1h-1zM14 5h1v1h-1zM18 5h1v1h-1zM19 5h1v1h-1zM21 5h1v1h-1zM22 5h1v1h-1zM24 5h1v1h-1zM26 5h1v1h-1zM27 5h1v1h-1zM28 5h1v1h-1zM30 5h1v1h-1zM2 6h1v1h-1zM4 6h1v1h-1zM5 6h1v1h-1zM6 6h1v1h-1zM8 6h1v1h-1zM10 6h1v1h-1zM11 6h1v1h-1zM12 6h1v1h-1zM16 6h1v1h-1zM17 6h1v1h-1zM18 6h1v1h-1zM19 6h1v1h-1zM20 6h1v1h-1zM21 6h1v1h-1zM24 6h1v1h-1zM26 6h1v1h-1zM27 6h1v1h-1zM28 6h1v1h-1zM30 6h1v1h-1zM2 7h1v1h-1zM8 7h1v1h-1zM11 7h1v1h-1zM12 7h1v1h-1zM14 7h1v1h-1zM17 7h1v1h-1zM18 7h1v1h-1zM19 7h1v1h-1zM20 7h1v1h-1zM22 7h1v1h-1zM24 7h1v1h-1zM30 7h1v1h-1zM2 8h1v1h-1zM3 8h1v1h-1zM4 8h1v1h-1zM5 8h1v1h-1zM6 8h1v1h-1zM7 8h1v1h-1zM8 8h1v1h-1zM10 8h1v1h-1zM12 8h1v1h-1zM14 8h1v1h-1zM16 8h1v1h-1zM18 8h1v1h-1zM20 8h1v1h-1zM22 8h1v1h-1zM24 8h1v1h-1zM25 8h1v1h-1zM26 8h1v1h-1zM27 8h1v1h-1zM28 8h1v1h-1zM29 8h1v1h-1zM30 8h1v1h-1zM11 9h1v1h-1zM13 9h1v1h-1zM15 9h1v1h-1zM17 9h1v1h-1zM18 9h1v1h-1zM21 9h1v1h-1zM2 10h1v1h-1zM5 10h1v1h-1zM6 10h1v1h-1zM7 10h1v1h-1zM8 10h1v1h-1zM9 10h1v1h-1zM10 10h1v1h-1zM12 10h1v1h-1zM13 10h1v1h-1zM15 10h1v1h-1zM19 10h1v1h-1zM21 10h1v1h-1zM22 10h1v1h-1zM23 10h1v1h-1zM26 10h1v1h-1zM28 10h1v1h-1zM29 10h1v1h-1zM30 10h1v1h-1zM2 11h1v1h-1zM3 11h1v1h-1zM7 11h1v1h-1zM9 11h1v1h-1zM14 11h1v1h-1zM15 11h1v1h-1zM18 11h1v1h-1zM21 11h1v1h-1zM25 11h1v1h-1zM26 11h1v1h-1zM28 11h1v1h-1zM29 11h1v1h-1zM5 12h1v1h-1zM8 12h1v1h-1zM9 12h1v1h-1zM10 12h1v1h-1zM15 12h1v1h-1zM17 12h1v1h-1zM18 12h1v1h-1zM19 12h1v1h-1zM23 12h1v1h-1zM25 12h1v1h-1zM28 12h1v1h-1zM2 13h1v1h-1zM4 13h1v1h-1zM5 13h1v1h-1zM10 13h1v1h-1zM11 13h1v1h-1zM14 13h1v1h-1zM15 13h1v1h-1zM18 13h1v1h-1zM19 13h1v1h-1zM20 13h1v1h-1zM21 13h1v1h-1zM22 13h1v1h-1zM23 13h1v1h-1zM24 13h1v1h-1zM27 13h1v1h-1zM30 13h1v1h-1zM4 14h1v1h-1zM5 14h1v1h-1zM6 14h1v1h-1zM8 14h1v1h-1zM9 14h1v1h-1zM10 14h1v1h-1zM12 14h1v1h-1zM13 14h1v1h-1zM14 14h1v1h-1zM15 14h1v1h-1zM17 14h1v1h-1zM18 14h1v1h-1zM22 14h1v1h-1zM24 14h1v1h-1zM25 14h1v1h-1zM30 14h1v1h-1zM6 15h1v1h-1zM12 15h1v1h-1zM13 15h1v1h-1zM15 15h1v1h-1zM16 15h1v1h-1zM18 15h1v1h-1zM19 15h1v1h-1zM20 15h1v1h-1zM24 15h1v1h-1zM26 15h1v1h-1zM27 15h1v1h-1zM28 15h1v1h-1zM29 15h1v1h-1zM30 15h1v1h-1zM4 16h1v1h-1zM5 16h1v1h-1zM6 16h1v1h-1zM7 16h1v1h-1zM8 16h1v1h-1zM10 16h1v1h-1zM12 16h1v1h-1zM14 16h1v1h-1zM15 16h1v1h-1zM18 16h1v1h-1zM20 16h1v1h-1zM21 16h1v1h-1zM26 16h1v1h-1zM28 16h1v1h-1zM30 16h1v1h-1zM3 17h1v1h-1zM6 17h1v1h-1zM7 17h1v1h-1zM9 17h1v1h-1zM10 17h1v1h-1zM12 17h1v1h-1zM13 17h1v1h-1zM14 17h1v1h-1zM17 17h1v1h-1zM21 17h1v1h-1zM24 17h1v1h-1zM26 17h1v1h-1zM28 17h1v1h-1zM30 17h1v1h-1zM2 18h1v1h-1zM4 18h1v1h-1zM5 18h1v1h-1zM6 18h1v1h-1zM8 18h1v1h-1zM9 18h1v1h-1zM11 18h1v1h-1zM16 18h1v1h-1zM22 18h1v1h-1zM27 18h1v1h-1zM2 19h1v1h-1zM7 19h1v1h-1zM11 19h1v1h-1zM14 19h1v1h-1zM15 19h1v1h-1zM16 19h1v1h-1zM18 19h1v1h-1zM20 19h1v1h-1zM21 19h1v1h-1zM22 19h1v1h-1zM23 19h1v1h-1zM26 19h1v1h-1zM28 19h1v1h-1zM29 19h1v1h-1zM2 20h1v1h-1zM3 20h1v1h-1zM8 20h1v1h-1zM9 20h1v1h-1zM10 20h1v1h-1zM11 20h1v1h-1zM14 20h1v1h-1zM17 20h1v1h-1zM21 20h1v1h-1zM24 20h1v1h-1zM25 20h1v1h-1zM26 20h1v1h-1zM27 20h1v1h-1zM30 20h1v1h-1zM2 21h1v1h-1zM3 21h1v1h-1zM5 21h1v1h-1zM9 21h1v1h-1zM11 21h1v1h-1zM12 21h1v1h-1zM13 21h1v1h-1zM16 21h1v1h-1zM17 21h1v1h-1zM18 21h1v1h-1zM22 21h1v1h-1zM23 21h1v1h-1zM24 21h1v1h-1zM26 21h1v1h-1zM27 21h1v1h-1zM28 21h1v1h-1zM2 22h1v1h-1zM3 22h1v1h-1zM5 22h1v1h-1zM6 22h1v1h-1zM8 22h1v1h-1zM11 22h1v1h-1zM12 22h1v1h-1zM14 22h1v1h-1zM15 22h1v1h-1zM16 22h1v1h-1zM17 22h1v1h-1zM18 22h1v1h-1zM19 22h1v1h-1zM21 22h1v1h-1zM22 22h1v1h-1zM23 22h1v1h-1zM24 22h1v1h-1zM25 22h1v1h-1zM26 22h1v1h-1zM27 22h1v1h-1zM28 22h1v1h-1zM29 22h1v1h-1zM10 23h1v1h-1zM12 23h1v1h-1zM14 23h1v1h-1zM16 23h1v1h-1zM17 23h1v1h-1zM19 23h1v1h-1zM20 23h1v1h-1zM21 23h1v1h-1zM22 23h1v1h-1zM26 23h1v1h-1zM27 23h1v1h-1zM2 24h1v1h-1zM3 24h1v1h-1zM4 24h1v1h-1zM5 24h1v1h-1zM6 24h1v1h-1zM7 24h1v1h-1zM8 24h1v1h-1zM10 24h1v1h-1zM11 24h1v1h-1zM12 24h1v1h-1zM13 24h1v1h-1zM14 24h1v1h-1zM16 24h1v1h-1zM17 24h1v1h-1zM21 24h1v1h-1zM22 24h1v1h-1zM24 24h1v1h-1zM26 24h1v1h-1zM27 24h1v1h-1zM2 25h1v1h-1zM8 25h1v1h-1zM10 25h1v1h-1zM14 25h1v1h-1zM16 25h1v1h-1zM17 25h1v1h-1zM18 25h1v1h-1zM19 25h1v1h-1zM20 25h1v1h-1zM21 25h1v1h-1zM22 25h1v1h-1zM26 25h1v1h-1zM30 25h1v1h-1zM2 26h1v1h-1zM4 26h1v1h-1zM5 26h1v1h-1zM6 26h1v1h-1zM8 26h1v1h-1zM10 26h1v1h-1zM14 26h1v1h-1zM15 26h1v1h-1zM16 26h1v1h-1zM17 26h1v1h-1zM20 26h1v1h-1zM21 26h1v1h-1zM22 26h1v1h-1zM23 26h1v1h-1zM24 26h1v1h-1zM25 26h1v1h-1zM26 26h1v1h-1zM27 26h1v1h-1zM29 26h1v1h-1zM30 26h1v1h-1zM2 27h1v1h-1zM4 27h1v1h-1zM5 27h1v1h-1zM6 27h1v1h-1zM8 27h1v1h-1zM10 27h1v1h-1zM13 27h1v1h-1zM14 27h1v1h-1zM17 27h1v1h-1zM18 27h1v1h-1zM19 27h1v1h-1zM20 27h1v1h-1zM22 27h1v1h-1zM23 27h1v1h-1zM25 27h1v1h-1zM30 27h1v1h-1zM2 28h1v1h-1zM4 28h1v1h-1zM5 28h1v1h-1zM6 28h1v1h-1zM8 28h1v1h-1zM11 28h1v1h-1zM12 28h1v1h-1zM13 28h1v1h-1zM14 28h1v1h-1zM17 28h1v1h-1zM19 28h1v1h-1zM21 28h1v1h-1zM22 28h1v1h-1zM23 28h1v1h-1zM25 28h1v1h-1zM26 28h1v1h-1zM28 28h1v1h-1zM29 28h1v1h-1zM30 28h1v1h-1zM2 29h1v1h-1zM8 29h1v1h-1zM13 29h1v1h-1zM15 29h1v1h-1zM17 29h1v1h-1zM20 29h1v1h-1zM21 29h1v1h-1zM24 29h1v1h-1zM25 29h1v1h-1zM26 29h1v1h-1zM27 29h1v1h-1zM28 29h1v1h-1zM30 29h1v1h-1zM2 30h1v1h-1zM3 30h1v1h-1zM4 30h1v1h-1zM5 30h1v1h-1zM6 30h1v1h-1zM7 30h1v1h-1zM8 30h1v1h-1zM10 30h1v1h-1zM16 30h1v1h-1zM21 30h1v1h-1zM22 30h1v1h-1zM25 30h1v1h-1zM26 30h1v1h-1z" fill="#14352F"/></svg>"""
STEPS_APP = [
    ('Before', 'Ready for any conversation', 'Sent 30, a 30-day plan for everyday evangelists, guides for friends of every background, and well-loved training from partners and ministries worldwide.', 'learn', 'The Learn screen of Always Sent'),
    ('During', 'God&rsquo;s story, in their language', 'Created, broken, rescued, restored. Four moments you can share in a few minutes, in seven languages spoken across Australia.', 'story-zh', 'God&rsquo;s story in Simplified Chinese'),
    ('The yes', 'A next step, right there', 'Show a QR code or hand them your phone. With their consent, a church near home is introduced to welcome them.', 'gather', 'The Gather screen with a QR code'),
    ('After', 'Walk with them', 'Gentle steps over their first month, a Today card on your home screen, and reminders in your own calendar.', 'walk', 'Walking with Sam, with steps for the month'),
]
APP = f'''<section class="page-hero ap-hero"><div class="wrap ap-hero-in">
  <div class="ap-copy">{PR.mod_icon("app", "mi-lg")}<p class="pl-kick">Always Sent</p>
  <h1>Share Jesus.<br>Tell your story.</h1>
  <p>Be equipped to share Jesus, tell your story and help someone take their next step. A free evangelism companion for every Christian, with nothing to download.</p>
  <div class="pg-cta"><a class="btn btn-peach" href="https://app.alwaysfoundation.org">Open Always Sent</a><a class="btn btn-ghost" href="#/docs/app">How it works</a></div>
  <div class="ap-qr"><span>{AP_QR}</span><p>On a computer? Scan to open it on your phone.</p></div></div>
  <div class="ap-stage" aria-hidden="true">{ph('splash', '', 'ap-l')}{ph('home-dark', '', 'ap-c')}{ph('card', '', 'ap-r')}</div>
</div></section>
<section class="sec pg-sec ap-journey"><div class="wrap">
  <h2 class="pg-h rv">From hello to home.</h2>
  <p class="pg-lead rv">One app for the whole conversation, from the first hello to a church family.</p>
  <ol class="ap-steps">{''.join(f'<li class="rv"><div class="ap-step-ph">{ph(img, alt)}</div><p class="ap-n"><span>{i}</span>{k}</p><h3>{t}</h3><p>{d}</p></li>' for i, (k, t, d, img, alt) in enumerate(STEPS_APP, 1))}</ol>
</div></section>
<section class="sec pg-sec ap-rows"><div class="wrap">
  <div class="ap-row rv"><div class="ap-row-art">{ph('testimony', 'A 30-second testimony, ready to share')}</div>
    <div class="ap-row-tx"><h2>Tell your story.</h2><p>Three prompts help you put into words what Jesus has done in your life: before, meeting Jesus, and since. Then shape a 30-second version for everyday conversations, practise it, and send it or turn it into a card when the moment comes. It stays on your phone and is never posted for you.</p></div></div>
  <div class="ap-row ap-flip rv"><div class="ap-row-art ap-duo">{ph('bible', 'The Bible in light mode')}{ph('bible-dark', 'The Bible in dark mode')}</div>
    <div class="ap-row-tx"><h2>A Bible that feels like home.</h2><p>Read, highlight, bookmark and listen, with notes kept on your phone. Dark by default, easy on the eyes at night, or choose Light or Warm. Set a daily reminder to pray for the people on your list.</p></div></div>
  <div class="ap-row rv"><div class="ap-row-art">{ph('card', 'Sharing the verse of the day as a card')}</div>
    <div class="ap-row-tx"><h2>Share the verse of the day.</h2><p>One tap turns today&rsquo;s verse, or any verse, into a beautiful card. Choose from eight backgrounds, four fonts and three shapes for posts, messages and stories. It&rsquo;s made on your phone and nothing is uploaded.</p></div></div>
  <div class="ap-row ap-flip rv"><div class="ap-row-art">{ph('invite', 'Inviting a friend to church')}</div>
    <div class="ap-row-tx"><h2>Invite a friend to church.</h2><p>Many people visit a church for the first time because a friend asked. Choose what to invite them to, and the app writes a warm, personal message to send by text, with an invitation card to match. Need a church to invite them to? Find one near any postcode, right in the app. Your friend joins your prayer list so you can keep walking with them.</p></div></div>
  <div class="ap-row rv"><div class="ap-row-art">{ph('sent', 'Day 3 of the Sent plan')}</div>
    <div class="ap-row-tx"><h2>Sent 30: a month of small steps.</h2><p>Each day has a reading, a verse to keep and one small step of faith, from praying for three people by name to inviting a friend to church. Turn the day&rsquo;s verse into a card in one tap.</p></div></div>
  <div class="ap-row ap-flip rv"><div class="ap-row-art">{ph('library', 'The training library')}</div>
    <div class="ap-row-tx"><h2>The best training, in one place.</h2><p>Our partners The Global Harvest and NeedGod.net, alongside well-loved training like Christianity Explained, Two Ways to Live, The Way of the Master, The Bridge to Life, Steps to Peace with God and Alpha. Each opens on its own site.</p>
    <p>Read the Bible with a friend, too: Read together walks you through a Discovery Bible Study, with ten stories of people meeting Jesus.</p></div></div>
  <div class="ap-row rv"><div class="ap-row-art">{ph('baptism', 'Asking about baptism')}</div>
    <div class="ap-row-tx"><h2>Ready to be baptised?</h2><p>Anyone can ask. They choose who helps them take the step: a local church, a partner, or both, each by its own tick.</p></div></div>
</div></section>
<section class="sec pg-sec ap-trust"><div class="wrap ap-trust-in rv">
  <span class="ap-lock" aria-hidden="true"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/></svg></span>
  <div><h2>Your phone, your notes.</h2><p>The people you pray for, your notes and your highlights stay on your phone. No ads and no tracking. <a href="#/docs/saving">How your information is saved</a></p></div>
</div></section>
<section class="sec pg-sec ap-end"><div class="wrap ap-end-in">
  <div><h2>Open it on your phone.</h2><p>Free for every Christian. Add it to your home screen and it works like any other app.</p><div class="pg-cta"><a class="btn btn-peach" href="https://app.alwaysfoundation.org">Open Always Sent</a><a class="btn btn-ghost" href="#/join/evangelist">For street teams and ministries</a></div></div>
  <span class="ap-qr-lg">{AP_QR}</span>
</div></section>'''


FAQ_GROUPS = [
 ('About Always', [
  ('What is the Always Foundation?', 'A gospel technology ministry and not-for-profit serving churches and ministries freely. We bring churches and Christian ministries across Australia together for the Gospel. We serve quietly in the background, building practical tools once and sharing them freely, so ministries spend less time on administration and more time making disciples.'),
  ('Are you a gospel ministry or a mercy ministry?', 'Neither, directly. We are a ministry that serves ministries. In Acts 6 the early church appointed people to carry the practical work so the apostles could devote themselves to prayer and the word, and the Gospel spread. We play that role for the wider Church: we exist to equip the saints for the work of ministry (Ephesians 4:12). We are not on the frontline. We stand behind it.'),
  ('What does Always do for a church or ministry?', 'Three things. We equip, with Always Sent and Always Respond, your own branded way for people to respond. We support, with Always Safety and Always Reports, so the administration is lighter. And we connect, with Always Connect, so everyone who says yes to Jesus can be welcomed by a local church.'),
  ('Who can become a partner?', 'Churches and Christian ministries. Partners affirm the Nicene Creed (AD 381), so churches across denominations can serve together on the historic faith. Our partner churches and ministries help shape what we build through feedback and shared standards. Supporters can stand with us in prayer.'),
  ('What is Always Platform?', 'One open-source platform with one sign-in and shared data. Partners switch on the modules they need: Always Sent, Always Respond, Always Safety, Always Reports and Always Connect. Like YouVersion, there are tools people use every day and an open platform underneath that others can build on.'),
  ('Why modules?', 'Every ministry is different. Start with the one you need, perhaps Always Safety, and add others as you grow. Because every module runs on the same platform, your team signs in once and your information works together, with nothing to move later.'),
  ('Who runs it?', 'The Always Foundation: a gospel technology ministry and not-for-profit serving churches and ministries freely. It is being established in Australia. Churches and ministries that affirm the Nicene Creed are its partners.'),
  ('Is it only for one denomination?', 'No. Evangelical and Pentecostal churches and ministries across denominations and networks take part, on the common ground of the Nicene Creed.'),
  ('Is Always Platform only in Australia?', 'Our focus is Australia. The technology is open source, so churches and ministries in other countries are welcome to use it.'),
  ('Do I need an account?', 'Not for Always Sent: open it and start, and your prayer list and notes stay on your phone. Church and ministry teams sign in with an email link for tools like Always Safety.')]),
 ('For churches', [
  ('Does it cost anything?', 'No. Always is free for churches and ministries.'),
  ('How do we partner with Always?', 'Register at Partner with Always and get ready at your own pace. We check with your denomination or network, and then you\'re a partner church.'),
  ('What if we can\'t welcome someone?', 'Pass, with a reason. The next church or ministry nearby is asked. If none can, our care team helps.'),
  ('Do we have to change our church software?', 'No. Use the free Always Connect inbox, in any browser, or connect your system through the API. Elvanto and Planning Center come first.'),
  ('What does welcoming now mean?', 'You\'re a partner church, trained, have room this month and usually reply on time. If you get busy, introductions simply pause.'),
  ('Who on our team can see people\'s details?', 'Only the people you add to your team, and only after your church accepts an introduction.')]),
 ('For ministries and events', [
  ('Can we use our own brand?', 'Yes. Always Respond pages, QR codes, NFC taps and texts can use your colours, logo and wording.'),
  ('Does Always work with our church management system?', 'Yes. Always hands people on to Elvanto, Planning Center, Fluro, ChurchSuite and Breeze. See Integrations at alwaysfoundation.org/#/integrations.'),
  ('What results do we see?', 'Totals for each event: responded, introduced, accepted and connected. Each person\'s details go only to the church that welcomes them.'),
  ('Can Always Platform help us report to our funders?', 'Yes. It writes a monthly report for you: who responded, who was introduced, who was contacted, and who is now part of a church family. Download it as a PDF or spreadsheet, or send your funder a link.'),
  ('Will our funders see people\'s details?', 'No. Reports show totals only, and small numbers are hidden so no one can be identified.'),
  ('Can Always Platform help with privacy and child safety paperwork?', 'Yes. Your Safety tab keeps your consent records, privacy requests, child safety checklists and Working With Children Check reminders, ready to export.'),
  ('Can we make the report our own?', 'Yes. Add your title, your funder\'s name and a short introduction. If a funder needs something specific, talk to us.'),
  ('Can we receive introductions ourselves?', 'Yes, for the steps you offer, like a youth night or a course.'),
  ('Can people respond online?', 'Yes. Add a response link or QR to a video description or post, or embed the response card on your website. An invisible check stops spam without puzzles.'),
  ('How do evangelists and street teams use it?', 'With Always Sent, a free web app: they start a response point, show their own QR, or connect someone in a conversation with their yes.')]),
 ('For people who respond', [
  ('What happens when I respond?', 'You choose a next step, see who will be in touch, and a church or ministry near you reaches out.'),
  ('What do you need from me?', 'Your first name, a mobile number and your suburb.'),
  ('Do I need to download an app?', 'No. You respond on a simple web page. Later, you\'re welcome to try Always Sent in your browser to read the Bible and grow.'),
  ('Can I change my mind?', 'Yes, any time, from the link in your text. Your details are then deleted.'),
  ('I\'m under 18. Can I still respond?', 'Yes. If you\'re under 15, a parent or guardian says yes with you. From 15 you can decide for yourself. Young people are introduced only to youth partners, and no AI ever touches your information.')]),
 ('Always Sent', [
  ('Who is it for?', 'Every Christian who wants to share Jesus and walk with people, and church teams who welcome them.'),
  ('How do I get it?', 'It\'s a web app, so there\'s nothing to download. Open app.alwaysfoundation.org on any phone.'),
  ('Is there a mobile app?', 'Not for now. Always Sent and our tools for churches and ministries run in the browser on your phone, tablet or computer, and you can add it to your home screen.'),
  ('Which Bible translations are included?', 'The King James Version and the World English Bible, with more through YouVersion.'),
  ('Where are my notes and prayer list kept?', 'In your browser, on your own device. They aren\'t sent to us.')]),
 ('Privacy and safety', [
  ('Where is information kept?', 'In Australia, encrypted, under Australian privacy law.'),
  ('Do you sell information or use it for advertising?', 'No.'),
  ('How do you use AI?', 'To save time on routine work, like writing your monthly report. Every welcome comes from a real person, and young people\'s information is kept out of AI entirely.'),
  ('What is Always Safety?', 'A guide to the privacy, child safety, charity and messaging rules that apply to your ministry, with a check-up every quarter that a person at your ministry approves, and updates when the law changes. It is free for churches and is not legal advice. Try the free check-up at alwaysfoundation.org/#/compliance.'),
  ('What do Always agents do?', 'They help your team with follow-up and administration: drafting messages, setting reminders and keeping records up to date. A person approves every step, people\'s details stay in Australia, and agents never handle young people\'s information.'),
  ('Do churches and ministries share my information with each other?', 'No. Your details go only to the church or ministry you ask to be introduced to. Always does not link your information across organisations.'),
  ('How do I report a concern?', 'Email safeguarding@alwaysfoundation.org for safeguarding, privacy@ for privacy and security@ for security.')]),
 ('Supporters and builders', [
  ('How can I support the work?', 'Stand with us in prayer, and get in touch at hello@alwaysfoundation.org to book a catch-up call.'),
  ('Can developers build on Always Platform?', 'Yes. The API, SDK and open standard are open source under Apache 2.0, with docs under CC BY 4.0. An MCP server for AI assistants is coming, and it never sees a person\'s details.')])]

FAQ = '<section class="page-hero"><div class="wrap"><h1>FAQs</h1><p>Short answers to the questions we hear most.</p></div></section><section class="sec pg-sec"><div class="wrap pg-faq">' + \
  '<nav class="pg-faq-nav" aria-label="FAQ topics">' + ''.join(f'<a href="#faq-{i}" data-faq="{i}">{g}</a>' for i, (g, _) in enumerate(FAQ_GROUPS)) + '</nav><div>' + \
  ''.join(f'<div class="pg-faq-g" id="faq-{i}"><h2>{g}</h2>' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in qs) + '</div>' for i, (g, qs) in enumerate(FAQ_GROUPS)) + \
  '<div class="pg-faq-more"><h3>Still have a question?</h3><p>We\'d love to hear from you, and to book a catch-up call. <a href="#/contact">Get in touch</a> or email <a href="mailto:hello@alwaysfoundation.org">hello@alwaysfoundation.org</a>.</p></div></div></div></section>'

CSS = '''
/* ---- App page ---- */
.ap-hero { overflow: hidden; }
.ap-hero-in { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1.05fr); gap: 40px; align-items: center; }
.ap-copy h1 { font-size: clamp(44px, 5.4vw, 82px); line-height: .95; letter-spacing: -.04em; }
.ap-copy > p:not(.pl-kick) { max-width: 42ch; margin-top: 22px; font-size: 19px; line-height: 1.55; }
.ap-qr { display: flex; align-items: center; gap: 14px; margin-top: 28px; }
.ap-qr span { flex: none; width: 76px; height: 76px; padding: 6px; border-radius: 14px; background: #fff; line-height: 0; }
.ap-qr svg, .ap-qr-lg svg { width: 100%; height: 100%; }
.page-hero .ap-qr p { margin: 0; max-width: 22ch; font-size: 14.5px; opacity: .75; }
.ap-ph { margin: 0; border-radius: 42px; padding: 9px; background: #0E1613; box-shadow: inset 0 0 0 1.5px rgba(255,255,255,.08), 0 40px 80px -36px rgba(0,0,0,.65); }
.ap-ph img { display: block; width: 100%; height: auto; border-radius: 34px; }
.ap-stage { position: relative; height: clamp(520px, 52vw, 680px); }
.ap-stage .ap-ph { position: absolute; top: 50%; width: clamp(200px, 19vw, 280px); }
.ap-c { left: 50%; z-index: 3; transform: translate(-50%, -50%); }
.ap-l { left: 50%; z-index: 1; transform: translate(-118%, -46%) rotate(-7deg); opacity: .92; }
.ap-r { left: 50%; z-index: 2; transform: translate(18%, -44%) rotate(6deg); opacity: .95; }
@media (prefers-reduced-motion: no-preference) {
  .ap-stage .ap-ph { animation: apIn 1s cubic-bezier(.2,.75,.15,1) both; }
  .ap-c { animation-delay: .1s !important; } .ap-l { animation-delay: .3s !important; } .ap-r { animation-delay: .45s !important; }
}
@keyframes apIn { from { opacity: 0; margin-top: 40px; } to { margin-top: 0; } }
.ap-steps { list-style: none; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 24px; margin: 44px 0 0; padding: 0; }
.ap-step-ph { padding: 26px 26px 0; border-radius: 28px 28px 0 0; background: linear-gradient(170deg, #E7F0EA, #D5E5DB); height: 340px; overflow: hidden; }
.ap-steps li:nth-child(2) .ap-step-ph { background: linear-gradient(170deg, #F8E6D6, #F1D2B9); }
.ap-steps li:nth-child(3) .ap-step-ph { background: linear-gradient(170deg, #1F5248, #14352F); }
.ap-steps li:nth-child(4) .ap-step-ph { background: linear-gradient(170deg, #EFE6D6, #E4D6BE); }
.ap-step-ph .ap-ph { border-radius: 34px 34px 0 0; padding-bottom: 0; } .ap-step-ph .ap-ph img { border-radius: 26px 26px 0 0; }
.ap-n { display: flex; align-items: center; gap: 10px; margin-top: 22px; font: 700 14px/1 var(--head); color: var(--clay, #A4562A); }
.ap-n span { display: grid; place-items: center; width: 26px; height: 26px; border-radius: 50%; background: var(--green); color: var(--cream); font-size: 13px; }
.ap-steps h3 { margin-top: 10px; font: 800 21px/1.25 var(--head); color: var(--green); }
.ap-steps li > p:last-child { margin-top: 8px; font-size: 15.5px; line-height: 1.55; color: var(--soft); }
.ap-rows .wrap { display: grid; gap: clamp(64px, 9vw, 120px); }
.ap-row { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: clamp(32px, 6vw, 96px); align-items: center; }
.ap-flip .ap-row-art { order: 2; }
.ap-row-art { display: grid; place-items: center; padding: clamp(32px, 4vw, 56px); border-radius: 36px; background: radial-gradient(80% 70% at 50% 30%, #E9F1EB, #D6E5DB); }
.ap-flip .ap-row-art { background: radial-gradient(80% 70% at 50% 30%, #FBEBDD, #F2D6C0); }
.ap-row-art .ap-ph { width: min(260px, 64%); }
.ap-duo { grid-template-columns: 1fr 1fr; gap: 18px; } .ap-duo .ap-ph { width: 100%; } .ap-duo .ap-ph + .ap-ph { transform: translateY(36px); }
.ap-row-tx h2 { font: 800 clamp(32px, 3.6vw, 48px)/1.05 var(--head); letter-spacing: -.03em; color: var(--green); }
.ap-row-tx p { margin-top: 18px; max-width: 44ch; font-size: 18px; line-height: 1.6; color: var(--soft); }
.ap-trust-in { display: flex; gap: 22px; align-items: center; padding: 34px 38px; border-radius: 28px; background: #FFFDF8; box-shadow: 0 1px 0 rgba(27,71,64,.05); }
.ap-lock { display: grid; place-items: center; flex: none; width: 60px; height: 60px; border-radius: 20px; background: var(--green); color: var(--cream); } .ap-lock svg { width: 28px; height: 28px; }
.ap-trust h2 { font: 800 26px/1.2 var(--head); color: var(--green); } .ap-trust p { margin-top: 6px; font-size: 16.5px; line-height: 1.55; color: var(--soft); } .ap-trust a { color: var(--green); font-weight: 600; }
.ap-end { background: var(--green); color: var(--cream); }
.ap-end-in { display: grid; grid-template-columns: minmax(0, 1fr) auto; gap: 48px; align-items: center; }
.ap-end h2 { font: 800 clamp(36px, 4.4vw, 60px)/1 var(--head); letter-spacing: -.035em; color: var(--cream); }
.ap-end p { margin-top: 16px; max-width: 40ch; font-size: 18px; line-height: 1.55; color: rgba(248,243,234,.78); }
.ap-qr-lg { display: block; width: 180px; height: 180px; padding: 14px; border-radius: 24px; background: #fff; line-height: 0; }
@media (max-width: 1000px) {
  .ap-hero-in, .ap-row, .ap-end-in { grid-template-columns: 1fr; } .ap-flip .ap-row-art { order: 0; }
  .ap-steps { grid-template-columns: 1fr 1fr; } .ap-stage { height: 560px; } .ap-qr { display: none; }
}
@media (max-width: 600px) {
  .ap-steps { grid-template-columns: 1fr; } .ap-stage { height: 470px; } .ap-stage .ap-ph { width: 190px; }
  .ap-trust-in { flex-direction: column; align-items: flex-start; } .ap-qr-lg { display: none; }
}
/* ---- New in Always Sent ---- */
.app-new-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 18px; margin-top: 36px; }
.an { display: grid; align-content: start; gap: 10px; }
.an h3 { margin-top: 8px; font: 800 20px/1.25 var(--head); color: var(--green); }
.an p { font-size: 15.5px; line-height: 1.55; color: var(--soft); }
.an-art { display: grid; place-items: center; aspect-ratio: 4 / 3; border-radius: 24px; background: linear-gradient(150deg, #E7F0EA, #D3E4D9); overflow: hidden; }
.an-dark { background: linear-gradient(150deg, #22302B, #101A17); }
.an-share { display: grid; gap: 6px; height: 82%; aspect-ratio: 4 / 5; padding: 18px; border-radius: 16px; background: linear-gradient(160deg, #F2B48A, #E08E5E); color: #1E2A26; align-content: center; box-shadow: 0 20px 40px -24px rgba(164,86,42,.7); }
.an-share .an-t { font: 400 26px/1.1 Newsreader, Georgia, serif; }
.an-k { font: 700 12.5px/1.2 var(--head); color: var(--clay, #A4562A); } .an-share .an-k { color: #1B4740; }
.an-s { font: 500 13px/1.3 var(--head); opacity: .8; }
.an-langs { display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; padding: 18px; }
.an-langs span { padding: 7px 12px; border-radius: 99px; background: #FFFDF8; font: 600 14px/1.2 var(--head); color: var(--green); box-shadow: 0 1px 0 rgba(27,71,64,.06); }
.an-langs span:nth-child(2) { background: var(--green); color: var(--cream); }
.an-today { display: grid; gap: 4px; width: 78%; padding: 18px 20px; border-radius: 18px; background: linear-gradient(150deg, #FBE7D8, #F5D3BA); color: #1E2A26; box-shadow: 0 20px 40px -26px rgba(164,86,42,.6); }
.an-today b { font: 700 17px/1.3 var(--head); }
.an-ptrs { display: flex; gap: 14px; } .an-mono { display: grid; place-items: center; width: 76px; height: 76px; border-radius: 24px; background: var(--green); color: var(--cream); font: 800 24px/1 var(--head); } .an-mono.an-ng { background: #F8D486; color: #1E2A26; }
.an-modes { display: flex; gap: 12px; } .an-modes i { width: 70px; height: 120px; border-radius: 16px; background: #F8F3EA; box-shadow: 0 16px 30px -18px rgba(0,0,0,.7); } .an-modes i + i { background: #1B2B26; box-shadow: inset 0 0 0 1px rgba(255,255,255,.08), 0 16px 30px -18px rgba(0,0,0,.7); }
@media (max-width: 900px) { .app-new-grid { grid-template-columns: 1fr 1fr; } }
@media (max-width: 600px) { .app-new-grid { grid-template-columns: 1fr; } }
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
.pg-night .pg-feat h3, .pg-green .pg-feat h3 { color: var(--green); }
.pg-night .pg-feat p, .pg-green .pg-feat p { color: var(--soft); }
@media (min-width: 1081px) { .pg-feats:has(> .pg-feat:nth-child(4):last-child) { grid-template-columns: repeat(4, 1fr); } }
@media (max-width: 640px) { .pg-link-card { justify-self: start; } }
.pg-link-card { background: #FFFDF8; border-radius: 22px; padding: 26px; display: grid; gap: 8px; max-width: 380px; justify-self: end; width: 100%; box-shadow: 0 20px 40px -24px rgba(27,71,64,.35); }
.pg-link-card .plc-k { font: 600 13px/1 var(--head); color: var(--muted); }
.pg-link-card b { font: 700 20px/1.3 var(--head); color: var(--green); }
.pg-link-card .plc-qr { width: 96px; height: 96px; border-radius: 12px; margin: 8px 0; background: repeating-conic-gradient(var(--green) 0 25%, #FFFDF8 0 50%) 0 0 / 16px 16px; opacity: .85; }
.pg-link-card .plc-f { font-size: 14.5px; color: var(--soft); line-height: 1.5; }
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
    <div><h3>Running an event?</h3><p>Churches and ministries add events when they sign in to Always. Anyone can suggest one, and our team checks every event before it shows.</p></div>
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
    <ol><li><b>We check your role</b> with your denomination or network.</li><li><b>You set up your page</b>: welcome, service times and next steps.</li><li><b>Your connect lead</b> completes the 20-minute welcoming course.</li><li><b>You're a partner church</b>, and people nearby can be introduced to you.</li></ol>
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
    <label>Where<select name="area"><option>The website</option><option>Always Sent</option><option>Always Connect</option><option>Always Safety</option><option>Always Respond</option><option>Somewhere else</option></select></label>
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
  ('Field notes', 'Published', 'Agents with a human in the loop', 'Always Connect grew out of an earlier project called Branches. Its agent checked each response and handed it to a person before anything was shared. Trialled at a youth event with UEN, it shaped how agents in Always Platform work today.', '#/docs/always-agent'),
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

import base64 as _b64, os as _os
def _sq(name):
    path = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), '..', 'brand', name + '.svg')
    return 'data:image/svg+xml;base64,' + _b64.b64encode(open(path, 'rb').read()).decode()

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
  <h3 class="br-sub rv">Square</h3>
  <p class="br-fine rv">For profile pictures, social media, app icons and anywhere that needs a square. 1024 by 1024 pixels.</p>
  <div class="br-logos br-squares">
    <figure class="br-logo br-sq"><img src="{_sq('always-foundation-square')}" alt="Always Foundation square logo"><figcaption>Square</figcaption><div class="br-dl"><a class="btn btn-green" href="/brand/always-foundation-square.png?download">Download PNG</a><a class="br-alt" href="/brand/always-foundation-square.svg?download">SVG</a></div></figure>
    <figure class="br-logo br-sq dark"><img src="{_sq('always-foundation-square-on-green')}" alt="Always Foundation square logo on green"><figcaption>Square on green</figcaption><div class="br-dl"><a class="btn btn-peach" href="/brand/always-foundation-square-on-green.png?download">Download PNG</a><a class="br-alt" href="/brand/always-foundation-square-on-green.svg?download">SVG</a></div></figure>
    <figure class="br-logo br-sq dark"><img src="{_sq('always-foundation-icon')}" alt="Always Foundation icon: the cross"><figcaption>Icon</figcaption><div class="br-dl"><a class="btn btn-peach" href="/brand/always-foundation-icon.png?download">Download PNG</a><a class="br-alt" href="/brand/always-foundation-icon.svg?download">SVG</a></div></figure>
  </div>

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
.br-sub { margin: 48px 0 6px; font-size: 22px; color: var(--green); }
.br-logos.br-squares { grid-template-columns: repeat(3, minmax(0, 1fr)); }
.br-logo.dark.br-sq img { box-shadow: 0 0 0 1px rgba(248,243,234,.28); }
.br-sq img { aspect-ratio: 1; width: 100%; max-width: 220px; height: auto; border-radius: 18px; }
@media (max-width: 760px) { .br-logos.br-squares { grid-template-columns: 1fr; } }

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
  ('Find a church', 'Partner churches near any postcode, ready to welcome and safe for young people.', 'Church feed'),
  ('Introduce someone', 'Pass on someone who said yes, with their permission.', 'Handoff'),
  ('Welcome them', 'Churches say yes, reach out, and keep walking with them.', 'Church inbox'),
  ('Gather', 'Christian events across Australia, in one place.', 'Events'),
  ('See the fruit', 'Show supporters what God is doing, without sharing a single name.', 'Reports'),
  ('Follow up and admin', 'Agents draft follow-up messages, reminders and records for your team. A person approves every step.', 'Agents'),
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
  ('Always Sent', 'Share Jesus, start a response point and walk with people.', '#/app',
   [('Connect', 'Church feed and Events'), ('Gather', 'Response pages and Handoff'), ('Bible', 'YouVersion Platform'), ('Walk', 'Kept in your browser')]),
  ('Always Connect', 'Accept or pass introductions, welcome people and keep walking with them.', '#/churches',
   [('Inbox', 'Handoff'), ('Your page', 'Church feed and partner status'), ('Leaders\' report', 'Reports')]),
  ('Always Respond', 'Response pages and QR codes under your own brand, with live results.', '#/respond',
   [('Response pages', 'Your own brand'), ('Live results', 'Handoff'), ('Funder reports', 'Always Reports'), ('Consent records', 'Always Safety')]),
]
def _prod(name, line, href, uses):
    rows = ''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in uses)
    return f'<a class="pl-prod rv" href="{href}"><p class="pl-prod-k">Web app</p><h3>{name}</h3><p>{line}</p><ul>{rows}</ul></a>'
BUILT_ON = f'''<section class="sec pg-sec pg-sage"><div class="wrap">
  <p class="pl-kick rv">Built on Always Platform</p>
  <h2 class="pg-h rv">We build our own apps on it too.</h2>
  <p class="pg-lead rv">Always Sent, and our tools for churches and ministries, are free web apps that run in any browser, with nothing to download. Each one talks to the platform through the same public API and SDK that are open to you. There's no private back door: if we can build it, so can you.</p>
  <div class="pl-prods">{''.join(_prod(*p) for p in PRODUCTS)}</div>
</div></section>'''

PLATFORM = f'''<section class="page-hero"><div class="wrap pg-split">
  <div><p class="pl-kick">Always Platform</p><h1>For developers</h1><p class="pd-line">The API, SDK, feeds and AI connector behind every Always product, open to build on.</p><p>The same open-source foundation every Always product runs on, ready for your own website, app or platform.</p>
  <div class="pl-ctas"><a class="btn btn-peach" href="#/docs/feed">Start building</a><a class="btn btn-ghost" href="#/contact">Talk to us</a></div></div>
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
    <div class="pl-layer" role="listitem"><b>Web apps</b><span>The Always products, your own apps and websites, and AI assistants</span></div>
    <div class="pl-layer mid" role="listitem"><b>Always Platform</b><span>Find a church, introduce someone, welcome them, trust, gather, see the fruit</span></div>
    <div class="pl-layer base" role="listitem"><b>Network</b><span>Partner churches, permission that travels with people, and a care team when no one else can</span></div>
  </div>
</div></section>
<section class="sec pg-sec pg-green"><div class="wrap">
  <p class="pl-kick rv">What never changes</p>
  <h2 class="pg-h rv">A gift to the Church.</h2>
  <div class="pl-never">{''.join(f'<div class="rv"><b>{t}</b><span>{d}</span></div>' for t, d in [('Free', 'Always is free for churches and ministries.'), ('Open', 'Every line is public, to check and build on.'), ('Permission first', 'Nothing about a person moves without their yes.'), ('Kept in Australia', 'People\'s details stay here.'), ('Safe for young people', 'No AI and no sharing for anyone under 18.'), ('People decide', 'AI helps with the work. People make the calls.')])}</div>
  <div class="pg-cta rv"><a class="btn btn-peach" href="#/docs/feed">Start building</a><a class="btn btn-ghost" href="#/contact">Talk to us</a></div>
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


MINISTRIES += """<section class="sec pg-sec pg-green"><div class="wrap">
  <h2 class="pg-h rv">For evangelists and street teams</h2>
  <p class="pg-lead rv">Share Jesus with confidence, save every contact safely, and connect people with a local church, like evangelists in Sydney.</p>
  <div class="sl-rows sl-rows-3">
    <div class="sl-row rv"><h3>Share with confidence</h3><p>The Good News, Scripture and short training in Always Sent.</p></div>
    <div class="sl-row rv"><h3>Save every contact safely</h3><p>Your own branded response app, with contacts kept safe in Australia.</p></div>
    <div class="sl-row rv"><h3>Connect people locally</h3><p>With their consent, pass people to a church near them, or to Alpha if they want to explore faith.</p></div>
  </div>
  <div class="pg-cta rv"><a class="btn btn-peach" href="#/join/evangelist">Join as an evangelist</a><a class="btn btn-ghost" href="#/streets">Read their story</a></div>
</div></section>"""
