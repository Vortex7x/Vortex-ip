import sys
import time

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

def show_banner():
    banner = r"""
██╗   ██╗ ██████╗ ██████╗ ████████╗███████╗██╗  ██╗
██║   ██║██╔═══██╗██╔══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
██║   ██║██║   ██║██████╔╝   ██║   █████╗   ╚███╔╝ 
╚██╗ ██╔╝██║   ██║██╔══██╗   ██║   ██╔══╝   ██╔██╗ 
 ╚████╔╝ ╚██████╔╝██║  ██║   ██║   ███████╗██╔╝ ██╗
  ╚═══╝   ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
"""
    print(color(banner, "cyan"))
    print(color("[+] VORTEX-IP — Advanced IP Intelligence Tool", "red"))
print(color("[!] For educational & legal use only\n", "yellow"))

def hacker_intro(text="VORTEX-IP", delay=0.12):
    for ch in text:
        sys.stdout.write(color(ch, "magenta"))
        sys.stdout.flush()
        time.sleep(delay)
    print("\n")

def show_menu():
    print(color("1) Analyze single IP", "cyan"))
    print(color("2) Analyze multiple IPs", "cyan"))
    print(color("3) Analyze IPs from file", "cyan"))
    print(color("0) Exit", "cyan"))
    return input(color("➜ Select option: ", "yellow")).strip()