"""Story pages for Sydney Fire Evangelism and the Alpha integration. Reuse the article styles from faithtech.py."""

ARROW = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11M9 4l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'

SYDNEYFIRE = '''
<article class="ft">
<div class="ft-hero"><div class="wrap ft-hero-in">
  <p class="ft-kick"><a href="#/stories">Stories</a> <span aria-hidden="true">/</span> Sydney Fire Evangelism</p>
  <h1>Sydney Fire takes the Gospel to the streets</h1>
  <p class="ft-dek">A team of street evangelists with their own branded response app, so every yes on a Sydney street has a next step.</p>
</div></div>

<figure class="ft-fig wrap">
  <img src="{{SF_PHOTO}}" alt="A crowd in a Sydney city square, hands raised in worship, around a banner that reads Jesus is the Way" width="1600" height="1067" loading="lazy">
  <figcaption>Photo: Sydney Fire Evangelism, used with permission.</figcaption>
</figure>

<div class="wrap ft-body">
  <div class="prose ft-prose">
    <p class="ft-lead">On a busy Sydney street, a conversation about Jesus can change a life in minutes. Sydney Fire makes sure that moment doesn't end when the crowd moves on.</p>

    <h2>Who Sydney Fire is</h2>
    <p>Sydney Fire Evangelism is a team of street evangelists. They share Jesus in public places across Sydney, with worship, preaching and prayer, and they meet people who have never set foot in a church.</p>

    <h2>Their own app, live today</h2>
    <p>Sydney Fire runs Always Platform live in a ministry setting. Their team has its own response app, with their name and logo, at <a href="https://sydneyfire.alwaysfoundation.org">sydneyfire.alwaysfoundation.org</a>. Anyone curious can read the Good News through the Romans Road, verse by verse, and respond right there.</p>

    <ol class="st-steps">
      <li><b>Scan</b><span>Someone who says yes scans a QR code on the street.</span></li>
      <li><b>Choose</b><span>They pick a next step: find a church, explore faith, or talk with someone.</span></li>
      <li><b>Connect</b><span>With their permission, their details are kept securely in Australia, so the team can follow up and help them find a church.</span></li>
    </ol>

    <blockquote class="ft-pull">“How beautiful are the feet of those who preach the good news!”<cite>Romans 10:15</cite></blockquote>

    <h2>Explore faith with Alpha</h2>
    <p>Not everyone is ready for church on day one. When someone chooses "Explore faith" in Sydney Fire's app, the Alpha integration routes them to Alpha, where they can find a course near them straight away.</p>
    <a class="st-card" href="#/alpha">
      <img src="{{ALPHA_LOGO}}" alt="" width="56" height="56">
      <span><b>The Alpha integration</b><span>How people who want to explore faith are routed to a course near them.</span></span>
      <i>''' + ARROW + '''</i>
    </a>

    <h2>What it means for the team</h2>
    <p>The team can give their full attention to the person in front of them. Every response is saved safely, every person has a clear next step, and no one slips through the cracks after the outreach ends.</p>
  </div>

  <aside class="ft-side" aria-label="At a glance">
    <div class="ft-card">
      <h2>At a glance</h2>
      <dl>
        <dt>Ministry</dt><dd>Street evangelism across Sydney</dd>
        <dt>Uses</dt><dd>Always Respond, Always App and Always Connect</dd>
        <dt>Integration</dt><dd><a href="#/alpha">Alpha</a>, for people exploring faith</dd>
        <dt>Their app</dt><dd><a href="https://sydneyfire.alwaysfoundation.org">sydneyfire.alwaysfoundation.org</a></dd>
      </dl>
      <a class="btn btn-peach" href="#/evangelists">Tools for evangelists</a>
      <a class="ft-link" href="#/join/evangelist">Join as an evangelist</a>
    </div>
  </aside>
</div>
</article>
'''

