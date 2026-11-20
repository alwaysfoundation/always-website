"""The Journeys initiative: privacy-preserving record linkage for journeys across ministries."""

SLUG = 'pprl'
TITLE = 'The Journeys initiative · Always Foundation'

TOC = [
    ('rp-physician', 'A physician of the soul'),
    ('rp-why', 'Why it matters'),
    ('rp-abstract', 'In short'),
    ('rp-problem', '1. The problem'),
    ('rp-options', '2. Why today’s options fail'),
    ('rp-pprl', '3. Record linkage, privately'),
    ('rp-design', '4. Our design'),
    ('rp-security', '5. Security analysis'),
    ('rp-health', '6. Lessons from Australian health'),
    ('rp-cyber', '7. The cyber threat'),
    ('rp-open', '8. Open source as assurance'),
    ('rp-pilot', '9. The pilot'),
    ('rp-limits', '10. Limitations'),
    ('rp-refs', 'Sources'),
]


def _toc():
    return ''.join(f'<button type="button" data-goto="{i}">{t}</button>' for i, t in TOC)


PAGE = '''
<article class="rp">
<div class="rp-hero"><div class="wrap rp-hero-in">
  <p class="rp-kick"><a href="#/stories">Stories</a> <span aria-hidden="true">/</span> Initiative</p>
  <h1>Linking journeys, not databases</h1>
  <p class="rp-dek">Helping churches and ministries care for people as one body, without ever sharing their databases. Built on privacy-preserving record linkage, the approach trusted in Australian health for three decades.</p>
  <p class="rp-meta">The Journeys initiative <span aria-hidden="true">&middot;</span> Always Foundation <span aria-hidden="true">&middot;</span> November 2026</p>
  <div class="rp-pilot" role="note" aria-label="Pilot">
    <span class="rp-pulse" aria-hidden="true"></span>
    <div><b>Piloting in Australia through Always Respond and Always Connect.</b>
    <span>Expressions of interest from churches and ministries close <strong>10 December 2026</strong>. Email <a href="mailto:hello@alwaysfoundation.org?subject=Journeys%20pilot%20expression%20of%20interest">hello@alwaysfoundation.org</a>.</span></div>
  </div>
  <figure class="rp-heroart" aria-hidden="true">
    <svg viewBox="0 0 1000 300" preserveAspectRatio="xMidYMid meet">
      <defs><linearGradient id="rpg" x1="0" x2="1"><stop offset="0" stop-color="#E8A577" stop-opacity=".1"/><stop offset=".6" stop-color="#E8A577"/><stop offset="1" stop-color="#F2C29E"/></linearGradient></defs>
      <path d="M60 190 C 200 70, 320 70, 390 140 S 600 230, 650 130 S 860 70, 940 150" fill="none" stroke="rgba(255,253,248,.2)" stroke-width="3" stroke-dasharray="2 12" stroke-linecap="round"/>
      <path class="rp-h-draw" d="M60 190 C 200 70, 320 70, 390 140 S 600 230, 650 130 S 860 70, 940 150" fill="none" stroke="url(#rpg)" stroke-width="5" stroke-linecap="round"/>
      <g class="rp-h-nodes">
        <circle cx="60" cy="190" r="16"/><circle cx="390" cy="140" r="16"/><circle cx="650" cy="130" r="16"/><circle cx="940" cy="150" r="20" class="rp-h-church"/>
      </g>
      <circle class="rp-h-dot" r="9" fill="#FFFDF8"><animateMotion dur="7s" repeatCount="indefinite" path="M60 190 C 200 70, 320 70, 390 140 S 600 230, 650 130 S 860 70, 940 150"/></circle>
      <g class="rp-h-text"><text x="60" y="250" text-anchor="start">Event</text><text x="390" y="200" text-anchor="middle">Course</text><text x="650" y="90" text-anchor="middle">Bible study</text><text x="940" y="215" text-anchor="end">Church</text></g>
    </svg>
  </figure>
</div></div>

<div class="wrap rp-body">
  <nav class="rp-toc" aria-label="Contents"><p>Contents</p>''' + _toc() + '''</nav>

  <div class="rp-main">
    <section id="rp-physician" class="rp-mlj">
      <p class="rp-mlj-k">Where this begins</p>
      <h2>A physician of the soul</h2>
      <p class="rp-mlj-lead">In the 1920s, one of the most promising young doctors in London was Martyn Lloyd-Jones. He trained at St Bartholomew&rsquo;s Hospital and became chief clinical assistant to Sir Thomas Horder, physician to the royal family.<sup><a data-goto="rp-refs">[10, 11]</a></sup></p>
      <p>Then, for two years, he wrestled with a call to give it up: to leave medicine and become a &lsquo;physician of the soul&rsquo;. In 1927 he did, moving to a small mission church in Aberavon, South Wales, and went on to become one of the most influential preachers of the twentieth century.<sup><a data-goto="rp-refs">[11]</a></sup> He never stopped thinking like a doctor: careful diagnosis, care for the whole person, and the long view.</p>
      <div class="rp-mlj-pair">
        <div><b>Medicine learned</b><p>A patient seen by many clinicians needs one continuous record, held with discretion and shared only with those caring for them.</p></div>
        <div><b>The church can too</b><p>Someone who meets Jesus at an event and joins a church months later deserves the same: continuity from those who care for them, confidentiality from everyone else.</p></div>
      </div>
      <p>Australian health has shown for three decades that both can be had together. The Journeys initiative brings that same discipline to the care of souls.</p>
    </section>

    <section id="rp-why" class="rp-why">
      <p class="rp-why-lead">&ldquo;Saying yes to Jesus shouldn&rsquo;t be the end of a form. It should be the beginning of a journey.&rdquo;</p>
      <div class="rp-why-grid">
        <div class="rp-why-card rp-why-a">
          <h2>The why</h2>
          <p>People rarely come to faith through one ministry. They respond at an event, try a course, read the Bible with a friend, and find a church months later. Each ministry sees only its own step, so people slip through the gaps, follow-up depends on someone remembering, and no one can tell whether a yes became a church family.</p>
        </div>
        <div class="rp-why-card rp-why-b">
          <h2>The benefits</h2>
          <ul class="rp-ben">
            <li><span class="rp-ic" aria-hidden="true"><svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c1.5-4 4.5-6 8-6s6.5 2 8 6"/></svg></span><div><b>For people</b><p>Welcomed by a church that knows their story, with their own yes, and a way to withdraw any time.</p></div></li>
            <li><span class="rp-ic" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M12 3v4M10 5h4M5 21V11l7-4 7 4v10"/><path d="M10 21v-5h4v5"/></svg></span><div><b>For churches</b><p>Know where someone has come from and meet them where they are.</p></div></li>
            <li><span class="rp-ic" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M4 12h10M10 6l6 6-6 6"/><circle cx="19" cy="12" r="2"/></svg></span><div><b>For ministries and evangelists</b><p>Learn whether the people you reached found a church, and improve your follow-up.</p></div></li>
            <li><span class="rp-ic" aria-hidden="true"><svg viewBox="0 0 24 24"><path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/></svg></span><div><b>For networks and funders</b><p>Honest totals across ministries, each person counted once, never a name.</p></div></li>
          </ul>
        </div>
        <div class="rp-why-card rp-why-c">
          <h2>The unlock</h2>
          <ul class="rp-unlock">
            <li><b>One body, many ministries.</b> Churches and ministries care for people together while each keeps its own records and independence.</li>
            <li><b>Fruit, not activity.</b> For the first time, the church can see whether hands raised became lasting connection.</li>
            <li><b>Collaboration without honeypots.</b> No central database of who responded to the Gospel is ever built.</li>
            <li><b>A shared public good.</b> Open code and an open standard any network in Australia can adopt.</li>
          </ul>
        </div>
      </div>
    </section>

    <section id="rp-abstract" class="rp-abstract">
      <h2>In short</h2>
      <p>People rarely come to faith through one ministry. They respond at an event, try a course, read the Bible with a friend and, God willing, join a local church. Each ministry keeps its own records, so no one can see the whole path, people fall through the gaps between ministries, and the church cannot tell whether a response became a lasting home. The two ways to close the gap today, pooling databases or reconciling them by hand, are respectively unsafe and impractical.</p>
      <p>The Journeys initiative is how Always Platform links one adult&rsquo;s steps across ministries using privacy-preserving record linkage (PPRL), an approach with three decades of use in Australian health research. Linkage runs only with the person&rsquo;s explicit consent, on a keyed cryptographic fingerprint of their mobile number. Ministries never exchange records, each sees a different code for the same person, only milestones and months are shared, and funders see aggregate totals with small groups withheld. We set out the design, a threat model, the trade-offs we accepted, and a six-month live pilot in Australia, run through Always Respond and Always Connect.</p>
      <dl class="rp-keys">
        <div><dt>Approach</dt><dd>Consent-based PPRL with a trusted linkage service</dd></div>
        <div><dt>Identifier</dt><dd>Normalised Australian mobile, keyed with HMAC-SHA256</dd></div>
        <div><dt>Shared</dt><dd>Milestone and month only</dd></div>
        <div><dt>Excluded</dt><dd>Anyone under 18, notes, other ministries&rsquo; names</dd></div>
      </dl>
    </section>

    <section id="rp-problem">
      <h2>1. The problem: care that breaks between ministries</h2>
      <p>Consider Sam. Sam says yes to Jesus at a youth event in February, signs up for a course run by another ministry in March, reads the Bible with a friend through a third, and is welcomed by a local church in May. Four organisations each hold a fragment. None knows the others exist in Sam&rsquo;s story.</p>
      <figure class="rp-fig rv" id="rp-fig1">
        <div class="f1">
          <div class="f1-row">
            <div class="f1-node"><b>Event</b><span>Responded, Feb</span></div>
            <div class="f1-node"><b>Course</b><span>Signed up, Mar</span></div>
            <div class="f1-node"><b>Bible study</b><span>Reading, Apr</span></div>
            <div class="f1-node f1-church"><b>Church</b><span>Welcomed, May</span></div>
          </div>
          <div class="f1-line" aria-hidden="true"><i></i></div>
          <div class="f1-states" aria-hidden="true"><span class="f1-a">Today: four disconnected records</span><span class="f1-b">With linkage: one journey, with Sam&rsquo;s yes</span></div>
        </div>
        <figcaption><b>Figure 1.</b> One person, four fragments. Without linkage each ministry sees only its own step; with consent-based linkage the steps join into one journey that every ministry on it can see by milestone and month.</figcaption>
      </figure>
      <p>The cost is pastoral and practical. Follow-up depends on someone remembering to pass a name on. The event team never learns whether Sam found a church. The church does not know Sam has already taken steps of faith. And when four ministries each report Sam, the network counts four people where there was one.</p>
    </section>

    <section id="rp-options">
      <h2>2. Why today&rsquo;s options fail</h2>
      <figure class="rp-fig rv">
        <div class="f2">
          <div class="f2-col f2-bad"><h3>Pool the databases</h3><ul><li>Every ministry sees every person</li><li>One breach exposes all of them</li><li>Hard to justify under the Australian Privacy Principles, because faith is sensitive information</li></ul></div>
          <div class="f2-col f2-bad"><h3>Reconcile by hand</h3><ul><li>Phone calls and spreadsheets</li><li>Names passed around in email</li><li>So much work it rarely happens</li></ul></div>
          <div class="f2-col f2-good"><h3>Privacy-preserving linkage</h3><ul><li>No records exchanged</li><li>Only with the person&rsquo;s yes</li><li>Only steps and months shared</li></ul></div>
        </div>
        <figcaption><b>Figure 2.</b> The two common approaches trade privacy for usefulness or usefulness for privacy. PPRL is designed to avoid that trade.</figcaption>
      </figure>
    </section>

    <section id="rp-pprl">
      <h2>3. Record linkage, privately</h2>
      <p>Record linkage identifies records that belong to the same person across separate collections. Privacy-preserving record linkage does this without the collections revealing their identifying details to one another. In the common &ldquo;trusted third party&rdquo; model, each data holder sends only an encoded identifier to a linkage unit, the unit determines which encodings match, and it returns or uses link keys rather than names.<sup><a data-goto="rp-refs">[1, 2]</a></sup></p>
      <p>Two families of encoding dominate. <b>Keyed hashing</b> applies a secret-keyed one-way function to a normalised identifier, giving exact matches only. <b>Bloom-filter encoding</b> splits identifiers such as names into fragments and sets bits in a filter, which allows approximate matches that tolerate spelling differences.<sup><a data-goto="rp-refs">[3, 5]</a></sup> Section 5 explains why Always uses the first.</p>
    </section>

    <section id="rp-design">
      <h2>4. Our design</h2>
      <p>Linkage lives inside Always Platform&rsquo;s API and database. It is used by Always Respond, which records a response and its consent, and Always Connect, which introduces the person to a church or ministry. The full implementation is open source, and the design is recorded in ADR 0012.<sup><a data-goto="rp-refs">[12]</a></sup></p>

      <figure class="rp-fig rv" id="rp-fig3">
        <ol class="f3">
          <li class="f3-s"><span class="f3-k">Input</span><code>0412 345 678</code><small>Mobile given with consent</small></li>
          <li class="f3-s"><span class="f3-k">Normalise</span><code>+61412345678</code><small>One canonical form</small></li>
          <li class="f3-s f3-key"><span class="f3-k">Fingerprint</span><code>HMAC-SHA256(LINK_KEY, &middot;)</code><small>Key held outside the database</small></li>
          <li class="f3-s"><span class="f3-k">Match</span><code>9f3c&hellip;e1a7</code><small>Same fingerprint, same journey</small></li>
          <li class="f3-s f3-key"><span class="f3-k">Per-ministry code</span><code>jny_Q2v&hellip; &ne; jny_8Lk&hellip;</code><small>HMAC(ORG_CODE_KEY, journey | ministry)</small></li>
        </ol>
        <figcaption><b>Figure 3.</b> From a mobile number to a journey. The number is normalised, fingerprinted with a secret key, matched, and then shown to each ministry under its own unrelated code. The fingerprint is never returned by any API. (Example values are illustrative.)</figcaption>
      </figure>

      <h3>4.1 Eligibility and consent</h3>
      <p>A response can be linked only if the person is an adult and has given the separate consent purpose <code>share.journey</code>, never pre-ticked, alongside but distinct from consent to be connected with a church. The API refuses the purpose for anyone under 18, and the database refuses to link without a current, unwithdrawn consent. These rules are not configurable.</p>

      <h3>4.2 Normalisation</h3>
      <p>Australian mobiles are written many ways. Before fingerprinting, the number is reduced to one canonical form, <code>+614XXXXXXXX</code>, so the same number always produces the same fingerprint. Anything that is not an Australian mobile is not linked.</p>

      <h3>4.3 The keyed fingerprint</h3>
      <p>The fingerprint is <code>HMAC-SHA256(LINK_KEY, normalised mobile)</code>, a standard keyed hash.<sup><a data-goto="rp-refs">[13]</a></sup> Without the key, the fingerprint cannot be recomputed from a number or reversed into one. <code>LINK_KEY</code> is held in the environment, separate from the database and from the key used for sign-in, so it can be rotated or destroyed without affecting anything else.</p>

      <h3>4.4 A different code for every ministry</h3>
      <p>Ministries never see the fingerprint or the internal journey id. Each sees <code>HMAC(ORG_CODE_KEY, journey id | ministry id)</code>: stable for that ministry, unrelated between ministries. Two ministries comparing their codes learn nothing.</p>

      <h3>4.5 What a ministry sees</h3>
      <p>Every ministry on the journey (the one the person responded through, and each church or ministry that welcomed them) sees the same thing: each milestone and its month, with its own steps marked. Never notes, exact dates, or the names of other ministries. Every view is written to a tamper-evident audit log.</p>
      <figure class="rp-fig rv">
        <div class="f4" role="table" aria-label="Who sees what">
          <div class="f4-r f4-h" role="row"><span role="columnheader">Party</span><span role="columnheader">Identity</span><span role="columnheader">Steps</span><span role="columnheader">Notes</span></div>
          <div class="f4-r" role="row"><span role="cell">The person</span><span role="cell" data-l="Identity" class="y">Own</span><span role="cell" data-l="Steps" class="y">All, and can withdraw</span><span role="cell" data-l="Notes">&mdash;</span></div>
          <div class="f4-r" role="row"><span role="cell">Each ministry on the journey</span><span role="cell" data-l="Identity" class="p">Its own record only</span><span role="cell" data-l="Steps" class="y">Milestone and month</span><span role="cell" data-l="Notes" class="n">Its own only</span></div>
          <div class="f4-r" role="row"><span role="cell">Always Platform</span><span role="cell" data-l="Identity" class="p">Fingerprint, keys held apart</span><span role="cell" data-l="Steps" class="y">To serve the journey</span><span role="cell" data-l="Notes" class="n">None</span></div>
          <div class="f4-r" role="row"><span role="cell">Funders and networks</span><span role="cell" data-l="Identity" class="n">None</span><span role="cell" data-l="Steps" class="p">Totals, groups under 10 withheld</span><span role="cell" data-l="Notes" class="n">None</span></div>
        </div>
        <figcaption><b>Figure 4.</b> Who sees what. Only totals leave the circle of ministries caring for the person.</figcaption>
      </figure>

      <h3>4.6 Reporting</h3>
      <p>Reports read a de-identified tally, never journeys. Funders and networks see results by event, city, month, channel and pathway, and the time it takes people to find a church. Any group of fewer than 10 people is withheld, following the de-identification principle that a journey is personal information even without a name.</p>

      <h3>4.7 Withdrawal</h3>
      <p>A person can withdraw <code>share.journey</code> at any time. The response is unlinked at once, and every view afterwards shows nothing.</p>
    </section>

    <section id="rp-security">
      <h2>5. Security analysis</h2>
      <figure class="rp-fig rv" id="rp-fig5">
        <div class="f5">
          <div class="f5-z"><h3>Sources</h3><p>Response pages, the church inbox, ministries&rsquo; systems via the API</p><ul><li>TLS in transit</li><li>Consent checked first</li></ul></div>
          <div class="f5-arrow" aria-hidden="true"><i></i></div>
          <div class="f5-z f5-core"><h3>Linkage service</h3><p>Fingerprints and journey ids in the database; <b>keys outside it</b></p><ul><li>Row-level security</li><li>Audit log of every view</li><li>Adults and consent enforced in the database</li></ul></div>
          <div class="f5-arrow" aria-hidden="true"><i></i></div>
          <div class="f5-z"><h3>Outputs</h3><p>Per-ministry codes and milestones; totals for reports</p><ul><li>No fingerprint leaves</li><li>Small groups withheld</li></ul></div>
          <div class="f5-threat" aria-hidden="true"><span>Attacker with a copy of the database</span><b>Sees fingerprints, cannot reverse them without the key</b></div>
        </div>
        <figcaption><b>Figure 5.</b> Trust zones. The design assumes the database can be stolen and keeps the keys elsewhere.</figcaption>
      </figure>

      <h3>5.1 Threat model</h3>
      <ul>
        <li><b>A curious ministry</b> tries to learn about people beyond its own care. It sees only milestones for people on journeys it is part of, under its own code.</li>
        <li><b>Colluding ministries</b> compare data. Their codes differ, so they cannot join records through Always; they can only compare what they already held.</li>
        <li><b>Database theft.</b> An attacker gets fingerprints and journey links, but not the keys, so cannot turn fingerprints back into numbers.</li>
        <li><b>A rogue insider at Always</b> is the strongest adversary, because Always holds the keys. Mitigations: least-privilege access, keys held apart from data, every view logged, open code, board oversight and an independent review.</li>
      </ul>

      <h3>5.2 The small-identifier problem</h3>
      <p>Australian mobile numbers come from a space of about a hundred million. Hashing alone would be useless: anyone could hash every number and compare. The protection comes entirely from the secret key. With it, enumeration is trivial; without it, the fingerprints are unusable. That is why key custody is the centre of the design, why the key never sits beside the data, and why the person&rsquo;s consent, not the fingerprint, is what authorises any linking.</p>

      <h3>5.3 Why not Bloom filters</h3>
      <p>Bloom-filter PPRL tolerates typos and is widely used in health linkage, but published attacks have re-identified encoded values, particularly common names, from sets of filters, including without knowledge of the encoding parameters.<sup><a data-goto="rp-refs">[5, 6]</a></sup> Approximate matching also needs more personal details, such as names and dates of birth. We chose exact matching on one identifier the person gives with consent, under a key held by a single linkage service. We accept that we will miss some true links, and we prefer that to joining two different people or holding more data.</p>

      <h3>5.4 Residual risks</h3>
      <ul>
        <li><b>Recycled numbers.</b> Telcos reissue disconnected numbers, so two people could share a number over time. Steps are shown by month and only to ministries on the journey, and anyone can withdraw.</li>
        <li><b>Shared phones.</b> A family phone could link two people. The same limits apply.</li>
        <li><b>Changed numbers.</b> A new number starts a new journey. We may later let the person add an email as a second identifier, with their yes.</li>
      </ul>
    </section>

    <section id="rp-health">
      <h2>6. Lessons from Australian health</h2>
      <p>Australia is one of the most experienced countries in the world at linking records responsibly. Health researchers have shown for decades that linkage can serve people well when it is governed carefully.</p>
      <figure class="rp-fig rv" id="rp-fig6">
        <ol class="f6">
          <li><span class="f6-y">1995</span><b>WA Data Linkage System</b><p>Established in Western Australia, now the longest-running linkage system in Australia, supporting hundreds of research projects.<sup><a data-goto="rp-refs">[1]</a></sup></p></li>
          <li><span class="f6-y">2009&ndash;12</span><b>A national network</b><p>The Population Health Research Network, under the National Collaborative Research Infrastructure Strategy, adds linkage units in every state and a Centre for Data Linkage for cross-jurisdictional research.<sup><a data-goto="rp-refs">[2]</a></sup></p></li>
          <li><span class="f6-y">2018</span><b>Tested at scale</b><p>A NSW evaluation links primary-care records from 16 general practices to tens of millions of hospital records using privacy-preserving methods.<sup><a data-goto="rp-refs">[4]</a></sup></p></li>
          <li><span class="f6-y">2018</span><b>Tested by attackers</b><p>Researchers at the Australian National University publish efficient attacks on Bloom-filter encodings, shaping safer designs.<sup><a data-goto="rp-refs">[5]</a></sup></p></li>
          <li><span class="f6-y">2022</span><b>As accurate as plain linkage</b><p>A blinded WA evaluation finds 99.3% of groupings identical between privacy-preserving and clear-text linkage.<sup><a data-goto="rp-refs">[3]</a></sup></p></li>
          <li class="f6-now"><span class="f6-y">2026</span><b>Applied to ministry</b><p>Always Platform pilots consent-based linkage for journeys across ministries.</p></li>
        </ol>
        <figcaption><b>Figure 6.</b> Three decades of Australian record linkage, from health research to ministry.</figcaption>
      </figure>
      <p>Two lessons carry over directly. First, separation of duties: the parties who hold records are not the party that links them, and the party that links does not need what is in them. Second, governance is as important as cryptography: custodians, approvals, audit and publication of methods are what earn public trust. Ministry differs in one important way. Much health research proceeds under an ethics-approved waiver of consent;<sup><a data-goto="rp-refs">[1]</a></sup> journeys proceed only with each person&rsquo;s own yes.</p>
    </section>

    <section id="rp-cyber">
      <h2>7. The cyber threat to shared infrastructure</h2>
      <p>Any system that brings ministries together becomes infrastructure, and infrastructure is a target. Australia&rsquo;s cyber agency reports that state-sponsored actors are a serious and growing threat to government, critical infrastructure and business networks.<sup><a data-goto="rp-refs">[7]</a></sup></p>
      <figure class="rp-fig rv" id="rp-fig7">
        <div class="f7">
          <div class="f7-stats">
            <div><b>1,200+</b><span>cyber incidents responded to by ASD&rsquo;s ACSC in 2024&ndash;25, up 11%</span></div>
            <div><b>190+</b><span>notifications to critical infrastructure of malicious activity, up 111%</span></div>
            <div><b>95%</b><span>of healthcare and social assistance incidents where attackers succeeded</span></div>
          </div>
          <div class="f7-bars" aria-label="People affected by major Australian breaches">
            <p class="f7-t">People affected by major Australian breaches (millions)</p>
            <div class="f7-bar" style="--w:100%"><span>MediSecure, 2024</span><i></i><b>12.9</b></div>
            <div class="f7-bar" style="--w:77.5%"><span>Optus, 2022</span><i></i><b>10</b></div>
            <div class="f7-bar" style="--w:75.2%"><span>Medibank, 2022</span><i></i><b>9.7</b></div>
          </div>
        </div>
        <figcaption><b>Figure 7.</b> The threat environment. Sources: ASD&rsquo;s Annual Cyber Threat Report 2024&ndash;25; OAIC; AAP.<sup><a data-goto="rp-refs">[7, 8, 9]</a></sup></figcaption>
      </figure>
      <p>The MediSecure breach, affecting about 12.9 million people&rsquo;s personal and health information, is the largest ever notified under the Notifiable Data Breaches scheme.<sup><a data-goto="rp-refs">[8]</a></sup> The lesson for the church is not to stop collaborating. It is to collaborate without building honeypots: collect less, share less, separate keys from data, and design every system on the assumption that it will one day be attacked. A pooled database of who responded to the Gospel, and where, would be one of the most sensitive collections in the country. PPRL lets ministries work together without anyone ever building it.</p>
    </section>

    <section id="rp-open">
      <h2>8. Open source as assurance</h2>
      <p>It can seem safer to keep the workings of a privacy system secret. For linkage the opposite is true. The protection is the key, not the obscurity of the method, just as the encryption that secures online banking is public. Publishing the code lets a church&rsquo;s volunteer, an independent reviewer or a regulator check what is collected and who sees what, lets flaws be found and fixed sooner, gives reviews something exact to test, and means no church depends on one organisation staying around. The keys, the data and every access token stay private.</p>
    </section>

    <section id="rp-pilot">
      <h2>9. The pilot</h2>
      <figure class="rp-fig rv" id="rp-fig8">
        <ol class="f8">
          <li class="f8-now"><b>Now to 10 December 2026</b><span>Expressions of interest</span></li>
          <li><b>Onboarding</b><span>Consent wording, terms, training</span></li>
          <li><b>Six months live</b><span>Through Always Respond and Always Connect</span></li>
          <li><b>Published results</b><span>Totals and lessons, small groups hidden</span></li>
        </ol>
        <figcaption><b>Figure 8.</b> Pilot timeline.</figcaption>
      </figure>
      <p>We are inviting Australian churches, ministries and evangelists to run journeys live with us for six months. Responses are taken through Always Respond, with the separate journey consent; people are welcomed through Always Connect; and outcomes are reported as totals through Always Reports.</p>
      <h3>What we will measure</h3>
      <ul>
        <li>How many people choose to link their journey.</li>
        <li>Match quality, checked against cases the person or church confirms.</li>
        <li>How many people find a church, and how long it takes.</li>
        <li>Security and privacy incidents, which we aim to keep at none, and reported openly if any occur.</li>
        <li>What churches and ministries found helpful, and what they did not.</li>
      </ul>
      <h3>Safeguards from day one</h3>
      <p>Adults only. Only with each person&rsquo;s yes, withdrawable at any time. Steps and months, never notes. Totals only beyond the ministries caring for the person. An independent privacy and security review before journeys open widely, and legal review of the consent wording.</p>
      <div class="rp-eoi">
        <div><h3>Express interest by 10 December 2026</h3><p>Tell us who you are, how people respond through your ministry, and which churches or ministries you work alongside.</p></div>
        <a class="btn btn-peach" href="mailto:hello@alwaysfoundation.org?subject=Journeys%20pilot%20expression%20of%20interest">Email hello@alwaysfoundation.org</a>
      </div>
    </section>

    <section id="rp-limits">
      <h2>10. Limitations and future work</h2>
      <ul>
        <li><b>Coverage.</b> Only steps taken through Always are counted. Ministries using other systems can connect through the API.</li>
        <li><b>Exact matching.</b> One identifier misses people who change numbers. A second identifier, such as an email the person adds, is under consideration.</li>
        <li><b>Trust in the linkage service.</b> Always holds the keys. Independent review, open code and audit reduce, but do not remove, the need for that trust.</li>
        <li><b>Contribution, not cause.</b> Journeys show what happened, not why. Fruit belongs to God; the data helps us care better.</li>
      </ul>
    </section>

    <section id="rp-refs" class="rp-refs">
      <h2>Sources</h2>
      <ol>
        <li>Hodges S, Eitelhuber T, Merchant A, Alan J. Population Data Centre Profile: the Western Australian Data Linkage Branch. <i>International Journal of Population Data Science</i>, 2020. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7477781/">PMC7477781</a></li>
        <li>Boyd JH et al. Data linkage infrastructure for cross-jurisdictional health-related research in Australia. <i>BMC Health Services Research</i> 12:480, 2012. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3579698/">PMC3579698</a></li>
        <li>A blinded evaluation of privacy preserving record linkage with Bloom filters. <i>BMC Medical Research Methodology</i> 22:22, 2022. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8761329/">PMC8761329</a></li>
        <li>Irvine K et al. Real world performance of privacy preserving record linkage. <i>International Journal of Population Data Science</i>, 2018. <a href="https://doaj.org/article/a1c61969fe8b4470884c42661e243e17">DOAJ</a></li>
        <li>Christen P, Ranbaduge T, Vatsalan D, Schnell R. Precise and fast cryptanalysis for Bloom filter based privacy-preserving record linkage. Australian National University, 2018. <a href="https://openresearch-repository.anu.edu.au/items/305e45a1-3d3a-4301-8f6c-126b3398968b">ANU Open Research</a></li>
        <li>Niedermeyer F et al. Cryptanalysis of basic Bloom filters used for privacy preserving record linkage. <i>Journal of Privacy and Confidentiality</i> 6(2), 2014. <a href="https://doaj.org/article/198c67d232af44ac94e06027d64a3928">DOAJ</a></li>
        <li>Australian Signals Directorate. Annual Cyber Threat Report 2024&ndash;25. <a href="https://www.cyber.gov.au/about-us/view-all-content/reports-and-statistics/annual-cyber-threat-report-2024-2025">cyber.gov.au</a></li>
        <li>Office of the Australian Information Commissioner. Statement on MediSecure breach, July 2024. <a href="https://oaic.gov.au/newsroom/statement-on-medisecure-breach">oaic.gov.au</a></li>
        <li>Australian Associated Press. Millions of people hit by prescription cyber attack, 2024. <a href="https://aapnews.aap.com.au/news/millions-of-people-hit-by-prescription-cyber-attack">aapnews.aap.com.au</a></li>
        <li>MLJ Trust. Meet Martyn Lloyd-Jones. <a href="https://mljtrust.org/meet-mlj/">mljtrust.org</a></li>
        <li>MLJ Trust. 10 years and 20 million downloads. <a href="https://www.mljtrust.org/blog/10-year-anniversary/">mljtrust.org</a></li>
        <li>Always Platform. ADR 0012: Journeys across ministries, and source code. <a href="https://github.com/alwaysfoundation/always-platform">github.com/alwaysfoundation/always-platform</a></li>
        <li>Krawczyk H, Bellare M, Canetti R. HMAC: Keyed-Hashing for Message Authentication. RFC 2104, IETF, 1997. <a href="https://www.rfc-editor.org/rfc/rfc2104">rfc-editor.org</a></li>
      </ol>
      <p class="rp-note">This page describes our design and is not legal advice. Prolegis Lawyers are reviewing the consent wording. Questions and corrections are welcome at <a href="mailto:hello@alwaysfoundation.org">hello@alwaysfoundation.org</a>.</p>
    </section>
  </div>
</div>
</article>
'''

