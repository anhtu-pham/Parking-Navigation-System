#!/usr/bin/env python3

import subprocess
import os
from flask import Flask, render_template, Response

app = Flask(__name__)

def generate_frames(video_path):
    yolov5_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../../yolov5")
    detect_script = os.path.join(yolov5_path, "detect.py")
    command = f"python3 {detect_script} --source {video_path} --mjpeg"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    while True:
        frame = process.stdout.read(1024)
        if not frame:
            break
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    video_path = "/home/ubuntu/Parking-Spot-Detection-System/parking_lot_1.mp4"
    return Response(generate_frames(video_path), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
