from llama_index import SimpleDirectoryReader, GPTListIndex, GPTVectorStoreIndex, LLMPredictor, PromptHelper, ServiceContext, StorageContext, load_index_from_storage
import os
import gradio as gr
from langchain.embeddings import OpenAIEmbeddings
from langchain import OpenAI
from dotenv import load_dotenv

load_dotenv('.env')
os.environ.get('OPENAI_API_KEY')

max_input = 4098
tokens = 256
chnk_size = 600
max_chnk_overlap = 20

def entrenamiento(path):
    docs = SimpleDirectoryReader(path).load_data()
    prompt_helper = PromptHelper(max_input,tokens,max_chnk_overlap,chunk_size_limit=chnk_size)
    modelo = LLMPredictor(llm=OpenAI(temperature=0,model_name='text-ada-001',max_tokens=tokens)) # type: ignore
    contexto = ServiceContext.from_defaults(llm_predictor=modelo,prompt_helper=prompt_helper)
    index_model = GPTVectorStoreIndex.from_documents(docs,service_context=contexto)
    index_model.storage_context.persist('modelo')

entrenamiento('datos')