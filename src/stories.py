"""Story pages for evangelists in Sydney and the Alpha, Discovery Bible Study and Christianity Explained integrations. Reuse the article styles from faithtech.py."""

ARROW = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h11M9 4l4 4-4 4" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'

STREETS = '''
<article class="ft">
<div class="ft-hero"><div class="wrap ft-hero-in">
  <p class="ft-kick"><a href="#/stories">Stories</a> <span aria-hidden="true">/</span> Evangelists in Sydney</p>
  <h1>Taking the Gospel to Sydney&rsquo;s streets</h1>
  <p class="ft-dek">Evangelists in Sydney use Always Platform, so every yes on a street corner has a next step.</p>
</div></div>

<figure class="ft-fig wrap">
  <img src="{{SF_PHOTO}}" alt="A crowd in a Sydney city square, hands raised in worship, around a banner that reads Jesus is the Way" width="1600" height="1067" loading="lazy">
  <figcaption>Photo used with permission.</figcaption>
</figure>

<div class="wrap ft-body">
  <div class="prose ft-prose">
    <p class="ft-lead">On a busy Sydney street, a conversation about Jesus can change a life in minutes. Always Platform makes sure that moment doesn&rsquo;t end when the crowd moves on.</p>

    <h2>Who they are</h2>
    <p>Evangelists across Sydney share Jesus in public places, with worship, preaching and prayer. Many of the people they meet have never set foot in a church.</p>

    <h2>How they use it</h2>
    <p>Teams hand out a QR code or show it on a sign. Anyone curious can read the Good News through the Romans Road, verse by verse, and respond right there.</p>

    <ol class="st-steps">
      <li><b>Scan</b><span>Someone who says yes scans a QR code on the street.</span></li>
      <li><b>Choose</b><span>They pick a next step: find a church, explore faith, or talk with someone.</span></li>
      <li><b>Connect</b><span>With their permission, their details are kept safely, so a local church can welcome them.</span></li>
    </ol>

    <blockquote class="ft-pull">&ldquo;How beautiful are the feet of those who preach the good news!&rdquo;<cite>Romans 10:15</cite></blockquote>

    <h2>Explore faith with Alpha</h2>
    <p>Not everyone is ready for church on day one. When someone chooses &ldquo;Explore faith&rdquo;, the Alpha integration routes them to Alpha, where they can find a course near them straight away.</p>
    <a class="st-card" href="#/alpha">
      <img src="{{ALPHA_LOGO}}" alt="" width="56" height="56">
      <span><b>The Alpha integration</b><span>How people who want to explore faith are routed to a course near them.</span></span>
      <i>''' + ARROW + '''</i>
    </a>

    <h2>Training on the go</h2>
    <p>Evangelists carry Always Sent in their pocket: the Gospel in four words, their own testimony, and studies to read with someone afterwards, like Discovery Bible Study.</p>
    <a class="st-card" href="#/dbs">
      <img src="img/story-dbs.webp" alt="" width="56" height="56">
      <span><b>Discovery Bible Study in Always Sent</b><span>Read the Bible with a friend, one story at a time.</span></span>
      <i>''' + ARROW + '''</i>
    </a>

    <h2>What it means for the team</h2>
    <p>The team can give their full attention to the person in front of them. Every response is saved safely, every person has a clear next step, and no one slips through the cracks after the outreach ends.</p>
  </div>

  <aside class="ft-side" aria-label="At a glance">
    <div class="ft-card">
      <h2>At a glance</h2>
      <dl>
        <dt>Who</dt><dd>Street evangelists in Sydney</dd>
        <dt>Uses</dt><dd>Always Respond, Always Sent and Always Connect</dd>
        <dt>Integration</dt><dd><a href="#/alpha">Alpha</a>, for people exploring faith</dd>
      </dl>
      <a class="btn btn-peach" href="#/ministries">Tools for ministries</a>
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
    <p>Evangelists in Sydney route people who choose "Explore faith" to Alpha. Any ministry using Always Respond can offer the same next step.</p>
    <a class="st-card" href="#/streets">
      <img src="{{SF_PHOTO}}" alt="" width="56" height="56">
      <span><b>Evangelists in Sydney</b><span>Taking the Gospel to Sydney&rsquo;s streets.</span></span>
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
        <dt>In use</dt><dd><a href="#/streets">Evangelists in Sydney</a></dd>
      </dl>
      <a class="btn btn-peach" href="#/respond">See Always Respond</a>
      <a class="ft-link" href="https://alpha.org.au/">Visit alpha.org.au</a>
    </div>
  </aside>
</div>
</article>
'''

