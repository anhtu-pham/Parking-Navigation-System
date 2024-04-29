#!/usr/bin/env python3

import subprocess
import os

def run_yolov5_detection(video_path):
    yolov5_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "yolov5")
    detect_script = os.path.join(yolov5_path, "detect.py")
    command = f"python3 {detect_script} --source {video_path}"
    process = subprocess.Popen(command, shell=True)
    process.communicate()

# Example usage
video_path = "/home/ubuntu/Parking-Spot-Detection-System/parking_lot_1.mp4"
run_yolov5_detection(video_path)

