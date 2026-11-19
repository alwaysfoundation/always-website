"""The Always product line and solutions: one source of truth for names, positioning and pages.

Brand architecture
  Always Foundation  the member-based Christian nonprofit
  Always Platform    the open-source technology every product runs on
  Always + one word  the products ministries use (never "the Always X platform")

Every product's one-line positioning is defined once here and reused on the home page,
the Platform page, the product page, solution pages, the menu and the footer.
"""
from html import escape

PILLARS = [
    ('equip', 'Equip', 'Resources for every ministry.'),
    ('support', 'Support', 'More time for ministry.'),
    ('connect', 'Connect', 'One body. Many members.'),
    ('agents', 'Agents', 'Help that never sleeps, with a person in charge.'),
    ('build', 'Build', 'The foundation everything runs on.'),
]

# slug: (route, name, pillar, positioning, for)
PRODUCTS = {
    'app':        ('app',        'Always App',        'equip',   'Everything a Christian needs to share Jesus and walk with people.', 'Every Christian and evangelist'),
    'pages':      ('pages',      'Always Pages',      'equip',   'Your own branded response pages, from the street to the altar call to online.', 'Churches, evangelists, events and ministries'),
    'compliance': ('compliance', 'Always Compliance', 'support', 'Stay lawful on privacy, child safety, charity and messaging rules, with a quarterly check-up.', 'Every ministry'),
    'reports':    ('reports',    'Always Reports',    'support', 'A monthly report for your board and funders, written for you, with totals only.', 'Ministries with boards and funders'),
    'connect':    ('connect',    'Always Connect',    'connect', 'The church directory and a safe, consent-based handoff, so no one walks alone.', 'Churches, ministries and events'),
    'agents':     ('agents',     'Always Agents',     'agents',  'Help with follow-up and admin. A person approves every step.', 'Ministry teams'),
    'build':      ('build',      'Always Build',      'build',   'The API, SDK, feeds and AI connector, for developers and partner platforms.', 'Developers and Christian tech platforms'),
}

# slug: (route, menu name, one line, products used, story)
SOLUTIONS = {
    'churches':   ('churches',    'Churches',                     'Welcome people near you who have said yes to Jesus, and help them grow as disciples.', ['connect', 'pages', 'reports', 'compliance'], None),
    'youth':      ('youth',       'Youth ministries',             'Keep young people safe, stay compliant, and give every young person a safe next step.', ['compliance', 'pages', 'connect', 'reports'], ('UEN', 'A Christian gaming ministry that tried Always Platform at youth events.')),
    'ministries': ('ministries',  'Events, tours and ministries', 'Give everyone who responds a next step near home, and show funders the fruit.', ['pages', 'connect', 'reports', 'agents'], ('CXMMXNS', 'A worship tour giving every response a next step across Australia.')),
    'evangelists':('evangelists', 'Evangelists and street teams', 'Share Jesus with confidence, save every contact safely, and connect people with a local church.', ['app', 'pages', 'connect', 'agents'], ('Sydney Fire Evangelism', 'Street evangelists using their own branded response app.')),
    'networks':   ('networks',    'Denominations and networks',   'Help every church be ready to welcome, and see the fruit across your network, with totals only.', ['connect', 'reports', 'compliance', 'build'], None),
    'platforms':  ('platforms',   'Christian tech platforms',     'Build compliance, handoff and church data into your own product, on open standards.', ['build', 'compliance', 'connect'], ('Love is Our Weapon', 'Our first Always Compliance user, ready to roll it out to youth ministries and churches.')),
}

PILLAR_NAME = {k: n for k, n, _ in PILLARS}


def product_link(slug, cls='pd-link'):
    route, name, _, line, _ = PRODUCTS[slug]
    return f'<a class="{cls}" href="#/{route}"><b>{name}</b><span>{line}</span></a>'


def product_card(slug):
    route, name, pillar, line, who = PRODUCTS[slug]
    return (f'<a class="pd-card rv" href="#/{route}"><span class="pd-pill">{PILLAR_NAME[pillar]}</span>'
            f'<h3>{name}</h3><p>{line}</p><span class="pd-for">For {who[0].lower() + who[1:]}</span></a>')


