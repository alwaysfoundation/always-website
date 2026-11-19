"""The Always product line and solutions: one source of truth for names, positioning and pages.

Brand architecture
  Always Foundation  the member-based Christian nonprofit
  Always Platform    the open-source technology every product runs on
  Always + one word  the products ministries use (never "the Always X platform")

Every product's one-line positioning is defined once here and reused on the home page,
the Platform page, the product page, solution pages, the menu and the footer.
"""
from html import escape
from mocks import mock, CSS as MOCK_CSS

PILLARS = [
    ('equip', 'Equip', 'Resources for every ministry.'),
    ('support', 'Support', 'More time for ministry.'),
    ('connect', 'Connect', 'One body. Many members.'),
]

# slug: (route, name, pillar, positioning, for)
PRODUCTS = {
    'app':        ('app',        'Always App',        'equip',   'Everything a Christian needs to share Jesus and walk with people.', 'Every Christian and evangelist'),
    'pages':      ('pages',      'Always Pages',      'equip',   'Your own branded response pages, from the street to the altar call to online.', 'Churches, evangelists, events and ministries'),
    'compliance': ('compliance', 'Always Compliance', 'support', 'Stay lawful on privacy, child safety, charity and messaging rules, with a quarterly check-up.', 'Every ministry'),
    'reports':    ('reports',    'Always Reports',    'support', 'A monthly report for your board and funders, written for you, with totals only.', 'Ministries with boards and funders'),
    'connect':    ('connect',    'Always Connect',    'connect', 'Find a local church, hand people on safely, and follow up together.', 'Churches, ministries and events'),
}
DEVELOPERS = ('developers', 'Developers', 'The API, SDK, MCP connector, feeds and webhooks behind every Always product.')
# Old routes: agents live inside Always Connect; the developer page moved.
ALIASES = {'agents': 'connect', 'build': 'developers', 'join': 'contact'}

# slug: (route, menu name, one line, products used, story)
SOLUTIONS = {
    'churches':   ('churches',    'Churches',                     'Welcome people near you who have said yes to Jesus, and help them grow as disciples.', ['connect', 'pages', 'reports', 'compliance'], None),
    'youth':      ('youth',       'Youth ministries',             'Keep young people safe, stay compliant, and give every young person a safe next step.', ['compliance', 'pages', 'connect', 'reports'], ('UEN', 'A Christian gaming ministry that tried Always Platform at youth events.')),
    'ministries': ('ministries',  'Events, tours and ministries', 'Give everyone who responds a next step near home, and show funders the fruit.', ['pages', 'connect', 'reports'], ('CXMMXNS', 'A worship tour giving every response a next step across Australia.')),
    'evangelists':('evangelists', 'Evangelists and street teams', 'Share Jesus with confidence, save every contact safely, and connect people with a local church.', ['app', 'pages', 'connect'], ('Sydney Fire Evangelism', 'Street evangelists using their own branded response app.')),
    'networks':   ('networks',    'Denominations and networks',   'Help every church be ready to welcome, and see the fruit across your network, with totals only.', ['connect', 'reports', 'compliance'], None),
    'platforms':  ('platforms',   'Christian tech platforms',     'Build compliance, handoff and church data into your own product, on open standards.', ['compliance', 'connect'], ('Love is Our Weapon', 'Our first Always Compliance user, ready to roll it out to youth ministries and churches.')),
}

PILLAR_NAME = {k: n for k, n, _ in PILLARS} | {'build': 'Build'}


def for_name(name):
    return 'For ' + (name if name.startswith('Christian') else name[0].lower() + name[1:])


def product_link(slug, cls='pd-link'):
    route, name, _, line, _ = PRODUCTS[slug]
    return f'<a class="{cls}" href="#/{route}"><b>{name}</b><span>{line}</span></a>'


def product_card(slug):
    route, name, pillar, line, who = PRODUCTS[slug]
    return (f'<a class="pd-card rv" href="#/{route}"><span class="pd-pill">{PILLAR_NAME[pillar]}</span>'
            f'<h3>{name}</h3><p>{line}</p><span class="pd-for">For {who[0].lower() + who[1:]}</span></a>')


def _and(items):
    return items[0] if len(items) == 1 else ', '.join(items[:-1]) + ' and ' + items[-1]


def solution_card(slug):
    route, name, line, uses, _ = SOLUTIONS[slug]
    names = [PRODUCTS[u][1].replace('Always ', '') for u in uses]
    return (f'<a class="sl-row rv" href="#/{route}"><h3>{name}</h3><p>{line}</p>'
            f'<span class="sl-with">With Always {_and(names)}</span></a>')


