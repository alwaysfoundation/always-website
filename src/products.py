"""The Always modules and solutions: one source of truth for names, positioning and pages.

Brand architecture
  Always Foundation  the member-based Christian nonprofit
  Always Platform    the open-source technology every product runs on
  Always + one word  the modules ministries switch on (never "the Always X platform")

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
    'pages':      ('respond',    'Always Respond',    'equip',   'A branded way to respond, by QR, tap, ticket or link, from the street to the altar call to online.', 'Churches, evangelists, events and ministries'),
    'compliance': ('compliance', 'Always Compliance', 'support', 'Stay lawful on privacy, child safety, charity and messaging rules, with a quarterly check-up.', 'Every ministry'),
    'reports':    ('reports',    'Always Reports',    'support', 'A monthly report for your board and funders, written for you, with totals only.', 'Ministries with boards and funders'),
    'connect':    ('connect',    'Always Connect',    'connect', 'Find a local church, hand people on safely, and follow up together.', 'Churches, ministries and events'),
}
DEVELOPERS = ('developers', 'Developers', 'The API, SDK, MCP connector, feeds and webhooks behind every Always module.')
# Old routes: agents live inside Always Connect; the developer page moved.
ALIASES = {'agents': 'connect', 'build': 'developers', 'pages': 'respond', 'claim': 'join/church', 'events': 'stories', 'research': 'stories', 'brand': 'docs/brand', 'directory': 'join/church', 'evangelists': 'ministries', 'platforms': 'networks'}

# slug: (route, menu name, one line, products used, story)
SOLUTIONS = {
    'churches':   ('churches',   'Churches',   'Welcome people near you who have said yes to Jesus, and help them grow as disciples.', ['connect', 'pages', 'reports', 'compliance'], None),
    'youth':      ('youth',      'Youth',      'Keep young people safe, stay compliant, and give every young person a safe next step.', ['compliance', 'pages', 'connect', 'reports'], ('UEN', 'A Christian gaming ministry that tried Always Platform at youth events.')),
    'ministries': ('ministries', 'Ministries', 'Events, tours, evangelists and street teams: a next step near home for everyone who responds, and the fruit to show for it.', ['pages', 'app', 'connect', 'reports'], ('Sydney Fire Evangelism', 'Street evangelists using their own branded response app.')),
    'networks':   ('networks',   'Networks',   'Denominations, networks and the tech platforms that serve them: every church ready to welcome, with totals only.', ['connect', 'reports', 'compliance'], ('Love is Our Weapon', 'Our first Always Compliance user, ready to roll it out to youth ministries and churches.')),
}

VERBS = {'app': 'Share Jesus', 'pages': 'Capture every yes', 'compliance': 'Stay lawful', 'reports': 'Show the fruit', 'connect': 'Hand people on'}
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
            f'<div class="bt-body"><span class="bt-k btv-{slug}">{VERBS[slug]}</span>'
            f'<h3>{name}</h3><p>{line}</p></div></a>')


def product_bento():
    return '<div class="bento">' + ''.join(bento_tile(s) for s in BENTO) + '</div>'




def platform_diagram():
    groups = ''.join(f'<a class="dg-mod dg-m-{s}" href="#/{PRODUCTS[s][0]}"><span class="dg-sw" aria-hidden="true"><i></i></span><b>{PRODUCTS[s][1]}</b><span>{VERBS[s]}</span></a>' for s in PRODUCTS)
    return f'''<figure class="dg rv" aria-label="How Always Platform fits together">
  <div class="dg-top"><b>Your church or ministry</b><span>Your team, your people, your brand</span></div>
  <div class="dg-mods">{groups}</div>
  <div class="dg-base"><b>Always Platform</b><ul><li>One sign-in</li><li>Shared data, with consent</li><li>Kept in Australia</li><li>Open source</li></ul></div>
  <a class="dg-dev" href="#/developers"><b>Developers</b><span>Build on the same foundation with the API, SDK and MCP connector</span></a>
</figure>'''


def developers_band():
    return (f'<a class="dev-band rv" href="#/{DEVELOPERS[0]}"><div><span class="bt-k">Underneath it all</span><h3>Build on Always Platform</h3>'
            f'<p>{DEVELOPERS[2]}</p></div>{mock("build")}</a>')


def switcher():
    """Platform hero: one sign-in, every product a tab."""
    tabs = ''.join(f'<button type="button" role="tab" class="sw-tab" id="sw-t-{s}" aria-controls="sw-p-{s}" aria-selected="{str(s == "pages").lower()}" tabindex="{0 if s == "pages" else -1}">{PRODUCTS[s][1].replace("Always ", "")}</button>' for s in BENTO)
    panels = ''.join(f'<div class="sw-panel" role="tabpanel" id="sw-p-{s}" aria-labelledby="sw-t-{s}"{"" if s == "pages" else " hidden"}>{mock(s)}<p class="sw-line"><b>{PRODUCTS[s][1]}</b> {PRODUCTS[s][3]} <a href="#/{PRODUCTS[s][0]}">Explore</a></p></div>' for s in BENTO)
    return (f'<div class="sw"><div class="sw-bar"><span class="sw-me"><i></i>Signed in to Always</span></div>'
            f'<div class="sw-tabs" role="tablist" aria-label="Always modules">{tabs}</div>{panels}</div>')


def solutions_grid(prefix='sx'):
    """Who it's for: pick an audience, see what Always does for them."""
    keys = list(SOLUTIONS)
    tabs = ''.join(
        f'<button type="button" role="tab" class="sx-tab" id="{prefix}-t-{k}" aria-controls="{prefix}-p-{k}" aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}">{SOLUTIONS[k][1]}</button>'
        for i, k in enumerate(keys))
    panels = []
    for i, k in enumerate(keys):
        route, name, line, uses, story = SOLUTIONS[k]
        mods = ''.join(f'<li><a href="#/{PRODUCTS[u][0]}"><b>{PRODUCTS[u][1]}</b><span>{VERBS[u]}</span></a></li>' for u in uses)
        story_html = f'<p class="sx-story"><b>{story[0]}</b> {story[1]}</p>' if story else ''
        panels.append(
            f'<div class="sx-panel" role="tabpanel" id="{prefix}-p-{k}" aria-labelledby="{prefix}-t-{k}"{"" if i == 0 else " hidden"}>'
            f'<div class="sx-art">{mock(uses[0])}</div>'
            f'<div class="sx-body"><h3>{name}</h3><p class="sx-line">{line}</p>'
            f'<p class="sx-k">Modules to switch on</p><ul class="sx-mods">{mods}</ul>{story_html}'
            f'<a class="btn btn-green sx-cta" href="#/{route}">See how we help</a></div></div>')
    return f'<div class="sx rv"><div class="sx-list" role="tablist" aria-orientation="vertical" aria-label="Who it\'s for">{tabs}</div><div class="sx-panels">{"".join(panels)}</div></div>'


