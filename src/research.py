"""Notice at the old Journeys initiative address: the proposal is discontinued."""

SLUG = 'pprl'
TITLE = 'Journeys initiative discontinued · Always Foundation'

PAGE = '''
<article class="rp-end">
<div class="rp-end-top"><div class="wrap rp-end-in">
  <p class="rp-end-kick">Notice, 21 November 2026</p>
  <h1>The Journeys initiative has been discontinued</h1>
</div></div>
<div class="wrap rp-end-in rp-end-body">
  <p>In November 2026 we proposed a Journeys initiative. It would have used privacy-preserving record linkage to recognise the same person across the churches and ministries that helped them, and we invited expressions of interest in a pilot.</p>
  <p>We have decided not to go ahead. The pilot will not run, and expressions of interest are closed. The feature was never switched on, so no one&rsquo;s information was linked.</p>
  <p>Always does not link people across organisations. Each church and ministry keeps its own records. When someone asks to be introduced to a church, their details go to that church with their permission, and to no one else. Reports show each ministry its own results, and any network figures are totals that do not follow individuals.</p>
  <p>If you registered interest or have questions, email <a href="mailto:hello@alwaysfoundation.org">hello@alwaysfoundation.org</a>.</p>
  <p class="rp-end-links"><a href="#/docs/privacy">How we look after information</a> <a href="#/">Home</a></p>
</div>
</article>
'''

CSS = r'''
.rp-end-top { background: var(--green); color: var(--cream); padding: 168px 0 48px; }
.rp-end-in { max-width: 680px; }
.rp-end-kick { font: 600 14px/1 var(--head); color: rgba(255,253,248,.72); margin: 0 0 18px; }
.rp-end h1 { font-size: clamp(34px, 5vw, 52px); letter-spacing: -0.035em; line-height: 1.05; margin: 0; color: var(--cream); }
.rp-end-body { padding-top: 44px; padding-bottom: 96px; }
.rp-end-body p { font-size: 18px; line-height: 1.65; margin: 0 0 18px; }
.rp-end-links { display: flex; gap: 24px; flex-wrap: wrap; margin-top: 32px !important; }
.rp-end-links a { display: inline-flex; align-items: center; min-height: 44px; font-weight: 600; }
@media (max-width: 700px) { .rp-end-top { padding: 124px 0 36px; } .rp-end-body { padding-top: 32px; padding-bottom: 64px; } }
'''

JS = ''
