"""Technical illustrations for the record linkage case study."""

INK = '#1B4740'
DEEP = '#14352F'
RULE = '#BFCFC6'
WASH = '#EDF2EC'
PAPER = '#FFFDF8'
MUTED = '#6E7F78'

_T = 'font-family="Inter, system-ui, sans-serif"'
_M = 'font-family="ui-monospace, SFMono-Regular, Menlo, monospace"'


def _cyl(cx, y, w=76, h=50):
    rx, ry = w / 2, 9
    x0, x1 = cx - rx, cx + rx
    return (f'<path d="M{x0} {y} v{h} a{rx} {ry} 0 0 0 {w} 0 v-{h}" fill="{PAPER}" stroke="{INK}" stroke-width="1.5"/>'
            f'<ellipse cx="{cx}" cy="{y}" rx="{rx}" ry="{ry}" fill="{WASH}" stroke="{INK}" stroke-width="1.5"/>'
            f'<path d="M{x0} {y + h / 2} a{rx} {ry} 0 0 0 {w} 0" fill="none" stroke="{RULE}" stroke-width="1.2"/>')


def journey():
    cols = [(95, 'Youth event', 'Responded', 'Feb'), (285, 'Course', 'Enrolled', 'Mar'),
            (475, 'Bible study', 'Reading', 'Apr'), (665, 'Local church', 'Welcomed', 'May')]
    g = [f'<svg viewBox="0 0 760 452" role="img" aria-labelledby="rxf1t" {_T}><title id="rxf1t">Four organisations each hold one record about the same person. A central linked record would exist only if linkage were built.</title>']
    g.append(f'<rect x="250" y="16" width="260" height="62" rx="6" fill="{PAPER}" stroke="{MUTED}" stroke-width="1.5" stroke-dasharray="6 5"/>')
    g.append(f'<text x="380" y="42" text-anchor="middle" font-size="15" font-weight="600" fill="{INK}">Central journey record</text>')
    g.append(f'<text x="380" y="62" text-anchor="middle" font-size="12.5" fill="{MUTED}">created only by linkage; not built</text>')
    for cx, *_ in cols:
        g.append(f'<path d="M380 78 C 380 100, {cx} 96, {cx} 120" fill="none" stroke="{MUTED}" stroke-width="1.3" stroke-dasharray="4 5"/>')
    for cx, org, step, mon in cols:
        x = cx - 82
        g.append(f'<rect x="{x}" y="120" width="164" height="206" rx="6" fill="{WASH}" stroke="{RULE}" stroke-width="1.2"/>')
        g.append(f'<text x="{cx}" y="146" text-anchor="middle" font-size="14" font-weight="600" fill="{INK}">{org}</text>')
        g.append(_cyl(cx, 166))
        g.append(f'<rect x="{x + 16}" y="248" width="132" height="62" rx="4" fill="{PAPER}" stroke="{INK}" stroke-width="1.2"/>')
        g.append(f'<text x="{x + 28}" y="270" font-size="12.5" font-weight="600" fill="{INK}">Sam</text>')
        g.append(f'<text x="{x + 28}" y="288" font-size="12" fill="{MUTED}">{step}, {mon}</text>')
        g.append(f'<text x="{x + 28}" y="302" font-size="11" fill="{MUTED}" {_M}>own record only</text>')
    g.append(f'<line x1="40" y1="372" x2="720" y2="372" stroke="{INK}" stroke-width="1.2"/>')
    for cx, _o, _s, mon in cols:
        g.append(f'<line x1="{cx}" y1="366" x2="{cx}" y2="378" stroke="{INK}" stroke-width="1.2"/>')
        g.append(f'<text x="{cx}" y="398" text-anchor="middle" font-size="12.5" fill="{MUTED}">{mon} 2026</text>')
    g.append(f'<path d="M95 350 L285 350 L475 350 L665 350" fill="none" stroke="{INK}" stroke-width="2"/>')
    for cx, *_ in cols:
        g.append(f'<circle cx="{cx}" cy="350" r="6" fill="{INK}"/>')
    g.append(f'<text x="40" y="432" font-size="12.5" fill="{MUTED}">Solid: the path Sam actually takes. Dashed: the record linkage would create.</text>')
    g.append('</svg>')
    return ''.join(g)


def _box(x, y, w, h, title, body, dark=False, mono=True, dash=False):
    fill = DEEP if dark else PAPER
    tc = PAPER if dark else INK
    bc = '#CFE0D6' if dark else MUTED
    d = ' stroke-dasharray="6 5"' if dash else ''
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="6" fill="{fill}" stroke="{INK}" stroke-width="1.5"{d}/>',
           f'<text x="{x + 14}" y="{y + 24}" font-size="12.5" font-weight="600" fill="{tc}">{title}</text>']
    for i, line in enumerate(body):
        out.append(f'<text x="{x + 14}" y="{y + 46 + i * 18}" font-size="12.5" fill="{bc}" {_M if mono else ""}>{line}</text>')
    return ''.join(out)


