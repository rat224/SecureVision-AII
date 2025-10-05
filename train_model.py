import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib

# Use a small sample dataset
data = pd.read_csv('dataset/cloud_logs.csv')
X = data[['login_hour', 'failed_attempts', 'ip_risk_score']]

model = IsolationForest(contamination=0.2, random_state=42)
model.fit(X)

# Save the trained model
joblib.dump(model, 'model/anomaly_detector.pkl')
print("✅ Model trained and saved successfully.")

