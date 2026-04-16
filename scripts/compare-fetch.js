const https = require('https');

const TOKEN = 'EAAbG6Y0TtiEBRKi9XkBEb0wd55OEHSMXHqA8Acl0TvFheIDvI5wkKNpGAdcjK47BTlZAXxLsgTFZCUS4ZATXBnThyVztfMTFroyOP2EBYb4HZBqH4LMKZB2t6dBpuauPD9YS5snoZCfRVAEequyo7fwft6DzTFhcGMd7TIdq9NmgrvK6yOv796ZC6oSgcyvX3fIw6cZBgrZBPlneAyUHterCTo0BxYZAk3kOnWDWw7krQJZCNXcBdmAV7DNLaHiybmqoUQCJ1xQsVMzy9mTa5CmYTGv';
const IG_ID  = '17841454974456376';
const AD_ACT = 'act_255327741430906' + '10';

function get(url) {
  return new Promise((res, rej) => {
    https.get(url, r => {
      let d = '';
      r.on('data', c => d += c);
      r.on('end', () => { try { res(JSON.parse(d)); } catch(e) { res({raw: d}); } });
    }).on('error', rej);
  });
}

async function getMediaForPeriod(since, until, label) {
  const url = `https://graph.facebook.com/v19.0/${IG_ID}/media?fields=id,media_type,timestamp,like_count,comments_count,insights.metric(reach,saved,shares)&since=${since}&until=${until}&limit=50&access_token=${TOKEN}`;
  const data = await get(url);
  const posts = data.data || [];
  let totalReach = 0, totalLikes = 0, totalComments = 0, totalShares = 0, totalSaved = 0;
  posts.forEach(p => {
    totalLikes    += p.like_count || 0;
    totalComments += p.comments_count || 0;
    (p.insights?.data || []).forEach(m => {
      const v = m.values?.[0]?.value || 0;
      if (m.name === 'reach')  totalReach  += v;
      if (m.name === 'saved')  totalSaved  += v;
      if (m.name === 'shares') totalShares += v;
    });
  });
  return { label, posts: posts.length, totalReach, totalLikes, totalComments, totalShares, totalSaved, raw: posts };
}

async function getAdsForPeriod(since, until, label) {
  const params = new URLSearchParams({
    fields: 'name,status,insights{spend,impressions,reach,clicks,cpc,cpm,frequency,actions,video_play_actions}',
    time_range: JSON.stringify({ since, until }),
    access_token: TOKEN, limit: 20
  });
  const url = `https://graph.facebook.com/v19.0/${AD_ACT}/campaigns?${params}`;
  const data = await get(url);
  let totalSpend=0, totalImp=0, totalReach=0, totalClicks=0, totalViews=0;
  (data.data || []).forEach(c => {
    (c.insights?.data || []).forEach(i => {
      totalSpend  += parseFloat(i.spend  || 0);
      totalImp    += parseInt(i.impressions || 0);
      totalReach  += parseInt(i.reach || 0);
      totalClicks += parseInt(i.clicks || 0);
      (i.actions || []).forEach(a => { if(a.action_type === 'video_view') totalViews += parseInt(a.value||0); });
    });
  });
  return { label, totalSpend: totalSpend.toFixed(2), totalImp, totalReach, totalClicks, totalViews };
}

async function getProfileFollowers() {
  const url = `https://graph.facebook.com/v19.0/${IG_ID}?fields=followers_count,media_count&access_token=${TOKEN}`;
  return await get(url);
}

async function main() {
  const [feb_ig, mar_ig, feb_ads, mar_ads, profile] = await Promise.all([
    getMediaForPeriod('2026-02-01','2026-02-28','Febrero 2026'),
    getMediaForPeriod('2026-03-01','2026-03-31','Marzo 2026'),
    getAdsForPeriod('2026-02-01','2026-02-28','Febrero 2026'),
    getAdsForPeriod('2026-03-01','2026-03-31','Marzo 2026'),
    getProfileFollowers()
  ]);

  const result = {
    profile,
    instagram: { feb: feb_ig, mar: mar_ig },
    ads: { feb: feb_ads, mar: mar_ads }
  };
  // remove raw posts to keep output clean
  delete result.instagram.feb.raw;
  delete result.instagram.mar.raw;

  console.log(JSON.stringify(result, null, 2));
}

main().catch(console.error);
