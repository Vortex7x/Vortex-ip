import sys
from ui import show_banner, hacker_intro, show_menu
from engine import analyze_ip
from io_handler import read_ips_from_file

def main():
    # =====     +  =====
    delay_speed = 0.02  #         

    show_banner(delay_speed)
    hacker_intro("VORTEX-IP", delay_speed)

    args = sys.argv[1:]
    if args:
        for ip in args:
            analyze_ip(ip)
        return

    while True:
        choice = show_menu(delay_speed)
        if choice == "1":
            ip = input("IP: ").strip()
            analyze_ip(ip)
        elif choice == "2":
            ips = input("IPs (space separated): ").split()
            for ip in ips:
                analyze_ip(ip)
        elif choice == "3":
            path = input("File path: ").strip()
            for ip in read_ips_from_file(path):
                analyze_ip(ip)
        elif choice == "0":
            print("Bye ")
            break
        else:
            print("Invalid choice!")
            
if __name__ == "__main__":
    main()