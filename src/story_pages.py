import re

STORIES = {
    'uen': {
        'slug': 'uen', 'title': 'UEN · Always Foundation',
        'dek': 'A Christian gaming ministry that meets young Australians where they play, and was our founding design partner.',
        'glance': [('Ministry', 'UEN, the Universal eSports Network'), ('Founder', 'Jake Wilson'), ('Role', 'Founding design partner'), ('Uses', 'Always Respond and Always Connect')],
        'cta': ('#/connect', 'See Always Connect'), 'link': ('#/youth', 'For youth ministries'),
    },
    'tgh': {
        'slug': 'globalharvest', 'title': 'The Global Harvest · Always Foundation',
        'dek': 'An Australian disciple-making network, with a shared way to ask about baptism and their training a tap away in Always Sent.',
        'glance': [('Network', 'The Global Harvest'), ('Focus', 'Everyday believers making disciples'), ('Training', 'The 4 Fields, the 3 Circles, the 15 Second Testimony'), ('With Always', 'Baptism requests and training in Always Sent')],
        'cta': ('#/app', 'See Always Sent'), 'link': ('https://theglobalharvest.com', 'Visit The Global Harvest'),
    },
    'needgod': {
        'slug': 'needgod', 'title': 'NeedGod.net · Always Foundation',
        'dek': 'Street evangelists in Brisbane and online, with their free training in Always Sent and a church near home for whoever says yes.',
        'glance': [('Ministry', 'NeedGod.net'), ('Where', 'King George Square, Brisbane, and online'), ('Library', 'More than 2,000 videos'), ('With Always', 'Training in Always Sent, and a next step near home')],
        'cta': ('#/app', 'See Always Sent'), 'link': ('https://needgod.net', 'Visit NeedGod.net'),
    },
    'rejoice': {
        'slug': 'rejoice', 'title': 'Rejoice · Always Foundation',
        'dek': 'An Australian Christian technology company using Always Safety and Always Reports across its consumer apps.',
        'glance': [('Company', 'Rejoice'), ('Builds', 'Apps for churches, creators and families'), ('Uses', 'Always Safety and Always Reports'), ('Role', 'Contributor to Always Platform')],
        'cta': ('#/compliance', 'See Always Safety'), 'link': ('#/reports', 'See Always Reports'),
    },
    'journeys': {
        'slug': 'journeys', 'title': 'Journeys across ministries · Always Foundation',
        'dek': 'How Always Reports links one person&rsquo;s steps across ministries, only with their yes, so no one is lost in between.',
        'glance': [('Module', 'Always Reports'), ('Approach', 'Privacy-preserving record linkage'), ('Who', 'Adults who choose it'), ('Shared', 'Steps and months, never notes'), ('Code', 'Open source'), ('Pilot', 'Six months, live')],
        'cta': ('#/docs/journeys', 'Read how journeys work'), 'link': ('#/reports', 'See Always Reports'),
    },
}


