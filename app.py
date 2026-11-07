from flask import Flask, jsonify
from flask_cors import CORS
from sklearn.ensemble import IsolationForest
import numpy as np
import random
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Train ML model using normal simulated signal data
rng = np.random.RandomState(42)

normal_data = np.column_stack([
    rng.uniform(75, 99, 500),  # Signal quality
    rng.uniform(0, 3, 500),    # Packet loss
    rng.uniform(20, 100, 500)  # Latency
])

model = IsolationForest(
    n_estimators=100,
    contamination=0.1,
    random_state=42
)

model.fit(normal_data)


def generate_signal():
    # Generate synthetic readings for the demo
    unusual = random.random() < 0.2

    if unusual:
        quality = random.uniform(25, 55)
        packet_loss = random.uniform(5, 15)
        latency = random.uniform(130, 230)
    else:
        quality = random.uniform(75, 99)
        packet_loss = random.uniform(0, 3)
        latency = random.uniform(20, 100)

    sample = np.array([[
        quality,
        packet_loss,
        latency
    ]])

    prediction = model.predict(sample)[0]
    anomaly = prediction == -1

    if anomaly:
        severity = (
            "high"
            if quality < 60 and packet_loss > 5
            else "medium"
        )
    else:
        severity = "normal"

    return {
        "timestamp": datetime.now().isoformat(
            timespec="seconds"
        ),
        "signal_quality": round(quality, 1),
        "packet_loss": round(packet_loss, 1),
        "latency_ms": round(latency, 0),
        "anomaly_detected": bool(anomaly),
        "severity": severity,
        "message": (
            "Unusual simulated readings detected"
            if anomaly
            else "Simulated readings look normal"
        ),
        "data_type": "synthetic_demo"
    }


@app.route("/")
def home():
    return jsonify({
        "message": "AI Signal Monitor backend is running",
        "mode": "synthetic simulation",
        "endpoint": "/api/signal"
    })


@app.route("/api/signal", methods=["GET"])
def get_signal():
    return jsonify(generate_signal())


@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({
        "status": "healthy",
        "model": "IsolationForest",
        "mode": "demo"
    })


if __name__ == "__main__":
    print("Starting AI Signal Monitor...")
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )