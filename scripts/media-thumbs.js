const https = require('https');

const TOKEN = 'EAAbG6Y0TtiEBRKi9XkBEb0wd55OEHSMXHqA8Acl0TvFheIDvI5wkKNpGAdcjK47BTlZAXxLsgTFZCUS4ZATXBnThyVztfMTFroyOP2EBYb4HZBqH4LMKZB2t6dBpuauPD9YS5snoZCfRVAEequyo7fwft6DzTFhcGMd7TIdq9NmgrvK6yOv796ZC6oSgcyvX3fIw6cZBgrZBPlneAyUHterCTo0BxYZAk3kOnWDWw7krQJZCNXcBdmAV7DNLaHiybmqoUQCJ1xQsVMzy9mTa5CmYTGv';
const IG_ID = '17841454974456376';

function get(url) {
  return new Promise((res, rej) => {
    https.get(url, r => {
      let d = '';
      r.on('data', c => d += c);
      r.on('end', () => { try { res(JSON.parse(d)); } catch(e) { res({raw: d}); } });
    }).on('error', rej);
  });
}

async function main() {
  // Jalar media con thumbnail_url, media_url y permalink
  const url = `https://graph.facebook.com/v19.0/${IG_ID}/media?fields=id,media_type,timestamp,like_count,comments_count,thumbnail_url,media_url,permalink,insights.metric(reach,saved,shares)&since=2026-03-01&until=2026-03-31&limit=50&access_token=${TOKEN}`;
  const data = await get(url);
  
  const posts = (data.data || []).map(p => {
    const metrics = {};
    (p.insights?.data || []).forEach(m => { metrics[m.name] = m.values?.[0]?.value || 0; });
    return {
      id: p.id,
      type: p.media_type,
      date: p.timestamp?.substring(0, 10),
      likes: p.like_count || 0,
      comments: p.comments_count || 0,
      reach: metrics.reach || 0,
      saved: metrics.saved || 0,
      shares: metrics.shares || 0,
      thumbnail: p.thumbnail_url || p.media_url || null,
      permalink: p.permalink || null
    };
  });

  // Ordenar por alcance desc
  posts.sort((a, b) => b.reach - a.reach);
  console.log(JSON.stringify(posts, null, 2));
}

main().catch(console.error);