CSS = r'''
/* ---- Journeys initiative ---- */
.rp-hero { background: var(--green); color: var(--cream); padding: 160px 0 56px; overflow: hidden; }
.rp-hero-in { max-width: 1040px; }
.rp-kick { font: 600 14px/1 var(--head); color: rgba(255,253,248,.7); margin: 0 0 22px; }
.rp-kick a { color: inherit; }
.rp-hero h1 { font-size: clamp(40px, 6vw, 76px); letter-spacing: -0.045em; line-height: 1; color: var(--cream); max-width: 15ch; }
.rp-dek { margin: 22px 0 0; max-width: 60ch; font-size: clamp(18px, 1.7vw, 21px); line-height: 1.55; color: rgba(255,253,248,.82); }
.rp-meta { margin: 18px 0 0; font-size: 14px; color: rgba(255,253,248,.6); }
.rp-pilot { display: flex; gap: 14px; align-items: flex-start; margin-top: 30px; padding: 18px 20px; max-width: 760px; border-radius: 18px; background: rgba(255,253,248,.08); border: 1px solid rgba(232,165,119,.45); }
.rp-pilot b { display: block; font: 700 16px/1.35 var(--head); color: var(--cream); }
.rp-pilot span { display: block; margin-top: 4px; font-size: 15px; line-height: 1.5; color: rgba(255,253,248,.82); }
.rp-pilot strong { color: #F2C29E; }
.rp-pilot a { color: #F2C29E; text-decoration: underline; text-underline-offset: 3px; }
.rp-pulse { flex: none; width: 12px; height: 12px; margin-top: 5px; border-radius: 50%; background: #E8A577; box-shadow: 0 0 0 0 rgba(232,165,119,.6); animation: rpPulse 2.4s infinite; }
@keyframes rpPulse { 70% { box-shadow: 0 0 0 12px rgba(232,165,119,0); } 100% { box-shadow: 0 0 0 0 rgba(232,165,119,0); } }
.rp-heroart { margin: 40px 0 0; }
.rp-heroart svg { display: block; width: 100%; height: auto; }
.rp-h-draw { stroke-dasharray: 1500; stroke-dashoffset: 1500; animation: rpDraw 7s linear infinite; }
@keyframes rpDraw { to { stroke-dashoffset: 0; } }
.rp-h-nodes circle { fill: #173F37; stroke: rgba(255,253,248,.7); stroke-width: 3; }
.rp-h-text text { fill: rgba(255,253,248,.78); font: 700 28px Manrope, sans-serif; }
.rp-h-nodes .rp-h-church { fill: #E8A577; stroke: #FFFDF8; }
.rp-body { display: grid; grid-template-columns: 220px minmax(0, 1fr); gap: 64px; padding-top: 64px; padding-bottom: 96px; }
.rp-toc { position: sticky; top: 96px; align-self: start; display: flex; flex-direction: column; gap: 2px; }
.rp-toc p { margin: 0 0 10px; font: 700 13px/1 var(--head); color: var(--soft); }
.rp-toc button { text-align: left; min-height: 36px; padding: 6px 10px; border: 0; border-radius: 10px; background: none; color: var(--soft); font: 500 14px/1.3 var(--text); cursor: pointer; }
.rp-toc button:hover, .rp-toc button.on { background: rgba(29,76,67,.08); color: var(--green); }
.rp-main { max-width: 760px; }
.rp-main section { scroll-margin-top: 96px; }
.rp-main section + section { margin-top: 64px; }
.rp-main h2 { font-size: clamp(26px, 3vw, 34px); letter-spacing: -0.025em; line-height: 1.15; color: var(--green); margin: 0 0 18px; }
.rp-main h3 { font-size: 19px; color: var(--green); margin: 30px 0 8px; }
.rp-main p, .rp-main li { font-size: 17px; line-height: 1.7; color: #2B3A36; }
.rp-main p { margin: 0 0 16px; }
.rp-main ul { margin: 0 0 16px; padding-left: 20px; }
.rp-main li { margin-bottom: 8px; }
.rp-main code { font-size: .88em; padding: 1px 6px; border-radius: 6px; background: rgba(29,76,67,.08); color: var(--green); }
.rp-main sup a { color: #9A4A22; font: 600 12px/1 var(--head); text-decoration: none; cursor: pointer; }
.rp-abstract { padding: 32px; border-radius: 24px; background: #fff; box-shadow: 0 1px 0 rgba(20,53,47,.08), 0 24px 48px -32px rgba(20,53,47,.35); }
.rp-keys { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px 24px; margin: 22px 0 0; padding-top: 18px; border-top: 1px solid rgba(20,53,47,.1); }
.rp-keys dt { font: 700 13px/1.2 var(--head); color: #9A4A22; }
.rp-keys dd { margin: 4px 0 0; font-size: 15px; line-height: 1.45; color: var(--green); }

.rp-fig { margin: 30px 0 34px; }
.rp-fig figcaption { margin-top: 12px; font-size: 14px; line-height: 1.55; color: var(--soft); }
.rp-fig figcaption b { color: var(--green); }

.rp-mlj { margin-bottom: 64px; }
.rp-mlj-k { margin: 0 0 10px !important; font: 700 14px/1 var(--head) !important; color: #9A4A22 !important; }
.rp-mlj h2 { font-size: clamp(32px, 4vw, 46px) !important; letter-spacing: -0.035em !important; margin-bottom: 20px !important; }
.rp-mlj-lead { font-size: 20px !important; line-height: 1.6 !important; color: var(--green) !important; }
.rp-mlj-pair { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 14px; margin: 26px 0 22px; }
.rp-mlj-pair div { padding: 22px; border-radius: 20px; background: #fff; box-shadow: 0 1px 0 rgba(20,53,47,.08), 0 20px 40px -34px rgba(20,53,47,.4); }
.rp-mlj-pair div + div { background: #14352F; }
.rp-mlj-pair b { display: block; font: 700 15px/1.2 var(--head); color: #9A4A22; margin-bottom: 6px; }
.rp-mlj-pair div + div b { color: #F2C29E; }
.rp-mlj-pair p { margin: 0 !important; font-size: 16px !important; line-height: 1.55 !important; }
.rp-mlj-pair div + div p { color: rgba(255,253,248,.88) !important; }
.rp-why { margin-bottom: 72px; }
.rp-why-lead { margin: 0 0 28px !important; font-family: var(--serif) !important; font-size: clamp(24px, 2.6vw, 32px) !important; line-height: 1.3 !important; color: var(--green) !important; max-width: 30ch; }
.rp-why-grid { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 14px; }
.rp-why-card { padding: 28px; border-radius: 24px; background: #fff; box-shadow: 0 1px 0 rgba(20,53,47,.08), 0 24px 48px -36px rgba(20,53,47,.4); }
.rp-why-card h2 { font-size: 15px !important; letter-spacing: 0 !important; color: #9A4A22 !important; margin: 0 0 12px !important; }
.rp-why-a { background: #14352F; }
.rp-why-a p { color: rgba(255,253,248,.88) !important; font-size: 18px !important; line-height: 1.6 !important; margin: 0 !important; }
.rp-why-a h2 { color: #F2C29E !important; }
.rp-why-b { grid-row: span 2; }
.rp-ben { list-style: none; margin: 0 !important; padding: 0 !important; display: grid; gap: 18px; }
.rp-ben li { display: flex; gap: 14px; margin: 0 !important; }
.rp-ben b { display: block; font: 700 16px/1.3 var(--head); color: var(--green); }
.rp-ben p { margin: 4px 0 0 !important; font-size: 15px !important; line-height: 1.55 !important; }
.rp-ic { flex: none; display: grid; place-items: center; width: 44px; height: 44px; border-radius: 14px; background: rgba(232,165,119,.18); }
.rp-ic svg { width: 22px; height: 22px; fill: none; stroke: #9A4A22; stroke-width: 1.8; stroke-linecap: round; stroke-linejoin: round; }
.rp-why-c { background: linear-gradient(160deg, #F7E7DA, #F1D3BC); }
.rp-unlock { list-style: none; margin: 0 !important; padding: 0 !important; display: grid; gap: 12px; }
.rp-unlock li { margin: 0 !important; padding-left: 18px; position: relative; font-size: 15.5px !important; line-height: 1.55 !important; }
.rp-unlock li::before { content: ''; position: absolute; left: 0; top: .6em; width: 8px; height: 8px; border-radius: 50%; background: #9A4A22; }
.rp-unlock b { color: var(--green); }

/* Figure 1 */
.f1 { position: relative; padding: 26px 22px 20px; border-radius: 22px; background: #14352F; color: var(--cream); overflow: hidden; }
.f1-row { position: relative; z-index: 1; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 12px; }
.f1-node { padding: 14px; border-radius: 14px; background: rgba(255,253,248,.06); border: 1px dashed rgba(255,253,248,.3); }
.f1-node b { display: block; font: 700 15px/1.2 var(--head); }
.f1-node span { display: block; margin-top: 4px; font-size: 13px; color: rgba(255,253,248,.7); }
.f1-line { position: relative; height: 4px; margin: 18px 6% 14px; border-radius: 4px; background: repeating-linear-gradient(90deg, rgba(255,253,248,.25) 0 8px, transparent 8px 16px); }
.f1-line i { position: absolute; inset: 0; transform-origin: left; transform: scaleX(0); border-radius: 4px; background: #E8A577; }
.f1-states { position: relative; height: 20px; font: 600 14px/20px var(--head); }
.f1-states span { position: absolute; inset: 0; transition: opacity .4s; }
.f1-b { opacity: 0; color: #F2C29E; }
.rp-fig.in .f1-line i { animation: f1Join 8s ease-in-out infinite; }
.rp-fig.in .f1-node { animation: f1Node 8s ease-in-out infinite; }
.rp-fig.in .f1-a { animation: f1A 8s ease-in-out infinite; }
.rp-fig.in .f1-b { animation: f1B 8s ease-in-out infinite; }
@keyframes f1Join { 0%, 35% { transform: scaleX(0); } 65%, 90% { transform: scaleX(1); } 100% { transform: scaleX(0); } }
@keyframes f1Node { 0%, 45% { border-style: dashed; border-color: rgba(255,253,248,.3); } 60%, 90% { border-style: solid; border-color: rgba(232,165,119,.8); } 100% { border-style: dashed; } }
@keyframes f1A { 0%, 40% { opacity: 1; } 50%, 92% { opacity: 0; } 100% { opacity: 1; } }
@keyframes f1B { 0%, 45% { opacity: 0; } 55%, 90% { opacity: 1; } 100% { opacity: 0; } }

/* Figure 2 */
.f2 { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; }
.f2-col { padding: 20px; border-radius: 18px; background: #fff; border: 1px solid rgba(20,53,47,.1); }
.f2-col h3 { margin: 0 0 10px; font-size: 17px; }
.f2-col ul { margin: 0; padding-left: 18px; }
.f2-col li { font-size: 15px; line-height: 1.5; }
.f2-bad h3 { color: #9A4A22; }
.f2-good { background: #14352F; border-color: #14352F; }
.f2-good h3, .f2-good li { color: var(--cream); }

/* Figure 3 */
.f3 { list-style: none; margin: 0; padding: 14px; border-radius: 22px; background: #14352F; }
.f3-s { position: relative; display: grid; grid-template-columns: 150px minmax(0, 1.3fr) minmax(0, 1fr); align-items: center; gap: 16px; padding: 14px 16px; border-radius: 14px; color: var(--cream); }
.f3-s + .f3-s { margin-top: 18px; }
.f3-s + .f3-s::before { content: ''; position: absolute; left: 30px; top: -16px; width: 2px; height: 14px; background: rgba(255,253,248,.3); }
.f3-k { font: 700 13px/1.2 var(--head); color: #F2C29E; }
.f3-s code { display: block; padding: 8px 10px; border-radius: 8px; background: rgba(0,0,0,.28); color: #FFFDF8; font-size: 14px; line-height: 1.4; overflow-wrap: anywhere; }
.f3-s small { font-size: 13.5px; line-height: 1.45; color: rgba(255,253,248,.72); }
.f3-key code { box-shadow: inset 0 0 0 1px rgba(232,165,119,.55); }
.rp-fig.in .f3-s { animation: f3Step 7.5s ease-in-out infinite; }
.rp-fig.in .f3-s:nth-child(2) { animation-delay: 1.2s; } .rp-fig.in .f3-s:nth-child(3) { animation-delay: 2.4s; } .rp-fig.in .f3-s:nth-child(4) { animation-delay: 3.6s; } .rp-fig.in .f3-s:nth-child(5) { animation-delay: 4.8s; }
@keyframes f3Step { 0% { background: transparent; } 5% { background: rgba(232,165,119,.2); box-shadow: inset 3px 0 0 #E8A577; } 17% { background: transparent; box-shadow: none; } 100% { background: transparent; } }

/* Figure 4 */
.f4 { border-radius: 18px; overflow: hidden; border: 1px solid rgba(20,53,47,.12); background: #fff; }
.f4-r { display: grid; grid-template-columns: 1.3fr 1fr 1fr .8fr; }
.f4-r + .f4-r { border-top: 1px solid rgba(20,53,47,.08); }
.f4-r span { padding: 12px 14px; font-size: 14.5px; line-height: 1.4; color: #2B3A36; }
.f4-h span { font: 700 13px/1.2 var(--head); color: var(--green); background: rgba(29,76,67,.06); }
.f4 .y { color: #1F5C4F; font-weight: 600; } .f4 .p { color: #8A5A1F; } .f4 .n { color: #8C9592; }

/* Figure 5 */
.f5 { position: relative; display: grid; grid-template-columns: 1fr 40px 1.2fr 40px 1fr; align-items: stretch; padding: 22px 22px 86px; border-radius: 22px; background: #F1EDE4; }
.f5-z { padding: 16px; border-radius: 16px; background: #fff; border: 1px solid rgba(20,53,47,.1); }
.f5-z h3 { margin: 0 0 6px; font-size: 16px; }
.f5-z p { font-size: 14px; line-height: 1.45; margin: 0 0 8px; }
.f5-z ul { margin: 0; padding-left: 16px; }
.f5-z li { font-size: 13.5px; line-height: 1.4; margin: 0 0 4px; }
.f5-core { background: #14352F; border-color: #14352F; }
.f5-core h3, .f5-core p, .f5-core li { color: var(--cream); }
.f5-arrow { position: relative; }
.f5-arrow i { position: absolute; top: 50%; left: 6px; right: 6px; height: 2px; background: rgba(20,53,47,.3); overflow: hidden; }
.f5-arrow i::after { content: ''; position: absolute; top: -2px; left: -30%; width: 30%; height: 6px; border-radius: 6px; background: #E8A577; }
.rp-fig.in .f5-arrow i::after { animation: f5Flow 2.2s linear infinite; }
@keyframes f5Flow { to { left: 100%; } }
.f5-threat { position: absolute; left: 22px; right: 22px; bottom: 18px; display: flex; flex-wrap: wrap; gap: 4px 12px; align-items: center; padding: 12px 16px; border-radius: 14px; border: 1px dashed #B5532A; background: rgba(181,83,42,.06); }
.f5-threat span { font: 700 13px/1.2 var(--head); color: #9A4A22; }
.f5-threat b { font-size: 13.5px; font-weight: 500; color: #2B3A36; }

/* Figure 6 */
.f6 { position: relative; list-style: none; margin: 0; padding: 0 0 0 28px; }
.f6::before { content: ''; position: absolute; left: 7px; top: 6px; bottom: 6px; width: 2px; background: rgba(20,53,47,.15); }
.f6::after { content: ''; position: absolute; left: 7px; top: 6px; width: 2px; height: 0; background: #E8A577; transition: height 2.4s ease; }
.rp-fig.in .f6::after { height: calc(100% - 12px); }
.f6 li { position: relative; padding: 0 0 22px; }
.f6 li::before { content: ''; position: absolute; left: -26px; top: 6px; width: 12px; height: 12px; border-radius: 50%; background: #fff; border: 2px solid var(--green); }
.f6-now::before { background: #E8A577 !important; border-color: #E8A577 !important; box-shadow: 0 0 0 6px rgba(232,165,119,.25); }
.f6-y { display: inline-block; margin-right: 10px; font: 800 14px/1 var(--head); color: #9A4A22; }
.f6 li > b { font: 700 16px/1.3 var(--head); color: var(--green); }
.f6 li p { margin: 4px 0 0; font-size: 15px; line-height: 1.55; }

/* Figure 7 */
.f7 { display: grid; gap: 18px; padding: 22px; border-radius: 22px; background: #14352F; color: var(--cream); }
.f7-stats { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; }
.f7-stats div { padding: 16px; border-radius: 14px; background: rgba(255,253,248,.06); }
.f7-stats b { display: block; font: 800 32px/1 var(--head); letter-spacing: -0.03em; color: #F2C29E; font-variant-numeric: tabular-nums; }
.f7-stats span { display: block; margin-top: 8px; font-size: 13.5px; line-height: 1.45; color: rgba(255,253,248,.8); }
.rp-main .f7-t { margin: 0 0 10px; font: 600 13px/1.3 var(--head); color: rgba(255,253,248,.7); }
.f7-bar { display: grid; grid-template-columns: 150px minmax(0, 1fr) 44px; align-items: center; gap: 10px; margin: 8px 0; }
.f7-bar span { font-size: 13.5px; color: rgba(255,253,248,.85); }
.f7-bar i { display: block; height: 14px; border-radius: 7px; background: rgba(255,253,248,.08); position: relative; overflow: hidden; }
.f7-bar i::after { content: ''; position: absolute; inset: 0 auto 0 0; width: 0; border-radius: 7px; background: #E8A577; transition: width 1.6s cubic-bezier(.2,.7,.2,1); }
.rp-fig.in .f7-bar i::after { width: var(--w); }
.f7-bar b { font: 700 14px/1 var(--head); text-align: right; font-variant-numeric: tabular-nums; }

/* Figure 8 */
.f8 { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); gap: 10px; }
.f8 li { position: relative; padding: 16px; border-radius: 16px; background: #fff; border: 1px solid rgba(20,53,47,.1); }
.f8 li b { display: block; font: 700 15px/1.3 var(--head); color: var(--green); }
.f8 li span { display: block; margin-top: 4px; font-size: 13.5px; line-height: 1.45; color: var(--soft); }
.f8-now { background: #14352F !important; border-color: #14352F !important; }
.f8-now b { color: #F2C29E !important; } .f8-now span { color: rgba(255,253,248,.8) !important; }

.rp-quote { margin: 0 0 22px; padding: 4px 0 4px 22px; border-left: 3px solid #E8A577; }
.rp-quote p { font-family: var(--serif) !important; font-size: 24px !important; line-height: 1.4 !important; color: var(--green) !important; margin: 0 !important; }
.rp-eoi { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 18px; margin-top: 28px; padding: 26px; border-radius: 22px; background: #14352F; }
.rp-eoi h3 { margin: 0 0 6px; color: var(--cream); }
.rp-eoi p { margin: 0; color: rgba(255,253,248,.8); font-size: 15.5px; max-width: 44ch; }
.rp-refs ol { padding-left: 22px; }
.rp-refs li { font-size: 14.5px; line-height: 1.55; }
.rp-refs a { color: var(--green); word-break: break-word; }
.rp-note { margin-top: 18px !important; font-size: 14px !important; color: var(--soft) !important; }

@media (max-width: 1000px) {
  .rp-body { grid-template-columns: minmax(0, 1fr); gap: 0; }
  .rp-toc { display: none; }
  .f5 { grid-template-columns: minmax(0, 1fr); padding-bottom: 22px; }
  .f5-arrow { height: 26px; }
  .f5-arrow i { top: 4px; bottom: 4px; left: 50%; right: auto; width: 2px; height: auto; }
  .f5-arrow i::after { top: -30%; left: -2px; width: 6px; height: 30%; }
  .rp-fig.in .f5-arrow i::after { animation-name: f5FlowV; }
  @keyframes f5FlowV { to { top: 100%; } }
  .f5-threat { position: static; margin-top: 14px; }
}
@media (max-width: 680px) {
  .rp-hero { padding: 124px 0 40px; }
  .rp-abstract { padding: 22px; }
  .rp-keys { grid-template-columns: minmax(0, 1fr); }
  .rp-why-grid, .rp-mlj-pair { grid-template-columns: minmax(0, 1fr); }
  .rp-why-b { grid-row: auto; }
  .rp-why-card { padding: 22px; }
  .rp-heroart { margin-top: 28px; }
  .f1-row, .f2, .f7-stats, .f8 { grid-template-columns: minmax(0, 1fr); }
  .f3-s { grid-template-columns: minmax(0, 1fr); gap: 6px; }
  .f1-row { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .f4-r { grid-template-columns: 1fr 1fr; }
  .f4-h { display: none; }
  .f4-r span:first-child { grid-column: 1 / -1; font-weight: 700; color: var(--green); padding-bottom: 0; }
  .f4-r { grid-template-columns: minmax(0, 1fr); }
  .f4-r span { padding-top: 4px; padding-bottom: 4px; }
  .f4-r span[data-l]::before { content: attr(data-l) ': '; font-weight: 700; color: var(--soft); }
  .f4-r span:last-child { padding-bottom: 12px; }
  .f7-bar { grid-template-columns: 110px minmax(0, 1fr) 36px; }
  .rp-main p, .rp-main li { font-size: 16.5px; }
}
@media (prefers-reduced-motion: reduce) {
  .rp-pulse, .rp-h-draw, .rp-fig.in .f1-line i, .rp-fig.in .f1-node, .rp-fig.in .f1-a, .rp-fig.in .f1-b, .rp-fig.in .f3-s, .rp-fig.in .f5-arrow i::after { animation: none !important; }
  .rp-h-draw { stroke-dashoffset: 0; }
  .rp-h-dot { display: none; }
  .f1-line i { transform: scaleX(1); } .f1-a { opacity: 0; } .f1-b { opacity: 1; }
  .f6::after, .f7-bar i::after { transition: none !important; }
}
'''

