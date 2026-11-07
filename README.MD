# AI-Powered Intelligent Signal Interference Detection and Resilient Communication System

## 📌 About the Project

This project is an AI/ML-based prototype designed to monitor simulated wireless communication signals, detect unusual signal conditions, classify anomaly severity, and demonstrate communication recovery.

It provides a dashboard to visualize signal quality, packet loss, latency, and anomaly alerts.

## ✨ Features

- 📊 Signal quality monitoring
- 📉 Packet loss and latency tracking
- 🤖 Machine learning-based anomaly detection
- ⚠️ Anomaly severity classification
- 📈 Interactive signal visualization
- 🔄 Simulated communication recovery
- 🌐 Flask-based backend API

## 🛠️ Technologies Used

- HTML
- CSS
- JavaScript
- Python
- Flask
- Flask-CORS
- NumPy
- Scikit-learn
- Chart.js

## 📁 Project Structure

```text
SIGNAL-MONITOR/
├── index.html
├── style.css
├── script.js
├── README.md
└── backend/
    ├── app.py
    ├── recovery.py
    └── requirements.txt
```

## ⚙️ Installation and Setup

### 1. Install Python

Install Python 3 on your computer.

### 2. Install Dependencies

Open the terminal in the project folder and run:

```bash
python -m pip install -r backend/requirements.txt
```

### 3. Start the Backend

Run:

```bash
python backend/app.py
```

### 4. Test the API

Open these addresses in your browser while the backend is running:

- Backend status: http://127.0.0.1:5000/
- Signal API: http://127.0.0.1:5000/api/signal
- Health check: http://127.0.0.1:5000/api/health

### 5. Open the Dashboard

Open `index.html` using the VS Code Live Server extension.

## 🧠 Machine Learning

The backend uses the Isolation Forest algorithm from Scikit-learn to identify unusual patterns in simulated signal quality, packet loss, and latency readings.

## 🔄 Recovery Simulation

The `recovery.py` file demonstrates simulated signal quality recovery over multiple steps. It does not control or repair a real wireless network.

## 🚧 Current Status

Prototype under development.

The backend generates synthetic readings. The dashboard and backend may require further integration to display live API data.

## 🔮 Future Improvements

- Connect the frontend dashboard to the backend API
- Improve anomaly detection using labelled datasets
- Add historical signal analysis
- Display recovery performance metrics
- Add automated tests

## ⚠️ Disclaimer

This project is for educational and demonstration purposes. It uses synthetic data and does not verify real-world wireless interference or jamming.

## 👨‍💻 Author

Developed as an AI/ML communication monitoring prototype.