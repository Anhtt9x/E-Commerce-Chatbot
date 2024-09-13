import pandas as pd
from langchain_core.documents import Document

def data_converter():
    
    product_data = pd.read_csv("data/flipkart_product_review.csv")

    data = product_data[['product_title','review']]

    docs = []

    for index , row in data.iterrows():

        meta_data = {"product_title":row['product_title']}

        doc = Document(page_content=row['review'], metadata=meta_data)

        docs.append(doc)

    return docs