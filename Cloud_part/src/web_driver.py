#!/usr/bin/env python3

from flask import Flask, request, send_file, Response, render_template
from flask_socketio import SocketIO, emit, Namespace
import io
import os
import base64
import time
import subprocess
from detection import perform_object_detection
import cv2

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

image_data = None

@socketio.on("connect", namespace="/")
def handle_connect():
	print("Client connected")
	# emit("image_update", image_data)

@socketio.on("image_update", namespace="/")
def handle_image_update(data):
	print("Image received")
	perform_object_detection(data)
	socketio.emit("upload", namespace="/")

@app.route("/image")
def serve_image():
	return send_file(os.getcwd() + "/templates/temp_image.jpg", mimetype="image/jpeg")

@app.route("/", methods=["GET", "POST"])
def index():
	global image_data
	if request.method == "POST":
		image_data = request.data
		socketio.emit("image_update", image_data, namespace="/")
	return render_template("index.html")

if __name__ == "__main__":
	socketio.run(app, host="0.0.0.0", port=5000)
