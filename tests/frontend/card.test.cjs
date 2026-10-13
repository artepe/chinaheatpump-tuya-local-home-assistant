const { test } = require("node:test");
const assert = require("node:assert/strict");
const { create } = require("./harness.cjs");

test("all 770 controls appear in their 17 categories with English help", async () => {
  const h = await create();
  try {
    assert.equal(h.card.shadowRoot.querySelectorAll("nav [data-group]").length, 18);
    assert.equal(h.card.shadowRoot.querySelectorAll(".parameter").length, 46);
    h.card.shadowRoot.querySelector('[data-group="-1"]').click();
    assert.equal(h.card.shadowRoot.querySelectorAll(".parameter").length, 770);
    assert.equal(h.card.shadowRoot.querySelectorAll(".description").length, 770);
    assert.equal(h.calls.length, 0);
  } finally { h.close(); }
});

test("working frequency filters separate all four operating tables", async () => {
  const h = await create();
  try {
    h.card.shadowRoot.querySelector('[data-family="Heating / upper table"]').click();
    assert.equal(h.card.shadowRoot.querySelectorAll(".parameter").length, 18);
    h.card.shadowRoot.querySelector('[data-family="Heating / lower table"]').click();
    assert.equal(h.card.shadowRoot.querySelectorAll(".parameter").length, 12);
    h.card.shadowRoot.querySelector('[data-family="Cooling / upper table"]').click();
    assert.equal(h.card.shadowRoot.querySelectorAll(".parameter").length, 12);
    h.card.shadowRoot.querySelector('[data-family="Cooling / lower table"]').click();
    assert.equal(h.card.shadowRoot.querySelectorAll(".parameter").length, 4);
  } finally { h.close(); }
});

test("editing sends no service until Apply and targets only the mapped entity", async () => {
  const h = await create();
  try {
    const input = h.card.shadowRoot.querySelector('.value-input[data-key="14:16"]');
    input.value = "31"; input.dispatchEvent(new h.dom.window.Event("input", { bubbles: true }));
    assert.equal(h.calls.length, 0);
    const p = h.card._parameters().find(p => p.key === "14:16");
    await h.card._apply(p);
    assert.deepEqual(h.calls, [{ domain: "number", service: "set_value", args: { entity_id: "number.demo_field_14_16", value: 31 } }]);
    assert.equal(h.hass.states[p.entity_id].state, "31");
  } finally { h.close(); }
});

test("invalid step, empty value, out-of-bounds and fixed bounds never write", async () => {
  const h = await create();
  try {
    const p = h.card._parameters().find(p => p.key === "14:16");
    assert.equal(h.card._valid(p, ""), false);
    assert.equal(h.card._valid(p, "30.5"), false);
    assert.equal(h.card._valid(p, "10000"), false);
    h.hass.states[p.entity_id].attributes.min = 30;
    h.hass.states[p.entity_id].attributes.max = 30;
    assert.equal(h.card._valid(p, "31"), false);
    assert.equal(h.calls.length, 0);
  } finally { h.close(); }
});

test("decimal scale and alarm selection use the correct Home Assistant services", async () => {
  const h = await create();
  try {
    h.card._group = 1; h.card._drawRows();
    const cool = h.card._parameters().find(p => p.key === "1:10");
    h.card.shadowRoot.querySelector('.value-input[data-key="1:10"]').value = "0.2";
    await h.card._apply(cool);
    assert.equal(h.calls[0].args.value, 0.2);
    assert.equal(h.card._valid(cool, "0.15"), false);
    h.card._group = 0; h.card._drawRows();
    const alarm = h.card._parameters().find(p => p.key === "0:20");
    h.card.shadowRoot.querySelector('.value-input[data-key="0:20"]').value = "Sound On";
    await h.card._apply(alarm);
    assert.equal(h.calls[1].service, "select_option");
    assert.equal(h.calls[1].args.option, "Sound On");
  } finally { h.close(); }
});

test("failed write keeps current state and reports recovery instead of optimistic success", async () => {
  const h = await create();
  try {
    h.hass.fail = true;
    const p = h.card._parameters().find(p => p.key === "14:16");
    h.card.shadowRoot.querySelector('.value-input[data-key="14:16"]').value = "31";
    await h.card._apply(p);
    const row = h.card.shadowRoot.querySelector('.parameter[data-key="14:16"]');
    assert.equal(row.querySelector(".current-value").textContent, "30.0");
    assert.match(row.querySelector(".result").textContent, /original value restored/);
    assert.equal(row.querySelector(".result").classList.contains("error"), true);
  } finally { h.close(); }
});

test("unknown button timestamp still permits refresh while unavailable controls are disabled", async () => {
  const h = await create();
  try {
    assert.equal(h.card.shadowRoot.querySelector('[data-action="refresh"]').disabled, false);
    await h.card._refresh();
    assert.equal(h.calls[0].service, "press");
    const p = h.card._parameters().find(p => p.key === "14:16");
    h.hass.states[p.entity_id].state = "unavailable";
    h.card._update();
    assert.equal(h.card.shadowRoot.querySelector('.value-input[data-key="14:16"]').disabled, true);
    assert.equal(h.card._valid(p, "31"), false);
  } finally { h.close(); }
});

test("missing configured pump never falls back to another device", async () => {
  const h = await create({ entry_id: "missing-pump" });
  try { assert.equal(h.card._device(), undefined); assert.equal(h.card.shadowRoot.querySelectorAll(".parameter").length, 0); }
  finally { h.close(); }
});

test("read-only HA permission disables edits without hiding the explanation", async () => {
  const h = await create();
  try {
    const p = h.card._parameters().find(p => p.key === "14:16");
    p.can_control = false; h.card._update();
    const row = h.card.shadowRoot.querySelector('.parameter[data-key="14:16"]');
    assert.equal(row.querySelector(".value-input").disabled, true);
    assert.match(row.querySelector(".limits").textContent, /Read-only/);
    assert.equal(h.card._valid(p, "31"), false);
  } finally { h.close(); }
});

test("live state refresh preserves a typed draft and never turns missing temperature into zero", async () => {
  const h = await create();
  try {
    const input = h.card.shadowRoot.querySelector('.value-input[data-key="14:16"]');
    input.value = "31"; input.dispatchEvent(new h.dom.window.Event("input", { bubbles: true }));
    h.hass.states["sensor.demo_current_temperature"].state = "unavailable";
    h.card._update();
    assert.equal(input.value, "31");
    assert.equal(h.card.shadowRoot.querySelector('[data-metric="current_temperature"]').textContent, "\u2014");
  } finally { h.close(); }
});
