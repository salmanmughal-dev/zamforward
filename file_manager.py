import os
import shutil
import uuid
from werkzeug.utils import secure_filename

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')

DIRECTORIES = {
    'designs': os.path.join(UPLOAD_DIR, 'designs'),
    'payment_slips': os.path.join(UPLOAD_DIR, 'payment_slips'),
    'templates': os.path.join(UPLOAD_DIR, 'templates'),
    'invoices': os.path.join(UPLOAD_DIR, 'invoices'),
}

ALLOWED_EXTENSIONS = {
    'designs': {'png', 'jpg', 'jpeg', 'svg', 'webp', 'ai', 'cdr', 'eps', 'pdf'},
    'payment_slips': {'png', 'jpg', 'jpeg', 'pdf'},
    'templates': {'cdr', 'svg', 'ai', 'eps', 'pdf', 'png'},
    'invoices': {'pdf', 'html', 'json'}
}

def init_file_directories():
    """Create local upload directories if they do not exist."""
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    for path in DIRECTORIES.values():
        os.makedirs(path, exist_ok=True)
    print("Local file management storage initialized successfully.")

def is_allowed_file(category, filename):
    if '.' not in filename:
        return False
    ext = filename.rsplit('.', 1)[1].lower()
    return ext in ALLOWED_EXTENSIONS.get(category, set())

def save_local_file(category, file_obj, custom_prefix=None):
    """
    Saves an uploaded file locally and returns a dict with metadata.
    """
    if category not in DIRECTORIES:
        raise ValueError(f"Unknown category: {category}")
    
    original_name = secure_filename(file_obj.filename)
    if not original_name:
        original_name = "upload.bin"
    
    ext = original_name.rsplit('.', 1)[1].lower() if '.' in original_name else 'bin'
    unique_id = uuid.uuid4().hex[:8]
    prefix = f"{custom_prefix}_" if custom_prefix else ""
    stored_name = f"{prefix}{unique_id}_{original_name}"
    
    target_path = os.path.join(DIRECTORIES[category], stored_name)
    file_obj.save(target_path)
    file_size = os.path.getsize(target_path)
    
    relative_url = f"/uploads/{category}/{stored_name}"
    
    return {
        "original_name": original_name,
        "stored_name": stored_name,
        "local_path": target_path,
        "relative_url": relative_url,
        "file_size": file_size,
        "category": category
    }

def get_file_path(category, filename):
    folder = DIRECTORIES.get(category)
    if not folder:
        return None
    safe_name = secure_filename(filename)
    path = os.path.join(folder, safe_name)
    if os.path.exists(path):
        return path
    return None
