/* VS Code style code window + terminal (vk.ide). Shared by every video; build_canh.py appends it after core/vk.js.
   Everything is a pure function of timeline progress, so seeking works in both directions.

   const ide = vk.ide(root, { x: 160, y: 80, width: 1600, file: "notes.py", terminal: 240,
                              code: ['name = "Son"', "capital = 20000000"] });   // level: "auto" by default
   let t = ide.type(tl, { from: 1, to: 2, t: 3.0, cps: 30 });   // type lines 1..2 char by char; returns the end time
   ide.show(tl, 3, 4, t);                                         // lines 3..4 appear at once
   ide.hide(tl, 1, 4, t2);                                        // lines 1..4 disappear (reuse the window for the next step)
   ide.highlight(tl, 2, tOn, tOff, "rgba(250,204,21,0.2)");       // highlight one line while the narration talks about it
   ide.run(tl, t, { command: "python notes.py", output: ["Name: Son", "Capital: 20000000"] });   // terminal: type a command, print output
   ide.line(2)                                                    // DOM element of line 2, for custom tweens

   Options: x, y, width, height ("auto" = as tall as the lines need, or a number), file, code (array or string), lang ("python" | "text"),
   level ("auto" | "large" | "normal" | "small"), fontSize (overrides level), fit (true: keep `height` and shrink the font until all lines fit),
   terminal (terminal height in px, omit for none), title, tabLabel ("PY"), languageName ("Python"), statusBar (false to hide), id.
   Levels by number of lines: large 1-6 (40px), normal 7-9 (32px), small 10-14 (26px). More than 14 lines: split into screens (show / hide). */
