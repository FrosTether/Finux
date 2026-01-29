import hashlib
import json
import http.server
import socketserver
import os

PORT = 8080
UPDATE_FILE = "finux_rc1_iceland.zip"
MANIFEST_FILE = "update_manifest.json"

def calculate_sha256(filepath):
    sha256_hash = hashlib.sha256()
    with open(filepath, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

def update_manifest():
    if not os.path.exists(UPDATE_FILE):
        print(f"[!] Error: {UPDATE_FILE} not found.")
        return

    print(f"[❄️] Hashing {UPDATE_FILE}...")
    file_hash = calculate_sha256(UPDATE_FILE)
    
    manifest_data = {
        "release": "Finux RC1 (Iceland)",
        "version": "1.0.0",
        "file": UPDATE_FILE,
        "sha256": file_hash,
        "priority": "critical"
    }

    with open(MANIFEST_FILE, "w") as f:
        json.dump(manifest_data, f, indent=4)
    print(f"[+] Manifest updated: {file_hash}")

def start_ota_server():
    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"[❄️] OTA Dispatcher running at port {PORT}")
        print(f"[i] Devices can pull updates from this node.")
        httpd.serve_forever()

if __name__ == "__main__":
    update_manifest()
    start_ota_server()
