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

# ===== Slow Print (موحّد لكل التصميم) =====
def slow_print(text, color_name="reset", delay=0.08):
    for ch in text:
        sys.stdout.write(color(ch, color_name))
        sys.stdout.flush()
        time.sleep(delay)
    print()

# ===== Banner (بطيء 0.12) =====
def show_banner():
    banner = r"""
██╗   ██╗ ██████╗ ██████╗ ████████╗███████╗██╗  ██╗
██║   ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
██║   ██║██║   ██║██████╔╝   ██║   █████╗   ╚███╔╝
╚██╗ ██╔╝██║   ██║██╔══██╗   ██║   ██╔══╝   ██╔██╗
 ╚████╔╝ ╚██████╔╝██║  ██║   ██║   ███████╗██╔╝ ██╗
  ╚═══╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
"""
    slow_print(banner, "cyan", 0.08)
    slow_print("[+] VORTEX-IP — Advanced IP Intelligence Tool", "red", 0.08)
    slow_print("[!] For educational & legal use only\n", "yellow", 0.08)

# ===== Hacker Intro (نفس السرعة) =====
def hacker_intro(text="vortex-ip"):
    slow_print(text, "magenta", 0.08)
    print()

# ===== Menu (نفس السرعة 0.12) =====
def show_menu():
    slow_print("1) Analyze single IP", "cyan", 0.08)
    slow_print("2) Analyze multiple IPs", "cyan", 0.08)
    slow_print("3) Analyze IPs from file", "cyan", 0.08)
    slow_print("0) Exit", "cyan", 0.08)
    return input(color("➜ Select option: ", "yellow")).strip()