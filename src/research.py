"""Research case study: privacy-preserving record linkage across ministries, assessed and not deployed."""

import research_figs as F

SLUG = 'pprl'
TITLE = 'Why Always does not link people across ministries \u00b7 Always Foundation'

TOC = [('rx-prologue', 'A physician of the soul'), ('rx-abstract', 'Abstract'), ('rx-problem', '1. Problem statement'), ('rx-pprl', '2. Record linkage'), ('rx-design', '3. Architecture'), ('rx-threats', '4. Threat model'), ('rx-health', '5. Australian health'), ('rx-environment', '6. Threat environment'), ('rx-open', '7. Open source'), ('rx-assessment', '8. Assessment'), ('rx-church', '9. The local church'), ('rx-instead', '10. Evidence without linkage'), ('rx-conditions', '11. Conditions for study'), ('rx-decision', '12. Decision'), ('rx-refs', 'Sources')]


def _toc():
    return ''.join(f'<button type="button" data-goto="{i}">{t}</button>' for i, t in TOC)


PAGE = '''
<article class="rx">
<div class="rx-mast"><div class="wrap rx-mast-in">
  <p class="rx-series"><a href="#/stories">Stories</a> <span aria-hidden="true">/</span> Research case study</p>
  <h1>Why Always does not link people across ministries</h1>
  <p class="rx-dek">Privacy-preserving record linkage for Christian ministry: the problem, the architecture, the threat model, and the reasons the Foundation declined to deploy it.</p>
  <dl class="rx-front">
    <div><dt>Published</dt><dd>Always Foundation, November 2026</dd></div>
    <div><dt>Status</dt><dd><span class="rx-status">Not deployed</span>. Implemented, tested and removed. No personal information was processed.</dd></div>
    <div><dt>Decision record</dt><dd>ADR 0013, No linkage of individuals across organisations</dd></div>
  </dl>
</div></div>

<div class="rx-sheet"><div class="wrap rx-body">
  <nav class="rx-toc" aria-label="Contents"><p>Contents</p>''' + _toc() + '''</nav>

  <div class="rx-main">
    <section id="rx-prologue" class="rx-prologue">
      <h2>A physician of the soul</h2>
      <p class="rx-lead">In the 1920s, one of the most promising young doctors in London was Martyn Lloyd-Jones. He trained at St Bartholomew&rsquo;s Hospital and became chief clinical assistant to Sir Thomas Horder, physician to the royal family.<sup><a data-goto="rx-refs">[10, 11]</a></sup></p>
      <p>Over two years he weighed a call to leave medicine and become a &lsquo;physician of the soul&rsquo;. In 1927 he moved to a small mission church in Aberavon, South Wales, and went on to become one of the most influential preachers of the twentieth century.<sup><a data-goto="rx-refs">[11]</a></sup> He carried a clinician&rsquo;s discipline of diagnosis and attention to the whole person into the care of a local congregation.</p>
      <div class="rx-pair">
        <div><h3>Medicine</h3><p>Continuity of care across many clinicians depends on linked records. Australian health achieves this through independent linkage units, enabling legislation and ethics oversight.</p></div>
        <div><h3>The church</h3><p>Pastoral care is exercised within local congregations, where people are known personally. Each congregation can hold its own people without a shared record of them.</p></div>
      </div>
      <p>This case study examines whether the church requires medicine&rsquo;s apparatus for linking records across institutions. Having designed and tested that apparatus, the Foundation concluded that it does not.</p>
    </section>

    <section id="rx-abstract" class="rx-abstract">
      <h2>Abstract</h2>
      <p>Faith formation rarely occurs within a single organisation. A person may respond at an event, complete a course run by another ministry, read the Bible with a friend and later join a local church. Each organisation observes one stage. Funders and networks that support many independent ministries can measure activity at each stage, yet cannot determine whether the same individuals progress from one to the next.</p>
      <p>We treated this as a problem of interoperability between independent institutions: how organisations might recognise records relating to the same person without exchanging their databases. Australian health research has addressed the same problem for three decades through privacy-preserving record linkage (PPRL). We adapted that method to ministry, implemented a consent-based design using a keyed cryptographic fingerprint of the person&rsquo;s mobile number with organisation-specific pseudonyms, and verified it under automated tests.</p>
      <p>We then assessed the system&rsquo;s second-order effects. Its utility increases with adoption, and so does its value as a target: at scale, the key and the resulting links would constitute a record of religious participation across the network. We concluded that the residual risk was not justified by the benefit, removed the implementation, and adopted a standing architectural prohibition. The decision was taken before any personal information was processed and before any organisation depended on the capability.</p>
      <dl class="rx-keys">
        <div><dt>Method</dt><dd>Consent-based PPRL with a single linkage service</dd></div>
        <div><dt>Encoding</dt><dd>HMAC-SHA256 over a normalised Australian mobile number</dd></div>
        <div><dt>Status</dt><dd>Implemented and tested; never deployed</dd></div>
        <div><dt>Outcome</dt><dd>Not deployed at any scale (ADR 0013)</dd></div>
      </dl>
    </section>

    <section id="rx-problem">
      <h2><span>1</span>Problem statement</h2>
      <p>Consider a hypothetical individual, Sam, who responds at a youth event in February, enrols in a course run by another ministry in March, joins a Bible reading group through a third in April, and is welcomed by a local church in May. Four organisations each hold one record. None can observe the sequence.</p>
      <figure class="rx-fig rx-wide">''' + F.journey() + '''<figcaption><span class="rx-fn">Figure 1</span> One individual, four organisations. Each holds its own record. Linkage would reconstruct the sequence, and in doing so create a central record that does not otherwise exist.</figcaption></figure>
      <p>At the level of a single ministry the consequence is incomplete follow-up: the event team does not learn whether Sam found a church, and the church does not know the steps Sam has already taken. At the level of a network it is a measurement gap. A funder supporting evangelism, discipleship and church planting can count activity in each, but cannot observe progression between them, and an individual reported by four ministries is counted four times.</p>
      <p>The research question was whether that gap could be closed without creating an unacceptable concentration of sensitive information.</p>
    </section>

    <section id="rx-pprl">
      <h2><span>2</span>Privacy-preserving record linkage</h2>
      <p>Record linkage identifies records that refer to the same individual across separate collections. Privacy-preserving record linkage performs this without the collections disclosing identifying information to one another. In the conventional trusted-third-party model, each data custodian submits only an encoded identifier to a linkage unit, which determines matches and returns link keys in place of identities.<sup><a data-goto="rx-refs">[1, 2]</a></sup></p>
      <p>Two encoding families predominate. <em>Keyed hashing</em> applies a secret-keyed one-way function to a normalised identifier and supports exact matching only. <em>Bloom-filter encoding</em> decomposes identifiers such as names into fragments, permitting approximate matching that tolerates variation in spelling.<sup><a data-goto="rx-refs">[3, 5]</a></sup> The design adopted keyed hashing, for the reasons set out in section 4.</p>
      <figure class="rx-fig">
        <div class="rx-tw"><table class="rx-table">
          <thead><tr><th scope="col"></th><th scope="col">Pooled database</th><th scope="col">Manual reconciliation</th><th scope="col">Privacy-preserving linkage</th></tr></thead>
          <tbody>
            <tr><th scope="row">Records exchanged</th><td>All, with every participant</td><td>Identities circulated by email</td><td>None; encoded identifiers only</td></tr>
            <tr><th scope="row">Impact of one breach</th><td>Every record exposed</td><td>Scattered and untracked</td><td>Fingerprints, unusable without the key</td></tr>
            <tr><th scope="row">Practicality</th><td>High</td><td>Too costly to sustain</td><td>High</td></tr>
            <tr><th scope="row">Residual trust</th><td>Every participant</td><td>Every recipient</td><td>The linkage service and its key</td></tr>
          </tbody>
        </table></div>
        <figcaption><span class="rx-fn">Figure 2</span> Approaches to joining records across organisations. PPRL dominates the alternatives, but retains a key and a linkage service that must be trusted.</figcaption>
      </figure>
    </section>

    <section id="rx-design">
      <h2><span>3</span>Architecture</h2>
      <p>The design was implemented within the Always Platform API and database, published as open source, verified by automated tests including tests that attempt to read across organisational boundaries, and recorded in ADR 0012.<sup><a data-goto="rx-refs">[12]</a></sup> It was never enabled, and has since been removed by migration.</p>
      <figure class="rx-fig rx-wide">''' + F.hmac() + '''<figcaption><span class="rx-fn">Figure 3</span> Linkage architecture as designed. The number is normalised and transformed under a secret key held outside the database. The resulting fingerprint is matched to a journey, which each organisation sees under an unrelated pseudonym. Values are illustrative.</figcaption></figure>

      <h3>3.1 Consent and eligibility</h3>
      <p>Linkage required a distinct consent purpose, <code>share.journey</code>, never pre-selected, separate from consent to be introduced to a church, and verified by the database before any link was written. The API rejected the purpose for anyone under 18, and the database refused to link without a current, unwithdrawn consent. These rules were not configurable.</p>

      <h3>3.2 Normalisation</h3>
      <p>Australian mobile numbers are written in many forms. Before transformation each was reduced to a single canonical form, <code>+614XXXXXXXX</code>, so that the same number always produced the same fingerprint. Identifiers that were not Australian mobile numbers were not linked.</p>

      <h3>3.3 Keyed fingerprint</h3>
      <p>The fingerprint was <code>HMAC-SHA256(LINK_KEY, normalised number)</code>, a standard keyed hash.<sup><a data-goto="rx-refs">[13]</a></sup> The key was held in the runtime environment, isolated from the database and from authentication secrets, so that it could be rotated or destroyed independently. Functionally the transformation behaves as one-way encryption: without the key, a fingerprint cannot be computed from a number or inverted to recover one.</p>

      <h3>3.4 Organisation-specific pseudonyms</h3>
      <p>No organisation received the fingerprint or the internal journey identifier. Each received <code>HMAC(ORG_CODE_KEY, journey id | organisation id)</code>, stable within that organisation and uncorrelated across organisations. Two organisations comparing their data could not establish that they held the same individual.</p>

      <h3>3.5 Disclosure</h3>
      <p>Each organisation on a journey would have seen milestones and months, with its own steps marked. Notes, exact dates and the names of other organisations were never disclosed.</p>
      <figure class="rx-fig">
        <div class="rx-tw"><table class="rx-table">
          <thead><tr><th scope="col">Party</th><th scope="col">Identity</th><th scope="col">Milestones</th><th scope="col">Notes</th></tr></thead>
          <tbody>
            <tr><th scope="row">The individual</th><td>Own</td><td>All; withdrawal at any time</td><td>&mdash;</td></tr>
            <tr><th scope="row">Each organisation on the journey</th><td>Its own record only</td><td>Milestone and month</td><td>Its own only</td></tr>
            <tr class="rx-hl"><th scope="row">Always Platform</th><td>Fingerprints and keys</td><td>As required to operate</td><td>None</td></tr>
            <tr><th scope="row">Funders and networks</th><td>None</td><td>Aggregates; groups under 10 suppressed</td><td>None</td></tr>
          </tbody>
        </table></div>
        <figcaption><span class="rx-fn">Figure 4</span> Disclosure by party. The highlighted row concentrates the fingerprints and the keys in a single organisation, and is the locus of the residual risk.</figcaption>
      </figure>

      <h3>3.6 Reporting</h3>
      <p>Reports were to read from a de-identified tally rather than from journeys. Funders and networks would have seen results by event, city, month, channel and pathway, and the time taken to find a church. Any group of fewer than ten people was suppressed, on the principle that a journey remains personal information even without a name.</p>

      <h3>3.7 Withdrawal and audit</h3>
      <p>Withdrawal of <code>share.journey</code> unlinked the response immediately, enforced by a database trigger, and every subsequent view returned nothing. Every view of a journey was written to a tamper-evident audit log.</p>
    </section>

    <section id="rx-threats">
      <h2><span>4</span>Threat model</h2>
      <p>The cryptographic primitives are sound. The material risks arise from the system&rsquo;s position, its custodian and its trajectory.</p>
      <figure class="rx-fig rx-wide">''' + F.trust() + '''
        <ol class="rx-legend">
          <li><b>1</b><span><em>Database exfiltration.</em> The attacker obtains fingerprints and journeys but not the keys. Withstood.</span></li>
          <li><b>2</b><span><em>Key compromise or misuse.</em> Every fingerprint can be inverted and every journey reconstructed. Not withstood.</span></li>
          <li><b>3</b><span><em>Privileged insider.</em> Access to both zones. Reduced by least privilege, logging and oversight; not eliminated.</span></li>
          <li><b>4</b><span><em>Inference from outputs.</em> Sequences of milestones and months may identify an individual in a small community.</span></li>
          <li><b>5</b><span><em>Compelled disclosure.</em> Courts, regulators or foreign authorities may demand the linked data.</span></li>
        </ol>
        <figcaption><span class="rx-fn">Figure 5</span> Institutional trust boundary. The design withstands theft of the database. It does not withstand compromise or misuse of the key, and the key must be held by someone.</figcaption>
      </figure>

      <h3>4.1 Adversaries</h3>
      <ul>
        <li><em>A curious organisation</em> seeking information beyond its own care sees only milestones for journeys it is part of, under its own pseudonym.</li>
        <li><em>Colluding organisations</em> comparing data hold uncorrelated pseudonyms and cannot join records through Always; they can compare only what each already held.</li>
        <li><em>An external attacker</em> who exfiltrates the database obtains fingerprints and links, but cannot invert fingerprints without the keys.</li>
        <li><em>A privileged insider</em> at Always is the strongest adversary, because Always holds the keys. Mitigations are least-privilege access, separation of keys from data, logging of every view, open code, board oversight and independent review.</li>
      </ul>

      <h3>4.2 Risk register</h3>
      <dl class="rx-risks">
        <div><dt>Value increases with adoption</dt><dd>Linkage across ten ministries offers modest utility. Linkage across a thousand would produce one of the most sensitive datasets on religious participation in the country. Utility and attractiveness to adversaries scale together.</dd></div>
        <div><dt>Small identifier space</dt><dd>Australian mobile numbers occupy roughly 10<sup>8</sup> values. An unkeyed hash would offer no protection, and with the key, exhaustive enumeration is computationally trivial. The entire protection reduces to the custody of a single secret.</dd></div>
        <div><dt>Privileged insider</dt><dd>The linkage service holds both the data and the keys. Controls reduce the risk; they cannot remove it.</dd></div>
        <div><dt>Inference from sequences</dt><dd>Without the key, a sequence of milestones, places and months may still identify an individual within a small community.</dd></div>
        <div><dt>Compelled disclosure</dt><dd>Linked data may be demanded by courts, regulators or foreign authorities. Data that has not been created cannot be compelled.</dd></div>
        <div><dt>Function creep</dt><dd>Requests for additional participants, longer histories and finer reporting are each individually defensible and collectively produce a register of religious participation.</dd></div>
        <div><dt>Recycled numbers</dt><dd>Carriers reissue disconnected numbers, so two people may share a number over time and be merged into one journey.</dd></div>
        <div><dt>Shared handsets</dt><dd>A family phone may link two people. Changed numbers have the opposite effect, starting a new journey for the same person.</dd></div>
      </dl>

      <h3>4.3 Rejection of Bloom-filter encoding</h3>
      <p>Bloom-filter linkage tolerates typographical variation and is widely used in health research, but published cryptanalysis has re-identified encoded values, particularly common names, from sets of filters, including without knowledge of the encoding parameters.<sup><a data-goto="rx-refs">[5, 6]</a></sup> It also requires additional identifying attributes, such as names and dates of birth. Exact matching on a single consented identifier, under a key held by one linkage service, was the more conservative choice, accepting missed links in preference to false ones or wider collection. It did not resolve the custody problem.</p>
    </section>

    <section id="rx-health">
      <h2><span>5</span>Lessons from Australian health</h2>
      <p>Australia has one of the most mature record-linkage environments in the world, and its health researchers have shown for decades that linkage can serve people well when it is governed carefully. It was the natural reference point.</p>
      <figure class="rx-fig">
        <ol class="rx-time">
          <li><span>1995</span><div><b>WA Data Linkage System</b><p>Established in Western Australia; now the longest-running linkage system in Australia, supporting hundreds of research projects.<sup><a data-goto="rx-refs">[1]</a></sup></p></div></li>
          <li><span>2009&ndash;12</span><div><b>National infrastructure</b><p>The Population Health Research Network, under the National Collaborative Research Infrastructure Strategy, establishes linkage units in every state and a Centre for Data Linkage for cross-jurisdictional research.<sup><a data-goto="rx-refs">[2]</a></sup></p></div></li>
          <li><span>2018</span><div><b>Evaluated at scale</b><p>A NSW evaluation links primary-care records from 16 general practices to tens of millions of hospital records using privacy-preserving methods.<sup><a data-goto="rx-refs">[4]</a></sup></p></div></li>
          <li><span>2018</span><div><b>Evaluated adversarially</b><p>Researchers at the Australian National University publish efficient attacks on Bloom-filter encodings, shaping safer designs.<sup><a data-goto="rx-refs">[5]</a></sup></p></div></li>
          <li><span>2022</span><div><b>Accuracy established</b><p>A blinded WA evaluation finds 99.3% of groupings identical between privacy-preserving and clear-text linkage.<sup><a data-goto="rx-refs">[3]</a></sup></p></div></li>
          <li class="rx-now"><span>2026</span><div><b>Assessed for ministry</b><p>Always implements and evaluates consent-based linkage across ministries, and declines to deploy it.</p></div></li>
        </ol>
        <figcaption><span class="rx-fn">Figure 6</span> Three decades of Australian record linkage, and the point at which the Foundation stopped.</figcaption>
      </figure>
      <p>Two lessons carry across directly. The first is separation of duties: those who hold records are not those who link them, and those who link do not need the content. The second is that governance matters as much as cryptography: custodians, approvals, audit and published methods are what earn public trust. Much health research proceeds under an ethics-approved waiver of consent;<sup><a data-goto="rx-refs">[1]</a></sup> the ministry design would have required each person&rsquo;s own consent.</p>
      <p>The safety of health linkage derives less from its cryptography than from its institutional setting: enabling legislation, ethics review, and units that link records without holding them. That setting was built over decades by public institutions. A voluntary network of churches and ministries has no equivalent, and it would be inappropriate for a small foundation to attempt to become one.</p>
    </section>

    <section id="rx-environment">
      <h2><span>6</span>Threat environment</h2>
      <p>Any system that connects independent organisations acquires the characteristics of infrastructure, and with them its exposure. The Australian Signals Directorate assesses state-sponsored actors as a serious and growing threat to government, critical infrastructure and business networks.<sup><a data-goto="rx-refs">[7]</a></sup></p>
      <figure class="rx-fig">
        <div class="rx-stats">
          <div><b>1,200+</b><span>cyber incidents responded to by ASD&rsquo;s ACSC in 2024&ndash;25, up 11%</span></div>
          <div><b>190+</b><span>notifications to critical infrastructure of malicious activity, up 111%</span></div>
          <div><b>95%</b><span>of healthcare and social assistance incidents in which attackers succeeded</span></div>
        </div>
        <div class="rx-bars" role="img" aria-label="People affected by major Australian breaches: MediSecure 2024, 12.9 million; Optus 2022, 10 million; Medibank 2022, 9.7 million.">
          <p>People affected by major Australian breaches, millions</p>
          <div style="--w:100%"><span>MediSecure, 2024</span><i></i><b>12.9</b></div>
          <div style="--w:77.5%"><span>Optus, 2022</span><i></i><b>10.0</b></div>
          <div style="--w:75.2%"><span>Medibank, 2022</span><i></i><b>9.7</b></div>
        </div>
        <figcaption><span class="rx-fn">Figure 7</span> The threat environment. Sources: ASD&rsquo;s Annual Cyber Threat Report 2024&ndash;25; OAIC; AAP.<sup><a data-goto="rx-refs">[7, 8, 9]</a></sup></figcaption>
      </figure>
      <p>The MediSecure breach, affecting approximately 12.9 million people&rsquo;s personal and health information, is the largest notified under the Notifiable Data Breaches scheme.<sup><a data-goto="rx-refs">[8]</a></sup> A linked record of who responded to the Gospel, and where they subsequently went, would rank among the most sensitive collections in the country. PPRL raises the cost of exploiting such a record. Declining to create it removes the record altogether.</p>
    </section>

    <section id="rx-open">
      <h2><span>7</span>Open source as assurance</h2>
      <p>Because the security of keyed linkage rests on the secrecy of the key, the method itself can be public, in the same way that the cryptography protecting online banking is published. Open code allows a church volunteer, an independent reviewer or a regulator to verify what is collected and who sees what; allows flaws to be found and corrected sooner; gives reviews an exact artefact to test; and ensures that no church depends on a single organisation&rsquo;s continued existence. The keys, the data and every access token remain private. The same openness now allows anyone to verify that the implementation has been removed.</p>
    </section>

    <section id="rx-assessment">
      <h2><span>8</span>Assessment</h2>
      <figure class="rx-fig">
        <div class="rx-tw"><table class="rx-table rx-two">
          <thead><tr><th scope="col">Benefits</th><th scope="col">Costs</th></tr></thead>
          <tbody>
            <tr><td>Visibility of progression between ministries</td><td>A key and link set attractive to theft and compulsion</td></tr>
            <tr><td>De-duplicated network totals</td><td>Re-identification risk in small communities</td></tr>
            <tr><td>Reduced manual coordination</td><td>A commitment to individuals beyond an introduction to one church</td></tr>
            <tr><td></td><td>Structural pressure to extend scope</td></tr>
          </tbody>
        </table></div>
        <figcaption><span class="rx-fn">Figure 8</span> The assessment. Most benefits are obtainable by other means (section 10). The costs are intrinsic to the capability.</figcaption>
      </figure>
      <h3>8.1 Timing</h3>
      <p>The assessment was completed while the system functioned and before any dependency had formed: no personal information had been processed, no ministry workflows relied on it, and no funder reporting had been built upon it. Decisions of this kind become materially harder once a capability is embedded in operations and expectations.</p>
      <h3>8.2 Limited deployment</h3>
      <p>Restricting linkage to selected high-impact programmes would reduce the number of individuals exposed without reducing the principal risks. Smaller cohorts are more readily re-identified, the key retains its value irrespective of scale, and an exception granted to one funder establishes a precedent for the next.</p>
      <h3>8.3 Legal context</h3>
      <p>Australian law does not prohibit record linkage, but classifies religious belief as sensitive information. Under the Privacy Act 1988, collection generally requires consent, and use or disclosure is confined to the primary purpose or a directly related secondary purpose the individual would reasonably expect. A Children&rsquo;s Online Privacy Code is required to be registered by 10 December 2026, imposing further obligations for children&rsquo;s information online.<sup><a data-goto="rx-refs">[14]</a></sup> The Foundation&rsquo;s position is more restrictive than the law requires.</p>
      <h3>8.4 Limitations of the design</h3>
      <ul>
        <li><em>Coverage.</em> Only steps recorded through Always would have been counted.</li>
        <li><em>Exact matching.</em> A single identifier misses people who change numbers.</li>
        <li><em>Trust in the linkage service.</em> Review, open code and audit reduce the trust required of Always; they do not remove it.</li>
        <li><em>Contribution and cause.</em> Linked records describe what happened, not why. Fruit belongs to God; data can only support better care.</li>
      </ul>
    </section>

    <section id="rx-church">
      <h2><span>9</span>The local church as privacy architecture</h2>
      <p>The church has always existed as many local congregations, each responsible for the care of its own people. That structure is a strength for privacy as well as for pastoral care.</p>
      <div class="rx-pair">
        <div><h3>No central register</h3><p>Where each congregation holds its own records, there is no single collection to steal, sell or seize, and a compromise at one does not expose another.</p></div>
        <div><h3>Care where people are known</h3><p>A person who asks to be introduced is referred to one church, with their permission, and that church assumes their care. Always facilitates the introduction and retains nothing further.</p></div>
      </div>
      <p>Always Platform follows the same principle. It connects churches and ministries while leaving each responsible for its own people.</p>
    </section>

    <section id="rx-instead">
      <h2><span>10</span>Evidence without linkage</h2>
      <p>Most questions asked by ministries and funders can be answered without recognising any individual across organisations.</p>
      <figure class="rx-fig">
        <div class="rx-tw"><table class="rx-table">
          <thead><tr><th scope="col">Question</th><th scope="col">Method</th><th scope="col">Disclosure</th><th scope="col">Linkage</th></tr></thead>
          <tbody>
            <tr><th scope="row">Did respondents at this event join a church?</th><td>Handoff outcomes recorded by the receiving church</td><td>Aggregates per event</td><td>Not required</td></tr>
            <tr><th scope="row">Are they still connected after some months?</th><td>Self-report collected by the chosen church, with consent to count</td><td>Aggregates only</td><td>Not required</td></tr>
            <tr><th scope="row">How is a ministry performing over time?</th><td>The ministry&rsquo;s own handoffs and outcomes by month</td><td>That ministry</td><td>Not required</td></tr>
            <tr><th scope="row">What is happening across the network?</th><td>Totals across partners, small groups suppressed</td><td>Aggregates only</td><td>Not required</td></tr>
            <tr><th scope="row">Did a programme cause the outcome?</th><td>Not identifiable from routine data</td><td>&mdash;</td><td>Research study</td></tr>
          </tbody>
        </table></div>
        <figcaption><span class="rx-fn">Figure 9</span> Evidence without linkage. Only causal attribution requires linkage, and it is properly a research question.</figcaption>
      </figure>
    </section>

    <section id="rx-conditions">
      <h2><span>11</span>Conditions for any future study</h2>
      <p>Should causal attribution ever be required, it would need to be pursued as a discrete study conducted outside Always. The following are minimum conditions for consideration:</p>
      <ol class="rx-cond">
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
    </section>

    <section id="rx-decision" class="rx-decision">
      <h2><span>12</span>Decision</h2>
      <dl class="rx-adr">
        <div><dt>Record</dt><dd>ADR 0013</dd></div>
        <div><dt>Title</dt><dd>No linkage of individuals across organisations</dd></div>
        <div><dt>Status</dt><dd><span class="rx-status">Accepted</span></dd></div>
        <div><dt>Date</dt><dd>21 November 2026</dd></div>
        <div><dt>Supersedes</dt><dd>ADR 0012, Journeys across ministries (withdrawn)</dd></div>
      </dl>
      <p class="rx-verdict">Always does not link individuals across organisations, at any scale or under any name.</p>
      <p>The prohibition covers persistent identity linkage between organisations, central reconstruction of a person&rsquo;s journey, shared fingerprints or matching codes, databases of religious participation histories, and analytics across ministries that recognise the same individual. It binds the Foundation&rsquo;s code, its partners and its funders.</p>
      <p>Participant-initiated referrals to a chosen church or ministry, each organisation&rsquo;s own reporting, and aggregate statistics that do not link individuals across organisations remain within scope.</p>
      <p>The implementation and its database objects have been removed. Exceptions for major funders or high-impact programmes are excluded. Any future proposal must meet the conditions in section 11 and be decided in the open, so that the decision does not depend on the continued presence of those who made it.</p>
      <p class="rx-close">The technical capacity to build a capability and the institutional standing to hold it are distinct questions. For an organisation constituted to serve independent churches, the second is decisive.</p>
    </section>

    <section id="rx-refs" class="rx-refs">
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
      <p class="rx-note">This research case study does not constitute legal advice. Nothing described here operates on Always Platform. Correspondence is welcome at <a href="mailto:hello@alwaysfoundation.org">hello@alwaysfoundation.org</a>.</p>
    </section>
  </div>
</div></div>
</article>
'''