def solution_card(slug):
    route, name, line, _, _ = SOLUTIONS[slug]
    return f'<a class="sl-card rv" href="#/{route}"><h3>{name}</h3><p>{line}</p></a>'


def pillar_grid():
    """Home and Platform: the five pillars, each listing its products."""
    cards = []
    for key, name, tagline in PILLARS:
        items = ''.join(f'<li><a href="#/{PRODUCTS[s][0]}"><b>{PRODUCTS[s][1]}</b><span>{PRODUCTS[s][3]}</span></a></li>' for s in PRODUCTS if PRODUCTS[s][2] == key)
        cards.append(f'<article class="pl-pillar rv pl-{key}"><h3>{name}</h3><p class="pl-ptag">{tagline}</p><ul>{items}</ul></article>')
    return '<div class="pl-pillars">' + ''.join(cards) + '</div>'


def solutions_grid():
    return '<div class="sl-grid">' + ''.join(solution_card(s) for s in SOLUTIONS) + '</div>'


def menu_html():
    """Platform and Solutions drop-downs for the main menu."""
    plat = ''.join(
        f'<div class="dd-col"><p class="dd-h">{name}</p>' + ''.join(f'<a href="#/{PRODUCTS[s][0]}" data-route="{PRODUCTS[s][0]}"><b>{PRODUCTS[s][1]}</b><span>{PRODUCTS[s][3]}</span></a>' for s in PRODUCTS if PRODUCTS[s][2] == key) + '</div>'
        for key, name, _ in PILLARS)
    sol = ''.join(f'<a href="#/{r}" data-route="{r}"><b>{n}</b><span>{l}</span></a>' for r, n, l, _, _ in SOLUTIONS.values())
    return (
        '<li class="dd dd-static"><button type="button" class="dd-btn" aria-expanded="false" aria-controls="dd-platform" data-group="platform">Platform</button>'
        f'<div class="dd-panel dd-wide" id="dd-platform"><div class="dd-grid">{plat}</div><a class="dd-all" href="#/platform" data-route="platform">See Always Platform</a></div></li>'
        '<li class="dd"><button type="button" class="dd-btn" aria-expanded="false" aria-controls="dd-solutions" data-group="solutions">Solutions</button>'
        f'<div class="dd-panel" id="dd-solutions"><div class="dd-list">{sol}</div></div></li>'
        '<li><a href="#/stories" data-route="stories">Stories</a></li>'
        '<li><a href="#/docs/introduction" data-route="docs">Docs</a></li>'
        '<li><a href="#/about" data-route="about">About</a></li>'
    )


PRODUCT_ROUTES = [v[0] for v in PRODUCTS.values()] + ['platform']
SOLUTION_ROUTES = [v[0] for v in SOLUTIONS.values()]


def footer_cols():
    plat = ''.join(f'<a href="#/{v[0]}">{v[1]}</a>' for v in PRODUCTS.values())
    sol = ''.join(f'<a href="#/{v[0]}">{v[1]}</a>' for v in SOLUTIONS.values())
    return (f'<div><h2>Platform</h2>{plat}</div>'
            f'<div><h2>Solutions</h2>{sol}</div>'
            '<div><h2>Foundation</h2><a href="#/about">About</a><a href="#/stories">Stories</a><a href="#/events">Events</a><a href="#/research">Research</a><a href="#/brand">Brand</a><a href="#/faq">FAQs</a></div>'
            '<div><h2>Help</h2><a href="#/docs/introduction">Docs</a><a href="#/claim">Claim your church</a><a href="#/feedback">Ideas and problems</a><a href="#/docs/privacy">Privacy</a><a href="#/docs/young-people">Keeping young people safe</a></div>')


# ---------------------------------------------------------------- Product pages

def _feats(items):
    return '<div class="pg-feats">' + ''.join(f'<div class="pg-feat rv"><h3>{t}</h3><p>{d}</p></div>' for t, d in items) + '</div>'


def _works_with(slugs):
    return '<div class="pd-with">' + ''.join(product_link(s) for s in slugs) + '</div>'


