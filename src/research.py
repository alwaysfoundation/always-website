"""Research case study: record linkage across ministries, designed, tested and not used."""

SLUG = 'pprl'
TITLE = 'Why Always does not link people across ministries \u00b7 Always Foundation'

TOC = [('rp-physician', 'A physician of the soul'), ('rp-abstract', 'Abstract'), ('rp-problem', '1. Problem statement'), ('rp-pprl', '2. Privacy-preserving linkage'), ('rp-design', '3. Architecture'), ('rp-security', '4. Threat model'), ('rp-health', '5. Lessons from Australian health'), ('rp-cyber', '6. Threat environment'), ('rp-decision', '7. Decision'), ('rp-church', '8. The local church'), ('rp-instead', '9. Evidence without linkage'), ('rp-conditions', '10. Conditions for any study'), ('rp-refs', 'Sources')]


def _toc():
    return ''.join(f'<button type="button" data-goto="{i}">{t}</button>' for i, t in TOC)


PAGE = '''
<article class="rp">
<div class="rp-hero"><div class="wrap rp-hero-in">
  <p class="rp-kick"><a href="#/stories">Stories</a> <span aria-hidden="true">/</span> Research case study</p>
  <h1>Why Always does not link people across ministries</h1>
  <p class="rp-dek">A case study in privacy-preserving record linkage for Christian ministry: the problem, the architecture, the threat model, and the reasons the Foundation declined to deploy it.</p>
  <dl class="rp-mast">
    <div><dt>Published</dt><dd>Always Foundation, November 2026</dd></div>
    <div><dt>Status</dt><dd>Not deployed. Implemented, tested and removed; no personal information was processed.</dd></div>
    <div><dt>Decision record</dt><dd>ADR 0013, no linkage of individuals across organisations</dd></div>
  </dl>
  <figure class="rp-heroart" aria-hidden="true">
    <svg viewBox="0 0 1000 300" preserveAspectRatio="xMidYMid meet">
      <path d="M60 190 C 200 70, 320 70, 390 140 S 600 230, 650 130 S 860 70, 940 150" fill="none" stroke="rgba(255,253,248,.16)" stroke-width="3" stroke-dasharray="2 14" stroke-linecap="round"/>
      <g class="rp-h-rings">
        <circle cx="60" cy="190" r="40"/><circle cx="390" cy="140" r="40"/><circle cx="650" cy="130" r="40"/><circle cx="940" cy="150" r="44"/>
      </g>
      <g class="rp-h-nodes">
        <circle cx="60" cy="190" r="16"/><circle cx="390" cy="140" r="16"/><circle cx="650" cy="130" r="16"/><circle cx="940" cy="150" r="20" class="rp-h-church"/>
      </g>
      <g fill="#F2C29E">
        <circle r="6"><animateMotion dur="6s" repeatCount="indefinite" path="M60 150 a40 40 0 1 1 0 80 a40 40 0 1 1 0 -80"/></circle>
        <circle r="6"><animateMotion dur="7s" repeatCount="indefinite" path="M390 100 a40 40 0 1 0 0 80 a40 40 0 1 0 0 -80"/></circle>
        <circle r="6"><animateMotion dur="5.5s" repeatCount="indefinite" path="M650 90 a40 40 0 1 1 0 80 a40 40 0 1 1 0 -80"/></circle>
        <circle r="7" fill="#FFFDF8"><animateMotion dur="8s" repeatCount="indefinite" path="M940 106 a44 44 0 1 0 0 88 a44 44 0 1 0 0 -88"/></circle>
      </g>
      <g class="rp-h-text"><text x="60" y="268" text-anchor="start">Event</text><text x="390" y="222" text-anchor="middle">Course</text><text x="650" y="70" text-anchor="middle">Bible study</text><text x="940" y="232" text-anchor="end">Church</text></g>
    </svg>
  </figure>
</div></div>

<div class="wrap rp-body">
  <nav class="rp-toc" aria-label="Contents"><p>Contents</p>''' + _toc() + '''</nav>

  <div class="rp-main">
    <section id="rp-physician" class="rp-mlj">
      <h2>A physician of the soul</h2>
      <p class="rp-mlj-lead">In the 1920s, one of the most promising young doctors in London was Martyn Lloyd-Jones. He trained at St Bartholomew&rsquo;s Hospital and became chief clinical assistant to Sir Thomas Horder, physician to the royal family.<sup><a data-goto="rp-refs">[10, 11]</a></sup></p>
      <p>Over two years he weighed a call to leave medicine and become a &lsquo;physician of the soul&rsquo;. In 1927 he moved to a small mission church in Aberavon, South Wales, and went on to become one of the most influential preachers of the twentieth century.<sup><a data-goto="rp-refs">[11]</a></sup> He carried a clinician&rsquo;s discipline of diagnosis and attention to the whole person into the care of a local congregation.</p>
      <div class="rp-mlj-pair">
        <div><b>Medicine</b><p>Continuity of care across many clinicians depends on linked records. Australian health achieves this through independent linkage units, enabling legislation and ethics oversight.</p></div>
        <div><b>The church</b><p>Pastoral care is exercised within local congregations, where people are known personally. Each congregation can hold its own people without a shared record of them.</p></div>
      </div>
      <p>This case study examines whether the church requires medicine&rsquo;s apparatus for linking records across institutions. Having designed and tested that apparatus, the Foundation concluded that it does not.</p>
    </section>

    <section id="rp-abstract" class="rp-abstract">
      <h2>Abstract</h2>
      <p>Faith formation rarely occurs within a single organisation. A person may respond at an event, complete a course run by another ministry, read the Bible with a friend and later join a local church. Each organisation observes one stage. Funders and networks that support many independent ministries can measure activity at each stage, yet cannot determine whether the same individuals progress from one to the next.</p>
      <p>We treated this as a problem of interoperability between independent institutions: how organisations might recognise records relating to the same person without exchanging their databases. Australian health research has addressed the same problem for three decades through privacy-preserving record linkage (PPRL). We adapted that method to ministry, implemented a consent-based design using a keyed cryptographic fingerprint of the person&rsquo;s mobile number with organisation-specific pseudonyms, and verified it under automated tests.</p>
      <p>We then assessed the system&rsquo;s second-order effects. Its utility increases with adoption, and so does its value as a target: at scale, the key and the resulting links would constitute a record of religious participation across the network. We concluded that the residual risk was not justified by the benefit, removed the implementation, and adopted a standing architectural prohibition. The decision was taken before any personal information was processed and before any organisation depended on the capability.</p>
      <dl class="rp-keys">
        <div><dt>Method</dt><dd>Consent-based PPRL with a single linkage service</dd></div>
        <div><dt>Encoding</dt><dd>HMAC-SHA256 over a normalised Australian mobile number</dd></div>
        <div><dt>Status</dt><dd>Implemented and tested; never deployed</dd></div>
        <div><dt>Decision</dt><dd>Not to deploy, at any scale (ADR 0013)</dd></div>
      </dl>
    </section>

    <section id="rp-problem">
      <h2>1. Problem statement</h2>
      <p>Consider a hypothetical individual, Sam, who responds at a youth event in February, enrols in a course run by another ministry in March, joins a Bible reading group through a third in April, and is welcomed by a local church in May. Four organisations each hold one record. None can observe the sequence.</p>
      <figure class="rp-fig rv" id="rp-fig1">
        <div class="f1">
          <div class="f1-row">
            <div class="f1-node"><b>Event</b><span>Responded, Feb</span></div>
            <div class="f1-node"><b>Course</b><span>Enrolled, Mar</span></div>
            <div class="f1-node"><b>Bible study</b><span>Reading, Apr</span></div>
            <div class="f1-node f1-church"><b>Church</b><span>Welcomed, May</span></div>
          </div>
          <div class="f1-line" aria-hidden="true"><i></i></div>
          <div class="f1-states" aria-hidden="true"><span class="f1-a">Present state: four independent records</span><span class="f1-b">With linkage: one reconstructed journey, held centrally</span></div>
        </div>
        <figcaption><b>Figure 1.</b> One individual, four organisations. Linkage reconstructs the sequence. In doing so it creates a record that did not previously exist.</figcaption>
      </figure>
      <p>At the level of a single ministry the consequence is incomplete follow-up. At the level of a network it is a measurement gap: a funder supporting evangelism, discipleship and church planting can count activity in each, but cannot observe progression between them. The research question was whether that gap could be closed without creating an unacceptable concentration of sensitive information.</p>
    </section>

    <section id="rp-pprl">
      <h2>2. Privacy-preserving record linkage</h2>
      <p>Record linkage identifies records that refer to the same individual across separate collections. Privacy-preserving record linkage performs this without the collections disclosing identifying information to one another. In the conventional trusted-third-party model, each data custodian submits only an encoded identifier to a linkage unit, which determines matches and returns link keys in place of identities.<sup><a data-goto="rp-refs">[1, 2]</a></sup></p>
      <p>Two encoding families predominate. <b>Keyed hashing</b> applies a secret-keyed one-way function to a normalised identifier and supports exact matching only. <b>Bloom-filter encoding</b> decomposes identifiers such as names into fragments, permitting approximate matching that tolerates variation in spelling.<sup><a data-goto="rp-refs">[3, 5]</a></sup> The design adopted keyed hashing, for the reasons set out in section 4.</p>
      <figure class="rp-fig rv">
        <div class="f2">
          <div class="f2-col f2-bad"><h3>Pooled database</h3><ul><li>Every participant sees every individual</li><li>A single breach exposes all records</li><li>Difficult to justify for sensitive information</li></ul></div>
          <div class="f2-col f2-bad"><h3>Manual reconciliation</h3><ul><li>Telephone calls and spreadsheets</li><li>Identities circulated by email</li><li>Too costly to sustain</li></ul></div>
          <div class="f2-col f2-good"><h3>Privacy-preserving linkage</h3><ul><li>No exchange of records</li><li>Conditional on individual consent</li><li>Requires a key and a linkage service</li></ul></div>
        </div>
        <figcaption><b>Figure 2.</b> Approaches to joining records across organisations. PPRL dominates the alternatives, but retains a key and a linkage service that must be trusted.</figcaption>
      </figure>
    </section>

    <section id="rp-design">
      <h2>3. Architecture</h2>
      <p>The design was implemented within the Always Platform API and database, published as open source, verified by automated tests including tests that attempt to read across organisational boundaries, and recorded in ADR 0012.<sup><a data-goto="rp-refs">[12]</a></sup> It was never enabled, and has since been removed by migration.</p>

      <figure class="rp-fig rv" id="rp-fig3">
        <ol class="f3">
          <li class="f3-s"><span class="f3-k">Input</span><code>0412 345 678</code><small>Provided with consent</small></li>
          <li class="f3-s"><span class="f3-k">Normalise</span><code>+61412345678</code><small>Canonical E.164 form</small></li>
          <li class="f3-s f3-key"><span class="f3-k">Fingerprint</span><code>HMAC-SHA256(LINK_KEY, &middot;)</code><small>Key held outside the database</small></li>
          <li class="f3-s"><span class="f3-k">Match</span><code>9f3c&hellip;e1a7</code><small>Equal fingerprint, same journey</small></li>
          <li class="f3-s f3-key"><span class="f3-k">Pseudonym</span><code>jny_Q2v&hellip; &ne; jny_8Lk&hellip;</code><small>HMAC(ORG_CODE_KEY, journey | organisation)</small></li>
        </ol>
        <figcaption><b>Figure 3.</b> Identifier processing as designed. The number is normalised, transformed under a secret key, matched, and presented to each organisation under an unrelated pseudonym. Values shown are illustrative.</figcaption>
      </figure>

      <h3>3.1 Consent and eligibility</h3>
      <p>Linkage required a distinct consent purpose, <code>share.journey</code>, never pre-selected, separate from consent to be introduced to a church, and verified by the database before any link was written. The API rejected the purpose for anyone under 18. In practical terms, participation was a separate and explicit choice, and minors were excluded without exception.</p>

      <h3>3.2 Keyed fingerprint</h3>
      <p>The fingerprint was <code>HMAC-SHA256(LINK_KEY, +614XXXXXXXX)</code>, a standard keyed hash,<sup><a data-goto="rp-refs">[13]</a></sup> with the key held in the runtime environment and isolated from the database and from authentication secrets. Functionally it behaves as one-way encryption: without the key, the fingerprint cannot be computed from a number or inverted to recover one.</p>

      <h3>3.3 Organisation-specific pseudonyms</h3>
      <p>No organisation received the fingerprint or the internal journey identifier. Each received <code>HMAC(ORG_CODE_KEY, journey id | organisation id)</code>, stable within that organisation and uncorrelated across organisations. Two organisations comparing their data could not establish that they held the same individual.</p>

      <h3>3.4 Disclosure matrix</h3>
      <figure class="rp-fig rv">
        <div class="f4" role="table" aria-label="Disclosure matrix">
          <div class="f4-r f4-h" role="row"><span role="columnheader">Party</span><span role="columnheader">Identity</span><span role="columnheader">Milestones</span><span role="columnheader">Notes</span></div>
          <div class="f4-r" role="row"><span role="cell">The individual</span><span role="cell" data-l="Identity" class="y">Own</span><span role="cell" data-l="Milestones" class="y">All; withdrawal at any time</span><span role="cell" data-l="Notes">&mdash;</span></div>
          <div class="f4-r" role="row"><span role="cell">Each organisation on the journey</span><span role="cell" data-l="Identity" class="p">Its own record only</span><span role="cell" data-l="Milestones" class="y">Milestone and month</span><span role="cell" data-l="Notes" class="n">Its own only</span></div>
          <div class="f4-r" role="row"><span role="cell">Always Platform</span><span role="cell" data-l="Identity" class="p">Fingerprints and keys</span><span role="cell" data-l="Milestones" class="y">As required to operate</span><span role="cell" data-l="Notes" class="n">None</span></div>
          <div class="f4-r" role="row"><span role="cell">Funders and networks</span><span role="cell" data-l="Identity" class="n">None</span><span role="cell" data-l="Milestones" class="p">Aggregates; small cells suppressed</span><span role="cell" data-l="Notes" class="n">None</span></div>
        </div>
        <figcaption><b>Figure 4.</b> Disclosure by party. The third row concentrates the fingerprints and the keys in a single organisation, and is the locus of the residual risk.</figcaption>
      </figure>
    </section>

    <section id="rp-security">
      <h2>4. Threat model</h2>
      <figure class="rp-fig rv" id="rp-fig5">
        <div class="f5">
          <div class="f5-z"><h3>Sources</h3><p>Response pages, church inboxes, partner systems</p><ul><li>Encrypted in transit</li><li>Consent verified first</li></ul></div>
          <div class="f5-arrow" aria-hidden="true"><i></i></div>
          <div class="f5-z f5-core"><h3>Linkage service</h3><p>Fingerprints and journeys in the database; <b>keys held separately</b></p><ul><li>Row-level security</li><li>All access logged</li></ul></div>
          <div class="f5-arrow" aria-hidden="true"><i></i></div>
          <div class="f5-z"><h3>Outputs</h3><p>Pseudonyms and milestones; aggregates for reporting</p><ul><li>No fingerprint disclosed</li><li>Small cells suppressed</li></ul></div>
          <div class="f5-threat" aria-hidden="true"><span>Adversary holding the key and the data</span><b>Inverts every fingerprint and reconstructs every journey</b></div>
        </div>
        <figcaption><b>Figure 5.</b> Trust zones. The design withstands exfiltration of the database. It does not withstand compromise or misuse of the key, and the key must be held by someone.</figcaption>
      </figure>
      <p>The cryptographic primitives are sound. The material risks arise from the system&rsquo;s position, its custodian and its trajectory.</p>
      <dl class="rp-risks">
        <div><dt>Value increases with adoption</dt><dd>Linkage across ten ministries offers modest utility. Linkage across a thousand would produce one of the most sensitive datasets on religious participation in the country. Utility and attractiveness to adversaries scale together.</dd></div>
        <div><dt>Small identifier space</dt><dd>Australian mobile numbers occupy roughly 10<sup>8</sup> values. With the key, exhaustive enumeration is computationally trivial. The entire protection therefore reduces to the custody of a single secret.</dd></div>
        <div><dt>Privileged insider</dt><dd>The strongest adversary sits within the linkage service, where the keys reside. Access controls, logging and oversight reduce this risk but cannot eliminate it.</dd></div>
        <div><dt>Inference from sequences</dt><dd>Without the key, a sequence of milestones, places and months may still identify an individual within a small community.</dd></div>
        <div><dt>Compelled disclosure</dt><dd>Courts, regulators or foreign authorities may demand linked data. Data that has not been created cannot be compelled.</dd></div>
        <div><dt>Function creep</dt><dd>Requests for additional participants, longer histories and finer reporting are each individually defensible and collectively produce a register of religious participation.</dd></div>
        <div><dt>Identifier instability</dt><dd>Reissued numbers and shared handsets can merge distinct individuals into a single journey.</dd></div>
      </dl>
      <h3>4.1 Rejection of Bloom-filter encoding</h3>
      <p>Bloom-filter linkage tolerates typographical variation and is widely used in health research, but published cryptanalysis has re-identified encoded values, particularly common names, from sets of filters.<sup><a data-goto="rp-refs">[5, 6]</a></sup> It also requires additional identifying attributes, such as names and dates of birth. Exact matching on a single consented identifier was the more conservative choice. It did not resolve the custody problem.</p>
    </section>

    <section id="rp-health">
      <h2>5. Lessons from Australian health</h2>
      <p>Australia has one of the most mature record-linkage environments in the world, which made it the natural reference point.</p>
      <figure class="rp-fig rv" id="rp-fig6">
        <ol class="f6">
          <li><span class="f6-y">1995</span><b>WA Data Linkage System</b><p>Established in Western Australia; now the longest-running linkage system in Australia.<sup><a data-goto="rp-refs">[1]</a></sup></p></li>
          <li><span class="f6-y">2009&ndash;12</span><b>National infrastructure</b><p>The Population Health Research Network establishes linkage units in every state and a Centre for Data Linkage.<sup><a data-goto="rp-refs">[2]</a></sup></p></li>
          <li><span class="f6-y">2018</span><b>Evaluated at scale</b><p>A NSW evaluation links primary-care records from 16 general practices to tens of millions of hospital records using privacy-preserving methods.<sup><a data-goto="rp-refs">[4]</a></sup></p></li>
          <li><span class="f6-y">2018</span><b>Evaluated adversarially</b><p>Researchers at the Australian National University publish efficient attacks on Bloom-filter encodings.<sup><a data-goto="rp-refs">[5]</a></sup></p></li>
          <li><span class="f6-y">2022</span><b>Accuracy established</b><p>A blinded WA evaluation finds 99.3% of groupings identical between privacy-preserving and clear-text linkage.<sup><a data-goto="rp-refs">[3]</a></sup></p></li>
          <li class="f6-now"><span class="f6-y">2026</span><b>Assessed for ministry</b><p>Always implements and evaluates consent-based linkage across ministries, and declines to deploy it.</p></li>
        </ol>
        <figcaption><b>Figure 6.</b> Three decades of Australian record linkage, and the point at which the Foundation stopped.</figcaption>
      </figure>
      <p>The safety of health linkage derives less from its cryptography than from its institutional setting: separation between those who link records and those who hold them, enabling legislation, ethics review, and published methods. That setting was built over decades by public institutions. A voluntary network of churches and ministries has no equivalent, and it would be inappropriate for a small foundation to attempt to become one.</p>
    </section>

    <section id="rp-cyber">
      <h2>6. Threat environment</h2>
      <p>Any system that connects independent organisations acquires the characteristics of infrastructure, and with them its exposure. The Australian Signals Directorate assesses state-sponsored actors as a serious and growing threat to government, critical infrastructure and business networks.<sup><a data-goto="rp-refs">[7]</a></sup></p>
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
      <p>The MediSecure breach, affecting approximately 12.9 million people, is the largest notified under the Notifiable Data Breaches scheme.<sup><a data-goto="rp-refs">[8]</a></sup> A linked record of who responded to the Gospel, and where they subsequently went, would rank among the most sensitive collections in the country. PPRL raises the cost of exploiting such a record. Declining to create it removes the record altogether.</p>
    </section>

    <section id="rp-decision">
      <h2>7. Decision</h2>
      <figure class="rp-fig rv">
        <div class="f2 f2-two">
          <div class="f2-col f2-good"><h3>Benefits</h3><ul><li>Visibility of progression between ministries</li><li>De-duplicated network totals</li><li>Reduced manual coordination</li></ul></div>
          <div class="f2-col f2-bad"><h3>Costs</h3><ul><li>A key and link set attractive to theft and compulsion</li><li>Re-identification risk in small communities</li><li>A commitment to individuals beyond an introduction to one church</li><li>Structural pressure to extend scope</li></ul></div>
        </div>
        <figcaption><b>Figure 8.</b> The assessment. Most benefits are obtainable by other means (section 9). The costs are intrinsic to the capability.</figcaption>
      </figure>
      <h3>7.1 Timing</h3>
      <p>The assessment was completed while the system functioned and before any dependency had formed: no personal information had been processed, no ministry workflows relied on it, and no funder reporting had been built upon it. Decisions of this kind become materially harder once a capability is embedded in operations and expectations.</p>
      <h3>7.2 Limited deployment</h3>
      <p>Restricting linkage to selected high-impact programmes would reduce the number of individuals exposed without reducing the principal risks. Smaller cohorts are more readily re-identified, the key retains its value irrespective of scale, and an exception granted to one funder establishes a precedent for the next.</p>
      <h3>7.3 Legal context</h3>
      <p>Australian law does not prohibit record linkage, but classifies religious belief as sensitive information. Under the Privacy Act 1988, collection generally requires consent, and use or disclosure is confined to the primary purpose or a directly related secondary purpose the individual would reasonably expect. A Children&rsquo;s Online Privacy Code is required to be registered by 10 December 2026, imposing further obligations for children&rsquo;s information online.<sup><a data-goto="rp-refs">[14]</a></sup> The Foundation&rsquo;s position is more restrictive than the law requires.</p>
      <h3>7.4 Durability</h3>
      <p>The implementation and its database objects were removed, a standing prohibition was recorded in ADR 0013, exceptions for major funders or high-impact programmes were expressly excluded, and conditions were set for any future study. The intent is that the decision should not depend on the continued presence of those who made it.</p>
    </section>

    <section id="rp-church">
      <h2>8. The local church as privacy architecture</h2>
      <p>The church has always existed as many local congregations, each responsible for the care of its own people. That structure is a strength for privacy as well as for pastoral care.</p>
      <div class="rp-mlj-pair">
        <div><b>No central register</b><p>Where each congregation holds its own records, there is no single collection to steal, sell or seize, and a compromise at one does not expose another.</p></div>
        <div><b>Care where people are known</b><p>A person who asks to be introduced is referred to one church, with their permission, and that church assumes their care. Always facilitates the introduction and retains nothing further.</p></div>
      </div>
      <p>Always Platform follows the same principle. It connects churches and ministries while leaving each responsible for its own people.</p>
    </section>

    <section id="rp-instead">
      <h2>9. Evidence without linkage</h2>
      <p>Most questions asked by ministries and funders can be answered without recognising any individual across organisations.</p>
      <figure class="rp-fig rv">
        <div class="f4" role="table" aria-label="Evidence without linkage">
          <div class="f4-r f4-h" role="row"><span role="columnheader">Question</span><span role="columnheader">Method</span><span role="columnheader">Disclosure</span><span role="columnheader">Linkage</span></div>
          <div class="f4-r" role="row"><span role="cell">Did respondents at this event join a church?</span><span role="cell" data-l="Method">Handoff outcomes recorded by the receiving church</span><span role="cell" data-l="Disclosure" class="p">Aggregates per event</span><span role="cell" data-l="Linkage" class="y">Not required</span></div>
          <div class="f4-r" role="row"><span role="cell">Are they still connected after some months?</span><span role="cell" data-l="Method">Self-report collected by the chosen church, with consent to count</span><span role="cell" data-l="Disclosure" class="p">Aggregates only</span><span role="cell" data-l="Linkage" class="y">Not required</span></div>
          <div class="f4-r" role="row"><span role="cell">How is a ministry performing over time?</span><span role="cell" data-l="Method">The ministry&rsquo;s own handoffs and outcomes by month</span><span role="cell" data-l="Disclosure" class="p">That ministry</span><span role="cell" data-l="Linkage" class="y">Not required</span></div>
          <div class="f4-r" role="row"><span role="cell">Did a programme cause the outcome?</span><span role="cell" data-l="Method">Not identifiable from routine data</span><span role="cell" data-l="Disclosure">&mdash;</span><span role="cell" data-l="Linkage" class="n">Research study</span></div>
        </div>
        <figcaption><b>Figure 9.</b> Evidence without linkage. Only causal attribution requires linkage, and it is properly a research question.</figcaption>
      </figure>
    </section>

    <section id="rp-conditions">
      <h2>10. Conditions for any future study</h2>
      <p>Should causal attribution ever be required, it would need to be pursued as a discrete study conducted outside Always. The following are minimum conditions for consideration:</p>
      <ol>
        <li>Conducted by an independent university or accredited researcher, not by Always, a funder or a participating ministry.</li>
        <li>Approved by a human research ethics committee.</li>
        <li>Study-specific consent in plain language, which may be declined without any effect on care.</li>
        <li>Adults only.</li>
        <li>Separation of identifying data from study data.</li>
        <li>A fixed end date, after which linked data and keys are destroyed and destruction is recorded.</li>
        <li>Publication of results in aggregate, irrespective of findings.</li>
        <li>No linkage capability in Always Platform, and no linkage key held by Always.</li>
        <li>An open decision process: a new architecture decision record, legal and independent privacy review, and board approval.</li>
      </ol>
      <p>A proposal that does not satisfy every condition will not proceed.</p>
      <h3>Position</h3>
      <p>Always does not link individuals across organisations, at any scale or under any name. The position is recorded in the Foundation&rsquo;s open-source architecture decisions (ADR 0013) and binds its code, its partners and its funders.</p>
      <p>The technical capacity to build a capability and the institutional standing to hold it are distinct questions. For an organisation constituted to serve independent churches, the second is decisive.</p>
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
        <li>Always Platform. ADR 0012 (withdrawn) and ADR 0013: no linkage of individuals across organisations. <a href="https://github.com/alwaysfoundation/always-platform">github.com/alwaysfoundation/always-platform</a></li>
        <li>Krawczyk H, Bellare M, Canetti R. HMAC: Keyed-Hashing for Message Authentication. RFC 2104, IETF, 1997. <a href="https://www.rfc-editor.org/rfc/rfc2104">rfc-editor.org</a></li>
        <li>Office of the Australian Information Commissioner. Children&rsquo;s Online Privacy Code. <a href="https://www.oaic.gov.au/privacy/privacy-registers/privacy-codes/childrens-online-privacy-code">oaic.gov.au</a></li>
      </ol>
      <p class="rp-note">This research case study does not constitute legal advice. Nothing described here operates on Always Platform. Correspondence is welcome at <a href="mailto:hello@alwaysfoundation.org">hello@alwaysfoundation.org</a>.</p>
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
.rp-h-text text { fill: rgba(255,253,248,.78); font: 600 26px var(--head, Inter), Inter, sans-serif; letter-spacing: -0.01em; }
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

.rp-mast { display: grid; grid-template-columns: 1fr 1.5fr 1.3fr; gap: 28px; max-width: 920px; margin: 40px 0 0; padding: 22px 0 0; border-top: 1px solid rgba(255,253,248,.18); }
.rp-mast dt { font: 600 13px/1.3 var(--head); color: rgba(255,253,248,.55); margin: 0 0 6px; }
.rp-mast dd { margin: 0; font-size: 15.5px; line-height: 1.5; color: rgba(255,253,248,.9); }
@media (max-width: 760px) { .rp-mast { grid-template-columns: 1fr; gap: 16px; } }
.rp-h-rings circle { fill: none; stroke: rgba(242,194,158,.38); stroke-width: 2; stroke-dasharray: 3 8; }
.rp-risks { margin: 22px 0 8px; border-top: 1px solid rgba(20,53,47,.14); }
.rp-risks div { display: grid; grid-template-columns: 210px 1fr; gap: 24px; padding: 16px 0; border-bottom: 1px solid rgba(20,53,47,.1); }
.rp-risks dt { font: 700 16px/1.4 var(--head); color: var(--green); }
.rp-risks dd { margin: 0; font-size: 16.5px; line-height: 1.6; color: #2B3A36; }
@media (max-width: 700px) { .rp-risks div { grid-template-columns: 1fr; gap: 4px; } }
.f2-two { grid-template-columns: repeat(2, minmax(0, 1fr)); }
@media (max-width: 700px) { .f2-two { grid-template-columns: minmax(0, 1fr); } }
'''

