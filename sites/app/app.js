/* Always App. A free web app to share Jesus and walk with people.
   Everything personal (prayer list, notes, people, highlights) stays on this device.
   Only a response someone chooses to send, with their consent, leaves the device, to the Always database in Sydney. */
(() => {
'use strict';
const AC = window.AC;
const $ = (s, r = document) => r.querySelector(s);
const $$ = (s, r = document) => [...r.querySelectorAll(s)];
const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const uid = () => Math.random().toString(36).slice(2, 10) + Date.now().toString(36).slice(-4);
const today = () => new Date().toISOString().slice(0, 10);
const fmtDate = (d) => new Date(d).toLocaleDateString('en-AU', { day: 'numeric', month: 'short' });
const SAVE_URL = 'https://scoitzteqsvomsghtxfe.supabase.co/functions/v1/field-contact?forceFunctionRegion=ap-southeast-2';
const SOURCE = 'always-app';
const WORDING = 'always-app-2026-11-v1';

// ---------------------------------------------------------------- State (on this device only)
const KEY = 'always.app.v1';
const blank = () => ({ onboarded: false, settings: { tr: 'web', size: 20, theme: 'auto', name: '' }, pos: { b: 43, c: 1 }, hl: {}, notes: {}, marks: [], plans: {}, courses: {}, people: [], prayer: [], fieldNotes: [], points: [], connected: [], testimony: { before: '', meet: '', since: '' } });
let S;
try { S = Object.assign(blank(), JSON.parse(localStorage.getItem(KEY) || '{}')); } catch { S = blank(); }
S.settings = Object.assign(blank().settings, S.settings);
const save = () => { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch {} };

// ---------------------------------------------------------------- Icons
const P = {
  home: '<path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z"/>',
  book: '<path d="M5 4h11a3 3 0 0 1 3 3v13H8a3 3 0 0 1-3-3z"/><path d="M5 17a3 3 0 0 1 3-3h11"/>',
  qr: '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><path d="M14 14h3v3h-3zM20 14v.01M14 20h.01M17 20h4v-3"/>',
  cap: '<path d="M2 9l10-5 10 5-10 5z"/><path d="M6 11v5c3 2 9 2 12 0v-5"/>',
  walk: '<circle cx="9" cy="7" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20a6 6 0 0 1 12 0M14 20a4 4 0 0 1 7-2.6"/>',
  heart: '<path d="M12 20s-7-4.4-9-9a5 5 0 0 1 9-3 5 5 0 0 1 9 3c-2 4.6-9 9-9 9z"/>',
  pin: '<path d="M12 21s-7-6.2-7-11a7 7 0 0 1 14 0c0 4.8-7 11-7 11z"/><circle cx="12" cy="10" r="2.5"/>',
  chat: '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>',
  play: '<path d="M7 4v16l13-8z"/>', pause: '<path d="M7 4v16M17 4v16"/>',
  moon: '<path d="M20 14A8 8 0 0 1 10 4a8 8 0 1 0 10 10z"/>', music: '<path d="M9 18V5l11-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="17" cy="16" r="3"/>',
  user: '<circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/>', search: '<circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/>',
  left: '<path d="M15 5l-7 7 7 7"/>', right: '<path d="M9 5l7 7-7 7"/>', down: '<path d="M6 9l6 6 6-6"/>',
  share: '<path d="M12 3v13M7 8l5-5 5 5M5 14v6h14v-6"/>', check: '<path d="M5 12l5 5 9-10"/>', plus: '<path d="M12 5v14M5 12h14"/>',
  x: '<path d="M6 6l12 12M18 6L6 18"/>', ext: '<path d="M7 17L17 7M9 7h8v8"/>', type: '<path d="M4 7V5h16v2M9 19h6M12 5v14"/>', sun: '<circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4 12H2M22 12h-2M5 5l1.5 1.5M17.5 17.5 19 19M5 19l1.5-1.5M17.5 6.5 19 5"/>',
  lock: '<rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3"/>', bookmark: '<path d="M6 3h12v18l-6-4-6 4z"/>',
  pen: '<path d="M4 20h4L19 9l-4-4L4 16z"/><path d="M14 6l4 4"/>', copy: '<rect x="8" y="8" width="12" height="12" rx="2"/><path d="M16 8V5a1 1 0 0 0-1-1H5a1 1 0 0 0-1 1v10a1 1 0 0 0 1 1h3"/>',
  image: '<rect x="3" y="4" width="18" height="16" rx="2"/><circle cx="9" cy="10" r="2"/><path d="M21 16l-5-5-9 9"/>', headphones: '<path d="M4 15v-3a8 8 0 0 1 16 0v3"/><rect x="3" y="14" width="5" height="7" rx="2"/><rect x="16" y="14" width="5" height="7" rx="2"/>',
  cal: '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>', flame: '<path d="M12 22a7 7 0 0 0 7-7c0-4-3-6-4-10-2 2-3 4-3 6-1-1-2-2-2-4-2 2-5 5-5 8a7 7 0 0 0 7 7z"/>',
  church: '<path d="M12 2v4M10 4h4M5 21V11l7-5 7 5v10"/><path d="M10 21v-5h4v5"/>', note: '<path d="M6 3h9l4 4v14H6z"/><path d="M14 3v5h5M9 13h7M9 17h5"/>',
  trash: '<path d="M4 7h16M9 7V4h6v3M6 7l1 14h10l1-14"/>', download: '<path d="M12 3v13M7 11l5 5 5-5M5 21h14"/>', send: '<path d="M21 3 10 14M21 3l-7 18-4-7-7-4z"/>',
  sparkle: '<path d="M12 3l1.8 5.2L19 10l-5.2 1.8L12 17l-1.8-5.2L5 10l5.2-1.8z"/>', globe: '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
};
const ic = (n, s = 22, sw = 2) => `<svg width="${s}" height="${s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">${P[n] || ''}</svg>`;
const LOGO = "<svg viewBox=\"186 250 1328 366\" width=\"100\" height=\"28\" role=\"img\" aria-label=\"Always\"><path fill=\"currentColor\" fill-rule=\"evenodd\" d=\"M1030.8,608.4C1046.2,605.2 1061.0,596.1 1069.8,584.4C1077.9,573.6 1081.9,564.7 1101.5,514.5C1111.9,488.1 1128.3,446.2 1138.0,421.5C1147.8,396.8 1157.6,371.4 1160.0,365.2C1166.0,349.0 1167.7,350.0 1134.5,350.0C1109.8,350.0 1108.2,350.1 1106.6,351.9C1105.6,353.0 1101.7,362.3 1097.9,372.7C1094.1,383.0 1084.8,408.5 1077.3,429.2C1069.7,450.0 1063.2,467.0 1062.9,467.0C1062.5,467.0 1059.3,459.7 1055.7,450.8C1050.1,437.0 1029.3,386.6 1018.0,359.7C1016.3,355.5 1014.0,351.5 1013.0,351.0C1010.4,349.6 958.5,349.7 955.9,351.0C954.9,351.6 954.0,352.9 954.0,353.8C954.0,354.8 957.1,362.3 960.8,370.5C964.6,378.8 970.4,391.6 973.7,399.0C977.1,406.4 984.1,421.9 989.3,433.5C994.5,445.1 1006.2,470.9 1015.3,491.0C1024.3,511.1 1032.8,529.9 1034.0,532.8L1036.3,538.1L1033.5,544.6C1030.1,552.5 1024.9,557.3 1017.8,559.0C1011.6,560.5 1006.1,559.8 997.5,556.4C992.7,554.5 990.3,554.0 989.2,554.7C987.3,555.8 972.0,589.2 971.3,593.7C970.8,596.5 971.2,597.1 974.1,598.9C979.3,602.1 993.4,606.9 1001.9,608.4C1012.2,610.3 1021.6,610.3 1030.8,608.4ZM290.8,550.7C302.4,547.4 313.4,541.1 323.4,531.9L329.0,526.8L329.0,535.7C329.0,549.8 327.2,549.0 357.1,549.0C380.7,549.0 382.1,548.9 384.0,547.0C386.0,545.0 386.0,543.7 386.0,483.1C386.0,444.5 385.6,418.2 384.9,413.3C383.4,401.9 378.4,387.9 373.0,379.6C358.9,358.1 334.9,346.8 299.9,345.3C277.1,344.3 257.2,348.0 239.4,356.4C226.2,362.7 215.0,370.6 215.0,373.6C215.0,375.3 233.4,404.2 235.2,405.3C236.3,406.0 239.8,404.8 248.1,400.7C261.5,394.2 269.0,392.1 282.1,391.3C303.0,390.0 319.1,396.4 325.2,408.4C327.2,412.2 329.2,428.0 327.7,428.0C327.4,428.0 322.5,426.5 316.8,424.6C295.5,417.5 273.2,416.4 252.2,421.5C224.5,428.2 206.5,443.5 198.5,467.1C196.0,474.4 195.6,477.0 195.6,487.5C195.5,497.4 195.9,500.8 197.9,507.0C204.9,529.9 224.5,546.4 251.1,552.0C257.5,553.3 284.5,552.4 290.8,550.7ZM861.0,550.9C872.2,548.3 882.3,543.1 892.6,534.8C897.2,531.0 901.1,528.0 901.2,528.0C901.4,528.0 901.5,532.1 901.5,537.1C901.5,544.9 901.8,546.4 903.4,547.6C905.0,548.7 910.3,549.0 930.1,549.0C954.6,549.0 954.9,549.0 956.4,546.8C957.8,544.8 958.0,537.0 958.0,482.3C958.0,443.7 957.6,417.2 956.9,412.3C953.3,385.7 940.3,366.7 917.8,355.4C898.3,345.6 866.7,342.3 840.2,347.5C824.4,350.5 804.6,358.9 792.8,367.6C786.6,372.0 786.6,374.0 792.8,383.3C795.5,387.3 799.8,394.0 802.4,398.2C805.1,402.5 807.8,406.0 808.6,406.0C809.4,406.0 813.9,404.0 818.7,401.6C837.7,392.0 856.9,388.8 874.3,392.5C891.6,396.1 901.0,406.8 901.0,422.7C901.0,425.6 900.9,428.0 900.7,428.0C900.5,428.0 896.4,426.6 891.5,425.0C877.3,420.2 867.3,418.6 851.0,418.6C829.0,418.7 812.5,423.2 797.0,433.5C785.0,441.5 775.9,453.5 771.3,467.4C769.1,474.3 768.7,477.3 768.7,488.0C768.6,499.1 768.9,501.4 771.4,508.5C772.9,512.9 775.7,519.0 777.5,522.0C781.3,528.2 790.3,537.2 796.6,541.2C802.7,545.1 814.3,549.8 821.8,551.4C832.1,553.6 850.8,553.4 861.0,550.9ZM1262.7,550.6C1300.7,542.3 1323.0,511.4 1316.6,476.0C1314.6,464.6 1309.4,454.4 1302.1,447.1C1291.7,436.8 1278.0,430.6 1246.5,422.0C1221.5,415.1 1216.0,411.8 1216.0,403.5C1216.0,396.2 1221.1,392.0 1232.5,389.9C1243.3,387.9 1260.8,392.6 1275.7,401.7C1279.6,404.0 1283.8,406.0 1284.9,406.0C1286.2,406.0 1287.9,404.6 1289.4,402.2C1299.6,386.1 1307.0,373.7 1307.0,372.5C1307.0,369.2 1289.4,357.6 1276.7,352.6C1250.2,342.1 1217.5,342.8 1194.5,354.3C1173.0,365.0 1160.8,382.2 1159.4,403.8C1158.2,420.7 1162.9,434.0 1173.9,445.0C1184.4,455.4 1195.2,460.2 1237.6,473.0C1256.3,478.7 1263.4,486.5 1258.6,495.8C1254.9,503.0 1247.9,506.0 1235.0,506.0C1219.7,506.0 1204.7,500.8 1187.4,489.5C1182.2,486.1 1177.9,484.0 1176.6,484.2C1175.2,484.4 1171.1,489.3 1163.8,499.5C1149.3,519.8 1149.9,518.3 1154.1,522.6C1158.9,527.6 1172.1,536.3 1182.1,540.9C1192.1,545.6 1208.7,550.6 1218.5,551.9C1228.5,553.3 1254.1,552.5 1262.7,550.6ZM460.6,547.6C462.5,546.2 462.5,543.5 462.8,411.9C463.0,292.7 462.9,277.4 461.5,275.3L460.0,273.0L434.1,273.0C411.9,273.0 408.1,273.2 407.0,274.6C405.9,275.8 405.7,292.4 405.8,357.3C406.0,558.6 405.9,545.7 407.6,547.4C409.8,549.7 457.5,549.8 460.6,547.6ZM585.3,547.8C586.2,547.1 590.1,538.0 593.9,527.5C618.9,459.0 626.2,439.4 627.0,438.6C627.6,438.0 628.0,437.9 628.0,438.2C628.0,438.5 633.7,454.5 640.6,473.7C647.5,492.8 656.1,516.8 659.7,527.0C663.5,537.7 667.1,546.2 668.2,547.2C670.0,548.8 672.8,549.0 693.5,549.0C715.1,549.0 716.8,548.9 718.4,547.1C719.4,546.0 726.9,525.4 735.0,501.3C743.2,477.2 757.7,434.3 767.4,405.9C783.6,358.1 784.8,354.1 783.4,352.1C781.9,350.1 781.3,350.0 756.1,350.0C732.9,350.0 730.0,350.2 728.1,351.8C726.7,353.0 722.8,363.7 715.1,388.0C709.1,407.0 701.4,431.2 698.0,441.9C694.6,452.5 691.5,460.8 691.1,460.4C690.6,459.9 687.5,451.4 684.0,441.5C675.5,417.0 657.5,366.0 654.4,357.8C653.0,354.2 651.2,350.9 650.4,350.6C649.5,350.3 639.4,350.0 627.9,350.0C609.1,350.0 606.8,350.2 605.2,351.8C604.2,352.8 600.8,361.0 597.6,370.1C594.4,379.1 587.2,399.3 581.5,415.0C575.9,430.7 569.8,447.7 568.0,452.8C566.2,457.9 564.5,461.9 564.3,461.7C564.1,461.4 562.1,455.2 559.9,447.9C557.6,440.5 554.1,429.1 552.1,422.5C550.0,415.9 544.4,397.7 539.5,382.0C534.7,366.3 530.0,352.7 529.2,351.8C527.8,350.2 525.2,350.0 500.9,350.0C477.9,350.0 473.9,350.2 472.6,351.6C471.7,352.4 471.0,353.5 471.0,353.8C471.0,354.2 475.5,368.0 481.0,384.5C489.8,410.8 510.4,474.5 527.4,528.0C530.5,537.7 533.8,546.4 534.7,547.3C536.2,548.8 539.1,549.0 560.0,549.0C577.3,549.0 584.1,548.7 585.3,547.8ZM276.4,509.0C266.5,507.0 258.1,501.8 254.2,495.1C252.0,491.4 251.5,489.3 251.5,484.0C251.5,476.0 254.8,469.6 261.7,464.6C269.8,458.7 274.8,457.5 290.5,457.5C305.4,457.5 311.7,458.9 323.2,464.7L328.0,467.0L328.0,474.4C328.0,480.5 327.5,482.6 324.9,487.8C317.1,503.5 295.8,512.8 276.4,509.0ZM848.3,509.0C825.1,504.1 816.4,482.6 831.5,467.5C838.7,460.2 845.3,457.9 860.1,457.2C873.5,456.7 882.8,458.5 894.4,464.1L901.2,467.4L900.8,474.9C899.9,489.9 890.4,501.5 874.6,507.0C867.8,509.3 854.5,510.3 848.3,509.0Z\"/><path fill=\"#E8A577\" d=\"M1434.5,553.6C1436.3,552.3 1436.4,549.1 1436.4,463.1L1436.5,374.0L1468.9,374.0C1497.7,374.0 1501.5,373.8 1503.2,372.3C1504.8,370.9 1505.0,368.9 1505.0,352.8C1505.0,342.3 1504.6,334.1 1504.0,332.9C1503.0,331.1 1501.5,331.0 1470.0,331.0L1437.0,331.0L1437.0,296.4C1437.0,274.5 1436.6,261.2 1436.0,259.9C1435.0,258.1 1433.7,258.0 1413.4,258.0L1392.0,258.0L1391.0,260.6C1390.4,262.0 1390.0,277.4 1390.0,297.1L1390.0,331.0L1357.7,331.0C1333.9,331.0 1325.1,331.3 1324.2,332.2C1323.3,333.1 1323.0,339.0 1323.0,352.7C1323.0,370.7 1323.1,372.0 1324.9,373.0C1326.2,373.6 1338.6,374.0 1358.4,374.0L1390.0,374.0L1390.0,462.5C1390.0,549.7 1390.0,551.0 1392.0,553.0C1393.9,554.9 1395.3,555.0 1413.3,555.0C1428.1,555.0 1433.1,554.7 1434.5,553.6Z\"/></svg>";

// ---------------------------------------------------------------- Bible
let BOOKS = [];
const CODE = {};
const cache = { kjv: {}, web: {} };
const TR = { web: { name: 'WEB', full: 'World English Bible' }, kjv: { name: 'KJV', full: 'King James Version' } };
async function loadBooks() {
  if (BOOKS.length) return BOOKS;
  const r = await fetch('/bible/books.json');
  BOOKS = (await r.json()).books.map(([code, name, chapters], i) => ({ i: i + 1, code, name, chapters }));
  BOOKS.forEach((b) => (CODE[b.code] = b));
  return BOOKS;
}
async function getBook(n, tr = S.settings.tr) {
  if (cache[tr][n]) return cache[tr][n];
  const r = await fetch(`/bible/${tr}/${n}.json`);
  if (!r.ok) throw new Error('bible_' + r.status);
  return (cache[tr][n] = await r.json());
}
function parseRef(ref) {
  const [code, c, vs] = ref.split(' ');
  const b = CODE[code];
  if (!b) return null;
  let v1 = null, v2 = null;
  if (vs) { const [a, z] = vs.split('-').map(Number); v1 = a; v2 = z || a; }
  return { b: b.i, code, name: b.name, c: Number(c), v1, v2 };
}
const refLabel = (r) => `${r.name} ${r.c}${r.v1 ? ':' + r.v1 + (r.v2 && r.v2 !== r.v1 ? '–' + r.v2 : '') : ''}`;
const clean = (t) => esc(t).replace(/\[([^\]]+)\]/g, '<i>$1</i>');
const plain = (t) => String(t).replace(/[\[\]]/g, '');
async function passage(ref, tr) {
  await loadBooks();
  const r = parseRef(ref);
  if (!r) return { label: ref, text: '' };
  const bk = await getBook(r.b, tr);
  const ch = bk.c[r.c - 1] || [];
  const vs = r.v1 ? ch.slice(r.v1 - 1, r.v2) : ch;
  return { label: refLabel(r), text: plain(vs.join(' ')), r };
}
async function fillScripture(root = document) {
  const els = $$('[data-scripture]', root);
  await Promise.all(els.map(async (el) => {
    try { const p = await passage(el.dataset.scripture); el.innerHTML = `“${esc(p.text)}”<span class="r">${esc(p.label)} (${TR[S.settings.tr].name})</span>`; }
    catch { el.innerHTML = `<span class="r">${esc(el.dataset.scripture)}</span>`; }
  }));
}
const dayOfYear = () => Math.floor((Date.now() - new Date(new Date().getFullYear(), 0, 0)) / 864e5);
const votdRef = () => AC.votd[dayOfYear() % AC.votd.length];

// ---------------------------------------------------------------- Shell
const app = $('#app');
let cleanup = [];
const darkMQ = matchMedia('(prefers-color-scheme: dark)');
function applyTheme() {
  const t = S.settings.theme === 'auto' || !S.settings.theme ? (darkMQ.matches ? 'dark' : 'light') : S.settings.theme;
  document.documentElement.dataset.theme = t; document.body.dataset.theme = t;
  const m = $('meta[name=theme-color]'); if (m) m.content = t === 'dark' ? '#13201C' : t === 'sepia' ? '#F3E9D7' : '#F8F3EA';
}
darkMQ.addEventListener?.('change', () => { if (S.settings.theme === 'auto') applyTheme(); });
function toast(msg) { $$('.toast').forEach((t) => t.remove()); const t = document.createElement('div'); t.className = 'toast'; t.setAttribute('role', 'status'); t.textContent = msg; document.body.appendChild(t); setTimeout(() => t.remove(), 2600); }
function tabs(active) {
  const t = (id, label, icon, href) => `<a class="tab" href="${href}" ${active === id ? 'aria-current="page"' : ''}>${ic(icon, 23, active === id ? 2.3 : 1.9)}${label}</a>`;
  return `<nav class="tabs" aria-label="Main">${t('home', 'Home', 'home', '#/')}${t('bible', 'Bible', 'book', '#/bible')}<a class="tab" href="#/gather" aria-label="Gather: start a response point" ${active === 'gather' ? 'aria-current="page"' : ''}><span class="tab-gather">${ic('qr', 25)}</span></a>${t('learn', 'Learn', 'cap', '#/learn')}${t('walk', 'Walk', 'walk', '#/walk')}</nav>`;
}
const top = (back, title = '', right = '') => `<div class="top">${back ? `<button class="back" data-back="${back}">${ic('left', 18)}Back</button>` : '<span></span>'}${title ? `<span class="h3">${title}</span>` : ''}${right || '<span style="width:44px"></span>'}</div>`;
function render(html, { tab = null, cls = '' } = {}) {
  cleanup.forEach((f) => f()); cleanup = [];
  $$('.sheet,.scrim').forEach((e) => e.remove());
  app.innerHTML = `<main class="${tab ? '' : 'no-tabs'} ${cls} fade-in" id="main" tabindex="-1">${html}</main>${tab ? tabs(tab) : ''}`;
  window.scrollTo(0, 0);
  fillScripture(app);
}
document.addEventListener('click', (e) => {
  const b = e.target.closest('[data-back]');
  if (b) { e.preventDefault(); if (history.length > 1 && b.dataset.back === 'history') history.back(); else location.hash = b.dataset.back; }
});

// ---------------------------------------------------------------- Router
const routes = [];
const on = (re, fn) => routes.push([re, fn]);
async function route() {
  const h = location.hash.replace(/^#/, '') || '/';
  const [path, qs] = h.split('?');
  const q = new URLSearchParams(qs || '');
  if (!S.onboarded && !path.startsWith('/respond')) return welcome();
  for (const [re, fn] of routes) { const m = path.match(re); if (m) { try { await fn(m, q); } catch (err) { console.error(err); render(`${top('#/')}<div class="empty"><p class="h3">Something went wrong</p><p class="p">Please check your connection and try again.</p></div>`, { tab: 'home' }); } return; } }
  location.hash = '#/';
}
addEventListener('hashchange', route);

// ---------------------------------------------------------------- Welcome
function welcome() {
  app.innerHTML = `<div class="welcome fade-in">
    <div class="ring" style="right:-120px;top:-80px;width:340px;height:340px;background:#1B4740"></div>
    <div class="ring" style="right:40px;top:90px;width:120px;height:120px;border:2px solid #E8A577"></div>
    <div style="color:#F8F3EA">${LOGO}</div>
    <div style="margin-top:auto" class="stack">
      <p class="k" style="color:#E8A577">The Always App</p>
      <h1 class="big-serif" style="font-size:40px;color:#F8F3EA">Share Jesus.<br>Walk with people.</h1>
      <p class="p" style="color:#CFE0D7;font-size:16.5px">A Bible, conversation guides, training and follow-up in one free app. Your prayer list and notes stay on this phone.</p>
      <div class="field" style="margin-top:6px"><label for="w-name" style="color:#F8F3EA">What should we call you? <span style="font-weight:500;color:#B9D0C6">(optional)</span></label><input class="input" id="w-name" autocomplete="given-name" maxlength="40" placeholder="First name"></div>
      <div class="label" style="color:#F8F3EA">Choose your Bible</div>
      <div class="seg" role="group" aria-label="Bible translation" style="background:#24534B"><button data-tr="web" aria-pressed="true" style="color:#F8F3EA">WEB, modern</button><button data-tr="kjv" aria-pressed="false" style="color:#F8F3EA">KJV, classic</button></div>
      <button class="btn peach" id="w-go" style="margin-top:10px">Get started</button>
      <p class="note" style="color:#8FB0A3;text-align:center">Free. No ads. No account needed.</p>
    </div></div>`;
  let tr = 'web';
  $$('[data-tr]').forEach((b) => b.addEventListener('click', () => { tr = b.dataset.tr; $$('[data-tr]').forEach((x) => { x.setAttribute('aria-pressed', x === b); x.style.background = x === b ? '#1B4740' : 'transparent'; }); }));
  $('[data-tr="web"]').style.background = '#1B4740';
  $('#w-go').addEventListener('click', () => { S.onboarded = true; S.settings.name = $('#w-name').value.trim().slice(0, 40); S.settings.tr = tr; save(); location.hash = '#/'; route(); });
}

// ---------------------------------------------------------------- Home
on(/^\/$/, async () => {
  const hr = new Date().getHours();
  const greet = hr < 12 ? 'Good morning' : hr < 18 ? 'Good afternoon' : 'Good evening';
  const name = S.settings.name ? `, ${esc(S.settings.name)}` : '';
  const activePlan = Object.entries(S.plans).find(([, p]) => p.done.length < (AC.plans.find((x) => x.id === p.id)?.days || 0));
  const plan = activePlan && AC.plans.find((x) => x.id === activePlan[0]);
  const pray = S.prayer.filter((p) => !p.answered).slice(0, 3).map((p) => esc(p.name));
  await loadBooks();
  const pos = BOOKS[S.pos.b - 1];
  render(`
    <div class="row between" style="padding-top:8px"><div class="logo">${LOGO}</div><a class="icon-btn" href="#/me" aria-label="Me and settings">${ic('user')}</a></div>
    <div class="hello stack-s"><p class="k">${greet}${name}</p><h1 class="big-serif">Who will you walk with today?</h1></div>
    <div class="sp"></div>
    <a class="verse-card tod-${hr < 6 || hr >= 20 ? 'night' : hr < 10 ? 'dawn' : hr < 17 ? 'day' : 'dusk'}" href="#/bible?ref=${encodeURIComponent(votdRef())}" style="text-decoration:none;display:block"><p class="k" style="color:#E8A577">Verse of the day</p><p class="serif" data-votd>…</p><span class="ref" data-votd-ref></span></a>
    <div class="sp2"></div>
    <div class="quick">
      <a class="card peach" href="#/gather"><span class="ico" style="background:rgba(30,42,38,.1);color:var(--night)">${ic('qr')}</span><div><p class="h3">Start a response point</p><p class="note" style="color:#5A3A22">Show a QR code</p></div></a>
      <a class="card" href="#/bible"><span class="ico">${ic('book')}</span><div><p class="h3">Keep reading</p><p class="note">${esc(pos.name)} ${S.pos.c}</p></div></a>
      <a class="card" href="#/learn/story"><span class="ico sand">${ic('sparkle')}</span><div><p class="h3">God’s story</p><p class="note">In four moments</p></div></a>
      <a class="card" href="#/walk/pray"><span class="ico peach">${ic('heart')}</span><div><p class="h3">Pray</p><p class="note">${pray.length ? pray.join(', ') : 'Start your list'}</p></div></a>
    </div>
    ${(() => { const d = dueToday(); return d.length ? `<div class="sp2"></div><a class="card today" href="#/walk/p/${d[0].p.id}" style="text-decoration:none"><p class="k">Today</p><p class="h3">${esc(d[0].st)} · ${esc(d[0].p.name)}</p>${d.length > 1 ? `<p class="note">and ${d.length - 1} more step${d.length > 2 ? 's' : ''} for people you’re walking with</p>` : ''}</a>` : ''; })()}
    <div class="sp2"></div>
    ${plan ? `<a class="card" href="#/plan/${plan.id}" style="text-decoration:none"><div class="row between"><p class="k">Your reading plan</p><span class="pill">Day ${Math.min(activePlan[1].done.length + 1, plan.days)} of ${plan.days}</span></div><p class="h3">${esc(plan.title)}</p><div class="progress"><i style="width:${(activePlan[1].done.length / plan.days) * 100}%"></i></div></a>` :
      `<a class="sent-hero sm" href="#/plan/sent30"><span class="sent-badge">30-day plan</span><p class="sent-ht">Sent</p><p class="sent-hs">A reading, a verse and one small step of faith each day.</p></a>`}
    <div class="sp2"></div>
    <p class="h2">Ready for a conversation</p><div class="sp"></div>
    <div class="list">
      <a class="li" href="#/gather/moment"><span class="ico peach">${ic('flame')}</span><div class="grow"><div class="t">Leading the moment</div><div class="s">When someone says yes to Jesus</div></div><span class="chev">${ic('right', 18)}</span></a>
      <a class="li" href="#/learn/guides"><span class="ico">${ic('chat')}</span><div class="grow"><div class="t">Conversation guides</div><div class="s">No faith, Muslim, Buddhist, and more</div></div><span class="chev">${ic('right', 18)}</span></a>
      <a class="li" href="#/connect"><span class="ico sand">${ic('church')}</span><div class="grow"><div class="t">Find a church</div><div class="s">A next step near home</div></div><span class="chev">${ic('right', 18)}</span></a>
      <a class="li" href="#/card" onclick="window.CARD=null"><span class="ico">${ic('image')}</span><div class="grow"><div class="t">Make a share card</div><div class="s">A verse or an invitation, ready to send</div></div><span class="chev">${ic('right', 18)}</span></a>
      <a class="li" href="#/baptism"><span class="ico peach">${ic('sparkle')}</span><div class="grow"><div class="t">Ready to be baptised?</div><div class="s">Ask a church to help you take the step</div></div><span class="chev">${ic('right', 18)}</span></a>
    </div>`, { tab: 'home' });
  passage(votdRef()).then((p) => { const v = $('[data-votd]'); if (v) { v.textContent = `“${p.text}”`; $('[data-votd-ref]').textContent = `${p.label} · ${TR[S.settings.tr].name}`; } }).catch(() => {});
});

// ---------------------------------------------------------------- Bible reader
let sel = new Set();
on(/^\/bible$/, async (m, q) => {
  await loadBooks();
  if (q.get('ref')) { const r = parseRef(q.get('ref')); if (r) { S.pos = { b: r.b, c: r.c }; save(); } }
  const planId = q.get('plan'), planDay = Number(q.get('day'));
  const { b, c } = S.pos;
  const book = BOOKS[b - 1];
  const tr = S.settings.tr;
  render(`<div class="bible-bar">
      <a class="bible-ref" href="#/bible/books" aria-label="Choose book and chapter">${esc(book.name)} ${c} ${ic('down', 16)}</a>
      <button class="bible-tr" id="tr" aria-label="Translation: ${TR[tr].full}. Tap to switch">${TR[tr].name}</button>
      <a class="icon-btn" href="#/bible/search" aria-label="Search the Bible">${ic('search')}</a>
      <a class="icon-btn" href="#/listen" aria-label="Listen">${ic('headphones')}</a>
      <button class="icon-btn" id="aa" aria-label="Text settings">${ic('type')}</button>
    </div>
    ${planId ? `<div class="card sage" style="margin:6px 0 10px"><div class="row between"><div><p class="k">Reading plan</p><p class="h3">Day ${planDay}</p></div><button class="btn small" id="plan-done">${ic('check', 18)}Done</button></div></div>` : ''}
    <article class="reader" id="reader" style="--rs:${S.settings.size}px" aria-live="polite"><p class="p">Loading…</p></article>
    <div class="chap-nav"><button class="btn light small" id="prev" ${b === 1 && c === 1 ? 'disabled' : ''}>${ic('left', 18)}Previous</button><a class="btn light small" href="#/bible/library">${ic('bookmark', 18)}Saved</a><button class="btn light small" id="next" ${b === 66 && c === book.chapters ? 'disabled' : ''}>Next${ic('right', 18)}</button></div>
    <p class="note" style="text-align:center;margin-top:22px">${TR[tr].full}, public domain.</p>`, { tab: 'bible' });
  const data = await getBook(b, tr);
  const verses = data.c[c - 1] || [];
  const paras = new Set((data.p && data.p[c - 1]) || []);
  let html = `<h2>${esc(book.name)}</h2><div class="chap">${c}</div><p>`;
  verses.forEach((t, i) => {
    const n = i + 1, k = `${b}.${c}.${n}`;
    if (n > 1 && paras.has(n)) html += '</p><p>';
    html += `<span class="v${S.hl[k] ? ' h-' + S.hl[k] : ''}" data-v="${n}" role="button" tabindex="0" aria-label="Verse ${n}"><sup>${n}</sup>${clean(t)}${S.notes[k] ? '<span class="nmark" aria-label="has a note"></span>' : ''} </span>`;
  });
  $('#reader').innerHTML = html + '</p>';
  sel = new Set();
  const go = (db, dc) => { S.pos = { b: db, c: dc }; save(); location.hash = '#/bible'; route(); };
  $('#prev').onclick = () => (c > 1 ? go(b, c - 1) : go(b - 1, BOOKS[b - 2].chapters));
  $('#next').onclick = () => (c < book.chapters ? go(b, c + 1) : go(b + 1, 1));
  $('#tr').onclick = () => { S.settings.tr = tr === 'web' ? 'kjv' : 'web'; save(); route(); toast(`Now reading the ${TR[S.settings.tr].full}`); };
  $('#aa').onclick = textSheet;
  if (planId) $('#plan-done').onclick = () => { const p = S.plans[planId]; if (p && !p.done.includes(planDay)) p.done.push(planDay); save(); toast('Day marked as read'); location.hash = '#/plan/' + planId; };
  const pick = (el) => { const n = Number(el.dataset.v); sel.has(n) ? sel.delete(n) : sel.add(n); el.classList.toggle('sel', sel.has(n)); sel.size ? verseSheet(b, c, verses) : closeSheet(); };
  $('#reader').addEventListener('click', (e) => { const v = e.target.closest('.v'); if (v) pick(v); });
  $('#reader').addEventListener('keydown', (e) => { const v = e.target.closest('.v'); if (v && (e.key === 'Enter' || e.key === ' ')) { e.preventDefault(); pick(v); } });
  let sx = null;
  const ts = (e) => (sx = e.touches[0].clientX), te = (e) => { if (sx === null) return; const dx = e.changedTouches[0].clientX - sx; sx = null; if (Math.abs(dx) > 90 && !$('.sheet')) (dx < 0 ? $('#next') : $('#prev')).click(); };
  $('#reader').addEventListener('touchstart', ts, { passive: true }); $('#reader').addEventListener('touchend', te);
});
function closeSheet() { $$('.sheet,.scrim').forEach((e) => e.remove()); }
function sheet(html, { scrim = true } = {}) { closeSheet(); if (scrim) { const s = document.createElement('div'); s.className = 'scrim'; s.onclick = () => { closeSheet(); $$('.v.sel').forEach((v) => v.classList.remove('sel')); sel = new Set(); }; document.body.appendChild(s); } const d = document.createElement('div'); d.className = 'sheet'; d.setAttribute('role', 'dialog'); d.innerHTML = '<div class="grab"></div>' + html; document.body.appendChild(d); return d; }
function textSheet() {
  const d = sheet(`<p class="h3" style="margin-bottom:12px">Text</p>
    <div class="row between"><span class="label">Size</span><div class="row"><button class="chip" data-sz="-2" aria-label="Smaller text">A−</button><button class="chip" data-sz="2" aria-label="Larger text">A+</button></div></div>
    <div class="sp2"></div><span class="label">Background</span><div class="sp"></div>
    <div class="seg" role="group" aria-label="Theme">${[['auto', 'Auto'], ['light', 'Light'], ['sepia', 'Warm'], ['dark', 'Dark']].map(([k, l]) => `<button data-th="${k}" aria-pressed="${S.settings.theme === k}">${l}</button>`).join('')}</div>`);
  $$('[data-sz]', d).forEach((b) => (b.onclick = () => { S.settings.size = Math.max(15, Math.min(30, S.settings.size + Number(b.dataset.sz))); save(); $('#reader')?.style.setProperty('--rs', S.settings.size + 'px'); }));
  $$('[data-th]', d).forEach((b) => (b.onclick = () => { S.settings.theme = b.dataset.th; save(); applyTheme(); $$('[data-th]', d).forEach((x) => x.setAttribute('aria-pressed', x === b)); }));
}
function verseSheet(b, c, verses) {
  const list = [...sel].sort((x, y) => x - y);
  const book = BOOKS[b - 1];
  const label = `${book.name} ${c}:${list.length > 1 && list[list.length - 1] - list[0] === list.length - 1 ? list[0] + '–' + list[list.length - 1] : list.join(',')}`;
  const text = list.map((n) => plain(verses[n - 1])).join(' ');
  const keys = list.map((n) => `${b}.${c}.${n}`);
  const marked = S.marks.some((m) => m.k === keys[0]);
  const d = sheet(`<div class="row between"><p class="h3">${esc(label)}</p><button class="icon-btn" data-close aria-label="Close">${ic('x')}</button></div>
    <div class="sp"></div><div class="swatches" role="group" aria-label="Highlight colour">${['yellow', 'peach', 'sage', 'blue', 'pink'].map((col) => `<button class="sw" data-hl="${col}" style="background:var(--hl-${col})" aria-label="Highlight ${col}" aria-pressed="${keys.every((k) => S.hl[k] === col)}"></button>`).join('')}<button class="sw" data-hl="" aria-label="Remove highlight" style="display:grid;place-items:center;background:var(--card)">${ic('x', 16)}</button></div>
    <div class="sp2"></div><div class="actions">
      <button class="act" data-a="copy">${ic('copy')}Copy</button><button class="act" data-a="share">${ic('share')}Share</button><button class="act" data-a="image">${ic('image')}Image</button><button class="act" data-a="note">${ic('pen')}Note</button>
    </div><div class="sp"></div><button class="btn light small" data-a="mark" style="width:100%">${ic('bookmark', 18)}${marked ? 'Remove bookmark' : 'Bookmark'}</button>`, { scrim: false });
  $('[data-close]', d).onclick = () => { closeSheet(); $$('.v.sel').forEach((v) => v.classList.remove('sel')); sel = new Set(); };
  $$('[data-hl]', d).forEach((s) => (s.onclick = () => { keys.forEach((k) => { if (s.dataset.hl) S.hl[k] = s.dataset.hl; else delete S.hl[k]; }); save(); list.forEach((n) => { const el = $(`.v[data-v="${n}"]`); el.className = 'v' + (S.hl[`${b}.${c}.${n}`] ? ' h-' + S.hl[`${b}.${c}.${n}`] : ''); }); sel = new Set(); closeSheet(); }));
  const full = `“${text}” — ${label} (${TR[S.settings.tr].name})`;
  $('[data-a="copy"]', d).onclick = async () => { try { await navigator.clipboard.writeText(full); toast('Copied'); } catch { toast('Copy isn’t available here'); } };
  $('[data-a="share"]', d).onclick = async () => { if (navigator.share) { try { await navigator.share({ text: full }); } catch {} } else { try { await navigator.clipboard.writeText(full); toast('Copied to share'); } catch {} } };
  $('[data-a="image"]', d).onclick = () => verseImage(text, label);
  $('[data-a="note"]', d).onclick = () => noteSheet(keys[0], label);
  $('[data-a="mark"]', d).onclick = () => { if (marked) S.marks = S.marks.filter((m) => m.k !== keys[0]); else S.marks.unshift({ k: keys[0], label, text: text.slice(0, 160), at: Date.now() }); save(); toast(marked ? 'Bookmark removed' : 'Bookmarked'); closeSheet(); $$('.v.sel').forEach((v) => v.classList.remove('sel')); sel = new Set(); };
}
function noteSheet(k, label) {
  const d = sheet(`<p class="h3">Note on ${esc(label)}</p><p class="note">Kept on this device.</p><div class="sp"></div><textarea class="input" id="note-t" aria-label="Your note">${esc(S.notes[k]?.text || '')}</textarea><div class="sp"></div><div class="row"><button class="btn" id="note-s">Save note</button>${S.notes[k] ? `<button class="btn ghost small" id="note-d">${ic('trash', 18)}</button>` : ''}</div>`);
  $('#note-t').focus();
  $('#note-s').onclick = () => { const t = $('#note-t').value.trim(); if (t) S.notes[k] = { text: t, label, at: Date.now() }; else delete S.notes[k]; save(); closeSheet(); toast('Note saved'); route(); };
  if ($('#note-d')) $('#note-d').onclick = () => { delete S.notes[k]; save(); closeSheet(); route(); };
}
function verseImage(text, label) { window.CARD = { kind: 'verse', text, label: `${label} · ${TR[S.settings.tr].name}` }; closeSheet(); location.hash = '#/card'; }
const CARD_STYLES = {
  forest: { bg: ['#1F5248', '#12302A'], glow: '#2C6A5C', ink: '#F8F3EA', accent: '#E8A577', label: 'Forest' },
  dawn: { bg: ['#F2B48A', '#E08E5E'], glow: '#F8D2B4', ink: '#1E2A26', accent: '#1B4740', label: 'Dawn' },
  paper: { bg: ['#FBF6EC', '#EFE5D3'], glow: '#FFFFFF', ink: '#1B4740', accent: '#A4562A', label: 'Paper' },
  night: { bg: ['#22302B', '#101A17'], glow: '#34463F', ink: '#F8F3EA', accent: '#F8D486', label: 'Night' },
};
function wrapText(x, text, maxW) { const words = text.split(/\s+/), lines = []; let line = ''; for (const w of words) { const t = line ? line + ' ' + w : w; if (x.measureText(t).width > maxW && line) { lines.push(line); line = w; } else line = t; } if (line) lines.push(line); return lines; }
function drawCard(cv, c) {
  const W = 1080, H = 1350, x = cv.getContext('2d'), st = CARD_STYLES[c.style] || CARD_STYLES.forest; cv.width = W; cv.height = H;
  const g = x.createLinearGradient(0, 0, W * .4, H); g.addColorStop(0, st.bg[0]); g.addColorStop(1, st.bg[1]); x.fillStyle = g; x.fillRect(0, 0, W, H);
  const r = x.createRadialGradient(W * .92, H * .06, 10, W * .92, H * .06, 760); r.addColorStop(0, st.glow + 'AA'); r.addColorStop(1, st.glow + '00'); x.fillStyle = r; x.fillRect(0, 0, W, H);
  x.strokeStyle = st.accent; x.globalAlpha = .9; x.lineWidth = 4; x.beginPath(); x.arc(W - 150, 210, 92, 0, Math.PI * 2); x.stroke(); x.globalAlpha = 1;
  x.fillStyle = st.accent; x.beginPath(); x.arc(W - 150, 210, 28, 0, Math.PI * 2); x.fill();
  x.fillStyle = st.ink; let y;
  if (c.kind === 'invite') {
    x.font = '800 40px Manrope, sans-serif'; x.fillStyle = st.accent; x.fillText(c.kicker || 'You’re invited', 100, 520);
    x.fillStyle = st.ink; x.font = '400 104px Newsreader, Georgia, serif'; y = 650;
    wrapText(x, c.title || 'Come as you are', W - 200).slice(0, 4).forEach((l) => { x.fillText(l, 100, y); y += 116; });
    x.font = '600 40px Manrope, sans-serif'; y += 30;
    [c.when, c.where].filter(Boolean).forEach((l) => { wrapText(x, l, W - 200).slice(0, 2).forEach((ll) => { x.fillText(ll, 100, y); y += 56; }); });
  } else {
    const text = `“${c.text}”`, size = text.length > 300 ? 44 : text.length > 200 ? 52 : text.length > 120 ? 62 : 74;
    x.font = `400 ${size}px Newsreader, Georgia, serif`; const lines = wrapText(x, text, W - 200), lh = size * 1.3;
    y = Math.max(360, (H - lines.length * lh) / 2 + 30); lines.forEach((l) => { x.fillText(l, 100, y); y += lh; });
    x.font = '800 34px Manrope, sans-serif'; x.fillStyle = st.accent; x.fillText(c.label || '', 100, y + 36);
  }
  x.fillStyle = st.ink; x.font = '800 40px Manrope, sans-serif'; x.fillText('always', 100, H - 100);
  x.strokeStyle = st.accent; x.lineWidth = 7; x.lineCap = 'round'; x.beginPath(); x.moveTo(268, H - 140); x.lineTo(268, H - 92); x.moveTo(256, H - 128); x.lineTo(280, H - 128); x.stroke();
}
on(/^\/card$/, async () => {
  const c = Object.assign({ kind: 'verse', style: 'forest', title: 'Come as you are', kicker: 'You’re invited', when: '', where: '' }, window.CARD || {});
  if (c.kind === 'verse' && !c.text) { const p = await passage(votdRef()); c.text = p.text; c.label = `${p.label} · ${TR[S.settings.tr].name}`; }
  window.CARD = c;
  try { await Promise.all([document.fonts.load('400 60px Newsreader'), document.fonts.load('800 30px Manrope'), document.fonts.load('600 30px Manrope')]); } catch {}
  render(`${top('#/', 'Share card')}
    <div class="seg" role="group" aria-label="Card"><button data-k="verse" aria-pressed="${c.kind === 'verse'}">Verse</button><button data-k="invite" aria-pressed="${c.kind === 'invite'}">Invitation</button></div>
    <div class="sp"></div><div class="card-preview"><canvas id="cv" aria-label="Preview of your card" role="img"></canvas></div><div class="sp"></div>
    <div class="swatches" role="group" aria-label="Style">${Object.entries(CARD_STYLES).map(([k, v]) => `<button data-st="${k}" aria-pressed="${c.style === k}" aria-label="${v.label}" style="background:linear-gradient(150deg,${v.bg[0]},${v.bg[1]})"><i style="background:${v.accent}"></i></button>`).join('')}</div>
    <div id="inv" class="stack-s" style="${c.kind === 'invite' ? '' : 'display:none'}"><div class="sp"></div>
      <div class="field"><label for="ci-t">Headline</label><input class="input" id="ci-t" maxlength="60" value="${esc(c.title)}"></div>
      <div class="field"><label for="ci-w">When</label><input class="input" id="ci-w" maxlength="60" placeholder="Tuesdays at 7pm" value="${esc(c.when)}"></div>
      <div class="field"><label for="ci-p">Where</label><input class="input" id="ci-p" maxlength="60" placeholder="Hope Church, Parramatta" value="${esc(c.where)}"></div></div>
    <div class="sp2"></div><button class="btn peach" id="c-share">${ic('share', 20)}Share card</button>
    <p class="note" style="margin-top:10px;text-align:center">Made on your phone. Nothing is uploaded.</p>`, { tab: 'home' });
  const cv = $('#cv'), redraw = () => drawCard(cv, window.CARD); redraw();
  $$('[data-k]').forEach((b) => (b.onclick = () => { window.CARD.kind = b.dataset.k; route(); }));
  $$('[data-st]').forEach((b) => (b.onclick = () => { window.CARD.style = b.dataset.st; $$('[data-st]').forEach((x) => x.setAttribute('aria-pressed', x === b)); redraw(); }));
  [['ci-t', 'title'], ['ci-w', 'when'], ['ci-p', 'where']].forEach(([id, k]) => $('#' + id)?.addEventListener('input', (e) => { window.CARD[k] = e.target.value; redraw(); }));
  $('#c-share').onclick = () => cv.toBlob(async (blob) => {
    const name = window.CARD.kind === 'invite' ? 'invitation.png' : 'verse.png', file = new File([blob], name, { type: 'image/png' });
    if (navigator.canShare && navigator.canShare({ files: [file] })) { try { await navigator.share({ files: [file] }); return; } catch {} }
    const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = name; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 4000);
  }, 'image/png');
});
on(/^\/bible\/books$/, async () => {
  await loadBooks();
  const btn = (b) => `<button class="book" data-b="${b.i}">${esc(b.name)}</button>`;
  render(`${top('#/bible', 'Books')}<div class="seg" role="group" aria-label="Translation">${Object.entries(TR).map(([k, t]) => `<button data-tr="${k}" aria-pressed="${S.settings.tr === k}">${t.name}</button>`).join('')}</div>
    <div class="sp2"></div><p class="k">Old Testament</p><div class="sp"></div><div class="books">${BOOKS.slice(0, 39).map(btn).join('')}</div>
    <div class="sp2"></div><p class="k">New Testament</p><div class="sp"></div><div class="books">${BOOKS.slice(39).map(btn).join('')}</div>`);
  $$('[data-tr]').forEach((b) => (b.onclick = () => { S.settings.tr = b.dataset.tr; save(); $$('[data-tr]').forEach((x) => x.setAttribute('aria-pressed', x === b)); }));
  $$('[data-b]').forEach((el) => (el.onclick = () => {
    const bk = BOOKS[el.dataset.b - 1];
    if (bk.chapters === 1) { S.pos = { b: bk.i, c: 1 }; save(); location.hash = '#/bible'; return; }
    render(`${top('#/bible/books', esc(bk.name))}<div class="chaps">${Array.from({ length: bk.chapters }, (_, i) => `<button data-c="${i + 1}">${i + 1}</button>`).join('')}</div>`);
    $$('[data-c]').forEach((c) => (c.onclick = () => { S.pos = { b: bk.i, c: Number(c.dataset.c) }; save(); location.hash = '#/bible'; }));
  }));
});
on(/^\/bible\/search$/, async () => {
  await loadBooks();
  render(`${top('#/bible', 'Search')}<form id="sf" class="row"><input class="input grow" id="sq" type="search" placeholder="Search words, like “peace”" aria-label="Search the Bible" enterkeyhint="search"><button class="btn small" type="submit">Search</button></form>
    <div class="sp"></div><div class="chips" role="group" aria-label="Search in"><button class="chip on" data-scope="all" aria-pressed="true">Whole Bible</button><button class="chip" data-scope="nt" aria-pressed="false">New Testament</button><button class="chip" data-scope="ot" aria-pressed="false">Old Testament</button></div>
    <p class="note" id="sstat" style="margin-top:12px"></p><div id="sres"></div>`);
  let scope = 'all';
  $$('[data-scope]').forEach((b) => (b.onclick = () => { scope = b.dataset.scope; $$('[data-scope]').forEach((x) => { x.classList.toggle('on', x === b); x.setAttribute('aria-pressed', x === b); }); }));
  $('#sq').focus();
  $('#sf').onsubmit = async (e) => {
    e.preventDefault();
    const term = $('#sq').value.trim(); if (term.length < 2) return;
    const tr = S.settings.tr, list = BOOKS.filter((b) => scope === 'all' || (scope === 'nt' ? b.i > 39 : b.i <= 39));
    const re = new RegExp(term.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'), 'i'), out = [];
    let done = 0;
    for (const b of list) {
      const d = await getBook(b.i, tr); done++;
      $('#sstat').textContent = `Searching… ${Math.round((done / list.length) * 100)}%`;
      d.c.forEach((ch, ci) => ch.forEach((t, vi) => { if (out.length < 300 && re.test(plain(t))) out.push({ b, c: ci + 1, v: vi + 1, t: plain(t) }); }));
    }
    $('#sstat').textContent = out.length ? `${out.length >= 300 ? '300+' : out.length} verses found in the ${TR[tr].full}` : 'No verses found. Try another word.';
    const hi = (t) => esc(t).replace(new RegExp('(' + esc(term).replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + ')', 'ig'), '<mark>$1</mark>');
    $('#sres').innerHTML = out.map((r) => `<a class="result" href="#/bible?ref=${encodeURIComponent(r.b.code + ' ' + r.c)}"><b>${esc(r.b.name)} ${r.c}:${r.v}</b><p>${hi(r.t)}</p></a>`).join('');
  };
});
on(/^\/bible\/library$/, async () => {
  await loadBooks();
  const hl = Object.entries(S.hl).map(([k, col]) => ({ k, col })).slice(-200).reverse();
  const notes = Object.entries(S.notes).sort((a, b) => b[1].at - a[1].at);
  const open = (k) => { const [b, c] = k.split('.').map(Number); return `#/bible?ref=${encodeURIComponent(BOOKS[b - 1].code + ' ' + c)}`; };
  const lbl = (k) => { const [b, c, v] = k.split('.').map(Number); return `${BOOKS[b - 1].name} ${c}:${v}`; };
  render(`${top('#/bible', 'Saved')}<div class="seg" role="tablist"><button data-t="marks" aria-pressed="true">Bookmarks</button><button data-t="hl" aria-pressed="false">Highlights</button><button data-t="notes" aria-pressed="false">Notes</button></div><div class="sp2"></div>
    <div data-p="marks">${S.marks.length ? `<div class="list">${S.marks.map((m) => `<a class="li" href="${open(m.k)}"><span class="ico">${ic('bookmark')}</span><div class="grow"><div class="t">${esc(m.label)}</div><div class="s">${esc(m.text)}</div></div></a>`).join('')}</div>` : '<div class="empty"><p class="h3">No bookmarks yet</p><p class="p">Tap a verse, then Bookmark.</p></div>'}</div>
    <div data-p="hl" hidden>${hl.length ? `<div class="list">${hl.map((h) => `<a class="li" href="${open(h.k)}"><span class="sw" style="width:22px;height:22px;background:var(--hl-${h.col})"></span><div class="grow"><div class="t">${esc(lbl(h.k))}</div></div><span class="chev">${ic('right', 18)}</span></a>`).join('')}</div>` : '<div class="empty"><p class="h3">No highlights yet</p><p class="p">Tap a verse and choose a colour.</p></div>'}</div>
    <div data-p="notes" hidden>${notes.length ? `<div class="list">${notes.map(([k, n]) => `<a class="li" href="${open(k)}"><span class="ico peach">${ic('pen')}</span><div class="grow"><div class="t">${esc(n.label)}</div><div class="s">${esc(n.text)}</div></div></a>`).join('')}</div>` : '<div class="empty"><p class="h3">No notes yet</p><p class="p">Tap a verse, then Note.</p></div>'}</div>`);
  $$('[data-t]').forEach((b) => (b.onclick = () => { $$('[data-t]').forEach((x) => x.setAttribute('aria-pressed', x === b)); $$('[data-p]').forEach((p) => (p.hidden = p.dataset.p !== b.dataset.t)); }));
});

// ---------------------------------------------------------------- Listen
let audio = null;
on(/^\/listen$/, async () => {
  await loadBooks();
  const { b, c } = S.pos, book = BOOKS[b - 1];
  const voices = () => (speechSynthesis?.getVoices() || []).filter((v) => /^en/i.test(v.lang));
  render(`${top('#/bible', 'Listen')}
    <div class="listen-art paused" id="art"><div class="ring"></div><div class="orb"></div></div>
    <div class="sp2"></div><div style="text-align:center"><p class="k">${TR[S.settings.tr].full}</p><p class="h2">${esc(book.name)} ${c}</p><p class="note" id="lstat">Ready</p></div>
    <div class="sp2"></div><div class="row" style="justify-content:center;gap:22px"><button class="icon-btn" id="lprev" aria-label="Previous chapter">${ic('left', 26)}</button><button class="big-play" id="lplay" aria-label="Play">${ic('play', 30)}</button><button class="icon-btn" id="lnext" aria-label="Next chapter">${ic('right', 26)}</button></div>
    <div class="sp2"></div><div class="list">
      <div class="li"><span class="ico">${ic('music')}</span><div class="grow"><div class="t">Soft music</div><div class="s">A gentle pad under the reading</div></div><input type="checkbox" id="lmusic" style="width:24px;height:24px;accent-color:var(--green)" aria-label="Soft music"></div>
      <div class="li"><span class="ico sand">${ic('moon')}</span><div class="grow"><div class="t">Sleep timer</div><div class="chips" style="margin-top:8px">${[0, 10, 20, 30, 60].map((n) => `<button class="chip${n === 0 ? ' on' : ''}" data-sleep="${n}" aria-pressed="${n === 0}">${n ? n + ' min' : 'Off'}</button>`).join('')}</div></div></div>
      <div class="li"><span class="ico peach">${ic('user')}</span><div class="grow"><label class="t" for="lvoice">Voice</label><select class="input" id="lvoice" style="margin-top:8px;min-height:44px"></select></div></div>
    </div>${!('speechSynthesis' in window) ? '<p class="err" style="margin-top:12px">Listening isn’t supported in this browser.</p>' : ''}`);
  const fillVoices = () => { const vs = voices(); $('#lvoice').innerHTML = vs.map((v, i) => `<option value="${i}" ${/AU/.test(v.lang) && !$('#lvoice').dataset.set ? 'selected' : ''}>${esc(v.name)} (${esc(v.lang)})</option>`).join('') || '<option>Default voice</option>'; };
  fillVoices(); if ('speechSynthesis' in window) speechSynthesis.onvoiceschanged = fillVoices;
  let playing = false, idx = 0, verses = [], sleepAt = 0, ctx = null, nodes = [];
  const stat = (t) => ($('#lstat').textContent = t);
  const music = (onm) => {
    if (!onm) { nodes.forEach((n) => { try { n.stop(); } catch {} }); nodes = []; return; }
    ctx = ctx || new (window.AudioContext || window.webkitAudioContext)();
    const master = ctx.createGain(); master.gain.value = 0.045; master.connect(ctx.destination);
    [146.83, 220, 293.66, 369.99].forEach((f, i) => { const o = ctx.createOscillator(); o.type = 'sine'; o.frequency.value = f; const g = ctx.createGain(); g.gain.value = 0.5; const l = ctx.createOscillator(); l.frequency.value = 0.05 + i * 0.03; const lg = ctx.createGain(); lg.gain.value = 0.4; l.connect(lg).connect(g.gain); o.connect(g).connect(master); o.start(); l.start(); nodes.push(o, l); });
  };
  const speakNext = () => {
    if (!playing) return;
    if (sleepAt && Date.now() > sleepAt) { stop(); stat('Sleep timer ended'); return; }
    if (idx >= verses.length) { stop(); stat('Chapter finished'); return; }
    const u = new SpeechSynthesisUtterance(plain(verses[idx])); const vs = voices(); const v = vs[Number($('#lvoice').value)]; if (v) u.voice = v; u.rate = 0.95;
    u.onend = () => { idx++; speakNext(); }; u.onerror = () => { idx++; speakNext(); };
    stat(`Verse ${idx + 1} of ${verses.length}`); speechSynthesis.speak(u);
  };
  const stop = () => { playing = false; speechSynthesis?.cancel(); music(false); $('#art').classList.add('paused'); $('#lplay').innerHTML = ic('play', 30); $('#lplay').setAttribute('aria-label', 'Play'); };
  $('#lplay').onclick = async () => {
    if (!('speechSynthesis' in window)) return;
    if (playing) { stop(); stat('Paused'); return; }
    verses = (await getBook(b)).c[c - 1]; playing = true; $('#art').classList.remove('paused'); $('#lplay').innerHTML = ic('pause', 30); $('#lplay').setAttribute('aria-label', 'Pause');
    if ($('#lmusic').checked) music(true);
    speakNext();
  };
  $('#lmusic').onchange = (e) => { if (playing) music(e.target.checked); };
  $$('[data-sleep]').forEach((x) => (x.onclick = () => { const n = Number(x.dataset.sleep); sleepAt = n ? Date.now() + n * 60000 : 0; $$('[data-sleep]').forEach((y) => { y.classList.toggle('on', y === x); y.setAttribute('aria-pressed', y === x); }); toast(n ? `Stopping in ${n} minutes` : 'Sleep timer off'); }));
  const move = (d) => { stop(); let nb = b, nc = c + d; if (nc < 1) { nb = b - 1; if (nb < 1) return; nc = BOOKS[nb - 1].chapters; } if (nc > book.chapters) { nb = b + 1; if (nb > 66) return; nc = 1; } S.pos = { b: nb, c: nc }; save(); route(); };
  $('#lprev').onclick = () => move(-1); $('#lnext').onclick = () => move(1);
  cleanup.push(stop);
});

// ---------------------------------------------------------------- Plans
on(/^\/plans$/, () => {
  render(`${top('#/learn', 'Reading plans')}<div class="stack">${AC.plans.map((p) => { const st = S.plans[p.id]; return `<a class="card" href="#/plan/${p.id}" style="text-decoration:none"><div class="row between"><p class="h3">${esc(p.title)}</p><span class="pill${st ? '' : ' peach'}">${st ? `${st.done.length} of ${p.days}` : `${p.days} days`}</span></div><p class="p">${esc(p.sub)}</p>${st ? `<div class="progress"><i style="width:${(st.done.length / p.days) * 100}%"></i></div>` : ''}</a>`; }).join('')}</div>`, { tab: 'learn' });
});
on(/^\/plan\/([\w-]+)$/, async (m) => {
  await loadBooks();
  const p = AC.plans.find((x) => x.id === m[1]); if (!p) return (location.hash = '#/plans');
  const st = S.plans[p.id];
  const next = st ? Array.from({ length: p.days }, (_, i) => i + 1).find((d) => !st.done.includes(d)) : 1;
  render(`${top('#/plans')}<p class="k">Reading plan</p><h1 class="h1">${esc(p.title)}</h1><p class="p" style="margin-top:6px">${esc(p.sub)}</p><div class="sp2"></div>
    ${st ? `<div class="progress"><i style="width:${(st.done.length / p.days) * 100}%"></i></div><p class="note" style="margin-top:8px">${st.done.length} of ${p.days} days read</p><div class="sp2"></div>
      ${next && p.items ? `<div class="sent-day"><p class="k">Day ${next}</p><p class="sent-t">${esc(p.items[next - 1].t)}</p><p class="scripture" data-scripture="${p.items[next - 1].key}"></p><div class="sent-do"><span>${ic('sparkle', 18)}</span><p><b>Today</b>${esc(p.items[next - 1].do)}</p></div>
        <div class="row" style="margin-top:14px"><a class="btn" href="#/bible?ref=${encodeURIComponent(p.readings[next - 1])}&plan=${p.id}&day=${next}">Read ${esc(refLabel(parseRef(p.readings[next - 1])))}</a><button class="btn light small" id="sent-card" aria-label="Share this verse as a card">${ic('image', 18)}</button></div></div>` :
      next ? `<a class="btn" href="#/bible?ref=${encodeURIComponent(p.readings[next - 1])}&plan=${p.id}&day=${next}">Read day ${next}: ${esc(refLabel(parseRef(p.readings[next - 1])))}</a>` : '<div class="card sage"><p class="h3">Plan complete</p><p class="p">Well done. Why not start another, or read it with a friend?</p></div>'}
      <div class="sp2"></div><div class="days">${p.readings.map((r, i) => `<a class="day${st.done.includes(i + 1) ? ' done' : ''}${next === i + 1 ? ' today' : ''}" href="#/bible?ref=${encodeURIComponent(r)}&plan=${p.id}&day=${i + 1}" aria-label="Day ${i + 1}: ${esc(refLabel(parseRef(r)))}">${i + 1}</a>`).join('')}</div>
      <div class="sp"></div><button class="btn ghost" id="pl-reset">Start again</button>` :
      `<div class="list">${p.readings.map((r, i) => `<div class="li"><span class="ico">${i + 1}</span><div class="grow"><div class="t">${p.items ? esc(p.items[i].t) : esc(refLabel(parseRef(r)))}</div>${p.items ? `<div class="s">${esc(refLabel(parseRef(r)))}</div>` : ''}</div></div>`).join('')}</div><div class="sp2"></div><button class="btn" id="pl-start">Start this plan</button>`}`, { tab: 'learn' });
  if ($('#pl-start')) $('#pl-start').onclick = () => { S.plans[p.id] = { id: p.id, start: today(), done: [] }; save(); route(); };
  if ($('#sent-card')) $('#sent-card').onclick = async () => { const it = p.items[next - 1], v = await passage(it.key); window.CARD = { kind: 'verse', style: 'dawn', text: v.text, label: `${v.label} · ${TR[S.settings.tr].name}` }; location.hash = '#/card'; };
  fillScripture();
  if ($('#pl-reset')) $('#pl-reset').onclick = () => { if (confirmBox('Start this plan again?')) { S.plans[p.id] = { id: p.id, start: today(), done: [] }; save(); route(); } };
});
const confirmBox = (t) => window.confirm(t);

// ---------------------------------------------------------------- Learn
on(/^\/learn$/, () => {
  const done = (c) => (S.courses[c.id] || []).length;
  render(`<div class="sp"></div><h1 class="h1">Learn</h1><p class="p" style="margin-top:6px">Grow in sharing Jesus and walking with people.</p><div class="sp2"></div>
    <a class="hero-card" href="#/learn/story" style="display:block;text-decoration:none"><p class="k" style="color:#E8A577">The heart of it</p><p class="big-serif" style="color:#F8F3EA;margin:8px 0">God’s story in four moments</p><p class="p">Created, broken, rescued, restored. Share it with anyone in a few minutes.</p></a>
    <div class="sp"></div><a class="sent-hero" href="#/plan/sent30"><span class="sent-badge">30-day plan</span><p class="sent-ht">Sent</p><p class="sent-hs">For everyday evangelists. A reading, a verse to keep and one small step of faith each day.</p>${S.plans.sent30 ? `<div class="progress"><i style="width:${(S.plans.sent30.done.length / 30) * 100}%"></i></div>` : ''}</a>
    <div class="sp2"></div><div class="row between"><p class="h2">Learn from partners</p></div><p class="p" style="margin-top:4px">Trusted training from ministries we work with. It opens on their sites.</p><div class="sp"></div>
    <div class="ptrs">${AC.partners.map((x) => `<a class="ptr ptr-${x.tone}" href="#/learn/partner/${x.id}"><span class="ptr-mono" aria-hidden="true">${x.mono}</span><span class="ptr-tx"><span class="ptr-by">Training by</span><b>${esc(x.name)}</b><span>${esc(x.tag)}</span></span><span class="ptr-n">${x.tools.length} tools</span></a>`).join('')}</div>
    <div class="sp2"></div><div class="row between"><p class="h2">More good training</p><a class="see" href="#/learn/library">See all</a></div><p class="p" style="margin-top:4px">Well-loved resources from ministries around the world.</p><div class="sp"></div>
    <div class="libs">${AC.library.slice(0, 5).map((x) => `<a class="lib lib-${x.tone}" href="${x.url}${x.url.includes('?') ? '&' : '?'}utm_source=always-app&utm_medium=referral" target="_blank" rel="noopener"><span class="lib-k">${esc(x.kind)}</span><b>${esc(x.name)}</b><span class="lib-by">${esc(x.by)}</span><span class="lib-go">${ic('ext', 16)}</span></a>`).join('')}</div>
    <div class="sp2"></div><div class="list">
      <a class="li" href="#/learn/road"><span class="ico peach">${ic('book')}</span><div class="grow"><div class="t">The Romans Road</div><div class="s">Six verses that explain the Gospel</div></div><span class="chev">${ic('right', 18)}</span></a>
      <a class="li" href="#/learn/guides"><span class="ico">${ic('chat')}</span><div class="grow"><div class="t">Conversation guides</div><div class="s">${AC.guides.length} guides for different friends</div></div><span class="chev">${ic('right', 18)}</span></a>
      <a class="li" href="#/learn/testimony"><span class="ico sand">${ic('pen')}</span><div class="grow"><div class="t">Your story</div><div class="s">Write and practise your three-minute story</div></div><span class="chev">${ic('right', 18)}</span></a>
      <a class="li" href="#/learn/questions"><span class="ico">${ic('sparkle')}</span><div class="grow"><div class="t">Big questions</div><div class="s">Honest, short answers</div></div><span class="chev">${ic('right', 18)}</span></a>
      <a class="li" href="#/plans"><span class="ico peach">${ic('cal')}</span><div class="grow"><div class="t">Reading plans</div><div class="s">Read with someone you’re walking with</div></div><span class="chev">${ic('right', 18)}</span></a>
    </div>
    <div class="sp2"></div><p class="h2">Training</p><p class="p" style="margin-top:4px">Short courses made with evangelists and churches.</p><div class="sp"></div>
    <div class="stack">${AC.courses.map((c) => `<a class="card" href="#/learn/course/${c.id}" style="text-decoration:none"><div class="row between"><p class="h3">${esc(c.title)}</p><span class="pill${done(c) === c.lessons.length ? '' : ' peach'}">${done(c) === c.lessons.length ? 'Done' : `${c.mins} min`}</span></div><p class="p">${esc(c.sub)}</p>${done(c) ? `<div class="progress"><i style="width:${(done(c) / c.lessons.length) * 100}%"></i></div>` : ''}</a>`).join('')}</div>`, { tab: 'learn' });
});
on(/^\/learn\/library$/, (m, q) => {
  const kinds = ['All', ...new Set(AC.library.map((x) => x.kind))], k = q.get('k') || 'All';
  const out = (u) => u + (u.includes('?') ? '&' : '?') + 'utm_source=always-app&utm_medium=referral';
  render(`${top('#/learn', 'Training library')}<p class="p">Well-loved evangelism training from ministries around the world. Each opens on their own site. We’re not affiliated with them, and nothing about you is sent.</p><div class="sp"></div>
    <div class="langs" role="group" aria-label="Kind">${kinds.map((x) => `<a href="#/learn/library?k=${encodeURIComponent(x)}" aria-pressed="${x === k}" class="lang-a">${x}</a>`).join('')}</div><div class="sp"></div>
    <div class="stack">${AC.library.filter((x) => k === 'All' || x.kind === k).map((x) => `<a class="libc lib-${x.tone}" href="${out(x.url)}" target="_blank" rel="noopener"><div class="row between"><span class="lib-k">${esc(x.kind)}</span><span class="lib-go">${ic('ext', 18)}</span></div><p class="libc-t">${esc(x.name)}</p><p class="libc-l">${esc(x.line)}</p><span class="lib-by">${esc(x.by)}</span></a>`).join('')}</div>
    <div class="sp2"></div><a class="card" href="#/learn" style="text-decoration:none"><p class="k">Our partners</p><p class="h3">The Global Harvest and NeedGod.net</p><p class="p">Training from ministries we work alongside in Australia.</p></a>`, { tab: 'learn' });
});
on(/^\/learn\/partner\/([\w-]+)$/, (m) => {
  const x = AC.partners.find((y) => y.id === m[1]); if (!x) return (location.hash = '#/learn');
  const out = (u) => u + (u.includes('?') ? '&' : '?') + 'utm_source=always-app&utm_medium=referral';
  render(`${top('#/learn')}<div class="ptr-hero ptr-${x.tone}"><span class="ptr-mono lg" aria-hidden="true">${x.mono}</span><p class="ptr-by">Training by</p><h1 class="h1">${esc(x.name)}</h1><p class="p">${esc(x.about)}</p></div>
    <div class="sp2"></div><div class="list">${x.tools.map((t, i) => `<a class="li" href="${out(t.url)}" target="_blank" rel="noopener"><span class="ico ${['', 'peach', 'sand'][i % 3]}">${i + 1}</span><div class="grow"><div class="t">${esc(t.t)}</div><div class="s">${esc(t.s)}</div></div><span class="chev">${ic('ext', 17)}</span></a>`).join('')}</div>
    <div class="sp2"></div><a class="btn" href="${out(x.join.url)}" target="_blank" rel="noopener">${esc(x.join.label)}</a>
    ${x.id === 'tgh' ? `<div class="sp2"></div><a class="card sage" href="#/baptism" style="text-decoration:none;display:block"><p class="k">Baptism</p><p class="h3">Ready to be baptised?</p><p class="p">Ask a local church, ${esc(x.name)}, or both, to help you take that step.</p></a>` : ''}
    <div class="sp2"></div><a class="card" href="#/connect" style="text-decoration:none;display:block"><p class="k">After a conversation</p><p class="h3">Help them find a church</p><p class="p">Partner churches near home, ready to welcome someone who said yes.</p></a>
    <p class="note" style="margin-top:16px">${esc(x.name)}’s training belongs to them. Links open on their site, and nothing about you is sent with them.</p>`, { tab: 'learn' });
});
on(/^\/learn\/story$/, () => {
  const tones = [['var(--sage)', 'var(--ink)'], ['var(--sand)', 'var(--ink)'], ['#1B4740', '#F8F3EA'], ['var(--peach)', '#1E2A26']];
  let i = 0;
  const draw = () => {
    const code = AC.storyLangs[S.settings.storyLang] ? S.settings.storyLang : 'en';
    const L = AC.storyLangs[code], en = AC.story[i];
    const s = L.items ? { title: L.items[i][0], line: L.items[i][1], body: L.items[i][2], ask: L.items[i][3] } : en;
    const [bg, fg] = tones[i];
    render(`${top('#/learn', 'God’s story')}
      <div class="langs" role="group" aria-label="Language">${Object.entries(AC.storyLangs).map(([k, v]) => `<button lang="${k}" data-lang="${k}" aria-pressed="${k === code}">${v.name}</button>`).join('')}</div><div class="sp"></div>
      <div class="story-card fade-in" lang="${code}" dir="${L.dir || 'ltr'}" style="background:${bg};color:${fg}" aria-live="polite"><span class="n">${i + 1}</span><p class="h1" style="color:inherit">${esc(s.title)}</p><p class="big-serif" style="font-size:24px;color:inherit">${esc(s.line)}</p><p style="margin:0;font-size:16px;line-height:1.6;opacity:.88">${esc(s.body)}</p>
        ${code === 'en' ? `<div class="stack-s">${en.refs.map((r) => `<p class="scripture" data-scripture="${r}" style="font-size:17px"></p>`).join('')}</div>` : `<p class="story-refs" dir="ltr">${en.refs.map((r) => r.replace(/^(\w+) (\d+) /, (m, b, c) => `${b} ${c}:`)).join(' · ')}</p>`}
        <p style="margin:auto 0 0;font:700 15px var(--head)">${esc(L.ask || 'Ask: ')}${esc(s.ask)}</p></div>
      <div class="sp2"></div><div class="dots" aria-hidden="true">${AC.story.map((_, j) => `<i class="${j === i ? 'on' : ''}"></i>`).join('')}</div><div class="sp2"></div>
      <div class="row"><button class="btn light" id="sb" ${i === 0 ? 'disabled' : ''}>Back</button>${i < 3 ? '<button class="btn" id="sn">Next</button>' : '<a class="btn peach" href="#/gather/moment">If they say yes</a>'}</div>`);
    $('#sb').onclick = () => { i--; draw(); };
    if ($('#sn')) $('#sn').onclick = () => { i++; draw(); };
    $$('[data-lang]').forEach((b) => (b.onclick = () => { S.settings.storyLang = b.dataset.lang; save(); draw(); }));
    $$('.scripture').forEach((el) => (el.style.color = 'inherit'));
  };
  draw();
});
on(/^\/learn\/road$/, () => {
  render(`${top('#/learn')}<p class="k">Explaining the Gospel</p><h1 class="h1">The Romans Road</h1><p class="p" style="margin-top:6px">Six verses from Romans that walk through the good news of Jesus.</p><div class="sp2"></div>
    <div class="stack">${AC.romansRoad.map((r, i) => `<div class="card"><div class="row"><span class="ico ${i % 2 ? 'peach' : ''}">${i + 1}</span><p class="h3 grow">${esc(r.note)}</p></div><p class="scripture" data-scripture="${r.ref}"></p></div>`).join('')}</div>
    <div class="sp2"></div><a class="btn peach" href="#/gather/moment">If someone says yes</a>`, { tab: 'learn' });
});
on(/^\/learn\/guides$/, () => {
  render(`${top('#/learn')}<h1 class="h1">Conversation guides</h1><p class="p" style="margin-top:6px">Listen first, find common ground, and point gently to Jesus.</p><div class="sp2"></div>
    <div class="list">${AC.guides.map((g, i) => `<a class="li" href="#/learn/guide/${g.id}"><span class="ico ${['', 'peach', 'sand'][i % 3]}">${ic('chat')}</span><div class="grow"><div class="t">${esc(g.title)}</div><div class="s">${esc(g.sub)}</div></div><span class="chev">${ic('right', 18)}</span></a>`).join('')}</div>`, { tab: 'learn' });
});
on(/^\/learn\/guide\/([\w-]+)$/, (m) => {
  const g = AC.guides.find((x) => x.id === m[1]); if (!g) return (location.hash = '#/learn/guides');
  const ul = (xs) => `<ul class="bullets">${xs.map((x) => `<li>${esc(x)}</li>`).join('')}</ul>`;
  render(`${top('#/learn/guides')}<p class="k">Conversation guide</p><h1 class="h1">${esc(g.title)}</h1><div class="sp"></div><p class="p" style="font-size:16px">${esc(g.intro)}</p><div class="sp2"></div>
    <div class="stack">
      <div class="card"><p class="h3">Listen for</p>${ul(g.listen)}</div>
      <div class="card sage"><p class="h3">Common ground</p>${ul(g.common)}</div>
      <div class="card"><p class="h3">Questions to ask</p><div class="stack-s">${g.questions.map((q) => `<p class="serif" style="font-size:19px;margin:0">“${esc(q)}”</p>`).join('')}</div></div>
      <div class="card"><p class="h3">Sharing Jesus</p><div class="stack">${g.share.map((s) => `<div class="stack-s"><p style="margin:0;font-weight:600">${esc(s.p)}</p><p class="scripture" data-scripture="${s.ref}" style="font-size:17px"></p></div>`).join('')}</div></div>
      <div class="card sand"><p class="h3">Be gentle</p>${ul(g.gentle)}</div>
    </div><div class="sp2"></div><a class="btn" href="#/learn/story">Share God’s story</a>`, { tab: 'learn' });
});
on(/^\/learn\/course\/([\w-]+)$/, (m) => {
  const c = AC.courses.find((x) => x.id === m[1]); if (!c) return (location.hash = '#/learn');
  const done = S.courses[c.id] || [];
  render(`${top('#/learn')}<p class="k">Training · ${c.mins} minutes</p><h1 class="h1">${esc(c.title)}</h1><p class="p" style="margin-top:6px">${esc(c.sub)}</p><div class="sp2"></div>
    <div class="list">${c.lessons.map((l, i) => `<a class="li" href="#/learn/lesson/${c.id}/${i}"><span class="ico ${done.includes(i) ? 'green' : ''}">${done.includes(i) ? ic('check', 20) : i + 1}</span><div class="grow"><div class="t">${esc(l.t)}</div><div class="s">Lesson ${i + 1} of ${c.lessons.length}</div></div><span class="chev">${ic('right', 18)}</span></a>`).join('')}</div>`, { tab: 'learn' });
});
on(/^\/learn\/lesson\/([\w-]+)\/(\d+)$/, (m) => {
  const c = AC.courses.find((x) => x.id === m[1]); const i = Number(m[2]); const l = c?.lessons[i]; if (!l) return (location.hash = '#/learn');
  render(`${top('#/learn/course/' + c.id, '', `<span class="note">${i + 1} of ${c.lessons.length}</span>`)}<p class="k">${esc(c.title)}</p><h1 class="h1">${esc(l.t)}</h1><div class="sp2"></div>
    <div class="stack">${l.body.map((p) => `<p style="margin:0;font-size:17px;line-height:1.6">${esc(p)}</p>`).join('')}
    <div class="card sage"><p class="scripture" data-scripture="${l.ref}"></p></div>
    <div class="card"><p class="k">Reflect</p><p class="h3">${esc(l.reflect)}</p></div></div><div class="sp2"></div>
    <button class="btn" id="ldone">${i < c.lessons.length - 1 ? 'Done, next lesson' : 'Finish course'}</button>`, { tab: 'learn' });
  $('#ldone').onclick = () => { const d = (S.courses[c.id] = S.courses[c.id] || []); if (!d.includes(i)) d.push(i); save(); if (i < c.lessons.length - 1) location.hash = `#/learn/lesson/${c.id}/${i + 1}`; else { toast('Course complete. Well done!'); location.hash = '#/learn/course/' + c.id; } };
});
on(/^\/learn\/testimony$/, () => {
  const t = S.testimony;
  render(`${top('#/learn')}<p class="k">Your story</p><h1 class="h1">How Jesus changed your life</h1><p class="p" style="margin-top:6px">Three short parts, about a minute each. Kept on this device.</p><div class="sp2"></div>
    <div class="stack">${[['before', 'Before', 'What was life like? What were you looking for?'], ['meet', 'Meeting Jesus', 'How did you come to trust Him?'], ['since', 'Since', 'What has changed? What does He mean to you now?']].map(([k, l, h]) => `<div class="field"><label for="t-${k}">${l}</label><textarea class="input" id="t-${k}" placeholder="${h}" data-k="${k}">${esc(t[k])}</textarea></div>`).join('')}
    <p class="note" id="t-count"></p><div class="row"><button class="btn" id="t-save">Save</button><button class="btn ghost" id="t-time">${ic('play', 18)}Practise</button></div></div>`, { tab: 'learn' });
  const count = () => { const words = ['before', 'meet', 'since'].map((k) => $('#t-' + k).value.trim().split(/\s+/).filter(Boolean).length).reduce((a, b) => a + b, 0); $('#t-count').textContent = `${words} words, about ${Math.max(1, Math.round(words / 140))} minute${words > 200 ? 's' : ''} to say.`; };
  $$('textarea[data-k]').forEach((x) => x.addEventListener('input', count)); count();
  $('#t-save').onclick = () => { ['before', 'meet', 'since'].forEach((k) => (S.testimony[k] = $('#t-' + k).value)); save(); toast('Your story is saved'); };
  let timer = null;
  $('#t-time').onclick = () => { if (timer) { clearInterval(timer); timer = null; $('#t-time').innerHTML = ic('play', 18) + 'Practise'; return; } let s = 180; $('#t-time').textContent = '3:00'; timer = setInterval(() => { s--; $('#t-time').textContent = `${Math.floor(s / 60)}:${String(s % 60).padStart(2, '0')}`; if (s <= 0) { clearInterval(timer); timer = null; $('#t-time').innerHTML = ic('check', 18) + 'Time'; toast('Three minutes. Great practice!'); } }, 1000); };
  cleanup.push(() => clearInterval(timer));
});
on(/^\/learn\/questions$/, () => {
  render(`${top('#/learn')}<h1 class="h1">Big questions</h1><p class="p" style="margin-top:6px">Short, honest answers to talk through together.</p><div class="sp2"></div>
    <div class="card">${AC.questions.map((q) => `<details class="qa"><summary>${esc(q.q)}<span class="chev">${ic('right', 18)}</span></summary><div class="stack-s" style="padding-bottom:16px"><p style="margin:0">${esc(q.a)}</p>${q.refs.map((r) => `<p class="scripture" data-scripture="${r}" style="font-size:16.5px"></p>`).join('')}</div></details>`).join('')}</div>`, { tab: 'learn' });
});

// ---------------------------------------------------------------- Gather
on(/^\/gather$/, () => {
  render(`<div class="sp"></div><h1 class="h1">Gather</h1><p class="p" style="margin-top:6px">Someone said yes to Jesus. Give them a next step.</p><div class="sp2"></div>
    <div class="gather-hero"><p class="k" style="color:#5A3A22">For a crowd</p><p class="big-serif" style="margin:6px 0 10px">Start a response point</p><p style="margin:0 0 16px;color:#3E2A1C">Show a QR code. People scan it on their own phone and choose a next step.</p><a class="btn" href="#/gather/point">${ic('qr', 20)}Show a QR code</a></div>
    <div class="sp2"></div><div class="list">
      <a class="li" href="#/gather/connect"><span class="ico">${ic('send')}</span><div class="grow"><div class="t">Connect someone now</div><div class="s">One person, on your phone, with their consent</div></div><span class="chev">${ic('right', 18)}</span></a>
      <a class="li" href="#/gather/moment"><span class="ico peach">${ic('flame')}</span><div class="grow"><div class="t">Leading the moment</div><div class="s">What to say and pray when someone says yes</div></div><span class="chev">${ic('right', 18)}</span></a>
      <a class="li" href="#/gather/people"><span class="ico sand">${ic('walk')}</span><div class="grow"><div class="t">People you’ve connected</div><div class="s">${S.connected.length ? `${S.connected.length} so far` : 'None yet'}</div></div><span class="chev">${ic('right', 18)}</span></a>
      <a class="li" href="#/walk/notes"><span class="ico">${ic('note')}</span><div class="grow"><div class="t">Field notes</div><div class="s">A quick note after a conversation</div></div><span class="chev">${ic('right', 18)}</span></a>
    </div><div class="sp2"></div>
    <div class="card sage"><div class="row"><span class="ico green">${ic('lock')}</span><p class="p grow" style="color:var(--ink)">Details go only to the Always Foundation in Sydney, with the person’s consent, so a church nearby can welcome them. Never sold.</p></div></div>`, { tab: 'gather' });
});
on(/^\/gather\/point$/, () => {
  render(`${top('#/gather', 'New response point')}<p class="p">Give it a name so you can remember it, like “Friday street team” or “Youth camp”. The name stays on your phone.</p><div class="sp2"></div>
    <div class="field"><label for="pt-n">Name</label><input class="input" id="pt-n" maxlength="60" placeholder="e.g. Town Hall street team"></div><div class="sp2"></div>
    <div class="field"><span class="label">What will people see first?</span><div class="stack-s">
      <label class="opt"><input type="radio" name="pt-k" value="yes" checked><span>I said yes to Jesus<small>For altar calls and the moment someone responds</small></span></label>
      <label class="opt"><input type="radio" name="pt-k" value="step"><span>Take a next step<small>For events, tours and street outreach</small></span></label></div></div>
    <div class="sp2"></div><button class="btn peach" id="pt-go">${ic('qr', 20)}Show QR code</button>
    ${S.points.length ? `<div class="sp2"></div><p class="k">Your response points</p><div class="sp"></div><div class="list">${S.points.slice(0, 8).map((p) => `<a class="li" href="#/gather/live/${p.id}"><span class="ico peach">${ic('qr')}</span><div class="grow"><div class="t">${esc(p.name)}</div><div class="s">${fmtDate(p.at)}</div></div><span class="chev">${ic('right', 18)}</span></a>`).join('')}</div>` : ''}`);
  $('#pt-go').onclick = () => { const p = { id: uid(), name: $('#pt-n').value.trim() || 'Response point', kind: $('input[name=pt-k]:checked').value, at: Date.now() }; S.points.unshift(p); S.points = S.points.slice(0, 30); save(); location.hash = '#/gather/live/' + p.id; };
});
function qrSvg(text) {
  const q = window.qrcode(0, 'M'); q.addData(text); q.make();
  const n = q.getModuleCount(), m = 4, size = n + m * 2; let d = '';
  for (let r = 0; r < n; r++) for (let c = 0; c < n; c++) if (q.isDark(r, c)) d += `M${c + m} ${r + m}h1v1h-1z`;
  return `<svg viewBox="0 0 ${size} ${size}" role="img" aria-label="QR code"><rect width="${size}" height="${size}" fill="#fff"/><path d="${d}" fill="#14352F"/></svg>`;
}
on(/^\/gather\/live\/([\w-]+)$/, (m) => {
  const p = S.points.find((x) => x.id === m[1]); if (!p) return (location.hash = '#/gather/point');
  const url = `${location.origin}/#/respond/${p.kind}`;
  render(`<div class="top"><button class="back" data-back="#/gather" style="color:#E8A577">${ic('left', 18)}Done</button><span class="h3" style="color:#F8F3EA">${esc(p.name)}</span><span style="width:44px"></span></div>
    <div style="text-align:center" class="stack"><p class="big-serif" style="color:#F8F3EA">${p.kind === 'yes' ? 'Said yes to Jesus?' : 'Take a next step'}</p><p class="p" style="color:#B9D0C6">Scan with your phone camera.</p>
    <div class="qr-wrap">${qrSvg(url)}</div><p class="note" style="color:#8FB0A3;word-break:break-all">${esc(url.replace('https://', ''))}</p>
    <div class="row"><button class="btn peach" id="lv-share">${ic('share', 18)}Share link</button><a class="btn light" href="#/gather/connect">${ic('send', 18)}Connect one</a></div></div>`, { cls: 'live' });
  document.body.style.background = '#14352F';
  cleanup.push(() => (document.body.style.background = ''));
  let lock = null; try { navigator.wakeLock?.request('screen').then((l) => (lock = l)).catch(() => {}); } catch {}
  cleanup.push(() => lock?.release?.());
  $('#lv-share').onclick = async () => { if (navigator.share) { try { await navigator.share({ title: 'Take a next step', url }); } catch {} } else { try { await navigator.clipboard.writeText(url); toast('Link copied'); } catch {} } };
});
on(/^\/gather\/moment$/, () => {
  render(`${top('#/gather')}<p class="k">When someone says yes</p><h1 class="h1">Leading the moment</h1><div class="sp2"></div>
    <div class="moment">${AC.moment.map((s, i) => `<div class="card${i === 2 ? ' sage' : ''}"><div class="row"><span class="ico ${i === 2 ? 'green' : 'peach'}">${i + 1}</span><p class="h3 grow">${esc(s.t)}</p></div><p class="p">${esc(s.d)}</p>${s.prayer ? `<p class="serif" style="font-size:19px;line-height:1.5;margin:6px 0 0">${esc(s.prayer)}</p>` : ''}</div>`).join('')}</div>
    <div class="sp2"></div><a class="btn peach" href="#/gather/connect">${ic('send', 20)}Connect them now</a><div class="sp"></div><a class="btn light" href="#/learn/story">God’s story in four moments</a>`, { tab: 'gather' });
});
on(/^\/gather\/people$/, () => {
  render(`${top('#/gather', 'People you’ve connected')}${S.connected.length ? `<div class="list">${S.connected.map((c) => `<div class="li"><span class="avatar">${esc((c.name || '•')[0])}</span><div class="grow"><div class="t">${esc(c.name || 'A family')}</div><div class="s">${esc(STEP_LABEL[c.step] || '')} · ${fmtDate(c.at)}</div></div><a class="btn small light" href="#/walk/new?name=${encodeURIComponent(c.name || '')}">Walk</a></div>`).join('')}</div><p class="note" style="margin-top:12px">Only first names are kept here, on your phone. Their details went securely to the Always Foundation.</p>` :
    '<div class="empty"><p class="h3">No one yet</p><p class="p">When you connect someone, they’ll appear here so you can keep praying and walking with them.</p></div>'}`, { tab: 'gather' });
});

// ---------------------------------------------------------------- Respond flow (shared by Connect someone now and the public QR page)
const STEP_LABEL = { church: 'Find a church', youth: 'Youth group', talk: 'Talk with someone', explore: 'Explore faith', baptism: 'Baptism' };
const BAPTISM_WORDING = 'always-app-baptism-2026-11-v1';
function respondFlow({ mode, kind }) {
  const assist = mode === 'assist';
  const f = {};
  const back = assist ? '#/gather' : null;
  const mobileOk = (v) => /^(\+?61|0)4\d{8}$/.test(String(v).replace(/[\s()-]/g, ''));
  const bar = (n) => `<div class="step-bar" aria-hidden="true"><i style="width:${n * 25}%"></i></div><p class="note" style="margin-top:8px">Step ${n} of 4</p>`;
  const shell = (body, bk) => render(`${bk ? top(bk) : `<div class="row between" style="padding-top:10px"><div class="logo">${LOGO}</div><span class="pill">Always Foundation</span></div>`}${body}`, { tab: assist ? 'gather' : null, cls: assist ? '' : 'respond' });
  const intro = () => {
    if (assist) return age();
    shell(`<div class="sp2"></div><div class="stack">
      <p class="k">${kind === 'baptism' ? 'Baptism' : kind === 'yes' ? 'Welcome to the family' : 'Hello'}</p>
      <h1 class="big-serif" style="font-size:36px">${kind === 'baptism' ? 'Ready to be baptised?' : kind === 'yes' ? 'You said yes to Jesus. You won’t walk alone.' : 'Take a next step with Jesus.'}</h1>
      <p class="p" style="font-size:16.5px">${kind === 'baptism' ? 'Baptism is a joyful step of following Jesus. Tell us a little about you, and choose who you’d like to help you take it.' : kind === 'yes' ? 'This is the best decision anyone can make. We’d love to help you find a church nearby to welcome you and walk with you.' : 'Whether you’re curious, have questions, or are ready to find a church, we’d love to help.'}</p>
      <div class="card sage"><p class="scripture" data-scripture="${kind === 'baptism' ? 'ACT 2 38' : kind === 'yes' ? '2CO 5 17' : 'MAT 11 28'}"></p></div>
      <button class="btn peach" id="r-go">Get started</button><p class="note" style="text-align:center">About a minute. Your details are kept in Australia and never sold.</p></div>`);
    $('#r-go').onclick = age;
  };
  const age = () => {
    shell(`${bar(1)}<div class="sp2"></div><h1 class="h1" id="age-h">${assist ? 'How old are they?' : 'How old are you?'}</h1><p class="p" style="margin-top:6px">This helps us connect ${assist ? 'them' : 'you'} safely.</p><div class="sp2"></div>
      <div class="stack-s" role="radiogroup" aria-labelledby="age-h">
        <label class="opt"><input type="radio" name="age" value="18+"><span>18 or over</span></label>
        <label class="opt"><input type="radio" name="age" value="15-17"><span>15 to 17</span></label>
        <label class="opt"><input type="radio" name="age" value="13-14"><span>13 to 14<small>We’ll also ask a parent or guardian to say yes.</small></span></label>
        <label class="opt"><input type="radio" name="age" value="under13"><span>Under 13<small>A parent or guardian fills this in.</small></span></label></div>
      <div class="sp2"></div><button class="btn" id="a-next" disabled>Next</button>`, back);
    $$('input[name=age]').forEach((i) => (i.onchange = () => ($('#a-next').disabled = false)));
    if (f.ageBand) { const r = $(`input[name=age][value="${f.ageBand}"]`); if (r) { r.checked = true; $('#a-next').disabled = false; } }
    $('#a-next').onclick = () => { f.ageBand = $('input[name=age]:checked').value; if (kind === 'baptism') { f.step = 'baptism'; details(); } else step(); };
  };
  const step = () => {
    const adult = f.ageBand === '18+';
    const opts = (adult ? ['church', 'talk', 'explore'] : ['youth', 'talk']).map((k) => `<label class="opt"><input type="radio" name="step" value="${k}"><span>${{ church: 'Find a church near me', youth: 'Join a youth group', talk: 'Talk with someone', explore: 'Explore faith' }[k]}<small>${{ church: 'A church nearby that will welcome you.', youth: 'A safe, checked youth group nearby.', talk: 'About Jesus, life or prayer.', explore: 'Relaxed conversations about life, faith and meaning.' }[k]}</small></span></label>`).join('');
    shell(`${bar(2)}<div class="sp2"></div><h1 class="h1" id="step-h">What would help next?</h1><div class="sp2"></div><div class="stack-s" role="radiogroup" aria-labelledby="step-h">${opts}</div><div class="sp2"></div><div class="row"><button class="btn light" id="s-back">Back</button><button class="btn" id="s-next" disabled>Next</button></div>`, back);
    $$('input[name=step]').forEach((i) => (i.onchange = () => ($('#s-next').disabled = false)));
    $('#s-back').onclick = age;
    $('#s-next').onclick = () => { f.step = $('input[name=step]:checked').value; details(); };
  };
  const details = () => {
    const u13 = f.ageBand === 'under13', u15 = f.ageBand === '13-14';
    shell(`${bar(3)}<div class="sp2"></div><h1 class="h1">${u13 ? 'How can we reach the family?' : assist ? 'How can we reach them?' : 'How can we reach you?'}</h1><p class="p" style="margin-top:6px">${u13 ? 'We’ll only contact the parent or guardian.' : 'Just the basics, so someone can get in touch.'}</p><div class="sp2"></div>
      <form id="d-form" class="stack" novalidate>
        ${u13 ? '' : `<div class="field"><label for="d-name">First name</label><input class="input" id="d-name" autocomplete="${assist ? 'off' : 'given-name'}" autocapitalize="words" maxlength="60"></div>`}
        <div class="field"><label for="d-mobile">${u13 ? 'Parent or guardian’s mobile' : 'Mobile'}</label><input class="input" id="d-mobile" type="tel" inputmode="tel" autocomplete="${assist ? 'off' : 'tel'}" maxlength="20" placeholder="0400 000 000"></div>
        ${u15 ? '<div class="field"><label for="d-parent">Parent or guardian’s mobile</label><input class="input" id="d-parent" type="tel" inputmode="tel" maxlength="20" placeholder="0400 000 000"></div>' : ''}
        <div class="row" style="align-items:flex-start"><div class="field" style="width:120px"><label for="d-pc">Postcode</label><input class="input" id="d-pc" inputmode="numeric" maxlength="4" placeholder="2000"></div><div class="field grow"><label for="d-sub">Suburb</label><input class="input" id="d-sub" autocapitalize="words" maxlength="60"></div></div>
        <div aria-hidden="true" style="position:absolute;left:-9999px;height:0;overflow:hidden"><label>Website<input id="d-hp" tabindex="-1" autocomplete="off"></label></div>
        <p class="err" id="d-err" role="alert"></p><div class="row"><button class="btn light" type="button" id="d-back">Back</button><button class="btn" type="submit">Next</button></div></form>`, back);
    $('#d-back').onclick = kind === 'baptism' ? age : step;
    $('#d-form').onsubmit = (e) => {
      e.preventDefault();
      const v = (id) => ($('#' + id)?.value || '').trim();
      let err = '';
      if (!u13 && !v('d-name')) err = 'Please add a first name.';
      else if (!mobileOk(v('d-mobile'))) err = 'Please check the mobile number.';
      else if (u15 && !mobileOk(v('d-parent'))) err = 'Please add a parent or guardian’s mobile.';
      else if (!/^\d{4}$/.test(v('d-pc'))) err = 'Please add a 4-digit postcode.';
      else if (v('d-sub').length < 2) err = 'Please add a suburb.';
      $('#d-err').textContent = err; if (err) return;
      Object.assign(f, { firstName: u13 ? '' : v('d-name'), mobile: v('d-mobile'), parentMobile: u15 ? v('d-parent') : '', postcode: v('d-pc'), suburb: v('d-sub'), hp: v('d-hp') });
      consent();
    };
  };
  const consent = () => {
    if (kind === 'baptism') return consentBaptism();
    const u13 = f.ageBand === 'under13';
    shell(`${bar(4)}<div class="sp2"></div>${assist ? `<div class="card peach"><p class="h3">Hand your phone to ${esc(f.firstName || 'them')}</p><p style="margin:0">This choice is theirs to make.</p></div><div class="sp2"></div>` : ''}<h1 class="h1">Your yes, your choice</h1><div class="sp2"></div>
      <div class="stack-s"><div class="check"><input type="checkbox" id="c-connect"><label for="c-connect"><b>Connect me.</b> I’m happy for the Always Foundation to keep my first name, mobile and suburb, so they can get in touch and help me find a church or ministry near me.</label></div>
      <div class="check"><input type="checkbox" id="c-nearby" checked><label for="c-nearby"><b>Try the next one nearby</b> if the first church can’t welcome me.</label></div>
      ${u13 ? '<div class="check"><input type="checkbox" id="c-assent"><label for="c-assent"><b>My child agrees too.</b> I’ve talked with my child and they’re happy to be connected with a youth group.</label></div>' : ''}</div>
      <p class="note" style="margin-top:12px">Details are kept in Australia and never sold. We delete them after 90 days. To change your mind any time, email hello@alwaysfoundation.org and we’ll delete them straight away.</p>
      <p class="err" id="c-err" role="alert"></p><div class="row"><button class="btn light" id="c-back">Back</button><button class="btn peach" id="c-send" disabled>Send</button></div>`, back);
    const upd = () => ($('#c-send').disabled = !$('#c-connect').checked || (u13 && !$('#c-assent').checked));
    ['c-connect', 'c-assent'].forEach((id) => $('#' + id)?.addEventListener('change', upd));
    $('#c-back').onclick = details;
    $('#c-send').onclick = async () => {
      $('#c-send').disabled = true; $('#c-send').textContent = 'Sending…';
      const body = { source: SOURCE, firstName: f.firstName, mobile: f.mobile, parentMobile: f.parentMobile, suburb: f.suburb, postcode: f.postcode, ageBand: f.ageBand, step: f.step, website: f.hp,
        consent: { shareWith: [], connect: $('#c-connect').checked, allowNextNearby: $('#c-nearby').checked, notifySender: false, wordingVersion: WORDING, party: u13 ? 'parent' : 'self', childAssent: u13 ? !!$('#c-assent')?.checked : false } };
      try {
        const r = await fetch(SAVE_URL, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body), signal: AbortSignal.timeout(15000) });
        if (!r.ok) throw new Error('http_' + r.status);
        if (assist) { S.connected.unshift({ name: f.firstName, step: f.step, at: Date.now() }); S.connected = S.connected.slice(0, 200); save(); }
        done();
      } catch { $('#c-err').textContent = 'That didn’t send. Please check the connection and try again.'; $('#c-send').disabled = false; $('#c-send').textContent = 'Send'; }
    };
  };
  const consentBaptism = () => {
    const u13 = f.ageBand === 'under13', adult = f.ageBand === '18+';
    const partner = AC.partners.find((x) => x.id === 'tgh');
    shell(`${bar(4)}<div class="sp2"></div><h1 class="h1">Who should help you take this step?</h1><p class="p" style="margin-top:6px">${adult ? 'Choose one or both. Each only hears from you if you tick it.' : 'A safe local church or youth group near you will help, with your parent or guardian.'}</p><div class="sp2"></div>
      <div class="stack-s">
        <div class="check"><input type="checkbox" id="b-church"><label for="b-church"><b>A local church near me.</b> Share my first name, mobile and suburb with one partner church nearby, so they can talk with me about baptism.</label></div>
        ${adult ? `<div class="check"><input type="checkbox" id="b-tgh"><label for="b-tgh"><b>${esc(partner.name)}.</b> Share my first name, mobile and suburb with ${esc(partner.name)}, so their team can talk with me about baptism.</label></div>` : ''}
        <div class="check" id="b-near-w" style="display:none"><input type="checkbox" id="b-near" checked><label for="b-near"><b>Try the next church nearby</b> if the first can’t help.</label></div>
        ${u13 ? '<div class="check"><input type="checkbox" id="c-assent"><label for="c-assent"><b>My child agrees too.</b> I’ve talked with my child and they’d like to talk with a church about baptism.</label></div>' : ''}</div>
      <p class="note" style="margin-top:12px">Your faith is personal, so nothing is shared without your tick. Details are kept in Australia, never sold, and deleted after 90 days. To change your mind, email hello@alwaysfoundation.org.</p>
      <p class="err" id="c-err" role="alert"></p><div class="row"><button class="btn light" id="c-back">Back</button><button class="btn peach" id="c-send" disabled>Send</button></div>`, back);
    const upd = () => {
      const ch = $('#b-church').checked, tg = !!$('#b-tgh')?.checked;
      $('#b-near-w').style.display = ch ? '' : 'none';
      $('#c-send').disabled = !(ch || tg) || (u13 && !$('#c-assent').checked);
    };
    ['b-church', 'b-tgh', 'c-assent'].forEach((id) => $('#' + id)?.addEventListener('change', upd));
    $('#c-back').onclick = details;
    $('#c-send').onclick = async () => {
      $('#c-send').disabled = true; $('#c-send').textContent = 'Sending…';
      const ch = $('#b-church').checked, tg = adult && !!$('#b-tgh')?.checked;
      f.toChurch = ch; f.toPartner = tg;
      const body = { source: SOURCE, firstName: f.firstName, mobile: f.mobile, parentMobile: f.parentMobile, suburb: f.suburb, postcode: f.postcode, ageBand: f.ageBand, step: 'baptism', website: f.hp,
        consent: { shareWith: tg ? ['tgh'] : [], connect: ch, allowNextNearby: ch && $('#b-near').checked, notifySender: false, wordingVersion: BAPTISM_WORDING, party: u13 ? 'parent' : 'self', childAssent: u13 ? !!$('#c-assent')?.checked : false } };
      try {
        const r = await fetch(SAVE_URL, { method: 'POST', headers: { 'content-type': 'application/json' }, body: JSON.stringify(body), signal: AbortSignal.timeout(15000) });
        if (!r.ok) throw new Error('http_' + r.status);
        if (assist) { S.connected.unshift({ name: f.firstName, step: 'baptism', at: Date.now() }); S.connected = S.connected.slice(0, 200); save(); }
        done();
      } catch { $('#c-err').textContent = 'That didn’t send. Please check the connection and try again.'; $('#c-send').disabled = false; $('#c-send').textContent = 'Send'; }
    };
  };
  const done = () => {
    const parent = f.ageBand === '13-14';
    shell(`<div class="sp2"></div><div class="stack" style="text-align:center"><span class="ico green" style="width:72px;height:72px;border-radius:50%;margin:0 auto">${ic('check', 34)}</span>
      <h1 class="big-serif" style="font-size:34px">${assist ? `${esc(f.firstName || 'They')}${f.firstName ? '’s' : '’re'} connected` : `You won’t walk alone${f.firstName ? ', ' + esc(f.firstName) : ''}.`}</h1>
      <p class="p" style="font-size:16px">${parent ? 'We’ll ask a parent or guardian to say yes first, then a safe youth group nearby will be in touch.' : kind === 'baptism' ? `${f.toChurch && f.toPartner ? 'A church near you and The Global Harvest will' : f.toPartner ? 'The Global Harvest team will' : 'A church near you will'} be in touch to talk about baptism. What a joy.` : 'Someone from a church or ministry nearby, or our care team, will be in touch soon.'}</p>
      ${assist ? `<a class="btn" href="#/walk/new?name=${encodeURIComponent(f.firstName || '')}">${ic('walk', 20)}Keep walking with them</a><a class="btn light" href="#/gather">Back to Gather</a>` :
        `<div class="card sage" style="text-align:left"><p class="k">Start reading</p><p class="h3">The Gospel of John</p><p class="p">Meet Jesus, a chapter a day.</p><a class="btn small" href="#/plan/john21" style="margin-top:6px">Start reading</a></div><p class="note">Want the Always App for yourself? <a href="#/">Open it here</a>.</p>`}</div>`, assist ? '#/gather' : null);
  };
  intro();
}
on(/^\/gather\/connect$/, () => respondFlow({ mode: 'assist' }));
on(/^\/respond\/(yes|step|baptism)$/, (m) => respondFlow({ mode: 'self', kind: m[1] }));
on(/^\/baptism$/, () => respondFlow({ mode: 'self', kind: 'baptism' }));
on(/^\/respond$/, () => respondFlow({ mode: 'self', kind: 'step' }));


