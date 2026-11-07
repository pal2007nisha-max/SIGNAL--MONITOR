
const qualityElement = document.getElementById("quality");
const packetLossElement = document.getElementById("packetLoss");
const statusElement = document.getElementById("status");
const confidenceElement = document.getElementById("confidence");
const analysisElement = document.getElementById("analysis");
const eventLog = document.getElementById("eventLog");

const startButton = document.getElementById("startButton");
const stopButton = document.getElementById("stopButton");

let timer = null;

const chartCanvas = document.getElementById("signalChart");

const chart = new Chart(chartCanvas, {
    type: "line",
    data: {
        labels: [],
        datasets: [{
            label: "Signal Quality (%)",
            data: [],
            borderColor: "#d8b4fe",
            backgroundColor: "rgba(216,180,254,0.15)",
            fill: true,
            tension: 0.3
        }]
    },
    options: {
        responsive: true,
        animation: false,
        scales: {
            y: {
                min: 0,
                max: 100
            }
        }
    }
});

function addLog(message) {
    const item = document.createElement("li");
    item.textContent =
        new Date().toLocaleTimeString() + " — " + message;

    eventLog.prepend(item);

    while (eventLog.children.length > 8) {
        eventLog.lastElementChild.remove();
    }
}

async function updateSimulation() {
    try {
        const response = await fetch(
            "http://127.0.0.1:5000/api/signal"
        );

        if (!response.ok) {
            throw new Error("API request failed");
        }

        const data = await response.json();

        qualityElement.textContent =
            data.signal_quality + "%";

        packetLossElement.textContent =
            data.packet_loss + "%";

        statusElement.textContent =
            data.severity.toUpperCase();

        confidenceElement.textContent = "N/A";

        analysisElement.textContent =
            data.message +
            " | Latency: " + data.latency_ms + " ms";

        chart.data.labels.push(
            new Date().toLocaleTimeString()
        );

        chart.data.datasets[0].data.push(
            data.signal_quality
        );

        if (chart.data.labels.length > 15) {
            chart.data.labels.shift();
            chart.data.datasets[0].data.shift();
        }

        chart.update();

        addLog(
            "Signal: " + data.signal_quality +
            "% | Severity: " + data.severity
        );

    } catch (error) {
        analysisElement.textContent =
            "Backend se connection nahi ho raha. " +
            "Check karo ki Python server chal raha hai.";

        addLog("Backend connection error.");
        stopSimulation();
    }
}

function startSimulation() {
    if (timer !== null) return;

    addLog("Backend monitoring started.");
    updateSimulation();

    timer = setInterval(updateSimulation, 2000);
}

function stopSimulation() {
    if (timer !== null) {
        clearInterval(timer);
        timer = null;
        addLog("Monitoring stopped.");
    }
}

startButton.addEventListener("click", startSimulation);
stopButton.addEventListener("click", stopSimulation);