def _arrow(x1, y1, x2, y2, dashed=False):
    d = ' stroke-dasharray="4 4"' if dashed else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="1.5" marker-end="url(#rxa)"{d}/>'


def hmac():
    g = [f'<svg viewBox="0 0 760 500" role="img" aria-labelledby="rxf3t" {_T}><title id="rxf3t">Linkage architecture: a mobile number is normalised, transformed with HMAC-SHA256 under a key held outside the database, matched to a journey, and shown to each organisation under a different pseudonym.</title>',
         f'<defs><marker id="rxa" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{INK}"/></marker></defs>']
    g.append(_box(20, 40, 160, 76, 'Input, with consent', ['0412 345 678']))
    g.append(_box(205, 40, 160, 76, 'Normalise', ['+61412345678']))
    g.append(_box(390, 40, 170, 76, 'Keyed hash', ['HMAC-SHA256', '(LINK_KEY, number)'], dark=True))
    g.append(_box(585, 40, 155, 76, 'Fingerprint', ['9f3c&#8230;e1a7']))
    g.append(_arrow(180, 78, 203, 78) + _arrow(365, 78, 388, 78) + _arrow(560, 78, 583, 78))
    g.append(f'<rect x="378" y="172" width="194" height="78" rx="6" fill="{WASH}" stroke="{INK}" stroke-width="1.5" stroke-dasharray="2 4"/>')
    g.append(f'<text x="392" y="196" font-size="12.5" font-weight="600" fill="{INK}">Key management service</text>')
    g.append(f'<text x="392" y="218" font-size="12" fill="{MUTED}" {_M}>LINK_KEY</text><text x="392" y="236" font-size="12" fill="{MUTED}" {_M}>ORG_CODE_KEY</text>')
    g.append(f'<line x1="475" y1="172" x2="475" y2="118" stroke="{INK}" stroke-width="1.3" stroke-dasharray="2 4"/>')
    g.append(f'<line x1="475" y1="250" x2="475" y2="310" stroke="{INK}" stroke-width="1.3" stroke-dasharray="2 4"/>')
    g.append(f'<rect x="572" y="150" width="180" height="124" rx="8" fill="none" stroke="{RULE}" stroke-width="1.5" stroke-dasharray="7 5"/>')
    g.append(f'<text x="584" y="268" font-size="11.5" fill="{MUTED}">Database boundary</text>')
    g.append(_box(585, 166, 155, 80, 'Match', ['fingerprint &#8594;', 'journey j_7&#8230;']))
    g.append(_arrow(662, 116, 662, 164))
    g.append(_box(378, 312, 194, 76, 'Per-organisation pseudonym', ['HMAC(ORG_CODE_KEY,', ' journey | org)'], dark=True))
    g.append(f'<path d="M640 246 C 640 300, 600 330, 562 345" fill="none" stroke="{INK}" stroke-width="1.5" marker-end="url(#rxa)"/>')
    g.append(_box(170, 420, 190, 64, 'Course ministry sees', ['jny_Q2v&#8230;']))
    g.append(_box(410, 420, 190, 64, 'Local church sees', ['jny_8Lk&#8230;']))
    g.append(f'<text x="385" y="460" text-anchor="middle" font-size="22" fill="{INK}">&#8800;</text>')
    g.append(f'<path d="M440 388 C 420 410, 330 400, 300 418" fill="none" stroke="{INK}" stroke-width="1.5" marker-end="url(#rxa)"/>')
    g.append(_arrow(505, 388, 505, 418))
    g.append(f'<text x="20" y="200" font-size="12.5" fill="{MUTED}">Without the key, a fingerprint</text><text x="20" y="218" font-size="12.5" fill="{MUTED}">cannot be computed from a</text><text x="20" y="236" font-size="12.5" fill="{MUTED}">number or reversed into one.</text>')
    g.append(f'<text x="20" y="330" font-size="12.5" fill="{MUTED}">Two organisations comparing</text><text x="20" y="348" font-size="12.5" fill="{MUTED}">pseudonyms cannot tell they</text><text x="20" y="366" font-size="12.5" fill="{MUTED}">hold the same person.</text>')
    g.append('</svg>')
    return ''.join(g)


