# 🎨 Paint Defect Detection System with Machine Learning & Agentic AI Skills

## 🚀 Project Overview

The **Paint Defect Detection System** is a Machine Learning and Agentic AI-based application that automatically detects and classifies surface defects in steel sheets. The system extracts color histogram features from uploaded images and uses a trained **Random Forest Classifier** to predict the defect category.

Beyond traditional Machine Learning, this project demonstrates the integration of **Agentic AI concepts**, including **Agents, Skills, Prompts, Instructions, and Hooks**, making the application modular, reusable, explainable, and extensible.

In addition, this repository includes a **Project Analysis Skill** capable of analyzing any software project and generating a comprehensive Markdown report. Together, these skills demonstrate how AI agents can perform specialized tasks through reusable capabilities.

---

# 🎯 Problem Statement

Manual inspection of industrial metal surfaces is time-consuming, expensive, and prone to human error. Defective products can lead to quality issues, production delays, and increased manufacturing costs.

This project automates defect detection using Machine Learning while showcasing how **Agentic AI Skills** can organize complex AI workflows into reusable, maintainable components.

---

# 📂 Dataset

**Dataset:** NEU Surface Defect Database

## Dataset Statistics

- **Total Images:** 1800
- **Number of Classes:** 6
- **Images per Class:** 300
- **Dataset Type:** Balanced

## Defect Classes

- Crazing
- Inclusion
- Patches
- Pitted Surface
- Rolled-in Scale
- Scratches

---

# 🔄 Project Workflow

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
Random Forest Classifier
        │
        ▼
Defect Prediction
        │
        ▼
🤖 Paint Detection Agent
        │
        ▼
📄 AI Analysis Report
```

---

# 🤖 Machine Learning Models

## Decision Tree Classifier

The Decision Tree model serves as the baseline classification algorithm.

- Accuracy: **93%**

---

## Random Forest Classifier

The Random Forest model is the primary prediction model used in the application.

### Model Details

- Algorithm: Random Forest
- Accuracy: **94.79%**
- Number of Classes: **6**
- Feature Extraction: **96-Dimensional Color Histogram**

The trained model predicts one of the six steel surface defect categories from uploaded images.

---
# 🤖 Agentic AI Components

This project demonstrates the integration of **Agentic AI** concepts into a Machine Learning application. Instead of using AI only for prediction, the project organizes intelligence into reusable components such as **Agents, Skills, Prompts, Instructions, and Hooks**.

---

## 🧠 AI Skills

This repository contains two reusable AI Skills that demonstrate how an AI Agent can perform specialized tasks.

### 🎨 Paint Defect Detection Skill

**Location**

```text
paint-defect-skill/SKILL.md
```

#### Purpose

The **Paint Defect Detection Skill** enables an AI Agent to analyze predicted steel surface defects and generate a structured, human-readable analysis report.

#### Capabilities

- Analyze predicted defect category
- Explain the detected defect
- Describe possible causes
- Estimate industrial impact
- Suggest preventive measures
- Generate a structured Markdown report

#### Input

- Predicted defect class from the Machine Learning model

#### Output

- AI-generated Paint Defect Analysis Report

---

### 📊 Project Analysis Skill

**Location**

```text
project-analysis/SKILL.md
```

#### Purpose

The **Project Analysis Skill** enables an AI Agent to analyze any software project and automatically generate a comprehensive Markdown report.

The skill is designed to work with multiple programming languages and frameworks without requiring project-specific customization.

#### Analysis Includes

- Project Overview
- Project Purpose
- Programming Languages
- Frameworks & Technologies
- Software Architecture
- Features & Functionalities
- Dependencies
- APIs
- Database Analysis
- Security Implementation
- Code Structure
- Design Patterns
- Build Process
- Deployment Process
- Strengths
- Weaknesses
- Improvement Suggestions

#### Input

- Source Code Repository
- Local Project Folder
- ZIP Archive

#### Output

- Comprehensive Markdown Project Analysis Report

---

# 🤖 AI Agent

### Paint Detection Agent

The **Paint Detection Agent** is responsible for generating intelligent explanations after the Machine Learning model predicts the surface defect.

Instead of simply displaying the predicted class, the agent provides contextual insights including:

- Defect explanation
- Possible causes
- Industrial impact
- Recommended actions
- AI-generated report

---

# 📝 Prompt

### Defect Analysis Prompt

The prompt provides structured guidance to the AI Agent for generating meaningful explanations based on the predicted defect.

It ensures responses remain:

- Accurate
- Consistent
- Structured
- Human-readable

---

# 📋 Instructions

Project-specific instructions define how the AI Agent should behave.

Examples include:

- Always return Markdown output.
- Explain detected defects clearly.
- Never modify user data.
- Maintain consistent report formatting.
- Use evidence-based reasoning.

---

# 🪝 Hook

### Preprocessing Hook

The preprocessing hook automatically executes before prediction.

Responsibilities include:

- Image validation
- Image resizing
- Feature extraction
- Feature normalization

This demonstrates automatic workflow execution before the AI Agent begins reasoning.

---

# 📄 AI Generated Reports

This repository includes sample reports generated by the AI Skills.

---

## 🎨 Paint Defect Detection Report

**File**

```text
PAINT_DEFECT_DETECTION_REPORT.md
```

This report demonstrates the structured output generated by the **Paint Defect Detection Skill**, including defect explanation, industrial impact, and recommendations.

---

## 📊 Project Analysis Report

**File**

```text
PROJECT_ANALYSIS_REPORT.md
```

This report demonstrates the output generated by the **Project Analysis Skill**, providing a detailed analysis of a software project, including architecture, technologies, APIs, dependencies, security, strengths, and improvement suggestions.

---

# ✨ Features

- Steel surface defect detection using Machine Learning
- Image preprocessing using Hooks
- Color Histogram feature extraction
- Decision Tree & Random Forest classification
- Streamlit-based web application
- AI-generated defect analysis report
- Paint Defect Detection Skill
- Project Analysis Skill
- Modular Agentic AI architecture
- Reusable AI Skills
- Sample AI-generated Markdown reports
- Easily extensible for future AI capabilities

---

# 💻 Technologies Used

## Programming Language

- Python

## Machine Learning

- Scikit-Learn
- Decision Tree Classifier
- Random Forest Classifier

## Libraries

- OpenCV
- NumPy
- Joblib
- Pillow
- Streamlit

## Agentic AI Concepts

- AI Agent
- AI Skills
- AI Prompts
- AI Instructions
- AI Hooks
- Markdown Report Generation

# 📁 Project Structure

```text
Paint_Defect_Detection_System/
│
├── app.py
├── README.md
├── requirements.txt
├── Paint_Defect_Detection_Model.pkl
├── Paint_Defect_Detection.ipynb
├── check_model.py
│
├── agents/
│   ├── paint_detection_agent.py
│   └── paint_detection_agent.md
│
├── hooks/
│   └── preprocess_hook.py
│
├── prompts/
│   └── defect_prompts.md
│
├── instructions/
│   └── instructions.md
│
├── paint-defect-skill/
│   └── SKILL.md
│
├── project-analysis/
│   └── SKILL.md
│
├── PAINT_DEFECT_DETECTION_REPORT.md
├── PROJECT_ANALYSIS_REPORT.md
│
└── assets/
    └── sample_images/
