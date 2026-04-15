# 🔧 predictive-maintenance-nasa-bearings-for-1st-Test

## 📌 Overview

This project builds a predictive maintenance system using vibration data from rotating machinery. The goal is to detect degradation patterns and predict failure using signal processing and machine learning techniques.

---

## 📊 Dataset

This project uses the **NASA IMS Bearing Dataset**.
The dataset contains vibration signals collected from rotating machinery under controlled **test-to-failure conditions**. :contentReference[oaicite:0]{index=0}  

It was developed by:
- NASA Ames Research Center  
- Center for Intelligent Maintenance Systems (IMS), University of Cincinnati :contentReference[oaicite:1]{index=1}  

---
* ## Dataset
The raw dataset is not included due to size.
Download it here: [NASA IMS Bearing Dataset](https://www.kaggle.com/datasets/vinayak123tyagi/bearing-dataset/data)

---

### Dataset Characteristics

- Time-series sensor data (vibration signals)
- 20 kHz sampling rate
- Each file contains **20,480 data points (1-second snapshot)** :contentReference[oaicite:2]{index=2}  
- Collected across multiple test runs until failure
- Bearings experience different failure modes:
  - inner race faults
  - outer race faults
  - rolling element defects :contentReference[oaicite:3]{index=3}  

---

### Structure

- Multiple datasets (1st_test, 2nd_test, 3rd_test)
- Files are timestamped
- Each file represents a vibration snapshot over time
- Channels correspond to different bearings and sensor axes

---

### Why This Dataset

- Real-world industrial data (not synthetic)
- Designed for predictive maintenance and prognostics
- Widely used benchmark in:
  - anomaly detection
  - remaining useful life (RUL) prediction
  - vibration signal analysis

---
### Use in This Project

In this project, the dataset is used to:

- Extract statistical features (mean, RMS, kurtosis, skewness)
- Extract frequency-domain features (FFT)
- Track degradation patterns over time
- Build models to estimate machine health and failure risk

---

### Note

Due to its size (thousands of files), the dataset is **not included in this repository**.  

Please download it manually from the link above and place it in the appropriate data directory before running the notebook.

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

---

## 🔗 Live Demo
[Streamlit App](https://predictive-maintenance-using-nasa-bearing-dataset-y3urgrwbnkmw.streamlit.app/)

---
## 🏆 Skills Demonstrated

* Time-series analysis
* Signal processing (FFT)
* Feature engineering
* Machine learning (regression)
* Data visualization

---

## 📁 Project Structure

```
predictive-maintenance-nasa-bearings-for-1st-Test/
│
├── app/
│   └── dashboard.py
├── data/
│   └── processed_data_1st_test.csv
├── README.md
|--.gitignore
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

## 🧠 Key Insight

RMS increases steadily as the bearing degrades, while kurtosis captures early-stage faults through spikes in vibration.

This demonstrates that statistical feature engineering effectively transforms noisy raw signals into interpretable indicators of machine health.

---

## Industrial Relevance

Predictive maintenance systems like this are used in:

- Manufacturing plants
- Oil and gas pipelines
- Power generation systems
- Robotics and automated production lines

They help:
- reduce downtime
- prevent catastrophic failures
- optimize maintenance schedules

---
## Author
- Caleb Gikombo - Mechatronics Engineer | Data Scientist
---
# License
This project is open-source and available under the MIT License.

