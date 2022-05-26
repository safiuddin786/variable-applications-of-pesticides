import os

def predictModel(image):
    cmd = "python yolov5/detect.py --weights yolov5/best.pt --source yolov5/"+image
    os.system(cmd)