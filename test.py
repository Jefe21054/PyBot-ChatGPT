from llama_index import SimpleDirectoryReader, GPTListIndex, GPTVectorStoreIndex, LLMPredictor, PromptHelper, ServiceContext, StorageContext, load_index_from_storage
import os
import gradio as gr
from langchain.embeddings import OpenAIEmbeddings
from langchain import OpenAI
from dotenv import load_dotenv

load_dotenv('.env')
os.environ.get('OPENAI_API_KEY')

def chatbot(inputText):
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir='modelo')
    modelo = load_index_from_storage(storage_context)
    query_engine = modelo.as_query_engine()
    respuesta = query_engine.query(inputText)
    return respuesta

app = gr.Interface(fn=chatbot,
            inputs=gr.Textbox(lines=5,label='Ingresa una peticion'),
            outputs='text',
            title='ChatBot')

app.launch(share=False)