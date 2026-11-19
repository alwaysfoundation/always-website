"""The Developers area: the API, SDK, MCP connector, feeds and webhooks under every Always module."""
from html import escape

SNIPPETS = [
    ('api', 'API', 'REST, OpenAPI 3.1, hosted in Sydney', 'docs/api', 'API=https://api.alwaysfoundation.org\n\n# Churches near Parramatta\ncurl $API/v1/directory?q=parramatta\n\n# The open compliance register\ncurl $API/v1/compliance/register'),
    ('sdk', 'SDK', 'TypeScript, for any app or site', 'docs/sdk', "import { AlwaysClient } from '@always/sdk';\n\nconst always = new AlwaysClient();\nconst { items } = await always.directory.search({\n  q: 'parramatta', kind: 'church',\n});"),
    ('mcp', 'MCP', 'For Claude and other AI assistants', 'docs/mcp', '# Add as a custom connector\nhttps://api.alwaysfoundation.org/mcp\n\n# Tools: find_churches, verify_church,\n#        list_events, how_always_works'),
    ('webhooks', 'Webhooks', 'Signed CloudEvents, ids only', 'docs/webhooks', "import { verifyWebhook } from '@always/sdk';\n\nconst ok = await verifyWebhook({\n  secret, body, timestamp, signature,\n});"),
]

WAYS = [
    ('The API', 'Send responses, receive introductions, manage a church page and read the church feed. Scoped tokens, shown once, revocable.', 'docs/api', 'API reference'),
    ('The SDK', 'A TypeScript client, a drop-in response card, the compliance check-up and guardrails that fail closed.', 'docs/sdk', 'SDK guide'),
    ('The MCP connector', 'Let AI assistants find churches, check verification and list events, using public information only.', 'docs/mcp', 'Connect an assistant'),
]

BUILD = [
    ('Church feed and finder', 'Verified churches near any postcode, for your website, app or map.', 'docs/feed'),
    ('Responses and handoff', 'Pass people to a verified local church, with consent that travels with them.', 'docs/standard'),
    ('Compliance infrastructure', 'The open register, change alerts and an embeddable check-up.', 'docs/compliance-platforms'),
    ('Webhooks', 'Hear about introductions, handoffs and rule changes as they happen.', 'docs/webhooks'),
    ('Response pages and embeds', 'Branded response cards and pages you drop into your own site.', 'docs/senders'),
    ('Scripture', 'The Bible in your app through YouVersion.', 'docs/youversion'),
]

RULES = [
    ('Consent travels with the data', 'Every send, share and sync checks it first, and fails closed.'),
    ('Young people first', 'Age is asked first. No AI and no sharing for anyone under 18.'),
    ('Kept in Australia', "People's details are stored and processed here."),
    ('Nothing personal in messages', 'No personal details in logs, webhooks, emails or texts.'),
    ('Open source', 'Code under Apache 2.0, the standard open, so no one is locked in.'),
    ('Free for churches', 'Partner platforms and larger ministries contribute according to their size.'),
]


def _code_card(code):
    return f'<div class="mk mk-build dv-code" aria-hidden="true"><div class="mk-card mk-code"><div class="mk-dots"><i></i><i></i><i></i></div><code>{escape(code)}</code></div></div>'


def _switcher():
    tabs = ''.join(f'<button type="button" role="tab" class="sw-tab" id="dv-t-{k}" aria-controls="dv-p-{k}" aria-selected="{str(i == 0).lower()}" tabindex="{0 if i == 0 else -1}">{n}</button>' for i, (k, n, _, _, _) in enumerate(SNIPPETS))
    panels = ''.join(f'<div class="sw-panel" role="tabpanel" id="dv-p-{k}" aria-labelledby="dv-t-{k}"{"" if i == 0 else " hidden"}>{_code_card(code)}<p class="sw-line"><b>{n}</b> {line}. <a href="#/{doc}">Read the docs</a></p></div>' for i, (k, n, line, doc, code) in enumerate(SNIPPETS))
    return f'<div class="sw"><div class="sw-bar"><span class="sw-me"><i></i>api.alwaysfoundation.org</span></div><div class="sw-tabs" role="tablist" aria-label="Ways to build">{tabs}</div>{panels}</div>'


PAGE = f'''<section class="page-hero pf-hero"><div class="wrap pf-split">
  <div><p class="pl-kick">Developers</p>
  <h1>Build on Always Platform.</h1>
  <p>The same open-source API, SDK and AI connector every Always module runs on. Free for churches and ministries, and open to the platforms that serve them.</p>
  <div class="pg-cta"><a class="btn btn-peach" href="#/docs/api">Read the docs</a><a class="btn btn-ghost" href="#/join/platform">Register as a platform</a></div></div>
  {_switcher()}
</div></section>
<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">Three ways in</h2>
  <div class="sl-rows dv-ways">{''.join(f'<a class="sl-row rv" href="#/{d}"><h3>{t}</h3><p>{p}</p><span class="sl-with">{l}</span></a>' for t, p, d, l in WAYS)}</div>
</div></section>
<section class="sec pd-statement"><div class="wrap"><p class="rv">Open by default. Built for the Church.</p></div></section>
<section class="sec pg-sec pg-sage"><div class="wrap">
  <h2 class="pg-h rv">What you can build</h2>
  <div class="sl-rows">{''.join(f'<a class="sl-row rv" href="#/{d}"><h3>{t}</h3><p>{p}</p></a>' for t, p, d in BUILD)}</div>
</div></section>
<section class="sec pg-sec solutions-home"><div class="wrap">
  <h2 class="pg-h rv">Rules every integration follows</h2>
  <div class="sl-rows">{''.join(f'<div class="sl-row rv"><h3>{t}</h3><p>{p}</p></div>' for t, p in RULES)}</div>
</div></section>
<section class="sec pg-sec"><div class="wrap sl-end">
  <h2 class="pg-h rv">Building for churches or ministries?</h2>
  <p class="pg-lead rv">Tell us what you're making. We'll help you get started and keep it safe for the people it serves.</p>
  <div class="pg-cta rv"><a class="btn btn-peach" href="#/contact/developer">Talk to us</a><a class="btn btn-green" href="#/docs/introduction">Browse the docs</a></div>
</div></section>'''

CSS = '''
.dv-code { min-height: 300px; border-radius: 22px; }
.dv-code .mk-card { width: min(440px, 100%); }
.dv-code code { font-size: 12.5px; overflow-x: auto; }
.dv-code .mk-card { min-width: 0; }
@media (max-width: 640px) { .dv-code { padding: 18px 12px; min-height: 240px; } .dv-code code { font-size: 11px; } }
.solutions-home .sl-row h3 { color: var(--cream); }
'''
