// Track's End Ticket Timer: serves the cook page at finux.tech/cook and lets it ask Claude
// without the API key ever reaching a phone.
//   Secret  ANTHROPIC_API_KEY  (required)  your Claude API key from console.anthropic.com
//   Secret  KITCHEN_CODE       (optional)  if set, a phone must enter this code before it can use Claude
//   Vars    QUICK_MODEL / STRONG_MODEL      which Claude models read tickets (see wrangler.toml)
//   Var     ANTHROPIC_URL      (optional)  send calls through a Cloudflare AI Gateway instead of straight to Anthropic
import PAGE from './cook.html';

const ANTHROPIC = 'https://api.anthropic.com/v1/messages';
const MEDIA = /^image\/(jpeg|png|webp|gif)$/;

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const path = url.pathname;

    if (path === '/cook/api/claude' || path === '/api/claude') {
      if (request.method === 'OPTIONS') return new Response(null, { status: 204, headers: cors(request) });
      if (request.method !== 'POST') return reply({ error: { code: 'invalid_request', message: 'Use POST.' } }, 405, request);
      return askClaude(request, env);
    }
    // the page lives at /cook/ so its relative api/claude calls stay under the finux.tech/cook* route
    if (path === '/' || path === '/cook') return Response.redirect(new URL('/cook/', url).href, 302);
    if (path === '/cook/' || path === '/cook/index.html') {
      return new Response(PAGE, {
        headers: {
          'content-type': 'text/html; charset=utf-8',
          'cache-control': 'no-cache',
          'x-content-type-options': 'nosniff',
          'referrer-policy': 'same-origin',
        },
      });
    }
    return new Response('Not found', { status: 404 });
  },
};

async function askClaude(request, env) {
  if (!env.ANTHROPIC_API_KEY) {
    return reply({ error: { code: 'not_configured', message: 'Add the ANTHROPIC_API_KEY secret to this Worker in Cloudflare.' } }, 500, request);
  }
  if (env.KITCHEN_CODE && request.headers.get('x-kitchen-code') !== env.KITCHEN_CODE) {
    return reply({ error: { code: 'bad_code', message: 'Wrong or missing kitchen code.' } }, 401, request);
  }

  let body;
  try { body = await request.json(); } catch { return reply({ error: { code: 'invalid_request', message: 'The request body must be JSON.' } }, 400, request); }

  const prompt = typeof body.prompt === 'string' ? body.prompt : '';
  if (!prompt || prompt.length > 200000) {
    return reply({ error: { code: 'prompt_too_large', message: 'The prompt is missing or too long.' } }, 400, request);
  }
  const content = [];
  for (const im of (Array.isArray(body.images) ? body.images : []).slice(0, 2)) {
    if (im && MEDIA.test(im.type) && typeof im.data === 'string' && im.data.length < 6800000) {
      content.push({ type: 'image', source: { type: 'base64', media_type: im.type, data: im.data } });
    }
  }
  content.push({ type: 'text', text: prompt });

  const model = body.tier === 'default'
    ? (env.STRONG_MODEL || 'claude-sonnet-5-5')
    : (env.QUICK_MODEL || 'claude-haiku-5-5');

  let res, data;
  try {
    res = await fetch(env.ANTHROPIC_URL || ANTHROPIC, {
      method: 'POST',
      headers: {
        'content-type': 'application/json',
        'x-api-key': env.ANTHROPIC_API_KEY,
        'anthropic-version': '2023-06-01',
      },
      body: JSON.stringify({ model, max_tokens: 2048, messages: [{ role: 'user', content }] }),
    });
    data = await res.json();
  } catch {
    return reply({ error: { code: 'upstream_error', message: 'Could not reach the Claude API.' } }, 502, request);
  }

  if (!res.ok) {
    const code = res.status === 401 || res.status === 403 ? 'bad_api_key'
      : res.status === 429 || res.status === 529 ? 'rate_limited'
      : res.status === 400 ? 'invalid_request'
      : 'upstream_error';
    const message = (data && data.error && data.error.message) || `The Claude API answered ${res.status}.`;
    return reply({ error: { code, message } }, 502, request);
  }

  const text = (data.content || []).filter((b) => b.type === 'text').map((b) => b.text).join('');
  return reply({ text, model: data.model, stop: data.stop_reason }, 200, request);
}

function cors(request) {
  const origin = request.headers.get('origin');
  return origin
    ? {
        'access-control-allow-origin': origin,
        'access-control-allow-headers': 'content-type, x-kitchen-code',
        'access-control-allow-methods': 'POST, OPTIONS',
        vary: 'origin',
      }
    : {};
}

function reply(obj, status, request) {
  return new Response(JSON.stringify(obj), {
    status,
    headers: { 'content-type': 'application/json', 'cache-control': 'no-store', ...cors(request) },
  });
}
