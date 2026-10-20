import re

with open('public/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. User's exact CSS rules
zt_css = '''
<style>
  :root{
    --canvas:#F4F1EA; --card:#FFFFFF; --recess:#EDE8DE; --border:#DFD9CC;
    --ink:#111417; --ink-2:#22282E; --muted:#6B675E;
    --cyan:#088395; --cyan-soft:#DDF3F6; --cyan-ink:#065d69;
    --gold:#C9A86A; --gold-soft:#F6EBD3;
    --ok:#107C41; --warn:#9A6A12; --warn-soft:#FBF0D8; --err:#C53030;
    --r-sm:6px; --r:8px; --r-lg:16px; --r-xl:24px;
    --shadow:0 14px 34px -6px rgba(17,20,23,.08),0 2px 6px -1px rgba(17,20,23,.04);
    --head:'Space Grotesk',system-ui,sans-serif;
    --body:'Plus Jakarta Sans',system-ui,sans-serif;
  }

  /* ============ ZamForward Custom Order Tracker Component ============ */
  .zt{max-width:1100px;margin:0 auto 80px;background:var(--card);border:1px solid var(--border);border-radius:var(--r-xl);box-shadow:var(--shadow);padding:clamp(20px,4vw,44px)}
  .zt *:focus-visible{outline:3px solid var(--cyan);outline-offset:2px;border-radius:var(--r-sm)}

  .zt-top{display:grid;grid-template-columns:1fr minmax(320px,440px);gap:28px 40px;align-items:end}
  .zt-eyebrow{display:inline-flex;align-items:center;gap:8px;font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--cyan-ink)}
  .zt-eyebrow i{width:8px;height:8px;border-radius:50%;background:var(--cyan);box-shadow:0 0 0 0 rgba(8,131,149,.5);animation:ping 2s infinite}
  .zt h2{font-family:var(--head);font-size:clamp(28px,4.2vw,40px);line-height:1.1;letter-spacing:-.02em;margin:10px 0 8px}
  .zt-sub{margin:0;color:var(--muted);font-size:15px;line-height:1.55;max-width:46ch}

  .zt-form label{display:block;font-size:12px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;margin-bottom:8px}
  .zt-field{display:flex;gap:8px}
  .zt-input{flex:1;display:flex;align-items:center;gap:10px;background:var(--canvas);border:1.5px solid var(--border);border-radius:var(--r);padding:0 14px;height:48px;transition:.15s}
  .zt-input:focus-within{border-color:var(--cyan);background:#fff;box-shadow:0 0 0 4px var(--cyan-soft)}
  .zt-input svg{flex:none;color:var(--muted)}
  .zt-input input{all:unset;flex:1;min-width:0;font:600 15px var(--body);letter-spacing:.02em;text-transform:uppercase}
  .zt-input input::placeholder{color:#a39e92;font-weight:500;text-transform:none;letter-spacing:0}
  .zt-btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;height:44px;padding:0 18px;border-radius:var(--r);border:1.5px solid transparent;font:700 14px var(--body);cursor:pointer;text-decoration:none;white-space:nowrap;transition:transform .12s,background .15s,border-color .15s}
  .zt-btn:hover{transform:translateY(-1px)}
  .zt-btn:active{transform:none}
  .zt-btn.primary{background:var(--ink);color:var(--canvas)}
  .zt-btn.primary:hover{background:var(--ink-2)}
  .zt-btn.cyan{background:var(--cyan);color:#fff}
  .zt-btn.cyan:hover{background:#0a7a8b}
  .zt-btn.ghost{background:transparent;border-color:var(--ink);color:var(--ink)}
  .zt-btn.ghost:hover{background:var(--recess)}
  .zt-btn.soft{background:var(--recess);color:var(--ink)}
  .zt-btn.soft:hover{background:#e5dfd2}
  .zt-btn[disabled]{opacity:.45;cursor:not-allowed;transform:none}
  .zt-form .zt-btn{height:48px}
  .zt-hint{margin:10px 0 0;font-size:13px;color:var(--muted);display:flex;flex-wrap:wrap;align-items:center;gap:8px}
  .zt-chip{font:600 12px var(--body);letter-spacing:.03em;background:var(--recess);border:1px solid var(--border);color:var(--ink);border-radius:999px;padding:5px 11px;cursor:pointer;transition:.15s}
  .zt-chip:hover{background:#fff;border-color:var(--cyan);color:var(--cyan-ink)}
  .zt-error{display:none;margin-top:10px;font-size:13px;font-weight:600;color:var(--err)}
  .zt-error.show{display:block}

  /* Result */
  .zt-result{margin-top:32px;border:1px solid var(--border);border-radius:var(--r-lg);background:linear-gradient(180deg,#faf8f3,#f4f1ea);overflow:hidden}
  .zt-result.in{animation:rise .35s ease both}

  .zt-head{display:grid;grid-template-columns:auto 1fr auto;gap:16px 20px;align-items:center;padding:22px 24px}
  .zt-badge{width:64px;height:64px;border-radius:16px;background:var(--ink);color:var(--canvas);display:grid;place-items:center;text-align:center;line-height:1}
  .zt-badge small{display:block;font:700 10px var(--body);letter-spacing:.14em;color:#9aa0a6;margin-bottom:4px}
  .zt-badge b{font:700 20px var(--head)}
  .zt-title{display:flex;flex-wrap:wrap;align-items:center;gap:8px 12px}
  .zt-title h3{margin:0;font:700 20px var(--head);letter-spacing:-.01em}
  .zt-pill{display:inline-flex;align-items:center;gap:6px;font:700 12px var(--body);letter-spacing:.05em;text-transform:uppercase;padding:5px 11px;border-radius:999px;background:var(--cyan-soft);color:var(--cyan-ink)}
  .zt-pill.wait{background:var(--warn-soft);color:var(--warn)}
  .zt-pill.done{background:#dcf1e4;color:var(--ok)}
  .zt-pill i{width:7px;height:7px;border-radius:50%;background:currentColor}
  .zt-meta{margin:6px 0 0;font-size:14px;color:var(--muted)}
  .zt-meta strong{color:var(--ink);font-weight:600}

  .zt-eta{text-align:right;background:#fff;border:1px solid var(--border);border-radius:var(--r-lg);padding:12px 18px;min-width:170px}
  .zt-eta span{display:block;font-size:11px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
  .zt-eta b{display:block;font:700 22px var(--head);letter-spacing:-.01em;margin-top:2px}
  .zt-eta em{display:block;font-style:normal;font-size:13px;font-weight:600;color:var(--cyan-ink);margin-top:2px}

  /* Status message */
  .zt-now{margin:0 24px;display:flex;gap:14px;align-items:flex-start;background:#fff;border:1px solid var(--border);border-left:4px solid var(--cyan);border-radius:var(--r);padding:14px 16px}
  .zt-now.wait{border-left-color:var(--gold);background:#fffdf7}
  .zt-now svg{flex:none;margin-top:2px;color:var(--cyan)}
  .zt-now.wait svg{color:var(--warn)}
  .zt-now h4{margin:0 0 2px;font:700 16px var(--head)}
  .zt-now p{margin:0;font-size:14px;line-height:1.5;color:var(--muted)}

  /* Stepper */
  .zt-steps{list-style:none;margin:0;padding:34px 24px 10px;display:grid;grid-template-columns:repeat(7,1fr);position:relative;--p:0%}
  .zt-steps::before,.zt-steps::after{content:"";position:absolute;top:53px;left:calc(24px + (100% - 48px)/14);height:6px;border-radius:6px}
  .zt-steps::before{right:calc(24px + (100% - 48px)/14);background:#e4dfd3}
  .zt-steps::after{width:calc((100% - 48px) * 6/7 * var(--p-n,0));background:linear-gradient(90deg,var(--cyan),#2bb4c7);transition:width .9s cubic-bezier(.2,.8,.2,1)}
  .zt-step{position:relative;z-index:1;text-align:center;padding:0 6px}
  .zt-dot{width:40px;height:40px;margin:0 auto 12px;border-radius:50%;display:grid;place-items:center;font:700 14px var(--body);background:#fff;border:2px solid #d4cebf;color:#a39e92;transition:.3s}
  .zt-step.done .zt-dot{background:var(--cyan);border-color:var(--cyan);color:#fff}
  .zt-step.now .zt-dot{background:#fff;border-color:var(--cyan);color:var(--cyan-ink);box-shadow:0 0 0 6px rgba(8,131,149,.16);animation:pulse 2s infinite}
  .zt-step.now.wait .zt-dot{border-color:var(--gold);color:var(--warn);box-shadow:0 0 0 6px rgba(201,168,106,.28);animation:none}
  .zt-step b{display:block;font:700 13px var(--body);line-height:1.25}
  .zt-step small{display:block;margin-top:3px;font-size:12px;line-height:1.35;color:var(--muted)}
  .zt-step time{display:block;margin-top:5px;font-size:11px;font-weight:700;letter-spacing:.03em;color:var(--cyan-ink)}
  .zt-step:not(.done):not(.now) b{color:#9a958a}
  .zt-step:not(.done):not(.now) small{color:#b3ada1}

  /* Details + actions */
  .zt-foot{display:grid;grid-template-columns:1.3fr 1fr;gap:16px;padding:18px 24px 24px}
  .zt-card{background:#fff;border:1px solid var(--border);border-radius:var(--r);padding:16px}
  .zt-card h5{margin:0 0 10px;font:700 11px var(--body);letter-spacing:.1em;text-transform:uppercase;color:var(--muted)}
  .zt-item{display:flex;gap:12px;align-items:center}
  .zt-thumb{width:54px;height:54px;flex:none;border-radius:var(--r);background:var(--ink);display:grid;place-items:center}
  .zt-item b{display:block;font-size:15px;line-height:1.3}
  .zt-item span{display:block;font-size:13px;color:var(--muted);margin-top:2px}
  .zt-kv{display:grid;grid-template-columns:auto 1fr;gap:6px 14px;margin:14px 0 0;font-size:13px}
  .zt-kv dt{color:var(--muted)}
  .zt-kv dd{margin:0;font-weight:600;text-align:right}
  .zt-track{display:inline-flex;align-items:center;gap:8px;font-family:ui-monospace,Menlo,Consolas,monospace;font-size:12.5px;background:var(--recess);border-radius:var(--r-sm);padding:4px 6px 4px 10px}
  .zt-track button{all:unset;cursor:pointer;display:inline-flex;padding:4px;border-radius:4px;color:var(--cyan-ink)}
  .zt-track button:hover{background:#fff}
  .zt-actions{display:flex;flex-direction:column;gap:10px;justify-content:center}
  .zt-actions .zt-btn{width:100%;justify-content:flex-start;height:48px}
  .zt-actions small{font-size:12px;color:var(--muted);line-height:1.45}

  /* Skeleton & empty */
  .zt-skel{margin-top:32px;border:1px solid var(--border);border-radius:var(--r-lg);padding:24px;display:none}
  .zt-skel.show{display:block}
  .zt-skel div{height:14px;border-radius:7px;background:linear-gradient(90deg,#eee9de 25%,#f8f5ee 50%,#eee9de 75%);background-size:200% 100%;animation:shimmer 1.2s infinite;margin-bottom:14px}
  .zt-empty{margin-top:32px;text-align:center;padding:36px 16px;border:1.5px dashed var(--border);border-radius:var(--r-lg);color:var(--muted);font-size:14px}
  .zt-toast{position:fixed;left:50%;bottom:24px;transform:translate(-50%,20px);background:var(--ink);color:var(--canvas);padding:10px 16px;border-radius:var(--r);font:600 13px var(--body);opacity:0;pointer-events:none;transition:.25s;z-index:9999}
  .zt-toast.show{opacity:1;transform:translate(-50%,0)}

  @keyframes ping{70%{box-shadow:0 0 0 8px rgba(8,131,149,0)}100%{box-shadow:0 0 0 0 rgba(8,131,149,0)}}
  @keyframes pulse{50%{box-shadow:0 0 0 10px rgba(8,131,149,.05)}}
  @keyframes rise{from{opacity:0;transform:translateY(10px)}}
  @keyframes shimmer{to{background-position:-200% 0}}

  /* Tablet */
  @media (max-width:900px){
    .zt-top{grid-template-columns:1fr}
    .zt-head{grid-template-columns:auto 1fr}
    .zt-eta{grid-column:1/-1;text-align:left;display:flex;align-items:baseline;justify-content:space-between;gap:12px}
    .zt-eta b{margin:0;font-size:18px}
    .zt-eta span,.zt-eta em{white-space:nowrap}
    .zt-foot{grid-template-columns:1fr}
  }
  /* Mobile: vertical timeline */
  @media (max-width:720px){
    .zt-head,.zt-foot{padding-left:16px;padding-right:16px}
    .zt-now{margin:0 16px}
    .zt-steps{grid-template-columns:1fr;padding:26px 16px 6px;gap:0}
    .zt-steps::before,.zt-steps::after{top:46px;left:35px;width:4px!important;right:auto;bottom:46px;height:auto}
    .zt-steps::before{width:4px}
    .zt-steps::after{width:4px!important;height:calc((100% - 92px) * var(--p-n,0));bottom:auto;background:linear-gradient(180deg,var(--cyan),#2bb4c7);transition:height .9s ease}
    .zt-step{display:grid;grid-template-columns:40px 1fr;gap:0 14px;text-align:left;padding:0 0 22px}
    .zt-dot{margin:0;grid-row:1/4}
    .zt-field{flex-direction:column}
    .zt-form .zt-btn{width:100%}
  }
</style>
'''

# 2. User's exact HTML Section
zt_html = '''<!-- 6. LIVE ORDER TRACKER (ZamForward Apex Combat Order Tracking) -->
  <section class="zt" id="tracking" aria-labelledby="zt-title">
    <div class="zt-top">
      <div>
        <span class="zt-eyebrow"><i></i> Live order tracking</span>
        <h2 id="zt-title">Where's my order?</h2>
        <p class="zt-sub">Enter your ZAM order ID to see production progress, your deadline, invoice and shipment — all in one place.</p>
      </div>

      <form class="zt-form" id="zt-form" novalidate>
        <label for="zt-id">Order ID</label>
        <div class="zt-field">
          <div class="zt-input">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>
            <input id="zt-id" name="id" placeholder="e.g. ZAM-401-26" autocomplete="off" spellcheck="false" aria-describedby="zt-err" maxlength="14" value="ZAM-401-26">
          </div>
          <button class="zt-btn primary" type="submit">Track order</button>
        </div>
        <p class="zt-error" id="zt-err" role="alert"></p>
        <p class="zt-hint">Try a demo order:
          <button type="button" class="zt-chip" data-id="ZAM-401-26">ZAM-401-26</button>
          <button type="button" class="zt-chip" data-id="ZAM-402-26">ZAM-402-26</button>
          <button type="button" class="zt-chip" data-id="ZAM-405-26">ZAM-405-26</button>
        </p>
      </form>
    </div>

    <div class="zt-skel" id="zt-skel" aria-hidden="true"><div style="width:40%"></div><div style="width:75%"></div><div style="width:100%;height:60px"></div></div>
    <div id="zt-out" aria-live="polite"></div>
  </section>
  <div class="zt-toast" id="zt-toast" role="status"></div>
'''

# 3. User's exact Script logic with live SQLite API integration
zt_script = '''
<script>
/* ---------- Order Tracker Engine (Live SQLite API + Fallback Cache) ---------- */
const ORDERS = {
  'ZAM-401-26': { customer:'Marcus Vance', stage:5, item:'Apex Sublimated Short-Sleeve Rashguard', variant:'L · Combat Cyan / Carbon Black', qty:15,
    deadline:'2026-11-15', total:'$ 850.00', paid:'50% deposit paid', carrier:'DHL Express', tracking:'DHL-EXP-992144810', url:'https://www.dhl.com/global-en/home/tracking.html?tracking-id=DHL-EXP-992144810',
    deposit_amount: 425.00,
    dates:{1:'Oct 12',2:'Oct 13',3:'Oct 15',4:'Oct 16',5:'Oct 19'} },
  'ZAM-402-26': { customer:'Elena Rostova', stage:2, item:'IBJJF Pro Gold Weave Kimono (Gi)', variant:'A2 · Blue Belt Rank', qty:3,
    deadline:null, total:'$ 405.00', paid:'Deposit due: $ 202.50', carrier:null, tracking:null,
    deposit_amount: 202.50,
    dates:{1:'Oct 18',2:'Oct 19'} },
  'ZAM-405-26': { customer:'Inferno Fight Team', stage:5, item:'Apex Combat Flex-Split MMA Shorts (CDR Custom)', variant:'L · Champion Gold', qty:15,
    deadline:'2026-11-20', total:'$ 720.00', paid:'50% deposit paid', carrier:'DHL Express', tracking:'DHL-EXP-889102', url:'https://www.dhl.com/global-en/home/tracking.html?tracking-id=DHL-EXP-889102',
    deposit_amount: 360.00,
    dates:{1:'Oct 19',2:'Oct 19',3:'Oct 20',4:'Oct 20',5:'Oct 20'} }
};

const STEPS = [
  ['Order placed','Received by ZamForward'],
  ['Invoice ready','Specs checked & priced'],
  ['Deposit cleared','50% payment confirmed'],
  ['Scheduled','Slot booked in the factory'],
  ['In production','Printing & sewing'],
  ['Shipped','On the way'],
  ['Delivered','At your door']
];

const NOW = {
  1:['We\'ve got your order','Our team is reviewing your designs and files. You\'ll get an invoice shortly.',false],
  2:['Your invoice is ready','Pay the 50% deposit and upload the transfer slip so we can schedule production.',true],
  3:['Deposit confirmed','Thanks! We\'re booking your production slot now.',false],
  4:['Production is scheduled','Your order is queued. We\'ll start printing very soon.',false],
  5:['Your gear is being made','Sublimation printing and sewing are underway. We\'ll notify you when it ships.',false],
  6:['Your order is on its way','It has left our factory. Use the tracking number to follow the parcel.',false],
  7:['Delivered — enjoy your gear!','Your order has arrived. Ready to run it back?',false]
};

/* ---------- Helpers ---------- */
const $ = s => document.querySelector(s);
const esc = s => String(s).replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
const ID_RE = /^ZAM-\d{3,}-\d{2}$/;
const ico = {
  check:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m5 12 5 5 9-10"/></svg>',
  info:'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 8h.01M11 12h1v5h1"/></svg>',
  clock:'<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg>',
  doc:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 3H7a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2V8z"/><path d="M14 3v5h5M9 13h6M9 17h4"/></svg>',
  up:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 16V4m0 0-4 4m4-4 4 4M4 16v3a1 1 0 0 0 1 1h14a1 1 0 0 0 1-1v-3"/></svg>',
  redo:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 3-6.7L3 8"/><path d="M3 3v5h5"/></svg>',
  truck:'<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M1 6h13v11H1zM14 10h4l4 3v4h-8"/><circle cx="6" cy="18" r="2"/><circle cx="17" cy="18" r="2"/></svg>',
  copy:'<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="9" y="9" width="12" height="12" rx="2"/><path d="M5 15V5a2 2 0 0 1 2-2h10"/></svg>',
  shirt:'<svg width="30" height="30" viewBox="0 0 24 24" fill="none" stroke="#C9A86A" stroke-width="1.6" stroke-linejoin="round"><path d="m8 3-5 3 2 5 3-1v11h8V10l3 1 2-5-5-3c-.5 1.5-2 2.5-4 2.5S8.5 4.5 8 3z"/></svg>'
};

function daysLeft(iso){ return Math.ceil((new Date(iso+'T00:00:00') - new Date().setHours(0,0,0,0))/864e5); }
function fmtDate(iso){ return new Date(iso+'T00:00:00').toLocaleDateString('en-GB',{day:'numeric',month:'short',year:'numeric'}); }

/* ---------- Render Function ---------- */
function render(id,o){
  const waiting = NOW[o.stage][2];
  const [nowTitle,nowText] = NOW[o.stage];
  const pill = o.stage===7 ? ['done','Delivered'] : waiting ? ['wait','Action needed'] : ['',STEPS[o.stage-1][0]];

  const steps = STEPS.map(([t,s],i)=>{
    const n=i+1, cls = n<o.stage?'done':n===o.stage?('now'+(waiting?' wait':'')):'';
    const sub = n===6 && o.carrier && n<=o.stage ? o.carrier : s;
    return `<li class="zt-step ${cls}" ${n===o.stage?'aria-current="step"':''}>
      <span class="zt-dot">${n<o.stage?ico.check:n}</span>
      <b>${esc(t)}</b><small>${esc(sub)}</small>
      ${o.dates && o.dates[n]?`<time>${esc(o.dates[n])}</time>`:''}
      <span class="sr-only" style="position:absolute;left:-9999px">${cls.includes('done')?'completed':cls?'current step':'upcoming'}</span>
    </li>`;}).join('');

  let eta='';
  if(o.stage===7) eta=`<div class="zt-eta"><span>Status</span><b>Delivered</b></div>`;
  else if(o.deadline && o.deadline!=='TBD' && o.deadline!=='Pending Review'){ const d=daysLeft(o.deadline);
    eta=`<div class="zt-eta"><span>${o.stage===6?'Expected by':'Ready by'}</span><b>${fmtDate(o.deadline)}</b><em>${d>0?d+' day'+(d>1?'s':'')+' to go':d===0?'Due today':'Slightly overdue — we\'re on it'}</em></div>`; }
  else eta=`<div class="zt-eta"><span>Deadline</span><b>Set after deposit</b><em>We confirm it once paid</em></div>`;

  // Contextual actions
  const acts=[];
  if(o.stage===2) acts.push(`<button class="zt-btn cyan" data-act="slip" data-id="${esc(id)}">${ico.up} Upload 50% payment slip</button>`);
  if(o.stage===6 && o.url) acts.push(`<a class="zt-btn cyan" href="${esc(o.url)}" target="_blank" rel="noopener">${ico.truck} Track parcel with ${esc(o.carrier)}</a>`);
  if(o.stage===7) acts.push(`<button class="zt-btn primary" data-act="reorder" data-id="${esc(id)}">${ico.redo} Reorder in 1 click</button>`);
  if(o.stage>=2) acts.push(`<button class="zt-btn ${acts.length?'soft':'primary'}" data-act="invoice" data-id="${esc(id)}">${ico.doc} View invoice</button>`);
  if(o.stage>=4 && o.stage<7) acts.push(`<button class="zt-btn ghost" data-act="reorder" data-id="${esc(id)}">${ico.redo} Reorder these items</button>`);
  if(o.stage===1) acts.push(`<small>We'll email you the moment your invoice is ready — nothing to do right now.</small>`);

  return `<article class="zt-result in" aria-label="Order ${esc(id)}">
    <div class="zt-head">
      <div class="zt-badge" aria-hidden="true"><div><small>ZAM</small><b>#${esc(id.split('-')[1])}</b></div></div>
      <div>
        <div class="zt-title"><h3>Order ${esc(id)}</h3><span class="zt-pill ${pill[0]}"><i></i>${esc(pill[1])}</span></div>
        <p class="zt-meta"><strong>${esc(o.customer)}</strong> · ${o.qty} items · ${esc(o.total)}</p>
      </div>
      ${eta}
    </div>

    <div class="zt-now ${waiting?'wait':''}">
      ${waiting?ico.clock:ico.info}
      <div><h4>${esc(nowTitle)}</h4><p>${esc(nowText)}</p></div>
    </div>

    <ol class="zt-steps" style="--p-n:${(o.stage-1)/6}">${steps}</ol>

    <div class="zt-foot">
      <div class="zt-card">
        <h5>Order summary</h5>
        <div class="zt-item">
          <div class="zt-thumb">${ico.shirt}</div>
          <div><b>${o.qty}× ${esc(o.item)}</b><span>${esc(o.variant)}</span></div>
        </div>
        <dl class="zt-kv">
          <dt>Payment</dt><dd>${esc(o.paid)}</dd>
          ${o.deadline && o.deadline!=='TBD' && o.deadline!=='Pending Review'?`<dt>Deadline</dt><dd>${fmtDate(o.deadline)}</dd>`:''}
          ${o.tracking?`<dt>Tracking</dt><dd><span class="zt-track">${esc(o.tracking)}<button type="button" data-copy="${esc(o.tracking)}" aria-label="Copy tracking number">${ico.copy}</button></span></dd>`:''}
        </dl>
      </div>
      <div class="zt-card zt-actions">
        <h5>What would you like to do?</h5>
        ${acts.join('')}
      </div>
    </div>
  </article>`;
}

/* ---------- Behaviour & Live API Wiring ---------- */
const form=$('#zt-form'), input=$('#zt-id'), out=$('#zt-out'), skel=$('#zt-skel'), err=$('#zt-err');
const toast=m=>{const t=$('#zt-toast');t.textContent=m;t.classList.add('show');clearTimeout(toast.t);toast.t=setTimeout(()=>t.classList.remove('show'),2200)};
const showErr=m=>{err.textContent=m;err.classList.toggle('show',!!m)};

// Stage mapping from SQLite status string to 1-7 stage number
function mapStatusToStage(status) {
  const s = (status || '').toLowerCase();
  if (s.includes('confirm')) return 1;
  if (s.includes('invoice sent') || s.includes('received')) return 2;
  if (s.includes('clear') || s.includes('deposit') || s.includes('slip')) return 3;
  if (s.includes('progress') || s.includes('scheduled')) return 4;
  if (s.includes('production')) return 5;
  if (s.includes('dispatch') || s.includes('ship')) return 6;
  if (s.includes('complete') || s.includes('deliver')) return 7;
  return 1;
}

function lookup(raw){
  const id=raw.trim().toUpperCase();
  showErr('');
  if(!id){ showErr('Please enter your order ID.'); input.focus(); return; }
  if(!ID_RE.test(id)){ showErr('That doesn\'t look right. Order IDs look like ZAM-401-26.'); input.focus(); return; }
  input.value=id; out.innerHTML=''; skel.classList.add('show');

  // Query live SQLite backend API
  fetch('/api/track/' + id)
    .then(r => {
      if (!r.ok) throw new Error('Not found in database');
      return r.json();
    })
    .then(dbOrder => {
      skel.classList.remove('show');
      window.currentTrackingOrder = dbOrder;
      
      const item0 = dbOrder.items && dbOrder.items[0] ? dbOrder.items[0] : {};
      const totalQty = (dbOrder.items || []).reduce((acc, it) => acc + (it.quantity || 1), 0) || 1;
      const stageNum = mapStatusToStage(dbOrder.status);

      // Construct dates mapping from status logs if available
      const datesMap = { 1: 'Oct 12' };
      if (dbOrder.status_logs) {
        dbOrder.status_logs.forEach(log => {
          const st = mapStatusToStage(log.new_status);
          datesMap[st] = log.timestamp ? log.timestamp.slice(5, 10).replace('-', '/') : 'Recent';
        });
      }

      const o = {
        customer: dbOrder.customer_name || 'Customer Athlete',
        stage: stageNum,
        item: item0.product_name || 'Apex Combat Gear',
        variant: `${item0.size || 'L'} · ${item0.color || 'Standard'}`,
        qty: totalQty,
        deadline: dbOrder.production_deadline,
        total: `$ ${parseFloat(dbOrder.total_amount || 0).toFixed(2)}`,
        paid: dbOrder.paid_amount > 0 ? `$ ${parseFloat(dbOrder.paid_amount).toFixed(2)} deposit paid` : (dbOrder.invoice ? `Deposit due: $ ${parseFloat(dbOrder.invoice.deposit_required).toFixed(2)}` : '50% deposit required'),
        carrier: dbOrder.courier || (dbOrder.tracking_number ? 'DHL Express' : null),
        tracking: dbOrder.tracking_number || null,
        url: dbOrder.tracking_number ? `https://www.dhl.com/global-en/home/tracking.html?tracking-id=${dbOrder.tracking_number}` : null,
        deposit_amount: dbOrder.invoice ? dbOrder.invoice.deposit_required : (dbOrder.total_amount * 0.5),
        dates: datesMap
      };

      out.innerHTML = render(id, o);
    })
    .catch(() => {
      // Fallback to local demo dictionary if offline
      skel.classList.remove('show');
      const o = ORDERS[id];
      if (o) {
        out.innerHTML = render(id, o);
      } else {
        out.innerHTML = `<div class="zt-empty"><strong style="display:block;color:var(--ink);font-size:16px;margin-bottom:4px">No order found for ${esc(id)}</strong>Double-check the ID in your confirmation email, or contact our team and we'll help.</div>`;
      }
    });
}

// Global lookupOrder hook so any button on the page triggers the new UI
window.lookupOrder = lookup;

// Wire events
form.addEventListener('submit',e=>{e.preventDefault();lookup(input.value)});
document.querySelectorAll('.zt-chip').forEach(b=>b.addEventListener('click',()=>{input.value=b.dataset.id;lookup(b.dataset.id)}));

out.addEventListener('click',e=>{
  const c=e.target.closest('[data-copy]');
  if(c){navigator.clipboard?.writeText(c.dataset.copy);toast('Tracking number copied');return}
  const a=e.target.closest('[data-act]');
  if(a){ 
    const action = a.dataset.act;
    const orderId = a.dataset.id || input.value;
    if (action === 'slip') {
      openSlipModal(orderId, 425);
    } else if (action === 'invoice') {
      openInvoiceModal(orderId);
    } else if (action === 'reorder') {
      reorderFast(orderId);
    }
  }
});

// Pre-load default order on page load
setTimeout(() => lookup('ZAM-401-26'), 200);
</script>
'''

# 1. Insert CSS into <head>
if '.zt{' not in html:
    html = html.replace('</head>', zt_css + '\n</head>')

# 2. Replace the old tracking section with the user's exact section
pos_track = html.find('<!-- 6. LIVE ORDER TRACKER')
if pos_track == -1:
    pos_track = html.find('id="tracking"')
    pos_track = html.rfind('<section', 0, pos_track)

end_track = html.find('</section>', pos_track) + 10

html = html[:pos_track] + zt_html + html[end_track:]

# 3. Add the tracker script right before </body>
html = html.replace('</body></html>', zt_script + '\n</body></html>')

with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Custom Order Tracker user interface integrated successfully.")
