import requests
import socket
from collections import Counter
from ui import color

# =========================
# APIs + ASN DB
# =========================
APIS = [
    "http://ip-api.com/json/{ip}",
    "https://ipwho.is/{ip}",
]

ASN_DB_PATH = "asn_db.txt"

def load_asn_db():
    asns = set()
    try:
        with open(ASN_DB_PATH, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    asns.add(line)
    except:
        pass
    return asns

ASN_DB = load_asn_db()

# =========================
# Fetch Data from APIs
# =========================
def fetch_all(ip):
    results = []
    for api in APIS:
        try:
            r = requests.get(api.format(ip=ip), timeout=6)
            if r.status_code == 200:
                results.append(r.json())
        except:
            pass
    return results

# =========================
# TOR Check
# =========================
TOR_EXIT_NODES = [
    # أمثلة فقط، ممكن تحدث بالقوائم الرسمية
    "185.220.101.", "185.220.102.", "185.220.103."
]

def is_tor(ip):
    return any(ip.startswith(prefix) for prefix in TOR_EXIT_NODES)

# =========================
# Reverse DNS
# =========================
def reverse_dns(ip):
    try:
        return socket.gethostbyaddr(ip)[0]
    except:
        return "Unknown"

# =========================
# Fake IP Reputation & Abuse Score
# يمكن تطويرها لاحقًا باستخدام APIs خارجية
# =========================
def reputation_score(ip):
    # مبدئي: 0-100 عشوائي / أو يعتمد على بيانات API لاحقًا
    return 85  # مثال ثابت، ممكن تعديله

def abuse_score(ip):
    # مبدئي: تقارير سابقة / لاحقًا API خارجي
    return {"reports": 3, "confidence": 92}  # مثال ثابت

# =========================
# Main Analyzer
# =========================
def analyze_ip(ip):
    print(color(f"\nAnalyzing: {ip}", "blue"))
    data = fetch_all(ip)
    if not data:
        print(color("Failed to fetch data.", "red"))
        return

    countries, cities, isps, asns = [], [], [], []

    for d in data:
        if d.get("country"):
            countries.append(d.get("country"))
        if d.get("city"):
            cities.append(d.get("city"))
        if d.get("isp"):
            isps.append(d.get("isp"))
        if d.get("asn"):
            asns.append(str(d.get("asn")))

    c_country = Counter(countries)
    c_city = Counter(cities)
    c_isp = Counter(isps)

    best_country, conf_country = c_country.most_common(1)[0]
    best_city, conf_city = (c_city.most_common(1)[0] if c_city else ("Unknown", 0))
    best_isp, conf_isp = (c_isp.most_common(1)[0] if c_isp else ("Unknown", 0))

    total = len(data)
    conf_score = int(((conf_country + conf_city + conf_isp) / (3*total)) * 100)

    is_vpn = any(a in ASN_DB for a in asns)
    tor_status = is_tor(ip)
    rev_dns = reverse_dns(ip)
    rep_score = reputation_score(ip)
    abuse = abuse_score(ip)

    # =========================
    # Print Results
    # =========================
    print(color(f"Country      : {best_country}", "green"))
    print(color(f"City         : {best_city}", "yellow"))
    print(color(f"ISP          : {best_isp}", "cyan"))
    print(color(f"VPN          : {'YES' if is_vpn else 'NO'}", "red" if is_vpn else "green"))
    print(color(f"TOR Network  : {'YES' if tor_status else 'NO'}", "red" if tor_status else "green"))
    print(color(f"Reverse DNS  : {rev_dns}", "magenta"))
    print(color(f"Confidence   : {conf_score}%", "magenta"))
    print(color(f"Reputation   : {rep_score}/100", "cyan"))
    print(color(f"Abuse Reports: {abuse['reports']} (Confidence {abuse['confidence']}%)", "red" if abuse['confidence']>70 else "green"))