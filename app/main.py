from flask import Flask, request, jsonify
import subprocess
import os

app = Flask(__name__)


@app.get("/")
def home():
    return jsonify({"message": "DevSecOps security guardrails demo API"})


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/diagnostic")
def diagnostic():
    host = request.args.get("host", "127.0.0.1")

    # Intentionally insecure for SAST demonstration only.
    # This will be reviewed and remediated later in the project.
    result = subprocess.run(
        f"echo Checking {host}",
        shell=True,
        capture_output=True,
        text=True
    )

    return jsonify({"output": result.stdout})


@app.get("/config-status")
def config_status():
    demo_key = os.getenv("DEMO_API_KEY", "not-set")
    return jsonify({"demo_key_configured": demo_key != "not-set"})
