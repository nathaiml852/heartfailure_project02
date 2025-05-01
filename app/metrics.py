# app/metrics.py
from prometheus_client import Counter, Histogram, Gauge

# Count of all predictions
PREDICTION_COUNT = Counter(
    "predictions_total",
    "Total prediction requests",
    ["status"]
)

# Histogram of prediction latency
PREDICTION_LATENCY = Histogram(
    "prediction_duration_seconds",
    "Time spent in prediction"
)

# Count of prediction errors by type
PREDICTION_ERROR_TYPE = Counter(
    "prediction_errors_total",
    "Total number of prediction errors by type",
    ["error_type"]
)

# Optional: Track bad input fields
INPUT_ANOMALY_COUNT = Counter(
    "input_anomalies_total",
    "Number of input validation anomalies detected",
    ["field"]
)

# Optional: Track request source
REQUEST_SOURCE_COUNT = Counter(
    "request_sources_total",
    "Requests by source",
    ["source"]
)

# Optional: Track model version
MODEL_VERSION = Gauge(
    "model_version_info",
    "Current model version in use",
    ["version"]
)

# Set the current model version (call once)
MODEL_VERSION.labels(version="1.0.0").set(1)
