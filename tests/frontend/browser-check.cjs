/* Optional real-browser check of the same component used in Home Assistant. */
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const http = require("node:http");
const { chromium } = require("playwright");

(async () => {
  const root = path.resolve(__dirname, "../..");
  const server = http.createServer((request, response) => {
    const pathname = decodeURIComponent(new URL(request.url, "http://localhost").pathname);
    const filename = path.resolve(root, "." + pathname);
    if (!filename.startsWith(root + path.sep) || !fs.existsSync(filename) || !fs.statSync(filename).isFile()) {
      response.writeHead(404); response.end(); return;
    }
    response.setHeader("Content-Type", filename.endsWith(".js") ? "text/javascript" : filename.endsWith(".json") ? "application/json" : "text/html");
    response.end(fs.readFileSync(filename));
  });
  await new Promise(resolve => server.listen(0, "127.0.0.1", resolve));
  const browser = await chromium.launch({ headless: true, executablePath: process.env.MANGO_CHROMIUM_EXECUTABLE || undefined, args: ["--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage"] });
  const page = await browser.newPage({ viewport: { width: 1500, height: 1120 } });
  const errors = [];
  page.on("pageerror", error => errors.push(error.message));
  const url = process.env.MANGO_DEMO_URL || `http://127.0.0.1:${server.address().port}/tests/frontend/demo.html`;
  try {
    await page.goto(url);
    await page.locator("mango-control-panel .parameter").first().waitFor();
    assert.equal(await page.locator("mango-control-panel .parameter").count(), 46);
    assert.equal(await page.locator("mango-control-panel .description").count(), 46);
    await page.locator('[data-family="Heating / upper table"]').click();
    assert.equal(await page.locator(".parameter").count(), 18);
    const input = page.locator('.value-input[data-key="14:16"]');
    await input.fill("31");
    assert.equal(await page.evaluate(() => window.mangoDemo.calls.length), 0);
    await page.locator('[data-apply="14:16"]').click();
    await page.waitForFunction(() => window.mangoDemo.calls.length === 1 && !window.mangoDemo.card._pending.size);
    assert.equal(await page.locator('.parameter[data-key="14:16"] .current-value').textContent(), "31");
    await page.evaluate(() => { window.demoFail = true; });
    await input.fill("32");
    await page.locator('[data-apply="14:16"]').click();
    await page.waitForFunction(() => window.mangoDemo.calls.length === 2 && !window.mangoDemo.card._pending.size);
    assert.match(await page.locator('.parameter[data-key="14:16"] .result').textContent(), /original value restored/);
    assert.equal(await page.locator('.parameter[data-key="14:16"] .current-value').textContent(), "31");
    await page.evaluate(() => { window.demoFail = false; });
    await page.locator('[data-action="refresh"]').click();
    assert.equal(await page.evaluate(() => window.mangoDemo.calls.at(-1).service), "press");
    await page.locator(".search").fill("Cool Ctrl Cpst");
    assert.equal(await page.locator(".parameter").count(), 1);
    assert.match(await page.locator(".description").textContent(), /Raw 1/);

    await page.goto(url);
    await page.locator(".parameter").first().waitFor();
    await page.locator('[data-family="Heating / upper table"]').click();
    await page.evaluate(() => document.fonts.ready);
    const out = path.resolve(__dirname, "../../docs/images");
    fs.mkdirSync(out, { recursive: true });
    await page.screenshot({ path: path.join(out, "dashboard-desktop.png") });
    const desktop = await page.evaluate(() => {
      const card = document.querySelector("mango-control-panel");
      return { viewport: innerWidth, width: card.scrollWidth, cards: card.shadowRoot.querySelectorAll(".parameter").length };
    });
    assert.ok(desktop.width <= desktop.viewport, "Desktop view overflows horizontally");
    await page.setViewportSize({ width: 390, height: 1250 });
    await page.locator(".parameter").first().waitFor();
    await page.screenshot({ path: path.join(out, "dashboard-mobile.png") });
    const mobile = await page.evaluate(() => {
      const card = document.querySelector("mango-control-panel"), root = card.shadowRoot;
      return { viewport: innerWidth, width: card.scrollWidth, widest: Math.max(...[...root.querySelectorAll(".parameter")].map(e => e.getBoundingClientRect().right)) };
    });
    assert.ok(mobile.width <= mobile.viewport, "Mobile view overflows horizontally");
    assert.ok(mobile.widest <= mobile.viewport, "Mobile parameter card exceeds screen width");
    assert.deepEqual(errors, []);
    console.log("Real-browser checks passed: categories, descriptions, explicit writes, recovery errors, refresh, search, desktop and mobile layout.");
  } finally { await browser.close(); await new Promise(resolve => server.close(resolve)); }
})().catch(error => { console.error(error); process.exit(1); });
