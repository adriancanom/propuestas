const https = require('https');

const USER_TOKEN = 'EAAbG6Y0TtiEBRKi9XkBEb0wd55OEHSMXHqA8Acl0TvFheIDvI5wkKNpGAdcjK47BTlZAXxLsgTFZCUS4ZATXBnThyVztfMTFroyOP2EBYb4HZBqH4LMKZB2t6dBpuauPD9YS5snoZCfRVAEequyo7fwft6DzTFhcGMd7TIdq9NmgrvK6yOv796ZC6oSgcyvX3fIw6cZBgrZBPlneAyUHterCTo0BxYZAk3kOnWDWw7krQJZCNXcBdmAV7DNLaHiybmqoUQCJ1xQsVMzy9mTa5CmYTGv';
const IG_ID   = '17841454974456376';
const PAGE_ID = '976877848844666';
const SINCE   = process.argv[2] || '2026-03-01';
const UNTIL   = process.argv[3] || '2026-03-31';

function get(url) {
  return new Promise((res, rej) => {
    https.get(url, r => {
      let d = '';
      r.on('data', c => d += c);
      r.on('end', () => { try { res(JSON.parse(d)); } catch(e) { res({ raw: d }); } });
    }).on('error', rej);
  });
}

async function getPageToken() {
  // Obtener el Page Access Token desde el User Token
  const url = `https://graph.facebook.com/v19.0/me/accounts?access_token=${USER_TOKEN}`;
  const data = await get(url);
  const page = (data.data || []).find(p => p.id === PAGE_ID);
  if (!page) {
    console.error('Página no encontrada. Páginas disponibles:', (data.data || []).map(p => `${p.name} (${p.id})`));
    return null;
  }
  return page.access_token;
}

async function getIGMedia() {
  const fields = 'id,media_type,timestamp,like_count,comments_count,thumbnail_url,media_url,permalink,insights.metric(reach,saved,shares)';
  const url = `https://graph.facebook.com/v19.0/${IG_ID}/media?fields=${fields}&since=${SINCE}&until=${UNTIL}&limit=50&access_token=${USER_TOKEN}`;
  const data = await get(url);
  const posts = (data.data || []).map(p => {
    const metrics = {};
    (p.insights?.data || []).forEach(m => { metrics[m.name] = m.values?.[0]?.value || 0; });
    return {
      id: p.id, type: p.media_type,
      date: p.timestamp?.substring(0, 10),
      likes: p.like_count || 0, comments: p.comments_count || 0,
      reach: metrics.reach || 0, saved: metrics.saved || 0, shares: metrics.shares || 0,
      thumbnail: p.thumbnail_url || p.media_url || null,
      permalink: p.permalink || null
    };
  });
  posts.sort((a, b) => b.reach - a.reach);
  return posts;
}

async function getIGProfile() {
  const url = `https://graph.facebook.com/v19.0/${IG_ID}?fields=followers_count,media_count,biography,website&access_token=${USER_TOKEN}`;
  return await get(url);
}

async function getPageInsights(pageToken) {
  const metrics = [
    'page_impressions', 'page_reach', 'page_engaged_users',
    'page_fans', 'page_fan_adds', 'page_fan_removes',
    'page_views_total', 'page_post_engagements',
    'page_video_views', 'page_actions_post_reactions_total'
  ].join(',');
  const url = `https://graph.facebook.com/v19.0/${PAGE_ID}/insights?metric=${metrics}&since=${SINCE}&until=${UNTIL}&period=month&access_token=${pageToken}`;
  return await get(url);
}

async function getPagePosts(pageToken) {
  const fields = 'message,created_time,full_picture,permalink_url,insights.metric(post_impressions,post_reach,post_engaged_users)';
  const url = `https://graph.facebook.com/v19.0/${PAGE_ID}/posts?fields=${fields}&since=${SINCE}&until=${UNTIL}&limit=20&access_token=${pageToken}`;
  return await get(url);
}

async function main() {
  console.error('Jalando Page Access Token...');
  const pageToken = await getPageToken();

  const results = { instagram: {}, facebook: {} };

  // ── INSTAGRAM ──────────────────────────────────────────────
  console.error('Jalando IG media + métricas...');
  results.instagram.profile = await getIGProfile();
  results.instagram.posts   = await getIGMedia();

  // ── FACEBOOK PAGE ───────────────────────────────────────────
  if (pageToken) {
    console.error('Jalando Facebook Page Insights...');
    const rawInsights = await getPageInsights(pageToken);
    // Convertir array de insights a objeto clave:valor
    const insights = {};
    (rawInsights.data || []).forEach(item => {
      const val = item.values?.find(v => v.value !== undefined);
      insights[item.name] = val?.value ?? 0;
    });
    results.facebook.insights = insights;

    console.error('Jalando Facebook Page posts...');
    const rawPosts = await getPagePosts(pageToken);
    results.facebook.posts = (rawPosts.data || []).map(p => {
      const metrics = {};
      (p.insights?.data || []).forEach(m => {
        metrics[m.name] = m.values?.[0]?.value || 0;
      });
      return {
        date: p.created_time?.substring(0, 10),
        message: (p.message || '').substring(0, 100),
        image: p.full_picture || null,
        url: p.permalink_url || null,
        impressions: metrics.post_impressions || 0,
        reach: metrics.post_reach || 0,
        engaged: metrics.post_engaged_users || 0
      };
    });
  } else {
    results.facebook.error = 'No se pudo obtener Page Access Token';
  }

  console.log(JSON.stringify(results, null, 2));
}

main().catch(console.error);