```

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/KeerthanadeviBaskaran/Paint_Defect_Detection_System.git
```

---

## Navigate to the Project Folder

```bash
cd Paint_Defect_Detection_System
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Streamlit Application

```bash
streamlit run app.py
```

The application will launch in your default web browser.

---

# 📈 Results

### Machine Learning

- Random Forest Accuracy: **94.79%**
- Decision Tree Accuracy: **93%**
- Successfully classifies six steel surface defect categories.

### Agentic AI

- Generates AI-assisted defect analysis reports.
- Demonstrates modular Agentic AI architecture.
- Includes reusable AI Skills for different tasks.
- Uses Hooks to automate preprocessing.
- Uses Prompts and Instructions to standardize AI reasoning.

### Project Analysis Skill

- Supports analysis of software projects.
- Generates comprehensive Markdown reports.
- Detects technologies, architecture, APIs, dependencies, databases, security, and build processes.
- Provides strengths, weaknesses, and improvement suggestions.

---

# 🚀 Future Enhancements

## Paint Defect Detection

- Add **Normal (No Defect)** class.
- Support multiple defect detection within a single image.
- Display confidence scores for predictions.
- Improve model accuracy using Deep Learning (CNN).

---

## Agentic AI

- Integrate OpenAI or Gemini for advanced reasoning.
- Add Retrieval-Augmented Generation (RAG).
- Support memory-enabled AI agents.
- Add multi-agent collaboration.

---

## Project Analysis Skill

- Analyze larger enterprise codebases.
- Detect code smells and technical debt.
- Support UML and architecture diagram generation.
- Generate dependency graphs automatically.
- Detect CI/CD pipelines.
- Recommend software design improvements.
- Generate API documentation automatically.

---

# 🎯 Learning Outcomes

This project demonstrates practical knowledge of:

- Machine Learning
- Computer Vision
- Image Processing
- Feature Extraction
- Random Forest Classification
- Decision Tree Classification
- Streamlit Development
- Agentic AI Concepts
- AI Skills
- AI Agents
- AI Prompts
- AI Instructions
- AI Hooks
- Markdown Report Generation
- Software Project Analysis

---

# 🤝 Contributing

Contributions, suggestions, and improvements are always welcome.

If you find any issues or have ideas for enhancement:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Open a Pull Request.

---

# 📜 License

This project is intended for **educational, research, and demonstration purposes**.

---

# 👩‍💻 Author

**Keerthanadevi Baskaran**

Artificial Intelligence | Machine Learning | Computer Vision | Agentic AI

---

# ⭐ Repository Highlights

✅ Machine Learning Based Paint Defect Detection

✅ Streamlit Web Application

✅ Random Forest Classifier

✅ AI Agent Integration

✅ Paint Defect Detection Skill

✅ Project Analysis Skill

✅ AI Prompts

✅ AI Instructions

✅ AI Hooks

✅ AI Generated Markdown Reports

✅ Reusable Agentic AI Architecture

---

## 🌟 If you found this project useful, consider giving it a ⭐ on GitHub!