def pillar_grid():
    """Home and Platform: the five pillars, each listing its products."""
    cards = []
    for key, name, tagline in PILLARS:
        items = ''.join(f'<li><a href="#/{PRODUCTS[s][0]}"><b>{PRODUCTS[s][1]}</b><span>{PRODUCTS[s][3]}</span></a></li>' for s in PRODUCTS if PRODUCTS[s][2] == key)
        cards.append(f'<article class="pl-pillar rv pl-{key}"><h3>{name}</h3><p class="pl-ptag">{tagline}</p><ul>{items}</ul></article>')
    return '<div class="pl-pillars">' + ''.join(cards) + '</div>'


BENTO = ['app', 'pages', 'compliance', 'reports', 'connect']


def bento_tile(slug):
    route, name, pillar, line, _ = PRODUCTS[slug]
    return (f'<a class="bt bt-{slug} rv" href="#/{route}">{mock(slug)}'
            f'<div class="bt-body"><span class="bt-k btp-{pillar}">{PILLAR_NAME[pillar]}</span>'
            f'<h3>{name}</h3><p>{line}</p></div></a>')


def product_bento():
    return '<div class="bento">' + ''.join(bento_tile(s) for s in BENTO) + '</div>'


def developers_band():
    return (f'<a class="dev-band rv" href="#/{DEVELOPERS[0]}"><div><span class="bt-k">Underneath it all</span><h3>Build on Always Platform</h3>'
            f'<p>{DEVELOPERS[2]}</p></div>{mock("build")}</a>')


def switcher():
    """Platform hero: one sign-in, every product a tab."""
    tabs = ''.join(f'<button type="button" role="tab" class="sw-tab" id="sw-t-{s}" aria-controls="sw-p-{s}" aria-selected="{str(s == "pages").lower()}" tabindex="{0 if s == "pages" else -1}">{PRODUCTS[s][1].replace("Always ", "")}</button>' for s in BENTO)
    panels = ''.join(f'<div class="sw-panel" role="tabpanel" id="sw-p-{s}" aria-labelledby="sw-t-{s}"{"" if s == "pages" else " hidden"}>{mock(s)}<p class="sw-line"><b>{PRODUCTS[s][1]}</b> {PRODUCTS[s][3]} <a href="#/{PRODUCTS[s][0]}">Explore</a></p></div>' for s in BENTO)
    return (f'<div class="sw"><div class="sw-bar"><span class="sw-me"><i></i>Signed in to Always</span></div>'
            f'<div class="sw-tabs" role="tablist" aria-label="Always products">{tabs}</div>{panels}</div>')


def solutions_grid():
    return '<div class="sl-rows">' + ''.join(solution_card(s) for s in SOLUTIONS) + '</div>'


def menu_html():
    """Platform and Solutions drop-downs for the main menu."""
    plat = ''.join(
        f'<div class="dd-col"><p class="dd-h">{name}</p>' + ''.join(f'<a href="#/{PRODUCTS[s][0]}" data-route="{PRODUCTS[s][0]}"><b>{PRODUCTS[s][1]}</b><span>{PRODUCTS[s][3]}</span></a>' for s in PRODUCTS if PRODUCTS[s][2] == key) + '</div>'
        for key, name, _ in PILLARS)
    build_row = f'<a class="dd-build" href="#/{DEVELOPERS[0]}" data-route="{DEVELOPERS[0]}"><b>{DEVELOPERS[1]}</b><span>{DEVELOPERS[2]}</span></a>'
    sol = ''.join(f'<a href="#/{r}" data-route="{r}"><b>{n}</b><span>{l}</span></a>' for r, n, l, _, _ in SOLUTIONS.values())
    return (
        '<li class="dd dd-static"><button type="button" class="dd-btn" aria-expanded="false" aria-controls="dd-platform" data-group="platform">Platform</button>'
        f'<div class="dd-panel dd-wide" id="dd-platform"><div class="dd-grid">{plat}</div><div class="dd-foot"><span class="dd-note">One sign-in for every product.</span><a class="dd-all" href="#/platform" data-route="platform">See Always Platform</a></div></div></li>'
        '<li class="dd"><button type="button" class="dd-btn" aria-expanded="false" aria-controls="dd-solutions" data-group="solutions">Solutions</button>'
        f'<div class="dd-panel" id="dd-solutions"><div class="dd-list">{sol}</div></div></li>'
        f'<li><a href="#/{DEVELOPERS[0]}" data-route="{DEVELOPERS[0]}">{DEVELOPERS[1]}</a></li>'
        '<li><a href="#/stories" data-route="stories">Stories</a></li>'
        '<li><a href="#/docs/introduction" data-route="docs">Docs</a></li>'
        '<li><a href="#/about" data-route="about">About</a></li>'
    )


