# 🎨 Paint Defect Detection System using Machine Learning & Agentic AI

## Project Overview

The **Paint Defect Detection System** is a Machine Learning and Agentic AI-based application that automatically detects and classifies surface defects in steel sheets. The system extracts color histogram features from uploaded images and uses a trained **Random Forest Classifier** to predict the defect category.

To demonstrate modern AI application development, the project also integrates **Agentic AI concepts** including **Skills, Agents, Prompts, Instructions, and Hooks**, making the application modular, reusable, and extensible.

---

# Problem Statement

Manual inspection of industrial metal surfaces is time-consuming, expensive, and prone to human error. Defective products can lead to quality issues and increased manufacturing costs.

This project automates defect detection using Machine Learning while demonstrating how **Agentic AI components** can organize and enhance AI workflows.

---

# Dataset

**Dataset:** NEU Surface Defect Database

### Dataset Statistics

* Total Images: **1800**
* Number of Classes: **6**
* Images per Class: **300**
* Dataset Type: **Balanced**

### Defect Classes

* Crazing
* Inclusion
* Patches
* Pitted Surface
* Rolled-in Scale
* Scratches

---

# Project Workflow

```text
Upload Image
        │
        ▼
🪝 Preprocessing Hook
        │
        ▼
Feature Extraction
(Color Histogram - 96 Features)
        │
        ▼
Feature Normalization
        │
        ▼
Random Forest Model
        │
        ▼
Defect Prediction
        │
        ▼
🤖 Paint Detection Agent
        │
        ▼
AI Analysis Report
```

---

# Machine Learning Model

# Decision Tree Classifier

The Decision Tree model serves as the primary classification algorithm.

* Accuracy: **93%**

## Random Forest Classifier

* Algorithm: Random Forest
* Accuracy: **94.79%**
* Number of Classes: 6

The model predicts one of the six surface defect categories based on extracted color histogram features.

---

# Agentic AI Components

This project demonstrates the integration of **Agentic AI** concepts into a Machine Learning application.

## 🧠 Skill

**Paint Defect Detection Skill**

Defines the AI's specialization in analyzing paint and surface defects and generating structured defect reports.

---

## 🤖 Agent

**Paint Detection Agent**

Responsible for generating an intelligent analysis report after the machine learning model predicts the defect.

---

## 📝 Prompt

**Defect Analysis Prompt**

Provides structured instructions to the agent for generating meaningful explanations based on the predicted defect.

---

## 📋 Instructions

Project-specific rules that define how the AI agent should respond, including report formatting and analysis behavior.

---

## 🪝 Hook

**Preprocessing Hook**

Automatically executes before prediction by preprocessing the uploaded image, demonstrating automated workflow execution.

---

# Features

* Upload steel surface images
* Automatic preprocessing using Hooks
* Color histogram feature extraction
* Random Forest and Decision Tree prediction
* AI-generated analysis report
* Streamlit web interface
* Modular Agentic AI architecture

---

# Technologies Used

### Programming Language

* Python

### Machine Learning

* Scikit-Learn
* Random Forest Classifier

### Libraries

* OpenCV
* NumPy
* Joblib
* Streamlit
* Pillow

---

# Project Structure

```text
Paint_Defect_Detection_System/
│
├── app.py
├── Paint_Defect_Detection_Model.pkl
├── requirements.txt
├── README.md
│
├── agents/
│   ├── paint_detection_agent.py
│   └── paint_detection_agent.md
│
├── hooks/
│   └── preprocess_hook.py
│
├── skills/
│   └── SKILL.md
│
├── prompts/
│   └── defect_prompts.md
│
├── instructions/
│   └── instructions.md
│
├── Paint_Defect_Detection.ipynb
└── check_model.py
```

---

# Installation

Clone the repository

```bash
git clone https://github.com/KeerthanadeviBaskaran/Paint_Defect_Detection_System.git
```

Move into the project folder

```bash
cd Paint_Defect_Detection_System
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the Streamlit application

```bash
streamlit run app.py
```

---

# Results

* Random Forest achieved **94.79%** accuracy.
* Successfully classifies six steel surface defect categories.
* Real-time prediction using Streamlit.
* Generates an AI analysis report using an Agent.
* Demonstrates Skills, Prompts, Instructions, and Hooks within an Agentic AI workflow.

---

# Future Enhancements

* Add a **Normal (No Defect)** class.
* Integrate Gemini/OpenAI for advanced AI-generated reports.
* Implement an MCP Server for external tool integration.
* Support multiple defect detection within a single image.
* Add confidence score visualization.

---

# Author

**Keerthanadevi Baskaran**

Machine Learning | Artificial Intelligence | Computer Vision | Agentic AI
