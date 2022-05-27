from unittest import result
import torch

def predictModel(image):
    #     return results.pandas().xyxy[0]
    model = torch.hub.load('ultralytics/yolov5:master', 'custom', 'best.pt') 
    # Inference
    results = model(image)
    # Results, change the flowing to: results.show()
    # or .show(), .save(), .crop(), .pandas(), etc
    # print(results.pandas().xyxy[0])

    confidence = results.pandas().xyxy[0]['confidence'].tolist()
    name = results.pandas().xyxy[0]['name'].tolist()
    disease_class = results.pandas().xyxy[0]['class'].tolist()

    # print(confidence, " ", name, " ", disease_class)


    return {
        "confidence": confidence,
        "class": disease_class,
        "name": name
    }




# model = torch.hub.load('ultralytics/yolov5:master', 'custom', 'yolov5/best.pt') 
# # Inference
# results = model('yolov5/tomato.jpeg')
# # Results, change the flowing to: results.show()
# # or .show(), .save(), .crop(), .pandas(), etc
# # print(results.pandas().xyxy[0])

# confidence = results.pandas().xyxy[0]['confidence'].tolist()
# name = results.pandas().xyxy[0]['name'].tolist()
# disease_class = results.pandas().xyxy[0]['class'].tolist()

# # print(confidence, " ", name, " ", disease_class)