ICON = {
    'app': '<rect x="7" y="3" width="10" height="18" rx="2.5"/><path d="M10.5 18h3"/>',
    'pages': '<rect x="4" y="4" width="6" height="6" rx="1"/><rect x="14" y="4" width="6" height="6" rx="1"/><rect x="4" y="14" width="6" height="6" rx="1"/><path d="M14 14h2v2h-2zM18 18h2v2h-2zM14 18h2M18 14h2"/>',
    'compliance': '<path d="M12 3l7 3v5c0 4.5-3 8.2-7 10-4-1.8-7-5.5-7-10V6l7-3z"/><path d="M9 12l2 2 4-4"/>',
    'reports': '<path d="M5 20V11M10 20V6M15 20v-7M20 20V9"/>',
    'connect': '<circle cx="6.5" cy="12" r="3"/><circle cx="17.5" cy="12" r="3"/><path d="M9.5 12h5"/>',
    'churches': '<path d="M12 3v4M10 5h4"/><path d="M5 21v-8l7-5 7 5v8"/><path d="M10 21v-4h4v4"/>',
    'youth': '<path d="M12 3l2.4 5 5.6.8-4 3.9.9 5.5L12 15.6 7.1 18.2l.9-5.5-4-3.9 5.6-.8z"/>',
    'ministries': '<path d="M4 8a2 2 0 002-2h12a2 2 0 002 2v8a2 2 0 00-2 2H6a2 2 0 00-2-2z"/><path d="M12 9v6"/>',
    'evangelists': '<path d="M4 10v4h3l6 4V6L7 10H4z"/><path d="M17 9a4 4 0 010 6"/>',
    'networks': '<circle cx="12" cy="5" r="2"/><circle cx="5" cy="18" r="2"/><circle cx="19" cy="18" r="2"/><path d="M11 7l-5 9M13 7l5 9M7 18h10"/>',
    'platforms': '<path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/>',
}
MENU_LINE = {
    'app': 'Share Jesus and walk with people', 'pages': 'Respond by QR, tap or link, in your name',
    'compliance': 'Stay lawful, state by state', 'reports': 'Monthly reports for funders',
    'connect': 'Hand people on to a local church',
    'churches': 'Welcome people near you', 'youth': 'Safe, compliant, welcoming',
    'ministries': 'Events, tours and street teams', 'networks': 'Denominations and tech platforms',
}


