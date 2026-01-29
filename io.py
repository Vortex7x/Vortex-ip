import os

def read_ips_from_file(path):
    ips = []
    if not os.path.exists(path):
        return ips
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                ips.append(line)
    return ips