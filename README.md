# 📈 Stock Predictor: Multi-Stage Financial Forecasting Platform

An enterprise-ready, open-source quantitative analysis and machine learning framework engineered for financial time-series forecasting. This project evolves through multiple iterative phases—integrating raw dataset ingestion, complex technical indicators, deep recurrent neural networks (LSTM), and highly accurate bidirectional architectures—all managed via a web-based visualization dashboard.

---

## 🌟 Core Features

* **Multi-Week Iterative Pipeline:** Developed dynamically across structured progressive sprints (Weeks 1 to 4) tracking sequential logic refinement.
* **Deep Learning Forecasting Engine:** High-performance sequence modeling utilizing **Long Short-Term Memory (LSTM)** and **Bidirectional LSTMs** to capture complex, non-linear market dependencies.
* **Quantitative Signal Engine:** Automated computation of critical technical indicators covering momentum, volume shifts, and rolling trends.
* **Interactive Visual Dashboard:** Full-stack frontend templates supported by raw JavaScript (`script.js`) and custom UI stylesheets (`style.css`) serving live evaluation metrics.
* **Isolated Scalar Normalization:** Strict application of modular serialization wrappers (`.pkl`) preventing cross-contamination and out-of-sample data leakage.

---

## 🏗️ Repository Architecture & Ecosystem

```text
Stock_Predictor/
├── models/
│   ├── week1_lstm.h5                 # Baseline sequence memory model
│   ├── week1_scaler.pkl              # Feature normalizer for initial phase
│   ├── week2_features_FIXED.h5       # Feature engineered deep learning weights
│   ├── week2_scaler_FIXED.pkl        # Adjusted transformation matrix pipeline
│   ├── week3_bidirectional.h5        # Advanced Bidirectional LSTM architecture
│   ├── week3_scaler.pkl              # Week 3 specific data normalization model
│   ├── week4_final_production.h5     # Fully-optimized production forecasting model
│   └── week4_scaler.pkl              # Production feature pipeline state map
├── static/
│   ├── script.js                     # Frontend interactive plotting algorithms
│   └── style.css                     # Custom visual components theme sheets
├── templates/
│   └── dashboard.html                # Web Application markup page template
├── app.py                            # Application orchestration backend entry-point
└── README.md                         # Framework documentation
