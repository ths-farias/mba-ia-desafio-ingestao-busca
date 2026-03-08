import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_postgres import PGVector

load_dotenv()

PDF_PATH = os.getenv("PDF_PATH")
path_object = PyPDFLoader("document.pdf")
connection = os.getenv("DATABASE_URL")
collection_name = os.getenv("PG_VECTOR_COLLECTION_NAME")


def ingest_pdf():
    embeddings = None

    if os.getenv("OPENAI_API_KEY"):
        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        print("Initialized OpenAIEmbeddings")
    elif os.getenv("GOOGLE_API_KEY"):
        embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-001")
        print("Initialized OpenAIEmbeddings")
    else:
        raise ValueError("API KEY environment variable is not set")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=150, separators=["\n\n", "\n", " ", ""]
    )
    texts = text_splitter.split_documents(path_object.load())

    vector_store = PGVector(
        embeddings=embeddings,
        collection_name=collection_name,
        connection=connection,
        use_jsonb=True,
    )

    vector_store.add_documents(texts)


if __name__ == "__main__":
    ingest_pdf()