// Walk rhythm: each step is suggested a set number of days after you start walking with someone.
const DAY = 864e5;
const stepDue = (p, i) => (p.since || Date.now()) + (AC.walkDays[i] || 0) * DAY;
function dueToday() { const end = new Date(); end.setHours(23, 59, 59, 999); const out = []; S.people.forEach((p) => AC.walkSteps.forEach((st, i) => { if (!p.steps?.[i] && stepDue(p, i) <= end.getTime()) out.push({ p, i, st }); })); return out; }
function walkIcs(p) {
  const pad = (n) => String(n).padStart(2, '0'), d = (t) => { const x = new Date(t); return `${x.getFullYear()}${pad(x.getMonth() + 1)}${pad(x.getDate())}`; };
  const ev = AC.walkSteps.map((st, i) => p.steps?.[i] ? '' : ['BEGIN:VEVENT', `UID:${p.id}-${i}@app.alwaysfoundation.org`, `DTSTAMP:${d(Date.now())}T000000Z`, `DTSTART;VALUE=DATE:${d(Math.max(stepDue(p, i), Date.now()))}`, `SUMMARY:${st} (${p.name})`, 'DESCRIPTION:From the Always App', 'BEGIN:VALARM', 'TRIGGER:PT9H', 'ACTION:DISPLAY', `DESCRIPTION:${st}`, 'END:VALARM', 'END:VEVENT'].join('\r\n')).filter(Boolean);
  return ['BEGIN:VCALENDAR', 'VERSION:2.0', 'PRODID:-//Always Foundation//Always App//EN', ...ev, 'END:VCALENDAR'].join('\r\n');
}
// ---------------------------------------------------------------- Walk
on(/^\/walk$/, () => {
  const people = S.people;
  render(`<div class="sp"></div><h1 class="h1">Walk</h1><p class="p" style="margin-top:6px">Pray for people by name and walk with them, one step at a time.</p><div class="sp2"></div>
    <div class="row between"><p class="h2">Walking with</p><a class="btn small light" href="#/walk/new">${ic('plus', 18)}Add</a></div><div class="sp"></div>
    ${people.length ? `<div class="list">${people.map((p) => { const n = Object.values(p.steps || {}).filter(Boolean).length; return `<a class="li" href="#/walk/p/${p.id}"><span class="avatar">${esc(p.name[0] || '?')}</span><div class="grow"><div class="t">${esc(p.name)}</div><div class="s">${n} of ${AC.walkSteps.length} steps · since ${fmtDate(p.since)}</div></div><span class="chev">${ic('right', 18)}</span></a>`; }).join('')}</div>` :
      '<div class="empty"><p class="h3">No one yet</p><p class="p">Add someone you’re praying for or walking with.</p></div>'}
    <div class="sp2"></div><div class="quick">
      <a class="card" href="#/walk/pray"><span class="ico peach">${ic('heart')}</span><div><p class="h3">Prayer list</p><p class="note">${S.prayer.filter((p) => !p.answered).length} people</p></div></a>
      <a class="card" href="#/walk/notes"><span class="ico">${ic('note')}</span><div><p class="h3">Field notes</p><p class="note">${S.fieldNotes.length} notes</p></div></a>
    </div><div class="sp2"></div><p class="note" style="text-align:center">${ic('lock', 14)} Everything in Walk stays on this phone.</p>`, { tab: 'walk' });
});
on(/^\/walk\/new$/, (m, q) => {
  render(`${top('#/walk', 'Walk with someone')}<div class="field"><label for="wn">First name</label><input class="input" id="wn" maxlength="40" value="${esc(q.get('name') || '')}" autocomplete="off"></div><div class="sp"></div><p class="note">Kept only on this phone.</p><div class="sp2"></div>
    <label class="check"><input type="checkbox" id="wp" checked><span>Add them to my prayer list too</span></label><div class="sp2"></div><button class="btn" id="wgo">Start walking</button>`, { tab: 'walk' });
  $('#wn').focus();
  $('#wgo').onclick = () => { const name = $('#wn').value.trim(); if (!name) return toast('Please add a first name'); const p = { id: uid(), name, since: Date.now(), steps: {}, log: [] }; S.people.unshift(p); if ($('#wp').checked && !S.prayer.some((x) => x.name === name)) S.prayer.unshift({ id: uid(), name, note: '', at: Date.now() }); save(); location.hash = '#/walk/p/' + p.id; };
});
on(/^\/walk\/p\/([\w-]+)$/, (m) => {
  const p = S.people.find((x) => x.id === m[1]); if (!p) return (location.hash = '#/walk');
  const n = Object.values(p.steps).filter(Boolean).length;
  render(`${top('#/walk', '', `<button class="icon-btn" id="pdel" aria-label="Remove ${esc(p.name)}">${ic('trash', 20)}</button>`)}
    <div class="row"><span class="avatar" style="width:60px;height:60px;font-size:24px">${esc(p.name[0])}</span><div><p class="k">Walking with</p><h1 class="h1">${esc(p.name)}</h1></div></div><div class="sp2"></div>
    <div class="progress"><i style="width:${(n / AC.walkSteps.length) * 100}%"></i></div><p class="note" style="margin-top:6px">${n} of ${AC.walkSteps.length} steps</p><div class="sp"></div>
    <div class="list" id="steps">${AC.walkSteps.map((s, i) => `<button class="tick${p.steps[i] ? ' done' : ''}" data-i="${i}" aria-pressed="${!!p.steps[i]}"><i>${ic('check', 16, 3)}</i><span>${esc(s)}</span>${p.steps[i] ? '' : `<em class="due${stepDue(p, i) <= Date.now() ? ' now' : ''}">${stepDue(p, i) <= Date.now() ? 'Today' : fmtDate(stepDue(p, i))}</em>`}</button>`).join('')}</div>
    <div class="sp"></div><button class="btn light small" id="pics">${ic('cal', 18)}Add reminders to my calendar</button>
    ${n === AC.walkSteps.length ? `<div class="sp2"></div><div class="card green"><p class="k">Milestone</p><p class="big-serif" style="color:#F8F3EA;font-size:24px">${esc(p.name)} is walking with a church family.</p><p class="p">Thank God for this. Keep praying and checking in.</p></div>` : ''}
    <div class="sp2"></div><p class="h2">Send a message</p><div class="sp"></div><div class="list">${AC.messages.map((x, i) => `<button class="li" data-msg="${i}"><span class="ico ${i % 2 ? 'peach' : ''}">${ic('chat')}</span><div class="grow"><div class="t">${esc(x.t)}</div><div class="s">${esc(x.m.replace('{name}', p.name)).slice(0, 70)}…</div></div></button>`).join('')}</div>
    <div class="sp2"></div><p class="h2">Notes</p><div class="sp"></div><div class="row"><input class="input grow" id="plog" placeholder="A quick note" maxlength="300"><button class="btn small" id="padd">Add</button></div>
    <div class="sp"></div>${p.log.length ? `<div class="list">${p.log.map((l) => `<div class="li"><div class="grow"><div class="s">${fmtDate(l.at)}</div><div style="font-size:15px">${esc(l.t)}</div></div></div>`).join('')}</div>` : ''}`, { tab: 'walk' });
  $$('#steps .tick').forEach((b) => (b.onclick = () => { const i = b.dataset.i; p.steps[i] = !p.steps[i]; save(); route(); }));
  $('#pics').onclick = () => { const blob = new Blob([walkIcs(p)], { type: 'text/calendar' }); const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = `walking-with-${p.name.replace(/[^\w]+/g, '-').toLowerCase()}.ics`; a.click(); setTimeout(() => URL.revokeObjectURL(a.href), 4000); toast('Open the file to add the reminders'); };
  $$('[data-msg]').forEach((b) => (b.onclick = async () => { const text = AC.messages[b.dataset.msg].m.replace('{name}', p.name); if (navigator.share) { try { await navigator.share({ text }); return; } catch {} } try { await navigator.clipboard.writeText(text); toast('Message copied. Paste it in your messages app.'); } catch {} }));
  $('#padd').onclick = () => { const t = $('#plog').value.trim(); if (!t) return; p.log.unshift({ t, at: Date.now() }); save(); route(); };
  $('#pdel').onclick = () => { if (confirmBox(`Remove ${p.name} from Walk? This deletes your notes about them.`)) { S.people = S.people.filter((x) => x.id !== p.id); save(); location.hash = '#/walk'; } };
});
on(/^\/walk\/pray$/, () => {
  const open = S.prayer.filter((p) => !p.answered), done = S.prayer.filter((p) => p.answered);
  render(`${top('#/walk', 'Prayer list')}<form id="pf" class="row"><input class="input grow" id="pn" placeholder="Add a name" maxlength="40" aria-label="Name to pray for"><button class="btn small" type="submit">${ic('plus', 18)}</button></form><div class="sp2"></div>
    ${open.length ? `<a class="btn peach" href="#/walk/praynow">${ic('heart', 20)}Pray now</a><div class="sp2"></div><div class="list">${open.map((p) => `<div class="li"><span class="avatar">${esc(p.name[0])}</span><div class="grow"><div class="t">${esc(p.name)}</div>${p.note ? `<div class="s">${esc(p.note)}</div>` : ''}</div><button class="btn small light" data-ans="${p.id}" aria-label="Mark prayer for ${esc(p.name)} answered">Answered</button></div>`).join('')}</div>` :
      '<div class="empty"><p class="h3">Who are you praying for?</p><p class="p">Add friends, family and people you’ve met. Pray for them by name.</p></div>'}
    ${done.length ? `<div class="sp2"></div><p class="k">Answered prayers</p><div class="sp"></div><div class="list">${done.map((p) => `<div class="li"><span class="ico green">${ic('check', 18)}</span><div class="grow"><div class="t">${esc(p.name)}</div><div class="s">${fmtDate(p.answered)}</div></div><button class="icon-btn" data-del="${p.id}" aria-label="Remove">${ic('x', 18)}</button></div>`).join('')}</div>` : ''}`, { tab: 'walk' });
  $('#pf').onsubmit = (e) => { e.preventDefault(); const n = $('#pn').value.trim(); if (!n) return; S.prayer.unshift({ id: uid(), name: n, note: '', at: Date.now() }); save(); route(); };
  $$('[data-ans]').forEach((b) => (b.onclick = () => { const p = S.prayer.find((x) => x.id === b.dataset.ans); p.answered = Date.now(); save(); toast('Praise God!'); route(); }));
  $$('[data-del]').forEach((b) => (b.onclick = () => { S.prayer = S.prayer.filter((x) => x.id !== b.dataset.del); save(); route(); }));
});
on(/^\/walk\/praynow$/, () => {
  const names = S.prayer.filter((p) => !p.answered).map((p) => p.name);
  const steps = [AC.prayerPrompts[0], ...names.map((n) => `Pray for ${n}.`), ...AC.prayerPrompts.slice(2)];
  let i = 0;
  const draw = () => {
    render(`${top('#/walk/pray', 'Pray now')}<div class="story-card" style="background:var(--deep);color:#F8F3EA;justify-content:center;text-align:center;min-height:440px"><p class="k" style="color:#E8A577">${i + 1} of ${steps.length}</p><p class="big-serif" style="color:#F8F3EA;font-size:32px">${esc(steps[i])}</p></div><div class="sp2"></div>
      <div class="row"><button class="btn light" id="pb" ${i === 0 ? 'disabled' : ''}>Back</button>${i < steps.length - 1 ? '<button class="btn" id="pn2">Next</button>' : '<a class="btn peach" href="#/walk/pray">Amen</a>'}</div>`, { tab: 'walk' });
    $('#pb').onclick = () => { i--; draw(); };
    if ($('#pn2')) $('#pn2').onclick = () => { i++; draw(); };
  };
  draw();
});
on(/^\/walk\/notes$/, () => {
  render(`${top('#/walk', 'Field notes')}<div class="card"><div class="field"><label for="fn">After a conversation</label><textarea class="input" id="fn" placeholder="Who did you meet? What did you talk about? What will you pray?" maxlength="2000"></textarea></div><div class="field"><label for="fp">Where <span class="note">(optional)</span></label><input class="input" id="fp" maxlength="60" placeholder="e.g. Town Hall steps"></div><button class="btn" id="fs">Save note</button></div>
    <div class="sp2"></div>${S.fieldNotes.length ? `<div class="list">${S.fieldNotes.map((n) => `<div class="li" style="align-items:flex-start"><div class="grow"><div class="s">${fmtDate(n.at)}${n.place ? ' · ' + esc(n.place) : ''}</div><div style="font-size:15px;white-space:pre-wrap">${esc(n.text)}</div></div><button class="icon-btn" data-del="${n.id}" aria-label="Delete note">${ic('trash', 18)}</button></div>`).join('')}</div>` : '<div class="empty"><p class="h3">No notes yet</p><p class="p">Notes stay on this phone. Avoid surnames and contact details.</p></div>'}`, { tab: 'walk' });
  $('#fs').onclick = () => { const t = $('#fn').value.trim(); if (!t) return; S.fieldNotes.unshift({ id: uid(), text: t, place: $('#fp').value.trim(), at: Date.now() }); save(); route(); };
  $$('[data-del]').forEach((b) => (b.onclick = () => { S.fieldNotes = S.fieldNotes.filter((x) => x.id !== b.dataset.del); save(); route(); }));
});