PRODUCT_ROUTES = [v[0] for v in PRODUCTS.values()] + ['platform', 'agents']
SOLUTION_ROUTES = [v[0] for v in SOLUTIONS.values()]


def footer_cols():
    plat = ''.join(f'<a href="#/{v[0]}">{v[1]}</a>' for v in PRODUCTS.values())
    sol = ''.join(f'<a href="#/{v[0]}">{v[1]}</a>' for v in SOLUTIONS.values())
    dev = '<a href="#/developers">Overview</a><a href="#/docs/api">API</a><a href="#/docs/sdk">SDK</a><a href="#/docs/mcp">MCP connector</a><a href="#/docs/webhooks">Webhooks</a><a href="https://github.com/alwaysfoundation">GitHub</a>'
    return (f'<div><h2>Platform</h2>{plat}</div>'
            f'<div><h2>Solutions</h2>{sol}</div>'
            f'<div><h2>Developers</h2>{dev}</div>'
            '<div><h2>Foundation</h2><a href="#/about">About</a><a href="#/stories">Stories</a><a href="#/events">Events</a><a href="#/research">Research</a><a href="#/brand">Brand</a><a href="#/faq">FAQs</a></div>'
            '<div><h2>Help</h2><a href="#/contact">Contact us</a><a href="#/docs/introduction">Docs</a><a href="#/claim">Claim your church</a><a href="#/docs/privacy">Privacy</a></div>')


# ---------------------------------------------------------------- Product pages

def _feats(items):
    return '<div class="pg-feats">' + ''.join(f'<div class="pg-feat rv"><h3>{t}</h3><p>{d}</p></div>' for t, d in items) + '</div>'


def _works_with(slugs):
    return '<div class="pd-with">' + ''.join(product_link(s) for s in slugs) + '</div>'


def product_page(slug, intro, feats, works_with, extra='', status=None, primary=('Join Always', '#/join'), secondary=None, feats_title='What you get', statement=None):
    route, name, pillar, line, who = PRODUCTS[slug]
    badge = f'<p class="pd-status">{status}</p>' if status else ''
    sec = f'<a class="btn btn-ghost" href="{secondary[1]}">{secondary[0]}</a>' if secondary else ''
    stmt = f'<section class="sec pd-statement"><div class="wrap"><p class="rv">{statement}</p></div></section>' if statement else ''
    return f'''<section class="page-hero pd-hero"><div class="wrap pd-split">
  <div><p class="pl-kick">Always Platform: {PILLAR_NAME[pillar]}</p>
  <h1>{name}</h1>
  <p class="pd-line">{line}</p>
  <p>{intro}</p>{badge}
  <div class="pg-cta"><a class="btn btn-peach" href="{primary[1]}">{primary[0]}</a>{sec}</div></div>
  {mock(slug, 'mk-lg')}
</div></section>
{stmt}
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
  <div class="pbt rv" aria-hidden="true"><div class="pbt-card" style="--b:#6B4FA0;--ink:#3A2A5C"><div class="pbt-top"><span></span><b>Your youth group</b></div><p>Tonight I said yes</p><i></i><i></i><em>Count me in</em></div><div class="pbt-card" style="--b:#C2562E;--ink:#5A2412"><div class="pbt-top"><span></span><b>Your street team</b></div><p>Want to know more?</p><i></i><i></i><em>Stay in touch</em></div><div class="pbt-card" style="--b:#1F6F78;--ink:#0F3A3F"><div class="pbt-top"><span></span><b>Your tour</b></div><p>Find a church near you</p><i></i><i></i><em>Take my next step</em></div></div>
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
    secondary=('Read the guide', '#/docs/senders'),
    statement='Every yes deserves a next step, in your name.')

CONNECT_EXTRA = f'''<section class="sec pg-sec pg-sage"><div class="wrap">
  <div class="cx-pair">
    <div class="cx rv">{mock('agents')}<h3>Follow up without the admin</h3><p>Agents draft welcome messages, reminders and records for your team. A person approves every step, and young people's details never go near AI.</p><span class="cx-note">In pilot with the foundation team</span></div>
    <a class="cx cx-link rv" href="#/reports">{mock('reports')}<h3>See the fruit with Always Reports</h3><p>Every introduction and welcome flows into a monthly report for your board and funders, with totals only.</p><span class="cx-note">Explore Always Reports</span></a>
  </div>