def _icon(k):
    return f'<span class="dd-ic dd-ic-{k}" aria-hidden="true"><svg viewBox="0 0 24 24">{ICON[k]}</svg></span>'


def menu_html():
    """Platform and Solutions drop-downs for the main menu."""
    plat = '<p class="dd-h">Modules</p><div class="dd-mods">' + ''.join(
        f'<a href="#/{PRODUCTS[s][0]}" data-route="{PRODUCTS[s][0]}">{_icon(s)}<span class="dd-tx"><b>{PRODUCTS[s][1]}</b><span>{MENU_LINE[s]}</span></span></a>'
        for s in PRODUCTS) + '</div>'
    feature = ('<a class="dd-feature" href="#/platform" data-route="platform"><span class="dd-f-k">Always Platform</span>'
               '<b>Five modules. One sign-in.</b><span class="dd-f-sw" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i></span>'
               '<span class="dd-f-l">See how it fits together</span></a>')
    sol = ''.join(f'<a href="#/{r}" data-route="{r}">{_icon(k)}<span class="dd-tx"><b>{n}</b><span>{MENU_LINE[k]}</span></span></a>' for k, (r, n, l, _, _) in SOLUTIONS.items())
    story = ('<a class="dd-story" href="#/sydneyfire"><span class="dd-story-img" aria-hidden="true"></span><span class="dd-f-k">Story</span><b>Sydney Fire Evangelism</b>'
             '<span>Street evangelists with their own branded response app.</span><span class="dd-f-l">Read the story</span></a>')
    return (
        '<li class="dd dd-static"><button type="button" class="dd-btn" aria-expanded="false" aria-controls="dd-platform" data-group="platform">Platform</button>'
        f'<div class="dd-panel dd-wide" id="dd-platform"><div class="dd-layout">{feature}<div class="dd-grid">{plat}</div></div></div></li>'
        '<li class="dd dd-static"><button type="button" class="dd-btn" aria-expanded="false" aria-controls="dd-solutions" data-group="solutions">Solutions</button>'
        f'<div class="dd-panel dd-wide dd-sol" id="dd-solutions"><div class="dd-layout dd-layout-sol"><div class="dd-sol-main"><div class="dd-list">{sol}</div><a class="dd-sol-foot" href="#/contact">Not sure which fits? <b>Talk to us</b></a></div>{story}</div></div></li>'
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
    dev = '<a href="#/developers">Overview</a><a href="#/docs/api">API</a><a href="#/docs/sdk">SDK</a><a href="#/docs/mcp">MCP connector</a><a href="#/docs/webhooks">Webhooks</a>'
    return (f'<div><h2>Platform</h2>{plat}</div>'
            f'<div><h2>Solutions</h2>{sol}</div>'
            f'<div><h2>Developers</h2>{dev}</div>'
            '<div><h2>Foundation</h2><a href="#/about">About</a><a href="#/stories">Stories</a><a href="#/docs/brand">Brand</a><a href="#/faq">FAQs</a></div>'
            '<div><h2>Help</h2><a href="#/contact">Contact us</a><a href="#/docs/introduction">Docs</a><a href="#/docs/privacy">Privacy</a><a href="#/docs/terms">Terms</a></div>')


# ---------------------------------------------------------------- Product pages

def _feats(items):
    return '<div class="pg-feats">' + ''.join(f'<div class="pg-feat rv"><h3>{t}</h3><p>{d}</p></div>' for t, d in items) + '</div>'


def _works_with(slugs):
    return '<div class="pd-with">' + ''.join(product_link(s) for s in slugs) + '</div>'


def product_page(slug, intro, feats, works_with, extra='', status=None, primary=('Join Always', '#/join'), secondary=None, feats_title='What you get', statement=None, feats_html=None):
    route, name, pillar, line, who = PRODUCTS[slug]
    badge = f'<p class="pd-status">{status}</p>' if status else ''
    sec = f'<a class="btn btn-ghost" href="{secondary[1]}">{secondary[0]}</a>' if secondary else ''
    stmt = f'<section class="sec pd-statement"><div class="wrap"><p class="rv">{statement}</p></div></section>' if statement else ''
    return f'''<section class="page-hero pd-hero"><div class="wrap pd-split">
  <div><p class="pl-kick">A module of Always Platform</p>
  <h1>{name}</h1>
  <p class="pd-line">{line}</p>
  <p>{intro}</p>{badge}
  <div class="pg-cta"><a class="btn btn-peach" href="{primary[1]}">{primary[0]}</a>{sec}</div></div>
  {mock(slug, 'mk-lg')}
</div></section>
{stmt}
{feats_html or f'''<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">{feats_title}</h2>
  {_feats(feats)}
</div></section>'''}
{extra}
<section class="sec pg-sec pg-sage"><div class="wrap">
  <h2 class="pg-h rv">Works with</h2>
  <p class="pg-lead rv">Every Always module runs on Always Platform, with one sign-in for your team.</p>
  {_works_with(works_with)}
</div></section>'''


PAGES_BRAND = '''<section class="sec pg-sec pg-green"><div class="wrap pd-brand">
  <div class="rv"><h2 class="pg-h">Your name. Your look. Your people.</h2>
  <p class="pg-lead">Every page carries your logo, colours and words, on your own link. People meet your ministry, not ours. We stay in the background.</p></div>
  <div class="pbt rv" aria-hidden="true"><div class="pbt-card" style="--b:#6B4FA0;--ink:#3A2A5C"><div class="pbt-top"><span></span><b>Your youth group</b></div><p>Tonight I said yes</p><i></i><i></i><em>Count me in</em></div><div class="pbt-card" style="--b:#C2562E;--ink:#5A2412"><div class="pbt-top"><span></span><b>Your street team</b></div><p>Want to know more?</p><i></i><i></i><em>Stay in touch</em></div><div class="pbt-card" style="--b:#1F6F78;--ink:#0F3A3F"><div class="pbt-top"><span></span><b>Your tour</b></div><p>Find a church near you</p><i></i><i></i><em>Take my next step</em></div></div>
</div></section>'''

PAGES_PAGE = product_page('pages',
    'Wherever someone says yes to Jesus, give them a simple page that looks like you. One scan or tap, from a QR code, an NFC armband or a ticket, takes them from a moment online, on the street or in the room to a real next step.',
    [('On the street', 'A QR card or phone link so evangelists can save a contact in seconds, safely.'),
     ('At the altar call', 'Put a code on the big screen and let everyone who responds say so, then and there.'),
     ('Landing pages', 'A page for your event, campaign or video, with a clear way to respond.'),
     ('Comments and embeds', 'A link for comments and posts, or a form you embed in your own website or app.'),
     ('Online to in person', 'Every response can become a welcome from a local church or ministry, with consent.'),
     ('Safe by design', 'Consent recorded on every form. Age asked first. Live totals with no names on screen.')],
    ['connect', 'app', 'reports'],
    extra=__import__('respond').FLOW + PAGES_BRAND,
    feats_title='Wherever people respond',
    feats_html=__import__('respond').SECTION,
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
    'Answer to donors, a foundation or a denomination? Always Reports writes your report each month from what already happened in Always Respond and Always Connect. Nothing extra to enter.',
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
    [('The directory', '3,937 churches and ministries mapped across Australia, each able to join and manage its own page.'),
     ('Verified churches', 'We check with each church\'s denomination or network before anyone is introduced.'),
     ('A safe handoff', 'The person chooses their next step and sees who will reach out before anything is shared.'),
     ('Your team inbox', 'Accept or pass introductions from any phone, and keep walking with people.'),
     ('Next steps beyond church', 'People exploring faith can choose Alpha. Others may need a youth group or a care team.'),
     ('No one dropped', 'If no one nearby can help, the Always care team reaches out.')],
    ['pages', 'app', 'reports'],
    extra=__import__('respond').FLOW + CONNECT_EXTRA,
    secondary=('Join as a church', '#/join/church'),
    statement='So no one walks alone.')

# ---------------------------------------------------------------- Solution pages

def solution_page(slug, outcomes, cta=('Talk to us', '#/contact')):
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
  <h2 class="pg-h rv">Modules you'll use</h2>
  <div class="bento bento-even bento-{len(uses)}">{''.join(bento_tile(s) for s in uses)}</div>
</div></section>
{story_html}'''


YOUTH_PAGE = solution_page('youth', [
    ('Stay lawful and compliant', 'Child Safe Standards, working with children checks and privacy, with a quarterly check-up your board approves.'),
    ('Welcome young people safely', 'Age comes first. Under-15s need a parent to confirm, and young people are introduced only to verified youth partners.'),
    ('Show the fruit', 'Monthly reports for your board and funders, with totals only.'),
], cta=('Try the free compliance check-up', '#/compliance/check'))

NETWORKS_PAGE = solution_page('networks', [
    ('Ready to welcome', 'Help every church in your network join, get verified and be ready to receive people.'),
    ('See the fruit across your network', 'Combined reports across your churches, with totals only.'),
    ('Shared compliance', 'One view of privacy and child safety obligations, so every church can stay lawful with less admin.'),
    ('Build it into your platform', 'Tech platforms can add the Always Compliance check-up and a safe handoff to local churches through the open API.'),
])

# ---------------------------------------------------------------- Platform overview

PLATFORM_OVERVIEW = f'''<section class="page-hero pf-hero"><div class="wrap pf-split">
  <div><p class="pl-kick">Always Platform</p>
  <h1>Five modules. One sign-in. Shared freely.</h1>
  <p>One open-source platform with shared data and one sign-in. Your team switches on the modules your ministry needs, and developers can build on the same foundation.</p>
  <div class="pg-cta"><a class="btn btn-peach" href="#/join">Join Always</a><a class="btn btn-ghost" href="#/developers">For developers</a></div></div>
  {switcher()}
</div></section>
<section class="sec pg-sec dg-sec"><div class="wrap">
  <h2 class="pg-h rv">One platform. Switch on what you need.</h2>
  <p class="pg-lead rv">Every module runs on the same foundation, so your team signs in once and your information works together. Start with one module and add more as you grow.</p>
  {platform_diagram()}
</div></section>
{__import__('respond').FLOW}
<section class="sec pg-sec pf-products"><div class="wrap">
  <h2 class="pg-h rv">The modules</h2>
  <p class="pg-lead rv">Equip, support and connect ministries, with agents to help with follow-up and admin wherever they're needed.</p>
  {product_bento()}
  {developers_band()}
</div></section>
<section class="sec pg-sec solutions-home"><div class="wrap">
  <h2 class="pg-h rv">Who it's for</h2>
  {solutions_grid('pfx')}
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

/* ---- Platform diagram ---- */
.dg { margin: 48px 0 0; display: grid; gap: 14px; }
.dg-top { display: flex; justify-content: space-between; align-items: center; gap: 16px; padding: 20px 26px; border-radius: 22px; background: #FFFDF8; border: 1px dashed rgba(27,71,64,.3); }
.dg-top b { font: 800 20px/1.2 var(--head); color: var(--green); } .dg-top span { color: var(--soft); font-size: 15px; }
.dg-mods { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 12px; padding: 14px; border-radius: 26px; background: var(--sage); }
.dg-m-app, .dg-m-pages { box-shadow: inset 0 3px 0 var(--peach), 0 14px 28px -24px rgba(20,53,47,.5); } .dg-m-compliance, .dg-m-reports { box-shadow: inset 0 3px 0 var(--green-2), 0 14px 28px -24px rgba(20,53,47,.5); } .dg-m-connect { box-shadow: inset 0 3px 0 #C9A55A, 0 14px 28px -24px rgba(20,53,47,.5); }
.dg-group { display: grid; gap: 10px; align-content: start; padding: 14px; border-radius: 24px; background: var(--peach-soft); }
.dg-support { background: var(--sage); } .dg-connect { background: #EFE5D1; }
.dg-pillar { font: 700 13px/1 var(--head); color: var(--clay); padding: 4px 6px 0; }
.dg-support .dg-pillar { color: var(--green-2); } .dg-connect .dg-pillar { color: #85651F; }
.dg-row { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px, 1fr)); gap: 10px; }
.dg-mod { position: relative; display: grid; gap: 6px; padding: 18px 18px 20px; border-radius: 18px; background: #FFFDF8; color: inherit; text-decoration: none; box-shadow: 0 14px 28px -24px rgba(20,53,47,.5); transition: transform .2s ease; }
.dg-mod b { font: 800 18px/1.2 var(--head); color: var(--green); padding-right: 40px; } .dg-mod > span:last-child { font-size: 14.5px; color: var(--soft); }
.dg-mod:hover, .dg-mod:focus-visible { transform: translateY(-2px); }
.dg-sw { position: absolute; top: 18px; right: 16px; width: 32px; height: 18px; border-radius: 99px; background: var(--green); }
.dg-sw i { position: absolute; top: 3px; right: 3px; width: 12px; height: 12px; border-radius: 50%; background: var(--cream); }
.dg-base { display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 12px 24px; padding: 24px 28px; border-radius: 22px; background: var(--green); color: var(--cream); }
.dg-base b { font: 800 22px/1 var(--head); letter-spacing: -0.02em; }
.dg-base ul { list-style: none; margin: 0; padding: 0; display: flex; flex-wrap: wrap; gap: 8px 28px; }
.dg-base li { font-size: 15px; color: var(--on-green); padding-left: 16px; position: relative; } .dg-base li::before { content: ''; position: absolute; left: 0; top: .55em; width: 6px; height: 6px; border-radius: 50%; background: var(--peach); }
.dg-dev { display: flex; gap: 16px; align-items: baseline; padding: 16px 28px; border-radius: 18px; background: var(--green-deep); color: var(--on-green); text-decoration: none; }
.dg-dev b { color: var(--cream); font: 800 16px/1 var(--head); } .dg-dev span { font-size: 14.5px; }
.dg-dev:hover b, .dg-dev:focus-visible b { text-decoration: underline; text-decoration-color: var(--peach); text-underline-offset: 5px; }
@media (max-width: 1000px) { .dg-mods { grid-template-columns: repeat(2, minmax(0, 1fr)); } .dg-m-connect { grid-column: span 2; } }
@media (max-width: 900px) { .dg-top { flex-direction: column; align-items: start; gap: 4px; } .dg-dev { flex-direction: column; gap: 6px; } }

/* ---- Who it's for: explorer ---- */
.sx { display: grid; grid-template-columns: minmax(0, .8fr) minmax(0, 1.2fr); gap: 48px; margin-top: 48px; align-items: start; }
.sx-list { display: grid; gap: 2px; position: sticky; top: 110px; }
.sx-tab { position: relative; text-align: left; background: none; border: 0; padding: 14px 0 14px 22px; color: var(--cream); opacity: .5; font: 800 clamp(20px, 2.1vw, 28px)/1.15 var(--head); letter-spacing: -0.02em; cursor: pointer; transition: opacity .2s, transform .25s cubic-bezier(.2,.8,.2,1); }
.sx-tab::before { content: ''; position: absolute; left: 0; top: 50%; width: 3px; height: 0; border-radius: 3px; background: var(--peach); transform: translateY(-50%); opacity: 0; transition: height .25s cubic-bezier(.2,.8,.2,1), opacity .2s; }
.sx-tab:hover { opacity: .85; }
.sx-tab[aria-selected="true"] { opacity: 1; transform: translateX(4px); } .sx-tab[aria-selected="true"]::before { height: 70%; opacity: 1; }
.sx-tab:focus-visible { outline: 2px solid var(--peach); outline-offset: 4px; border-radius: 6px; }
.sx-panel { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); background: #FFFDF8; border-radius: 30px; overflow: hidden; box-shadow: 0 40px 80px -40px rgba(0,0,0,.55); }
.sx-panel[hidden] { display: none; }
.sx-panel:not([hidden]) { animation: sxIn .45s cubic-bezier(.2,.8,.2,1); }
@keyframes sxIn { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: none; } }
.sx-art .mk { height: 100%; min-height: 420px; border-radius: 0; }
.sx-body { padding: 34px 32px 32px; display: grid; align-content: start; gap: 10px; }
.sx-body h3 { margin: 0; font: 800 28px/1.1 var(--head); letter-spacing: -0.02em; color: var(--green); }
.sx-line { margin: 0; font-size: 16.5px; line-height: 1.55; color: var(--soft); }
.sx-k { margin: 14px 0 0; font: 700 12.5px/1 var(--head); color: var(--clay); }
.sx-mods { list-style: none; margin: 0; padding: 0; display: grid; }
.sx-mods a { display: flex; justify-content: space-between; gap: 12px; padding: 11px 0; border-top: 1px solid var(--line); color: inherit; text-decoration: none; }
.sx-mods b { font: 700 15.5px/1.3 var(--head); color: var(--green); } .sx-mods span { font-size: 14px; color: var(--muted); text-align: right; }
.sx-mods a:hover b, .sx-mods a:focus-visible b { text-decoration: underline; text-decoration-color: var(--peach); text-underline-offset: 4px; }
.sx-story { margin: 8px 0 0; padding: 14px 16px; border-radius: 16px; background: var(--sage-2); font-size: 14.5px; line-height: 1.5; color: var(--soft); }
.sx-story b { display: block; color: var(--green); font-family: var(--head); margin-bottom: 2px; }
.sx-cta { justify-self: start; margin-top: 14px; }
@media (max-width: 1100px) { .sx-panel { grid-template-columns: minmax(0, 1fr); } .sx-art .mk { min-height: 260px; } }
@media (max-width: 860px) {
  .sx { grid-template-columns: minmax(0, 1fr); gap: 24px; }
  .sx-list { position: static; display: flex; overflow-x: auto; gap: 22px; padding-bottom: 6px; scrollbar-width: none; border-bottom: 1px solid rgba(248,243,234,.16); }
  .sx-list::-webkit-scrollbar { display: none; }
  .sx-tab { flex: none; padding: 10px 0 14px; font-size: 18px; white-space: nowrap; }
  .sx-tab::before { left: 0; right: 0; top: auto; bottom: -1px; width: 0; height: 3px; transform: none; transition: width .25s; }
  .sx-tab[aria-selected="true"] { transform: none; } .sx-tab[aria-selected="true"]::before { width: 100%; height: 3px; }
  .sx-body { padding: 26px 22px 24px; }
}
@media (prefers-reduced-motion: reduce) { .sx-panel:not([hidden]) { animation: none; } .sx-tab, .sx-tab::before { transition: none; } }

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
.bt-k.btv-compliance, .bt-k.btv-reports { color: var(--green-2); } .bt-k.btv-connect { color: #85651F; }

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
  .dd-panel a { margin: 0; padding: 6px 0; } .dd-panel a b { color: var(--cream); font-size: 17px; } .dd-panel a span { display: none; } .dd-panel a .dd-tx { display: block; } .dd-panel a .dd-tx > span, .dd-panel a .dd-ic { display: none; } .dd-panel a.dd-feature, .dd-panel a.dd-story, .dd-panel .dd-h { display: none; }
  .dd-all { border: 0; padding: 8px 0 !important; color: var(--peach) !important; }
  .dd-foot { display: grid; border: 0; padding: 0; margin: 4px 0 0; gap: 0; } .dd-panel .dd-build { margin: 0; }
}

/* ---- Menu drop-downs, refined ---- */
@media (min-width: 901px) {
  .dd-panel { display: block; visibility: hidden; opacity: 0; transform: translate(-50%, 8px); transition: opacity .18s ease, transform .22s cubic-bezier(.2,.8,.2,1), visibility 0s .22s; padding: 14px; border-radius: 26px; box-shadow: 0 40px 80px -30px rgba(10,30,26,.55), 0 0 0 1px rgba(27,71,64,.06); }
  .dd-panel.open { visibility: visible; opacity: 1; transform: translate(-50%, 0); transition: opacity .18s ease, transform .22s cubic-bezier(.2,.8,.2,1); }
  .dd-wide { width: min(980px, 94vw); }
  .dd-sol { width: min(860px, 94vw); }
  .dd-layout { display: grid; grid-template-columns: 250px minmax(0, 1fr); gap: 14px; }
  .dd-layout-sol { grid-template-columns: minmax(0, 1fr) 250px; }
  .dd-grid { display: block; padding: 10px 8px; }
  .dd-mods { display: grid; grid-template-columns: 1fr 1fr; gap: 2px 8px; }
  .dd-wide:not(.dd-sol) { width: min(820px, 94vw); }
  .dd-list { display: grid; grid-template-columns: 1fr 1fr; gap: 2px 8px; padding: 8px; align-content: start; }
  .dd-feature, .dd-story { display: grid !important; align-content: start; gap: 10px !important; margin: 0 !important; padding: 22px !important; border-radius: 20px !important; background: var(--green) !important; color: var(--cream) !important; }
  .dd-story { background: var(--green-deep) !important; }
  .dd-f-k { font: 700 12px/1 var(--head); color: var(--peach) !important; font-size: 12px !important; }
  .dd-feature b, .dd-story b { font: 800 21px/1.15 var(--head) !important; color: var(--cream) !important; letter-spacing: -0.01em; }
  .dd-story > span:not(.dd-f-k):not(.dd-f-l) { color: var(--on-green) !important; font-size: 14px !important; line-height: 1.45; }
  .dd-f-sw { display: flex; gap: 6px; margin-top: 4px; }
  .dd-f-sw i { width: 26px; height: 14px; border-radius: 99px; background: rgba(248,243,234,.18); position: relative; }
  .dd-f-sw i::after { content: ''; position: absolute; top: 2px; left: 2px; width: 10px; height: 10px; border-radius: 50%; background: var(--cream); transition: left .25s cubic-bezier(.2,.8,.2,1), background-color .25s; }
  .dd-panel.open .dd-f-sw i { background: var(--peach); transition: background-color .25s; }
  .dd-panel.open .dd-f-sw i::after { left: 14px; }
  .dd-panel.open .dd-f-sw i:nth-child(2), .dd-panel.open .dd-f-sw i:nth-child(2)::after { transition-delay: .06s; }
  .dd-panel.open .dd-f-sw i:nth-child(3), .dd-panel.open .dd-f-sw i:nth-child(3)::after { transition-delay: .12s; }
  .dd-panel.open .dd-f-sw i:nth-child(4), .dd-panel.open .dd-f-sw i:nth-child(4)::after { transition-delay: .18s; }
  .dd-panel.open .dd-f-sw i:nth-child(5), .dd-panel.open .dd-f-sw i:nth-child(5)::after { transition-delay: .24s; }
  .dd-f-l { margin-top: auto; padding-top: 18px; font: 700 14px/1 var(--head); color: var(--peach) !important; font-size: 14px !important; }
  .dd-feature:hover .dd-f-l, .dd-story:hover .dd-f-l, .dd-feature:focus-visible .dd-f-l, .dd-story:focus-visible .dd-f-l { text-decoration: underline; text-underline-offset: 4px; }
  .dd-h { padding: 4px 10px 6px; margin: 0; }
  .dd-mods a, .dd-col a, .dd-list a { display: flex !important; gap: 12px !important; align-items: flex-start; padding: 10px !important; margin: 0 !important; border-radius: 14px !important; }
  .dd-tx { display: grid; gap: 2px; }
  .dd-tx b { font: 700 15px/1.25 var(--head); color: var(--green); }
  .dd-tx span { font-size: 13px; line-height: 1.4; color: var(--soft); }
  .dd-ic { flex: none; display: grid; place-items: center; width: 36px; height: 36px; border-radius: 11px; background: var(--peach-soft); color: var(--clay); transition: transform .2s cubic-bezier(.2,.8,.2,1); }
  .dd-ic-compliance, .dd-ic-reports { background: var(--sage); color: var(--green); }
  .dd-ic-connect { background: #EFE5D1; color: #85651F; }
  .dd-list .dd-ic { background: var(--sage-2); color: var(--green); }
  .dd-ic svg { width: 20px; height: 20px; fill: none; stroke: currentColor; stroke-width: 1.7; stroke-linecap: round; stroke-linejoin: round; }
  .dd-mods a:hover .dd-ic, .dd-mods a:focus-visible .dd-ic, .dd-col a:hover .dd-ic, .dd-list a:hover .dd-ic, .dd-col a:focus-visible .dd-ic, .dd-list a:focus-visible .dd-ic { transform: scale(1.08) rotate(-3deg); }
  .dd-mods a:hover, .dd-mods a:focus-visible, .dd-mods a[aria-current="page"], .dd-col a:hover, .dd-list a:hover, .dd-col a:focus-visible, .dd-list a:focus-visible, .dd-col a[aria-current="page"], .dd-list a[aria-current="page"] { background: var(--cream) !important; }
}
@media (max-width: 900px) {
  .dd-mods { display: grid; gap: 2px; } .dd-mods a { display: block; padding: 6px 0; text-decoration: none; }
  .dd-feature, .dd-story, .dd-ic { display: none !important; }
  .dd-tx { display: block; } .dd-tx span { display: none; }
  .dd-tx b { color: var(--cream); font-size: 17px; }
  .dd-list { display: grid; gap: 2px; }
}
@media (prefers-reduced-motion: reduce) { .dd-panel, .dd-f-sw i, .dd-f-sw i::after, .dd-ic { transition: none !important; } }
'''

MENU_JS = '''
// Who it's for: vertical tabs, arrow keys move between audiences
document.querySelectorAll('.sx').forEach((sx) => {
  const tabs = [...sx.querySelectorAll('.sx-tab')];
  const pick = (t, focus) => { tabs.forEach((x) => { const on = x === t; x.setAttribute('aria-selected', String(on)); x.tabIndex = on ? 0 : -1; document.getElementById(x.getAttribute('aria-controls')).hidden = !on; }); if (focus) t.focus(); if (matchMedia('(max-width: 860px)').matches) t.scrollIntoView({ block: 'nearest', inline: 'center', behavior: 'smooth' }); };
  tabs.forEach((t, i) => { t.addEventListener('click', () => pick(t)); t.addEventListener('keydown', (e) => { const d = ['ArrowDown', 'ArrowRight'].includes(e.key) ? 1 : ['ArrowUp', 'ArrowLeft'].includes(e.key) ? -1 : 0; if (d) { e.preventDefault(); pick(tabs[(i + d + tabs.length) % tabs.length], true); } }); });
});
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
    'respond': PAGES_PAGE, 'reports': REPORTS_PAGE, 'connect': CONNECT_PAGE,
    'youth': YOUTH_PAGE, 'networks': NETWORKS_PAGE,
}
TITLES = {r: f'{n} · Always Foundation' for r, n, *_ in PRODUCTS.values()}
TITLES.update({r: f'{for_name(n)} · Always Foundation' for r, n, *_ in SOLUTIONS.values()})
TITLES['platform'] = 'Always Platform · Always Foundation'
TITLES['developers'] = 'Developers · Always Foundation'
TITLES['contact'] = 'Contact · Always Foundation'
TITLES['join'] = 'Join Always · Always Foundation'
TITLES['hello'] = "Let's stay in touch · Always Foundation"
