import gradio as gr

input_components = [
    gr.Number(label="Age"),
    gr.Radio([0, 1], label="Anaemia"),
    gr.Number(label="Creatinine Phosphokinase"),
    gr.Radio([0, 1], label="Diabetes"),
    gr.Number(label="Ejection Fraction"),
    gr.Radio([0, 1], label="High Blood Pressure"),
    gr.Number(label="Platelets"),
    gr.Number(label="Serum Creatinine"),
    gr.Number(label="Serum Sodium"),
    gr.Radio([0, 1], label="Sex"),
    gr.Radio([0, 1], label="Smoking"),
    gr.Number(label="Time")
]