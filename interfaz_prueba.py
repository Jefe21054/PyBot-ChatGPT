import gradio as gr
from transformers import pipeline

generador = pipeline('text-generation', model='gpt2')


def saludo(text):
    result = generador(text, max_length=30, num_return_sequences=1)
    return result[0]["generated_text"] # type: ignore

examples = [
    ["The Moon's orbit around Earth has"],
    ["The smooth Borealis basin in the Northern Hemisphere covers 40%"],
]

app = gr.Interface(fn=saludo,
                inputs= gr.inputs.Textbox(lines=5, label='Texto entrada'),
                outputs= gr.outputs.Textbox(label='Texto de salida'),
                examples=examples)

app.launch()