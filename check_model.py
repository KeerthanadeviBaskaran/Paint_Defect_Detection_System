import joblib

model = joblib.load("Paint_Defect_Detection_Model.pkl")

print(type(model))

if hasattr(model, "n_features_in_"):
    print("Expected Features:", model.n_features_in_)