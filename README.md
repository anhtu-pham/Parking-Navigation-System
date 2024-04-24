[![logo](https://github.com/anhtu-pham/Parking-Spot-Detection-System/assets/80482507/bc1b2c64-1eb6-4a13-97fa-1d3123521899)](http://ec2-54-225-46-150.compute-1.amazonaws.com:8000/)

# OpenSpot: A Parking Spot Detection System

## Description
OpenSpot is an IoT system that allows users to find an open parking spot in parking lots. Using an image processing solution with a machine learning approach through [YOLO](https://pjreddie.com/darknet/yolo/), OpenSpot will give real-time feedback on parking situations.

As shown in the graph of our project’s system architecture below, a camera attached to the [Raspberry Pi 3 board](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/) captures and streams images of the parking lot. Images, along with corresponding data, are sent from [Raspberry Pi 3 board](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/) through an Amazon Web Services (AWS) t2.micro [EC2 instance](https://aws.amazon.com/ec2/instance-types/?p=itt#general-purpose). An image processing algorithm finds open parking spots, and the result is shown in real-time on a simple web interface on the user’s device.

A machine learning detection model like [YOLO](https://pjreddie.com/darknet/yolo/) can be utilized for the image processing algorithm. Machine learning algorithms usually require large resources, so it would be more efficient to perform this algorithm on the AWS EC2 instance than [Raspberry Pi 3 board](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/) because of the limited resources that Raspberry Pi may allow.

## Project Constraints:
1. This project will not account for vibrations and shaking captured in camera images caused by bad weather conditions.
2. This project will detect parking spots for medium cars as the exemplification of an arbitrary car.
3. With the allowed duration, we develop fundamental functionalities with a simple user interface to guarantee the system’s deployability. However, we still allow for more advanced features to be integrated into the project in the future.


## Hardware and Software Resources
Hardware: [Raspberry Pi 3 board](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/), [Raspberry Pi Camera](https://www.raspberrypi.com/products/camera-module-v3/).

Software: [OpenCV](https://opencv.org), [Socket.IO](https://socket.io), [Flask](https://flask.palletsprojects.com/en/3.0.x/).
