from ultralytics import YOLO
# model = YOLO("yolo11n.pt")
# results = model.train(data= r"E:\Infosys Training\Detection Model\data.yaml", epochs=25, imgsz=640)
model = YOLO(r"E:\Infosys Training\runs\detect\train3\weights\best.pt")

metrics = model.val()
metrics.box.map
metrics.box.map50
metrics.box.map75
metrics.box.maps

# predict on a single image
results = model(r"E:\Infosys Training\Classification Model\Classification Dataset\train\aadhar\1.jpg")

metrics = model.val()
print(metrics.box.map)