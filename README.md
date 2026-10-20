# ZamForward — Combat Apparel Atelier & AI 3D Studio

An end-to-end custom combat apparel platform engineered for Brazilian Jiu-Jitsu, MMA, and Muay Thai academies. Features a real-time **WebGL 3D Garment Studio**, **CorelDraw (.CDR) vector pattern engine**, an integrated **163-item combat & belt-rank vector library**, automated SQLite order tracking (`ZAM-xxx-26`), invoice generation, and local file storage.

---

## Quickstart: Setup on a New Machine

Running ZamForward on any new machine (Windows, macOS, or Linux) takes less than 2 minutes.

### 1. Prerequisites
- **Python 3.8+** ([python.org](https://www.python.org/downloads/))
- **Git** ([git-scm.com](https://git-scm.com/downloads))

---

### 2. Installation Steps

#### Step 1: Clone the Repository
Using SSH (if your SSH key is added to GitHub):
```bash
git clone git@github.com:salmanmughal-dev/zamforward.git
cd zamforward
```
*Or using HTTPS:*
```bash
git clone https://github.com/salmanmughal-dev/zamforward.git
cd zamforward
```

#### Step 2: Create and Activate a Virtual Environment
**On Windows (PowerShell / Command Prompt):**
```powershell
python -m venv venv
venv\Scripts\activate
```

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

#### Step 4: Start the Server
```bash
python server.py
```

#### Step 5: Open in Your Browser
Navigate to:
```
http://127.0.0.1:5000/
```
or
```
http://localhost:5000/
```

---

## What Happens Automatically on First Launch
When `python server.py` starts, it automatically handles:
1. **Local Database Initialization:** Creates `zamforward.db` (SQLite) with 11 tables (`orders`, `order_items`, `products`, `categories`, `templates`, `invoices`, `payment_slips`, `audit_status_logs`, etc.).
2. **Database Seeding:** Automatically seeds standard combat products (IBJJF Gis, rashguards, split MMA shorts) and CorelDraw master template metadata.
3. **Storage Directories:** Automatically creates local storage directories:
   - `uploads/designs/` (User crests, sponsor logos)
   - `uploads/payment_slips/` (50% milestone bank transfer proofs)
   - `uploads/templates/` (Packaged CorelDraw `.cdr` files & thumbnails)
   - `uploads/invoices/` (Generated PDF / receipt assets)

---

## Key Features

- **Interactive AI 3D Studio (v2.0):**
  - Instant silhouette switching between **Long-Sleeve Rashguard (LS)**, **Short-Sleeve Rashguard (SS)**, and **MMA Fight Shorts**.
  - Real-time 360° Three.js WebGL rotation, custom multi-panel UV unwrap patterns, and lighting.
  - Interactive CAD gizmo for scaling, rotating, dragging, and layering artwork.
- **163 Vector Graphics & Belt Ranks Library:**
  - Located in `public/graphics/`, scoped to `.zg` (zero framework dependencies).
  - 9 Categories: Combat, Mascots, Warrior, Champion, Symbols, Ranks & belts (BJJ degree stripes 1–4, White/Blue/Purple/Brown/Black belts), Shapes & frames, Flags, and Wordmarks.
  - Integrated into the Studio's **Ranks** tab with 1-tap design injection.
- **CorelDraw (.CDR) Production Pipeline:**
  - Indexed master 36MB vector cut file (`Backup_of_ZAM_FORWARD_123456.cdr`) available for direct atelier download.
- **Milestone Order Lifecycle:**
  - Generates format `ZAM-xxx-26` orders with 50% deposit calculations, status audit logs, and slip upload verification.
- **Staff Atelier Operations Drawer:**
  - Slide-over console to manage batch queue, advance production stages, and update tracking numbers.

---

## Project Structure

```text
zamforward/
├── server.py              # Flask server, REST API & static file provider
├── database.py            # SQLite schema initialization and seed data
├── file_manager.py        # Local file storage handlers and validation
├── requirements.txt       # Python dependencies (Flask, Pillow)
├── code.html              # Reference production markup
├── public/                # Static web root
│   ├── index.html         # Main landing page & full 3D studio application
│   ├── images/            # Brand logos and product photography
│   │   ├── logo.jpeg      # Official ZamForward 3D brand logo
│   │   ├── home-page.jpg  # Hero product showcase
│   │   └── PRODUCT.jpeg   # Catalog product imagery
│   └── graphics/          # Vector symbols library
│       ├── graphics.css   # Scoped library styling
│       ├── graphics.js    # ZamGraphics mount and render engine
│       └── graphics-data.js # 163 vector SVGs, belts, and wordmark presets
└── uploads/               # Local user uploads and CDR templates (auto-created)
    └── templates/         # Master vector templates
```

---

## License & Credits
- **Icons & Graphics:** Game-icons.net (CC BY 3.0), Phosphor Icons (MIT), Circle Flags (MIT).
- **CorelDraw Templates & Garment Patterns:** ZamForward Atelier Direct.