// ---------------------------------------------------------------- Connect
on(/^\/connect$/, () => {
  render(`${top('#/', 'Find a church')}<div class="hero-card"><p class="k" style="color:#E8A577">A next step near home</p><p class="big-serif" style="color:#F8F3EA;margin:8px 0">Looking for a church?</p><p class="p">Tell us your suburb and what would help. A church or ministry nearby will be in touch, or our care team will.</p><div class="sp"></div><a class="btn peach" href="#/respond">Help me find a church</a></div>
    <div class="sp2"></div><div class="card"><p class="h3">The church finder is coming</p><p class="p">Soon you’ll be able to see partner churches near any postcode right here, through Always Connect.</p></div>
    <div class="sp2"></div><div class="list">
      <a class="li" href="https://alwaysfoundation.org/#/join/church" target="_blank" rel="noopener"><span class="ico">${ic('church')}</span><div class="grow"><div class="t">Are you a church?</div><div class="s">Join Always, free for churches</div></div><span class="chev">${ic('right', 18)}</span></a>
      <a class="li" href="https://alwaysfoundation.org" target="_blank" rel="noopener"><span class="ico peach">${ic('globe')}</span><div class="grow"><div class="t">About the Always Foundation</div><div class="s">Together for the Gospel</div></div><span class="chev">${ic('right', 18)}</span></a>
    </div>`, { tab: 'home' });
});