(() => {
  const KEYWORDS = new Set(["if", "elif", "else", "for", "while", "in", "not", "and", "or", "return", "pass", "break", "continue", "try", "except", "finally", "with", "is", "del", "raise", "yield", "assert"]);
  const DECL = new Set(["def", "class", "import", "from", "as", "lambda", "global", "nonlocal"]);
  const BUILTINS = new Set(["print", "len", "range", "input", "int", "str", "float", "bool", "list", "dict", "set", "tuple", "sum", "max", "min", "round", "type", "enumerate", "zip", "sorted", "abs", "append", "keys", "values", "items"]);
  const CONSTANTS = new Set(["True", "False", "None"]);
  const LEVELS = { large: 40, normal: 32, small: 26 };
  const esc = (s) => s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

  function tokenize(line, lang) {
    if (lang === "text") return [{ c: "", s: line }];
    const re = /(#.*$)|("(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*')|(\b\d[\d_]*(?:\.\d+)?\b)|([A-Za-z_À-ỹ][\wÀ-ỹ]*)|(\s+)|(.)/g;
    const out = [];
    let m;
    while ((m = re.exec(line)) !== null) {
      if (m[1]) out.push({ c: "t-cmt", s: m[1] });
      else if (m[2]) out.push({ c: "t-str", s: m[2] });
      else if (m[3]) out.push({ c: "t-num", s: m[3] });
      else if (m[4]) {
        const w = m[4], next = line.slice(m.index + w.length).trimStart()[0];
        const c = DECL.has(w) ? "t-ctrl" : KEYWORDS.has(w) ? "t-kw" : CONSTANTS.has(w) ? "t-const" : (BUILTINS.has(w) || next === "(") ? "t-fn" : "t-var";
        out.push({ c, s: w });
      } else out.push({ c: "", s: m[0] });
    }
    return out;
  }

  function renderRow(tokens, n) {
    let left = n, out = "";
    for (const tk of tokens) {
      if (left <= 0) break;
      const part = tk.s.slice(0, left);
      out += tk.c ? `<span class="${tk.c}">${esc(part)}</span>` : esc(part);
      left -= tk.s.length;
    }
    return out;
  }

  function ide(parent, o) {
    const lang = o.lang ?? "python";
    const lines = Array.isArray(o.code) ? o.code : String(o.code).split("\n");
    const termH = o.terminal || 0, statusH = o.statusBar === false ? 0 : 30, headH = 44, tabsH = 40, pad = 14 + 18;
    const needed = (px) => headH + tabsH + pad + lines.length * Math.round(px * 1.6) + termH + statusH;
    const level = o.level ?? "auto";
    let fontSize = o.fontSize ?? LEVELS[level === "auto" ? (lines.length <= 6 ? "large" : lines.length <= 9 ? "normal" : "small") : level];
    let height = o.height;
    if (height === undefined || height === "auto") height = needed(fontSize);
    else if (o.fit) while (fontSize > 18 && needed(fontSize) > height) fontSize -= 1;
    const lh = Math.round(fontSize * 1.6), width = o.width ?? 1600;

    const root = document.createElement("div");
    root.className = "ide"; if (o.id) root.id = o.id;
    root.style.cssText = `left:${o.x ?? 0}px;top:${o.y ?? 0}px;width:${width}px;height:${height}px;font-size:${fontSize}px;`;
    root.innerHTML = `<div class="ide-dau"><i></i><i></i><i></i><span>${esc(o.title ?? "Visual Studio Code")}</span></div>
      <div class="ide-tabs"><div class="ide-tab on"><b>${esc(o.tabLabel ?? "PY")}</b>${esc(o.file ?? "main.py")}</div></div>`;
    const body = document.createElement("div");
    body.className = "ide-body"; body.style.cssText = `top:${headH + tabsH}px;height:${height - headH - tabsH - termH - statusH}px;padding-top:14px;`;
    const gutter = document.createElement("div");
    gutter.className = "ide-gutter"; gutter.style.cssText = `width:${String(lines.length).length * fontSize * 0.62 + 34}px;font-size:${fontSize}px;line-height:${lh}px;`;
    gutter.innerHTML = lines.map((_, i) => `<div style="height:${lh}px">${i + 1}</div>`).join("");
    const code = document.createElement("div");
    code.className = "ide-code"; code.style.cssText = `font-size:${fontSize}px;line-height:${lh}px;`;
    const tokens = lines.map((l) => tokenize(l, lang));
    const len = lines.map((l) => l.length);
    const rows = lines.map(() => { const r = document.createElement("div"); r.className = "ide-row"; r.style.height = lh + "px"; code.appendChild(r); return r; });
    body.appendChild(gutter); body.appendChild(code); root.appendChild(body);

    let termBody = null;
    if (termH > 0) {
      const term = document.createElement("div");
      term.className = "ide-term"; term.style.cssText = `top:${height - termH - statusH}px;height:${termH}px;`;
      term.innerHTML = `<div class="ide-term-dau"><span>PROBLEMS</span><span>OUTPUT</span><b>TERMINAL</b></div><div class="ide-term-than"></div>`;
      termBody = term.querySelector(".ide-term-than");
      root.appendChild(term);
    }
    if (statusH) {
      const s = document.createElement("div");
      s.className = "ide-stt"; s.innerHTML = `<span>⎇ main</span><span>${esc(o.languageName ?? "Python")} · UTF-8</span>`;
      root.appendChild(s);
    }
    (typeof parent === "string" ? document.querySelector(parent) : parent).appendChild(root);

    const draw = (i, n, caret) => {
      rows[i].innerHTML = renderRow(tokens[i], n) + (caret && n > 0 && n < len[i] ? '<span class="ide-caret">&nbsp;</span>' : "");
    };
    const api = { root, fontSize, height, line: (n) => rows[n - 1] };

    api.type = (tl, a) => {
      const cps = a.cps ?? 26, pause = a.pause ?? 0.18;
      let t = a.t;
      for (let i = a.from - 1; i <= a.to - 1; i++) {
        const p = { n: 0 }, d = Math.max(0.05, len[i] / cps);
        draw(i, 0, false);
        tl.to(p, { n: len[i], duration: d, ease: "none", onUpdate() { draw(i, Math.round(p.n), true); } }, t);
        t += d + (len[i] ? pause : 0.05);
      }
      return t;
    };
    api.show = (tl, from, to, t) => {
      for (let i = from - 1; i <= to - 1; i++) {
        const p = { n: 0 };
        draw(i, 0, false);
        tl.to(p, { n: len[i], duration: 0.001, ease: "none", onUpdate() { draw(i, Math.round(p.n), false); } }, t);
      }
    };
    api.hide = (tl, from, to, t) => {
      for (let i = from - 1; i <= to - 1; i++) {
        const p = { n: len[i] };
        tl.fromTo(p, { n: len[i] }, { n: 0, duration: 0.001, ease: "none", onUpdate() { draw(i, Math.round(p.n), false); } }, t);
      }
    };
    api.highlight = (tl, n, tOn, tOff, color = "rgba(250,204,21,0.2)") => {
      tl.fromTo(rows[n - 1], { backgroundColor: "rgba(0,0,0,0)", borderLeftColor: "rgba(0,0,0,0)" }, { backgroundColor: color, borderLeftColor: "#F26A21", duration: 0.25, ease: "power2.out" }, tOn);
      if (tOff != null) tl.to(rows[n - 1], { backgroundColor: "rgba(0,0,0,0)", borderLeftColor: "rgba(0,0,0,0)", duration: 0.3, ease: "power2.in" }, tOff);
    };
    let previousPage = null;
    api.run = (tl, t, a) => {
      if (!termBody) throw new Error("vk.ide: pass the `terminal` option (terminal height in px) to use run()");
      const cps = a.cps ?? 22, gap = a.gap ?? 0.3, command = a.command ?? "python main.py", prompt = '<span class="dau">$ </span>';
      const page = document.createElement("div");
      page.className = "ide-trang"; page.style.fontSize = (a.fontSize ?? Math.round(fontSize * 0.78)) + "px"; page.style.lineHeight = "1.55";
      const cmd = document.createElement("div"); cmd.className = "ide-dong-term"; cmd.innerHTML = prompt; page.appendChild(cmd);
      const outs = (a.output || []).map((s) => { const d = document.createElement("div"); d.className = "ide-dong-term"; d.textContent = s; d.style.opacity = "0"; page.appendChild(d); return d; });
      termBody.appendChild(page);
      gsap.set(page, { opacity: 0 });
      if (a.clear !== false && previousPage) tl.to(previousPage, { opacity: 0, duration: 0.2 }, t);
      tl.to(page, { opacity: 1, duration: 0.05 }, t);
      const p = { n: 0 }, d = Math.max(0.2, command.length / cps);
      tl.to(p, { n: command.length, duration: d, ease: "none", onUpdate() { cmd.innerHTML = prompt + esc(command.slice(0, Math.round(p.n))); } }, t + 0.1);
      let tt = t + 0.1 + d + (a.wait ?? 0.35);
      outs.forEach((e) => { tl.to(e, { opacity: 1, duration: 0.08 }, tt); tt += gap; });
      previousPage = page;
      return tt;
    };
    return api;
  }
  vk.ide = ide;
})();
