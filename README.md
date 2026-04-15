Predictive Maintenance: NASA Bearing Degradation Analysis (Test 1)
## Overview
This project implements a predictive maintenance framework utilizing high-frequency vibration data to monitor rotating machinery health. By leveraging signal processing and machine learning, the system identifies degradation patterns and forecasts mechanical failure.

---

## Dataset
NASA IMS Bearing Dataset

The analysis is based on vibration signals captured under test-to-failure conditions by the NASA Ames Research Center and the University of Cincinnati's Center for Intelligent Maintenance Systems (IMS).

Note: The raw data is excluded from this repository due to its volume.

Source: NASA IMS Bearing Dataset (Kaggle)

Dataset Characteristics

- Signal Type: Time-series vibration snapshots.
- Sampling Rate: 20 kHz.
- Snapshot Size: 20,480 data points (1 second per file).
- Failure Modes: Inner race faults, outer race faults, and rolling element defects.
- Structure: Timestamped files organized across three distinct test runs (1st, 2nd, and 3rd tests).
  
---
## Project Utility

This benchmark dataset is essential for validating:

- Anomaly detection algorithms.
- Remaining Useful Life (RUL) estimation.
- Digital twin and prognostic modeling.

---
* 
The raw dataset is not included due to size.
Download it here: [NASA IMS Bearing Dataset](https://www.kaggle.com/datasets/vinayak123tyagi/bearing-dataset/data)

---

### Business Impact

This system enables:
- Early fault detection
- Reduced maintenance costs
- Increased machine uptime
- Data-driven maintenance scheduling

Used in:
- manufacturing plants
- oil & gas
- power systems
- robotics and automation

---

### Note

Due to its size (thousands of files), the dataset is **not included in this repository**.  

Please download it manually from the link above and place it in the appropriate data directory before running the notebook.

---

## Problem Statement
Industrial machines fail unexpectedly, causing:
- downtime
- revenue loss
- maintenance inefficiency

Predictive maintenance uses sensor data to anticipate failures before they occur.

Bearings are critical components that exhibit non-linear degradation. The objective is to:
- Identify early-stage fault signatures.
- Quantify the progression of mechanical wear.
- Accurately estimate the Remaining Useful Life (RUL) to optimize maintenance scheduling.

---

## Engineering Approach
### 1. Data Processing

* Systematic ingestion of timestamped vibration telemetry.
* Synchronization of time-series progression for longitudinal analysis.

### 2. Feature Engineering

Conversion of raw, high-dimensional signals into health indicators:

* Time-Domain: Root Mean Square (RMS) for energy tracking, Mean, Standard Deviation, Kurtosis (impulse detection), and Skewness.
* Frequency-Domain: Fast Fourier Transform (FFT) to isolate fault-specific frequencies.

### 3. Visualization & Analysis

* Comparative analysis of healthy vs. failing operating states.
* Trend analysis of RMS and Kurtosis as degradation proxies.
* Automated failure point identification.

### 4. Predictive Modeling

* Algorithm: Random Forest Regressor.
* Target: RUL estimation based on historical degradation trajectories.

---

## Key Results

### Signal Transformation: 
Feature extraction successfully reduced noise, revealing clear failure trajectories that raw signals masked. RMS increases as failure approaches.


### Degradation Indicators: 
RMS showed high correlation with end-of-life progression, while Kurtosis effectively flagged early-stage transient faults. Frequency-domain features capture early degradation.

### Model Performance: 
The Random Forest model maintained high fidelity in tracking the degradation curve and predicting RUL. Combining time + frequency features improves prediction.

---

## Visual Outputs

* RMS over time
* Healthy vs failing comparison
* Failure point highlighting
* Model predictions overlay

---

## 🚀 Streamlit Dashboard

An interactive deployment for real-time monitoring:
* Dynamic visualization of vibration trends.
* Real-time degradation health scores.
* Predictive RUL overlays and automated alerts.

---

## 🔗 Live Demo:
[Predictive Maintenance App](https://predictive-maintenance-using-nasa-bearing-dataset-y3urgrwbnkmw.streamlit.app/)

---
## Skills Demonstrated

* Signal Processing: Advanced FFT and time-domain analysis.
* ML Engineering: Feature selection, regression modeling, and RUL estimation.
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

## Deployment Scenario
- Sensors collect vibration data continuously
- Model predicts machine health score
- Alerts triggered when risk exceeds threshold
- Maintenance scheduled before failure occurs
---

## Future Roadmap

* Implementation of LSTM (Long Short-Term Memory) networks for raw sequence modeling.
* Integration of real-time streaming data pipelines (Kafka/MQTT).
* Development of Unsupervised Anomaly Detection for zero-label failure environments.

---

## 💡 Conclusion

Feature engineering transforms raw vibration signals into meaningful insights, enabling accurate detection and prediction of machine failure.

---

## Key Insight

RMS increases steadily as the bearing degrades, while kurtosis captures early-stage faults through spikes in vibration.

This demonstrates that statistical feature engineering effectively transforms noisy raw signals into interpretable indicators of machine health.

---

## Industrial Relevance

This architecture is applicable to high-stakes environments including manufacturing, aerospace, and energy production. By shifting from reactive to predictive maintenance, organizations can significantly reduce unscheduled downtime and prevent catastrophic equipment failure.

---
## Author
- Caleb Gikombo - Mechatronics Engineer | Data Scientist
---
# License
This project is open-source and available under the MIT License.

