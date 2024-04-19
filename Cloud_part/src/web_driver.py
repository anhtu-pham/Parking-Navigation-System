#!/usr/bin/env python3

from flask import Flask, request, send_file, Response, render_template
from flask_socketio import SocketIO, emit, Namespace
import io
import os
import base64
import time
import subprocess

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

image_data = None

@socketio.on("connect", namespace="/")
def handle_connect():
	print("Client connected")
	global image_data
	emit("image_update", image_data)

@socketio.on("image_update", namespace="/")
def handle_image_update(data):
	print("Received", data[:20])
	global image_data
	image_data = base64.b64encode(data).decode("utf-8")
	emit("image_update", image_data, broadcast=True)

@app.route("/", methods=["GET", "POST"])
def index():
	global image_data
	if request.method == "POST":
		image_data = request.data
		socketio.emit("image_update", image_data, namespace="/")
		# image_data = base64.b64encode(request.data).decode("utf-8")
	# return send_file(io.BytesIO(image_data), mimetype="image/jpeg")
	return render_template("index.html", image_data=image_data)

def stream_image():
	global image_data
	while True:
		emit("image_update", image_data)
		socketio.sleep(0.5)

if __name__ == "__main__":
	socketio.run(app, host="0.0.0.0", port=5000)
