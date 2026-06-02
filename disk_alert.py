import shutil

usage = shutil.disk_usage("/")

used_percent = (usage.used / usage.total) * 100

print(f"Disk Usage: {used_percent:.2f}%")

if used_percent > 80:
    print("WARNING: Disk usage exceeds 80%")
