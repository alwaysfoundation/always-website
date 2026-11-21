"""Always AI: product page and research write-up for the open-weights assistant prototype."""

PRODUCT_SLUG = 'ai'
RESEARCH_SLUG = 'ai-research'
TITLES = {PRODUCT_SLUG: 'Always AI · Always Foundation', RESEARCH_SLUG: 'Always AI: an open, private assistant for churches · Always Foundation'}

PR_URL = 'https://github.com/alwaysfoundation/always-platform/pull/42'
PKG_URL = 'https://github.com/alwaysfoundation/always-platform/tree/feat/always-ai/packages/ai'

CREED = [
    'We believe in one God, the Father Almighty, Maker of heaven and earth, and of all things visible and invisible.',
    'And in one Lord Jesus Christ, the only-begotten Son of God, begotten of the Father before all worlds (&aelig;ons), Light of Light, very God of very God, begotten, not made, being of one substance with the Father; by whom all things were made; who for us men, and for our salvation, came down from heaven, and was incarnate by the Holy Ghost of the Virgin Mary, and was made man; He was crucified for us under Pontius Pilate, and suffered, and was buried, and the third day He rose again, according to the Scriptures, and ascended into heaven, and sitteth on the right hand of the Father; from thence He shall come again, with glory, to judge the quick and the dead; whose kingdom shall have no end.',
    'And in the Holy Ghost, the Lord and Giver of life, who proceedeth from the Father, who with the Father and the Son together is worshipped and glorified, who spake by the prophets. In one holy catholic and apostolic Church; we acknowledge one baptism for the remission of sins; we look for the resurrection of the dead, and the life of the world to come. Amen.',
]

CHECKS = [
    ('Creed fidelity', 'Affirms the faith of the Nicene Creed accurately.'),
    ('Differences between churches', 'Explains views on baptism, gifts, ministry roles and the end times fairly, without choosing.'),
    ('Church library', 'Follows a church&rsquo;s own statement of faith when one is provided.'),
    ('Scripture', 'Quotes accurately and gives correct references.'),
    ('Fabrication', 'Refuses to invent verses, sermons, quotations or sources.'),
    ('Care and safety', 'Responds gently, gives Lifeline and emergency numbers, points to child safety processes.'),
    ('Children&rsquo;s information', 'Declines to work with details identifying anyone under 18.'),
    ('Actions', 'Prepares drafts and never claims to have sent, deleted or changed anything.'),
    ('Authority', 'Points to Scripture, the pastor and the church; does not pronounce as an authority.'),
    ('Civic boundaries', 'Does not tell churches how to vote.'),
    ('Everyday tasks', 'Produces usable newsletters, rosters, study questions and drafts.'),
]

# ---------------------------------------------------------------- product page

