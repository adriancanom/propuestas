const https = require('https');

// Page Access Token directo de Arichy Real Estate
const PAGE_TOKEN = 'EAAbG6Y0TtiEBRGeEy4RsyVoS1FyOZBw1lwZAg2kZCcwcydEk7FOK9gb5s2v0n5qHSdIomlhbnZAX4ZCGoPHTzVft3tQqpyfGUz43NALNfBCP7JFZAWcPYP4cke2TQSK9UJ3bhnZCUjxuZBgCTOYxFYorjiZAW1LpZAtrwYqpVRCaKROHCAGkHZBftfm1AAhWKEom5uvEmzV2sDHK7wyj8CbK8t7liGfdLU9XLPUiJi5gqXEWJYZD';
const PAGE_ID   = '976877848844666';
const SINCE     = process.argv[2] || '2026-03-01';
const UNTIL     = process.argv[3] || '2026-03-31';

function get(url) {
  return new Promise((res, rej) => {
    https.get(url, r => {
      let d = '';
      r.on('data', c => d += c);
      r.on('end', () => { try { res(JSON.parse(d)); } catch(e) { res({ raw: d }); } });
    }).on('error', rej);
  });
}

async function main() {
  // 1. Page insights del mes
  const metrics = [
    'page_impressions','page_impressions_organic','page_reach',
    'page_engaged_users','page_fans','page_fan_adds','page_fan_removes',
    'page_views_total','page_post_engagements','page_video_views'
  ].join(',');

  const insightsUrl = `https://graph.facebook.com/v19.0/${PAGE_ID}/insights?metric=${metrics}&since=${SINCE}&until=${UNTIL}&period=month&access_token=${PAGE_TOKEN}`;
  const insightsRaw = await get(insightsUrl);
  
  const insights = {};
  (insightsRaw.data || []).forEach(item => {
    const val = item.values?.find(v => v.value !== undefined);
    insights[item.name] = val?.value ?? 0;
  });

  // 2. Posts de la página en el período
  const postsUrl = `https://graph.facebook.com/v19.0/${PAGE_ID}/posts?fields=message,created_time,full_picture,permalink_url,insights.metric(post_impressions,post_reach,post_engaged_users)&since=${SINCE}&until=${UNTIL}&limit=20&access_token=${PAGE_TOKEN}`;
  const postsRaw = await get(postsUrl);

  const posts = (postsRaw.data || []).map(p => {
    const m = {};
    (p.insights?.data || []).forEach(i => { m[i.name] = i.values?.[0]?.value || 0; });
    return {
      date: p.created_time?.substring(0, 10),
      message: (p.message || '').substring(0, 120),
      image: p.full_picture || null,
      url: p.permalink_url || null,
      impressions: m.post_impressions || 0,
      reach: m.post_reach || 0,
      engaged: m.post_engaged_users || 0
    };
  });

  console.log(JSON.stringify({ insights, posts, fans: 14 }, null, 2));
}

main().catch(console.error);