// ---------------------------------------------------------------- Me
on(/^\/me$/, () => {
  render(`${top('#/', 'Me')}<div class="card"><div class="field"><label for="mn">Your first name</label><input class="input" id="mn" value="${esc(S.settings.name)}" maxlength="40"></div></div><div class="sp2"></div>
    <p class="k">Reading</p><div class="sp"></div><div class="card">
      <div class="row between"><span class="label">Bible</span><div class="seg" role="group" aria-label="Translation">${Object.entries(TR).map(([k, t]) => `<button data-tr="${k}" aria-pressed="${S.settings.tr === k}">${t.name}</button>`).join('')}</div></div>
      <div class="row between"><span class="label">Text size</span><div class="row"><button class="chip" data-sz="-2" aria-label="Smaller">A−</button><span id="szv" class="note">${S.settings.size}</span><button class="chip" data-sz="2" aria-label="Larger">A+</button></div></div>
      <div class="row between wrap"><span class="label">Theme</span><div class="seg" role="group" aria-label="Theme">${[['auto', 'Auto'], ['light', 'Light'], ['sepia', 'Warm'], ['dark', 'Dark']].map(([k, l]) => `<button data-th="${k}" aria-pressed="${S.settings.theme === k}">${l}</button>`).join('')}</div></div></div>
    <div class="sp2"></div><p class="k">Your data</p><div class="sp"></div><div class="card sage"><div class="row"><span class="ico green">${ic('lock')}</span><p class="p grow" style="color:var(--ink)">Your prayer list, notes, people and highlights are stored only on this phone. We can’t see them. No ads, no tracking.</p></div></div><a class="note" href="https://alwaysfoundation.org/#/docs/saving" target="_blank" rel="noopener" style="display:inline-block;margin-top:10px;text-decoration:underline;text-underline-offset:3px">How your information is saved</a><div class="sp"></div><div class="sp"></div>
    <div class="list"><button class="li" id="exp"><span class="ico">${ic('download')}</span><div class="grow"><div class="t">Download my data</div><div class="s">A file you can keep or move to another phone</div></div></button>
      <label class="li" for="imp" style="cursor:pointer"><span class="ico sand">${ic('share')}</span><div class="grow"><div class="t">Restore from a file</div><div class="s">Bring your data from another phone</div></div><input type="file" id="imp" accept="application/json" class="sr"></label>
      <button class="li" id="del"><span class="ico peach">${ic('trash')}</span><div class="grow"><div class="t">Delete everything</div><div class="s">Clears this app on this phone</div></div></button></div>
    <div class="sp2"></div><p class="k">About</p><div class="sp"></div><div class="list">
      <a class="li" href="https://alwaysfoundation.org/#/privacy" target="_blank" rel="noopener"><div class="grow"><div class="t">Privacy</div></div><span class="chev">${ic('right', 18)}</span></a>
      <a class="li" href="https://alwaysfoundation.org/#/terms" target="_blank" rel="noopener"><div class="grow"><div class="t">Terms</div></div><span class="chev">${ic('right', 18)}</span></a>
      <a class="li" href="mailto:hello@alwaysfoundation.org"><div class="grow"><div class="t">Contact us</div><div class="s">hello@alwaysfoundation.org</div></div><span class="chev">${ic('right', 18)}</span></a></div>
    <div class="sp2"></div><button class="btn light" id="inst" hidden>${ic('download', 18)}Add to home screen</button>
    <p class="note" style="text-align:center;margin-top:18px">The Always App, from the Always Foundation. Together for the Gospel.<br>Bible text: World English Bible and King James Version, public domain.</p>`, { tab: 'home' });
  $('#mn').onchange = (e) => { S.settings.name = e.target.value.trim().slice(0, 40); save(); toast('Saved'); };
  $$('[data-tr]').forEach((b) => (b.onclick = () => { S.settings.tr = b.dataset.tr; save(); $$('[data-tr]').forEach((x) => x.setAttribute('aria-pressed', x === b)); }));
  $$('[data-sz]').forEach((b) => (b.onclick = () => { S.settings.size = Math.max(15, Math.min(30, S.settings.size + Number(b.dataset.sz))); save(); $('#szv').textContent = S.settings.size; }));
  $$('[data-th]').forEach((b) => (b.onclick = () => { S.settings.theme = b.dataset.th; save(); applyTheme(); $$('[data-th]').forEach((x) => x.setAttribute('aria-pressed', x === b)); }));
  $('#exp').onclick = () => { const a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([JSON.stringify(S, null, 2)], { type: 'application/json' })); a.download = `always-app-${today()}.json`; a.click(); };
  $('#imp').onchange = async (e) => { try { const d = JSON.parse(await e.target.files[0].text()); if (typeof d !== 'object' || !d.settings) throw 0; S = Object.assign(blank(), d); save(); applyTheme(); toast('Restored'); route(); } catch { toast('That file couldn’t be read'); } };
  $('#del').onclick = () => { if (confirmBox('Delete everything in the Always App on this phone? This can’t be undone.')) { localStorage.removeItem(KEY); S = blank(); location.hash = '#/'; route(); } };
  if (deferredInstall) { $('#inst').hidden = false; $('#inst').onclick = async () => { deferredInstall.prompt(); deferredInstall = null; $('#inst').hidden = true; }; }
});

// ---------------------------------------------------------------- Start
let deferredInstall = null;
addEventListener('beforeinstallprompt', (e) => { e.preventDefault(); deferredInstall = e; });
if ('serviceWorker' in navigator && location.protocol === 'https:') navigator.serviceWorker.register('/sw.js').catch(() => {});
applyTheme();
loadBooks().catch(() => {});
route();
})();
