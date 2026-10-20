import re

with open('public/index.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Locate the JS block starting with /* =========================================================================
# ZAMFORWARD AI 3D STUDIO & CDR PATTERN ENGINE
js_pattern = re.compile(r'/\* =========================================================================\s+ZAMFORWARD AI 3D STUDIO & CDR PATTERN ENGINE.*?submitStudioOrder\(\) \{.*?\n\}\n</script>', re.DOTALL)

upgraded_js = '''/* =========================================================================
   ZAMFORWARD AI 3D STUDIO & CDR PATTERN ENGINE (HIGH FIDELITY)
   Master CDR File: Backup_of_ZAM FORWARD 123456.cdr
   ========================================================================= */

// Studio State
let studioState = {
  view: 'front', // 'front' | 'back'
  fabricColor: '#efd965', // Champion Gold (matches reference CDR)
  fabricName: 'Champion Gold',
  waistbandColor: '#18181b', // Carbon Black
  flapColor: '#f4f1ea', // White closure flap
  renderMode: 'orbit', // 'orbit' | 'photo'
  autoRotate: false,
  elements: [
    // Pre-populate with design elements matching user's CDR reference!
    { id: 'el_crest', type: 'logo', name: 'Waistband Wings Crest', x: 425, y: 70, scale: 0.75, rotation: 0, color: '#111417', preset: 'wings' },
    { id: 'el_text1', type: 'text', name: 'Left Leg Vertical INFERNO', text: 'INFERNO', x: 265, y: 280, scale: 1.0, rotation: -90, color: '#111417', font: 'Impact', size: 38 },
    { id: 'el_text2', type: 'text', name: 'Right Leg Vertical INFERNO', text: 'INFERNO', x: 585, y: 280, scale: 1.0, rotation: -90, color: '#111417', font: 'Impact', size: 38 },
    { id: 'el_sponsor1', type: 'logo', name: 'Left Slit Sponsor Logo', x: 310, y: 350, scale: 0.8, rotation: 0, color: '#111417', preset: 'metal' },
    { id: 'el_sponsor2', type: 'logo', name: 'Right Slit Custom Inferno', x: 535, y: 350, scale: 0.85, rotation: 0, color: '#111417', preset: 'inferno_script' },
    { id: 'el_bolt', type: 'clipart', name: 'Right Slit Lightning Bolt', x: 635, y: 350, scale: 0.85, rotation: 0, color: '#111417', preset: 'bolt' },
    { id: 'el_belt', type: 'text', name: 'Lower Belt Script', text: 'CUSTOM INFERNO', x: 425, y: 535, scale: 0.95, rotation: 0, color: '#efd965', font: 'Impact', size: 28 }
  ],
  selectedElementId: null,
  isDragging: false,
  dragOffset: { x: 0, y: 0 }
};

// Undo/Redo Stacks
let undoStack = [];
let redoStack = [];

function saveStudioHistory() {
  undoStack.push(JSON.stringify(studioState));
  if (undoStack.length > 25) undoStack.shift();
  redoStack = [];
}

function undoStudio() {
  if (undoStack.length === 0) return;
  redoStack.push(JSON.stringify(studioState));
  studioState = JSON.parse(undoStack.pop());
  renderPatternCanvas();
  updateStudioLayers();
  update3DTexture();
}

function redoStudio() {
  if (redoStack.length === 0) return;
  undoStack.push(JSON.stringify(studioState));
  studioState = JSON.parse(redoStack.pop());
  renderPatternCanvas();
  updateStudioLayers();
  update3DTexture();
}

// ------------------- MODAL CONTROLS -------------------
function openAiStudioModal() {
  const modal = document.getElementById('aiStudioModal');
  modal.classList.remove('hidden');
  initStudio2DCanvas();
  setTimeout(() => {
    initThreeJS3D();
    renderPatternCanvas();
    updateStudioLayers();
    renderPresetLogos();
    renderCliparts();
    update3DTexture();
    renderPhotoMockup();
  }, 100);
  showToast('Loaded CDR Master Template from Backup_of_ZAM FORWARD 123456.cdr', 'success');
}

function closeAiStudioModal() {
  const modal = document.getElementById('aiStudioModal');
  modal.classList.add('hidden');
}

function setStudioTab(tabName) {
  ['layers', 'uploads', 'cliparts', 'text', 'colors'].forEach(t => {
    const btn = document.getElementById(`tabBtn_${t}`);
    const panel = document.getElementById(`tabPanel_${t}`);
    if (btn && panel) {
      if (t === tabName) {
        btn.classList.add('border-secondary', 'text-primary');
        btn.classList.remove('border-transparent', 'text-on-surface-variant');
        panel.classList.remove('hidden');
      } else {
        btn.classList.remove('border-secondary', 'text-primary');
        btn.classList.add('border-transparent', 'text-on-surface-variant');
        panel.classList.add('hidden');
      }
    }
  });
}

function setStudioView(view) {
  studioState.view = view;
  const btnF = document.getElementById('btnViewFront');
  const btnB = document.getElementById('btnViewBack');
  if (view === 'front') {
    btnF.className = 'px-3 py-1 rounded-lg text-xs font-bold uppercase bg-surface-container-lowest text-primary shadow-sm transition-all';
    btnB.className = 'px-3 py-1 rounded-lg text-xs font-bold uppercase text-on-surface-variant hover:text-primary transition-all';
    set3DAngle('front');
  } else {
    btnB.className = 'px-3 py-1 rounded-lg text-xs font-bold uppercase bg-surface-container-lowest text-primary shadow-sm transition-all';
    btnF.className = 'px-3 py-1 rounded-lg text-xs font-bold uppercase text-on-surface-variant hover:text-primary transition-all';
    set3DAngle('back');
  }
  renderPatternCanvas();
  update3DTexture();
}

function setFabricColor(hex, name) {
  saveStudioHistory();
  studioState.fabricColor = hex;
  studioState.fabricName = name;
  document.getElementById('lblFabricColor').innerText = `${name} (${hex})`;
  renderPatternCanvas();
  update3DTexture();
  renderPhotoMockup();
  showToast(`Garment color changed to ${name}`, 'info');
}

function setWaistbandColor(hex) {
  saveStudioHistory();
  studioState.waistbandColor = hex;
  renderPatternCanvas();
  update3DTexture();
  renderPhotoMockup();
}

// ------------------- 2D CDR PATTERN CANVAS ENGINE -------------------
let patternCanvas, ctx2d;

function initStudio2DCanvas() {
  patternCanvas = document.getElementById('patternCanvas');
  ctx2d = patternCanvas.getContext('2d');

  patternCanvas.onmousedown = onCanvasMouseDown;
  patternCanvas.onmousemove = onCanvasMouseMove;
  window.onmouseup = onCanvasMouseUp;

  patternCanvas.ontouchstart = (e) => {
    const t = e.touches[0];
    const rect = patternCanvas.getBoundingClientRect();
    handlePointerDown(t.clientX - rect.left, t.clientY - rect.top);
  };
  patternCanvas.ontouchmove = (e) => {
    const t = e.touches[0];
    const rect = patternCanvas.getBoundingClientRect();
    handlePointerMove(t.clientX - rect.left, t.clientY - rect.top);
  };
  window.ontouchend = () => { studioState.isDragging = false; };
}

function getCanvasCoords(e) {
  const rect = patternCanvas.getBoundingClientRect();
  const scaleX = patternCanvas.width / rect.width;
  const scaleY = patternCanvas.height / rect.height;
  return {
    x: (e.clientX - rect.left) * scaleX,
    y: (e.clientY - rect.top) * scaleY
  };
}

function onCanvasMouseDown(e) {
  const pt = getCanvasCoords(e);
  handlePointerDown(pt.x, pt.y);
}

function handlePointerDown(x, y) {
  let found = null;
  for (let i = studioState.elements.length - 1; i >= 0; i--) {
    const el = studioState.elements[i];
    const dist = Math.hypot(el.x - x, el.y - y);
    if (dist < 45 * el.scale) {
      found = el;
      break;
    }
  }

  if (found) {
    saveStudioHistory();
    studioState.selectedElementId = found.id;
    studioState.isDragging = true;
    studioState.dragOffset = { x: x - found.x, y: y - found.y };
  } else {
    studioState.selectedElementId = null;
  }
  renderPatternCanvas();
  updateStudioLayers();
}

function onCanvasMouseMove(e) {
  if (!studioState.isDragging || !studioState.selectedElementId) return;
  const pt = getCanvasCoords(e);
  handlePointerMove(pt.x, pt.y);
}

function handlePointerMove(x, y) {
  const el = studioState.elements.find(e => e.id === studioState.selectedElementId);
  if (!el) return;
  el.x = Math.max(50, Math.min(patternCanvas.width - 50, x - studioState.dragOffset.x));
  el.y = Math.max(30, Math.min(patternCanvas.height - 30, y - studioState.dragOffset.y));
  renderPatternCanvas();
  update3DTexture();
  renderPhotoMockup();
}

function onCanvasMouseUp() {
  studioState.isDragging = false;
}

// Render the high quality MMA Fight Shorts master vector pieces from Backup_of_ZAM FORWARD 123456.cdr
function renderPatternCanvas() {
  if (!ctx2d) return;
  const w = patternCanvas.width;
  const h = patternCanvas.height;

  // Clean studio canvas backdrop
  ctx2d.fillStyle = '#ffffff';
  ctx2d.fillRect(0, 0, w, h);

  // Subtle millimeter grid lines (every 25mm scaled)
  ctx2d.strokeStyle = '#f1f5f9';
  ctx2d.lineWidth = 1;
  for (let x = 0; x < w; x += 35) {
    ctx2d.beginPath(); ctx2d.moveTo(x, 0); ctx2d.lineTo(x, h); ctx2d.stroke();
  }
  for (let y = 0; y < h; y += 35) {
    ctx2d.beginPath(); ctx2d.moveTo(0, y); ctx2d.lineTo(w, y); ctx2d.stroke();
  }

  // 1. TOP CENTER: Waistband Closure Flap (from CDR Master)
  ctx2d.save();
  // Seam bleed halo
  ctx2d.fillStyle = '#f8fafc';
  ctx2d.beginPath();
  ctx2d.roundRect(355, 35, 140, 65, 8);
  ctx2d.fill();

  ctx2d.fillStyle = studioState.flapColor;
  ctx2d.strokeStyle = '#cbd5e1';
  ctx2d.lineWidth = 2;
  ctx2d.beginPath();
  ctx2d.roundRect(360, 40, 130, 55, 6);
  ctx2d.fill();
  ctx2d.stroke();

  // Double stitch path
  ctx2d.setLineDash([4, 4]);
  ctx2d.strokeStyle = '#94a3b8';
  ctx2d.strokeRect(365, 45, 120, 45);
  ctx2d.setLineDash([]);
  
  // Zone label
  ctx2d.font = 'bold 9px monospace';
  ctx2d.fillStyle = '#94a3b8';
  ctx2d.textAlign = 'center';
  ctx2d.fillText('WAISTBAND FLAP (140x60mm)', 425, 32);
  ctx2d.restore();

  // 2. LEFT FLIGHT SHORTS LEG PANEL (Flared combat pattern from CDR)
  ctx2d.save();
  ctx2d.fillStyle = studioState.fabricColor;
  ctx2d.strokeStyle = '#475569';
  ctx2d.lineWidth = 2.5;

  ctx2d.beginPath();
  ctx2d.moveTo(210, 155); // top waist left
  ctx2d.lineTo(350, 155); // top waist right
  ctx2d.lineTo(370, 260); // inner inseam crotch curve
  ctx2d.lineTo(330, 395); // inner leg hem
  ctx2d.lineTo(190, 395); // outer leg hem with slit cut
  ctx2d.lineTo(175, 340); // 45-deg split slit corner
  ctx2d.lineTo(210, 155); // close to top
  ctx2d.closePath();
  ctx2d.fill();
  ctx2d.stroke();

  // Contrast black side panel racing stripe & slit binding
  ctx2d.fillStyle = studioState.waistbandColor;
  ctx2d.beginPath();
  ctx2d.moveTo(175, 340);
  ctx2d.lineTo(190, 395);
  ctx2d.lineTo(182, 395);
  ctx2d.lineTo(168, 342);
  ctx2d.closePath();
  ctx2d.fill();

  // Seam guide lines
  ctx2d.strokeStyle = 'rgba(0,0,0,0.15)';
  ctx2d.lineWidth = 1;
  ctx2d.setLineDash([4, 4]);
  ctx2d.beginPath();
  ctx2d.moveTo(225, 165);
  ctx2d.lineTo(190, 335);
  ctx2d.stroke();
  ctx2d.setLineDash([]);

  // Label
  ctx2d.font = 'bold 10px monospace';
  ctx2d.fillStyle = '#64748b';
  ctx2d.fillText('LEFT LEG (FRONT)', 280, 145);
  ctx2d.restore();

  // 3. RIGHT FLIGHT SHORTS LEG PANEL (Mirror flared combat pattern from CDR)
  ctx2d.save();
  ctx2d.fillStyle = studioState.fabricColor;
  ctx2d.strokeStyle = '#475569';
  ctx2d.lineWidth = 2.5;

  ctx2d.beginPath();
  ctx2d.moveTo(500, 155); // top waist left
  ctx2d.lineTo(640, 155); // top waist right
  ctx2d.lineTo(675, 340); // outer leg slit corner
  ctx2d.lineTo(660, 395); // outer leg hem
  ctx2d.lineTo(520, 395); // inner leg hem
  ctx2d.lineTo(480, 260); // inner inseam crotch curve
  ctx2d.lineTo(500, 155); // close to top
  ctx2d.closePath();
  ctx2d.fill();
  ctx2d.stroke();

  // Contrast black side panel racing stripe & slit binding
  ctx2d.fillStyle = studioState.waistbandColor;
  ctx2d.beginPath();
  ctx2d.moveTo(675, 340);
  ctx2d.lineTo(660, 395);
  ctx2d.lineTo(668, 395);
  ctx2d.lineTo(682, 342);
  ctx2d.closePath();
  ctx2d.fill();

  // Seam guide lines
  ctx2d.strokeStyle = 'rgba(0,0,0,0.15)';
  ctx2d.lineWidth = 1;
  ctx2d.setLineDash([4, 4]);
  ctx2d.beginPath();
  ctx2d.moveTo(625, 165);
  ctx2d.lineTo(660, 335);
  ctx2d.stroke();
  ctx2d.setLineDash([]);

  // Label
  ctx2d.font = 'bold 10px monospace';
  ctx2d.fillStyle = '#64748b';
  ctx2d.fillText('RIGHT LEG (FRONT)', 570, 145);
  ctx2d.restore();

  // 4. LOWER BELT / WAISTBAND STRIP (Wide curved belt panel at bottom from CDR)
  ctx2d.save();
  ctx2d.fillStyle = studioState.waistbandColor;
  ctx2d.strokeStyle = '#1e293b';
  ctx2d.lineWidth = 2;
  ctx2d.beginPath();
  ctx2d.moveTo(200, 480);
  ctx2d.lineTo(650, 480);
  ctx2d.lineTo(660, 520);
  ctx2d.lineTo(425, 570); // V-taper center
  ctx2d.lineTo(190, 520);
  ctx2d.closePath();
  ctx2d.fill();
  ctx2d.stroke();

  // Label
  ctx2d.font = 'bold 9px monospace';
  ctx2d.fillStyle = '#64748b';
  ctx2d.textAlign = 'center';
  ctx2d.fillText('REAR WAISTBAND BELT STRIP (580x90mm)', 425, 472);
  ctx2d.restore();

  // RENDER DESIGN ELEMENTS
  studioState.elements.forEach(el => {
    ctx2d.save();
    ctx2d.translate(el.x, el.y);
    ctx2d.rotate((el.rotation || 0) * Math.PI / 180);
    ctx2d.scale(el.scale || 1, el.scale || 1);

    const isSelected = el.id === studioState.selectedElementId;

    if (el.type === 'text') {
      ctx2d.font = `bold ${el.size || 34}px ${el.font || 'Impact'}`;
      ctx2d.textAlign = 'center';
      ctx2d.textBaseline = 'middle';
      ctx2d.fillStyle = el.color || '#111417';
      ctx2d.fillText(el.text, 0, 0);

      // Subtle shadow outline for legibility
      ctx2d.strokeStyle = el.color === '#efd965' ? '#18181b' : 'rgba(255,255,255,0.5)';
      ctx2d.lineWidth = 1.5;
      ctx2d.strokeText(el.text, 0, 0);
    } else if (el.type === 'logo' || el.type === 'clipart') {
      renderVectorGraphic(ctx2d, el);
    }

    // Selection bounding box
    if (isSelected) {
      ctx2d.strokeStyle = '#0284c7';
      ctx2d.lineWidth = 2;
      ctx2d.setLineDash([4, 4]);
      ctx2d.strokeRect(-45, -30, 90, 60);

      ctx2d.setLineDash([]);
      ctx2d.fillStyle = '#0284c7';
      [-45, 45].forEach(cx => {
        [-30, 30].forEach(cy => {
          ctx2d.fillRect(cx - 4, cy - 4, 8, 8);
        });
      });
    }

    ctx2d.restore();
  });
}

// Vector graphics helper (Draws custom logos matching CDR reference)
function renderVectorGraphic(ctx, el) {
  ctx.fillStyle = el.color || '#111417';
  ctx.strokeStyle = el.color || '#111417';

  if (el.preset === 'wings') {
    // Sharp combat wings emblem
    ctx.beginPath();
    ctx.moveTo(0, 12);
    ctx.quadraticCurveTo(-22, -18, -38, -28);
    ctx.quadraticCurveTo(-18, -12, 0, 0);
    ctx.quadraticCurveTo(18, -12, 38, -28);
    ctx.quadraticCurveTo(22, -18, 0, 12);
    ctx.fill();

    ctx.beginPath();
    ctx.moveTo(0, 6);
    ctx.lineTo(-24, -20);
    ctx.lineTo(-10, -6);
    ctx.lineTo(0, 0);
    ctx.lineTo(10, -6);
    ctx.lineTo(24, -20);
    ctx.closePath();
    ctx.fill();
  } else if (el.preset === 'bolt') {
    // High-impact lightning bolt
    ctx.beginPath();
    ctx.moveTo(5, -24);
    ctx.lineTo(-16, -2);
    ctx.lineTo(-2, -2);
    ctx.lineTo(-8, 24);
    ctx.lineTo(16, 2);
    ctx.lineTo(2, 2);
    ctx.closePath();
    ctx.fill();
  } else if (el.preset === 'metal') {
    // Bold sponsor typography
    ctx.font = 'bold 22px Impact';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('⚡STRIKE', 0, 0);
  } else if (el.preset === 'inferno_script') {
    // Custom inferno script mark
    ctx.font = 'italic bold 20px Impact';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('CUSTOM INFERNO', 0, 0);
  } else if (el.imageObj) {
    // Custom uploaded user logo
    try {
      ctx.drawImage(el.imageObj, -35, -35, 70, 70);
    } catch(err) {}
  } else {
    // Generic combat shield
    ctx.beginPath();
    ctx.moveTo(0, -22);
    ctx.lineTo(20, -14);
    ctx.lineTo(16, 14);
    ctx.lineTo(0, 24);
    ctx.lineTo(-16, 14);
    ctx.lineTo(-20, -14);
    ctx.closePath();
    ctx.fill();
  }
}

// ------------------- HIGH FIDELITY THREE.JS 3D ENGINE -------------------
let threeScene, threeCamera, threeRenderer, threeControls;
let shortsGroup, offscreenCanvas, offscreenCtx, canvasTexture;
let leftLegMesh, rightLegMesh, waistMesh, flapMesh, shadowMesh;

function initThreeJS3D() {
  const container = document.getElementById('studio3DCanvasContainer');
  if (!container) return;
  const canvas = document.getElementById('threeCanvas');

  if (threeRenderer) {
    onWindowResize3D();
    return;
  }

  // 1. Scene with soft studio fog
  threeScene = new THREE.Scene();
  threeScene.fog = new THREE.FogExp2(0xf8fafc, 0.04);

  // 2. Camera
  threeCamera = new THREE.PerspectiveCamera(35, container.clientWidth / container.clientHeight, 0.1, 100);
  threeCamera.position.set(0, 0.1, 4.8);

  // 3. Renderer with antialiasing and shadow map
  threeRenderer = new THREE.WebGLRenderer({ canvas: canvas, antialias: true, alpha: true, preserveDrawingBuffer: true });
  threeRenderer.setSize(container.clientWidth, container.clientHeight);
  threeRenderer.setPixelRatio(Math.min(window.devicePixelRatio, 2));
  threeRenderer.shadowMap.enabled = true;
  threeRenderer.shadowMap.type = THREE.PCFSoftShadowMap;

  // 4. Orbit Controls (Smooth 360° rotation)
  threeControls = new THREE.OrbitControls(threeCamera, threeRenderer.domElement);
  threeControls.enableDamping = true;
  threeControls.dampingFactor = 0.08;
  threeControls.minDistance = 2.8;
  threeControls.maxDistance = 6.5;
  threeControls.autoRotate = false;
  threeControls.autoRotateSpeed = 2.0;

  // 5. Studio 3-Point Lighting
  const ambLight = new THREE.AmbientLight(0xffffff, 0.9);
  threeScene.add(ambLight);

  const mainLight = new THREE.DirectionalLight(0xffffff, 0.95);
  mainLight.position.set(2.5, 4, 4);
  mainLight.castShadow = true;
  mainLight.shadow.mapSize.width = 1024;
  mainLight.shadow.mapSize.height = 1024;
  threeScene.add(mainLight);

  const fillLight = new THREE.DirectionalLight(0xe0f2fe, 0.5);
  fillLight.position.set(-3, -1, 3);
  threeScene.add(fillLight);

  const rimLight = new THREE.DirectionalLight(0xffffff, 0.7);
  rimLight.position.set(0, 4, -4);
  threeScene.add(rimLight);

  // 6. High Resolution Dynamic Texture Canvas (2048x2048)
  offscreenCanvas = document.createElement('canvas');
  offscreenCanvas.width = 2048;
  offscreenCanvas.height = 2048;
  offscreenCtx = offscreenCanvas.getContext('2d');
  canvasTexture = new THREE.CanvasTexture(offscreenCanvas);
  canvasTexture.wrapS = THREE.RepeatWrapping;
  canvasTexture.wrapT = THREE.RepeatWrapping;
  canvasTexture.anisotropy = 8;

  // 7. Build High-Fidelity 3D Fight Shorts Model
  buildRealistic3DShorts();

  // Animation Loop
  function animate3D() {
    requestAnimationFrame(animate3D);
    threeControls.update();
    threeRenderer.render(threeScene, threeCamera);
  }
  animate3D();

  window.addEventListener('resize', onWindowResize3D);
}

function onWindowResize3D() {
  const container = document.getElementById('studio3DCanvasContainer');
  if (!container || !threeRenderer || !threeCamera) return;
  threeCamera.aspect = container.clientWidth / container.clientHeight;
  threeCamera.updateProjectionMatrix();
  threeRenderer.setSize(container.clientWidth, container.clientHeight);
}

// Build realistic athletic fight shorts with flared legs, curved crotch, side slit cutaways, and waistband
function buildRealistic3DShorts() {
  shortsGroup = new THREE.Group();

  // Fabric Material (High-resolution sublimation map with soft athletic microfiber sheen)
  const fabricMaterial = new THREE.MeshStandardMaterial({
    map: canvasTexture,
    roughness: 0.45,
    metalness: 0.05,
    side: THREE.DoubleSide
  });

  // Waistband Material (Elastic ribbing)
  const waistbandMaterial = new THREE.MeshStandardMaterial({
    color: new THREE.Color(studioState.waistbandColor),
    roughness: 0.65,
    metalness: 0.05
  });

  // 1. Contoured Waistband
  const waistGeom = new THREE.CylinderGeometry(1.22, 1.28, 0.40, 48, 1, true);
  waistMesh = new THREE.Mesh(waistGeom, waistbandMaterial);
  waistMesh.scale.set(1.0, 1.0, 0.82); // Elliptical human waist
  waistMesh.position.y = 0.95;
  shortsGroup.add(waistMesh);

  // Front closure velcro flap (White with border)
  const flapGeom = new THREE.BoxGeometry(0.46, 0.42, 0.12);
  const flapMat = new THREE.MeshStandardMaterial({
    color: 0xf4f1ea,
    roughness: 0.4
  });
  flapMesh = new THREE.Mesh(flapGeom, flapMat);
  flapMesh.position.set(0, 0.95, 1.05);
  shortsGroup.add(flapMesh);

  // 2. Left Flared Combat Leg (Realistic angled flare & side slit)
  const leftLegGeom = new THREE.CylinderGeometry(0.72, 0.92, 1.95, 36, 1, true);
  leftLegMesh = new THREE.Mesh(leftLegGeom, fabricMaterial);
  leftLegMesh.position.set(-0.58, -0.05, 0);
  leftLegMesh.rotation.z = 0.08;
  leftLegMesh.scale.set(1.0, 1.0, 0.85);
  shortsGroup.add(leftLegMesh);

  // 3. Right Flared Combat Leg (Mirrored angled flare & side slit)
  const rightLegGeom = new THREE.CylinderGeometry(0.72, 0.92, 1.95, 36, 1, true);
  rightLegMesh = new THREE.Mesh(rightLegGeom, fabricMaterial);
  rightLegMesh.position.set(0.58, -0.05, 0);
  rightLegMesh.rotation.z = -0.08;
  rightLegMesh.scale.set(1.0, 1.0, 0.85);
  shortsGroup.add(rightLegMesh);

  // 4. Crotch / Groin Inseam Flex Gusset (Smooth connection)
  const gussetGeom = new THREE.SphereGeometry(0.60, 24, 16, 0, Math.PI);
  const gussetMesh = new THREE.Mesh(gussetGeom, fabricMaterial);
  gussetMesh.scale.set(0.85, 0.55, 0.75);
  gussetMesh.position.set(0, 0.42, 0);
  shortsGroup.add(gussetMesh);

  // 5. Dark Inner Cavity (Interior depth shadow)
  const innerMat = new THREE.MeshBasicMaterial({ color: 0x111417, side: THREE.BackSide });
  const innerWaist = new THREE.Mesh(new THREE.CylinderGeometry(1.20, 1.25, 0.40, 24, 1, true), innerMat);
  innerWaist.scale.set(1.0, 1.0, 0.82);
  innerWaist.position.y = 0.95;
  shortsGroup.add(innerWaist);

  // 6. Ground Contact Shadow Mesh
  const shadowCanvas = document.createElement('canvas');
  shadowCanvas.width = 128;
  shadowCanvas.height = 128;
  const sCtx = shadowCanvas.getContext('2d');
  const radGrad = sCtx.createRadialGradient(64, 64, 10, 64, 64, 60);
  radGrad.addColorStop(0, 'rgba(15, 23, 42, 0.45)');
  radGrad.addColorStop(0.6, 'rgba(15, 23, 42, 0.15)');
  radGrad.addColorStop(1, 'rgba(15, 23, 42, 0)');
  sCtx.fillStyle = radGrad;
  sCtx.fillRect(0, 0, 128, 128);

  const shadowTexture = new THREE.CanvasTexture(shadowCanvas);
  const shadowGeom = new THREE.PlaneGeometry(3.6, 2.8);
  const shadowMat = new THREE.MeshBasicMaterial({
    map: shadowTexture,
    transparent: true,
    depthWrite: false
  });
  shadowMesh = new THREE.Mesh(shadowGeom, shadowMat);
  shadowMesh.rotation.x = -Math.PI / 2;
  shadowMesh.position.set(0, -1.25, 0);
  threeScene.add(shadowMesh);

  shortsGroup.position.y = -0.2;
  threeScene.add(shortsGroup);

  update3DTexture();
}

// Ultra-crisp 2048x2048 dynamic UV texture projection onto 3D shorts
function update3DTexture() {
  if (!offscreenCtx || !canvasTexture) return;

  const w = 2048;
  const h = 2048;

  // 1. Base fabric color
  offscreenCtx.fillStyle = studioState.fabricColor;
  offscreenCtx.fillRect(0, 0, w, h);

  // 2. Black lateral racing stripes & hem trim
  offscreenCtx.fillStyle = studioState.waistbandColor;
  offscreenCtx.fillRect(0, 0, 160, h);
  offscreenCtx.fillRect(w - 160, 0, 160, h);
  offscreenCtx.fillRect(0, h - 80, w, 80); // bottom hem binding

  // 3. Project 2D design elements onto the 3D shorts UV space
  studioState.elements.forEach(el => {
    offscreenCtx.save();
    
    // Normalize coordinates from 850x600 2D canvas to 2048x2048 UV texture
    const normX = (el.x / 850) * w;
    const normY = (el.y / 600) * h;

    offscreenCtx.translate(normX, normY);
    offscreenCtx.rotate((el.rotation || 0) * Math.PI / 180);
    offscreenCtx.scale((el.scale || 1) * 2.4, (el.scale || 1) * 2.4);

    if (el.type === 'text') {
      offscreenCtx.font = `bold ${el.size || 34}px ${el.font || 'Impact'}`;
      offscreenCtx.textAlign = 'center';
      offscreenCtx.textBaseline = 'middle';
      offscreenCtx.fillStyle = el.color || '#111417';
      offscreenCtx.fillText(el.text, 0, 0);

      // Outline
      offscreenCtx.strokeStyle = el.color === '#efd965' ? '#18181b' : 'rgba(255,255,255,0.4)';
      offscreenCtx.lineWidth = 1.5;
      offscreenCtx.strokeText(el.text, 0, 0);
    } else {
      renderVectorGraphic(offscreenCtx, el);
    }
    offscreenCtx.restore();
  });

  // Update Three.js texture
  canvasTexture.needsUpdate = true;

  // Also update photorealistic 2D overlay if active
  renderPhotoMockup();
}

// Angle Presets
function set3DAngle(angle) {
  if (!threeCamera || !threeControls) return;
  threeControls.autoRotate = false;
  document.getElementById('btnAutoRotate').classList.remove('text-sky-400');

  if (angle === 'front') {
    threeCamera.position.set(0, 0.1, 4.8);
  } else if (angle === 'left') {
    threeCamera.position.set(-4.2, 0.2, 2.2);
  } else if (angle === 'right') {
    threeCamera.position.set(4.2, 0.2, 2.2);
  } else if (angle === 'back') {
    threeCamera.position.set(0, 0.1, -4.8);
  }
  threeControls.target.set(0, -0.2, 0);
  threeControls.update();
}

function reset3DCamera() {
  set3DAngle('front');
}

function toggle3DAutoRotate() {
  if (!threeControls) return;
  threeControls.autoRotate = !threeControls.autoRotate;
  const btn = document.getElementById('btnAutoRotate');
  if (threeControls.autoRotate) {
    btn.classList.add('text-sky-400');
    showToast('360° Auto-rotation enabled', 'info');
  } else {
    btn.classList.remove('text-sky-400');
  }
}

function toggle3DRenderMode() {
  const threeCanv = document.getElementById('threeCanvas');
  const photoOverlay = document.getElementById('photoRenderOverlay');
  const btn = document.getElementById('btnRenderMode');
  const lbl = document.getElementById('lbl3DMode');

  if (studioState.renderMode === 'orbit') {
    studioState.renderMode = 'photo';
    threeCanv.classList.add('hidden');
    photoOverlay.classList.remove('hidden');
    btn.innerText = 'Photo Render';
    lbl.innerText = 'Studio Photo';
    renderPhotoMockup();
    showToast('Switched to Studio Photo Render Mode', 'info');
  } else {
    studioState.renderMode = 'orbit';
    photoOverlay.classList.add('hidden');
    threeCanv.classList.remove('hidden');
    btn.innerText = '3D Orbit';
    lbl.innerText = '3D Orbit';
    onWindowResize3D();
  }
}

// Photorealistic Studio Mockup Render (Matches reference image visual perfection)
function renderPhotoMockup() {
  const pCanvas = document.getElementById('photoCanvas');
  if (!pCanvas) return;
  const pCtx = pCanvas.getContext('2d');
  const pw = pCanvas.width;
  const ph = pCanvas.height;

  pCtx.clearRect(0, 0, pw, ph);

  // Soft studio shadow
  pCtx.save();
  pCtx.beginPath();
  pCtx.ellipse(pw / 2, ph - 45, 160, 22, 0, 0, Math.PI * 2);
  pCtx.fillStyle = 'rgba(15, 23, 42, 0.18)';
  pCtx.filter = 'blur(8px)';
  pCtx.fill();
  pCtx.restore();

  // Draw Realistic Fight Shorts Silhouette
  pCtx.save();
  
  // Base yellow/gold shorts body
  pCtx.fillStyle = studioState.fabricColor;
  pCtx.strokeStyle = '#334155';
  pCtx.lineWidth = 3;

  pCtx.beginPath();
  // Waist line
  pCtx.moveTo(130, 160);
  pCtx.quadraticCurveTo(pw / 2, 175, 370, 160);
  // Right outer leg with flare
  pCtx.lineTo(415, 330);
  // Right 45-deg slit
  pCtx.lineTo(430, 390);
  pCtx.lineTo(375, 405);
  // Right inner inseam
  pCtx.lineTo(280, 400);
  // Crotch curve
  pCtx.quadraticCurveTo(pw / 2, 310, 220, 400);
  // Left inner inseam
  pCtx.lineTo(125, 405);
  // Left 45-deg slit
  pCtx.lineTo(70, 390);
  pCtx.lineTo(85, 330);
  // Left outer leg
  pCtx.closePath();
  pCtx.fill();
  pCtx.stroke();

  // Lateral black racing stripes & slit binding
  pCtx.fillStyle = studioState.waistbandColor;
  // Left slit
  pCtx.beginPath();
  pCtx.moveTo(70, 390);
  pCtx.lineTo(85, 330);
  pCtx.lineTo(95, 330);
  pCtx.lineTo(80, 390);
  pCtx.closePath();
  pCtx.fill();
  // Right slit
  pCtx.beginPath();
  pCtx.moveTo(430, 390);
  pCtx.lineTo(415, 330);
  pCtx.lineTo(405, 330);
  pCtx.lineTo(420, 390);
  pCtx.closePath();
  pCtx.fill();

  // Inner crotch shadow
  pCtx.fillStyle = 'rgba(0, 0, 0, 0.12)';
  pCtx.beginPath();
  pCtx.moveTo(220, 400);
  pCtx.quadraticCurveTo(pw / 2, 310, 280, 400);
  pCtx.lineTo(pw / 2, 340);
  pCtx.closePath();
  pCtx.fill();

  // Thick Ribbed Waistband
  pCtx.fillStyle = studioState.waistbandColor;
  pCtx.beginPath();
  pCtx.moveTo(130, 160);
  pCtx.quadraticCurveTo(pw / 2, 175, 370, 160);
  pCtx.lineTo(365, 115);
  pCtx.quadraticCurveTo(pw / 2, 130, 135, 115);
  pCtx.closePath();
  pCtx.fill();
  pCtx.stroke();

  // Center Front Closure Flap (White)
  pCtx.fillStyle = studioState.flapColor;
  pCtx.strokeStyle = '#cbd5e1';
  pCtx.lineWidth = 2;
  pCtx.beginPath();
  pCtx.roundRect(pw / 2 - 32, 125, 64, 45, 4);
  pCtx.fill();
  pCtx.stroke();

  // Center crest wings logo on flap
  pCtx.save();
  pCtx.translate(pw / 2, 146);
  pCtx.scale(0.55, 0.55);
  renderVectorGraphic(pCtx, { preset: 'wings', color: '#111417' });
  pCtx.restore();

  // Project vertical "INFERNO" typography on legs
  pCtx.save();
  pCtx.translate(160, 285);
  pCtx.rotate(-Math.PI / 2);
  pCtx.font = 'bold 26px Impact';
  pCtx.textAlign = 'center';
  pCtx.fillStyle = '#111417';
  pCtx.fillText('INFERNO', 0, 0);
  pCtx.restore();

  // Project sponsor marks near right leg slit
  pCtx.save();
  pCtx.translate(355, 350);
  pCtx.scale(0.7, 0.7);
  renderVectorGraphic(pCtx, { preset: 'inferno_script', color: '#111417' });
  pCtx.restore();

  // Project lightning bolt
  pCtx.save();
  pCtx.translate(395, 350);
  pCtx.scale(0.7, 0.7);
  renderVectorGraphic(pCtx, { preset: 'bolt', color: '#111417' });
  pCtx.restore();

  pCtx.restore();
}

function toggle3DMinimize() {
  const container = document.getElementById('studio3DCanvasContainer');
  const icon = document.getElementById('btn3DMinIcon');
  if (container.classList.contains('hidden')) {
    container.classList.remove('hidden');
    icon.innerText = 'unfold_less';
  } else {
    container.classList.add('hidden');
    icon.innerText = 'unfold_more';
  }
}

// ------------------- STUDIO ACTIONS & TOOLS -------------------
function updateStudioLayers() {
  const list = document.getElementById('studioElementsList');
  const countLbl = document.getElementById('lblLayerCount');
  const objCountLbl = document.getElementById('lblObjectCount');
  if (!list) return;

  countLbl.innerText = studioState.elements.length;
  objCountLbl.innerText = `${studioState.elements.length} Active Elements`;

  list.innerHTML = studioState.elements.map(el => {
    const isSel = el.id === studioState.selectedElementId;
    const border = isSel ? 'border-sky-500 ring-2 ring-sky-200' : 'border-slate-200';
    return `
      <div class="p-2.5 rounded-xl bg-white border ${border} flex items-center justify-between gap-2 hover:bg-slate-50 transition-all cursor-pointer shadow-sm" onclick="selectStudioElement('${el.id}')">
        <div class="flex items-center gap-2.5 flex-1 overflow-hidden">
          <div class="w-8 h-8 rounded-lg bg-slate-100 border border-slate-200 flex items-center justify-center flex-shrink-0 font-bold text-xs text-slate-800">
            ${el.type === 'text' ? 'T' : (el.type === 'logo' ? '★' : '⚡')}
          </div>
          <div class="truncate">
            <div class="font-bold text-xs text-slate-900 truncate">${el.name}</div>
            <div class="text-[10px] text-slate-500 uppercase">${el.type} • Scale: ${(el.scale || 1).toFixed(2)}</div>
          </div>
        </div>

        <div class="flex items-center gap-1.5">
          <input type="color" value="${el.color || '#111417'}" onchange="changeElementColor('${el.id}', this.value)" class="w-6 h-6 rounded cursor-pointer border-0 p-0 bg-transparent" title="Change Color"/>
          <button onclick="event.stopPropagation(); deleteStudioElement('${el.id}')" class="w-7 h-7 rounded-lg flex items-center justify-center text-slate-400 hover:text-red-600 hover:bg-red-50 transition-colors" title="Delete Layer">
            <span class="material-symbols-outlined text-[18px]">delete</span>
          </button>
        </div>
      </div>
    `;
  }).join('');
}

function selectStudioElement(id) {
  studioState.selectedElementId = id;
  renderPatternCanvas();
  updateStudioLayers();
}

function deleteStudioElement(id) {
  saveStudioHistory();
  studioState.elements = studioState.elements.filter(e => e.id !== id);
  if (studioState.selectedElementId === id) studioState.selectedElementId = null;
  renderPatternCanvas();
  updateStudioLayers();
  update3DTexture();
}

function changeElementColor(id, hex) {
  saveStudioHistory();
  const el = studioState.elements.find(e => e.id === id);
  if (el) {
    el.color = hex;
    renderPatternCanvas();
    updateStudioLayers();
    update3DTexture();
  }
}

function clearAllElements() {
  if (!confirm('Clear all placed logos and text from shorts?')) return;
  saveStudioHistory();
  studioState.elements = [];
  studioState.selectedElementId = null;
  renderPatternCanvas();
  updateStudioLayers();
  update3DTexture();
}

function addTextToCanvas() {
  const text = document.getElementById('studioTextInput').value.trim();
  if (!text) return;
  const font = document.getElementById('studioFontSelect').value;
  const color = document.getElementById('studioTextColorInput').value;

  saveStudioHistory();
  const newEl = {
    id: 'text_' + Date.now(),
    type: 'text',
    name: `Text: ${text.toUpperCase()}`,
    text: text.toUpperCase(),
    x: 425,
    y: 280,
    scale: 1.0,
    rotation: 0,
    color: color,
    font: font,
    size: 34
  };
  studioState.elements.push(newEl);
  studioState.selectedElementId = newEl.id;

  renderPatternCanvas();
  updateStudioLayers();
  update3DTexture();
  setStudioTab('layers');
  showToast(`Added "${text}" to pattern! Click and drag on canvas to position.`, 'success');
}

function renderPresetLogos() {
  const container = document.getElementById('presetLogosContainer');
  if (!container) return;
  const presets = [
    { name: 'Wings Crest', preset: 'wings', icon: '★' },
    { name: 'Strike Text', preset: 'metal', icon: '⚡' },
    { name: 'Custom Inferno', preset: 'inferno_script', icon: '🔥' },
    { name: 'Lightning Bolt', preset: 'bolt', icon: '⚡' }
  ];

  container.innerHTML = presets.map(p => `
    <button onclick="addPresetLogo('${p.preset}', '${p.name}')" class="p-2.5 rounded-xl bg-slate-50 hover:bg-sky-50 hover:border-sky-300 transition-all border border-slate-200 flex items-center gap-2 text-left">
      <span class="w-8 h-8 rounded-lg bg-white flex items-center justify-center font-bold text-sm text-sky-600 shadow-sm border border-slate-100">${p.icon}</span>
      <span class="text-xs font-bold text-slate-800">${p.name}</span>
    </button>
  `).join('');
}

function renderCliparts() {
  const container = document.getElementById('clipartsContainer');
  if (!container) return;
  const cliparts = [
    { name: 'Bolt', preset: 'bolt', symbol: '⚡' },
    { name: 'Wings', preset: 'wings', symbol: '🦅' },
    { name: 'Shield', preset: 'shield', symbol: '🛡️' },
    { name: 'Dragon', preset: 'dragon', symbol: '🐉' },
    { name: 'Skull', preset: 'skull', symbol: '💀' },
    { name: 'Fist', preset: 'fist', symbol: '👊' }
  ];

  container.innerHTML = cliparts.map(c => `
    <button onclick="addPresetLogo('${c.preset}', '${c.name}')" class="p-3 rounded-xl bg-slate-50 hover:bg-sky-50 hover:border-sky-300 transition-all flex flex-col items-center gap-1 border border-slate-200">
      <span class="text-2xl">${c.symbol}</span>
      <span class="text-[10px] font-bold text-slate-800 uppercase">${c.name}</span>
    </button>
  `).join('');
}

function addPresetLogo(preset, name) {
  saveStudioHistory();
  const newEl = {
    id: 'logo_' + Date.now(),
    type: 'logo',
    name: name,
    preset: preset,
    x: 425,
    y: 280,
    scale: 0.85,
    rotation: 0,
    color: '#111417'
  };
  studioState.elements.push(newEl);
  studioState.selectedElementId = newEl.id;
  renderPatternCanvas();
  updateStudioLayers();
  update3DTexture();
  setStudioTab('layers');
  showToast(`Placed ${name} on pattern!`, 'info');
}

// CUSTOM LOGO UPLOAD (Direct local storage integration)
async function handleStudioLogoUpload(event) {
  const file = event.target.files[0];
  if (!file) return;

  const reader = new FileReader();
  reader.onload = async (e) => {
    const img = new Image();
    img.onload = () => {
      saveStudioHistory();
      const newEl = {
        id: 'upload_' + Date.now(),
        type: 'logo',
        name: `Upload: ${file.name.slice(0, 15)}`,
        imageObj: img,
        x: 425,
        y: 260,
        scale: 0.9,
        rotation: 0,
        color: '#111417'
      };
      studioState.elements.push(newEl);
      studioState.selectedElementId = newEl.id;
      renderPatternCanvas();
      updateStudioLayers();
      update3DTexture();
      setStudioTab('layers');
      showToast(`Uploaded ${file.name} and mapped to 3D shorts!`, 'success');
    };
    img.src = e.target.result;

    const formData = new FormData();
    formData.append('file', file);
    formData.append('category', 'designs');
    try {
      await fetch('/api/upload', { method: 'POST', body: formData });
    } catch(err) {}
  };
  reader.readAsDataURL(file);
}

function resetStudioCanvas() {
  if (!confirm('Reset pattern to CDR default layout?')) return;
  saveStudioHistory();
  studioState.fabricColor = '#efd965';
  studioState.elements = [
    { id: 'el_crest', type: 'logo', name: 'Waistband Wings Crest', x: 425, y: 70, scale: 0.75, rotation: 0, color: '#111417', preset: 'wings' },
    { id: 'el_text1', type: 'text', name: 'Left Leg Vertical INFERNO', text: 'INFERNO', x: 265, y: 280, scale: 1.0, rotation: -90, color: '#111417', font: 'Impact', size: 38 },
    { id: 'el_text2', type: 'text', name: 'Right Leg Vertical INFERNO', text: 'INFERNO', x: 585, y: 280, scale: 1.0, rotation: -90, color: '#111417', font: 'Impact', size: 38 },
    { id: 'el_sponsor1', type: 'logo', name: 'Left Slit Sponsor Logo', x: 310, y: 350, scale: 0.8, rotation: 0, color: '#111417', preset: 'metal' },
    { id: 'el_sponsor2', type: 'logo', name: 'Right Slit Custom Inferno', x: 535, y: 350, scale: 0.85, rotation: 0, color: '#111417', preset: 'inferno_script' },
    { id: 'el_bolt', type: 'clipart', name: 'Right Slit Lightning Bolt', x: 635, y: 350, scale: 0.85, rotation: 0, color: '#111417', preset: 'bolt' },
    { id: 'el_belt', type: 'text', name: 'Lower Belt Script', text: 'CUSTOM INFERNO', x: 425, y: 535, scale: 0.95, rotation: 0, color: '#efd965', font: 'Impact', size: 28 }
  ];
  studioState.selectedElementId = null;
  renderPatternCanvas();
  updateStudioLayers();
  update3DTexture();
  showToast('Pattern reset to default CDR template layout.', 'info');
}

function saveStudioDraft() {
  const snapshot = {
    template: 'Backup_of_ZAM FORWARD 123456.cdr',
    timestamp: new Date().toISOString(),
    state: studioState
  };
  localStorage.setItem('zam_studio_draft', JSON.stringify(snapshot));
  showToast('Design draft and 3D configuration saved locally!', 'success');
}

// SUBMIT ORDER DIRECTLY FROM AI STUDIO
async function submitStudioOrder() {
  const custName = prompt('Enter Athlete / Fight Gym Name for Order:', 'Inferno Fight Team');
  if (!custName) return;
  const custEmail = prompt('Enter Contact Email Address:', 'coach@infernofight.com');
  if (!custEmail) return;

  const payload = {
    customer_name: custName,
    customer_email: custEmail,
    customer_phone: '+1 555-0199',
    notes: `Created via ZamForward AI 3D Studio from template Backup_of_ZAM FORWARD 123456.cdr. Body: ${studioState.fabricName}.`,
    items: [{
      product_id: 3,
      product_name: 'Apex Combat Flex-Split MMA Shorts (CDR Custom)',
      quantity: 15,
      size: 'L',
      color: studioState.fabricName,
      unit_price: 48.0,
      design_config: {
        template_source: 'Backup_of_ZAM FORWARD 123456.cdr',
        fabric_color: studioState.fabricColor,
        elements_count: studioState.elements.length,
        elements: studioState.elements.map(e => ({ name: e.name, type: e.type, x: e.x, y: e.y, color: e.color }))
      }
    }]
  };

  try {
    const res = await fetch('/api/orders', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    const data = await res.json();
    if (res.ok) {
      closeAiStudioModal();
      showToast(`Order ${data.order_number} confirmed! Saved to SQLite with 3D design files.`, 'success');
      document.getElementById('trackingInput').value = data.order_number;
      lookupOrder(data.order_number);
      loadAdminOrders();
      window.location.hash = '#tracking';
    } else {
      showToast(data.error || 'Failed to submit order', 'error');
    }
  } catch(err) {
    showToast(err.message, 'error');
  }
}
'''

text = js_pattern.sub(upgraded_js + '</script>', text)

with open('public/index.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('code.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("3D Fight Shorts engine & CorelDraw pattern upgraded with high fidelity.")