CSS = r'''.rx { --rx-ivory: #FBF7EE; --rx-paper: #FFFDF8; --rx-ink: #1B4740; --rx-deep: #14352F; --rx-text: #26332F; --rx-soft: #55635D; --rx-rule: rgba(27,71,64,.18); --rx-wash: #EDF2EC; --rx-amber: #8F5A10; --rx-amber-lt: #E6B86A; }
.rx-mast { background: var(--rx-deep); color: var(--cream); padding: 168px 0 64px; }
.rx-mast-in { max-width: 1040px; }
.rx-series { margin: 0 0 26px; font: 500 14px/1 var(--text); color: rgba(255,253,248,.66); }
.rx-series a { color: inherit; text-underline-offset: 3px; }
.rx-mast h1 { margin: 0; max-width: 17ch; font-family: var(--serif); font-weight: 500; font-size: clamp(40px, 5.6vw, 70px); line-height: 1.04; letter-spacing: -0.018em; color: var(--rx-paper); }
.rx-dek { margin: 26px 0 0; max-width: 58ch; font-size: clamp(18px, 1.6vw, 20px); line-height: 1.6; color: rgba(255,253,248,.82); }
.rx-front { display: grid; grid-template-columns: 1fr 1.5fr 1.4fr; gap: 32px; max-width: 980px; margin: 48px 0 0; padding: 22px 0 0; border-top: 1px solid rgba(255,253,248,.2); }
.rx-front dt { margin: 0 0 6px; font: 500 13px/1.3 var(--text); color: rgba(255,253,248,.56); }
.rx-front dd { margin: 0; font-size: 15px; line-height: 1.55; color: rgba(255,253,248,.9); }
.rx-front .rx-status { color: var(--rx-amber-lt); }
.rx-status { font-weight: 600; color: var(--rx-amber); }
.rx-sheet { background: var(--rx-ivory); }
.rx-body { display: grid; grid-template-columns: 210px minmax(0, 1fr); gap: 72px; padding-top: 72px; padding-bottom: 112px; }
.rx-toc { position: sticky; top: 100px; align-self: start; display: flex; flex-direction: column; border-left: 1px solid var(--rx-rule); }
.rx-toc p { margin: 0 0 12px; padding-left: 16px; font: 600 13px/1 var(--text); color: var(--rx-soft); }
.rx-toc button { min-height: 34px; margin-left: -1px; padding: 6px 0 6px 15px; border: 0; border-left: 2px solid transparent; background: none; text-align: left; font: 400 14px/1.35 var(--text); color: var(--rx-soft); cursor: pointer; }
.rx-toc button:hover { color: var(--rx-ink); }
.rx-toc button.on { border-left-color: var(--rx-ink); color: var(--rx-ink); font-weight: 600; }
.rx-toc button:focus-visible { outline: 2px solid var(--rx-ink); outline-offset: 2px; }
.rx-main { max-width: 720px; }
.rx-main section { scroll-margin-top: 100px; }
.rx-main section + section { margin-top: 80px; }
.rx-main h2 { display: flex; align-items: baseline; gap: 16px; margin: 0 0 22px; font-family: var(--serif); font-weight: 500; font-size: clamp(28px, 3vw, 38px); line-height: 1.12; letter-spacing: -0.01em; color: var(--rx-ink); }
.rx-main h2 span { flex: none; font: 600 15px/1 var(--text); color: var(--rx-soft); font-variant-numeric: tabular-nums; transform: translateY(-4px); }
.rx-main h3 { margin: 36px 0 10px; font: 600 17px/1.35 var(--text); color: var(--rx-ink); }
.rx-main p, .rx-main li { font-size: 17.5px; line-height: 1.75; color: var(--rx-text); }
.rx-main p { margin: 0 0 18px; }
.rx-main ul, .rx-main ol { margin: 0 0 18px; padding-left: 22px; }
.rx-main li { margin-bottom: 10px; }
.rx-main em { font-style: normal; font-weight: 600; color: var(--rx-ink); }
.rx-main code { font-size: .86em; padding: 1px 5px; border-radius: 4px; background: var(--rx-wash); color: var(--rx-ink); }
.rx-main sup a { font: 600 12px/1 var(--text); color: var(--rx-ink); text-decoration: none; cursor: pointer; }
.rx-main sup a:hover { text-decoration: underline; }
.rx-main a { color: var(--rx-ink); text-underline-offset: 3px; }
.rx-prologue h2 { font-size: clamp(32px, 3.8vw, 46px); }
.rx-lead { font-family: var(--serif); font-size: 23px !important; line-height: 1.55 !important; color: var(--rx-ink) !important; }
.rx-pair { display: grid; grid-template-columns: 1fr 1fr; margin: 30px 0 28px; border-top: 1px solid var(--rx-rule); border-bottom: 1px solid var(--rx-rule); }
.rx-pair > div { padding: 22px 28px 22px 0; }
.rx-pair > div + div { padding: 22px 0 22px 28px; border-left: 1px solid var(--rx-rule); }
.rx-pair h3 { margin: 0 0 8px; }
.rx-pair p { margin: 0; font-size: 16.5px; line-height: 1.65; }
.rx-abstract { padding: 34px 0 30px; border-top: 2px solid var(--rx-ink); border-bottom: 1px solid var(--rx-rule); }
.rx-abstract h2 { font-size: 28px; }
.rx-keys { display: grid; grid-template-columns: 1fr 1fr; gap: 16px 32px; margin: 26px 0 0; padding-top: 20px; border-top: 1px solid var(--rx-rule); }
.rx-keys dt { font: 600 13px/1.3 var(--text); color: var(--rx-soft); }
.rx-keys dd { margin: 4px 0 0; font-size: 15.5px; line-height: 1.5; color: var(--rx-ink); }
.rx-fig { margin: 38px 0 42px; }
.rx-fig > svg { display: block; width: 100%; height: auto; padding: 26px; background: var(--rx-paper); border: 1px solid var(--rx-rule); border-radius: 4px; }
.rx-fig figcaption { margin-top: 14px; font-size: 14.5px; line-height: 1.6; color: var(--rx-soft); }
.rx-fn { margin-right: 8px; font-weight: 600; color: var(--rx-amber); }
.rx-tw { overflow-x: auto; }
.rx-table { width: 100%; border-collapse: collapse; border-top: 2px solid var(--rx-ink); border-bottom: 2px solid var(--rx-ink); font-size: 15px; line-height: 1.5; }
.rx-table th, .rx-table td { padding: 12px 14px 12px 0; text-align: left; vertical-align: top; color: var(--rx-text); }
.rx-table thead th { font-weight: 600; color: var(--rx-ink); border-bottom: 1px solid var(--rx-ink); font-size: 14px; }
.rx-table tbody tr + tr th, .rx-table tbody tr + tr td { border-top: 1px solid var(--rx-rule); }
.rx-table tbody th { font-weight: 600; color: var(--rx-ink); min-width: 150px; }
.rx-table .rx-hl th, .rx-table .rx-hl td { background: var(--rx-wash); }
.rx-table .rx-hl th { padding-left: 10px; }
.rx-two td { width: 50%; }
.rx-legend { list-style: none; margin: 18px 0 0; padding: 0; display: grid; gap: 10px; }
.rx-legend li { display: grid; grid-template-columns: 28px 1fr; gap: 12px; margin: 0; font-size: 15px; line-height: 1.6; }
.rx-legend b { width: 24px; height: 24px; margin-top: 1px; border-radius: 50%; background: var(--rx-deep); color: var(--rx-paper); display: flex; align-items: center; justify-content: center; font: 700 12.5px/1 var(--text); }
.rx-risks { margin: 10px 0 18px; border-top: 1px solid var(--rx-ink); }
.rx-risks div { display: grid; grid-template-columns: 200px 1fr; gap: 28px; padding: 16px 0; border-bottom: 1px solid var(--rx-rule); }
.rx-risks dt { font: 600 15.5px/1.5 var(--text); color: var(--rx-ink); }
.rx-risks dd { margin: 0; font-size: 16px; line-height: 1.65; color: var(--rx-text); }
.rx-time { list-style: none; margin: 0; padding: 0; border-top: 1px solid var(--rx-ink); }
.rx-time li { display: grid; grid-template-columns: 96px 1fr; gap: 24px; margin: 0; padding: 16px 0; border-bottom: 1px solid var(--rx-rule); }
.rx-time li > span { font: 600 15px/1.5 var(--text); color: var(--rx-ink); font-variant-numeric: tabular-nums; }
.rx-time b { display: block; font: 600 16px/1.4 var(--text); color: var(--rx-ink); }
.rx-time p { margin: 4px 0 0; font-size: 15.5px; line-height: 1.6; }
.rx-time .rx-now > span, .rx-time .rx-now b { color: var(--rx-amber); }
.rx-stats { display: grid; grid-template-columns: repeat(3, 1fr); border-top: 1px solid var(--rx-ink); border-bottom: 1px solid var(--rx-rule); }
.rx-stats div { padding: 20px 20px 20px 0; }
.rx-stats div + div { padding-left: 20px; border-left: 1px solid var(--rx-rule); }
.rx-stats b { display: block; font-family: var(--serif); font-weight: 500; font-size: 40px; line-height: 1; color: var(--rx-ink); }
.rx-stats span { display: block; margin-top: 10px; font-size: 14px; line-height: 1.5; color: var(--rx-soft); }
.rx-bars { margin-top: 26px; }
.rx-bars p { margin: 0 0 12px; font: 600 14px/1.4 var(--text); color: var(--rx-ink); }
.rx-bars div { display: grid; grid-template-columns: 150px 1fr 44px; align-items: center; gap: 14px; padding: 6px 0; }
.rx-bars span { font-size: 14px; color: var(--rx-text); }
.rx-bars i { display: block; height: 10px; width: var(--w); background: var(--rx-ink); border-radius: 1px; }
.rx-bars b { font: 600 14px/1 var(--text); color: var(--rx-ink); text-align: right; font-variant-numeric: tabular-nums; }
.rx-cond li::marker { font-weight: 600; color: var(--rx-ink); }
.rx-decision { padding-top: 34px; border-top: 2px solid var(--rx-ink); }
.rx-adr { display: grid; grid-template-columns: repeat(5, auto); gap: 10px 28px; justify-content: start; margin: 0 0 30px; padding-bottom: 20px; border-bottom: 1px solid var(--rx-rule); }
.rx-adr dt { font: 500 12.5px/1.3 var(--text); color: var(--rx-soft); }
.rx-adr dd { margin: 4px 0 0; font-size: 14.5px; line-height: 1.45; color: var(--rx-ink); }
.rx-verdict { font-family: var(--serif); font-size: clamp(24px, 2.6vw, 30px) !important; line-height: 1.35 !important; color: var(--rx-ink) !important; margin-bottom: 24px !important; }
.rx-close { margin-top: 30px !important; padding-top: 22px; border-top: 1px solid var(--rx-rule); font-family: var(--serif); font-style: italic; font-size: 21px !important; line-height: 1.55 !important; color: var(--rx-ink) !important; }
.rx-refs { padding-top: 30px; border-top: 1px solid var(--rx-rule); }
.rx-refs h2 { font-size: 24px; }
.rx-refs li { font-size: 14.5px; line-height: 1.6; color: var(--rx-soft); }
.rx-note { margin-top: 24px !important; font-size: 14px !important; color: var(--rx-soft) !important; }
@media (max-width: 1000px) {
  .rx-body { grid-template-columns: minmax(0, 1fr); gap: 0; }
  .rx-toc { display: none; }
  .rx-adr { grid-template-columns: repeat(2, auto); }
}
@media (max-width: 700px) {
  .rx-mast { padding: 124px 0 44px; }
  .rx-front, .rx-keys, .rx-pair, .rx-stats { grid-template-columns: minmax(0, 1fr); }
  .rx-front { gap: 16px; }
  .rx-pair > div, .rx-pair > div + div { padding: 18px 0; border-left: 0; }
  .rx-pair > div + div { border-top: 1px solid var(--rx-rule); }
  .rx-stats div, .rx-stats div + div { padding: 16px 0; border-left: 0; }
  .rx-stats div + div { border-top: 1px solid var(--rx-rule); }
  .rx-risks div, .rx-time li { grid-template-columns: minmax(0, 1fr); gap: 4px; }
  .rx-bars div { grid-template-columns: 1fr 40px; }
  .rx-bars span { grid-column: 1 / -1; }
  .rx-wide { overflow-x: auto; -webkit-overflow-scrolling: touch; }
  .rx-wide > svg { min-width: 680px; padding: 14px; }
  .rx-wide figcaption, .rx-wide .rx-legend { position: sticky; left: 0; max-width: calc(100vw - 44px); }
  .rx-main section + section { margin-top: 60px; }
}
'''

JS = r'''
document.addEventListener('click', (e) => {
  const b = e.target.closest('[data-goto]'); if (!b) return;
  const t = document.getElementById(b.dataset.goto); if (!t) return;
  e.preventDefault();
  t.scrollIntoView({ behavior: matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth', block: 'start' });
});
(() => {
  if (!('IntersectionObserver' in window)) return;
  const setup = () => {
    const toc = document.querySelector('.rx-toc'); if (!toc || toc.dataset.ready) return; toc.dataset.ready = '1';
    const btns = [...toc.querySelectorAll('button')];
    const io = new IntersectionObserver((es) => es.forEach((en) => { if (en.isIntersecting) btns.forEach((x) => x.classList.toggle('on', x.dataset.goto === en.target.id)); }), { rootMargin: '-110px 0px -70% 0px' });
    btns.forEach((x) => { const s = document.getElementById(x.dataset.goto); if (s) io.observe(s); });
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
