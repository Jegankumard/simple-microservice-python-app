from flask import Flask, jsonify, render_template
import socket
app = Flask(__name__)

@app.route('/host')
def host():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print("Hostname   : ", host_name)
    print("IP Address : ", host_ip)
    return str(host_name), str(host_ip)

@app.route('/')
def hello():
    return 'Hello Welcome to this page...!!!'

@app.route('/health')
def health():
    return jsonify(
        status="UP"
    )

@app.route('/details')
def details():
    host_name_py, host_ip_py = host()
    return render_template('index.html', host_name_html=host_name_py, host_ip_html=host_ip_py)

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)