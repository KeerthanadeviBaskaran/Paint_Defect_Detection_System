import streamlit as st
import joblib
import cv2
import numpy as np
from PIL import Image
from sklearn.preprocessing import normalize

# ----------------------------
# PAGE CONFIG
# ----------------------------

st.set_page_config(
    page_title="Paint Defect Detection",
    page_icon="🎨",
    layout="centered"
)

# ----------------------------
# LOAD MODEL
# ----------------------------

model = joblib.load("Paint_Defect_Detection_Model.pkl")

# Class Names
class_names = [
    "crazing",
    "inclusion",
    "patches",
    "pitted_surface",
    "rolled-in_scale",
    "scratches"
]

# ----------------------------
# FEATURE EXTRACTION
# ----------------------------

def extract_features(image):

    h_r = cv2.calcHist(
        [image], [2],
        None,
        [32],
        [0, 256]
    ).flatten()

    h_g = cv2.calcHist(
        [image], [1],
        None,
        [32],
        [0, 256]
    ).flatten()

    h_b = cv2.calcHist(
        [image], [0],
        None,
        [32],
        [0, 256]
    ).flatten()

    features = np.concatenate(
        [h_r, h_g, h_b]
    )

    return features

# ----------------------------
# UI
# ----------------------------

st.title("🔍 Paint Defect Detection")

st.markdown(
    """
Upload a steel surface image and the AI model will identify
which defect class it belongs to.
"""
)

uploaded_file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

# ----------------------------
# PREDICTION
# ----------------------------

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    if st.button("Detect Defect"):

        img_array = np.array(image)

        if len(img_array.shape) == 2:
            img_array = cv2.cvtColor(
                img_array,
                cv2.COLOR_GRAY2BGR
            )

        else:
            img_array = cv2.cvtColor(
                img_array,
                cv2.COLOR_RGB2BGR
            )

        features = extract_features(img_array)

        features = normalize([features])

        prediction = model.predict(features)

        predicted_class = prediction[0]

        st.success(
            f"Detected Defect: {predicted_class}"
        )

        st.subheader("Prediction Result")

        st.write(
            f"**Defect Type:** {predicted_class}"
        )

        if predicted_class == "crazing":
            st.warning("Surface contains Crazing Defect")

        elif predicted_class == "inclusion":
            st.warning("Surface contains Inclusion Defect")

        elif predicted_class == "patches":
            st.warning("Surface contains Patches Defect")

        elif predicted_class == "pitted_surface":
            st.warning("Surface contains Pitted Surface Defect")

        elif predicted_class == "rolled-in_scale":
            st.warning("Surface contains Rolled-In Scale Defect")

        elif predicted_class == "scratches":
            st.warning("Surface contains Scratches Defect")

# ----------------------------
# SIDEBAR
# ----------------------------

st.sidebar.title("Model Information")

st.sidebar.write("Algorithm : Random Forest")

st.sidebar.write("Accuracy : 94.79%")

st.sidebar.write("Classes : 6")

st.sidebar.write("""
Classes:
- crazing
- inclusion
- patches
- pitted_surface
- rolled-in_scale
- scratches
""")