DBS = '''
<article class="ft">
<div class="ft-hero"><div class="wrap ft-hero-in">
  <p class="ft-kick"><a href="#/stories">Stories</a> <span aria-hidden="true">/</span> Integration</p>
  <h1>Reading the Bible together with Discovery Bible Study</h1>
  <p class="ft-dek">A simple way for anyone to read the Bible with a friend, built into Always Sent.</p>
</div></div>

<figure class="ft-fig wrap">
  <img src="{{DBS_IMG}}" alt="An illustration from above of five people around a table, each with a sheet of paper, reading and talking together" width="1600" height="1950" loading="lazy" style="max-height:620px;object-fit:cover;object-position:50% 45%">
  <figcaption>Illustration: Discovery Bible Study.</figcaption>
</figure>

<div class="wrap ft-body">
  <div class="prose ft-prose">
    <p class="ft-lead">After someone says yes to Jesus, the best next step is often the simplest: open the Bible with a friend and see what it says.</p>

    <h2>Who they are</h2>
    <p>Discovery Bible Study is a simple, shared way of reading the Bible. A small group reads a passage, retells it in their own words, asks what it shows about God and about people, and decides how to put it into practice and who to share it with. No one needs to be an expert, so it works anywhere and passes easily from friend to friend. Guides in several languages are free at <a href="https://dbsguide.org">dbsguide.org</a>.</p>

    <h2>Why it fits Always Platform</h2>
    <p>Always Platform helps people move from a yes to a church family. Reading the Bible together keeps them growing in between, and it equips ordinary Christians to disciple the friends they bring to faith, instead of handing them off.</p>

    <h2>How the integration works</h2>
    <ol class="st-steps st-steps-4">
      <li><b>Open</b><span>In Always Sent, tap Learn, then &ldquo;How do I read the Bible with a friend?&rdquo;</span></li>
      <li><b>Choose</b><span>Pick one of ten stories about meeting Jesus, from Nicodemus to the road to Emmaus.</span></li>
      <li><b>Read</b><span>The passage and questions are on one screen: look back, look up, look forward.</span></li>
      <li><b>Live it</b><span>Finish with &ldquo;This week I will&hellip;&rdquo;, mark the story done, and invite someone to read the next one with you.</span></li>
    </ol>

    <figure class="st-shot"><img src="img/story-dbs.webp" alt="Two Always Sent screens: Read together, with the three questions and ten stories about meeting Jesus, and the first story, A visit at night, with its questions and passage" width="1600" height="900" loading="lazy"><figcaption>Read together in Always Sent.</figcaption></figure>

    <blockquote class="ft-pull">&ldquo;Your word is a lamp to my feet, and a light for my path.&rdquo;<cite>Psalm 119:105</cite></blockquote>

    <h2>The three questions, in the app</h2>
    <ul>
      <li><b>Look back:</b> what are you thankful for, what&rsquo;s been hard, and did you do what you said last time?</li>
      <li><b>Look up:</b> read the passage aloud, retell it, and ask what it says about God and about people.</li>
      <li><b>Look forward:</b> if this is true, what will change this week, and who will you share it with?</li>
    </ul>

    <h2>Private by design</h2>
    <p>Nothing about your study is sent to Always or anyone else. Which stories you&rsquo;ve finished is saved only on your phone. The method and guides belong to Discovery Bible Study, and Always Sent links to their site for more.</p>

    <a class="st-card" href="#/cexp">
      <img src="img/story-cexp.webp" alt="" width="56" height="56">
      <span><b>Christianity Explained in Always Sent</b><span>A six-session course through Mark&rsquo;s Gospel, for a friend who wants to know more.</span></span>
      <i>''' + ARROW + '''</i>
    </a>
  </div>

  <aside class="ft-side" aria-label="At a glance">
    <div class="ft-card">
      <h2>At a glance</h2>
      <dl>
        <dt>Integration</dt><dd>Discovery Bible Study</dd>
        <dt>Where</dt><dd>Always Sent, Learn, Read together</dd>
        <dt>Stories</dt><dd>Ten, about meeting Jesus</dd>
        <dt>Your data</dt><dd>Stays on your phone</dd>
      </dl>
      <a class="btn btn-peach" href="https://app.alwaysfoundation.org/#/learn/dbs">Try it in Always Sent</a>
      <a class="ft-link" href="https://dbsguide.org">Visit dbsguide.org</a>
    </div>
  </aside>
</div>
</article>
'''

CEXP = '''
<article class="ft">
<div class="ft-hero"><div class="wrap ft-hero-in">
  <p class="ft-kick"><a href="#/stories">Stories</a> <span aria-hidden="true">/</span> Integration</p>
  <h1>Christianity Explained: a course for a friend&rsquo;s next step</h1>
  <p class="ft-dek">A six-session Australian course through Mark&rsquo;s Gospel, one tap away in Always Sent, and ready to invite a friend to.</p>
</div></div>

<figure class="ft-fig wrap">
  <img src="{{CEXP_IMG}}" alt="Hands holding the Christianity Explained Leader's Guide: Discovering the Christian message through Mark's gospel" width="1430" height="1100" loading="lazy" style="max-height:620px;object-fit:cover;object-position:50% 62%">
  <figcaption>Photo: Christianity Explained.</figcaption>
</figure>

<div class="wrap ft-body">
  <div class="prose ft-prose">
    <p class="ft-lead">Many people are curious about Jesus long before they&rsquo;re ready for a Sunday service. A short course, with a friend beside them, is often the bridge.</p>

    <h2>Who they are</h2>
    <p>Christianity Explained is a six-session course through Mark&rsquo;s Gospel, made in Australia for people with little or no Bible background. It comes from HumeRidge Church of Christ in Toowoomba. The session videos are free on YouTube, and a follow-up course, Your Walk with Jesus, helps new believers keep going. Find it at <a href="https://christianityexplained.com">christianityexplained.com</a>.</p>

    <h2>How the integration works</h2>
    <ol class="st-steps st-steps-4">
      <li><b>Find it</b><span>In Always Sent, tap Learn, then &ldquo;How do I help a curious friend?&rdquo;, or find it in the training library.</span></li>
      <li><b>Watch</b><span>All six sessions are listed, from &ldquo;Jesus: Son of God&rdquo; to &ldquo;Believing&rdquo;. Each opens the free video, and you can tick them off as you go.</span></li>
      <li><b>Invite</b><span>Tap &ldquo;Invite a friend to watch with you&rdquo;. Always Sent drafts a warm message to send from your own phone, and adds your friend to your prayer list.</span></li>
      <li><b>Keep going</b><span>Afterwards, Your Walk with Jesus helps new believers grow, and a church near them is one tap away.</span></li>
    </ol>

    <figure class="st-shot"><img src="img/story-cexp.webp" alt="Two Always Sent screens: Christianity Explained with its six sessions, and Invite a friend with a drafted message about the course" width="1600" height="900" loading="lazy"><figcaption>Christianity Explained and Invite a friend in Always Sent.</figcaption></figure>

    <blockquote class="ft-pull">&ldquo;The beginning of the Good News of Jesus Christ, the Son of God.&rdquo;<cite>Mark 1:1</cite></blockquote>

    <h2>For churches running the course</h2>
    <p>Leaders find the Study Guide and the How to Run video guide in the same screen. A church that runs the course can welcome people through Always Connect and invite them straight in. With their yes, journeys show whether people who did a course went on to join a church.</p>

    <h2>Private by design</h2>
    <p>Nothing about your friend is sent to Always. The invitation goes from your phone, and your prayer list stays on it. The course belongs to its authors, and Always Sent links to their site.</p>

    <p>Christianity Explored, a similar course through Mark&rsquo;s Gospel, sits alongside it in the training library for teams who use it.</p>

    <a class="st-card" href="#/dbs">
      <img src="img/story-dbs.webp" alt="" width="56" height="56">
      <span><b>Discovery Bible Study in Always Sent</b><span>Read the Bible with a friend, one story at a time.</span></span>
      <i>''' + ARROW + '''</i>
    </a>
  </div>

  <aside class="ft-side" aria-label="At a glance">
    <div class="ft-card">
      <h2>At a glance</h2>
      <dl>
        <dt>Integration</dt><dd>Christianity Explained</dd>
        <dt>Course</dt><dd>Six sessions through Mark&rsquo;s Gospel</dd>
        <dt>Where</dt><dd>Always Sent: training library and Invite a friend</dd>
        <dt>Your data</dt><dd>Stays on your phone</dd>
      </dl>
      <a class="btn btn-peach" href="https://app.alwaysfoundation.org/#/invite">Invite a friend</a>
      <a class="ft-link" href="https://christianityexplained.com">Visit christianityexplained.com</a>
    </div>
  </aside>
</div>
</article>
'''

CSS = '''
.st-steps { list-style: none; counter-reset: st; margin: 28px 0 8px; padding: 0; display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 14px; }
.ft-prose .st-steps { padding: 0; margin-left: 0; }
.st-shot { margin: 32px 0 8px; }
.st-shot img { display: block; width: 100%; height: auto; border-radius: 20px; }
.st-shot figcaption { margin-top: 10px; font-size: 14px; color: var(--soft); }
.st-steps.st-steps-4 { grid-template-columns: repeat(2, minmax(0, 1fr)); }
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
@media (max-width: 760px) { .st-steps, .st-steps.st-steps-4 { grid-template-columns: minmax(0, 1fr); } }
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
      <li><b>The Good News, live</b><span>The Romans Road in Always Respond, used by evangelists in Sydney, now draws each verse from YouVersion.</span></li>
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
      <li><b>Sign in with YouVersion</b> in Always Sent, for adults, so people can use the account they already have.</li>
      <li><b>Reading the Bible as a next step</b>, alongside finding a church, exploring faith with Alpha, or talking with someone.</li>
    </ul>
    <p>We’re completing our YouVersion Platform registration now. Until it’s switched on, every page shows the Scripture already written into it, so no one sees a gap.</p>
  </div>

  <aside class="ft-side" aria-label="At a glance">
    <div class="ft-card">
      <h2>At a glance</h2>
      <dl>
        <dt>Integration</dt><dd>YouVersion Platform</dd>
        <dt>Used in</dt><dd>Always Respond and Always Sent</dd>
        <dt>For developers</dt><dd>The <code>&lt;always-scripture&gt;</code> component</dd>
        <dt>Personal data sent</dt><dd>None</dd>
      </dl>
      <a class="btn btn-peach" href="#/docs/youversion">Read the docs</a>
      <a class="ft-link" href="#/streets">See it on Sydney&rsquo;s streets</a>
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
