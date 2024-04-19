#!/usr/bin/env python3

import os
import time
from picamera import PiCamera
import requests
from io import BytesIO
import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("Connected")

@sio.event
def disconnect():
    print("Disconnected")

camera = PiCamera()
ec2_instance_url = "http://3.223.161.13:5000/"
camera.start_preview(alpha=255)
stream = BytesIO()

sio.connect(ec2_instance_url)

for _ in camera.capture_continuous(stream, format="jpeg", use_video_port=True):
    stream.seek(0)
    image = stream.read()
    try:
        response = requests.post(ec2_instance_url, data=image, headers={"Content-Type": "image/jpeg"})
        if response.status_code == 200:
            sio.emit("image_update", image, namespace="/")
            print("Sent successfully Image sent: " + str(image)[:20])
        else:
            print("Failed to send")
    except Exception as e:
        print("Error:", e)
    # files = {"image": ("~/parking_web/images/image.jpg", stream.getvalue())}
    # response = requests.post(ec2_instance_url, files=files)
    stream.seek(0)
    stream.truncate()
    time.sleep(1.5)
