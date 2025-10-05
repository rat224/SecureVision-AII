import gradio as gr
import pandas as pd
import joblib
import plotly.express as px

# Load model
model = joblib.load("model/anomaly_detector.pkl")

def analyze_logs(file):
    data = pd.read_csv(file.name)
    X = data[['login_hour', 'failed_attempts', 'ip_risk_score']]
    data['anomaly'] = model.predict(X)
    data['anomaly'] = data['anomaly'].map({1: 'Normal', -1: 'Suspicious'})
    
    fig = px.histogram(
        data, x="login_hour", color="anomaly",
        title="Login Activity by Hour",
        barmode="group"
    )
    
    return fig, data[data['anomaly'] == 'Suspicious']

demo = gr.Interface(
    fn=analyze_logs,
    inputs=gr.File(label="Upload Cloud Logs (CSV)"),
    outputs=[
        gr.Plot(label="Threat Visualization"),
        gr.Dataframe(label="Suspicious Logins")
    ],
    title="🛡️ SecureVision.AI – Cloud Threat Detection Dashboard",
    description="Upload cloud log data to detect suspicious activity using AI anomaly detection."
)

if __name__ == "__main__":
    demo.launch()
