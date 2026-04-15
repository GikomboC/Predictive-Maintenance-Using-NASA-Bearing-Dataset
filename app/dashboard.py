import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set layout to centered for better screenshot framing
st.set_page_config(layout="centered", page_title="Maintenance Dashboard")

st.title("Predictive Maintenance Dashboard")

@st.cache_data
def load_data():
    # Ensure the path matches your repo structure
    return pd.read_csv("data/processed_data_1st_test.csv", parse_dates=["timestamp"])

df = load_data()

# Sidebar
st.sidebar.header("Controls")
dataset = st.sidebar.selectbox("Select Dataset", ["1st_test"])
feature = st.sidebar.selectbox("Select Feature", ["rms", "kurtosis", "fft_mean"])

# -------------------------------
# 📊 Feature Trend & Failure Point
# -------------------------------
# Using columns to constrain width for a better screenshot aspect ratio
col1, col2 = st.columns([3, 1])

with col1:
    st.subheader(f"{feature.upper()} Trend")
    # Reduced figsize for compactness
    fig, ax = plt.subplots(figsize=(6, 3.5)) 
    ax.plot(df["timestamp"], df[feature], color='#1f77b4')
    
    # Calculate Failure Point
    failure_idx = df["rms"].idxmax()
    failure_time = df.loc[failure_idx, "timestamp"]
    ax.axvline(failure_time, color='red', linestyle="--", label="Failure Point")
    
    ax.set_ylabel(feature.upper())
    plt.xticks(rotation=45, fontsize=8)
    plt.yticks(fontsize=8)
    ax.legend(fontsize=8)
    plt.tight_layout()
    
    st.pyplot(fig, use_container_width=True)

with col2:
    st.write("") # Spacer
    st.metric("Failure Time", f"{failure_time.strftime('%H:%M')}")
    st.metric("Status", "Critical" if feature == "rms" and df[feature].iloc[-1] > df[feature].mean() else "Stable")

# -------------------------------
# 🧠 Healthy vs Failing (Side-by-Side)
# -------------------------------
st.divider()
st.subheader("Comparative Health Analysis")

col_left, col_right = st.columns(2)

n = len(df)
healthy = df.iloc[:int(0.2*n)]
failing = df.iloc[int(0.8*n):]

with col_left:
    fig2, ax2 = plt.subplots(figsize=(5, 3))
    ax2.plot(healthy["timestamp"], healthy["rms"], label="Healthy Stage", color='green')
    ax2.set_title("Initial Health (Baseline)", fontsize=10)
    plt.xticks(rotation=45, fontsize=7)
    st.pyplot(fig2)

with col_right:
    fig3, ax3 = plt.subplots(figsize=(5, 3))
    ax3.plot(failing["timestamp"], failing["rms"], label="Failing Stage", color='orange')
    ax3.set_title("Degradation Stage", fontsize=10)
    plt.xticks(rotation=45, fontsize=7)
    st.pyplot(fig3)

# -------------------------------
# 🤖 Model Prediction
# -------------------------------
if "predicted_RUL" in df.columns:
    st.divider()
    st.subheader("Prognostics: Remaining Useful Life")
    
    # Constrain the RUL graph to the center
    _, mid_col, _ = st.columns([1, 4, 1])
    with mid_col:
        fig4, ax4 = plt.subplots(figsize=(7, 3))
        ax4.plot(df["timestamp"], df["predicted_RUL"], color='purple', linewidth=2)
        ax4.set_ylabel("RUL (Hours/Cycles)")
        plt.xticks(rotation=45, fontsize=8)
        plt.tight_layout()
        st.pyplot(fig4)