</div></section>'''

REPORTS_EXTRA = '''<section class="sec pg-sec pg-green"><div class="wrap rp-defs">
  <h2 class="pg-h rv">The same four numbers, every month</h2>
  <div class="rp-row rv"><div><b>Responded</b><span>Said yes, and agreed to be contacted.</span></div><div><b>Introduced</b><span>Passed to a verified church or ministry.</span></div><div><b>Contacted</b><span>A real person got in touch.</span></div><div><b>Part of a church family</b><span>Told us themselves, a few months on.</span></div></div>
</div></section>'''

REPORTS_PAGE = product_page('reports',
    'Answer to donors, a foundation or a denomination? Always Reports writes your report each month from what already happened in Always Pages and Always Connect. Nothing extra to enter.',
    [('Written for you', 'A clear monthly report, ready for your board and funders.'),
     ('Totals only', 'No names. Small numbers are hidden so no one can be identified.'),
     ('Your words', "Use your funder's titles and the outcomes they care about."),
     ('Download or share', 'PDF, spreadsheet, or a link you can switch off.'),
     ('Across events and campuses', 'One report, or one for each event, tour or campus.'),
     ('Across a network', 'Denominations and networks can see combined totals across their churches.')],
    ['pages', 'connect', 'compliance'],
    extra=REPORTS_EXTRA,
    secondary=("See what's in a report", '#/docs/results'),
    statement='Show the fruit, without showing the people.')

CONNECT_PAGE = product_page('connect',
    'When someone says yes to Jesus, Always Connect helps them find a next step near home, with a real person reaching out, and your team follows up together.',
    [('The directory', '3,937 churches and ministries mapped across Australia, each able to claim its page.'),
     ('Verified churches', 'We check with each church\'s denomination or network before anyone is introduced.'),
     ('A safe handoff', 'The person chooses their next step and sees who will reach out before anything is shared.'),
     ('Your team inbox', 'Accept or pass introductions from any phone, and keep walking with people.'),
     ('Next steps beyond church', 'People exploring faith can choose Alpha. Others may need a youth group or a care team.'),
     ('No one dropped', 'If no one nearby can help, the Always care team reaches out.')],
    ['pages', 'app', 'reports'],
    extra=CONNECT_EXTRA,
    secondary=('Claim your church', '#/claim'),
    statement='So no one walks alone.')

# ---------------------------------------------------------------- Solution pages

def solution_page(slug, outcomes, cta=('Talk to us', '#/join')):
    route, name, line, uses, story = SOLUTIONS[slug]
    story_html = ''
    if story:
        story_html = f'''<section class="sec pd-statement sl-story-sec"><div class="wrap">
  <p class="sl-story-k rv">{story[0]}</p><p class="rv">{story[1]}</p>
  <div class="sl-story-cta rv"><a class="btn btn-ghost-dark" href="#/stories">Read the stories</a></div>
</div></section>'''
    rows = ''.join(f'<div class="sl-row rv"><h3>{t}</h3><p>{d}</p></div>' for t, d in outcomes)
    return f'''<section class="page-hero pd-hero"><div class="wrap pd-split">
  <div><p class="pl-kick">Solutions</p>
  <h1>{for_name(name)}</h1>
  <p>{line}</p>
  <div class="pg-cta"><a class="btn btn-peach" href="{cta[1]}">{cta[0]}</a></div></div>
  {mock(uses[0], 'mk-lg')}
</div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">What you can do</h2>
  <div class="sl-rows sl-rows-{len(outcomes)}">{rows}</div>
</div></section>
<section class="sec pg-sec pg-sage"><div class="wrap">
  <h2 class="pg-h rv">Products you'll use</h2>
  <div class="bento bento-even bento-{len(uses)}">{''.join(bento_tile(s) for s in uses)}</div>
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
], cta=('For developers', '#/developers'))

# ---------------------------------------------------------------- Platform overview

