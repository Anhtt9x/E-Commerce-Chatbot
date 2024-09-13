import pandas as pd
from langchain_core.documents import Document

def data_converter():
    
    product_data = pd.read_csv("data/flipkart_product_review.csv")

    data = product_data[['product_title','review']]

    product_list = []

    for index , row in data.iterrows():

        obj = {
            "product_title": row['product_title'],
            "review": row['review']
        }

        product_list.append(obj)

    docs = []

    for  product in product_list:

        meta_data = {"product_title":product['product_title']}

        doc = Document(page_content=product['review'], metadata=meta_data)

        docs.append(doc)

    return docs