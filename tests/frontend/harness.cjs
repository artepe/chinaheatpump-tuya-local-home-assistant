const fs = require("node:fs");
const path = require("node:path");
const { JSDOM } = require("jsdom");
const source = fs.readFileSync(path.join(__dirname, "../../custom_components/mango_tuya_local/frontend/mango-parameter-card.js"), "utf8");
const fixture = JSON.parse(fs.readFileSync(path.join(__dirname, "demo-data.json"), "utf8"));

async function create(config = {}) {
  const dom = new JSDOM("<!doctype html><body></body>", { runScripts: "outside-only", pretendToBeVisual: true, url: "http://localhost/" });
  dom.window.eval(source);
  const card = dom.window.document.createElement("mango-parameter-card");
  const data = structuredClone(fixture), calls = [];
  const hass = {
    states: data.states,
    callWS: async () => data.catalog,
    callService: async (domain, service, args) => {
      calls.push({ domain, service, args: { ...args } });
      if (hass.fail) throw new Error("Write refused; original value restored.");
      if (hass.wait) await hass.wait;
      if (domain === "number") hass.states[args.entity_id] = { ...hass.states[args.entity_id], state: String(args.value) };
      if (domain === "select") hass.states[args.entity_id] = { ...hass.states[args.entity_id], state: args.option };
      card.hass = hass;
    }
  };
  card.setConfig(config);
  dom.window.document.body.append(card);
  card.hass = hass;
  await card._load();
  await new Promise(resolve => setTimeout(resolve, 25));
  return { dom, card, hass, calls, data, close: () => { card.remove(); dom.window.close(); } };
}
module.exports = { create };
