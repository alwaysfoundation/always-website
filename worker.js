// alwaysfoundation.org: serves the website and sends form messages to the foundation inbox.
// The inbox address is the FORMS_TO secret, set in the Cloudflare dashboard (a verified Email Routing destination).
import { EmailMessage } from 'cloudflare:email';
import HTML from './index.html';

const SECURITY = {
  'strict-transport-security': 'max-age=31536000; includeSubDomains',
  'x-content-type-options': 'nosniff',
  'referrer-policy': 'strict-origin-when-cross-origin',
  'permissions-policy': 'camera=(), microphone=(), geolocation=()',
  'x-frame-options': 'SAMEORIGIN',
};
const KINDS = { join: 'Get involved', claims: 'Church claim', feedback: 'Idea or problem' };
const clean = (v) => String(v ?? '').replace(/[\r\n]+/g, ' ').slice(0, 2000);

async function handleForm(request, env, kind) {
  if (request.method !== 'POST') return new Response('Method not allowed', { status: 405 });
  if (Number(request.headers.get('content-length') || 0) > 20000) return new Response('Too large', { status: 413 });
  const origin = request.headers.get('origin') || '';
  if (origin && !/^https:\/\/(www\.)?alwaysfoundation\.org$/.test(origin)) return new Response('Forbidden', { status: 403 });
  let data = {};
  if ((request.headers.get('content-type') || '').includes('application/json')) data = await request.json().catch(() => ({}));
  else { const f = await request.formData().catch(() => null); if (f) for (const [k, v] of f) data[k] = typeof v === 'string' ? v : ''; }
  if (data.company_site) return Response.json({ ok: true });
  delete data.company_site;
  const lines = Object.entries(data).map(([k, v]) => `${clean(k)}: ${clean(v)}`).join('\n');
  if (!lines.trim() || !env.FORMS_TO) return Response.json({ ok: false }, { status: env.FORMS_TO ? 400 : 503 });
  const email = clean(data.email);
  const replyTo = /^[^\s@<>]+@[^\s@<>]+\.[^\s@<>]+$/.test(email) ? `\r\nReply-To: ${email}` : '';
  const subject = `Website: ${KINDS[kind]}`;
  const from = 'forms@alwaysfoundation.org';
  const raw = `From: Always Foundation website <${from}>\r\nTo: ${env.FORMS_TO}\r\nSubject: ${subject}${replyTo}\r\nMessage-ID: <${crypto.randomUUID()}@alwaysfoundation.org>\r\nDate: ${new Date().toUTCString()}\r\nMIME-Version: 1.0\r\nContent-Type: text/plain; charset=utf-8\r\n\r\n${subject}\n\n${lines}\n`;
  try { await env.FORMS.send(new EmailMessage(from, env.FORMS_TO, raw)); return Response.json({ ok: true }); }
  catch { return Response.json({ ok: false }, { status: 502 }); }
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    if (url.hostname === 'www.alwaysfoundation.org') return Response.redirect(`https://alwaysfoundation.org${url.pathname}${url.search}`, 301);
    const m = url.pathname.match(/^\/api\/forms\/(join|v1\/orgs\/[^/]+\/claims|v1\/feedback)$/);
    if (m) return handleForm(request, env, m[1] === 'join' ? 'join' : m[1].endsWith('claims') ? 'claims' : 'feedback');
    if (url.pathname.startsWith('/api/')) return new Response('Not found', { status: 404 });
    const BRAND = { 'always-foundation-logo.svg': 'image/svg+xml', 'always-foundation-logo.png': 'image/png', 'always-foundation-logo-on-green.svg': 'image/svg+xml', 'always-foundation-logo-on-green.png': 'image/png', 'always-foundation-logo-reverse.svg': 'image/svg+xml' };
    if (url.pathname.startsWith('/brand/')) {
      const f = url.pathname.slice(7), type = BRAND[f];
      if (!type) return new Response('Not found', { status: 404 });
      const r = await fetch('https://raw.githubusercontent.com/alwaysfoundation/always-website/main/brand/' + f, { headers: { 'user-agent': 'always-website-worker' }, cf: { cacheTtlByStatus: { '200-299': 3600, '404': 0 }, cacheEverything: true } });
      if (!r.ok) return new Response('Not found', { status: 404 });
      const disp = url.searchParams.has('download') ? 'attachment; filename="' + f + '"' : 'inline';
      return new Response(r.body, { headers: { 'content-type': type, 'content-disposition': disp, 'cache-control': 'public, max-age=3600', 'x-content-type-options': 'nosniff' } });
    }
    if (url.pathname === '/robots.txt') return new Response('User-agent: *\nAllow: /\n', { headers: { 'content-type': 'text/plain' } });
    return new Response(HTML, { headers: { 'content-type': 'text/html; charset=utf-8', 'cache-control': 'public, max-age=300', ...SECURITY } });
  },
};