MORE = {
 "uen": "<h2>How it works at an event</h2><ol><li>A QR code on the big screens and at the stage invites anyone who said yes to Jesus to take a next step.</li><li>Age comes first. Young people only go to a youth partner, with a parent&rsquo;s okay where needed.</li><li>They choose what would help, like finding a church or a youth group nearby, and agree to be connected.</li><li>A UEN leader checks each introduction before anything is shared, then a local church or youth partner reaches out.</li></ol>\n<h2>What UEN gets</h2><ul><li>Response pages in UEN&rsquo;s own colours and words.</li><li>A clear picture after every event, with totals only, for the team and supporters.</li><li>The same safety rules for young people at every event, which can&rsquo;t be switched off.</li></ul>",
 "tgh": "<h2>About their training</h2><ul><li><b>The 4 Fields</b>, their online course on finding people open to the Gospel, sharing it, discipling new believers and gathering them into simple churches.</li><li><b>The 3 Circles</b>, a simple drawing for explaining the Gospel in everyday conversations.</li><li><b>The 15 Second Testimony</b>, a short way to tell what Jesus has done for you.</li></ul>\n<h2>Why it matters</h2><p>Baptism is a joyful step of following Jesus, and many people who are ready don&rsquo;t know who to ask. A shared, consented way to ask means no one is left wondering, and the church or ministry they choose can walk with them from there.</p>",
 "needgod": "<h2>What you&rsquo;ll find in Always Sent</h2><ul><li><b>The Gospel script</b> they use in open-air conversations.</li><li><b>The questions</b> that help someone think about where they stand with God.</li><li><b>Analogies</b> that make the Gospel clear and memorable.</li><li><b>The live stream</b>, to watch real conversations and learn.</li></ul>\n<h2>Why we feature them</h2><p>Many Christians want to share their faith and don&rsquo;t know how to start. Watching others do it, and learning a clear way to explain the Gospel, builds confidence. Always Sent puts that training next to everything else an everyday evangelist needs, from their own story to a next step for whoever says yes.</p>",
 "rejoice": "<h2>What shared tools save</h2><ul><li><b>Always Safety</b> gives a check-up every quarter on privacy, child safety and messaging rules, with plain updates when the law changes, so each app doesn&rsquo;t need its own compliance work.</li><li><b>Always Reports</b> shows spiritual impact, like responses and next steps, with totals only, so no one can be identified.</li></ul>\n<h2>Why it matters</h2><p>Every Christian app has the same hard parts: keeping people safe, following the law and showing real fruit. Solved once and shared, those parts get done well for everyone, and small teams can spend their time on the people they serve.</p>",
 "journeys": """
<h2>How it works, step by step</h2>
<ol>
<li><b>Sam says yes.</b> At an event, Sam responds on an Always page and ticks a separate box: &ldquo;The ministries that help me can see my steps.&rdquo; It&rsquo;s never pre-ticked.</li>
<li><b>A fingerprint, not a file.</b> Always turns Sam&rsquo;s mobile number into a fingerprint using a secret key. The journey holds no name and no number, only that fingerprint.</li>
<li><b>Sam takes another step.</b> Weeks later Sam signs up for a course through another ministry, with the same number and the same yes. The fingerprints match, so Always adds the step to Sam&rsquo;s journey.</li>
<li><b>Each ministry gets its own code.</b> The event team and the course see different codes for Sam, so they can&rsquo;t compare lists to find Sam.</li>
<li><b>Everyone on the journey sees how it&rsquo;s going.</b> The event team sees that Sam did a course and joined a church in May. The church sees where Sam has come from. No notes, no names of other ministries.</li>
<li><b>Funders see detailed totals.</b> Results by event, city, month and pathway, with any group under 10 hidden.</li>
<li><b>Sam can change their mind.</b> One tap to withdraw, and the journey is unlinked straight away.</li>
</ol>

<h2>Three groups say yes</h2>
<p>Journeys only work when everyone involved chooses them.</p>
<ul>
<li><b>The person.</b> Their own yes, separate from being introduced to a church, adults only, and withdrawable at any time.</li>
<li><b>Churches and ministries.</b> They partner with Always, switch on journeys and agree to the terms: use the steps only to care for the person, never pass codes on or combine them, and honour a withdrawal straight away.</li>
<li><b>Evangelists.</b> People sharing Jesus with Always Sent pass on a friend&rsquo;s response through Always, so the journey starts from the very first yes.</li>
</ul>

<h2>Why protecting privacy makes it work</h2>
<ul>
<li><b>People say yes more freely</b> when they know their faith won&rsquo;t be passed around.</li>
<li><b>Ministries keep their independence.</b> Each keeps its own records. No one hands over a database, and no one has to.</li>
<li><b>There&rsquo;s less to lose.</b> The journey holds fingerprints and months, not a shared list of names and numbers that could leak.</li>
<li><b>It stays on the right side of the law.</b> Faith is sensitive information under the Australian Privacy Principles. Sharing only steps, only with consent, is what the law expects.</li>
<li><b>Care gets better.</b> The church can meet Sam where they are, and the event team learns whether its follow-up worked.</li>
</ul>

<h2>Why open source is a safety feature</h2>
<p>It can seem safer to keep the workings secret. For this kind of technology, the opposite is true.</p>
<ul>
<li><b>The protection is the key, not the secrecy.</b> Like the encryption that protects online banking, the method can be public because no one can match records without the secret key. The key, the data and every access token stay private.</li>
<li><b>Claims can be checked, not just trusted.</b> A church&rsquo;s tech volunteer, an independent reviewer or a regulator can read exactly what is collected and who sees what. There are no hidden uses.</li>
<li><b>Problems are found sooner.</b> More eyes means flaws surface early and are fixed in the open. Anyone can report one through our security policy.</li>
<li><b>Reviews mean more.</b> An independent review can point to the exact code that runs, so its findings hold.</li>
<li><b>No one is locked in.</b> The code belongs to everyone, so churches and ministries never depend on one organisation staying around.</li>
</ul>

<h2>What you&rsquo;re trusting Always with</h2>
<p>Only Always holds the key that links journeys. The assurances behind that trust:</p>
<ul>
<li>The code is open source, as above.</li>
<li>Every view is logged in a record that can&rsquo;t be quietly changed, and staff see only what&rsquo;s needed to help.</li>
<li>Never for anyone under 18. This can&rsquo;t be switched on.</li>
<li>An independent privacy and security review before journeys open widely.</li>
<li>Board oversight of privacy and security.</li>
<li>The key is kept apart from the data, and destroying it unlinks every journey at once.</li>
</ul>

<h2>Join the pilot</h2>
<p>We&rsquo;re inviting churches, ministries and evangelists to run journeys live with us for six months, then publish the results the way health researchers do.</p>
<ul>
<li><b>What we&rsquo;ll measure:</b> how many people choose to link, how accurate the matches are, how many find a church and how long it takes, and what churches found helpful.</li>
<li><b>What we&rsquo;ll publish:</b> totals and lessons learned, with small groups hidden, so the whole church in Australia can learn from it.</li>
<li><b>Safeguards from day one:</b> adults only, only with their yes, and anyone can withdraw at any time.</li>
</ul>
<p><a href="#/pprl">Read the research paper</a>, or email <a href="mailto:hello@alwaysfoundation.org?subject=Journeys%20pilot%20expression%20of%20interest">hello@alwaysfoundation.org</a> by 10 December 2026 to join the pilot.</p>
""",
}