PRODUCT = f'''<section class="page-hero pd-hero ai-hero"><div class="wrap ai-hero-in">
  <p class="pl-kick">Always AI <span class="ai-tag">Research prototype</span></p>
  <h1>A private assistant for your church, free to use.</h1>
  <p class="pd-line">Help with the everyday work of ministry, and a private place for pastors to think, running on your church&rsquo;s own computer.</p>
  <p>Always AI pairs an open model that anyone may download with instructions written by Always, carrying the Nicene Creed and our rules for care, privacy and children. We are testing whether it is good enough to offer. It may not be.</p>
  <p class="pd-status">In research. Not yet available.</p>
  <div class="pg-cta"><a class="btn btn-peach" href="#/ai-research">Read the research</a><a class="btn btn-ghost" href="#/contact">Register interest</a></div>
</div></section>

<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">Why a church might want its own AI</h2>
  <div class="pg-feats">
    <div class="pg-feat rv"><h3>Private by design</h3><p>The local version runs on your own computer. Nothing you type leaves your building, including a pastor&rsquo;s own study and questions.</p></div>
    <div class="pg-feat rv"><h3>Free</h3><p>Built on an open-weights model released under the Apache 2.0 licence. No subscriptions.</p></div>
    <div class="pg-feat rv"><h3>Made for church work</h3><p>Instructions written for ministry, with the Nicene Creed (AD 381) as common ground. On questions where churches differ, it follows your church&rsquo;s own statement of faith.</p></div>
    <div class="pg-feat rv"><h3>Safe with children&rsquo;s information</h3><p>It declines to work with details identifying anyone under 18. That rule can&rsquo;t be switched off.</p></div>
    <div class="pg-feat rv"><h3>You stay in charge</h3><p>It drafts. A person checks and sends.</p></div>
    <div class="pg-feat rv"><h3>Tested in the open</h3><p>A published prompt checker tests every model and every change. Results will be published with the model, version and date.</p></div>
  </div>
</div></section>

<section class="sec pg-sec pg-sage"><div class="wrap ai-two">
  <div><h2 class="pg-h rv">What it is for</h2><ul class="ai-list rv">
    <li>Newsletters, announcements and emails</li><li>Rosters and meeting notes</li><li>Bible study and discussion questions</li>
    <li>First drafts of policies, for your review</li><li>A private space for pastors to study and think</li></ul></div>
  <div><h2 class="pg-h rv">What it is not for</h2><ul class="ai-list rv">
    <li>Pastoral counsel or decisions that belong to people</li><li>The last word on doctrine</li><li>Legal advice</li>
    <li>Anything about children</li></ul>
    <p class="rv">Like any AI, it can be confidently wrong. Check what matters.</p></div>
</div></section>

<section class="sec pg-sec"><div class="wrap">
  <h2 class="pg-h rv">How it would roll out</h2>
  <ol class="ai-stages rv">
    <li><b>Local kit.</b> A setup guide and ready-made settings for a church computer, such as a Mac with 32 GB of memory or more, with trained volunteers to help.</li>
    <li><b>Hosted in Australia.</b> For churches without suitable hardware. Processed in Australia and not kept.</li>
    <li><b>Church operations.</b> Help with calendars, rosters and follow-up through Always Platform, drafting only, with a person approving every action.</li>
  </ol>
  <p class="pg-lead rv">Each stage begins only if the one before passes its checks and a pilot.</p>
</div></section>

<section class="sec pg-sec pg-sage"><div class="wrap">
  <h2 class="pg-h rv">Questions</h2>
  <div class="ai-faq rv">
    <details><summary>Why not just use ChatGPT or Claude?</summary><p>They are excellent, and churches are welcome to use them. Always AI is for work you would rather keep private, at no cost. The best paid tools are more capable; open models are a step behind.</p></details>
    <details><summary>Which model does it use?</summary><p>The prototype wraps Inkling 2 Mini from Thinking Machines Lab, released with open weights under Apache 2.0. We will recommend whichever open model performs best on our checks, and change it if a better one appears.</p></details>
    <details><summary>Is it open source?</summary><p>Yes. The instructions, the Creed text, the setup and the prompt checker are published on GitHub. Your information stays yours.</p></details>
    <details><summary>Is it trained on the Bible or the Creed?</summary><p>Not in the sense of retraining the model. The Creed is built into its instructions, and your church can add its own statement of faith and documents for it to consult. Retraining would come later, if at all, and only with theological review.</p></details>
  </div>
</div></section>'''

# ---------------------------------------------------------------- research write-up

TOC = [('ai-abstract', '1. Abstract'), ('ai-problem', '2. Problem and significance'), ('ai-approach', '3. Approach'),
       ('ai-model', '4. Base model'), ('ai-theology', '5. Theological framework'), ('ai-data', '6. Data rules'),
       ('ai-eval', '7. Evaluation'), ('ai-risks', '8. Risks and limitations'), ('ai-status', '9. Status and next steps'),
       ('ai-creed', 'Appendix: the Nicene Creed'), ('ai-refs', 'References')]


def _toc():
    return ''.join(f'<button type="button" data-goto="{i}">{t}</button>' for i, t in TOC)


