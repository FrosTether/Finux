from flask import Flask, render_template_string
import os, psutil

app = Flask(__name__)

@app.route('/')
def index():
    temp = os.popen("cat /sys/class/thermal/thermal_zone0/temp").read().strip()
    node_addr = os.getenv("FROST_NODE_ADDR", "Axun...uJMCf")
    
    html = f'''
    <body style="background:#000; color:#0f0; font-family:monospace; padding:20px;">
        <h1>FROST PROTOCOL NODE v13.37</h1>
        <hr>
        <p><b>IDENTITY:</b> {node_addr}</p>
        <p><b>NPU TEMP:</b> {int(temp)/1000}°C</p>
        <p><b>CPU USAGE:</b> {psutil.cpu_percent()}%</p>
        <p><b>STATUS:</b> <span style="color:cyan;">LIVE ON AIR</span></p>
    </body>
    '''
    return render_template_string(html)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
openssl req -x509 -newkey rsa:2048 -nodes \
  -keyout ~/finux/vault/keys/key.pem \
  -out ~/finux/vault/keys/cert.pem \
  -days 3650 \
  -subj "/C=US/ST=Ohio/L=Monroeville/O=FrostProtocol/CN=SatoshiNode"
