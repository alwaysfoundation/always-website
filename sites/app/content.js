// Always App content. Bible references are loaded from the translation the person has chosen (KJV or WEB, both public domain).
// Refs: 'BOOK chapter verse' or 'BOOK chapter verse-verse'.
window.AC = {

  // Partner training. We link out to each partner's own pages and credit them; their content stays theirs.
  partners: [
    { id: 'tgh', name: 'The Global Harvest', short: 'Global Harvest', mono: 'GH', tone: 'sage', tag: 'Make disciples who make disciples',
      about: 'An Australian network helping everyday believers share Jesus, baptise and gather new believers, right where they live.',
      join: { label: 'Join the Harvest Network', url: 'https://theglobalharvest.com/join/' },
      tools: [
        { t: 'The 4 Fields', s: 'A simple map of disciple-making, from a first conversation to a new church.', url: 'https://theglobalharvest.com/global-harvest-4-fields/' },
        { t: '15 Second Testimony', s: 'Your before and after with Jesus, short enough for any moment.', url: 'https://theglobalharvest.com/15-second-testimony/' },
        { t: 'The 3 Circles', s: 'Draw the Gospel on a napkin in a few minutes.', url: 'https://theglobalharvest.com/circles/' },
        { t: 'The 411', s: 'A way to start Gospel conversations with people you meet.', url: 'https://theglobalharvest.com/the-411/' },
        { t: 'Discovery Bible Study', s: 'Read, discuss and obey Scripture together in a small group.', url: 'https://theglobalharvest.com/discovery-bible-study/' },
        { t: 'Healthy Church Circle', s: 'What a healthy gathering of believers looks like.', url: 'https://theglobalharvest.com/healthy-church-circle/' },
        { t: 'MAWL', s: 'Model, assist, watch, leave: how to train others.', url: 'https://theglobalharvest.com/mawl/' },
      ] },
    { id: 'needgod', name: 'NeedGod.net', short: 'NeedGod.net', mono: 'NG', tone: 'night', tag: 'Gospel conversations, on the street and online',
      about: 'Ryan and the NeedGod.net team share the Gospel every week in Brisbane and online, and offer free training so you can too.',
      join: { label: 'Apply for free training', url: 'https://training.needgod.net' },
      tools: [
        { t: 'The Gospel script', s: 'A full Gospel conversation, step by step.', url: 'https://www.needgod.net/script' },
        { t: 'Questions only', s: 'The same conversation as a short list of questions.', url: 'https://www.needgod.net/scriptquestions' },
        { t: 'Common analogies', s: 'A video of everyday pictures that help the Gospel land.', url: 'https://www.youtube.com/watch?v=mPTVgRuKj60' },
        { t: 'Watch live', s: 'Real Gospel conversations, streamed most days of the week.', url: 'https://www.youtube.com/needGodnet' },
        { t: 'Search 2,000+ videos', s: 'Find the moment a question was answered.', url: 'https://www.needgod.net/videos' },
        { t: 'Street evangelism in Brisbane', s: 'Join the team in King George Square and learn by watching.', url: 'https://www.needgod.net/outreaches' },
        { t: 'Gospels of John', s: 'Free tracts and Gospels to give away.', url: 'https://tracts.needgod.net' },
      ] },
  ],
  votd: ['JHN 3 16', 'PSA 23 1', 'ROM 8 28', 'PHP 4 6-7', 'ISA 41 10', 'JER 29 11', 'MAT 11 28', 'PRO 3 5-6', 'ROM 5 8', '2CO 5 17', 'EPH 2 8-9', 'JHN 14 6', 'PSA 46 1', 'LAM 3 22-23', 'MAT 28 19-20', '1JN 1 9', 'ROM 12 2', 'GAL 2 20', 'PSA 119 105', 'JHN 10 10', 'ISA 40 31', 'HEB 11 1', 'MAT 5 16', 'JHN 15 5', 'ROM 10 9', 'PSA 139 14', 'COL 3 23', '1PE 5 7', 'JHN 8 12', 'PSA 34 18', 'MAT 6 33', 'ROM 15 13', 'JAS 1 5', 'PSA 27 1', 'JHN 1 12', 'EPH 3 20', '2TI 1 7', 'PSA 121 1-2', 'LUK 19 10', 'MIC 6 8', 'ROM 6 23', 'JHN 16 33', 'ISA 53 5', 'PHP 1 6', '1CO 13 4', 'HEB 13 8', 'PSA 37 4', 'MAT 9 37-38', 'ACT 1 8', 'REV 21 4'],

  story: [
    { key: 'created', title: 'Created', line: 'God made us, and He loves us.', body: 'God made the world and everything in it, and He made people to know Him and enjoy Him. You are not an accident. You were made by God, for God.', refs: ['GEN 1 27', 'PSA 139 14'], ask: 'Have you ever sensed you were made for something more?' },
    { key: 'broken', title: 'Broken', line: 'We turned away from Him.', body: 'We have all gone our own way and done wrong, in what we think, say and do. Sin breaks our relationship with God and hurts the world around us. We cannot fix it on our own.', refs: ['ROM 3 23', 'ISA 59 2'], ask: 'Where do you see that brokenness in the world, or in your own life?' },
    { key: 'rescued', title: 'Rescued', line: 'Jesus came to bring us home.', body: 'God did not leave us. He sent His Son, Jesus, who lived the life we could not live, died on the cross in our place, and rose again. Through Him, forgiveness and new life are offered as a free gift.', refs: ['JHN 3 16', 'ROM 5 8', '1CO 15 3-4'], ask: 'What do you make of Jesus?' },
    { key: 'restored', title: 'Restored', line: 'We can know Him now and for ever.', body: 'Anyone who turns to Jesus and trusts Him is forgiven and welcomed into God’s family. He makes us new, and one day He will make all things new.', refs: ['ROM 10 9', 'JHN 1 12', '2CO 5 17'], ask: 'Is there anything stopping you from trusting Jesus today?' },
  ],

  romansRoad: [
    { ref: 'ROM 3 23', note: 'Everyone has sinned.' },
    { ref: 'ROM 6 23', note: 'Sin leads to death, but God offers life as a gift.' },
    { ref: 'ROM 5 8', note: 'God showed His love: Christ died for us while we were still sinners.' },
    { ref: 'ROM 10 9-10', note: 'Confess Jesus as Lord and believe God raised Him.' },
    { ref: 'ROM 10 13', note: 'Everyone who calls on the name of the Lord will be saved.' },
    { ref: 'ROM 5 1', note: 'We have peace with God through Jesus.' },
  ],

  moment: [
    { t: 'Slow down', d: 'Thank them for being honest. You don’t need perfect words. The Holy Spirit is already at work.' },
    { t: 'Check what they understand', d: 'Ask what they’re saying yes to. If it helps, walk through God’s story in four moments together.' },
    { t: 'Pray together', d: 'Invite them to talk to God in their own words. You can offer a simple prayer for them to say after you, if they would like.', prayer: 'Jesus, thank You for loving me. I’m sorry for the wrong I’ve done and for living my own way. Thank You for dying for me and rising again. I trust You now. Please forgive me, make me new, and help me follow You. Amen.' },
    { t: 'Celebrate', d: 'This is the best decision anyone can make. Tell them the angels in heaven rejoice (Luke 15:10).' },
    { t: 'Give a next step', d: 'Offer to connect them with a church nearby, with their consent. Nobody who says yes should walk alone.' },
    { t: 'Keep walking', d: 'Swap numbers if it’s appropriate, pray for them by name, and check in this week.' },
  ],

  guides: [
    {
      id: 'nofaith', title: 'Someone with no faith', sub: 'Friends who don’t believe in God, or aren’t sure.',
      intro: 'Many Australians have never really thought about God, or have quietly decided He isn’t there. Most aren’t hostile. They’re busy, unsure, or have never heard the story told well.',
      listen: ['What they believe about meaning, death and right and wrong', 'Experiences that shaped their view', 'Questions they’ve never had answered'],
      common: ['A longing for meaning, love and justice', 'Honesty about doubt and suffering', 'Interest in Jesus as a real person in history'],
      questions: ['What do you think happens when we die?', 'If God were real, what would you want to ask Him?', 'Have you ever read about Jesus for yourself?', 'What do you think makes a person truly good?'],
      share: [{ p: 'Start with Jesus, not religion. Invite them to read one of the Gospels with you.', ref: 'JHN 20 31' }, { p: 'Our longing for meaning and justice points to the God who made us.', ref: 'ECC 3 11' }, { p: 'God isn’t waiting for us to get our lives sorted. He comes to us.', ref: 'LUK 19 10' }],
      gentle: ['Don’t try to win the argument. Win the friend.', 'It’s fine to say “I don’t know, but I’ll find out.”', 'Big questions often need many conversations.'],
    },
    {
      id: 'spiritual', title: 'Spiritual but not religious', sub: 'People open to the spiritual, wary of church.',
      intro: 'Many people sense there is more to life, and may pray, meditate or read widely, but have little time for organised religion.',
      listen: ['What “spiritual” means to them', 'Practices that bring them peace', 'Why religion has put them off'],
      common: ['Hunger for the sacred and for peace', 'Desire for authenticity over performance', 'Awareness of something beyond ourselves'],
      questions: ['When have you felt most connected to something bigger than you?', 'What does peace look like for you?', 'Have you ever thought God might be personal, someone you can know?'],
      share: [{ p: 'God is not a force or an idea. He is personal, and He can be known.', ref: 'ACT 17 27-28' }, { p: 'Jesus offers rest, not religious performance.', ref: 'MAT 11 28-30' }, { p: 'Real peace comes from being made right with God.', ref: 'ROM 5 1' }],
      gentle: ['Honour their search. Many are genuinely seeking.', 'Show what following Jesus looks like day to day.', 'Invite them into community, not just a meeting.'],
    },
    {
      id: 'muslim', title: 'A Muslim friend', sub: 'Sharing with respect and warmth.',
      intro: 'Muslims honour Jesus (Isa) as a great prophet, born of the virgin Mary, and believe in one God. Many are devout, hospitable and glad to talk about faith.',
      listen: ['How they practise their faith', 'What they believe about Jesus', 'Their hopes about God’s mercy and judgement'],
      common: ['Belief in one Creator God', 'Respect for Jesus, Mary and the prophets', 'Prayer, family and moral seriousness'],
      questions: ['How do you know if God has accepted you?', 'What does the Qur’an say about Jesus?', 'Would you like to read the Injil (the Gospels) about Jesus together?'],
      share: [{ p: 'Christians also believe in one God. We know Him as Father, Son and Holy Spirit.', ref: 'DEU 6 4' }, { p: 'Jesus offers assurance of forgiveness, not uncertainty.', ref: '1JN 5 13' }, { p: 'Jesus’ death was not defeat. It was God’s plan to rescue us.', ref: 'ISA 53 5-6' }],
      gentle: ['Be hospitable and respectful, especially across genders.', 'Treat the Bible with care; it shows how much it matters to you.', 'Take time. Trust is built over many conversations.', 'Never pressure someone. Following Jesus can cost a great deal in some families.'],
    },
    {
      id: 'jw', title: 'A Jehovah’s Witness', sub: 'When someone knocks on your door, or is your friend.',
      intro: 'Jehovah’s Witnesses are often sincere and well-practised in discussing Scripture. They believe Jesus is God’s first creation, not God Himself, and that salvation involves faithful work within their organisation.',
      listen: ['Why they joined, and what they find meaningful', 'How sure they are of salvation', 'Who they believe Jesus is'],
      common: ['A high view of Scripture', 'A desire to please God', 'Belief that Jesus is the Messiah'],
      questions: ['How can you be sure God has forgiven you?', 'Who do you say Jesus is?', 'Would you read John 1 with me, slowly?'],
      share: [{ p: 'Jesus is fully God, who became flesh for us.', ref: 'JHN 1 1-3' }, { p: 'Salvation is God’s gift, not something we earn.', ref: 'EPH 2 8-9' }, { p: 'Thomas worshipped the risen Jesus as Lord and God.', ref: 'JHN 20 28' }],
      gentle: ['Be kind. They often face rejection.', 'Focus on Jesus and grace, not every disagreement.', 'Offer a cuppa and a real friendship if it’s safe and appropriate.'],
    },
    {
      id: 'buddhist', title: 'A Buddhist friend', sub: 'Sharing with someone who follows the Buddha’s teaching.',
      intro: 'Buddhism teaches that life involves suffering, caused by craving, and that it can end through the Eightfold Path. Many Buddhists value compassion, mindfulness and peace.',
      listen: ['How they practise and what it means to them', 'Their thoughts on suffering and karma', 'Whether they believe in a personal God'],
      common: ['Honest recognition of suffering', 'Compassion for others', 'Desire for inner peace and freedom'],
      questions: ['What do you hope for beyond this life?', 'How do you deal with the weight of karma or past wrongs?', 'What do you think of Jesus’ teaching on grace?'],
      share: [{ p: 'God is personal and loving, and He entered our suffering in Jesus.', ref: 'HEB 4 15' }, { p: 'Forgiveness is a gift, not something we must work off.', ref: 'ROM 6 23' }, { p: 'Jesus offers rest for the weary.', ref: 'MAT 11 28' }],
      gentle: ['Respect family and cultural traditions.', 'Grace is often the most surprising news. Let it land.', 'Show patience. Change of worldview takes time.'],
    },
    {
      id: 'hindu', title: 'A Hindu friend', sub: 'Sharing with warmth and understanding.',
      intro: 'Hinduism is diverse. Many Hindus honour many gods as expressions of one ultimate reality, and believe in karma and rebirth. Many respect Jesus as a holy teacher.',
      listen: ['Which traditions and practices matter to them', 'What they believe about karma and liberation', 'How they see Jesus'],
      common: ['Devotion and prayer', 'Respect for the spiritual life', 'A desire to be free from wrongdoing'],
      questions: ['What do you think Jesus meant when He said He is the way?', 'How do you hope to be free from karma?', 'Would you like to hear why I follow Jesus?'],
      share: [{ p: 'Jesus is not one way among many. He is God come near.', ref: 'JHN 14 6' }, { p: 'God offers forgiveness once and for all, not cycle after cycle.', ref: 'HEB 9 27-28' }, { p: 'God’s grace is a gift we receive, not earn.', ref: 'TIT 3 5' }],
      gentle: ['Honour family and hospitality.', 'Don’t mock other gods. Speak positively about Jesus.', 'Many Hindus are happy to pray with you. Pray in Jesus’ name.'],
    },
    {
      id: 'hurt', title: 'Someone hurt by church', sub: 'When church has been a source of pain.',
      intro: 'Some people have been let down, judged or even harmed by Christians or churches. Their pain is real, and it matters to God.',
      listen: ['What happened, if they want to share', 'What they still believe about God', 'What they wish Christians understood'],
      common: ['A sense of justice and how things should be', 'Jesus’ own anger at religious hypocrisy', 'A longing to be safe and loved'],
      questions: ['Would you be willing to tell me what happened?', 'Is your trouble mostly with God, or with church?', 'What would a safe community look like for you?'],
      share: [{ p: 'Jesus is gentle with the hurting and hard on hypocrisy.', ref: 'MAT 12 20' }, { p: 'God is close to the broken-hearted.', ref: 'PSA 34 18' }, { p: 'Jesus invites the weary to come to Him.', ref: 'MAT 11 28-29' }],
      gentle: ['Listen far more than you speak. Don’t defend what was wrong.', 'If someone has been abused, encourage them to seek safe, professional support, and follow your church’s safeguarding process.', 'Be patient. Trust may take a long time to rebuild.'],
    },
  ],

  courses: [
    {
      id: 'story', title: 'Sharing your story', mins: 15, sub: 'Tell how Jesus changed your life, in three minutes, in your own words.',
      lessons: [
        { t: 'Why your story matters', body: ['Your story is one of the most natural ways to talk about Jesus. People may argue with ideas, but it’s hard to argue with what Jesus has done in your life.', 'The man born blind didn’t have every answer. He simply said, “I was blind, but now I see.”'], ref: 'JHN 9 25', reflect: 'Who first told you about Jesus, and what did their story mean to you?' },
        { t: 'Before, meeting Jesus, since', body: ['A simple shape helps: what life was like before, how you came to trust Jesus, and what has changed since.', 'If you grew up in faith, talk about when it became your own, or a time Jesus carried you through.'], ref: '1PE 3 15', reflect: 'Write one sentence for each part: before, meeting Jesus, since.' },
        { t: 'Keep it short and real', body: ['Aim for three minutes. Avoid church words people won’t understand. Be honest about struggles: people connect with weakness more than polish.', 'Finish with a question, like “Has anything like that ever happened to you?”'], ref: '2CO 12 9', reflect: 'Practise your story out loud, then try it with a Christian friend.' },
      ],
    },
    {
      id: 'lead', title: 'Leading someone to Jesus', mins: 20, sub: 'What to say, how to pray, and what to do next when someone says yes.',
      lessons: [
        { t: 'The heart of the message', body: ['The Gospel is good news about Jesus: God made us, we turned away, Jesus died and rose to bring us home, and we can trust Him now.', 'You don’t need to say everything. You need to point to Jesus.'], ref: '1CO 15 3-4', reflect: 'Can you explain the Gospel in a minute, in everyday words?' },
        { t: 'When someone is ready', body: ['Ask gently: “Is there anything stopping you from trusting Jesus?” If they want to, pray together. A simple, honest prayer is enough.', 'It’s not the words that save. It’s Jesus, received by faith.'], ref: 'ROM 10 13', reflect: 'Read the prayer in Leading the moment. How would you say it in your own words?' },
        { t: 'The first next steps', body: ['A new believer needs a Bible, prayer, a church family and a friend. Offer to connect them with a church near them, with their consent.', 'Then keep walking with them. Check in this week.'], ref: 'ACT 2 42', reflect: 'Who could you introduce a new believer to at your church?' },
      ],
    },
    {
      id: 'welcome', title: 'Welcoming well', mins: 20, sub: 'For church connect leads: the first call, the first coffee, the first Sunday.',
      lessons: [
        { t: 'The first call', body: ['Call within a day if you can. Introduce yourself warmly, say how you got their details, and ask how they’re going.', 'Keep it short. The goal is a friendly next step, not a long conversation.'], ref: 'ROM 15 7', reflect: 'Write the first two sentences you’d say on that call.' },
        { t: 'The first coffee', body: ['Meet somewhere public and comfortable. Ask about their story and what led them to say yes. Share a little of yours.', 'Offer a simple way to read the Bible, like John in 21 days.'], ref: 'LUK 15 20', reflect: 'Where in your area is a good place for a first coffee?' },
        { t: 'The first Sunday', body: ['Offer to meet them outside and sit together. Introduce them to two or three people. Explain what’s happening as you go.', 'Afterwards, invite them to lunch or to a small group. Belonging grows from friendship.'], ref: 'HEB 10 24-25', reflect: 'Who in your church is great at making people feel at home?' },
      ],
    },
    {
      id: 'safe', title: 'Safe ministry with young people', mins: 25, sub: 'Child safe practice for youth leaders and events.',
      lessons: [
        { t: 'Why it matters', body: ['Jesus welcomed children and warned against causing them harm. Safe ministry protects young people and honours Him.', 'Every adult in ministry with young people needs a current Working with Children Check for their state, and should follow their church’s child safe policy.'], ref: 'MRK 10 14', reflect: 'Do you know where your church’s child safe policy is?' },
        { t: 'Good practice', body: ['Work in pairs, in visible places. Avoid one-to-one private messaging with young people; use group channels with parents informed.', 'Under 15s need a parent or guardian’s okay before their details are shared. The Always App builds that in.'], ref: 'PHP 4 8', reflect: 'What is one practice your team could strengthen?' },
        { t: 'If something worries you', body: ['If a young person tells you something concerning, listen calmly, don’t promise to keep secrets, and report it to your safe ministry contact straight away.', 'If anyone is in immediate danger, call 000.'], ref: 'PSA 82 3', reflect: 'Who is your church’s safe ministry contact?' },
      ],
    },
    {
      id: 'faiths', title: 'Conversations across faiths', mins: 20, sub: 'Listening well and sharing gently with friends of other beliefs.',
      lessons: [
        { t: 'Listen first', body: ['Ask what your friend believes and why. Listen to understand, not to reply. People can tell when they’re respected.'], ref: 'JAS 1 19', reflect: 'What is one question you could ask a friend about their faith?' },
        { t: 'Find common ground', body: ['Paul started from what the Athenians already knew and pointed them to Jesus. Look for shared longings: peace, forgiveness, hope.'], ref: 'ACT 17 22-23', reflect: 'What longing do you share with a friend of another faith?' },
        { t: 'Point to Jesus', body: ['Keep coming back to Jesus: who He is and what He did. Offer to read a Gospel together. Leave the results to God.'], ref: 'COL 4 5-6', reflect: 'Which guide in this app could help you this week?' },
      ],
    },
    {
      id: 'walk', title: 'Walking with someone', mins: 20, sub: 'The first months of following Jesus: Bible, prayer, church and friends.',
      lessons: [
        { t: 'The Bible', body: ['Help them start small and steady, perhaps a chapter of John a day. Read together and ask: what does this show us about God? About us? What will we do?'], ref: 'PSA 119 105', reflect: 'Which reading plan would suit the person you’re walking with?' },
        { t: 'Prayer', body: ['Teach that prayer is talking with our Father. Pray together, simply, and show them the Lord’s Prayer.'], ref: 'MAT 6 9-13', reflect: 'When could you pray together this week?' },
        { t: 'Church and friends', body: ['Faith grows in community. Go to church together, introduce friends, and look for a small group.', 'Expect ups and downs. Keep showing up.'], ref: 'ACT 2 46-47', reflect: 'What is one simple way you can show up for them this month?' },
      ],
    },
  ],

  plans: [
    { id: 'first7', title: 'First steps', days: 7, sub: 'Seven readings for anyone new to following Jesus.', readings: ['JHN 1', 'JHN 3', 'LUK 15', 'ROM 5', 'EPH 2', 'PSA 23', 'ACT 2'] },
    { id: 'john21', title: 'John in 21 days', days: 21, sub: 'Meet Jesus, a chapter a day.', readings: Array.from({ length: 21 }, (_, i) => 'JHN ' + (i + 1)) },
    { id: 'mark16', title: 'Mark in 16 days', days: 16, sub: 'The fast-moving story of Jesus.', readings: Array.from({ length: 16 }, (_, i) => 'MRK ' + (i + 1)) },
    { id: 'comfort', title: 'Psalms of comfort', days: 10, sub: 'For hard days, and for anyone who needs hope.', readings: ['PSA 23', 'PSA 27', 'PSA 34', 'PSA 46', 'PSA 62', 'PSA 91', 'PSA 103', 'PSA 121', 'PSA 139', 'PSA 145'] },
    { id: 'romans', title: 'Romans in 16 days', days: 16, sub: 'The good news, explained.', readings: Array.from({ length: 16 }, (_, i) => 'ROM ' + (i + 1)) },
  ],

  questions: [
    { q: 'Does God exist?', a: 'The beauty and order of the universe, our sense of right and wrong, and our longing for meaning all point beyond ourselves. Christians believe God has made Himself known most clearly in Jesus.', refs: ['PSA 19 1', 'ROM 1 20'] },
    { q: 'Can I trust the Bible?', a: 'The Bible was written over centuries by many authors, yet tells one story pointing to Jesus. We have thousands of early manuscripts, and the Gospels were written within living memory of Jesus.', refs: ['2TI 3 16', 'LUK 1 1-4'] },
    { q: 'Why is there suffering?', a: 'There are no easy answers. The Bible is honest about pain. It shows a God who does not stand far off, but entered our suffering in Jesus, and promises one day to wipe away every tear.', refs: ['REV 21 4', 'ROM 8 18'] },
    { q: 'Who is Jesus?', a: 'Jesus is a real figure of history. Christians believe He is God the Son, who became human, died for our sins and rose again, and that He is alive today.', refs: ['JHN 1 14', 'COL 1 15'] },
    { q: 'Aren’t all religions the same?', a: 'Religions differ deeply on who God is and how we are made right with Him. Jesus makes a unique claim: that He is the way to the Father, and that salvation is a gift of grace.', refs: ['JHN 14 6', 'ACT 4 12'] },
    { q: 'Can God forgive me?', a: 'Yes. No one is too far gone. Jesus came for people who know they need Him. Whoever turns to Him finds mercy.', refs: ['1JN 1 9', 'ISA 1 18'] },
  ],

  messages: [
    { t: 'A warm welcome', m: 'Hi {name}, it was so good to meet you. I’m really glad you said yes to Jesus. I’ll be praying for you this week. Let me know if you’d like to catch up for a coffee.' },
    { t: 'A reading to start', m: 'Hi {name}, here’s a great place to start reading the Bible: the Gospel of John, a chapter a day. Happy to read along with you!' },
    { t: 'Coffee this week', m: 'Hi {name}, would you be free for a coffee this week? I’d love to hear how you’re going.' },
    { t: 'Church together', m: 'Hi {name}, would you like to come to church with me this Sunday? I can meet you out the front and we can sit together.' },
    { t: 'Checking in', m: 'Hi {name}, just thinking of you and praying for you today. How are you going?' },
  ],

  walkSteps: ['Send a welcome message', 'Pray for them by name', 'Share a reading plan', 'Meet for a coffee', 'Go to church together', 'Introduce them to a small group'],

  prayerPrompts: ['Thank God for who He is.', 'Pray for each person on your list by name.', 'Ask God for an opportunity to share Jesus this week.', 'Pray for your church and its leaders.', 'Pray for those who have said yes recently, that they would grow.', 'Ask the Lord of the harvest to send out workers (Matthew 9:38).'],
};