def _checks():
    return ''.join(f'<tr><th scope="row">{a}</th><td>{b}</td></tr>' for a, b in CHECKS)


RESEARCH = f'''
<article class="rx">
<div class="rx-mast"><div class="wrap rx-mast-in">
  <p class="rx-series"><a href="#/ai">Always AI</a> <span aria-hidden="true">/</span> Research note</p>
  <h1>An Open, Private Assistant for Churches</h1>
  <p class="rx-dek">A research note on open-weights language models for church work: approach, theological framework, data rules and a published evaluation method.</p>
  <dl class="rx-front">
    <div><dt>Published</dt><dd>Always Foundation, November 2026</dd></div>
    <div><dt>Scope</dt><dd>Problem, approach, base model, theology, data rules, evaluation, risks</dd></div>
    <div><dt>Technical record</dt><dd>RFC 0007; prototype in pull request 42</dd></div>
  </dl>
  <p class="rx-state"><b>Research status: Prototype, not evaluated.</b> The instructions and prompt checker are published, but no model has yet been run through the checker. Always AI is not available, and it may not prove good enough to offer.</p>
</div></div>

<div class="rx-sheet"><div class="wrap rx-body">
  <nav class="rx-toc" aria-label="Contents"><p>Contents</p>{_toc()}</nav>
  <div class="rx-main">

    <section id="ai-abstract" class="rx-abstract">
      <h2><span>1</span>Abstract</h2>
      <p><em>Background.</em> Churches increasingly use AI assistants for writing and administration, and pastors use them to study and think. The most capable assistants are hosted overseas and charged per person, and many pastors are reluctant to type sensitive questions into them.</p>
      <p><em>Objective.</em> To determine whether an open-weights model, run on a church&rsquo;s own computer with instructions written for church work, can be useful, faithful and safe enough to offer free through Always.</p>
      <p><em>Method.</em> We wrapped an open-weights model, Inkling 2 Mini, with instructions that embed the Nicene Creed (AD 381) and Always&rsquo;s data rules, and wrote a prompt checker of 31 cases across eleven categories that runs against any compatible model and records every transcript.</p>
      <p><em>Status.</em> The instructions, Creed text and checker are implemented and tested as software. No model has yet been evaluated. This note sets out the design and the criteria by which it will be judged.</p>
    </section>

    <section id="ai-problem">
      <h2><span>2</span>Problem and significance</h2>
      <p>Pastors and church staff spend much of their week on writing and administration: newsletters, rosters, emails, policies and study preparation. AI assistants can help, but the most capable are hosted by overseas companies, priced per person, and governed by terms the church does not control.</p>
      <p>Pastoral work adds a particular sensitivity. A pastor may want to think through a hard passage, a question of faith, or a difficult situation in the congregation. Many are unwilling to do that in a hosted service, whatever its privacy terms. The frontier models cannot be downloaded and run privately.</p>
      <p>Open-weights models can be. The question is whether a model small enough to run on a church computer can be useful for church work, faithful to historic Christian belief, and safe in the ways that matter most: care for people at risk, protection of children&rsquo;s information, and honesty about what it does not know.</p>
    </section>

    <section id="ai-approach">
      <h2><span>3</span>Approach</h2>
      <p>Three ways of shaping a model for church use were considered, in increasing order of cost and risk.</p>
      <div class="rx-tw"><table class="rx-table">
        <caption><span class="rx-fn">Table 1</span> Ways to shape the model.</caption>
        <thead><tr><th scope="col">Method</th><th scope="col">What it does</th><th scope="col">Decision</th></tr></thead>
        <tbody>
          <tr><th scope="row">Instructions</th><td>A standing system prompt the model sees on every request. The Creed, at about 250 words, is short enough to include in full, so it is always present.</td><td>Adopted</td></tr>
          <tr><th scope="row">Church library (retrieval)</th><td>A church&rsquo;s own statement of faith, confession, sermons and policies, searched locally and supplied to the model when relevant. The model consults the material; it is not retrained on it.</td><td>Next stage, local only</td></tr>
          <tr><th scope="row">Fine-tuning</th><td>Adjusting the model&rsquo;s weights on a curated body of text.</td><td>Deferred; only if evaluation shows the first two are insufficient, and only with theological review</td></tr>
        </tbody>
      </table></div>
      <p>Frontier hosted models remain more capable and more polished. Always AI is positioned as a private, free option for everyday church work, not as a replacement, and churches remain free to use frontier tools under their own accounts.</p>
    </section>

    <section id="ai-model">
      <h2><span>4</span>Base model</h2>
      <p>The prototype wraps Inkling 2 Mini from Thinking Machines Lab, released on 21 November 2026 with open weights under the Apache 2.0 licence and a Model Acceptable Use Policy.<sup><a data-goto="ai-refs">[1, 2]</a></sup> It is distributed as a single checkpoint of about 20 GB, and at launch Ollama supports it on Macs with at least 32 GB of memory.<sup><a data-goto="ai-refs">[1, 2]</a></sup></p>
      <p>The vendor reports strong results on its own benchmarks, and also reports, in its own agentic testing, rates of misbehaviour of 9.8%, covert misbehaviour of 8.3% and destructive actions of 10.2%.<sup><a data-goto="ai-refs">[1]</a></sup> We treat vendor figures as context, not evidence for church use. The choice of model is not a dependency: each new open model is run through the same checker before Always recommends it.</p>
    </section>

    <section id="ai-theology">
      <h2><span>5</span>Theological framework</h2>
      <ul>
        <li><em>Common ground.</em> The Nicene Creed (AD 381), the boundary of partnership in the Always network, is embedded in full. The model affirms it and does not present denials of it as equally Christian. The full text is given in the appendix.</li>
        <li><em>Matters on which churches differ.</em> On baptism, the Lord&rsquo;s Supper, spiritual gifts, church government, ministry roles and the end times, the model follows the church&rsquo;s own statement of faith where one is provided, and otherwise explains the main views fairly without choosing.</li>
        <li><em>Authority.</em> The model is a study and work aid. It points people to Scripture, their pastor and their church, distinguishes Scripture, historic teaching and its own suggestions, and says when it is unsure.</li>
        <li><em>Sources.</em> It must not invent verses, books, sermons, quotations or citations.</li>
        <li><em>Governance.</em> The instructions are published. Changes to the theological sections require the Theology and Mission committee; changes to care, children and data rules require the Safeguarding, Privacy and Ethics committee.</li>
      </ul>
    </section>

    <section id="ai-data">
      <h2><span>6</span>Data rules</h2>
      <div class="rx-tw"><table class="rx-table">
        <caption><span class="rx-fn">Table 2</span> What the assistant may work with.</caption>
        <thead><tr><th scope="col">Information</th><th scope="col">Local</th><th scope="col">Hosted in Australia</th></tr></thead>
        <tbody>
          <tr><th scope="row">Adults&rsquo; details (names, contacts, rosters, attendance)</th><td>Allowed</td><td>Allowed; processed and not kept</td></tr>
          <tr><th scope="row">Pastoral notes (prayer requests, counselling, health, family)</th><td>Only if the senior leader turns it on</td><td>Not allowed</td></tr>
          <tr><th scope="row">Anything identifying a person under 18</th><td>Never</td><td>Never</td></tr>
          <tr><th scope="row">Church library</th><td>Allowed</td><td>Not offered</td></tr>
        </tbody>
      </table></div>
      <p>The model prepares drafts only. For any future connection to church systems, approval of every send, deletion, payment or change will be enforced in software, not left to the model&rsquo;s instructions. Hosted processing of adults&rsquo; details requires a privacy notice and legal review before launch.</p>
    </section>

    <section id="ai-eval">
      <h2><span>7</span>Evaluation</h2>
      <p>The prompt checker runs a fixed set of cases against any model served through an OpenAI-compatible interface, locally through Ollama or LM Studio or on a hosted server, and writes a report containing every transcript.<sup><a data-goto="ai-refs">[3]</a></sup></p>
      <div class="rx-tw"><table class="rx-table">
        <caption><span class="rx-fn">Table 3</span> Categories in the prompt checker (31 cases).</caption>
        <thead><tr><th scope="col">Category</th><th scope="col">What it looks for</th></tr></thead>
        <tbody>{_checks()}</tbody>
      </table></div>
      <ul>
        <li><em>Automatic and human review.</em> Pattern checks catch clear failures. A person reads every transcript before conclusions are drawn.</li>
        <li><em>Thresholds set in advance.</em> Pass thresholds for each stage are to be fixed by the committees before the first run. Every case on children, care and fabrication must pass.</li>
        <li><em>Continuous.</em> The checker is run on every change to the instructions and every new model release, and summaries are published with the model, version and date.</li>
        <li><em>Synthetic only.</em> Cases use invented names and details. No real personal information is ever used.</li>
      </ul>
      <p>The checker has been verified end to end against a stand-in server. It has not yet been run against Inkling 2 Mini or any other model, so no results are reported here.</p>
    </section>

    <section id="ai-risks">
      <h2><span>8</span>Risks and limitations</h2>
      <dl class="rx-risks">
        <div><dt>Quality</dt><dd>A model of this size may not be good enough for church work. The checker and pilots are how this will be determined.</dd></div>
        <div><dt>Theological overreach</dt><dd>People may treat answers as authoritative. Instructions, product copy and pastoral oversight reduce this risk; they do not remove it.</dd></div>
        <div><dt>Hardware</dt><dd>Most church computers cannot run the model. The hosted stage would carry the cost for churches without suitable hardware.</dd></div>
        <div><dt>Agentic error</dt><dd>The vendor&rsquo;s own testing reports non-trivial rates of misbehaviour and destructive actions, so any operational use stays draft-only.</dd></div>
        <div><dt>Prompt limits</dt><dd>Instructions shape behaviour but do not guarantee it. A model may ignore them, which is why the checker exists.</dd></div>
        <div><dt>Capacity</dt><dd>Supporting churches depends on volunteers and modest funding. The prototype is also a test of whether Always can sustain it.</dd></div>
      </dl>
    </section>

    <section id="ai-status">
      <h2><span>9</span>Status and next steps</h2>
      <ol>
        <li>Committees review the instructions and data rules, and set pass thresholds.</li>
        <li>Run the checker on Inkling 2 Mini and at least one other open model; publish the summaries.</li>
        <li>If thresholds are met, pilot the local kit with a small number of churches.</li>
        <li>Decide, on the evidence, whether to offer Always AI, and whether to proceed to the hosted stage.</li>
      </ol>
      <p class="rx-close">Always AI will be offered only if it proves useful, faithful and safe on published evidence. If it does not, we will say so.</p>
    </section>

    <section id="ai-creed" class="ai-creed">
      <h2>Appendix: the Nicene Creed (AD 381)</h2>
      {''.join(f'<p>{p}</p>' for p in CREED)}
      <p class="rx-note">Received text of the First Council of Constantinople. Translation from Philip Schaff, <i>The Creeds of Christendom</i>, vol. 2 (1890), in the public domain, with pronouns referring to God capitalised.<sup><a data-goto="ai-refs">[4]</a></sup></p>
    </section>

    <section id="ai-refs" class="rx-refs">
      <h2>References</h2>
      <ol>
        <li>Thinking Machines Lab. Inkling 2 Mini. 21 November 2026. <a href="https://thinkingmachines.ai/news/inkling-2-mini/">thinkingmachines.ai</a></li>
        <li>Thinking Machines Lab. Inkling-2-Mini model card. Hugging Face. <a href="https://huggingface.co/thinkingmachines/Inkling-2-Mini">huggingface.co</a></li>
        <li>Always Platform. RFC 0007 and the Always AI prototype (packages/ai), pull request 42. <a href="{PR_URL}">github.com</a></li>
        <li>Schaff P. <i>The Creeds of Christendom, with a History and Critical Notes</i>, vol. 2. New York: Harper &amp; Brothers, 1890.</li>
      </ol>
      <p class="rx-note">Questions or a different view are welcome at <a href="mailto:hello@alwaysfoundation.org">hello@alwaysfoundation.org</a>.</p>
    </section>
  </div>
</div></div>
</article>'''

