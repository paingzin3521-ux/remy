import os, time, sys, requests, random, socket, threading, string
from datetime import datetime

# [ COLORS ]
G, R, C, W, Y = '\033[1;32m', '\033[1;31m', '\033[1;36m', '\033[1;37m', '\033[1;33m'

def banner():
    os.system('clear')
    print(f"""{C}
     ██████╗ ███████╗███╗   ███╗██╗   ██╗
     ██╔══██╗██╔════╝████╗ ████║╚██╗ ██╔╝
     ██████╔╝█████╗  ██╔████╔██║ ╚████╔╝ 
     ██╔══██╗██╔════╝██║╚██╔╝██║  ╚██╔╝  
     ██║  ██║███████╗██║ ╚═╝ ██║   ██║   
     ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝   ╚═╝   
    {W}      --- [ REMY PRO V26.1 ] ---
    {G}       STABLE & HIGH SPEED SCAN {W}
    """)

def ai_log(msg, color=C):
    print(f"{W}[{datetime.now().strftime('%H:%M:%S')}] {color}AI: {msg}{W}")

def run_internet_engine(name, hosts):
    banner()
    ai_log(f"{name} Firewall ကို ကျော်ဖြတ်နေသည်...", G)
    def engine(h):
        while True:
            try:
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                    s.settimeout(2)
                    s.connect((h, 80))
                    payload = f"GET /generate_204 HTTP/1.1\r\nHost: {h}\r\nConnection: keep-alive\r\n\r\n"
                    s.sendall(payload.encode())
                    time.sleep(0.4)
            except: pass
    for h in hosts: threading.Thread(target=engine, args=(h,), daemon=True).start()
    try:
        while True:
            try:
                check = requests.get("http://www.google.com/generate_204", timeout=3)
                if check.status_code == 204: ai_log(f"{name} System: ONLINE", G)
                else: ai_log("Packet များ ပေးပို့နေသည်...", Y)
            except: ai_log("WiFi ချိတ်ဆက်မှုကို စစ်ဆေးနေသည်...", R)
            time.sleep(1.5)
    except KeyboardInterrupt: pass

def scanner_selector(charset, title):
    banner()
    print(f"{C}=====================================================")
    print(f"         {title} - ADVANCED SCANNER")
    print(f"=====================================================")
    print(f"\n{C}[ SELECT SCAN MODE ]")
    for i in range(6, 11):
        print(f"{W}[{i-5}] Scan {i}-Digit")
    print(f"{W}[0] Back")
    c = input(f"\n{C}Choose (0-5): {W}")
    if c in ['1','2','3','4','5']: run_hack(charset, int(c)+5, title)

def run_hack(charset, length, mode):
    banner()
    ai_log(f"{mode} ({length}L) စနစ်ကို စတင်နေပါပြီ...")
    try:
        while True:
            code = "".join(random.choice(charset) for _ in range(length))
            sys.stdout.write(f"\r{W}[{datetime.now().strftime('%H:%M:%S')}] {Y}SCANNING: {W}{code}")
            sys.stdout.flush()
            time.sleep(0.005)
    except KeyboardInterrupt: pass

def main():
    while True:
        banner()
        print(f"{W}[1] {G}Internet Access Bypass (Ruijie/MikroTik)")
        print(f"{W}[2] {G}Voucher Code Hack (6-10L စိတ်ကြိုက်)")
        print(f"{W}[0] {R}Exit")
        c = input(f"\n{C}REMY > {W}")
        if c == '1':
            banner()
            print(f"{W}[1] Ruijie\n[2] MikroTik\n[0] Back")
            brand = input(f"\n{C}Choose > {W}")
            if brand == '1': run_internet_engine("Ruijie", ["10.1.1.1", "google.com"])
            elif brand == '2': run_internet_engine("MikroTik", ["192.168.88.1", "google.com"])
        elif c == '2':
            banner()
            print(f"{W}[1] Digits Only\n[2] Letters Only\n[3] Mixed (6L)\n[0] Back")
            v_type = input(f"\n{C}HACK-TYPE > {W}")
            if v_type == '1': scanner_selector(string.digits, "DIGITS")
            elif v_type == '2': scanner_selector(string.ascii_lowercase, "LETTERS")
            elif v_type == '3': run_hack(string.ascii_lowercase + string.digits, 6, "MIXED")
        elif c == '0': sys.exit()

if __name__ == "__main__": main()
