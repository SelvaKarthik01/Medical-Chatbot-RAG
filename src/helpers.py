from langchain_community.embeddings import HuggingFaceEmbeddings
from typing import List
from langchain.schema import Document
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
def load_pdf_files(data):
    loader = DirectoryLoader(
        data,
        glob="*pdf",
        loader_cls = PyPDFLoader
        )
    documents = loader.load()
    return documents

def filter_to_minimal_docs(docs: List[Document]) -> List[Document]:
    # Implement filtering logic here
    minimal_docs: List[Document]=[]
    for doc in docs:
        src = doc.metadata.get("source")
        minimal_docs.append(
            Document(
                page_content=doc.page_content,
                metadata={"source": src,}
            )
        )
    return minimal_docs
def text_split(minimal_docs):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 20
    )
    texts_chunk = text_splitter.split_documents(minimal_docs)
    return texts_chunk
def download_embeddings():
    # https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2
    # 384 Dense Vector Model
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embeddings = HuggingFaceEmbeddings(
        model_name = model_name
    )
    return embeddings
