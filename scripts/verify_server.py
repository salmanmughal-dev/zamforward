import urllib.request
import re

url = "http://127.0.0.1:5000/"
try:
    with urllib.request.urlopen(url, timeout=5) as resp:
        code = resp.getcode()
        content = resp.read().decode('utf-8')
        print(f"Server response code: {code}")
        print(f"Content length: {len(content)}")
        
        # Verify key elements
        checks = [
            ('<svg width="0" height="0"', "SVG sprite"),
            ('class="ann"', "Announcement bar"),
            ('id="hdr"', "Header"),
            ('id="shopBtn"', "Shop button"),
            ('id="mega"', "Mega menu"),
            ('id="cart"', "Cart drawer"),
            ('id="mnav"', "Mobile nav drawer"),
            ('id="scrim"', "Scrim backdrop"),
            ('id="zam-navbar-style"', "Navbar CSS"),
            ('id="zam-navbar-script"', "Navbar JS"),
            ('id="tracking"', "Order tracking section"),
            ('id="aiStudioModal"', "AI 3D Studio modal")
        ]
        
        all_ok = True
        for pattern, label in checks:
            exists = pattern in content
            print(f"Checking {label}: {'PASS' if exists else 'FAIL'}")
            if not exists:
                all_ok = False
        
        print("\nOVERALL INTEGRITY:", "ALL CHECKS PASSED!" if all_ok else "SOME CHECKS FAILED")
except Exception as e:
    print("Error contacting server:", e)
