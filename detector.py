import csv
from datetime import datetime

print("=== Mini-SIEM SOC Lab by Mounika ===")
print("Analyzing alerts.csv with SOC logic...\n")

blocked = []

with open('alerts.csv','r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        ip = row['src_ip']
        count = int(row['failed_count'])
        user = row['user']

        if count > 5:
            threat = "CRITICAL" if count > 20 else "HIGH"
            print(f"[ALERT] {threat} - Brute force detected!")
            print(f" -> IP: {ip} | User: {user} | Attempts: {count}")
            print(f" -> ACTION: iptables -A INPUT -s {ip} -j DROP\n")
            
            blocked.append(ip)
            with open('blocked_ips.log','a') as log:
                log.write(f"{datetime.now()} - BLOCKED {ip} - {count} fails - User:{user}\n")

print(f"Total IPs Blocked: {len(blocked)}")
print("Check blocked_ips.log file")