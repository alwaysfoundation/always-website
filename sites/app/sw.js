// Always Sent service worker: the app shell works offline, and Bible books are kept once read.
const SHELL = 'always-shell-v14';
const BIBLE = 'always-bible-v1';
const FILES = ['/', '/index.html', '/app.css', '/app.js', '/content.js', '/qrcode.js', '/manifest.webmanifest', '/bible/books.json', '/icon-192.png',
  '/fonts/manrope-latin-500-normal.woff2', '/fonts/manrope-latin-600-normal.woff2', '/fonts/manrope-latin-700-normal.woff2', '/fonts/manrope-latin-800-normal.woff2',
  '/fonts/inter-latin-400-normal.woff2', '/fonts/inter-latin-500-normal.woff2', '/fonts/inter-latin-600-normal.woff2', '/fonts/newsreader-latin-400-normal.woff2', '/fonts/newsreader-latin-400-italic.woff2'];
self.addEventListener('install', (e) => { e.waitUntil(caches.open(SHELL).then((c) => c.addAll(FILES)).then(() => self.skipWaiting())); });
self.addEventListener('activate', (e) => { e.waitUntil(caches.keys().then((ks) => Promise.all(ks.filter((k) => ![SHELL, BIBLE].includes(k)).map((k) => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', (e) => {
  const u = new URL(e.request.url);
  if (e.request.method !== 'GET' || u.origin !== location.origin) return;
  if (u.pathname.startsWith('/bible/') && u.pathname !== '/bible/books.json') {
    e.respondWith(caches.open(BIBLE).then(async (c) => (await c.match(e.request)) || fetch(e.request).then((r) => { if (r.ok) c.put(e.request, r.clone()); return r; })));
    return;
  }
  // Shell: network first so updates arrive, cache when offline.
  e.respondWith(fetch(e.request).then((r) => { if (r.ok) caches.open(SHELL).then((c) => c.put(e.request, r.clone())); return r; }).catch(() => caches.match(e.request).then((m) => m || caches.match('/index.html'))));
});
