#!/usr/bin/env python

from flask import Flask, request, json, jsonify
import RPi.GPIO as GPIO
import time

PORT = 8080

OFF_PIN = 14
ON_PIN = 15

PULSE_WIDTH = 0.25

app = Flask(__name__, static_url_path='')

def start():
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(OFF_PIN, GPIO.OUT)
    GPIO.output(OFF_PIN, False)

    GPIO.setup(ON_PIN, GPIO.OUT)
    GPIO.output(ON_PIN, False)

    app.run(host='0.0.0.0', port=PORT, debug=True)

@app.route('/')
def root():
    return app.send_static_file('index.html')

@app.route('/lamp_on', methods=['PUT'])
def lamp_on():
    print "lamp_on"

    GPIO.output(ON_PIN, True)
    time.sleep(PULSE_WIDTH)
    GPIO.output(ON_PIN, False)

    return "Ok"

@app.route('/lamp_off', methods=['PUT'])
def lamp_off():
    print "lamp_off";

    GPIO.output(OFF_PIN, True)
    time.sleep(PULSE_WIDTH)
    GPIO.output(OFF_PIN, False)

    return "Ok"

if __name__ == "__main__":
    start()