def product_page(slug, intro, feats, works_with, extra='', status=None, primary=('Join Always', '#/join'), secondary=None, feats_title='What you get'):
    route, name, pillar, line, who = PRODUCTS[slug]
    badge = f'<p class="pd-status">{status}</p>' if status else ''
    sec = f'<a class="btn btn-ghost" href="{secondary[1]}">{secondary[0]}</a>' if secondary else ''
    return f'''<section class="page-hero pd-hero"><div class="wrap">
  <p class="pl-kick">Always Platform: {PILLAR_NAME[pillar]}</p>
  <h1>{name}</h1>
  <p class="pd-line">{line}</p>
  <p>{intro}</p>{badge}
  <div class="pg-cta"><a class="btn btn-peach" href="{primary[1]}">{primary[0]}</a>{sec}</div>
</div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">{feats_title}</h2>
  {_feats(feats)}
</div></section>
{extra}
<section class="sec pg-sec pg-sage"><div class="wrap">
  <h2 class="pg-h rv">Works with</h2>
  <p class="pg-lead rv">Every Always product runs on Always Platform, with one sign-in for your team.</p>
  {_works_with(works_with)}
</div></section>'''


PAGES_BRAND = '''<section class="sec pg-sec pg-green"><div class="wrap pd-brand">
  <div class="rv"><h2 class="pg-h">Your name. Your look. Your people.</h2>
  <p class="pg-lead">Every page carries your logo, colours and words, on your own link. People meet your ministry, not ours. We stay in the background.</p></div>
  <div class="pd-brand-mock rv" aria-hidden="true"><div class="pbm-top"><span class="pbm-logo"></span><span class="pbm-name">Your ministry</span></div>
  <p class="pbm-h">Today I said yes to Jesus</p><span class="pbm-in"></span><span class="pbm-in"></span><span class="pbm-btn">Take my next step</span></div>
</div></section>'''

PAGES_PAGE = product_page('pages',
    'Wherever someone says yes to Jesus, give them a simple page that looks like you. One scan or tap takes them from a moment online, on the street or in the room to a real next step.',
    [('On the street', 'A QR card or phone link so evangelists can save a contact in seconds, safely.'),
     ('At the altar call', 'Put a code on the big screen and let everyone who responds say so, then and there.'),
     ('Landing pages', 'A page for your event, campaign or video, with a clear way to respond.'),
     ('Comments and embeds', 'A link for comments and posts, or a form you embed in your own website or app.'),
     ('Online to in person', 'Every response can become a welcome from a local church or ministry, with consent.'),
     ('Safe by design', 'Consent recorded on every form. Age asked first. Live totals with no names on screen.')],
    ['connect', 'app', 'reports'],
    extra=PAGES_BRAND,
    feats_title='Wherever people respond',
    secondary=('Read the guide', '#/docs/senders'))

REPORTS_PAGE = product_page('reports',
    'Answer to donors, a foundation or a denomination? Always Reports writes your report each month from what already happened. Nothing extra to enter.',
    [('Written for you', 'A clear monthly report, ready for your board and funders.'),
     ('Totals only', 'No names. Small numbers are hidden so no one can be identified.'),
     ('Your words', "Use your funder's titles and the outcomes they care about."),
     ('Download or share', 'PDF, spreadsheet, or a link you can switch off.'),
     ('Definitions you can trust', 'Responded, introduced, contacted and now part of a church family, defined the same way every month.'),
     ('Across events and campuses', 'One report, or one for each event, tour or campus.')],
    ['pages', 'connect', 'compliance'],
    secondary=('See what\'s in a report', '#/docs/reports'))

CONNECT_PAGE = product_page('connect',
    'When someone says yes to Jesus, Always Connect helps them find a next step near home, often a local church and sometimes another ministry, with a real person reaching out.',
    [('The directory', '3,937 churches and ministries mapped across Australia, each able to claim its page.'),
     ('Verified churches', 'We check with each church\'s denomination or network before anyone is introduced.'),
     ('A safe handoff', 'The person chooses their next step and sees who will reach out before anything is shared.'),
     ('Your team inbox', 'Accept or pass introductions from any phone, and keep walking with people.'),
     ('Next steps beyond church', 'People exploring faith can choose Alpha. Others may need a youth group or a care team.'),
     ('No one dropped', 'If no one nearby can help, the Always care team reaches out.')],
    ['pages', 'app', 'agents'],
    secondary=('Claim your church', '#/claim'))