PLATFORM_OVERVIEW = f'''<section class="page-hero pf-hero"><div class="wrap pf-split">
  <div><p class="pl-kick">Always Platform</p>
  <h1>Five products. One sign-in. Shared freely.</h1>
  <p>The open-source technology behind every Always product. Your team signs in once and uses whichever tools your ministry needs.</p>
  <div class="pg-cta"><a class="btn btn-peach" href="#/join">Join Always</a><a class="btn btn-ghost" href="#/developers">For developers</a></div></div>
  {switcher()}
</div></section>
<section class="sec pd-statement"><div class="wrap"><p class="rv">Built once. Shared with every church and ministry.</p></div></section>
<section class="sec pg-sec pf-products"><div class="wrap">
  <h2 class="pg-h rv">The products</h2>
  <p class="pg-lead rv">Equip, support and connect ministries, with agents to help with follow-up and admin wherever they're needed.</p>
  {product_bento()}
  {developers_band()}
</div></section>
<section class="sec pg-sec solutions-home"><div class="wrap">
  <h2 class="pg-h rv">Who it's for</h2>
  {solutions_grid()}
</div></section>
<section class="sec pg-sec pg-sage"><div class="wrap">
  <h2 class="pg-h rv">What never changes</h2>
  <div class="pl-never">{''.join(f'<div class="rv"><b>{t}</b><span>{d}</span></div>' for t, d in [('Free for churches', 'Larger ministries contribute according to their size.'), ('Open', 'Every line is public, to check and build on.'), ('Permission first', 'Nothing about a person moves without their yes.'), ('Kept in Australia', "People's details stay here."), ('Safe for young people', 'No AI and no sharing for anyone under 18.'), ('People decide', 'Agents help with the work. People make the calls.')])}</div>
</div></section>'''

