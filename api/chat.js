// Vercel Serverless Function: Proxy to OpenRouter AI (100% Free Tier)
export default async function handler(req, res) {
  // Enable CORS
  res.setHeader('Access-Control-Allow-Credentials', 'true');
  res.setHeader('Access-Control-Allow-Origin', '*');
  res.setHeader('Access-Control-Allow-Methods', 'GET,OPTIONS,PATCH,DELETE,POST,PUT');
  res.setHeader(
    'Access-Control-Allow-Headers',
    'X-CSRF-Token, X-Requested-With, Accept, Accept-Version, Content-Length, Content-MD5, Content-Type, Date, X-Api-Version, Authorization'
  );

  if (req.method === 'OPTIONS') {
    return res.status(200).end();
  }

  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method Not Allowed' });
  }

  try {
    const apiKey = process.env.OPENROUTER_API_KEY;
    if (!apiKey) {
      return res.status(500).json({
        error: 'OPENROUTER_API_KEY is not configured in Vercel environment variables.'
      });
    }

    const { messages, model, max_tokens } = req.body || {};

    const targetModel = model && !model.startsWith('llama') && !model.startsWith('qwen3.5')
      ? (model.startsWith('openrouter/') ? model.replace('openrouter/', '') : model)
      : 'minimax/minimax-m3.1-flash:free';

    const openrouterResp = await fetch('https://openrouter.ai/api/v1/chat/completions', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${apiKey}`,
        'Content-Type': 'application/json',
        'HTTP-Referer': 'https://jarvis.syahmiaof.my',
        'X-Title': 'J.A.R.V.I.S. Mark 85',
      },
      body: JSON.stringify({
        model: targetModel,
        messages: messages || [
          { role: 'system', content: "You are J.A.R.V.I.S. built by Boss Syahmi." },
          { role: 'user', content: "Hello" }
        ],
        max_tokens: max_tokens || 120,
      }),
    });

    const data = await openrouterResp.json();
    return res.status(openrouterResp.status).json(data);
  } catch (error) {
    console.error('Serverless error:', error);
    return res.status(500).json({ error: error.message });
  }
}
