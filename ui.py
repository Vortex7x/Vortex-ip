import sys
import time

# ===== Colors =====
COLORS = {
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "reset": "\033[0m",
}

def color(text, c):
    return f"{COLORS.get(c,'')}{text}{COLORS['reset']}"

# ===== Slow Print (موحد) =====
def slow_print(text, color_name="reset", delay=0.01):
    for ch in text:
        sys.stdout.write(color(ch, color_name))
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ===== Banner =====
def show_banner(delay=0.01):
    banner = r"""
██╗   ██╗ ██████╗ ██████╗ ████████╗███████╗██╗  ██╗
██║   ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
██║   ██║██║   ██║██████╔╝   ██║   █████╗   ╚███╔╝
╚██╗ ██╔╝██║   ██║██╔══██╗   ██║   ██╔══╝   ██╔██╗
 ╚████╔╝ ╚██████╔╝██║  ██║   ██║   ███████╗██╔╝ ██╗
  ╚═══╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
"""
    slow_print(banner, "cyan", delay)
    slow_print("[+] VORTEX-IP — Advanced IP Intelligence Tool", "red", delay)
    slow_print("[!] For educational & legal use only\n", "yellow", delay)

# ===== Hacker Intro =====
def hacker_intro(text="vortex-ip", delay=0.01):
    slow_print(text, "magenta", delay)
    print()

# ===== Menu =====
def show_menu(delay=0.01):
    slow_print("1) Analyze single IP", "cyan", delay)
    slow_print("2) Analyze multiple IPs", "cyan", delay)
    slow_print("3) Analyze IPs from file", "cyan", delay)
    slow_print("0) Exit", "cyan", delay)
    return input(color("➜ Select option: ", "yellow")).strip()