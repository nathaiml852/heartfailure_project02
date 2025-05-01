from prometheus_client import Counter, Histogram

# Total number of prediction requests
PREDICTION_COUNT = Counter(
    "predictions_total",
    "Total prediction requests",
    ["status"]  # status can be 'success', 'error', etc.
)

# Latency of prediction requests
PREDICTION_LATENCY = Histogram(
    "prediction_duration_seconds",
    "Time spent in prediction"
)
