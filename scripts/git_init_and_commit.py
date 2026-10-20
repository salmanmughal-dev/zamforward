import subprocess
import os

GIT = r"C:\Program Files\Git\cmd\git.exe"

def run_git(args):
    cmd = [GIT] + args
    print(f"Running: {' '.join(cmd)}")
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.stdout:
        print("STDOUT:\n", res.stdout[:500])
    if res.stderr:
        print("STDERR:\n", res.stderr[:500])
    return res.returncode

# 1. Check user.name and user.email
res_name = subprocess.run([GIT, 'config', 'user.name'], capture_output=True, text=True)
res_email = subprocess.run([GIT, 'config', 'user.email'], capture_output=True, text=True)

print("Current git user.name:", res_name.stdout.strip() or "Not set")
print("Current git user.email:", res_email.stdout.strip() or "Not set")

# 2. git init
run_git(['init'])

# If user.name or user.email are not set globally, configure locally
if not res_name.stdout.strip():
    run_git(['config', 'user.name', 'Salman'])
if not res_email.stdout.strip():
    run_git(['config', 'user.email', 'salman@zamforward.com'])

# 3. git add .
run_git(['add', '.'])

# 4. git status --short
run_git(['status', '--short'])

# 5. git commit
run_git(['commit', '-m', 'feat: Initial commit of ZamForward full-stack platform with AI 3D Studio, CorelDraw pattern engine, and 163-item vector ranks library'])

# 6. git branch -M main
run_git(['branch', '-M', 'main'])

# 7. git log -1
run_git(['log', '-1', '--stat'])
