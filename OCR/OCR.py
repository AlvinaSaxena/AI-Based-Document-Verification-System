from ultralytics import YOLO
import easyocr, cv2
model = YOLO(r"E:\Infosys Training\runs\detect\train3\weights\best.pt") 
reader = easyocr.Reader(['en'])

image_path = r"E:\Infosys Training\Classification Model\Classification Dataset\train\aadhar\1.jpg" 
results = model(image_path)

image=cv2.imread(image_path)
extracted_data={}

for result in results[0].boxes.data.tolist():   # results[0].boxes.data contains bounding box details
    x1,y1,x2,y2,confidence,class_id= map(int, result[:6])
    field_class= model.names[class_id]    # Get class name(e.g. 'NAme', 'UID', 'Address')

    # Crop the detected region
    cropped_roi= image[y1:y2, x1:x2]

    # Convert cropped ROI to grayscale for OCR
    gray_roi= cv2.cvtColor(cropped_roi, cv2.COLOR_BGR2GRAY)

    # Use EasyOCR to extract text
    text= reader.readtext(gray_roi, detail=0)   #details=0 returns only the text

    # Save the text to the extracted_data dictionary
    extracted_data[field_class]= ''.join(text)

print("Extracted Data:", extracted_data)

    
