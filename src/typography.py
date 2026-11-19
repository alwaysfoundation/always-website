"""One type system for the whole site.

Manrope for headings, labels and numbers. Inter for reading. Newsreader only for Scripture and quotations.
Applied last, so it settles any page that drifted.
"""
import re

FONTS_URL = ('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800'
             '&family=Inter:wght@400;500;600;700'
             '&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;1,6..72,400&display=swap')

CSS = """
:root { --serif: 'Newsreader', Georgia, serif; }
html { -webkit-font-smoothing: antialiased; -moz-osx-font-smoothing: grayscale; text-rendering: optimizeLegibility; font-kerning: normal; }
body { font-family: var(--text); font-optical-sizing: auto; }
button, input, select, textarea { font-family: inherit; }
b, strong { font-weight: 700; }
:where(h1, h2, h3, h4) { font-family: var(--head); text-wrap: balance; }
:where(h1) { letter-spacing: -0.03em; }
:where(h2) { letter-spacing: -0.02em; }
:where(h3, h4) { letter-spacing: -0.01em; }
:where(p, li, dd, blockquote, figcaption) { text-wrap: pretty; }

/* Statements and success messages: headings, not quotations */
.ab-big, .pd-statement p, .cmx-big { font-family: var(--head) !important; font-weight: 700 !important; letter-spacing: -0.03em !important; line-height: 1.15 !important; }
.jn-done h2, .cf-done h3 { font-family: var(--head) !important; font-weight: 800 !important; letter-spacing: -0.025em !important; }

/* Numbers and step counters */
.cv-n, .cmx-q, .jn-aside li span, .jn-n, .pg-big, .rp-row b, .st-steps li::before, .pg-steps .pg-step span, .cm-steps li::before {
  font-family: var(--head) !important; font-weight: 800 !important; font-style: normal !important; letter-spacing: -0.03em; font-variant-numeric: tabular-nums;
}
.pg-steps .pg-step span, .cm-steps li::before { font-size: 34px !important; }

/* Ledes and captions: reading text */
.ft-dek { font-family: var(--text) !important; font-size: clamp(18px, 1.7vw, 21px) !important; line-height: 1.55 !important; font-weight: 400 !important; }
.ft-prose .ft-lead { font-family: var(--text) !important; font-size: 20px !important; line-height: 1.6 !important; font-weight: 500 !important; }
.cmx-caption, .sl-with, .hello-url { font-family: var(--text) !important; font-style: normal !important; font-weight: 500 !important; }
.cmx-caption { font-size: 17px !important; line-height: 1.55 !important; }
.sl-with { font-size: 15px !important; }

/* Scripture and quotations */
.ab-verse, .mk-verse, .br-verse, .word .verse, .sv, .case-quote, .ft-pull, .jbig p, .cs-dialog blockquote p, .pg-verse p {
  font-family: var(--serif) !important; font-weight: 400; letter-spacing: -0.005em;
}
.dd-f-k, .dd-f-l { font-weight: 600; }
"""

# Half-pixel and odd sizes, snapped to one scale.
SNAP = {'9': '10', '10.5': '11', '11.5': '12', '12.5': '13', '13.5': '14', '14.5': '15', '15.5': '16', '16.5': '17',
        '17.5': '18', '18.5': '18', '19': '20', '21': '22', '23': '24', '25': '26', '27': '28'}

_SIZE = re.compile(r'(font-size:\s*)(\d+(?:\.\d+)?)px')
_SHORT = re.compile(r'(font:\s*(?:normal\s+|italic\s+)?\d{3}\s+)(\d+(?:\.\d+)?)px')


def snap(doc: str) -> str:
    fix = lambda m: m.group(1) + SNAP.get(m.group(2), m.group(2)) + 'px'
    return _SHORT.sub(fix, _SIZE.sub(fix, doc))


def apply(doc: str) -> str:
    doc = re.sub(r'https://fonts\.googleapis\.com/css2\?family=Manrope[^"\']*', FONTS_URL, doc)
    doc = snap(doc)
    head_end = doc.index('</head>')
    style_end = doc.rindex('</style>', 0, head_end)
    return doc[:style_end] + CSS + doc[style_end:]
