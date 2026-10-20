/* ZamForward Graphics Library — a drop-in "add a graphic" panel + render API.
   Needs: js/graphics-data.js (window.ZG_DATA) and css/graphics.css.
   Quick start:
     const lib = ZamGraphics.mount(document.querySelector('#panel'), {
       color: '#C9A86A',
       onAdd: g => myEditor.addGraphic(g),          // g = { id, name, type:'icon'|'text', svg, color, ... }
       onUndo: g => myEditor.removeLast(g)          // optional: shows an Undo button in the toast
     });
   Rendering helpers (use them inside your own canvas / SVG editor):
     ZamGraphics.svg(id, {color, color2, size})        -> standalone <svg> string
     ZamGraphics.markup(item, {color, color2})          -> inner SVG markup (for embedding in your own <svg>)
     await ZamGraphics.toImage(id, {color, size})       -> Image (or Canvas for wordmarks), ready for ctx.drawImage
     await ZamGraphics.draw(ctx, id, {x, y, size, color, rotation, flipX})
*/
(function () {
  'use strict';
  const D = window.ZG_DATA;
  if (!D) throw new Error('ZamGraphics: load js/graphics-data.js before graphics.js');
  const BY = {}; D.items.forEach(i => { BY[i.id] = i; });
  const CATNAME = Object.fromEntries(D.cats.map(c => [c.id, c.name]));
  const DEFAULT_COLORS = ['#111417', '#F4F1EA', '#C9A86A', '#EFD965', '#088395', '#1F4FD8', '#6B3FA0', '#C53030', '#F2711C', '#39FF14'];

  /* ---------- colour helpers ---------- */
  const hex2rgb = h => { h = h.replace('#', ''); if (h.length === 3) h = h.replace(/./g, '$&$&'); const n = parseInt(h, 16); return [(n >> 16) & 255, (n >> 8) & 255, n & 255]; };
  const lum = c => { const [r, g, b] = hex2rgb(c).map(v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }); return 0.2126 * r + 0.7152 * g + 0.0722 * b; };
  const contrast = (a, b) => { const A = lum(a), B = lum(b); return (Math.max(A, B) + 0.05) / (Math.min(A, B) + 0.05); };
  const ink = c => (lum(c) > 0.4 ? '#111417' : '#F4F1EA');
  const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const f2 = n => Math.round(n * 100) / 100;

  /* ---------- markup / render API ---------- */
  let counter = 0;
  function markup(item, o) {
    o = o || {}; const color = o.color || '#111417', c2 = o.color2 || ink(color); let s = item.svg || '';
    if (item.mode === 'mono') s = s.replace(/currentColor/g, color);
    else if (item.mode === 'multi') s = s.replace(/\{c1\}/g, color).replace(/\{c2\}/g, c2);
    const n = ++counter; // keep ids (masks, gradients) unique when the same graphic is inlined many times
    return s.replace(/\bid="([^"]+)"/g, 'id="$1-' + n + '"').replace(/url\(#([^)]+)\)/g, 'url(#$1-' + n + ')');
  }
  function textMetrics(it, px) { const c = document.createElement('canvas').getContext('2d'); c.font = px + 'px "' + it.font + '", Impact, sans-serif'; if ('letterSpacing' in c) c.letterSpacing = it.spacing * px + 'px'; return c.measureText(it.text).width + 4; }
  function textSvg(it, o) {
    const px = 48, w = Math.ceil(textMetrics(it, px)), h = Math.round(px * 1.1), color = (o && o.color) || '#111417';
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + w + ' ' + h + '" width="' + w + '" height="' + h + '"><text x="' + w / 2 + '" y="' + h / 2 + '" text-anchor="middle" dominant-baseline="central" font-family="\'' + it.font + '\', Impact, sans-serif" font-size="' + px + '" letter-spacing="' + f2(it.spacing * px) + '" fill="' + color + '">' + esc(it.text) + '</text></svg>';
  }
  function svg(id, o) {
    o = o || {}; const it = typeof id === 'string' ? BY[id] : id; if (!it) throw new Error('Unknown graphic ' + id); if (it.mode === 'text') return textSvg(it, o);
    const w = it.vb[0], h = it.vb[1], k = (o.size || 128) / Math.max(w, h);
    return '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 ' + w + ' ' + h + '" width="' + f2(w * k) + '" height="' + f2(h * k) + '">' + markup(it, o) + '</svg>';
  }
  function textCanvas(it, o) {
    const px = Math.max(64, Math.min(256, (o && o.size) || 160)), c = document.createElement('canvas'), x = c.getContext('2d');
    x.font = px + 'px "' + it.font + '", Impact, sans-serif'; if ('letterSpacing' in x) x.letterSpacing = it.spacing * px + 'px';
    c.width = Math.ceil(x.measureText(it.text).width + 8); c.height = Math.ceil(px * 1.15);
    x.font = px + 'px "' + it.font + '", Impact, sans-serif'; if ('letterSpacing' in x) x.letterSpacing = it.spacing * px + 'px'; x.textAlign = 'center'; x.textBaseline = 'middle';
    x.fillStyle = (o && o.color) || '#111417'; x.fillText(it.text, c.width / 2, c.height / 2); return c;
  }
  function toImage(id, o) {
    const it = typeof id === 'string' ? BY[id] : id; if (it.mode === 'text') return Promise.resolve(textCanvas(it, o));
    return new Promise((res, rej) => { const im = new Image(); im.onload = () => res(im); im.onerror = rej; im.src = 'data:image/svg+xml;charset=utf-8,' + encodeURIComponent(svg(it, Object.assign({ size: 512 }, o))); });
  }
  async function draw(ctx, id, o) {
    o = o || {}; const img = await toImage(id, Object.assign({}, o, { size: Math.max(256, (o.size || 100) * 2) })), k = (o.size || 100) / Math.max(img.width, img.height);
    ctx.save(); ctx.translate(o.x || 0, o.y || 0); ctx.rotate(((o.rotation || 0) * Math.PI) / 180); if (o.flipX) ctx.scale(-1, 1);
    ctx.drawImage(img, (-img.width * k) / 2, (-img.height * k) / 2, img.width * k, img.height * k); ctx.restore();
  }

  /* ---------- storage ---------- */
  const store = { get(k, d) { try { const v = JSON.parse(localStorage.getItem(k)); return v == null ? d : v; } catch (e) { return d; } }, set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) { /* private mode */ } } };

  /* ---------- search ---------- */
  function search(q, list) {
    const toks = q.toLowerCase().split(/\s+/).filter(Boolean); if (!toks.length) return list || D.items;
    return (list || D.items).map(it => {
      const hay = (it.name + ' ' + it.tags.join(' ') + ' ' + CATNAME[it.cat] + ' ' + it.id).toLowerCase(); let score = 0;
      for (const t of toks) { if (!hay.includes(t)) return null; score += it.name.toLowerCase().startsWith(t) ? 3 : it.name.toLowerCase().includes(t) ? 2 : 1; } return { it, score };
    }).filter(Boolean).sort((a, b) => b.score - a.score).map(x => x.it);
  }

  /* ---------- UI ---------- */
  const IC = {
    search: '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
    x: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>',
    plus: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 5v14M5 12h14"/></svg>',
    star: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3.2l2.7 5.6 6.1.8-4.5 4.2 1.2 6.1L12 17l-5.5 2.9 1.2-6.1-4.5-4.2 6.1-.8z"/></svg>',
    check: '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="m5 12.5 4.5 4.5L19 7.5"/></svg>'
  };

  function mount(el, opts) {
    opts = Object.assign({ colors: DEFAULT_COLORS, color: '#111417', onAdd() {}, onUndo: null, onColor() {}, title: 'Graphics' }, opts || {});
    const st = { cat: 'all', q: '', color: opts.color, recent: store.get('zg.recent', []).filter(id => BY[id]), fav: store.get('zg.fav', []).filter(id => BY[id]) };
    el.classList.add('zg');
    el.innerHTML =
      '<div class="zg-head">' +
        '<div class="zg-title"><h2>' + esc(opts.title) + '</h2><span class="zg-count" id="zg-count" aria-live="polite"></span></div>' +
        '<div class="zg-search"><span class="zg-s-ic">' + IC.search + '</span><input class="zg-input" type="search" placeholder="Search wolf, bolt, crown, flag…" aria-label="Search graphics" autocomplete="off" spellcheck="false"><button class="zg-clear" type="button" aria-label="Clear search" hidden>' + IC.x + '</button></div>' +
        '<div class="zg-chips" role="group" aria-label="Categories"></div>' +
        '<div class="zg-colorrow"><span class="zg-label" id="zg-clabel">Colour</span><div class="zg-swatches" role="group" aria-labelledby="zg-clabel"></div></div>' +
        '<div class="zg-recent" hidden><span class="zg-label">Recent</span><div class="zg-recent-row"></div></div>' +
      '</div>' +
      '<div class="zg-body" tabindex="-1"></div>' +
      '<div class="zg-foot"><details><summary>Icon credits &amp; licences</summary><ul class="zg-credits"></ul></details></div>' +
      '<div class="zg-toast" role="status" aria-live="polite"></div>';
    const $ = s => el.querySelector(s), body = $('.zg-body'), input = $('.zg-input'), clear = $('.zg-clear'), chips = $('.zg-chips'), sw = $('.zg-swatches'), recentBox = $('.zg-recent'), recentRow = $('.zg-recent-row'), toast = $('.zg-toast'), count = $('#zg-count');
    $('.zg-credits').innerHTML = D.credits.map(c => '<li><a href="' + c.url + '" target="_blank" rel="noopener">' + esc(c.set) + '</a> · ' + esc(c.licence) + ' — ' + esc(c.note) + '</li>').join('');

    /* helpers */
    const tileDark = () => contrast(st.color, '#F4F1EA') < contrast(st.color, '#1B2025');
    const iconHTML = it => {
      if (it.mode === 'text') return '<span class="zg-word" style="color:' + st.color + ';font-family:\'' + it.font + '\',Impact,sans-serif;letter-spacing:' + it.spacing + 'em">' + esc(it.text) + '</span>';
      const wide = it.vb[0] / it.vb[1] > 1.6;
      return '<span class="zg-ic' + (wide ? ' wide' : '') + '"><svg viewBox="0 0 ' + it.vb[0] + ' ' + it.vb[1] + '" aria-hidden="true" focusable="false">' + markup(it, { color: st.color }) + '</svg></span>';
    };
    const cell = it => {
      const fav = st.fav.includes(it.id);
      return '<div class="zg-cell" role="listitem"><button class="zg-tile' + (it.mode === 'text' ? ' zg-tile-word' : '') + '" type="button" data-id="' + it.id + '" aria-label="Add ' + esc(it.name) + ' to design" title="' + esc(it.name) + '">' + iconHTML(it) + (it.mode === 'text' ? '' : '<span class="zg-name">' + esc(it.name) + '</span>') + '<span class="zg-plus" aria-hidden="true">' + IC.plus + '</span></button>' +
        '<button class="zg-fav" type="button" data-fav="' + it.id + '" aria-pressed="' + fav + '" aria-label="' + (fav ? 'Remove ' : 'Save ') + esc(it.name) + (fav ? ' from' : ' to') + ' favourites">' + IC.star + '</button></div>';
    };
    const section = (title, list, extra) => '<section class="zg-sec" aria-label="' + esc(title) + '"><h3 class="zg-h">' + esc(title) + '<span>' + list.length + '</span></h3><div class="zg-grid" role="list">' + list.map(cell).join('') + '</div>' + (extra || '') + '</section>';

    function renderChips() {
      const all = [['all', 'All'], ['fav', '★ Saved']].concat(D.cats.map(c => [c.id, c.name]));
      chips.innerHTML = all.map(([id, n]) => '<button type="button" class="zg-chip" data-cat="' + id + '" aria-pressed="' + (st.cat === id && !st.q) + '">' + esc(n) + '</button>').join('');
    }
    function renderSwatches() {
      sw.innerHTML = opts.colors.map(c => '<button type="button" class="zg-sw" data-color="' + c + '" style="--c:' + c + '" aria-label="Colour ' + c + '" aria-pressed="' + (c.toLowerCase() === st.color.toLowerCase()) + '"></button>').join('') +
        '<label class="zg-sw zg-sw-custom" title="Custom colour"><input type="color" value="' + st.color + '" aria-label="Custom colour"><span aria-hidden="true">+</span></label>';
    }
    function renderRecent() {
      recentBox.hidden = !st.recent.length;
      recentRow.innerHTML = st.recent.map(id => { const it = BY[id]; return '<button type="button" class="zg-mini" data-id="' + id + '" aria-label="Add ' + esc(it.name) + ' again" title="' + esc(it.name) + '">' + iconHTML(it) + '</button>'; }).join('');
      if (typeof fitWords === 'function') fitWords();
    }
    function fitWords() {   // shrink long wordmarks so they always fit their tile, whichever font loaded
      el.querySelectorAll('.zg-word').forEach(w => {
        w.style.fontSize = ''; const cw = w.clientWidth; if (!cw) return;
        if (w.scrollWidth > cw + 1) w.style.fontSize = (parseFloat(getComputedStyle(w).fontSize) * (cw / w.scrollWidth) * 0.97).toFixed(2) + 'px';
      });
    }
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(fitWords);
    function render() { renderChips(); renderSwatches(); renderRecent(); renderBody(); }
    function renderBody() {
      el.classList.toggle('zg-onlight', !tileDark()); el.classList.toggle('zg-ondark', tileDark());
      const q = st.q.trim(); let html = '', n = 0;
      if (q) {
        const res = search(q); n = res.length;
        html = res.length ? section('Results for “' + q + '”', res) : '<div class="zg-empty"><strong>No graphics match “' + esc(q) + '”</strong><p>Try one of these instead:</p><div class="zg-sugg">' + ['wolf', 'bolt', 'crown', 'flag', 'belt', 'flame', 'skull'].map(s => '<button type="button" class="zg-chip" data-q="' + s + '">' + s + '</button>').join('') + '</div></div>';
      } else if (st.cat === 'fav') {
        const l = st.fav.map(id => BY[id]); n = l.length;
        html = l.length ? section('Saved', l) : '<div class="zg-empty"><strong>No saved graphics yet</strong><p>Tap the ☆ on any graphic to keep it here.</p></div>';
      } else if (st.cat === 'all') {
        html = D.cats.map(c => { const l = D.items.filter(i => i.cat === c.id); n += l.length; return section(c.name, l); }).join('');
      } else { const l = D.items.filter(i => i.cat === st.cat); n = l.length; html = section(CATNAME[st.cat], l); }
      body.innerHTML = html; count.textContent = n + (n === 1 ? ' graphic' : ' graphics'); clear.hidden = !q; fitWords();
    }

    function showToast(msg, undo) {
      toast.innerHTML = '<span class="zg-t-ic">' + IC.check + '</span><span class="zg-t-msg">' + msg + '</span>' + (undo ? '<button type="button" class="zg-t-undo">Undo</button>' : '');
      toast.classList.add('show'); clearTimeout(showToast.t); showToast.t = setTimeout(() => toast.classList.remove('show'), 3600);
      if (undo) toast.querySelector('.zg-t-undo').onclick = () => { undo(); toast.classList.remove('show'); };
    }
    function payload(it) {
      const color = st.color, color2 = ink(color), base = { id: it.id, name: it.name, category: CATNAME[it.cat], mode: it.mode, color, color2, tags: it.tags, source: it.src };
      if (it.mode === 'text') return Object.assign(base, { type: 'text', text: it.text, font: it.font, spacing: it.spacing, svg: textSvg(it, { color }) });
      return Object.assign(base, { type: 'icon', vb: it.vb, aspect: it.vb[0] / it.vb[1], recolorable: it.mode !== 'fixed', svg: svg(it, { color, color2, size: 256 }) });
    }
    function add(id, node) {
      const it = BY[id]; if (!it) return; const p = payload(it);
      st.recent = [id].concat(st.recent.filter(x => x !== id)).slice(0, 8); store.set('zg.recent', st.recent); renderRecent();
      if (node) { node.classList.remove('zg-pop'); void node.offsetWidth; node.classList.add('zg-pop'); }
      opts.onAdd(p); showToast('Added <b>' + esc(it.name) + '</b>', opts.onUndo ? () => opts.onUndo(p) : null);
    }

    /* events */
    el.addEventListener('click', e => {
      const t = e.target.closest('[data-id]'); if (t && el.contains(t)) { add(t.dataset.id, t); return; }
      const fv = e.target.closest('[data-fav]'); if (fv) { const id = fv.dataset.fav; st.fav = st.fav.includes(id) ? st.fav.filter(x => x !== id) : [id].concat(st.fav); store.set('zg.fav', st.fav); const on = st.fav.includes(id); fv.setAttribute('aria-pressed', on); fv.setAttribute('aria-label', (on ? 'Remove ' : 'Save ') + BY[id].name + (on ? ' from' : ' to') + ' favourites'); showToast(on ? 'Saved <b>' + esc(BY[id].name) + '</b>' : 'Removed from saved'); if (st.cat === 'fav') render(); return; }
      const ch = e.target.closest('[data-cat]'); if (ch) { st.cat = ch.dataset.cat; st.q = ''; input.value = ''; render(); body.scrollTop = 0; return; }
      const sq = e.target.closest('[data-q]'); if (sq) { st.q = sq.dataset.q; input.value = st.q; render(); return; }
      const sc = e.target.closest('[data-color]'); if (sc) { setColor(sc.dataset.color); }
    });
    el.addEventListener('input', e => { if (e.target.matches('.zg-sw-custom input')) setColor(e.target.value, true); });
    input.addEventListener('input', () => { st.q = input.value; render(); });
    clear.addEventListener('click', () => { st.q = ''; input.value = ''; render(); input.focus(); });
    document.addEventListener('keydown', e => { if (e.key === '/' && !/input|textarea|select/i.test(document.activeElement.tagName) && el.offsetParent !== null) { e.preventDefault(); input.focus(); input.select(); } });
    body.addEventListener('keydown', e => {   // arrow-key navigation across the grid
      const cur = e.target.closest('.zg-tile'); if (!cur || !/^Arrow(Left|Right|Up|Down)$/.test(e.key)) return;
      const tiles = [...body.querySelectorAll('.zg-tile')], i = tiles.indexOf(cur), r = cur.getBoundingClientRect(); let next = null;
      if (e.key === 'ArrowRight') next = tiles[i + 1]; else if (e.key === 'ArrowLeft') next = tiles[i - 1];
      else { const down = e.key === 'ArrowDown', cx = r.left + r.width / 2; let best = 1e9; tiles.forEach(t => { const b = t.getBoundingClientRect(); if (down ? b.top > r.bottom - 4 : b.bottom < r.top + 4) { const d = Math.abs(b.left + b.width / 2 - cx) + Math.abs(down ? b.top - r.bottom : r.top - b.bottom) * 3; if (d < best) { best = d; next = t; } } }); }
      if (next) { e.preventDefault(); next.focus(); next.scrollIntoView({ block: 'nearest' }); }
    });
    function setColor(c, silent) {
      st.color = c; opts.onColor(c);
      if (silent) sw.querySelectorAll('[data-color]').forEach(b => b.setAttribute('aria-pressed', b.dataset.color.toLowerCase() === c.toLowerCase())); // keep the native picker open
      else renderSwatches();
      renderRecent(); renderBody();
    }

    render();
    return { setColor, getColor: () => st.color, focusSearch: () => input.focus(), setCategory: c => { st.cat = c; st.q = ''; render(); }, destroy() { el.innerHTML = ''; el.classList.remove('zg'); } };
  }

  window.ZamGraphics = { version: '1.0.0', data: D, items: D.items, categories: D.cats, get: id => BY[id], search, svg, markup, toImage, draw, mount, ink, contrast };
})();
