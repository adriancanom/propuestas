const https = require('https');

const TOKEN = 'EAAbG6Y0TtiEBRKi9XkBEb0wd55OEHSMXHqA8Acl0TvFheIDvI5wkKNpGAdcjK47BTlZAXxLsgTFZCUS4ZATXBnThyVztfMTFroyOP2EBYb4HZBqH4LMKZB2t6dBpuauPD9YS5snoZCfRVAEequyo7fwft6DzTFhcGMd7TIdq9NmgrvK6yOv796ZC6oSgcyvX3fIw6cZBgrZBPlneAyUHterCTo0BxYZAk3kOnWDWw7krQJZCNXcBdmAV7DNLaHiybmqoUQCJ1xQsVMzy9mTa5CmYTGv';
const PAGE_ID = '976877848844666';
const IG_ID   = '17841454974456376';
const SINCE   = process.argv[2] || '2026-03-01';
const UNTIL   = process.argv[3] || '2026-03-31';

function get(url) {
  return new Promise((res, rej) => {
    https.get(url, r => {
      let d = '';
      r.on('data', c => d += c);
      r.on('end', () => { try { res(JSON.parse(d)); } catch(e) { res(d); } });
    }).on('error', rej);
  });
}

async function main() {
  const results = {};

  // 1. PAGE insights
  const pageMetrics = 'page_impressions,page_reach,page_engaged_users,page_fans,page_fan_adds,page_fan_removes,page_views_total,page_post_engagements';
  const pageUrl = `https://graph.facebook.com/v19.0/${PAGE_ID}/insights?metric=${pageMetrics}&since=${SINCE}&until=${UNTIL}&period=month&access_token=${TOKEN}`;
  results.pageInsights = await get(pageUrl);

  // 2. PAGE posts en el período
  const postsUrl = `https://graph.facebook.com/v19.0/${PAGE_ID}/posts?fields=message,created_time,full_picture,insights.metric(post_impressions,post_reach,post_engaged_users,post_reactions_by_type_total)&since=${SINCE}&until=${UNTIL}&access_token=${TOKEN}`;
  results.pagePosts = await get(postsUrl);

  // 3. IG account insights
  const igMetrics = 'reach,impressions,profile_views,follower_count,accounts_engaged';
  const igInsightsUrl = `https://graph.facebook.com/v19.0/${IG_ID}/insights?metric=${igMetrics}&since=${SINCE}&until=${UNTIL}&period=month&access_token=${TOKEN}`;
  results.igInsights = await get(igInsightsUrl);

  // 4. IG media (posts/reels) del período
  const igMediaUrl = `https://graph.facebook.com/v19.0/${IG_ID}/media?fields=id,caption,media_type,timestamp,like_count,comments_count,insights.metric(reach,impressions,saved,plays,shares)&since=${SINCE}&until=${UNTIL}&access_token=${TOKEN}`;
  results.igMedia = await get(igMediaUrl);

  // 5. IG follower demographics
  const igFollowersUrl = `https://graph.facebook.com/v19.0/${IG_ID}?fields=followers_count,media_count,biography,website&access_token=${TOKEN}`;
  results.igProfile = await get(igFollowersUrl);

  console.log(JSON.stringify(results, null, 2));
}

main().catch(console.error);
