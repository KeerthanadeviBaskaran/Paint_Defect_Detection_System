# Paint Defect Detection System

## Project Overview

This project automatically detects and classifies surface defects on metal sheets using **Color Histogram** as the feature extraction technique and **Decision Tree** as the classification model. Random Forest was also explored as an improvement on top of the base Decision Tree.

It is built as a complete end-to-end project — from raw image data all the way to a working web app where anyone can upload an image and get a prediction.

## Problem Statement

In manufacturing, metal sheets often come out of production with surface defects. Manually inspecting every sheet is slow, inconsistent, and error-prone. This project automates that inspection using a machine learning model trained on real defect images.

## Dataset

**NEU Surface Defect Dataset** (Kaggle)

- Total images      : 1800
- Classes           : 6 defect types
- Images per class  : 300 (perfectly balanced)

| Defect Type     |
|-----------------|
| Crazing         |
| Inclusion       |
| Patches         |
| Pitted Surface  |
| Rolled-in Scale |
| Scratches       |

## Core Techniques

| Step               | Technique                                        |
|--------------------|--------------------------------------------------|
| Feature Extraction | Color Histogram (RGB, 32 bins × 3 channels = 96 features)|
| Core Model         | Decision Tree Classifier                         |
| Improved Model     | Random Forest (100 Decision Trees voting together)|
| Evaluation         | Accuracy, Precision, Recall, Confusion Matrix    |

## Workflow

Raw Image
   ↓
Color Histogram Extraction (96 features: 32 bins × 3 channels)
   ↓
Normalize Feature Vector
   ↓
Train / Test Split (80% train, 20% test)
   ↓
Decision Tree Classifier  ←── Core technique
   ↓
Random Forest (optional improvement)
   ↓
Evaluate on unseen images

## Results

| Model                      | Accuracy |
|----------------------------|----------|
| Decision Tree (core model) | 93%      |
| Random Forest (improved)   | 95%      |

The core project uses Decision Tree with Color Histogram features and achieves **93% accuracy**. Random Forest was explored as an extension and pushed accuracy to **95%** by combining 100 trees voting together.

## Output

The model predicts one of 6 defect classes:

- Crazing
- Inclusion
- Patches
- Pitted Surface
- Rolled-in Scale
- Scratches

Along with a **confidence score** for each class (e.g. "Scratches — 87% confidence").

## How to Run

1. Open the notebook in Google Colab
2. Mount Google Drive and set the dataset path
3. Run all cells from top to bottom
4. Cell 26 launches the Gradio app with a public shareable link
5. Upload any NEU defect image — the model returns the defect type instantly

## Libraries Used

- opencv-python — image loading and histogram extraction
- numpy — array operations
- scikit-learn — Decision Tree, Random Forest, evaluation metrics
- matplotlib / seaborn — charts and confusion matrix
- joblib — saving and loading the trained model

## Project Structure

paint_defect_detection_project/
├── Paint_Defect_Detection.ipynb # main Colab notebook
├── paint_defect_model.pkl # saved Decision Tree / Random Forest model
├── class_names.json       # class label names
└── README.md              # this file

## Key Learnings

- Images can be represented as compact feature vectors using color histograms
- Decision Tree alone achieves strong results (93%) on this task
- Random Forest improves accuracy further by reducing overfitting
- Balanced datasets lead to fairer and more reliable models