JS = r'''
// Case study: contents buttons and reference links scroll within the page (hash routes stay intact).
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
        <div class="cs-img rp-tile-art" aria-hidden="true"><svg viewBox="0 0 400 260"><path d="M40 170 C 110 70, 170 80, 200 130 S 300 200, 360 110" fill="none" stroke="rgba(255,253,248,.18)" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round"/><g fill="none" stroke="rgba(242,194,158,.45)" stroke-width="2" stroke-dasharray="3 6"><circle cx="40" cy="170" r="26"/><circle cx="200" cy="130" r="26"/><circle cx="360" cy="110" r="28"/></g><circle cx="40" cy="170" r="9" fill="#1F4D44" stroke="#FFFDF8" stroke-width="2"/><circle cx="200" cy="130" r="9" fill="#1F4D44" stroke="#FFFDF8" stroke-width="2"/><circle cx="360" cy="110" r="11" fill="#E8A577" stroke="#FFFDF8" stroke-width="2"/><text x="40" y="236" fill="rgba(255,253,248,.75)" font-family="Inter, sans-serif" font-weight="700" font-size="17">HMAC-SHA256(key, +614…)</text></svg></div>
        <div class="cs-text">
          <p class="cs-name">Research case study</p>
          <h3>Why Always does not link people across ministries.</h3>
          <p>Privacy-preserving record linkage for Christian ministry: the architecture, the threat model, and the decision not to deploy it.</p>
          <a class="cs-more" href="#/pprl">Read the case study</a>
        </div>
      </li>'''

TILE_CSS = '''
.rp-tile-art { background: radial-gradient(120% 90% at 85% 10%, rgba(232,165,119,.28), transparent 60%), #14352F; display: flex; align-items: center; justify-content: center; }
.rp-tile-art svg { width: 100%; height: 100%; }
'''
