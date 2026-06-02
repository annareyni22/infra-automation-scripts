import re

log_file = "application.log"

with open(log_file, "r") as file:
    for line in file:
        if re.search("ERROR", line):
            print(line.strip())