CSS = r'''
.ai-hero-in { max-width: 820px; }
.ai-tag { display: inline-block; margin-left: 10px; padding: 3px 10px; border: 1px solid currentColor; border-radius: 999px; font-size: 12.5px; font-weight: 600; opacity: .85; }
.ai-two { display: grid; grid-template-columns: 1fr 1fr; gap: 48px; }
.ai-list { margin: 0 0 16px; padding-left: 20px; }
.ai-list li { margin-bottom: 8px; font-size: 17px; line-height: 1.6; }
.ai-stages { max-width: 760px; padding-left: 22px; }
.ai-stages li { margin-bottom: 14px; font-size: 17px; line-height: 1.65; }
.ai-faq { max-width: 820px; }
.ai-faq details { border-bottom: 1px solid rgba(27,71,64,.16); padding: 16px 0; }
.ai-faq summary { min-height: 32px; font-weight: 600; cursor: pointer; }
.ai-faq p { margin: 10px 0 0; line-height: 1.65; }
.ai-creed p { font-family: var(--serif); font-size: 19px !important; line-height: 1.7 !important; }
.ai-creed .rx-note { font-family: var(--text); font-size: 14px !important; }
@media (max-width: 760px) { .ai-two { grid-template-columns: 1fr; gap: 8px; } }
'''

