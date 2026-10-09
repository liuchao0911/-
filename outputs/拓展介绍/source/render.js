const { chromium } = require('playwright');
(async () => {
  const dir = process.argv[2];
  const b = await chromium.launch({ proxy: process.env.HTTPS_PROXY ? { server: process.env.HTTPS_PROXY } : undefined, args: ['--ignore-certificate-errors-spki-list'] });
  const p = await b.newPage({ viewport: { width: 1280, height: 720 } });
  await p.goto('file://' + dir + '/deck.html', { waitUntil: 'networkidle' });
  await p.evaluate(() => document.fonts.ready);
  const fam = await p.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').length);
  console.log('fonts loaded', fam);
  await p.pdf({ path: dir + '/out.pdf', width: '1280px', height: '720px', printBackground: true });
  const n = await p.locator('section').count();
  for (let i = 0; i < n; i++) await p.locator('section').nth(i).screenshot({ path: dir + `/shot${i + 1}.png` });
  await b.close();
})();