JS = r'''
// Journeys initiative: contents buttons and reference links scroll within the page (hash routes stay intact).
document.addEventListener('click', (e) => {
  const b = e.target.closest('[data-goto]'); if (!b) return;
  const t = document.getElementById(b.dataset.goto); if (!t) return;
  e.preventDefault();
  t.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
});
(() => {
  if (!('IntersectionObserver' in window)) return;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)');
  const setup = () => {
    const toc = document.querySelector('.rp-toc'); if (!toc || toc.dataset.ready) return; toc.dataset.ready = '1';
    const btns = [...toc.querySelectorAll('button')];
    const io = new IntersectionObserver((es) => es.forEach((en) => { if (en.isIntersecting) btns.forEach((x) => x.classList.toggle('on', x.dataset.goto === en.target.id)); }), { rootMargin: '-110px 0px -70% 0px' });
    btns.forEach((x) => { const s = document.getElementById(x.dataset.goto); if (s) io.observe(s); });
    if (reduce.matches) document.querySelectorAll('.rp-heroart svg').forEach((s) => s.pauseAnimations && s.pauseAnimations());
  };
  window.addEventListener('hashchange', () => setTimeout(setup, 60));
  setup(); setTimeout(setup, 400);
})();
'''

TILE = '''
      <li class="cs-tile cs-tile-rp">
        <div class="cs-img rp-tile-art" aria-hidden="true"><svg viewBox="0 0 400 260"><path d="M30 190 C 110 60, 170 70, 210 140 S 320 220, 370 90" fill="none" stroke="rgba(255,253,248,.22)" stroke-width="3" stroke-dasharray="6 9"/><path d="M30 190 C 110 60, 170 70, 210 140 S 320 220, 370 90" fill="none" stroke="#E8A577" stroke-width="3" stroke-dasharray="520" stroke-dashoffset="0"/><circle cx="30" cy="190" r="9" fill="#1F4D44" stroke="#FFFDF8" stroke-width="2"/><circle cx="210" cy="140" r="9" fill="#1F4D44" stroke="#FFFDF8" stroke-width="2"/><circle cx="370" cy="90" r="11" fill="#E8A577" stroke="#FFFDF8" stroke-width="2"/><text x="30" y="236" fill="rgba(255,253,248,.75)" font-family="Manrope, sans-serif" font-weight="700" font-size="17">HMAC-SHA256(key, +614…)</text></svg></div>
        <div class="cs-text">
          <p class="cs-name">Initiative</p>
          <h3>Linking journeys, not databases.</h3>
          <p>Caring for people across ministries as one body, without sharing databases. Piloting in Australia; expressions of interest close 10 December.</p>
          <a class="cs-more" href="#/pprl">Explore the initiative</a>
        </div>
      </li>'''

TILE_CSS = '''
.rp-tile-art { background: radial-gradient(120% 90% at 85% 10%, rgba(232,165,119,.28), transparent 60%), #14352F; display: flex; align-items: center; justify-content: center; }
.rp-tile-art svg { width: 100%; height: 100%; }
'''