ALPHA = '''
<article class="ft">
<div class="ft-hero"><div class="wrap ft-hero-in">
  <p class="ft-kick"><a href="#/stories">Stories</a> <span aria-hidden="true">/</span> Integration</p>
  <h1>Routing people to Alpha to explore faith</h1>
  <p class="ft-dek">When someone wants to explore faith before they are ready for church, Always Platform helps them find an Alpha course near them.</p>
</div></div>

<figure class="ft-fig wrap">
  <img src="{{ALPHA_PHOTO}}" alt="A woman standing still on a busy Sydney street beside the words For everyone, everywhere" width="1600" height="1067" loading="lazy" style="object-position:30% 50%">
  <figcaption>Photo and logo: Alpha Australia, used with permission.</figcaption>
</figure>

<div class="wrap ft-body">
  <div class="prose ft-prose">
    <p class="ft-lead">A yes to Jesus is often the start of many questions. Alpha gives people a safe, honest place to ask them.</p>

    <h2>Who Alpha is</h2>
    <p>Alpha is a series of sessions, in person or online, that gives people space to explore life, faith and meaning. Churches across Australia run it, and everyone is welcome. Find out more at <a href="https://alpha.org.au/">alpha.org.au</a>.</p>

    <h2>How the integration works</h2>
    <ol class="st-steps">
      <li><b>Choose</b><span>After hearing the Gospel, someone chooses "Explore faith" in an outreach form.</span></li>
      <li><b>Agree</b><span>They're asked whether they'd like their first name, mobile and suburb passed to Alpha.</span></li>
      <li><b>Join</b><span>If they agree, the Alpha team helps them join a course near them.</span></li>
    </ol>

    <blockquote class="ft-pull">Every next step is the person's choice, and their details go only where they agree.</blockquote>

    <h2>Already in use</h2>
    <p>Sydney Fire Evangelism's response app routes people who choose "Explore faith" to Alpha. Any ministry using Always Respond can offer the same next step.</p>
    <a class="st-card" href="#/sydneyfire">
      <img src="{{SF_PHOTO}}" alt="" width="56" height="56">
      <span><b>Sydney Fire Evangelism</b><span>Street evangelists with their own branded response app.</span></span>
      <i>''' + ARROW + '''</i>
    </a>
  </div>

  <aside class="ft-side" aria-label="At a glance">
    <div class="ft-card">
      <img class="st-logo" src="{{ALPHA_LOGO}}" alt="Alpha logo" width="56" height="56">
      <h2>At a glance</h2>
      <dl>
        <dt>Integration</dt><dd>Alpha Australia</dd>
        <dt>Next step</dt><dd>Explore faith</dd>
        <dt>Shared with consent</dt><dd>First name, mobile and suburb</dd>
        <dt>In use</dt><dd><a href="#/sydneyfire">Sydney Fire Evangelism</a></dd>
      </dl>
      <a class="btn btn-peach" href="#/respond">See Always Respond</a>
      <a class="ft-link" href="https://alpha.org.au/">Visit alpha.org.au</a>
    </div>
  </aside>
</div>
</article>
'''

CSS = '''
.st-steps { list-style: none; counter-reset: st; margin: 28px 0 8px; padding: 0; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; }
.st-steps li { counter-increment: st; position: relative; padding: 22px 20px 20px; border-radius: 20px; background: var(--sage); }
.st-steps li::before { content: counter(st, decimal-leading-zero); display: block; margin-bottom: 14px; font: 400 26px/1 'Newsreader', Georgia, serif; color: var(--clay); }
.st-steps b { display: block; font: 800 19px/1.2 var(--head); color: var(--green); }
.st-steps span { display: block; margin-top: 6px; font-size: 15.5px; line-height: 1.5; color: var(--soft); }
.ft-pull cite { display: block; margin-top: 12px; font: normal 700 14px/1.2 var(--head); color: var(--clay); }
.st-card { display: grid; grid-template-columns: 56px minmax(0, 1fr) 44px; gap: 18px; align-items: center; margin: 24px 0 8px; padding: 18px 20px; border-radius: 20px; background: #FFFDF8; border: 1px solid var(--line); text-decoration: none !important; background-image: none !important; color: inherit; transition: transform .25s cubic-bezier(.2,.7,.2,1), box-shadow .25s ease, border-color .25s ease; }
.st-card:hover, .st-card:focus-visible { transform: translateY(-2px); border-color: rgba(27,71,64,.25); box-shadow: 0 18px 40px -24px rgba(10,30,26,.35); }
.st-card > img { width: 56px; height: 56px; border-radius: 14px; object-fit: cover; }
.st-card b { display: block; font: 800 18px/1.2 var(--head); color: var(--green); }
.st-card span span { display: block; margin-top: 4px; font-size: 15px; line-height: 1.45; color: var(--soft); }
.st-card i { width: 44px; height: 44px; border-radius: 50%; display: grid; place-items: center; background: var(--green); color: var(--cream); transition: transform .25s ease; }
.st-card i svg { width: 16px; height: 16px; }
.st-card:hover i { transform: translateX(3px); }
.ft-card .st-logo { display: block; width: 56px; height: 56px; border-radius: 14px; margin-bottom: 14px; }
.ft-card dd a { color: var(--green); font-weight: 600; }
@media (max-width: 760px) { .st-steps { grid-template-columns: minmax(0, 1fr); } }
@media (prefers-reduced-motion: reduce) { .st-card, .st-card i { transition: none; } .st-card:hover { transform: none; } }
'''