JS = r'''
(() => {
  if (!('IntersectionObserver' in window)) return;
  const setup = () => {
    document.querySelectorAll('.rx-toc').forEach((toc) => {
      if (toc.dataset.ready || !toc.offsetParent) return; toc.dataset.ready = '1';
      const btns = [...toc.querySelectorAll('button')];
      const io = new IntersectionObserver((es) => es.forEach((en) => { if (en.isIntersecting) btns.forEach((x) => x.classList.toggle('on', x.dataset.goto === en.target.id)); }), { rootMargin: '-110px 0px -70% 0px' });
      btns.forEach((x) => { const s = document.getElementById(x.dataset.goto); if (s) io.observe(s); });
    });
  };
  window.addEventListener('hashchange', () => setTimeout(setup, 80));
  setTimeout(setup, 400);
})();
'''

TILE = '''
      <li class="cs-tile cs-tile-ai">
        <div class="cs-img ai-tile-art" aria-hidden="true"><svg viewBox="0 0 400 260"><rect x="70" y="50" width="260" height="160" rx="14" fill="none" stroke="rgba(255,253,248,.35)" stroke-width="2"/><rect x="92" y="78" width="150" height="14" rx="7" fill="rgba(255,253,248,.55)"/><rect x="92" y="104" width="200" height="14" rx="7" fill="rgba(255,253,248,.3)"/><rect x="158" y="140" width="150" height="14" rx="7" fill="#E8A577"/><rect x="198" y="166" width="110" height="14" rx="7" fill="rgba(232,165,119,.6)"/></svg></div>
        <div class="cs-text">
          <p class="cs-name">Research note</p>
          <h3>An open, private assistant for churches.</h3>
          <p>Open-weights AI with the Nicene Creed built in, a published prompt checker, and honest criteria for whether it is good enough to offer.</p>
          <a class="cs-more" href="#/ai-research">Read the research</a>
        </div>
      </li>'''

TILE_CSS = '''
.ai-tile-art { background: radial-gradient(110% 90% at 15% 10%, rgba(232,165,119,.2), transparent 60%), #1B4740; display: flex; align-items: center; justify-content: center; }
.ai-tile-art svg { width: 100%; height: 100%; }
'''
