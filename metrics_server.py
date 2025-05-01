from prometheus_client import start_http_server, Counter
import threading

# Define a metric
PREDICTION_COUNTER = Counter("prediction_requests_total", "Total prediction requests made")

# Start Prometheus metrics server on port 8000
def start_metrics_server():
    start_http_server(8000)
    print("Prometheus metrics exposed at http://localhost:8000/metrics")