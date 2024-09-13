from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_google_genai import ChatGoogleGenerativeAI
from src.components.data_transformation import ingestion
import os
from dotenv import load_dotenv

load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv("GOOGLE_API_KEY")


def generation(vector_store):

    retriever = vector_store.as_retriever(search_kwargs={"k":3})


    PRODUCT_BOT_TEMPLATE = """
    Your ecommercebot bot is an expert in product recommendations and customer queries.
    It analyzes product titles and reviews to provide accurate and helpful responses.
    Ensure your answers are relevant to the product context and refrain from straying off-topic.
    Your responses should be concise and informative.

    CONTEXT:
    {context}

    QUESTION: {question}

    YOUR ANSWER:
    
    """

    prompt = ChatPromptTemplate.from_template(PRODUCT_BOT_TEMPLATE)

    llm = ChatGoogleGenerativeAI(model="models/gemini-1.5-flash")

    chain = {"context":  retriever, "question": RunnablePassthrough()} | prompt | llm | StrOutputParser()

    return chain


if __name__  == "__main__":

    vectorstore =ingestion("Done")
    chain = generation(vectorstore)

    print(chain.invoke("Tell me about the low budget sound basshead"))