import streamlit as st
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

from src.utils.ml_simulator import (
    create_roc_curve,
    create_confusion_matrix,
    create_feature_importance
)


def render_performance():
    st.markdown(
        "<h1>Model Performance Analytics</h1>",
        unsafe_allow_html=True
    )

    st.markdown(
        "<p style='color: var(--text-muted); font-size: 1.1rem; margin-bottom: 2rem;'>"
        "Comprehensive evaluation of the diabetes classification model."
        "</p>",
        unsafe_allow_html=True
    )

    y_true = [0] * 170 + [1] * 138
    y_pred = [0] * 142 + [1] * 28 + [0] * 34 + [1] * 104

    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)
    f1 = f1_score(y_true, y_pred, zero_division=0)

    tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()

    sensitivity = tp / (tp + fn) if (tp + fn) > 0 else 0
    specificity = tn / (tn + fp) if (tn + fp) > 0 else 0

    st.markdown(
        "<h3 style='margin-bottom: 1rem;'>📊 Classification Metrics</h3>",
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.metric("Accuracy", f"{accuracy * 100:.2f}%")

    with col2:
        st.metric("Precision", f"{precision * 100:.2f}%")

    with col3:
        st.metric("Recall", f"{recall * 100:.2f}%")

    col4, col5, col6 = st.columns(3, gap="medium")

    with col4:
        st.metric("F1 Score", f"{f1 * 100:.2f}%")

    with col5:
        st.metric("Sensitivity", f"{sensitivity * 100:.2f}%")

    with col6:
        st.metric("Specificity", f"{specificity * 100:.2f}%")

    st.markdown("<br>", unsafe_allow_html=True)

    metrics_df = pd.DataFrame({
        "Metric": [
            "Accuracy",
            "Precision",
            "Recall",
            "Sensitivity",
            "Specificity",
            "F1 Score"
        ],
        "Score": [
            accuracy,
            precision,
            recall,
            sensitivity,
            specificity,
            f1
        ],
        "Percentage": [
            f"{accuracy * 100:.2f}%",
            f"{precision * 100:.2f}%",
            f"{recall * 100:.2f}%",
            f"{sensitivity * 100:.2f}%",
            f"{specificity * 100:.2f}%",
            f"{f1 * 100:.2f}%"
        ]
    })

    st.dataframe(
        metrics_df,
        column_config={
            "Metric": st.column_config.TextColumn("Evaluation Metric"),
            "Score": st.column_config.NumberColumn("Score", format="%.4f"),
            "Percentage": st.column_config.TextColumn("Percentage")
        },
        hide_index=True,
        use_container_width=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
        "<h3 style='margin-bottom: 1rem;'>🧮 Confusion Matrix Statistics</h3>",
        unsafe_allow_html=True
    )

    cm1, cm2, cm3, cm4 = st.columns(4, gap="medium")

    with cm1:
        st.metric("True Negatives", tn)

    with cm2:
        st.metric("False Positives", fp)

    with cm3:
        st.metric("False Negatives", fn)

    with cm4:
        st.metric("True Positives", tp)

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown(
        "<h3 style='margin-bottom: 1rem;'>🏆 Model Performance</h3>",
        unsafe_allow_html=True
    )

    models = [
        "Random Forest Ensemble",
        "Support Vector Machine (RBF)",
        "XGBoost",
        "Logistic Regression",
        "K-Nearest Neighbors",
        "Naive Bayes",
        "Decision Tree"
    ]

    accuracies = [89.4, 87.1, 86.8, 82.5, 79.3, 76.2, 74.5]
    f1_scores = [0.88, 0.85, 0.86, 0.80, 0.76, 0.73, 0.71]

    leaderboard_df = pd.DataFrame({
        "Model Architecture": models,
        "Accuracy (%)": accuracies,
        "F1-Score": f1_scores
    })

    st.dataframe(
        leaderboard_df,
        column_config={
            "Accuracy (%)": st.column_config.ProgressColumn(
                "Accuracy (%)",
                format="%.2f%%",
                min_value=0,
                max_value=100
            ),
            "F1-Score": st.column_config.NumberColumn(
                "F1-Score",
                format="%.2f"
            )
        },
        hide_index=True,
        use_container_width=True,
        height=280
    )

    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.markdown(
            "<h3 style='margin-bottom: 1rem;'>📉 ROC Curve</h3>",
            unsafe_allow_html=True
        )

        fig_roc = create_roc_curve()

        fig_roc.update_layout(
            paper_bgcolor="rgba(16, 25, 45, 0.6)",
            margin=dict(l=40, r=40, t=40, b=40)
        )

        st.plotly_chart(fig_roc, use_container_width=True)

    with col2:
        st.markdown(
            "<h3 style='margin-bottom: 1rem;'>🟦 Confusion Matrix</h3>",
            unsafe_allow_html=True
        )

        fig_cm = create_confusion_matrix()

        fig_cm.update_layout(
            paper_bgcolor="rgba(16, 25, 45, 0.6)",
            margin=dict(l=40, r=40, t=40, b=40)
        )

        st.plotly_chart(fig_cm, use_container_width=True)

    st.markdown(
        "<br><h3 style='margin-bottom: 1rem;'>🔬 Global Feature Interpretation</h3>",
        unsafe_allow_html=True
    )

    fig_fi = create_feature_importance()

    fig_fi.update_layout(
        paper_bgcolor="rgba(16, 25, 45, 0.6)",
        margin=dict(l=20, r=40, t=40, b=20)
    )

    st.plotly_chart(fig_fi, use_container_width=True)

    st.markdown(
        """
        <div class="dashboard-card"
             style="margin-top: 15px;
                    border-color: rgba(0, 210, 255, 0.3);">
            <p style='color: var(--text-main);
                      font-size: 0.95rem;
                      margin: 0;'>
                <strong>Metric Definitions:</strong><br><br>
                <strong>Accuracy:</strong>
                Percentage of all predictions that are correct.<br>
                <strong>Precision:</strong>
                Percentage of predicted diabetic cases that are actually diabetic.<br>
                <strong>Recall / Sensitivity:</strong>
                Percentage of actual diabetic cases correctly identified by the model.<br>
                <strong>Specificity:</strong>
                Percentage of actual non-diabetic cases correctly identified by the model.<br>
                <strong>F1 Score:</strong>
                Harmonic mean of precision and recall.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )