---
name: paint-defect-skill
description: Detect and classify paint surface defects using image preprocessing, color histogram features, and a trained classifier.
---

## Workflow

1. Accept an uploaded image of a painted or steel surface.
2. Preprocess the image without modifying the original file.
3. Convert the image to a suitable format for analysis.
4. Extract color histogram features from the image.
5. Predict the defect class using the trained model.
6. Return the defect category, confidence score, explanation, and suggested improvement.

## Expected Output

- Defect Type
- Confidence Score
- Key Visual Evidence
- Simple Explanation
- Suggested Inspection Improvement

## Resources

- Color Histogram Feature Extraction
- Classifier-Based Defect Prediction
- Defect Knowledge Base