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
```

---

## ⚙️ Quick Start Infrastructure Setup

### 1. Clone the Architecture

```bash
git clone https://github.com/isidcode/Stock_Predictor.git
cd Stock_Predictor
```

### 2. Isolate and Activate Virtual Environment

```bash
# On Windows
python -m venv venv
.\venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Required Dependencies

Ensure your environment contains `tensorflow`, `scikit-learn`, `flask`, `pandas`, and `numpy` prior to initialization:

```bash
pip install -r requirements.txt
```

### 4. Deploy the Analytical Platform Dashboard

Fire up the central microservice locally to access your trained model iterations and charts:

```bash
python app.py
```

Once initialized, navigate directly to [http://127.0.0.1:5000](http://127.0.0.1:5000) inside your browser environment.

---

## 🧠 Algorithmic Deep Dive: Progressive Architecture Shift

The framework matures structurally across isolated verification milestones:

### 📊 Baseline Recurrent Block (Week 1)

Integrates a traditional unidirectional sequence matrix. While effective for short histories, it suffers from bounded error propagation over extended forecasting horizons.

### 🛠️ Feature Expansion & Robustness (Week 2)

Implements robust mathematical indicators alongside fixed transformation pipelines (`week2_features_FIXED.h5`) to enhance variance detection.

### 🔄 Spatial Bidirectional Integration (Week 3)

Introduces an advanced hidden layer configuration processing time steps in both true forward chronological and inverse tracking channels simultaneously. This dramatically decreases predictive lag near key market resistance points.

$$
\begin{aligned}
h_t^{\rightarrow} &= \text{LSTM}_{\text{fwd}}(x_t, h_{t-1}^{\rightarrow}) \\
h_t^{\leftarrow} &= \text{LSTM}_{\text{bwd}}(x_t, h_{t+1}^{\leftarrow})
\end{aligned}
$$

### 🚀 Production Deployment Core (Week 4)

Consolidates maximum accuracy parameters into a unified deployment runtime (`week4_final_production.h5`) mapped directly to client-facing charting layers.

---

## 🤝 Contributing & Code Review

We welcome contributions from structural data engineers and quantitative researchers alike:

1. Fork the primary codebase repository.
2. Spin up your explicit workspace feature track:

```bash
git checkout -b feature/OptimizedLayers
```

3. Commit structural revisions with strict tracking:

```bash
git commit -m 'Implement Attention Block'
```

4. Push code upstream:

```bash
git push origin feature/OptimizedLayers
```

5. Open a well-documented Pull Request detailing changes.

---

## 📜 Disclaimer

**Academic and Educational Intent Only.** Financial instruments carry extreme capital loss risks. This toolkit does not represent legal, investment, or personal brokerage advisory services. Never run automated capital assets live relying strictly on mathematical forecasting loops without active validation strategies.
