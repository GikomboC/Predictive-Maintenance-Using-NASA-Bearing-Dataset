import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(layout="wide")

st.title("🔧 Predictive Maintenance Dashboard")

# Load your processed dataset
@st.cache_data
def load_data():
    return pd.read_csv("your_dataset.csv", parse_dates=["timestamp"])

df = load_data()

# Sidebar
st.sidebar.header("Controls")
feature = st.sidebar.selectbox(
    "Select Feature",
    ["rms", "kurtosis", "fft_mean"]
)

# -------------------------------
# 📊 Feature Trend
# -------------------------------
st.subheader(f"{feature.upper()} Over Time")

fig, ax = plt.subplots()
ax.plot(df["timestamp"], df[feature])
ax.set_xlabel("Time")
ax.set_ylabel(feature.upper())
plt.xticks(rotation=45)

st.pyplot(fig)

# -------------------------------
# ⚠️ Failure Point
# -------------------------------
failure_idx = df["rms"].idxmax()
failure_time = df.loc[failure_idx, "timestamp"]

st.subheader("Failure Point")
st.write(f"Estimated Failure Time: {failure_time}")

# -------------------------------
# 🧠 Healthy vs Failing
# -------------------------------
st.subheader("Healthy vs Failing Comparison")

n = len(df)
healthy = df.iloc[:int(0.2*n)]
failing = df.iloc[int(0.8*n):]

fig2, ax2 = plt.subplots()
ax2.plot(healthy["timestamp"], healthy["rms"], label="Healthy")
ax2.plot(failing["timestamp"], failing["rms"], label="Failing")
ax2.legend()

st.pyplot(fig2)

# -------------------------------
# 🤖 Model Prediction (Optional)
# -------------------------------
if "predicted_RUL" in df.columns:
    st.subheader("Predicted Remaining Useful Life")

    fig3, ax3 = plt.subplots()
    ax3.plot(df["timestamp"], df["predicted_RUL"])
    ax3.set_title("Predicted RUL")

    st.pyplot(fig3)
