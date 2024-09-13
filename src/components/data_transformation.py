from src.components.data_ingestion import data_converter
from dotenv import load_dotenv
import os
import pandas as pd
from langchain_astradb import AstraDBVectorStore
from langchain_google_genai import GoogleGenerativeAIEmbeddings

load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')

API_ENDPOINT = os.getenv('API_ENDPOINT')
TOKENS = os.getenv('TOKENS')

embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

def ingestion(status):
    vectorstore = AstraDBVectorStore(collection_name="e_commerce",token=TOKENS,api_endpoint=API_ENDPOINT,
                               namespace="default_keyspace",embedding=embedding)
    
    storage = status

    if storage == None:
        docs = data_converter()
        inserted_data = vectorstore.add_documents(docs)

    else:
        return vectorstore
    
    return vectorstore, inserted_data


if __name__ == "__main__":

    vectorstore , inserted_data = ingestion(None)
    print(f"Inserted data {len(inserted_data)}")

    results = vectorstore.similarity_search("Tell me about the low budget sound basshead")

    for res in results:
        print(f"Content:{res.page_content} , Meta_data:{res.metadata}")    