YOUVERSION = '''
<article class="ft">
<div class="ft-hero"><div class="wrap ft-hero-in">
  <p class="ft-kick"><a href="#/stories">Stories</a> <span aria-hidden="true">/</span> Integration</p>
  <h1>Scripture at every yes: Always Platform and YouVersion</h1>
  <p class="ft-dek">Always Platform brings Scripture from YouVersion Platform to the moment people respond, so they can read God’s Word in their own language, right where they said yes.</p>
</div></div>

<figure class="ft-fig wrap">
  <img src="{{YV_IMG}}" alt="YouVersion Platform: build for eternal impact with the YouVersion Platform" width="1642" height="884" loading="lazy">
  <figcaption>Image: YouVersion, used with permission.</figcaption>
</figure>

<div class="wrap ft-body">
  <div class="prose ft-prose">
    <p class="ft-lead">The moment someone says yes to Jesus is the moment they most need His Word. YouVersion has spent years making the Bible available to everyone. Always Platform makes sure it’s there at every response.</p>

    <h2>Why YouVersion</h2>
    <p>YouVersion, the team behind the Bible App, has opened its Bible technology to ministries through YouVersion Platform, free for ministry use. It brings licensed translations in hundreds of languages, which matters in a country where so many people pray in more than one language.</p>

    <h2>What we built</h2>
    <ol class="st-steps">
      <li><b>A Scripture service</b><span>Always Platform fetches passages from YouVersion and caches them. Only Bible text is ever requested.</span></li>
      <li><b>The Good News, live</b><span>The Romans Road in Always Respond, starting with Sydney Fire’s app, now draws each verse from YouVersion.</span></li>
      <li><b>A Bible reader</b><span>“Start reading John” opens the Gospel inside the app, chapter by chapter, instead of sending people away.</span></li>
    </ol>
    <p>For developers, one line adds Scripture to any church or ministry app:</p>
    <pre><code>&lt;script type="module" src="https://alwaysfoundation.org/sdk/v0/scripture.js"&gt;&lt;/script&gt;
&lt;always-scripture ref="ROM.5.8"&gt;&lt;/always-scripture&gt;</code></pre>

    <blockquote class="ft-pull">“So faith comes from hearing, and hearing through the word of Christ.”<cite>Romans 10:17</cite></blockquote>

    <h2>What stays separate</h2>
    <p>YouVersion provides Scripture. Always Platform holds what a person agreed to share and which church welcomes them. No response, consent or church details are sent to YouVersion, and personal information stays in Australia.</p>

    <h2>What’s next</h2>
    <ul>
      <li><b>Sign in with YouVersion</b> in the Always App, for adults, so people can use the account they already have.</li>
      <li><b>Reading the Bible as a next step</b>, alongside finding a church, exploring faith with Alpha, or talking with someone.</li>
    </ul>
    <p>We’re completing our YouVersion Platform registration now. Until it’s switched on, every page shows the Scripture already written into it, so no one sees a gap.</p>
  </div>

  <aside class="ft-side" aria-label="At a glance">
    <div class="ft-card">
      <h2>At a glance</h2>
      <dl>
        <dt>Integration</dt><dd>YouVersion Platform</dd>
        <dt>Used in</dt><dd>Always Respond and the Always App</dd>
        <dt>For developers</dt><dd>The <code>&lt;always-scripture&gt;</code> component</dd>
        <dt>Personal data sent</dt><dd>None</dd>
      </dl>
      <a class="btn btn-peach" href="#/docs/youversion">Read the docs</a>
      <a class="ft-link" href="#/sydneyfire">See it in Sydney Fire’s app</a>
    </div>
  </aside>
</div>
</article>
'''

YV_TILE = '''      <li class="cs-tile">
        <div class="cs-img"><img src="{{YV_IMG}}" alt="YouVersion Platform" loading="lazy" style="object-position:60% 50%"></div>
        <div class="cs-text">
          <p class="cs-name">YouVersion</p>
          <h3>Scripture at every yes.</h3>
          <p>Scripture from YouVersion Platform, right where people say yes to Jesus.</p>
          <a class="cs-more" href="#/youversion">Read the story</a>
        </div>
      </li>
'''
