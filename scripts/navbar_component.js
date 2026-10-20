const $=(s,r=document)=>r.querySelector(s), $$=(s,r=document)=>[...r.querySelectorAll(s)];



/* Announcement rotator */

(()=>{const m=$$('#ann p');let i=0;setInterval(()=>{m[i].classList.remove('on');i=(i+1)%m.length;m[i].classList.add('on')},4200)})();



/* Sticky shrink */

const hdr=$('#hdr');addEventListener('scroll',()=>hdr.classList.toggle('stuck',scrollY>40),{passive:true});



/* Mega menu (hover on desktop, click/keyboard everywhere) */

const shopBtn=$('#shopBtn'),mega=$('#mega'),navrow=$('.navrow');navrow.style.position='relative';

let mt,pinned=false;const openMega=o=>{clearTimeout(mt);if(!o)pinned=false;mega.classList.toggle('open',o);shopBtn.setAttribute('aria-expanded',o)};

/* hover previews the menu; a click pins it open (click again to close) */

shopBtn.addEventListener('click',()=>{if(mega.classList.contains('open')&&pinned)openMega(false);else{openMega(true);pinned=true}});

shopBtn.addEventListener('mouseenter',()=>matchMedia('(hover:hover)').matches&&openMega(true));

[shopBtn,mega].forEach(e=>e.addEventListener('mouseleave',()=>{if(!pinned)mt=setTimeout(()=>openMega(false),140)}));

mega.addEventListener('mouseenter',()=>clearTimeout(mt));



/* Account menu */

const aBtn=$('#acctBtn'),aMenu=$('#acctMenu');

aBtn.addEventListener('click',e=>{e.stopPropagation();const o=!aMenu.classList.contains('open');aMenu.classList.toggle('open',o);aBtn.setAttribute('aria-expanded',o)});



/* Search suggestions */

const q=$('#q'),sg=$('#sugg');

const PRODUCTS=[['Apex Stealth Compression Rashguard','Rashguards'],['Hybrid Pro MMA Fight Shorts','MMA'],['Imperial Pearl Weave BJJ Gi','BJJ'],['Bangkok Retro Muay Thai Shorts','Muay Thai'],['Ranked BJJ Long Sleeve Rashguard','BJJ'],['Sub-Zero Thermal Grappling Spats','Compression'],['Custom Sublimated Team Kit','Custom']];

const hl=(t,s)=>{const i=t.toLowerCase().indexOf(s.toLowerCase());return i<0?t:t.slice(0,i)+'<mark>'+t.slice(i,i+s.length)+'</mark>'+t.slice(i+s.length)};

function paint(){

  const v=q.value.trim();let h='';

  if(!v){h=`<h6>Popular searches</h6><div class="chips"><a href="#">Rashguards</a><a href="#">BJJ gi</a><a href="#">Fight shorts</a><a href="#">Muay Thai</a><a href="#">Team kits</a></div><h6>Trending</h6>`+PRODUCTS.slice(0,3).map(p=>`<a href="#" role="option"><svg class="i"><use href="#i-search"/></svg>${p[0]}<em>${p[1]}</em></a>`).join('')}

  else{const r=PRODUCTS.filter(p=>p[0].toLowerCase().includes(v.toLowerCase())||p[1].toLowerCase().includes(v.toLowerCase()));

    h=r.length?`<h6>Products</h6>`+r.map(p=>`<a href="#" role="option"><svg class="i"><use href="#i-tee"/></svg><span>${hl(p[0],v)}</span><em>${p[1]}</em></a>`).join(''):`<h6>No matches</h6><a href="#"><svg class="i"><use href="#i-spark"/></svg>Design a custom "${v.replace(/[<>&]/g,'')}" with AI Studio</a>`}

  sg.innerHTML=h;sg.classList.add('open');q.setAttribute('aria-expanded','true')}

q.addEventListener('focus',paint);q.addEventListener('input',paint);



/* Drawers */

const scrim=$('#scrim');

function drawer(el,o){el.classList.toggle('open',o);el.setAttribute('aria-hidden',!o);scrim.classList.toggle('on',o);document.body.style.overflow=o?'hidden':''}

$('#cartBtn').addEventListener('click',()=>drawer($('#cart'),true));

$('#burger').addEventListener('click',()=>drawer($('#mnav'),true));

const closeAll=()=>$$('.drawer').forEach(d=>drawer(d,false));

scrim.addEventListener('click',closeAll);$$('[data-close]').forEach(b=>b.addEventListener('click',closeAll));



/* Global dismiss */

document.addEventListener('click',e=>{

  if(!e.target.closest('.rel')){aMenu.classList.remove('open');aBtn.setAttribute('aria-expanded','false')}

  if(!e.target.closest('.search')){sg.classList.remove('open');q.setAttribute('aria-expanded','false')}

  if(!e.target.closest('.has-mega,.mega'))openMega(false);

});

document.addEventListener('keydown',e=>{if(e.key==='Escape'){closeAll();openMega(false);aMenu.classList.remove('open');sg.classList.remove('open')}});

document.addEventListener('keydown',e=>{if(e.key==='/'&&!/input|textarea/i.test(document.activeElement.tagName)){e.preventDefault();q.focus()}});

$$('a[href="#"]').forEach(a=>a.addEventListener('click',e=>e.preventDefault()));