import subprocess

result = subprocess.run(["./sys_check"], capture_output=True, text=True)

print(result.stdout)

print(result.stderr)

print(result.returncode)