def _dialog(home, key):
    i = home.index(f'id="cs-{key}"')
    return home[home.rfind('<dialog', 0, i):home.index('</dialog>', i) + len('</dialog>')]


def _tile_art(home, key):
    t = home.rfind('<li class="cs-tile">', 0, home.index(f'data-cs="{key}"'))
    m = re.search(r'<div class="cs-img([^"]*)"[^>]*>(.*?)</div>\s*<div class="cs-text">', home[t:], re.S)
    cls, inner = m.group(1), m.group(2)
    img = re.search(r'<img[^>]*?src="([^"]+)"[^>]*?alt="([^"]*)"', inner)
    if img and 'jn-tile' not in cls:
        return f'<img src="{img.group(1)}" alt="{img.group(2)}" loading="lazy">'
    return f'<div class="sp-art{cls}">{inner}</div>'


def _body(dialog):
    d = re.sub(r'<button[^>]*cs-close[^>]*>.*?</button>', '', dialog, flags=re.S)
    d = re.sub(r'<img class="cs-hero"[^>]*>', '', d)
    d = re.sub(r'<div class="cs-two">.*?</div>', '', d, flags=re.S)
    d = re.sub(r'<p class="cs-name">.*?</p>', '', d, flags=re.S)
    d = re.sub(r'<h3[^>]*>.*?</h3>', '', d, flags=re.S)
    fine = re.search(r'<p class="cs-fine">(.*?)</p>', d, re.S)
    d = re.sub(r'<p class="cs-fine">.*?</p>', '', d, flags=re.S)
    d = re.sub(r'<a href="#/docs/journeys">Read how journeys work</a>', '', d)
    m = re.search(r'<div class="cs-dlg-in">(.*)</div>\s*</dialog>', d, re.S)
    body = m.group(1).strip()
    body = body.replace('<h4>', '<h2>').replace('</h4>', '</h2>')
    body = re.sub(r'<blockquote>\s*<p>(.*?)</p>\s*(?:<cite>(.*?)</cite>)?\s*</blockquote>',
                  lambda q: f'<blockquote class="ft-pull">{q.group(1)}{f"<cite>{q.group(2)}</cite>" if q.group(2) else ""}</blockquote>', body, flags=re.S)
    body = re.sub(r'<p>\s*</p>', '', body)
    return body, (fine.group(1) if fine else '')