def _mark(cx, cy, n):
    return (f'<circle cx="{cx}" cy="{cy}" r="12" fill="{DEEP}"/>'
            f'<text x="{cx}" y="{cy + 4.5}" text-anchor="middle" font-size="12.5" font-weight="700" fill="{PAPER}">{n}</text>')


def trust():
    g = [f'<svg viewBox="0 0 760 400" role="img" aria-labelledby="rxf5t" {_T}><title id="rxf5t">Institutional trust boundary: partner organisations send encoded data into the linkage service; the database and the key custody zone sit inside it; outputs are pseudonyms and aggregates. Numbered markers show where each threat applies.</title>',
         f'<defs><marker id="rxb" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{INK}"/></marker></defs>']
    g.append(f'<rect x="16" y="44" width="186" height="296" rx="8" fill="{WASH}" stroke="{RULE}" stroke-width="1.2"/>')
    g.append(f'<text x="30" y="70" font-size="13" font-weight="600" fill="{INK}">Partner organisations</text>')
    for i, t in enumerate(['Response pages', 'Church inboxes', 'Partner systems']):
        y = 92 + i * 74
        g.append(f'<rect x="30" y="{y}" width="158" height="52" rx="5" fill="{PAPER}" stroke="{INK}" stroke-width="1.2"/><text x="44" y="{y + 31}" font-size="12.5" fill="{INK}">{t}</text>')
    g.append(f'<rect x="236" y="20" width="300" height="344" rx="10" fill="none" stroke="{INK}" stroke-width="1.8" stroke-dasharray="9 6"/>')
    g.append(f'<rect x="250" y="8" width="208" height="22" fill="#FBF7EE"/><text x="258" y="24" font-size="13" font-weight="600" fill="{INK}">Linkage service (Always)</text>')
    g.append(f'<rect x="258" y="52" width="256" height="128" rx="6" fill="{PAPER}" stroke="{INK}" stroke-width="1.5"/>')
    g.append(f'<text x="274" y="78" font-size="13" font-weight="600" fill="{INK}">Database</text>')
    for i, t in enumerate(['Fingerprints', 'Journeys and milestones', 'Audit log of every view']):
        g.append(f'<text x="274" y="{104 + i * 22}" font-size="12.5" fill="{MUTED}">{t}</text>')
    g.append(f'<rect x="258" y="204" width="256" height="136" rx="6" fill="{DEEP}"/>')
    g.append(f'<rect x="264" y="210" width="244" height="124" rx="4" fill="none" stroke="#CFE0D6" stroke-width="1" stroke-dasharray="3 4"/>')
    g.append(f'<text x="278" y="236" font-size="13" font-weight="600" fill="{PAPER}">Key custody</text><text x="364" y="236" font-size="12" fill="#CFE0D6">outside the database</text>')
    g.append(f'<text x="278" y="264" font-size="12.5" fill="#CFE0D6" {_M}>LINK_KEY</text><text x="278" y="286" font-size="12.5" fill="#CFE0D6" {_M}>ORG_CODE_KEY</text>')
    g.append(f'<text x="278" y="316" font-size="12" fill="#CFE0D6">Least privilege; access logged</text>')
    g.append(f'<rect x="570" y="44" width="174" height="296" rx="8" fill="{WASH}" stroke="{RULE}" stroke-width="1.2"/>')
    g.append(f'<text x="584" y="70" font-size="13" font-weight="600" fill="{INK}">Outputs</text>')
    g.append(f'<rect x="584" y="92" width="146" height="96" rx="5" fill="{PAPER}" stroke="{INK}" stroke-width="1.2"/>')
    for i, t in enumerate(['Pseudonyms and', 'milestones, to each', 'organisation']):
        g.append(f'<text x="596" y="{118 + i * 18}" font-size="12.5" fill="{INK}">{t}</text>')
    g.append(f'<rect x="584" y="212" width="146" height="96" rx="5" fill="{PAPER}" stroke="{INK}" stroke-width="1.2"/>')
    for i, t in enumerate(['Aggregates for', 'funders; groups of', 'under 10 withheld']):
        g.append(f'<text x="596" y="{238 + i * 18}" font-size="12.5" fill="{INK}">{t}</text>')
    g.append(f'<line x1="202" y1="192" x2="234" y2="192" stroke="{INK}" stroke-width="1.5" marker-end="url(#rxb)"/>')
    g.append(f'<line x1="538" y1="192" x2="568" y2="192" stroke="{INK}" stroke-width="1.5" marker-end="url(#rxb)"/>')
    g.append(_mark(500, 66, 1) + _mark(500, 220, 2) + _mark(236, 300, 3) + _mark(716, 324, 4) + _mark(536, 30, 5))
    g.append('</svg>')
    return ''.join(g)
