import logging
import gradio as gr
from app.predict import predict_death_event
from app.config import input_components

# Set up logging for this module
logging.basicConfig(level=logging.INFO)

def launch_ui():
    logging.info("Initializing Gradio interface...")

    iface = gr.Interface(
        fn=predict_death_event,
        inputs=input_components,
        outputs=gr.Text(label="Prediction"),
        title="Patient Survival Prediction",
        description="Predict heart failure outcomes using clinical inputs.",
        flagging_mode="never"
    )

    logging.info("Launching Gradio app on 0.0.0.0:7860...")
    iface.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
        debug=True
    ) 