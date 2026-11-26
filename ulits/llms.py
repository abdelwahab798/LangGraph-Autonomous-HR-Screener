from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

load_dotenv()

def get_structred_llm(model_name:str,Structred_output):
    llm=ChatGoogleGenerativeAI(model=model_name,api_key=os.getenv("API_KEY"),temperature=0)
    structred_llm=llm.with_structured_output(Structred_output)
    return structred_llm
