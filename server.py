import ctypes
import socket
from time import sleep

import yaml
from flask import Flask, render_template, send_from_directory, jsonify

with open('data.yml', 'r') as data:
    json_data = yaml.safe_load(data)

user32 = ctypes.WinDLL('user32', use_last_error=True)
delay = 0.01


def press(key):
    user32.keybd_event(key, 0, 0, 0)
    sleep(delay)
    user32.keybd_event(key, 0, 2, 0)
    sleep(delay)


app = Flask(__name__)


class Key:
    f13 = 0x7C
    f14 = 0x7D
    f15 = 0x7E
    f16 = 0x7F
    f17 = 0x80
    f18 = 0x81
    f19 = 0x82
    f20 = 0x83
    f21 = 0x84
    f22 = 0x85
    f23 = 0x86
    f24 = 0x87


@app.route('/images/<path:path>')
def favicon(path):
    return send_from_directory('images', path)


@app.route('/data')
def send_data():
    return jsonify(json_data)


@app.route('/scripts/<path:path>')
def send_js(path):
    return send_from_directory('scripts', path)


@app.route('/css/<path:path>')
def send_css(path):
    return send_from_directory('css', path)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/button1')
def button1():
    press(Key.f13)
    return ""


@app.route('/button2')
def button2():
    press(Key.f14)
    return ""


@app.route('/button3')
def button3():
    press(Key.f15)
    return ""


@app.route('/button4')
def button4():
    press(Key.f16)
    return ""


@app.route('/button5')
def button5():
    press(Key.f17)
    return ""


@app.route('/button6')
def button6():
    press(Key.f18)
    return ""


@app.route('/button7')
def button7():
    press(Key.f19)
    return ""


@app.route('/button8')
def button8():
    press(Key.f20)
    return ""


@app.route('/button9')
def button9():
    press(Key.f21)
    return ""


if __name__ == '__main__':
    ip = socket.gethostbyname(socket.gethostname())
    app.run(host=ip, port=8000)
