// <always-scripture>: Scripture from YouVersion Platform, through Always Platform. Free, no cookies, no tracking.
// Put the verse you want shown inside the element; it stays as the fallback if Scripture can't be fetched.
//   <script type="module" src="https://alwaysfoundation.org/sdk/v0/scripture.js"></script>
//   <always-scripture ref="ROM.5.8">"But God shows his love for us..." Romans 5:8</always-scripture>
const DEFAULT_API = 'https://alwaysfoundation.org/api/scripture';
const cache = new Map();

export async function getPassage(ref, { bible, api = DEFAULT_API } = {}) {
  const key = (bible || '') + '|' + ref;
  if (!cache.has(key)) {
    const q = new URLSearchParams({ ref });
    if (bible) q.set('bible', bible);
    cache.set(key, fetch(api + '/passage?' + q).then((r) => (r.ok ? r.json() : Promise.reject(new Error('scripture_' + r.status)))));
  }
  return cache.get(key);
}

const CSS = `:host{display:block;font:inherit;color:inherit}
blockquote{margin:0;font:inherit;line-height:1.5}
cite{display:block;margin-top:.6em;font-style:normal;font-weight:700;font-size:.85em;color:var(--always-accent,#9A4F22)}
small{display:block;margin-top:.4em;font-size:.72em;opacity:.7}`;

class AlwaysScripture extends HTMLElement {
  static observedAttributes = ['ref', 'bible'];
  connectedCallback() { this.render(); }
  attributeChangedCallback() { if (this.isConnected) this.render(); }
  async render() {
    const ref = this.getAttribute('ref');
    if (!ref) return;
    try {
      const p = await getPassage(ref, { bible: this.getAttribute('bible') || undefined, api: this.getAttribute('api') || undefined });
      if (!p.text) return;
      const root = this.shadowRoot || this.attachShadow({ mode: 'open' });
      root.innerHTML = '';
      const style = document.createElement('style'); style.textContent = CSS;
      const q = document.createElement('blockquote'); q.textContent = '“' + p.text + '”';
      const c = document.createElement('cite'); c.textContent = p.reference + (p.bible?.abbreviation ? ' (' + p.bible.abbreviation + ')' : '');
      const s = document.createElement('small'); s.textContent = [p.bible?.copyright, 'via YouVersion'].filter(Boolean).join(' · ');
      root.append(style, q, c, s);
      this.dispatchEvent(new CustomEvent('always-scripture-load', { detail: p }));
    } catch (e) {
      // Keep the fallback text already inside the element.
    }
  }
}
if (!customElements.get('always-scripture')) customElements.define('always-scripture', AlwaysScripture);
