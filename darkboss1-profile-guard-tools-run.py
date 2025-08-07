import platform
import os
import time
import subprocess

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    clear()
    print("""
╔══════════════════════════════════════════════╗
║ 🛡️ DARKBOSS1 PROFILE GUARD TOOL LAUNCHER 🛡️ ║
╠══════════════════════════════════════════════╣
║ Author   : darkboss1 Ak47                    ║
║ GitHub   : https://github.com/darkboss1      ║
║ Version  : 2.1                               ║
╚══════════════════════════════════════════════╝
""")

def git_pull():
    print("\n[🔄] Pulling latest updates from GitHub...\n")
    try:
        subprocess.run(["git", "pull"], check=True)
        print("[✅] GitHub repo is up to date.")
    except subprocess.CalledProcessError:
        print("[❌] Failed to pull from GitHub. Is this even a git repo?")

def check_architecture():
    arch = platform.machine()
    if 'aarch64' in arch or 'arm64' in arch:
        return '64-bit'
    elif 'arm' in arch or 'i686' in arch:
        return '32-bit'
    else:
        return 'unknown'

def run_main_module():
    try:
        import main  # Assuming this is your compiled .so file
        main.main()  # Entry point defined in your main.py before Cythonizing
    except ImportError as e:
        print("[❗] Import error:", e)
    except AttributeError:
        print("[⚠️] .so module found, but no main() function inside it!")

def main():
    banner()
    git_pull()
    print("\n[*] Checking device architecture...\n")
    time.sleep(1)

    arch = check_architecture()
    print(f"[✔] Detected architecture: {arch}")

    if arch == '64-bit':
        print("\n[🚀] Device supported! Running Profile Guard Tool...\n")
        time.sleep(1)
        run_main_module()
    elif arch == '32-bit':
        print("\n[❌] Sorry bro, 32-bit devices aren't supported 😢")
    else:
        print("\n[❗] Unknown device architecture. Can't proceed.")

# 🔥 Entry point
if __name__ == "__main__":
    main()