AGENTS_PAGE = product_page('agents',
    'Always Agents take on the repetitive work of follow-up and administration, so your team can spend its time with people. Every agent works for a person, and a person approves every step.',
    [('Follow-up agent', 'Drafts welcome messages and reminders after an event, for your team to check and send.'),
     ('Admin agent', 'Keeps records up to date and prepares drafts for your reports and compliance check-up.'),
     ('A person decides', 'Agents suggest. Your team approves, edits or ignores every step.'),
     ('Never with young people\'s details', 'Young people\'s information is kept out of AI entirely.'),
     ('Kept in Australia', 'People\'s details are stored and processed in Australia.'),
     ('Every step recorded', 'An audit trail shows what each agent suggested and who approved it.')],
    ['connect', 'reports', 'compliance'],
    status='Now in pilot with the foundation team.')

# ---------------------------------------------------------------- Solution pages

def solution_page(slug, outcomes, cta=('Talk to us', '#/join')):
    route, name, line, uses, story = SOLUTIONS[slug]
    story_html = ''
    if story:
        story_html = f'''<section class="sec pg-sec"><div class="wrap sl-story rv">
  <p class="pl-kick">Story</p><h2 class="pg-h">{story[0]}</h2><p class="pg-lead">{story[1]}</p>
  <a class="btn btn-ghost-dark" href="#/stories">Read the stories</a>
</div></section>'''
    return f'''<section class="page-hero"><div class="wrap">
  <p class="pl-kick">Solutions</p>
  <h1>For {name[0].lower() + name[1:]}</h1>
  <p>{line}</p>
  <div class="pg-cta"><a class="btn btn-peach" href="{cta[1]}">{cta[0]}</a></div>
</div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">What you can do</h2>
  {_feats(outcomes)}
</div></section>
<section class="sec pg-sec pg-sage"><div class="wrap">
  <h2 class="pg-h rv">Products you'll use</h2>
  <div class="pd-grid">{''.join(product_card(s) for s in uses)}</div>
</div></section>
{story_html}'''


YOUTH_PAGE = solution_page('youth', [
    ('Stay lawful and compliant', 'Child Safe Standards, working with children checks and privacy, with a quarterly check-up your board approves.'),
    ('Welcome young people safely', 'Age comes first. Under-15s need a parent to confirm, and young people are introduced only to verified youth partners.'),
    ('Show the fruit', 'Monthly reports for your board and funders, with totals only.'),
], cta=('Try the free compliance check-up', '#/compliance/check'))

EVANGELISTS_PAGE = solution_page('evangelists', [
    ('Share with confidence', 'Bible, conversation guides and short training in the Always App.'),
    ('Save every contact safely', 'Your own branded response app, like Sydney Fire\'s, with contacts kept safe in Australia.'),
    ('Connect people locally', 'With their consent, pass people to a church near them or to Alpha if they want to explore faith.'),
], cta=('Join the pilot', '#/join'))

NETWORKS_PAGE = solution_page('networks', [
    ('Ready to welcome', 'Help every church in your network claim its page, get verified and be ready to receive people.'),
    ('See the fruit across your network', 'Combined reports across your churches, with totals only.'),
    ('Shared compliance', 'One view of privacy and child safety obligations, so every church can stay lawful with less admin.'),
])

PLATFORMS_PAGE = solution_page('platforms', [
    ('Compliance inside your product', 'Use the open Always Compliance register and check-up API, so your users stay lawful without leaving your app.'),
    ('A safe handoff to local churches', 'Pass people to a verified church or ministry near them, with consent that travels with the data.'),
    ('Open standards, Australian data', 'Open-source code, the Always Handoff standard, and personal data kept in Australia.'),
], cta=('Explore Always Build', '#/build'))

# ---------------------------------------------------------------- Platform overview

