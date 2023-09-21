#Dataset Link - https://public.roboflow.com/object-detection/american-sign-language-letters/1


from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch


# Use the model
model.train(data="data.yaml", epochs=3)  # train the model
