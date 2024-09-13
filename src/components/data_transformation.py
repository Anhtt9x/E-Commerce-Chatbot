from src.components.data_ingestion import data_converter
from dotenv import load_dotenv
import os
import pandas as pd
from langchain_astradb import AstraDBStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings, GoogleGenerativeAI

load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

