# 🔧 Predictive Maintenance Using NASA Bearing Dataset for 1st Test

## 📌 Overview

This project builds a predictive maintenance system using vibration data from rotating machinery. The goal is to detect degradation patterns and predict failure using signal processing and machine learning techniques.

---

## 📊 Dataset

* Source: NASA IMS Bearing Dataset
* Data Type: Vibration signals (accelerometer readings)
* Sampling Rate: 20 kHz
* Each file: 20,480 samples (1-second snapshot)
* Frequency: Recorded every 10 minutes
* ## Dataset
The raw dataset is not included due to size.
Download it here: [NASA IMS Bearing Dataset](https://www.kaggle.com/datasets/vinayak123tyagi/bearing-dataset/data)

---

## 🧠 Problem Statement

Rotating machinery (e.g., bearings) degrades over time. The challenge is to:

* Detect early signs of failure
* Monitor degradation
* Predict remaining useful life (RUL)

---

## ⚙️ Approach

### 1. Data Processing

* Loaded timestamp-based vibration files
* Parsed time-series progression

### 2. Feature Engineering

Extracted key features from raw signals:

* RMS (energy of vibration)
* Mean, Standard Deviation
* Kurtosis (detects spikes)
* Skewness
* FFT-based features (frequency domain)

### 3. Visualization

* Raw signal vs feature-based trends
* RMS degradation over time
* Healthy vs failing segment comparison
* Failure point detection

### 4. Modeling

* Built a Random Forest model
* Predicted Remaining Useful Life (RUL)

---

## 📈 Key Results

### 🔹 Raw Signal

* High-dimensional and noisy
* Difficult to interpret directly

### 🔹 Feature-Based Analysis

* Clear degradation trends
* RMS increases toward failure
* Kurtosis detects fault spikes

### 🔹 Model Performance

* Successfully tracks degradation trend
* Predicts RUL progression

---

## 📊 Visual Outputs

* RMS over time
* Healthy vs failing comparison
* Failure point highlighting
* Model predictions overlay

---

## 🚀 Streamlit Dashboard

Interactive dashboard to:

* Visualize vibration trends
* Monitor degradation
* View predictions
## 🔗 Live Demo
[Streamlit App](https://predictive-maintenance-using-nasa-bearing-dataset-y3urgrwbnkmw.streamlit.app/)---

## 🏆 Skills Demonstrated

* Time-series analysis
* Signal processing (FFT)
* Feature engineering
* Machine learning (regression)
* Data visualization

---

## 📁 Project Structure

```
nasa-predictive-maintenance/
│
├── notebooks/
├── src/
├── app/
│   └── dashboard.py
├── outputs/
├── README.md
└── requirements.txt
```

---

## 🔥 Future Improvements

* LSTM / deep learning on raw signals
* Real-time streaming data
* Advanced anomaly detection

---

## 💡 Conclusion

Feature engineering transforms raw vibration signals into meaningful insights, enabling accurate detection and prediction of machine failure.

---

## 👤 Author

Caleb Muriithi Gikombo
