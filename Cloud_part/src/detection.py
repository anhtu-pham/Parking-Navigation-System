import cv2
import numpy as np
import os

classes = open("model/coco.names").read().strip().split("\n")
net = cv2.dnn.readNetFromDarknet("model/yolov3-tiny.cfg", "model/yolov3-tiny.weights")
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
ln = net.getUnconnectedOutLayersNames()

def perform_object_detection(image_data):
    global classes, net, ln

    np_image = np.frombuffer(image_data, np.uint8)
    image = cv2.imdecode(np_image, cv2.IMREAD_COLOR)
    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416, 416), swapRB=True, crop=False)

    net.setInput(blob)
    outputs = np.vstack(net.forward(ln))

    H, W = image.shape[:2]
    boxes = []
    confidences = []
    classIDs = []
    confidence_threshold = 0.1

    for output in outputs:
        scores = output[5:]
        classID = np.argmax(scores)
        confidence = scores[classID]
        if confidence > confidence_threshold:
            x, y, w, h = output[:4] * np.array([W, H, W, H])
            p0 = int(x - w // 2), int(y - h // 2)
            p1 = int(x + w // 2), int(y + h // 2)
            boxes.append([*p0, int(w), int(h)])
            confidences.append(float(confidence))
            classIDs.append(classID)
            cv2.rectangle(image, p0, p1, (255, 255, 255), 1)

    indices = cv2.dnn.NMSBoxes(boxes, confidences, confidence_threshold, 1-confidence_threshold)
    if len(indices) > 0:
        for i in indices.flatten():
            (x, y) = (boxes[i][0], boxes[i][1])
            (w, h) = (boxes[i][2], boxes[i][3])
            cv2.rectangle(image, (x, y), (x+w, y+h), [0, 0, 255], 2)
            text = "{}: {:.2f}".format(classes[classIDs[i]], confidences[i])
            cv2.putText(image, text, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, [0, 0, 255], 1)
    
    cv2.imwrite(os.getcwd() + "/templates/temp_image.jpg", image)
