# main.py

import logging
from app.interface import launch_ui
from prometheus_client import start_http_server
import threading

logging.basicConfig(level=logging.INFO)

def start_metrics_server():
    # Expose metrics at http://localhost:8001/
    start_http_server(8001)
    logging.info("Prometheus metrics server started on port 8001.")

if __name__ == "__main__":
    # Start Prometheus server in background
    threading.Thread(target=start_metrics_server, daemon=True).start()

    # Launch the Gradio interface
    launch_ui()