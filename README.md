# Paint Defect Detection System using Machine Learning

## Project Overview

The Paint Defect Detection System is a machine learning-based application designed to automatically identify and classify surface defects in metal sheets. The system extracts color histogram features from images and uses machine learning algorithms to predict the defect category.

The project was developed as an end-to-end solution, covering data preprocessing, feature extraction, model training, evaluation, and deployment through an interactive Streamlit web application.

---

## Problem Statement

Manual inspection of industrial metal surfaces is time-consuming, expensive, and prone to human error. Defective products can lead to quality issues and increased manufacturing costs.

This project aims to automate defect detection using machine learning techniques, enabling faster and more reliable quality inspection.

---

## Dataset

Dataset: NEU Surface Defect Database

### Dataset Statistics

* Total Images: 1800
* Number of Classes: 6
* Images per Class: 300
* Dataset Type: Balanced

### Defect Classes

1. Crazing
2. Inclusion
3. Patches
4. Pitted Surface
5. Rolled-in Scale
6. Scratches

---

## Project Workflow

Image Input
↓
Image Preprocessing
↓
Color Histogram Feature Extraction
(96 Features)
↓
Feature Normalization
↓
Train-Test Split
↓
Decision Tree / Random Forest
↓
Model Evaluation
↓
Streamlit Web Application
↓
Defect Prediction

---

## Feature Extraction

Color Histogram was used to represent each image as a numerical feature vector.

### Histogram Configuration

* Red Channel: 32 bins
* Green Channel: 32 bins
* Blue Channel: 32 bins

Total Features:

96 Features = 32 + 32 + 32

The extracted histogram features were normalized before training the machine learning models.

---

## Machine Learning Models

### Decision Tree Classifier

The Decision Tree model serves as the primary classification algorithm.

**Accuracy:** 93%

### Random Forest Classifier

An ensemble learning approach using 100 decision trees was implemented to improve classification performance.

**Parameters:**

* n_estimators = 100
* random_state = 42

**Accuracy:** 95%

---

## Performance Comparison

| Model         | Accuracy |
| ------------- | -------- |
| Decision Tree | 93%      |
| Random Forest | 95%      |

Random Forest achieved higher accuracy by reducing overfitting and improving generalization performance.

---

## Web Application

The trained model was deployed using Streamlit, allowing users to interact with the system through a simple web interface.

### Features

* Upload defect images
* Automatic feature extraction
* Real-time defect prediction
* Support for six defect categories
* User-friendly interface
* Fast prediction results

---

## Prediction Output

The system predicts one of the following defect classes:

* Crazing
* Inclusion
* Patches
* Pitted Surface
* Rolled-in Scale
* Scratches

The application displays the predicted defect category immediately after image upload and analysis.

---

## Technologies Used

### Programming Language

* Python

### Libraries

* OpenCV
* NumPy
* Scikit-Learn
* Joblib
* Streamlit
* Matplotlib
* Seaborn

---

## Project Structure

```text
paint-defect-detection/
│
├── app.py
├── Paint_Defect_Detection_Model.pkl
├── Paint_Defect_Detection.ipynb
├── README.md
├── dataset/
│
├── images/
│
└── requirements.txt
```

---

## Installation

Clone the repository:

```bash
git clone <repository-link>
cd paint-defect-detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## Results

* Decision Tree achieved 93% classification accuracy.
* Random Forest achieved 95% classification accuracy.
* The model successfully classifies six different surface defect categories.
* Streamlit deployment enables real-time prediction through a web interface.

---

## Key Learnings

* Image data can be represented using color histogram features.
* Feature normalization improves model performance.
* Ensemble models such as Random Forest provide better accuracy than a single Decision Tree.
* Streamlit simplifies machine learning model deployment.
* End-to-end machine learning projects require data preprocessing, model development, evaluation, and deployment.

---

## Author

Keerthanadevi Baskaran

Machine Learning | Computer Vision | Artificial Intelligence
