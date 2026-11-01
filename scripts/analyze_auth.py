
import csv
from collections import Counter, defaultdict
from pathlib import Path

# Find the sample log file relative to this script.
project_root = Path(__file__).resolve().parent.parent
log_file = project_root / "sample-logs" / "authentication.csv"

failed_by_ip = Counter()
failed_by_user = Counter()
successful_by_ip = Counter()

with log_file.open("r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        event = row["event"]
        source_ip = row["source_ip"]
        username = row["username"]

        if event == "LOGIN_FAILED":
            failed_by_ip[source_ip] += 1
            failed_by_user[username] += 1

        elif event == "LOGIN_SUCCESS":
            successful_by_ip[source_ip] += 1

print("=== Authentication Log Analysis ===")
print(f"Log file: {log_file.name}")

print("\nFailed logins by source IP:")
for ip, count in failed_by_ip.most_common():
    print(f"  {ip}: {count}")

print("\nFailed logins by username:")
for user, count in failed_by_user.most_common():
    print(f"  {user}: {count}")

print("\nSuccessful logins by source IP:")
for ip, count in successful_by_ip.most_common():
    print(f"  {ip}: {count}")

print("\n=== Preliminary Detection ===")

for ip, failures in failed_by_ip.items():
    if failures >= 5 and successful_by_ip[ip] > 0:
        print(
            f"ALERT: {ip} had {failures} failed logins "
            "and at least one successful login."
        )
