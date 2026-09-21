# 📦 Warehouse Package Detection & Counting using YOLO11

## 📌 Project Overview

This project develops a Computer Vision application for automatically detecting and counting packages in warehouse images.

A YOLO11 object detection model is trained on a warehouse parcel dataset and integrated into a Streamlit web application.

Users can upload a warehouse image and receive:

- 📦 Automatic package detection
- 🔢 Package count
- 🎯 Confidence scores
- 🖼️ Bounding-box visualization
- 📊 Average detection confidence

---

## 🎯 Problem Statement

Manual package counting and monitoring in warehouses can be time-consuming and inefficient.

This project uses deep learning-based object detection to automate package identification and counting from images.

---

## 🧠 Technology Used

- Python
- YOLO11
- Ultralytics
- Computer Vision
- Deep Learning
- Streamlit
- Roboflow
- Google Colab
- GitHub

---

## 📊 Dataset

The project uses a warehouse parcel image dataset prepared using Roboflow.

### Dataset Configuration

- Total images: 2,341
- Object class: Package
- Image size: 640 × 640
- Task: Object Detection
- Dataset format: YOLO

The original dataset contained `box` and `fragile` classes. These were merged into a single `Package` class for this project.

---

## 🚀 Model Training

Model:

**YOLO11n**

Training configuration:

- Epochs: 50
- Image size: 640 × 640
- Batch size: 16
- GPU: NVIDIA Tesla T4
- Confidence threshold for application: 0.40

---

## 📈 Model Performance

### Test Set Results

| Metric | Score |
|---|---:|
| Precision | 94.4% |
| Recall | 86.7% |
| mAP@50 | 92.3% |
| mAP@50–95 | 85.1% |

The model was evaluated on 245 usable test images containing 386 package instances.

---

## 🖥️ Streamlit Application

The trained YOLO11 model is integrated into a Streamlit application.

### Application Workflow

```text
Upload Warehouse Image
          ↓
      YOLO11 Model
          ↓
   Package Detection
          ↓
 Bounding Boxes + Confidence
          ↓
     Package Count
📂 Project Structure
warehouse-package-detection-yolo/
│
├── app.py
├── best.pt
├── requirements.txt
└── README.md
▶️ Run Locally

Install the required packages:

python -m pip install -r requirements.txt

Run the application:

python -m streamlit run app.py

Open the local Streamlit URL displayed in the terminal.

💡 Key Features
1. Image Upload

Users can upload JPG, JPEG, or PNG warehouse images.

2. Package Detection

YOLO11 identifies packages and draws bounding boxes around detected objects.

3. Package Counting

The application automatically counts the detected package instances.

4. Confidence Analysis

The application displays the confidence score for each detected package and calculates the average confidence.

5. Adjustable Threshold

Users can adjust the detection confidence threshold using the sidebar.

🔬 Computer Vision Pipeline
Dataset Collection
       ↓
Class Consolidation
       ↓
Image Preprocessing
       ↓
YOLO11 Training
       ↓
Model Validation
       ↓
Test Evaluation
       ↓
Prediction
       ↓
Streamlit Deployment
📌 Project Outcome

The final system demonstrates how deep learning and Computer Vision can be applied to warehouse automation.

The trained model successfully detects packages in unseen test images and provides automated package counting through a user-friendly Streamlit interface.

👩‍💻 Author

Pallavi

Data Science & Computer Vision Portfolio Project


### Step 13 — Save README

Scroll down and click:

**Commit changes**

After that, your repository should contain:

```text
📦 warehouse-package-detection-yolo

├── app.py
├── best.pt
├── requirements.txt
└── README.md📂 Project Structure
warehouse-package-detection-yolo/
│
├── app.py
├── best.pt
├── requirements.txt
└── README.md
▶️ Run Locally

Install the required packages:

python -m pip install -r requirements.txt

Run the application:

python -m streamlit run app.py

Open the local Streamlit URL displayed in the terminal.

💡 Key Features
1. Image Upload

Users can upload JPG, JPEG, or PNG warehouse images.

2. Package Detection

YOLO11 identifies packages and draws bounding boxes around detected objects.

3. Package Counting

The application automatically counts the detected package instances.

4. Confidence Analysis

The application displays the confidence score for each detected package and calculates the average confidence.

5. Adjustable Threshold

Users can adjust the detection confidence threshold using the sidebar.

🔬 Computer Vision Pipeline
Dataset Collection
       ↓
Class Consolidation
       ↓
Image Preprocessing
       ↓
YOLO11 Training
       ↓
Model Validation
       ↓
Test Evaluation
       ↓
Prediction
       ↓
Streamlit Deployment
📌 Project Outcome

The final system demonstrates how deep learning and Computer Vision can be applied to warehouse automation.

The trained model successfully detects packages in unseen test images and provides automated package counting through a user-friendly Streamlit interface.

👩‍💻 Author

Pallavi

Data Science & Computer Vision Portfolio Project



