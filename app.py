from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def hello_world():
    result = subprocess.run(["./sys_check"], capture_output=True, text=True)
    response = f"stdout:\n{result.stdout}\n\nstderr:\n{result.stderr}\n\nreturncode: {result.returncode}"
    return response
if __name__ == "__main__":
    app.run()
