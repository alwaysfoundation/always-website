"""Final visual layer, loaded last: quiet hairline rows instead of card grids, serif step numerals."""

CSS = '''
/* ---- Quiet rows in place of card grids ---- */
.pg-feats { column-gap: 48px; row-gap: 0; }
.pg-feats .pg-feat, .pg-sage .pg-feats .pg-feat { background: none; border-radius: 0; padding: 28px 0 32px; border-top: 1px solid rgba(27,71,64,.16); box-shadow: none; }
.pg-feats .pg-feat h3 { margin: 0 0 8px; font-size: 21px; color: var(--green); }
.pg-feats .pg-feat p { max-width: 38ch; }
.pg-night .pg-feats .pg-feat, .pg-green .pg-feats .pg-feat { border-top-color: rgba(248,243,234,.16); }
.pg-night .pg-feats .pg-feat h3, .pg-green .pg-feats .pg-feat h3 { color: var(--cream); }
.pg-night .pg-feats .pg-feat p, .pg-green .pg-feats .pg-feat p { color: var(--on-green); }

/* ---- Steps: a real sequence, so numbered, in serif ---- */
.pg-steps { column-gap: 48px; }
.pg-steps .pg-step { background: none; border-radius: 0; padding: 26px 0 0; border-top: 2px solid var(--green); }
.pg-steps .pg-step span { display: block; font: 400 44px/1 'Newsreader', Georgia, serif; color: var(--clay); margin-bottom: 18px; }
.pg-steps .pg-step h3 { margin-top: 0; }

/* ---- Compliance steps, same language ---- */
.cm-steps { column-gap: 40px; row-gap: 0; }
.cm-steps li { background: none; border-radius: 0; padding: 26px 0 0; border-top: 2px solid var(--green); }
.cm-steps li::before { content: counter(s, decimal-leading-zero); display: block; width: auto; height: auto; background: none; border-radius: 0; font: 400 44px/1 'Newsreader', Georgia, serif; color: var(--clay); margin-bottom: 18px; }

/* ---- About: vision, name, posture ---- */
.mv { column-gap: 48px; row-gap: 0; }
.mv div { background: none; border-radius: 0; padding: 28px 0 0; border-top: 1px solid rgba(27,71,64,.16); }

/* ---- Solution heroes with a product screen ---- */
.page-hero .pd-split .pg-cta { margin-top: 28px; }
.sl-end { text-align: center; }
.sl-end .pg-lead { margin-left: auto; margin-right: auto; }
.sl-end .pg-cta { justify-content: center; }
'''
