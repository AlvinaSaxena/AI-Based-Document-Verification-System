from ultralytics import YOLO
# model = YOLO("yolo11n-cls.pt")
# results = model.train(data= r"E:\Infosys Training\Classification Model\Classification Dataset", epochs=12, imgsz=640, batch=8)
# model = YOLO("runs/classify/train/weights/best.pt")

model = YOLO(r"E:\Infosys Training\runs\classify\train\weights\best.pt")
results = model.predict(source=r"E:\Web Development\DetectAI\static\robot.png")
if results:
    results[0].show()
else:
    print("error")