def _page(home, key, meta):
    dialog = _dialog(home, key)
    name = re.sub(r'\s*·.*$', '', re.search(r'<p class="cs-name">(.*?)</p>', dialog).group(1))
    title = re.search(r'<h3[^>]*>(.*?)</h3>', dialog, re.S).group(1)
    body, fine = _body(dialog)
    glance = ''.join(f'<dt>{a}</dt><dd>{b}</dd>' for a, b in meta['glance'])
    ext = meta['link'][0].startswith('http')
    link = f'<a class="ft-link" href="{meta["link"][0]}"{" target=\"_blank\" rel=\"noopener\"" if ext else ""}>{meta["link"][1]}</a>'
    return f'''
<article class="ft sp-story">
<div class="ft-hero"><div class="wrap ft-hero-in">
  <p class="ft-kick"><a href="#/stories">Stories</a> <span aria-hidden="true">/</span> {name}</p>
  <h1>{title}</h1>
  <p class="ft-dek">{meta["dek"]}</p>
</div></div>
<figure class="ft-fig wrap sp-fig">{_tile_art(home, key)}{f"<figcaption>{fine}</figcaption>" if fine else ""}</figure>
<div class="wrap ft-body">
  <div class="prose ft-prose">{body}{MORE.get(key, "")}
    <h2>Find out more</h2><p><a href="#/join">Partner with Always</a> to use Always Platform with your church or ministry, or <a href="#/stories">read more stories</a>.</p>
  </div>
  <aside class="ft-side" aria-label="At a glance"><div class="ft-card">
    <h2>At a glance</h2><dl>{glance}</dl>
    <a class="btn btn-peach" href="{meta["cta"][0]}">{meta["cta"][1]}</a>{link}
  </div></aside>
</div>
</article>
'''


CSS = '''
.sp-fig img { display: block; width: 100%; height: auto; max-height: 560px; object-fit: cover; border-radius: 26px; box-shadow: 0 40px 80px -40px rgba(10,30,26,.45); }
.sp-fig .sp-art { position: relative; aspect-ratio: 16 / 7; border-radius: 26px; overflow: hidden; }
.sp-fig .sp-art.jn-tile { display: grid; place-items: center; background: radial-gradient(70% 60% at 85% 0%, rgba(232,165,119,.25), rgba(232,165,119,0) 60%), linear-gradient(160deg, #1D4C43, #12302A); }
.sp-fig .sp-art .jn-art { position: static; width: min(70%, 520px); }
.ft-card .btn { justify-content: center; text-align: center; }
.sp-story .ft-pull cite { display: block; margin-top: 10px; font: 600 15px/1.4 var(--head); font-style: normal; color: var(--soft); }
@media (max-width: 700px) { .sp-fig .sp-art { aspect-ratio: 4 / 3; } .sp-fig .sp-art .jn-art { width: 88%; } }
'''


def build(home):
    pages, titles = {}, {}
    for key, meta in STORIES.items():
        pages[meta['slug']] = _page(home, key, meta)
        titles[meta['slug']] = meta['title']
        home = re.sub(rf'<button type="button" class="cs-more" data-cs="{key}" aria-haspopup="dialog">(.*?)</button>',
                      rf'<a class="cs-more" href="#/{meta["slug"]}">\1</a>', home)
        home = home.replace(_dialog(home, key), '')
    return home, pages, titles