CSS = MOCK_CSS + '''
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

.pd-brand { display: grid; grid-template-columns: minmax(0, .9fr) minmax(0, 1.1fr); gap: 48px; align-items: center; }
.pd-brand .pg-h, .pd-brand .pg-lead { color: var(--cream); } .pd-brand .pg-lead { color: var(--on-green); }
.pbt { display: flex; justify-content: center; align-items: center; }
.pbt-card { width: 190px; flex: none; background: #FFFDF8; border-radius: 22px; padding: 16px; display: grid; gap: 9px; box-shadow: 0 30px 50px -26px rgba(0,0,0,.55); }
.pbt-card:nth-child(1) { transform: rotate(-6deg) translate(18px, 14px); }
.pbt-card:nth-child(2) { position: relative; z-index: 1; transform: translateY(-10px); }
.pbt-card:nth-child(3) { transform: rotate(6deg) translate(-18px, 14px); }
.pbt-top { display: flex; align-items: center; gap: 7px; } .pbt-top span { width: 18px; height: 18px; border-radius: 6px; background: var(--b); } .pbt-top b { font: 700 11px/1 var(--head); color: var(--ink); }
.pd-brand .pbt-card p { margin: 2px 0; font: 800 16px/1.15 var(--head); color: var(--ink); max-width: none; }
.pbt-card i { height: 28px; border-radius: 9px; border: 1.5px solid #E7E1DA; }
.pbt-card em { font: 700 11px/1 var(--head); font-style: normal; text-align: center; padding: 10px; border-radius: 999px; background: var(--b); color: #fff; }
@media (max-width: 1100px) { .pbt-card { width: 160px; } }
@media (max-width: 520px) { .pbt-card { width: 128px; padding: 12px; } .pd-brand .pbt-card p { font-size: 13px; } .pbt-card:nth-child(1) { transform: rotate(-6deg) translate(26px, 12px); } .pbt-card:nth-child(3) { transform: rotate(6deg) translate(-26px, 12px); } }
.pd-brand-mock { justify-self: center; width: min(300px, 100%); background: #FFFDF8; border-radius: 28px; padding: 22px; display: grid; gap: 12px; box-shadow: 0 30px 60px -24px rgba(0,0,0,.45); }
.pbm-top { display: flex; align-items: center; gap: 10px; } .pbm-logo { width: 30px; height: 30px; border-radius: 9px; background: #6B4FA0; }
.pbm-name { font: 700 15px/1 var(--head); color: #3A2A5C; } .pbm-h { margin: 6px 0 2px; font: 800 22px/1.15 var(--head); color: #3A2A5C; }
.pbm-in { height: 40px; border-radius: 12px; border: 1.5px solid #E2DCEC; } .pbm-btn { margin-top: 4px; padding: 13px; border-radius: 999px; background: #6B4FA0; color: #fff; font: 700 15px/1 var(--head); text-align: center; }
@media (max-width: 900px) { .pd-brand { grid-template-columns: minmax(0, 1fr); gap: 40px; } }

/* ---- Bento ---- */
.bento { display: grid; grid-template-columns: repeat(6, minmax(0, 1fr)); gap: 18px; margin-top: 44px; }
.bt { grid-column: span 2; display: grid; grid-template-rows: auto 1fr; background: var(--paper); border-radius: 28px; padding: 10px; color: inherit; text-decoration: none; box-shadow: 0 1px 0 rgba(30,42,38,.04); transition: transform .25s ease, box-shadow .25s ease; }
.bt-app, .bt-pages { grid-column: span 3; }
.bt .mk { min-height: 250px; }
.bt-body { padding: 20px 18px 16px; display: grid; align-content: start; gap: 8px; }
.bt h3 { margin: 0; font: 800 23px/1.15 var(--head); letter-spacing: -0.02em; color: var(--green); }
.bt p { margin: 0; font-size: 15.5px; line-height: 1.5; color: var(--soft); max-width: 44ch; }
.bt-pill { justify-self: start; font: 700 12px/1 var(--head); padding: 6px 10px; border-radius: 999px; background: var(--sage-2); color: var(--green); }
.btp-equip { background: var(--peach-soft); color: var(--clay); } .btp-agents { background: #E9E4F1; color: #4E3F73; } .btp-connect { background: #EFE5D1; color: #6E5520; } .btp-build { background: #DCE7E2; color: var(--green-deep); }
.bt:hover, .bt:focus-visible { transform: translateY(-3px); box-shadow: 0 26px 50px -30px rgba(20,53,47,.45); }
.bt:hover .mk-card, .bt:focus-visible .mk-card { transform: translateY(-3px); }
.mk-card { transition: transform .35s ease; }
@media (max-width: 1000px) { .bento { grid-template-columns: 1fr 1fr; } .bt, .bt-app, .bt-pages { grid-column: auto; } .bento > .bt-connect:last-child { grid-column: span 2; } }
@media (max-width: 640px) { .bento { grid-template-columns: 1fr; } .bento > .bt-connect:last-child { grid-column: auto; } .bt .mk { min-height: 210px; } }
.heart .bento { margin-top: 48px; }

/* ---- Developers band and Connect pair ---- */
.dev-band { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 32px; align-items: center; margin-top: 18px; padding: 14px 14px 14px 36px; border-radius: 28px; background: var(--green-deep); color: var(--on-green); text-decoration: none; }
.dev-band h3 { margin: 8px 0 8px; font: 800 26px/1.15 var(--head); color: var(--cream); letter-spacing: -0.02em; }
.dev-band p { margin: 0; max-width: 40ch; font-size: 16px; line-height: 1.55; } .dev-band .bt-k { color: var(--peach); }
.dev-band .mk { min-height: 220px; } .dev-band:hover h3, .dev-band:focus-visible h3 { text-decoration: underline; text-decoration-color: var(--peach); text-underline-offset: 6px; }
.cx-pair { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 18px; }
.cx { background: var(--paper); border-radius: 28px; padding: 10px 10px 26px; }
.cx h3 { margin: 22px 18px 8px; font: 800 24px/1.15 var(--head); letter-spacing: -0.02em; color: var(--green); }
.cx p { margin: 0 18px; font-size: 16px; line-height: 1.55; color: var(--soft); max-width: 46ch; }
.cx .cm-link, .cx-note { display: inline-block; margin: 14px 18px 0; font: 700 14px/1 var(--head); color: var(--clay); }
.cx .mk { height: 250px; min-height: 0; }
@media (max-width: 800px) { .dev-band, .cx-pair { grid-template-columns: minmax(0, 1fr); } .dev-band { padding: 28px 14px 14px; } .dev-band > div { padding: 0 14px; } }

.pg-sage .pl-never div { border-top-color: rgba(27,71,64,.16); } .pg-sage .pl-never b { color: var(--green); } .pg-sage .pl-never span { color: var(--soft); }

a.cx { display: block; color: inherit; text-decoration: none; } a.cx:hover h3, a.cx:focus-visible h3 { text-decoration: underline; text-decoration-color: var(--peach); text-underline-offset: 6px; }
.rp-row { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); column-gap: 40px; margin-top: 40px; }
.rp-row > div { padding-top: 22px; border-top: 2px solid var(--peach); display: grid; gap: 8px; }
.rp-row b { font: 400 30px/1.15 'Newsreader', Georgia, serif; color: var(--cream); } .rp-row span { color: var(--on-green); font-size: 16px; line-height: 1.5; }
.rp-defs .pg-h { color: var(--cream); }
.dd-note { font-size: 13.5px; color: var(--soft); padding: 10px 0; }
@media (max-width: 900px) { .rp-row { grid-template-columns: 1fr 1fr; row-gap: 28px; } .dd-note { display: none; } }
@media (max-width: 520px) { .rp-row { grid-template-columns: 1fr; } }

/* ---- Statement (deck style) ---- */
.pd-statement { padding: 120px 0; background: var(--cream); }
.pd-statement p { margin: 0 auto; max-width: 22ch; text-align: center; font: 400 clamp(34px, 4.6vw, 64px)/1.12 'Newsreader', Georgia, serif; letter-spacing: -0.02em; color: var(--green); }
@media (max-width: 640px) { .pd-statement { padding: 80px 0; } }

/* ---- Product and platform heroes ---- */
.pd-split, .pf-split { display: grid; grid-template-columns: minmax(0, 1.05fr) minmax(0, .95fr); gap: 64px; align-items: center; }
.pd-hero h1 { font-size: clamp(48px, 6vw, 88px); }
@media (max-width: 960px) { .pd-split, .pf-split { grid-template-columns: minmax(0, 1fr); gap: 44px; } }
.pf-hero h1 { font-size: clamp(44px, 5.2vw, 76px); }
.sw { min-width: 0; }
.sw { background: rgba(248,243,234,.07); border-radius: 30px; padding: 14px; box-shadow: inset 0 0 0 1px rgba(248,243,234,.12), 0 40px 80px -40px rgba(0,0,0,.5); }
.sw-bar { display: flex; justify-content: space-between; padding: 6px 8px 12px; }
.sw-me { display: inline-flex; align-items: center; gap: 8px; font: 600 13px/1 var(--head); color: var(--on-green); }
.sw-me i { width: 8px; height: 8px; border-radius: 50%; background: #8FD1A9; box-shadow: 0 0 0 4px rgba(143,209,169,.18); }
.sw-tabs { display: flex; gap: 4px; overflow-x: auto; padding: 4px; border-radius: 16px; background: rgba(0,0,0,.18); scrollbar-width: none; }
.sw-tabs::-webkit-scrollbar { display: none; }
.sw-tab { flex: 1 0 auto; min-height: 40px; padding: 0 14px; border: 0; border-radius: 12px; background: transparent; color: var(--on-green); font: 700 13.5px/1 var(--head); cursor: pointer; transition: background .2s, color .2s; }
.sw-tab:hover { color: var(--cream); background: rgba(248,243,234,.06); }
.sw-tab[aria-selected="true"] { background: var(--cream); color: var(--green); }
.sw-tab:focus-visible { outline: 2px solid var(--peach); outline-offset: 2px; }
.sw-panel { margin-top: 12px; }
.sw-panel .mk { min-height: 300px; border-radius: 22px; }
.sw-panel:not([hidden]) .mk-card, .sw-panel:not([hidden]) .mk-conn { animation: swIn .45s cubic-bezier(.2,.8,.2,1); }
@keyframes swIn { from { opacity: 0; transform: translateY(10px) scale(.98); } to { opacity: 1; transform: none; } }
.page-hero .sw-line { margin: 0; padding: 16px 8px 6px; font-size: 15.5px; line-height: 1.5; color: var(--on-green); max-width: none; }
.sw-line b { color: var(--cream); font-family: var(--head); margin-right: 4px; }
.sw-line a { color: var(--peach); font-weight: 600; margin-left: 4px; white-space: nowrap; }
@media (prefers-reduced-motion: reduce) { .sw-panel .mk-card, .sw-panel .mk-conn { animation: none !important; } .bt, .mk-card { transition: none; } }

/* ---- Solutions as quiet rows ---- */
.sl-rows { --sl-ink: var(--green); --sl-soft: var(--soft); --sl-with: var(--clay); --sl-line: rgba(27,71,64,.16);
  display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); column-gap: 48px; margin-top: 40px; }
.solutions-home .sl-rows { --sl-ink: var(--cream); --sl-soft: var(--on-green); --sl-with: var(--peach); --sl-line: rgba(248,243,234,.16); }
.sl-row { display: grid; align-content: start; gap: 10px; padding: 30px 0 36px; border-top: 1px solid var(--sl-line); color: inherit; text-decoration: none; }
.sl-row h3 { margin: 0; font: 800 clamp(22px, 2vw, 26px)/1.15 var(--head); letter-spacing: -0.02em; color: var(--sl-ink); transition: color .2s; }
.sl-row p { margin: 0; font-size: 16px; line-height: 1.55; color: var(--sl-soft); max-width: 36ch; }
.sl-with { margin-top: 4px; font: 400 17px/1.4 'Newsreader', Georgia, serif; font-style: italic; color: var(--sl-with); }
.sl-row:hover h3, .sl-row:focus-visible h3 { text-decoration: underline; text-decoration-thickness: 2px; text-underline-offset: 6px; text-decoration-color: var(--sl-with); }
.sl-row:focus-visible { outline: 2px solid var(--peach); outline-offset: 6px; border-radius: 4px; }
.solutions-home .pg-h { color: var(--cream); }
@media (max-width: 1000px) { .sl-rows { grid-template-columns: 1fr 1fr; } }
@media (max-width: 640px) { .sl-rows { grid-template-columns: 1fr; } .sl-row { padding: 26px 0 30px; } }
.bento-even { grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr)); }
.bento-even .bt { grid-column: auto; }
.bento-even.bento-4 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.bento-even.bento-3 { grid-template-columns: repeat(3, minmax(0, 1fr)); }
@media (max-width: 1000px) { .bento-even.bento-3 { grid-template-columns: repeat(2, minmax(0, 1fr)); } .bento-even.bento-3 .bt:last-child { grid-column: span 2; } }
@media (max-width: 640px) { .bento-even.bento-4, .bento-even.bento-3 { grid-template-columns: 1fr; } .bento-even.bento-3 .bt:last-child { grid-column: auto; } }
.bt .mk { height: 260px; min-height: 0; }
.bt .mk > .mk-card, .bt .mk > .mk-conn { zoom: .9; }
.bt .mk-in + .mk-in { display: none; }
@media (max-width: 640px) { .bt .mk { height: 230px; } }
.sl-story-sec p.sl-story-k { font: 700 15px/1.2 var(--head); color: var(--clay); margin-bottom: 18px; letter-spacing: 0; }
.sl-story-cta { text-align: center; margin-top: 32px; }
.bt-k { font: 700 13px/1 var(--head); color: var(--clay); background: none !important; padding: 0; }
.bt-k.btp-support, .bt-k.btp-build { color: var(--green-2); } .bt-k.btp-agents { color: #5B4A86; } .bt-k.btp-connect { color: #85651F; }

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
.dd-wide { width: min(860px, 92vw); top: 84px; }
.dd-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 22px; }
.dd-foot { display: flex; justify-content: space-between; align-items: end; gap: 16px; margin-top: 12px; padding-top: 12px; border-top: 1px solid rgba(27,71,64,.1); }
.dd-panel .dd-build { margin: 0 0 0 -12px; } .dd-panel .dd-build span { max-width: 52ch; }
.dd-foot .dd-all { margin: 0 !important; border: 0; padding: 10px 12px !important; white-space: nowrap; }
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
  .dd-foot { display: grid; border: 0; padding: 0; margin: 4px 0 0; gap: 0; } .dd-panel .dd-build { margin: 0; }
}
'''

