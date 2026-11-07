from flask import Flask, jsonify
from flask_cors import CORS
import random
from datetime import datetime
from sklearn.ensemble import IsolationForest
import numpy as np

app = Flask(__name__)
CORS(app)

# Demo-only synthetic data; no real radio signals are used.
rng = np.random.RandomState(42)

# Train a lightweight anomaly detector on normal simulated readings.
normal_samples = np.column_stack([
    rng.uniform(75, 99, 500),  # signal quality %
    rng.uniform(0, 3, 500),    # packet loss %
    rng.uniform(20, 100, 500)  # latency ms
])

model = IsolationForest(
    n_estimators=100,
    contamination=0.1,
    random_state=42
)
model.fit(normal_samples)


def generate_reading():
    unusual = random.random() < 0.2

    if unusual:
        quality = random.uniform(25, 55)
        packet_loss = random.uniform(5, 15)
        latency = random.uniform(130, 230)
    else:
        quality = random.uniform(75, 99)
        packet_loss = random.uniform(0, 3)
        latency = random.uniform(20, 100)

    features = np.array([[quality, packet_loss, latency]])
    prediction = int(model.predict(features)[0])

    is_anomaly = prediction == -1

    if is_anomaly:
        severity = "high" if (
            quality < 60 and packet_loss > 5
        ) else "medium"
    else:
        severity = "normal"

    return {
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "signal_quality": round(quality, 1),
        "packet_loss": round(packet_loss, 1),
        "latency_ms": round(latency, 0),
        "anomaly_detected": is_anomaly,
        "severity": severity,
        "message": (
            "Unusual simulated readings detected"
            if is_anomaly
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


@app.route("/api/signal")
def get_signal():
    return jsonify(generate_reading())


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)