# 🛡️ AI-Based Fraud Management System

An AI-driven system developed with Python and deep learning models to detect fraudulent activities through text and image analysis, leveraging OCR, classification models, and YOLO object detection.

---

## 🔍 Features
- **Text Analysis (OCR)**: Extract text from documents and analyze for fraud patterns.
- **Image Detection (YOLO)**: Detect fraudulent signatures, stamps, and tampering in documents.
- **Classification Model**: Classify transactions or documents as legitimate or fraudulent.
- **User Database**: Manage user accounts securely with SQLite (`users.db`).
- **Web Interface**: Organized directories for uploads, results, and model predictions.

---

## 🛠️ System Architecture
- OCR → Text extraction
- Classification Model → Text-based fraud detection
- YOLO Model → Image-based fraud detection
- Flask / Local scripts → Serve models and interface with users
- SQLite DB → Store user and prediction data

---

## 📋 Prerequisites
- Python 3.8+
- Flask
- PyTorch / TensorFlow
- Tesseract OCR
- OpenCV
- SQLite3
- Transformers (for text models)
- YOLO (for image detection)

---

## 🚀 Installation

Clone the repository:
```bash
git clone https://github.com/AlvinaSaxena/AI-Based-Fraud-Management-System.git
cd AI-Based-Fraud-Management-System
```

Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the dependencies:
```bash
pip install -r requirements.txt
```

---

## 📂 Project Structure
```
AI-Based-Fraud-Management-System/
├── OCR/                    # OCR models and scripts
├── Classification Model/   # Fraud classification models
├── Detection Model/        # YOLO object detection models
├── uploads/                # Upload folder for files
├── results/                # Output predictions
├── users.db                # User database
├── project/                # Main project configurations
├── runs/                   # YOLO training runs
└── README.md               # Project documentation
```

---

## 🏃‍♂️ Running the Application
Ensure OCR models, classification models, and YOLO detection models are ready.

Start the application:
```bash
python app.py
```

Access it in your browser:
```
http://localhost:5000
```

---

## 🔄 API Endpoints
| Endpoint         | Description                              |
|------------------|------------------------------------------|
| `/upload`        | Upload files for fraud analysis          |
| `/predict_text`  | Predict fraud from text input            |
| `/predict_image` | Detect fraud objects from uploaded image |
| `/results`       | View analysis reports                   |

---

## 📊 Models
- **OCR Module**: Extracts clean text from images for analysis.
- **Classification Model**: 
  - Input: Text data
  - Output: Fraud / No Fraud prediction
- **YOLOv5 Detection Model**: 
  - Input: Document images
  - Output: Bounding boxes around fraud markers (fake seals, signatures, etc.)

---

## 💻 Usage Example

**Text Prediction**
```python
from classification_module import predict_text

text = "Suspicious transaction details..."
prediction, confidence = predict_text(text)
print(f"Prediction: {prediction} (Confidence: {confidence:.2f}%)")
```

**Image Detection**
```python
from detection_module import detect_fraud_in_image

image_path = "uploads/document.jpg"
result = detect_fraud_in_image(image_path)
print(f"Detected: {result}")
```

---

## 🤝 Contributing
- Fork the repo
- Create your feature branch (`git checkout -b feature/AmazingFeature`)
- Commit your changes (`git commit -m 'Add some AmazingFeature'`)
- Push to the branch (`git push origin feature/AmazingFeature`)
- Open a Pull Request

---

## ⚖️ License
This project is licensed under the **MIT License**.

---

## 📧 Contact
- **GitHub**: [@AlvinaSaxena](https://github.com/AlvinaSaxena)
- **Project Link**: [AI-Based Fraud Management System](https://github.com/AlvinaSaxena/AI-Based-Fraud-Management-System)

---

## 🙏 Acknowledgments
- Hugging Face Transformers
- YOLOv5 for object detection
- Tesseract OCR
- Flask for rapid development
- Kaggle datasets for training models

---