MENU_JS = '''
// Platform hero product switcher (tabs with arrow keys)
document.querySelectorAll('.sw').forEach((sw) => {
  const tabs = [...sw.querySelectorAll('.sw-tab')];
  const pick = (t, focus) => { tabs.forEach((x) => { const on = x === t; x.setAttribute('aria-selected', String(on)); x.tabIndex = on ? 0 : -1; document.getElementById(x.getAttribute('aria-controls')).hidden = !on; }); if (focus) t.focus(); t.scrollIntoView({ block: 'nearest', inline: 'nearest' }); };
  tabs.forEach((t, i) => { t.addEventListener('click', () => pick(t)); t.addEventListener('keydown', (e) => { const d = e.key === 'ArrowRight' ? 1 : e.key === 'ArrowLeft' ? -1 : 0; if (d) { e.preventDefault(); pick(tabs[(i + d + tabs.length) % tabs.length], true); } }); });
});
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
    'pages': PAGES_PAGE, 'reports': REPORTS_PAGE, 'connect': CONNECT_PAGE,
    'youth': YOUTH_PAGE, 'evangelists': EVANGELISTS_PAGE, 'networks': NETWORKS_PAGE, 'platforms': PLATFORMS_PAGE,
}
TITLES = {r: f'{n} · Always Foundation' for r, n, *_ in PRODUCTS.values()}
TITLES.update({r: f'{for_name(n)} · Always Foundation' for r, n, *_ in SOLUTIONS.values()})
TITLES['platform'] = 'Always Platform · Always Foundation'
TITLES['developers'] = 'Developers · Always Foundation'
TITLES['contact'] = 'Contact · Always Foundation'
TITLES['hello'] = "Let's stay in touch · Always Foundation"
