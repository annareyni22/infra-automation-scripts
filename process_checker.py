import subprocess

process = input("Enter process name: ")

result = subprocess.getoutput(f"ps -ef | grep {process}")

print(result)
