const https = require('https');

const USER_TOKEN = 'EAAbG6Y0TtiEBRKi9XkBEb0wd55OEHSMXHqA8Acl0TvFheIDvI5wkKNpGAdcjK47BTlZAXxLsgTFZCUS4ZATXBnThyVztfMTFroyOP2EBYb4HZBqH4LMKZB2t6dBpuauPD9YS5snoZCfRVAEequyo7fwft6DzTFhcGMd7TIdq9NmgrvK6yOv796ZC6oSgcyvX3fIw6cZBgrZBPlneAyUHterCTo0BxYZAk3kOnWDWw7krQJZCNXcBdmAV7DNLaHiybmqoUQCJ1xQsVMzy9mTa5CmYTGv';
const PAGE_ID = '976877848844666';

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
  // 1. Ver qué páginas tiene el token
  console.log('=== /me/accounts ===');
  const accounts = await get(`https://graph.facebook.com/v19.0/me/accounts?access_token=${USER_TOKEN}`);
  console.log(JSON.stringify(accounts, null, 2));

  // 2. Intentar jalar la página directamente con el user token
  console.log('\n=== PAGE DIRECT ===');
  const page = await get(`https://graph.facebook.com/v19.0/${PAGE_ID}?fields=id,name,fan_count,access_token&access_token=${USER_TOKEN}`);
  console.log(JSON.stringify(page, null, 2));

  // 3. Ver los negocios del token
  console.log('\n=== /me/businesses ===');
  const biz = await get(`https://graph.facebook.com/v19.0/me/businesses?access_token=${USER_TOKEN}`);
  console.log(JSON.stringify(biz, null, 2));
}

main().catch(console.error);
