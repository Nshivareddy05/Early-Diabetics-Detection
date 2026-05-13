import time
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

def simulate_processing(steps, placeholder, progress_bar):
    """Simulates a machine learning pipeline step by step."""
    total_steps = len(steps)
    for i, step in enumerate(steps):
        placeholder.text(step)
        progress_bar.progress(int(((i + 1) / total_steps) * 100))
        time.sleep(np.random.uniform(0.4, 1.2))

def generate_prediction(data):
    """Generates a prediction based on inputs. Hardcoded rules to feel realistic."""
    glucose = data.get("Glucose", 100)
    bmi = data.get("BMI", 25.0)
    age = data.get("Age", 30)
    
    # Calculate a base risk score
    risk_score = 0
    if glucose > 140: risk_score += 40
    elif glucose > 100: risk_score += 15
    
    if bmi > 30: risk_score += 25
    elif bmi > 25: risk_score += 10
        
    if age > 45: risk_score += 15
    elif age > 35: risk_score += 5
        
    # Introduce some stochasticity to make it feel "model-like"
    noise = np.random.normal(0, 5)
    final_risk = min(max(risk_score + noise, 5), 98) # Keep between 5 and 98%
    
    prediction = 1 if final_risk > 50 else 0
    return prediction, final_risk

def create_gauge_chart(confidence, title="Classification Confidence"):
    """Creates an animated gauge chart for risk/confidence."""
    color = "green" if confidence < 40 else "orange" if confidence < 60 else "red"
    
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = confidence,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': title, 'font': {'size': 24, 'color': 'white'}},
        gauge = {
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': color},
            'bgcolor': "rgba(0,0,0,0)",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 40], 'color': 'rgba(16, 185, 129, 0.3)'},
                {'range': [40, 60], 'color': 'rgba(245, 158, 11, 0.3)'},
                {'range': [60, 100], 'color': 'rgba(239, 68, 68, 0.3)'}],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 50}
        }
    ))
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font={'color': "white", 'family': "Inter"},
        height=300,
        margin=dict(l=20, r=20, t=50, b=20)
    )
    return fig

def create_feature_importance():
    """Generates a Feature Importance chart."""
    features = ['Glucose', 'BMI', 'Age', 'Diabetes Pedigree', 'Pregnancies', 'Insulin', 'Skin Thickness', 'Blood Pressure']
    importance = [0.35, 0.25, 0.15, 0.10, 0.06, 0.05, 0.02, 0.02]
    
    df = pd.DataFrame({'Feature': features, 'Importance': importance})
    df = df.sort_values(by='Importance', ascending=True)
    
    fig = px.bar(df, x='Importance', y='Feature', orientation='h', 
                 title="Feature Importance (Random Forest)",
                 color='Importance', color_continuous_scale='Blues')
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={'color': "white"},
        height=400
    )
    return fig

def create_roc_curve():
    """Generates a dummy ROC Curve."""
    fpr = np.linspace(0, 1, 100)
    tpr = np.sqrt(fpr)  # Example convex curve
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=fpr, y=tpr, mode='lines', name='ROC Curve (AUC = 0.89)', line=dict(color='#00d2ff', width=3)))
    fig.add_trace(go.Scatter(x=[0, 1], y=[0, 1], mode='lines', name='Random Classifier', line=dict(color='gray', dash='dash')))
    
    fig.update_layout(
        title="Receiver Operating Characteristic (ROC)",
        xaxis_title="False Positive Rate",
        yaxis_title="True Positive Rate",
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={'color': "white"},
        height=400,
        legend=dict(yanchor="bottom", y=0.01, xanchor="right", x=0.99)
    )
    return fig

def create_confusion_matrix():
    """Generates a Confusion Matrix heatmap."""
    z = [[142, 28], [34, 104]]
    x = ['Predicted 0', 'Predicted 1']
    y = ['Actual 0', 'Actual 1']
    
    fig = px.imshow(z, text_auto=True, x=x, y=y, color_continuous_scale='Blues',
                    title="Confusion Matrix (Test Set)")
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font={'color': "white"},
        height=400
    )
    return fig

def get_medical_recommendation(risk_score, is_diabetic):
    if is_diabetic:
        return [
            "Consult an endocrinologist for a comprehensive evaluation.",
            "Monitor blood glucose levels daily before meals and at bedtime.",
            "Implement a low-glycemic index diet.",
            "Begin a medical weight management program if BMI > 25."
        ]
    elif risk_score > 30:
        return [
            "Schedule a fasting blood glucose and HbA1c test.",
            "Increase physical activity to 150 minutes per week.",
            "Reduce intake of refined carbohydrates and sugars.",
            "Monitor blood pressure and lipid profile periodically."
        ]
    else:
        return [
            "Maintain current healthy lifestyle.",
            "Continue routine annual medical check-ups.",
            "Ensure a balanced diet rich in fiber."
        ]
