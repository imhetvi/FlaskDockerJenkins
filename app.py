from flask import Flask, render_template
import datetime
import socket

app = Flask(__name__)

@app.route('/')
def home():
    current_time = datetime.datetime.now()
    hostname = socket.gethostname()
    ip_addr = socket.gethostbyname(hostname)
    return render_template('home.html', current_time=current_time, ip_addr=ip_addr)
if __name__ == '__main__':
    app.run(debug=True)