PLATFORM_OVERVIEW = f'''<section class="page-hero"><div class="wrap">
  <p class="pl-kick">Always Platform</p>
  <h1>Seven products. One platform. Shared freely.</h1>
  <p>Always Platform is the open-source technology behind every Always product. Ministries use the products; developers and partner platforms can build on the same foundation.</p>
  <div class="pg-cta"><a class="btn btn-peach" href="#/join">Join Always</a><a class="btn btn-ghost" href="#/build">For developers</a></div>
</div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">The products</h2>
  <p class="pg-lead rv">Grouped by how they help: equip, support and connect ministries, with agents to lighten the load and open tools to build on.</p>
  {pillar_grid()}
</div></section>
<section class="sec pg-sec pg-sage"><div class="wrap">
  <h2 class="pg-h rv">Who it's for</h2>
  {solutions_grid()}
</div></section>
<section class="sec pg-sec pg-green"><div class="wrap">
  <h2 class="pg-h rv">What never changes</h2>
  <div class="pl-never">{''.join(f'<div class="rv"><b>{t}</b><span>{d}</span></div>' for t, d in [('Free for churches', 'Larger ministries contribute according to their size.'), ('Open', 'Every line is public, to check and build on.'), ('Permission first', 'Nothing about a person moves without their yes.'), ('Kept in Australia', "People's details stay here."), ('Safe for young people', 'No AI and no sharing for anyone under 18.'), ('People decide', 'Agents help with the work. People make the calls.')])}</div>
</div></section>'''

