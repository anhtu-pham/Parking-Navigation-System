![logo](https://github.com/anhtu-pham/Parking-Spot-Detection-System/assets/80482507/bc1b2c64-1eb6-4a13-97fa-1d3123521899)

# OPENSPOT: A Parking Spot Detection System

## Description
OpenSpot is an IoT system that allows users to find an open parking spot in parking lots. Using an image processing solution with a machine learning approach through YOLO, OpenSpot will give real-time feedback on parking situations.

As shown in the graph of our project’s system architecture below, a camera attached to the LAMPI captures and streams images of the parking lot. Images, along with corresponding data, are sent from LAMPI through Amazon Web Services (AWS) EC2. An image processing algorithm finds open parking spots, and the result is shown in real-time on a simple web interface on the user’s device.

A machine learning detection model like YOLO can be utilized for the image processing algorithm. Machine learning algorithms usually require large resources, so it would be more efficient to perform this algorithm on the AWS EC2 instance than LAMPI because of the limited resources that Raspberry Pi may allow.


## Project Progress
### Accomplishments:
1. Captured images in real-time from the PI camera
2. Stream images to AWS EC2 instance.
3. Developed a simple front-end website to display streamed images.
4. An automatically changed image is displayed on the website as it is streamed.

### Remaining Tasks:
1. Perform detection on images on the AWS EC2 instance using YOLO algorithm.
2. Add functionality to the front-end website.
3. Perform system testing for the final product.

![Interface](https://github.com/anhtu-pham/Parking-Spot-Detection-System/assets/80482507/e1c6f5e8-dabc-4c22-a5a5-a8023193c4e0)


As shown above, we decided to update our midpoint goal to focus on streaming images from the Raspberry Pi Camera to the website for two main reasons:
1. This is the core functionality, the “skeleton” of the project. It includes all the essential steps, including capturing images, connecting with the AWS EC2 instance, sending images through real-time requests from the Raspberry Pi in the LAMPI to the AWS EC2 instance with event-driven methodology, and showing real-time images on the website.
2. The remaining work is to add the detection algorithm, improve the website, and perform testing.

In this project, this functionality is most aligned with concepts that we have been learning and applying in this course regarding IoT. The remaining functionalities are used to wrap around this core to construct the final product.

## Project Constraints:
1. This project will not account for vibrations and shaking captured in camera images caused by bad weather conditions.
2. This project will detect parking spots for medium cars as the exemplification of an arbitrary car.
3. With the allowed duration, we develop fundamental functionalities with a simple user interface to guarantee the system’s deployability. However, we still allow for more advanced features to be integrated into the project in the future.


## Hardware and Software Resources
Hardware: LAMPI with Raspberry Pi board, Raspberry Pi Camera.

Software: OpenCV, Socket.IO, Flask.

## Project Plan for the Next Steps
1. Develop image processing and examine with test images.
2. Develop real-time image processing for images captured by the camera.
3. Improve the Web interface that we currently have for the system.
4. Perform system testing and deploy the system.

