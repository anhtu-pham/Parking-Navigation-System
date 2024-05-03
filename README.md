[![openspot_logo](https://github.com/anhtu-pham/Parking-Spot-Detection-System/assets/80482507/90030a02-9d72-4119-b98d-10b9e6fb22ee)](http://ec2-3-223-161-13.compute-1.amazonaws.com:5000/)

# OpenSpot: A Parking Spot Detection System

## Description
OpenSpot is an IoT system that allows users to remotely detect and navigate around obstacles in the parking lot to find open parking spots. Using an image processing solution with a machine learning approach through [YOLO](https://pjreddie.com/darknet/yolo/), OpenSpot will give real-time feedback on parking situations.

As demonstrated in the graph of our project’s system architecture below, a camera attached to the [Raspberry Pi 3 board](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/) captures and streams images of the parking lot. Images, along with corresponding data, are sent from [Raspberry Pi 3 board](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/) through an Amazon Web Services (AWS) t2.micro [EC2 instance](https://aws.amazon.com/ec2/instance-types/?p=itt#general-purpose). This instance type was chosen for economical budget usage and market feasibility of the project. An image processing algorithm finds open parking spots, and the result is shown in real-time on a simple web interface on the user’s device. The system could detect not only the occupying cars, but also other objects that can be present and occupy the parking lots’ spaces, some of which include trucks, buses, bicycles, motorbikes, and humans. This provides users with higher power in detecting a wide variety of obstacles in the parking lot remotely and finding open spots more easily.

Machine learning detection model [YOLO](https://pjreddie.com/darknet/yolo/) can be utilized for the image processing algorithm. Machine learning algorithms usually require large resources, so it would be more efficient to perform this algorithm on the AWS EC2 instance than [Raspberry Pi 3 board](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/) because of the limited resources that the Raspberry Pi 3 board may allow.

## Project Constraints:
1. This project will not account for vibrations and shaking captured in camera images caused by bad weather conditions.
2. With the allowed duration, a simple web user interface was developed to guarantee the system’s deployability. However, more advanced features can still be integrated into the project in the future.


## Hardware and Software Resources
Hardware: [Raspberry Pi 3 board](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/), [Raspberry Pi Camera](https://www.raspberrypi.com/products/camera-module-v3/).

Software: [OpenCV](https://opencv.org), [Socket.IO](https://socket.io), [Flask](https://flask.palletsprojects.com/en/3.0.x/).

## Instructions

In order to run the system, the [Raspberry Pi Camera](https://www.raspberrypi.com/products/camera-module-3/) needs to be attached to [Raspberry Pi 3 board](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/), and setup on AWS EC2 instance terminal should be performed before working with Raspberry Pi 3 terminal.

Follow the following instructions to prepare for receiving requests with images through event-based methodology and updating real-time image display on website.

On the AWS EC2 instance terminal, clone the repository, and change to directory for Cloud (AWS EC2 instance) in the repository:
```
git clone git@github.com:anhtu-pham/Parking-Spot-Detection-System.git
cd Parking-Spot-Detection-System/Cloud_part/
```
In this directory, src provides the entire program needed to run for AWS EC2 instance. Change directory into src, provide executable permission for web_driver.py, then run this file.
```
cd src/
chmod a+x web_driver.py
./web_driver.py
```

After running on AWS EC2 instance terminal, open up another terminal for Raspberry Pi 3 terminal, and follow the following instructions to continuously capture images in real time from Raspberry Pi 3 board and send requests with images to AWS EC2 instance.

On Raspberry Pi 3 terminal, clone the repository again, but now change to directory for Raspberry Pi in the repository:
```
git clone git@github.com:anhtu-pham/Parking-Spot-Detection-System.git
cd Parking-Spot-Detection-System/Raspberry_Pi_part/
```
In this directory, src provides the entire program needed to run for the Raspberry Pi 3 board. Now change directory into src, provide executable permission for driver.py, then run this file.
```
cd src/
chmod a+x driver.py
./driver.py
```
The website is now ready. Image streaming can be seen in website link: http://ec2-3-223-161-13.compute-1.amazonaws.com:5000/.