CSS = '''
/* ---- Product line ---- */
.pd-line { font: 700 clamp(20px, 2.2vw, 26px)/1.35 var(--head); color: var(--peach); max-width: 34ch; margin-top: 14px; }
.pd-hero p:not(.pd-line):not(.pl-kick):not(.pd-status) { max-width: 52ch; }
.pd-status { display: inline-block; margin-top: 16px; padding: 8px 14px; border-radius: 999px; background: rgba(248,243,234,.12); font: 600 14px/1 var(--head); color: var(--cream); }
.pd-with { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; margin-top: 28px; }
.pd-link { display: grid; gap: 6px; padding: 22px; border-radius: 18px; background: #FFFDF8; color: inherit; text-decoration: none; transition: transform .15s ease; }
.pd-link b { font: 700 18px/1.2 var(--head); color: var(--green); } .pd-link span { font-size: 15px; color: var(--soft); line-height: 1.5; }
.pd-link:hover, .pd-link:focus-visible { transform: translateY(-2px); }
.pd-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 14px; margin-top: 28px; }
.pd-card { display: grid; align-content: start; gap: 8px; padding: 24px; border-radius: 20px; background: #FFFDF8; color: inherit; text-decoration: none; }
.pd-card h3 { margin: 0; font-size: 20px; color: var(--green); } .pd-card p { margin: 0; font-size: 15px; line-height: 1.5; color: var(--soft); }
.pd-pill { justify-self: start; font: 700 12px/1 var(--head); padding: 6px 10px; border-radius: 999px; background: rgba(27,71,64,.08); color: var(--green); }
.pd-for { font-size: 13.5px; color: var(--muted); margin-top: 4px; }
.pl-pillars { display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 16px; margin-top: 36px; }
.pl-pillar { grid-column: span 2; background: #FFFDF8; border-radius: 22px; padding: 26px; border-top: 3px solid var(--peach); }
.pl-pillar.pl-agents, .pl-pillar.pl-build { grid-column: span 3; }
.pl-pillar h3 { margin: 0; font-size: 22px; color: var(--green); }
.pl-pillar .pl-ptag { margin: 4px 0 0; font: 700 15px/1.35 var(--head); color: var(--clay, #B5603A); }
.pl-pillar ul { list-style: none; margin: 16px 0 0; padding: 0; display: grid; gap: 4px; }
.pl-pillar li a { display: grid; gap: 3px; padding: 12px 0; border-top: 1px solid rgba(27,71,64,.1); color: inherit; text-decoration: none; }
.pl-pillar li:first-child a { border-top: 0; padding-top: 4px; }
.pl-pillar li b { font: 700 17px/1.2 var(--head); color: var(--green); } .pl-pillar li span { font-size: 14.5px; line-height: 1.5; color: var(--soft); }
.pl-pillar li a:hover b, .pl-pillar li a:focus-visible b { text-decoration: underline; text-decoration-color: var(--peach); text-underline-offset: 4px; }
.sl-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; margin-top: 32px; }
.sl-card { display: grid; align-content: start; gap: 8px; padding: 24px; border-radius: 20px; background: #FFFDF8; color: inherit; text-decoration: none; transition: transform .15s ease; }
.sl-card:hover, .sl-card:focus-visible { transform: translateY(-2px); }
.sl-card h3 { margin: 0; font-size: 19px; color: var(--green); } .sl-card p { margin: 0; font-size: 15px; line-height: 1.5; color: var(--soft); }
.sl-story { max-width: 760px; }
.heart .ctas { margin-top: 36px; }
.solutions-home { background: var(--green-deep, #16332E); }
.solutions-home .sec-title, .solutions-home .tag { color: var(--cream); } .solutions-home .tag { color: var(--peach); }
.solutions-home .sec-lede { color: var(--on-green); }
@media (max-width: 1000px) { .pl-pillars { grid-template-columns: 1fr 1fr; } .pl-pillar, .pl-pillar.pl-agents, .pl-pillar.pl-build { grid-column: auto; } .sl-grid, .pd-with { grid-template-columns: 1fr 1fr; } }
@media (max-width: 640px) { .pl-pillars, .sl-grid, .pd-with { grid-template-columns: 1fr; } }

.pd-brand { display: grid; grid-template-columns: 1.1fr .9fr; gap: 48px; align-items: center; }
.pd-brand .pg-h, .pd-brand .pg-lead { color: var(--cream); } .pd-brand .pg-lead { color: var(--on-green); }
.pd-brand-mock { justify-self: center; width: min(300px, 100%); background: #FFFDF8; border-radius: 28px; padding: 22px; display: grid; gap: 12px; box-shadow: 0 30px 60px -24px rgba(0,0,0,.45); }
.pbm-top { display: flex; align-items: center; gap: 10px; } .pbm-logo { width: 30px; height: 30px; border-radius: 9px; background: #6B4FA0; }
.pbm-name { font: 700 15px/1 var(--head); color: #3A2A5C; } .pbm-h { margin: 6px 0 2px; font: 800 22px/1.15 var(--head); color: #3A2A5C; }
.pbm-in { height: 40px; border-radius: 12px; border: 1.5px solid #E2DCEC; } .pbm-btn { margin-top: 4px; padding: 13px; border-radius: 999px; background: #6B4FA0; color: #fff; font: 700 15px/1 var(--head); text-align: center; }
@media (max-width: 800px) { .pd-brand { grid-template-columns: 1fr; gap: 28px; } }

/* ---- Menu drop-downs ---- */
.dd { position: relative; }
@media (min-width: 901px) { #main-nav > ul { align-items: center; } #main-nav > ul > li > a { display: inline-flex; align-items: center; min-height: 44px; } }
.dd-btn { background: none; border: 0; color: rgb(228, 238, 231); font: 500 15.5px/1 var(--body, Inter, system-ui, sans-serif); cursor: pointer; display: inline-flex; align-items: center; gap: 6px; padding: 0; min-height: 44px; }
.dd-btn::after { content: ''; width: 7px; height: 7px; border-right: 1.5px solid currentColor; border-bottom: 1.5px solid currentColor; transform: rotate(45deg) translateY(-2px); transition: transform .15s; }
.dd-btn[aria-expanded="true"]::after { transform: rotate(225deg) translateY(-1px); }
.dd-btn:hover, .dd-btn[aria-expanded="true"] { color: var(--cream); }
.dd-btn.current { color: var(--cream); text-decoration: underline; text-decoration-color: var(--peach); text-underline-offset: 8px; text-decoration-thickness: 2px; }
.dd-panel { position: absolute; top: calc(100% + 10px); left: 50%; transform: translateX(-50%); background: #FFFDF8; color: var(--ink, #1A1410); border-radius: 22px; padding: 22px; box-shadow: 0 30px 60px -20px rgba(0,0,0,.4); width: 380px; z-index: 50; display: none; }
.dd-panel.open { display: block; }
.dd-static { position: static; }
.dd-wide { width: min(1080px, 92vw); top: 84px; }
.dd-grid { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 18px; }
.dd-h { margin: 0 0 8px; font: 700 12.5px/1 var(--head); color: var(--clay, #B5603A); }
.dd-panel a { display: grid; gap: 3px; padding: 10px 12px; margin: 0 -12px; border-radius: 12px; color: inherit; text-decoration: none; }
.dd-panel a b { font: 700 15px/1.25 var(--head); color: var(--green); } .dd-panel a span { font-size: 13px; line-height: 1.45; color: var(--soft); font-weight: 400; }
.dd-panel a:hover, .dd-panel a:focus-visible, .dd-panel a[aria-current="page"] { background: rgba(27,71,64,.06); }
.dd-list { display: grid; gap: 2px; }
.dd-all { margin-top: 12px !important; border-top: 1px solid rgba(27,71,64,.1); border-radius: 0 0 12px 12px !important; font: 700 14px/1 var(--head); color: var(--green) !important; padding: 16px 12px 6px !important; }
@media (max-width: 900px) {
  .dd-btn { font: 800 34px/1.1 var(--head); letter-spacing: -0.02em; color: var(--cream); padding: 10px 0; }
  .dd-btn::after { display: none; }
  .dd-panel { position: static; transform: none; width: auto; display: block; background: transparent; box-shadow: none; padding: 0 0 12px; }
  .dd-grid { grid-template-columns: 1fr; gap: 10px; }
  .dd-h { color: var(--peach); margin-top: 8px; }
  .dd-panel a { margin: 0; padding: 6px 0; } .dd-panel a b { color: var(--cream); font-size: 17px; } .dd-panel a span { display: none; }
  .dd-all { border: 0; padding: 8px 0 !important; color: var(--peach) !important; }
}
'''

