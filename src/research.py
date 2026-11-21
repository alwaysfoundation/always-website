"""Research case study: privacy-preserving record linkage for Gospel impact research."""

import research_figs as F

SLUG = 'pprl'
TITLE = 'Privacy-Preserving Record Linkage for Gospel Impact Research \u00b7 Always Foundation'

TOC = [('rx-abstract', '1. Abstract'), ('rx-problem', '2. Research problem'), ('rx-prior', '3. Prior research'), ('rx-design', '4. Architecture'), ('rx-testing', '5. Testing and findings'), ('rx-threats', '6. Threats and limitations'), ('rx-alternatives', '7. Alternatives and future research'), ('rx-decision', '8. Institutional decision'), ('rx-refs', '9. References')]


def _toc():
    return ''.join(f'<button type="button" data-goto="{i}">{t}</button>' for i, t in TOC)


PAGE = '''
<article class="rx">
<div class="rx-mast"><div class="wrap rx-mast-in">
  <p class="rx-series"><a href="#/stories">Stories</a> <span aria-hidden="true">/</span> Research case study</p>
  <h1>Privacy-Preserving Record Linkage for Gospel Impact Research</h1>
  <p class="rx-dek">An applied research case study in cross-ministry record linkage, cryptographic architecture and institutional risk.</p>
  <dl class="rx-front">
    <div><dt>Published</dt><dd>Always Foundation, November 2026</dd></div>
    <div><dt>Scope</dt><dd>Research problem, prior literature, architecture, implementation, testing, threat model and institutional decision</dd></div>
    <div><dt>Technical record</dt><dd>ADR 0012 (withdrawn); ADR 0013</dd></div>
  </dl>
  <p class="rx-state"><b>Research status: Not deployed.</b> The proposed architecture was implemented and tested but never operated with real participant records. Always Foundation subsequently removed the implementation and does not operate cross-organisation person linkage. See <a data-goto="rx-decision" href="#/pprl">ADR 0013</a>.</p>
</div></div>

<div class="rx-sheet"><div class="wrap rx-body">
  <nav class="rx-toc" aria-label="Contents"><p>Contents</p>''' + _toc() + '''</nav>

  <div class="rx-main">
    <section id="rx-abstract" class="rx-abstract">
      <h2><span>1</span>Abstract</h2>
      <p><em>Background.</em> People rarely come to faith, or grow in it, through a single organisation. A person may respond at an event, complete a course run by another ministry, read the Bible with a friend and later join a local church. Each organisation observes one stage. Funders and networks supporting many independent ministries can therefore measure activity, but not progression between ministries, and cannot avoid counting one person several times.</p>
      <p><em>Objective.</em> To determine whether independent ministries could recognise records relating to the same consenting adult without exchanging their databases, and what institutional risks such a capability would carry.</p>
      <p><em>Method.</em> We reviewed Australian health research on privacy-preserving record linkage (PPRL), designed a consent-based, deterministic linkage architecture using HMAC-SHA256 over a normalised mobile number with organisation-specific identifiers, implemented it in Always Platform, and tested it against synthetic data. We then conducted a threat analysis of the design in its intended institutional setting.</p>
      <p><em>Results.</em> The implementation met its functional and access-control specifications under automated tests: consent and age rules were enforced by the database, organisations received uncorrelated identifiers, and withdrawal removed links. Linkage accuracy was not evaluated. The threat analysis identified residual risks that the design does not remove, chiefly the concentration of key custody in a single organisation, re-identification from milestone sequences in small communities, compelled disclosure, and growth in the dataset&rsquo;s sensitivity with adoption.</p>
      <p><em>Conclusion.</em> Always Foundation decided not to deploy this architecture on its platform and recorded a standing prohibition on cross-organisation person linkage (ADR 0013). The decision concerns Always&rsquo;s own role and this design. It is not a general conclusion about PPRL, and cross-ministry longitudinal measurement remains a genuine and important research problem.</p>
    </section>

    <section id="rx-problem">
      <h2><span>2</span>Research problem and significance</h2>
      <p>Consider a hypothetical individual, Sam, who responds at a youth event in February, enrols in a course run by another ministry in March, joins a Bible reading group through a third in April, and is welcomed by a local church in May. Four organisations each hold one record. None can observe the sequence.</p>
      <figure class="rx-fig rx-wide">''' + F.journey() + '''<figcaption><span class="rx-fn">Figure 1</span> One individual, four organisations. Each organisation holds its own record. Linkage would reconstruct the sequence by creating a linked record held by the linkage service.</figcaption></figure>
      <h3>2.1 Significance</h3>
      <p>For a single ministry, the consequence is incomplete follow-up: an event team does not learn whether a respondent found a church, and a church does not know what steps a newcomer has already taken. For funders and networks it is a measurement problem. Organisations supporting evangelism, discipleship and church planting across many independent ministries receive substantial activity data, but cannot observe whether the same individuals progress from one ministry to the next. The sector&rsquo;s fragmentation, with different systems, different data and different levels of technical capacity, has made the problem difficult even to formulate technically.</p>
      <p>Australian health research faces a structurally similar problem: sensitive records about the same people held by separate custodians. Pastoral and clinical care have long been compared. Martyn Lloyd-Jones trained in medicine at St Bartholomew&rsquo;s Hospital and worked as assistant to the Royal Physician, Sir Thomas Horder, before spending two years deciding whether to give up medicine to become a &lsquo;physician of the soul&rsquo;; in 1927 he accepted a call to a struggling church in Aberavon, Port Talbot.<sup><a data-goto="rx-refs">[10, 11]</a></sup> The analogy made health information practice a natural point of departure.</p>
      <h3>2.2 Research questions</h3>
      <ol>
        <li>Can independent ministries recognise records relating to the same consenting adult without exchanging their databases?</li>
        <li>What architecture, drawing on established PPRL practice, would achieve this with the least collection and disclosure?</li>
        <li>What residual risks and governance requirements would such a capability carry in a voluntary network of churches and ministries?</li>
      </ol>
      <h3>2.3 What linkage can and cannot show</h3>
      <p>Record linkage joins recorded events, such as a response, an introduction or a welcome. It does not establish that one event caused another, and it does not measure spiritual conversion or growth, which no administrative record can observe. Any use of linked data for impact assessment would need to be interpreted within those limits.</p>
    </section>

    <section id="rx-prior">
      <h2><span>3</span>Prior research: Australian healthcare and PPRL</h2>
      <p>This section summarises established findings from the literature. None of these results was produced by Always, and none validates Always&rsquo;s implementation, which used a different method on different data.</p>
      <h3>3.1 Record linkage and its privacy-preserving form</h3>
      <p>Record linkage identifies records that refer to the same individual across separate collections. Privacy-preserving record linkage performs this without the collections disclosing identifying information to one another. In the trusted-third-party model common in Australian health, each data custodian supplies only encoded identifiers to a linkage unit, which determines matches and returns link keys in place of identities.<sup><a data-goto="rx-refs">[1, 2]</a></sup></p>
      <h3>3.2 Deterministic and probabilistic methods</h3>
      <p><em>Deterministic matching on keyed hashes</em> applies a secret-keyed one-way function to a normalised identifier. Two records match only if their encodings are identical, so any variation in the identifier produces a missed link. <em>Probabilistic matching on Bloom-filter encodings</em> splits identifiers such as names into character fragments and sets bits in a filter. Encodings can then be compared for similarity, which tolerates spelling and transcription variation and supports probabilistic match decisions.<sup><a data-goto="rx-refs">[3, 4]</a></sup> The Australian evaluations below concern Bloom-filter methods.</p>
      <h3>3.3 Infrastructure and evaluation</h3>
      <figure class="rx-fig">
        <ol class="rx-time">
          <li><span>1995</span><div><b>WA Data Linkage System</b><p>Established in Western Australia; described as Australia&rsquo;s longest-running data linkage agency, with linked data used in over 800 research projects.<sup><a data-goto="rx-refs">[1]</a></sup></p></div></li>
          <li><span>2006&ndash;10</span><div><b>Population Health Research Network</b><p>National investment under the National Collaborative Research Infrastructure Strategy funds linkage units in each state and a Centre for Data Linkage for cross-jurisdictional linkage, whose operating model was endorsed in 2010.<sup><a data-goto="rx-refs">[2]</a></sup></p></div></li>
          <li><span>2014</span><div><b>Cryptanalysis of basic Bloom filters</b><p>Niedermeyer and colleagues show that an attack on bigram-based Bloom filters can decipher an entire database of encrypted surnames.<sup><a data-goto="rx-refs">[6]</a></sup></p></div></li>
          <li><span>2018</span><div><b>Real-world performance, NSW</b><p>Linkage of 272,202 primary-care records from 16 general practices with 42.8 million emergency, hospital and death records achieved precision, recall and F-measure above 0.90 against a probabilistic gold standard, and about 0.98 to 0.99 when existing links were used.<sup><a data-goto="rx-refs">[4]</a></sup></p></div></li>
          <li><span>2019</span><div><b>Precise and fast cryptanalysis</b><p>Christen and colleagues present an attack that re-identifies attribute values encoded in Bloom filters from large real-world databases in minutes.<sup><a data-goto="rx-refs">[5]</a></sup></p></div></li>
          <li><span>2022</span><div><b>Blinded evaluation, WA</b><p>Hospital morbidity and death records for 2011&ndash;2015 linked with Bloom filters in a blinded setting produced 99.3% of groupings identical to clear-text linkage.<sup><a data-goto="rx-refs">[3]</a></sup></p></div></li>
        </ol>
        <figcaption><span class="rx-fn">Figure 2</span> Selected milestones in Australian record linkage and PPRL research. All results are from the cited literature.</figcaption>
      </figure>
      <h3>3.4 Governance and consent</h3>
      <p>Health linkage operates within an institutional setting that complements its cryptography: separation between custodians and linkers, enabling legislation, ethics review and published methods. Most population health research facilitated by the WA linkage branch proceeds under an ethics-approved waiver of consent.<sup><a data-goto="rx-refs">[1]</a></sup> The ministry design examined here would instead have required each person&rsquo;s own consent.</p>
    </section>

    <section id="rx-design">
      <h2><span>4</span>Technical architecture and implementation</h2>
      <p>The design was implemented within the Always Platform API and PostgreSQL database, published as open source and recorded in ADR 0012.<sup><a data-goto="rx-refs">[12]</a></sup> Its tables and triggers were introduced by database migration and are removed by migration 0022.</p>
      <figure class="rx-fig">
        <div class="rx-tw"><table class="rx-table">
          <caption><span class="rx-fn">Table 1</span> Design options considered.</caption>
          <thead><tr><th scope="col"></th><th scope="col">Pooled database</th><th scope="col">Manual reconciliation</th><th scope="col">Keyed-hash PPRL (chosen)</th></tr></thead>
          <tbody>
            <tr><th scope="row">Records exchanged</th><td>All, with every participant</td><td>Identities circulated between staff</td><td>None; encoded identifiers only</td></tr>
            <tr><th scope="row">Effect of one breach</th><td>Every record exposed</td><td>Scattered and untracked</td><td>Fingerprints, unusable without the key</td></tr>
            <tr><th scope="row">Matching</th><td>Exact or fuzzy, in the clear</td><td>Manual judgement</td><td>Deterministic, exact</td></tr>
            <tr><th scope="row">Residual trust</th><td>Every participant</td><td>Every recipient</td><td>The linkage service and its keys</td></tr>
          </tbody>
        </table></div>
      </figure>
      <figure class="rx-fig rx-wide">''' + F.hmac() + '''<figcaption><span class="rx-fn">Figure 3</span> Linkage architecture as implemented. The number is normalised and transformed under <code>LINK_KEY</code>, held outside the database. The fingerprint is matched to a journey, which each organisation sees under an identifier derived with <code>ORG_CODE_KEY</code>. Values are illustrative.</figcaption></figure>

      <h3>4.1 Consent and eligibility</h3>
      <p>Linkage required a distinct consent purpose, <code>share.journey</code>, never pre-selected and separate from consent to be introduced to a church. The API rejected the purpose for anyone under 18. Independently of the API, database constraints refused to link a minor or to link without a current, unwithdrawn consent. These rules were not configurable.</p>
      <h3>4.2 Identifier normalisation</h3>
      <p>Australian mobile numbers are written in many forms. Before transformation each was reduced to a canonical form, <code>+614XXXXXXXX</code>, so that the same number always produced the same fingerprint. Identifiers that were not Australian mobile numbers were not linked.</p>
      <h3>4.3 Keyed fingerprint</h3>
      <p>The fingerprint was <code>HMAC-SHA256(LINK_KEY, normalised number)</code>, a standard keyed hash.<sup><a data-goto="rx-refs">[13]</a></sup> <code>LINK_KEY</code> was supplied through the runtime environment, held apart from the database and from authentication secrets, so that it could be rotated or destroyed independently. Without the key a fingerprint can be neither computed from a number nor inverted to recover one. Matching was deterministic: equal fingerprints were treated as the same person.</p>
      <h3>4.4 Organisation-specific identifiers</h3>
      <p>No organisation received the fingerprint or the internal journey identifier. Each received <code>HMAC(ORG_CODE_KEY, journey id | organisation id)</code>, stable within that organisation and uncorrelated across organisations, so that two organisations comparing exports could not establish that they held the same individual.</p>
      <h3>4.5 Disclosure</h3>
      <figure class="rx-fig">
        <div class="rx-tw"><table class="rx-table">
          <caption><span class="rx-fn">Table 2</span> Disclosure by party.</caption>
          <thead><tr><th scope="col">Party</th><th scope="col">Identity</th><th scope="col">Milestones</th><th scope="col">Notes</th></tr></thead>
          <tbody>
            <tr><th scope="row">The individual</th><td>Own</td><td>All; withdrawal at any time</td><td>&mdash;</td></tr>
            <tr><th scope="row">Each organisation on the journey</th><td>Its own record only</td><td>Milestone and month</td><td>Its own only</td></tr>
            <tr class="rx-hl"><th scope="row">Always Platform</th><td>Fingerprints and keys</td><td>As required to operate</td><td>None</td></tr>
            <tr><th scope="row">Funders and networks</th><td>None</td><td>Aggregates; groups under 10 suppressed</td><td>None</td></tr>
          </tbody>
        </table></div>
      </figure>
      <p>Organisations would have seen milestones and months, with their own steps marked; notes, exact dates and the names of other organisations were excluded. The highlighted row is the locus of the residual risk discussed in section 6.</p>
      <h3>4.6 Reporting</h3>
      <p>Reports read from a de-identified tally of milestones, not from journeys, and suppressed any group of fewer than ten people, on the principle that a sequence of milestones remains personal information even without a name.</p>
      <h3>4.7 Withdrawal and audit</h3>
      <p>Withdrawing <code>share.journey</code> removed the person&rsquo;s links immediately through a database trigger, and a journey left with no linked responses was deleted. Views of journeys were recorded in the platform&rsquo;s audit log.</p>
      <h3>4.8 Why not Bloom filters</h3>
      <p>Bloom-filter methods offer better tolerance of identifier variation, as the evaluations in section 3 show. They were not adopted for two reasons: the published cryptanalysis of Bloom-filter encodings,<sup><a data-goto="rx-refs">[5, 6]</a></sup> and the need for additional identifying attributes, such as names and dates of birth, which would have increased collection. Deterministic matching on one consented identifier accepted missed links in preference to false links or wider collection. It did not resolve the custody problem described in section 6.</p>
    </section>

    <section id="rx-testing">
      <h2><span>5</span>Testing and findings</h2>
      <p>This section reports Always&rsquo;s own implementation results. All tests ran against synthetic records in disposable databases. No real participant data was used at any stage.</p>
      <figure class="rx-fig">
        <div class="rx-tw"><table class="rx-table">
          <caption><span class="rx-fn">Table 3</span> Automated tests of the implementation.</caption>
          <thead><tr><th scope="col">Suite</th><th scope="col">Properties verified</th></tr></thead>
          <tbody>
            <tr><th scope="row">Unit tests (7)</th><td>An adult with <code>share.journey</code> is linked; anyone under 18 is never linked, even with the purpose granted; the purpose is separate from consent to be introduced; linking stops when consent is withdrawn or lapses; differently written numbers normalise to the same identifier; only milestone and month are exposed; small numbers are withheld.</td></tr>
            <tr><th scope="row">API integration tests (7)</th><td><code>share.journey</code> is refused for minors; two responses from the same adult through different ministries are linked without the link leaving the platform; a receiving church sees earlier steps by month under its own identifier only; each organisation receives a different identifier for the same person; a church that has not accepted the person sees nothing; withdrawal hides the journey; network totals withhold small numbers.</td></tr>
            <tr><th scope="row">Database security checks</th><td>The database itself refuses to link a minor or to link without consent; the application role cannot read journey tables directly; withdrawal removes links and deletes an empty journey.</td></tr>
          </tbody>
        </table></div>
      </figure>
      <h3>5.1 Findings</h3>
      <ul>
        <li><em>Functional and access-control properties.</em> The implementation behaved as specified under all of the tests above.</li>
        <li><em>Linkage accuracy.</em> Not evaluated. No precision, recall or false-match rate was measured, and no simulation of linkage accuracy was conducted. The accuracy figures in section 3 belong to different, probabilistic methods applied to health data and should not be read as properties of this design.</li>
        <li><em>Not undertaken.</em> Performance and scale testing, penetration testing, independent security or privacy review, and research into how people understand the consent wording.</li>
      </ul>
      <p>The tests therefore establish that the design could be implemented with its consent, separation and withdrawal properties enforced at the database. They do not establish that it would be accurate, secure in operation, or acceptable to participants.</p>
    </section>

    <section id="rx-threats">
      <h2><span>6</span>Threat model and limitations</h2>
      <p>This section sets out risks identified by analysis. None was observed in operation, because the system was never operated with real records.</p>
      <figure class="rx-fig rx-wide">''' + F.trust() + '''
        <ol class="rx-legend">
          <li><b>1</b><span><em>Database exfiltration.</em> The attacker obtains fingerprints and journeys but not the keys. Withstood by design.</span></li>
          <li><b>2</b><span><em>Key compromise or misuse.</em> Every fingerprint can be inverted by enumeration and every journey reconstructed. Not withstood.</span></li>
          <li><b>3</b><span><em>Privileged insider.</em> Access to both the database and key custody. Reduced by least privilege, logging and oversight; not eliminated.</span></li>
          <li><b>4</b><span><em>Inference from outputs.</em> Sequences of milestones and months may identify an individual in a small community.</span></li>
          <li><b>5</b><span><em>Compelled disclosure.</em> Courts, regulators or foreign authorities may demand the linked data.</span></li>
        </ol>
        <figcaption><span class="rx-fn">Figure 4</span> Institutional trust boundary. The design withstands theft of the database. It does not withstand compromise or misuse of the keys, which must be held by some organisation.</figcaption>
      </figure>
      <h3>6.1 Adversaries</h3>
      <ul>
        <li><em>A curious organisation</em> sees only milestones for journeys it is part of, under its own identifier.</li>
        <li><em>Colluding organisations</em> hold uncorrelated identifiers and cannot join records through the platform; they can compare only what each already held.</li>
        <li><em>An external attacker</em> who exfiltrates the database obtains fingerprints and links, but cannot invert fingerprints without the keys.</li>
        <li><em>A privileged insider</em> at the linkage service is the strongest adversary, because that is where the keys reside.</li>
      </ul>
      <h3>6.2 Risk register</h3>
      <dl class="rx-risks">
        <div><dt>Key custody</dt><dd>Australian mobile numbers occupy roughly 10<sup>8</sup> values. An unkeyed hash would offer no protection, and with the key every number can be enumerated quickly. The protection of every record therefore reduces to the custody of one secret by one organisation.</dd></div>
        <div><dt>Sensitivity grows with adoption</dt><dd>Linkage across ten ministries offers modest utility. Linkage across a thousand would create one of the most sensitive datasets on religious participation in the country. Utility and attractiveness to adversaries increase together.</dd></div>
        <div><dt>Re-identification</dt><dd>Without the key, a sequence of milestones, places and months may still identify an individual in a small community. Small-cell suppression reduces but does not eliminate this risk.</dd></div>
        <div><dt>Compelled disclosure</dt><dd>Linked data may be demanded through legal process, domestically or abroad. Data that has not been created cannot be compelled.</dd></div>
        <div><dt>Scope pressure</dt><dd>Requests for more participants, longer histories and finer reporting are individually defensible and collectively change the character of the dataset.</dd></div>
        <div><dt>Consent quality</dt><dd>A single consent tick may not convey to a new participant what linkage across ministries entails. Comprehension was not tested.</dd></div>
        <div><dt>Identifier instability</dt><dd>Carriers reissue numbers and families share handsets, which can merge distinct people; a changed number splits one person into two journeys.</dd></div>
      </dl>
      <h3>6.3 Threat environment</h3>
      <p>Any system connecting independent organisations takes on the exposure of infrastructure. The Australian Signals Directorate reports that state-sponsored cyber actors continue to pose a serious and growing threat.<sup><a data-goto="rx-refs">[7]</a></sup></p>
      <figure class="rx-fig">
        <div class="rx-stats">
          <div><b>1,200+</b><span>cyber security incidents responded to by ASD&rsquo;s ACSC in 2024&ndash;25, up 11%</span></div>
          <div><b>190+</b><span>notifications to critical infrastructure of potential malicious activity, up 111%</span></div>
          <div><b>95%</b><span>of health care and social assistance incidents in which malicious actors were successful</span></div>
        </div>
        <div class="rx-bars" role="img" aria-label="People affected by major Australian breaches: MediSecure 2024, about 12.9 million; Optus 2022, 10 million; Medibank 2022, about 9.7 million.">
          <p>People affected by major Australian breaches, millions</p>
          <div style="--w:100%"><span>MediSecure, 2024</span><i></i><b>12.9</b></div>
          <div style="--w:77.5%"><span>Optus, 2022</span><i></i><b>10.0</b></div>
          <div style="--w:75.2%"><span>Medibank, 2022</span><i></i><b>9.7</b></div>
        </div>
        <figcaption><span class="rx-fn">Figure 5</span> The Australian threat environment. Sources: ASD Annual Cyber Threat Report 2024&ndash;25; OAIC; AAP.<sup><a data-goto="rx-refs">[7, 8, 9]</a></sup></figcaption>
      </figure>
      <p>The MediSecure breach, affecting approximately 12.9 million people, is the largest notified to the OAIC under the Notifiable Data Breaches scheme.<sup><a data-goto="rx-refs">[8]</a></sup> A linked record of responses to the Gospel and subsequent church connection would be among the most sensitive collections a ministry network could hold.</p>
      <h3>6.4 Legal context</h3>
      <p>Australian law does not prohibit record linkage, but classifies religious belief as sensitive information. Under the Privacy Act 1988, collection generally requires consent, and use or disclosure is confined to the primary purpose or a directly related secondary purpose the individual would reasonably expect. A Children&rsquo;s Online Privacy Code must be registered by 10 December 2026.<sup><a data-goto="rx-refs">[14]</a></sup> This summary is general and is not legal advice.</p>
      <h3>6.5 Limitations of the design</h3>
      <ul>
        <li><em>Coverage.</em> Only steps recorded through Always Platform would have been counted.</li>
        <li><em>Exact matching.</em> A single identifier misses people who change numbers and cannot recover from errors in entry.</li>
        <li><em>Trust.</em> Open code, logging and review reduce the trust required of the linkage service; they do not remove it.</li>
        <li><em>Inference.</em> Linked milestones describe recorded events. They do not establish causation and do not measure spiritual conversion.</li>
      </ul>
    </section>

    <section id="rx-alternatives">
      <h2><span>7</span>Alternative approaches and future research</h2>
      <p>Cross-ministry longitudinal measurement remains a genuine and important research problem. Several questions can be answered without person-level linkage; others would require different technical or institutional arrangements.</p>
      <figure class="rx-fig">
        <div class="rx-tw"><table class="rx-table">
          <caption><span class="rx-fn">Table 4</span> Evidence obtainable without cross-organisation linkage.</caption>
          <thead><tr><th scope="col">Question</th><th scope="col">Method</th><th scope="col">Disclosure</th></tr></thead>
          <tbody>
            <tr><th scope="row">Did respondents at an event join a church?</th><td>Handoff outcomes recorded by the receiving church</td><td>Aggregates per event</td></tr>
            <tr><th scope="row">Are people still connected after some months?</th><td>Self-report collected by the chosen church, with consent to count</td><td>Aggregates only</td></tr>
            <tr><th scope="row">How is a ministry performing over time?</th><td>The ministry&rsquo;s own handoffs and outcomes by month</td><td>That ministry</td></tr>
            <tr><th scope="row">What is happening across a network?</th><td>Totals across partners, small groups suppressed</td><td>Aggregates only</td></tr>
          </tbody>
        </table></div>
      </figure>
      <p>Questions of progression between ministries, and of attribution, are not answerable in this way. Directions that merit research, none of which Always has evaluated, include:</p>
      <ul>
        <li><em>Independent linkage units.</em> Linkage performed by an accredited body separate from any ministry or platform, on the health model described in section 3.</li>
        <li><em>Distributed key custody.</em> Threshold schemes in which no single organisation can compute or invert fingerprints alone.</li>
        <li><em>Private set intersection and secure multiparty computation.</em> Protocols that let organisations compute overlaps or aggregate statistics without a central linked record, at the cost of revealing the computed result.</li>
        <li><em>Formal privacy for released statistics.</em> Differential privacy or similar methods to bound what published aggregates reveal about individuals.</li>
        <li><em>Time-limited studies.</em> Discrete, ethics-approved studies with study-specific consent and destruction of linked data at a fixed date.</li>
      </ul>
      <h3>7.1 Conditions for Always&rsquo;s participation in any study</h3>
      <p>Always would consider supporting a future study only if it met all of the following conditions. They describe Always&rsquo;s own position, not a standard for others.</p>
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
    </section>

    <section id="rx-decision" class="rx-decision">
      <h2><span>8</span>Always Foundation&rsquo;s institutional decision</h2>
      <dl class="rx-adr">
        <div><dt>Record</dt><dd>ADR 0013</dd></div>
        <div><dt>Title</dt><dd>No linkage of individuals across organisations</dd></div>
        <div><dt>Status</dt><dd><span class="rx-status">Accepted</span></dd></div>
        <div><dt>Date</dt><dd>21 November 2026</dd></div>
        <div><dt>Supersedes</dt><dd>ADR 0012 (withdrawn)</dd></div>
      </dl>
      <p class="rx-verdict">Always Foundation decided not to deploy the architecture described in this case study, and does not operate cross-organisation person linkage.</p>
      <h3>8.1 Basis</h3>
      <p>The decision rests on institutional judgement informed by the analysis in section 6. Deployment would have made Always the custodian of the keys for every linked record, a role whose risk grows with each participating organisation. Always is not constituted as an independent linkage unit and could not offer the separation, legislative footing and external oversight that support linkage in health. The re-identification, compulsion and scope risks could be reduced but not removed. The assessment was completed while nothing depended on the system: no participant records had been processed, no ministry workflows relied on it and no funder reporting had been built on it.</p>
      <h3>8.2 Scope</h3>
      <p>ADR 0013 prohibits, on Always Platform, persistent identity linkage between organisations, central reconstruction of a person&rsquo;s journey, shared fingerprints or matching codes, databases of religious participation histories, and cross-ministry analytics that recognise the same individual. Participant-initiated referrals to a chosen church or ministry, each organisation&rsquo;s own reporting, and aggregate statistics without cross-organisation linkage remain within scope. Exceptions for major funders or high-impact programmes are excluded.</p>
      <h3>8.3 Implementation</h3>
      <p>The implementation, its database objects and its configuration keys are removed by migration 0022 and accompanying code changes, submitted for the platform&rsquo;s required independent review. The decision record, the removal and the tests asserting that no linkage remains are public in the platform repository.<sup><a data-goto="rx-refs">[12, 15]</a></sup></p>
      <h3>8.4 What the decision does not claim</h3>
      <p>The decision concerns Always&rsquo;s own platform and role, and this design. It is not a conclusion about privacy-preserving record linkage generally, nor about whether churches, ministries or researchers should pursue longitudinal research under other technical and governance arrangements.</p>
      <p class="rx-close">For Always, the technical capacity to build a capability and the institutional standing to hold it were distinct questions. The second decided the matter.</p>
    </section>

    <section id="rx-refs" class="rx-refs">
      <h2><span>9</span>References and technical documentation</h2>
      <h3>Literature</h3>
      <ol>
        <li>Hodges S, Eitelhuber T, Merchant A, Alan J. Population Data Centre Profile: the Western Australian Data Linkage Branch. <i>International Journal of Population Data Science</i> 2020. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC7477781/">PMC7477781</a></li>
        <li>Boyd JH, et al. Data linkage infrastructure for cross-jurisdictional health-related research in Australia. <i>BMC Health Services Research</i> 2012;12:480. <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3579698/">PMC3579698</a></li>
        <li>Randall S, Wichmann H, Brown A, Boyd J, Eitelhuber T, Merchant A, Ferrante A. A blinded evaluation of privacy preserving record linkage with Bloom filters. <i>BMC Medical Research Methodology</i> 2022;22:22. <a href="https://doi.org/10.1186/s12874-022-01510-2">doi:10.1186/s12874-022-01510-2</a></li>
        <li>Irvine K, Smith M, de Vos R, Brown A, Ferrante A, Boyd J, Thackway S. Real world performance of privacy preserving record linkage. <i>International Journal of Population Data Science</i> 2018. <a href="https://doaj.org/article/a1c61969fe8b4470884c42661e243e17">DOAJ</a></li>
        <li>Christen P, Ranbaduge T, Vatsalan D, Schnell R. Precise and fast cryptanalysis for Bloom filter based privacy-preserving record linkage. <i>IEEE Transactions on Knowledge and Data Engineering</i> 2019;31(11):2164&ndash;2177. <a href="https://openresearch-repository.anu.edu.au/items/305e45a1-3d3a-4301-8f6c-126b3398968b">ANU Open Research</a></li>
        <li>Niedermeyer F, Steinmetzer S, Kroll M, Schnell R. Cryptanalysis of basic Bloom filters used for privacy preserving record linkage. <i>Journal of Privacy and Confidentiality</i> 2014;6(2). <a href="https://doaj.org/article/198c67d232af44ac94e06027d64a3928">DOAJ</a></li>
        <li>Australian Signals Directorate. Annual Cyber Threat Report 2024&ndash;25. <a href="https://www.cyber.gov.au/about-us/view-all-content/reports-and-statistics/annual-cyber-threat-report-2024-2025">cyber.gov.au</a></li>
        <li>Office of the Australian Information Commissioner. Statement on MediSecure breach. 18 July 2024. <a href="https://oaic.gov.au/newsroom/statement-on-medisecure-breach">oaic.gov.au</a></li>
        <li>Australian Associated Press. Millions of people hit by prescription cyber attack. 2024. <a href="https://aapnews.aap.com.au/news/millions-of-people-hit-by-prescription-cyber-attack">aapnews.aap.com.au</a></li>
        <li>MLJ Trust. Meet Martyn Lloyd-Jones. <a href="https://mljtrust.org/meet-mlj/">mljtrust.org</a></li>
        <li>MLJ Trust. 10 years and 20 million downloads. <a href="https://www.mljtrust.org/blog/10-year-anniversary/">mljtrust.org</a></li>
        <li>Always Platform. Architecture decision records ADR 0012 (withdrawn) and ADR 0013. <a href="https://github.com/alwaysfoundation/always-platform">github.com/alwaysfoundation/always-platform</a></li>
        <li>Krawczyk H, Bellare M, Canetti R. HMAC: Keyed-Hashing for Message Authentication. RFC 2104. IETF, 1997. <a href="https://www.rfc-editor.org/rfc/rfc2104">rfc-editor.org</a></li>
        <li>Office of the Australian Information Commissioner. Children&rsquo;s Online Privacy Code. <a href="https://www.oaic.gov.au/privacy/privacy-registers/privacy-codes/childrens-online-privacy-code">oaic.gov.au</a></li>
        <li>Always Platform. Pull request 41: removal of record linkage, migration 0022 and tests. <a href="https://github.com/alwaysfoundation/always-platform/pull/41">github.com/alwaysfoundation/always-platform/pull/41</a></li>
      </ol>
      <h3>Technical documentation</h3>
      <ul class="rx-docs">
        <li>Consent purpose <code>share.journey</code>; keys <code>LINK_KEY</code> and <code>ORG_CODE_KEY</code> (removed).</li>
        <li>Unit tests <code>packages/core/test/journey.test.ts</code>; API tests <code>apps/api/test/journeys.test.ts</code>; database checks <code>db/test/journeys_rls_test.sql</code> (in repository history).</li>
        <li>Migration <code>0022_retire_journeys.sql</code>; regression tests asserting no linkage remains in <code>apps/api/test/api.test.ts</code>.</li>
      </ul>
      <p class="rx-note">This case study is published for transparency and does not constitute legal advice. Correspondence is welcome at <a href="mailto:hello@alwaysfoundation.org">hello@alwaysfoundation.org</a>.</p>
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

.rx-state { max-width: 760px; margin: 26px 0 0; padding: 0 0 0 16px; border-left: 2px solid var(--rx-amber-lt); font-size: 14.5px; line-height: 1.6; color: rgba(255,253,248,.82); }
.rx-state b { font-weight: 600; color: var(--rx-amber-lt); }
.rx-state a { color: inherit; text-decoration: underline; text-underline-offset: 3px; cursor: pointer; }
.rx-table caption { caption-side: top; text-align: left; padding: 0 0 12px; font-size: 14.5px; color: var(--rx-soft); }
.rx-main ol li::marker { color: var(--rx-ink); font-weight: 600; }
.rx-refs h3 { margin-top: 26px; }
.rx-docs li { font-size: 14.5px; line-height: 1.6; color: var(--rx-soft); }
.rx-abstract p em { margin-right: 4px; }
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
          <h3>Privacy-preserving record linkage for Gospel impact research.</h3>
          <p>An applied research case study in cross-ministry record linkage, cryptographic architecture and institutional risk.</p>
          <a class="cs-more" href="#/pprl">Read the case study</a>
        </div>
      </li>'''

TILE_CSS = '''
.rp-tile-art { background: radial-gradient(120% 90% at 85% 10%, rgba(232,165,119,.28), transparent 60%), #14352F; display: flex; align-items: center; justify-content: center; }
.rp-tile-art svg { width: 100%; height: 100%; }
'''
