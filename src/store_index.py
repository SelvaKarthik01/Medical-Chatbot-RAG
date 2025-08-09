import os 
from src.helpers import load_pdf_files, filter_to_minimal_docs, text_split, download_embeddings
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore

extracted_data = load_pdf_files("data/")
minimal_docs = filter_to_minimal_docs(extracted_data)
texts_chunk = text_split(minimal_docs)

embeddings = download_embeddings()

pinecone_api_key = "pcsk_3TuLAy_CraGA48vUGfGZzzMw6W5z1vNsvXrzi2SnQWv8s4WovxatnQc8NarzFdDe8Lnr4x"
pc = Pinecone(api_key=pinecone_api_key)
from pinecone import ServerlessSpec
index_name = "medical-chatbot"

if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension = 384, #Dimensions of Embeddings
        metric = "cosine",
        spec = ServerlessSpec(cloud = "aws",region="us-east-1")
    )
index = pc.Index(index_name) 
docsearch = PineconeVectorStore(
    index=index,
    embedding=embeddings,
    text_key="text"
)

# Add the documents to the vector store
docsearch.add_documents(texts_chunk)