MENU_JS = '''
// Menu drop-downs: click to open, Escape or outside click to close
(() => {
  const btns = [...document.querySelectorAll('.dd-btn')];
  const close = (except) => btns.forEach((b) => { if (b !== except) { b.setAttribute('aria-expanded', 'false'); document.getElementById(b.getAttribute('aria-controls')).classList.remove('open'); } });
  btns.forEach((b) => b.addEventListener('click', (e) => {
    e.stopPropagation();
    const open = b.getAttribute('aria-expanded') !== 'true';
    close(b); b.setAttribute('aria-expanded', String(open));
    document.getElementById(b.getAttribute('aria-controls')).classList.toggle('open', open);
  }));
  document.addEventListener('click', (e) => { if (!e.target.closest('.dd-panel')) close(); });
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') { const o = btns.find((b) => b.getAttribute('aria-expanded') === 'true'); close(); o?.focus(); } });
  window.addEventListener('hashchange', () => close());
  const GROUPS = { platform: __PRODUCT_ROUTES__, solutions: __SOLUTION_ROUTES__ };
  const mark = () => { const r = location.hash.replace(/^#\\/?/, '').split('/')[0] || 'home'; btns.forEach((b) => b.classList.toggle('current', GROUPS[b.dataset.group].includes(r))); };
  window.addEventListener('hashchange', mark); mark();
})();
'''.replace('__PRODUCT_ROUTES__', repr(PRODUCT_ROUTES).replace("'", '"')).replace('__SOLUTION_ROUTES__', repr(SOLUTION_ROUTES).replace("'", '"'))

NEW_PAGES = {
    'pages': PAGES_PAGE, 'reports': REPORTS_PAGE, 'connect': CONNECT_PAGE, 'agents': AGENTS_PAGE,
    'youth': YOUTH_PAGE, 'evangelists': EVANGELISTS_PAGE, 'networks': NETWORKS_PAGE, 'platforms': PLATFORMS_PAGE,
}
TITLES = {r: f'{n} · Always Foundation' for r, n, *_ in PRODUCTS.values()}
TITLES.update({r: f'For {n[0].lower() + n[1:]} · Always Foundation' for r, n, *_ in SOLUTIONS.values()})
TITLES['platform'] = 'Always Platform · Always Foundation'
