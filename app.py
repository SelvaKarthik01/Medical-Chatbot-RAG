from flask import Flask, render_template, jsonify, request
from src.helpers import download_embeddings
from langchain_pinecone import PineconeVectorStore 
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from src.prompt import *
from pinecone import Pinecone
import os

embeddings = download_embeddings()

pinecone_api_key = "pcsk_3TuLAy_CraGA48vUGfGZzzMw6W5z1vNsvXrzi2SnQWv8s4WovxatnQc8NarzFdDe8Lnr4x"
index_name = "medical-chatbot"

# Initialize Pinecone client
pc = Pinecone(api_key=pinecone_api_key)
index = pc.Index(index_name)

# Create vector store from existing index
docsearch = PineconeVectorStore(
    index=index,
    embedding=embeddings,
    text_key="text"
)
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})
groq_api_key = "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"

# Initialize Groq chat model (Free and Fast!)
chatModel = ChatGroq(
    model="llama3-8b-8192",
    api_key=groq_api_key,
    temperature=0.1
)
prompt = ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt),
        ("human","{input}")
    ]
)
question_answer_chain = create_stuff_documents_chain(chatModel,prompt)
rag_chain = create_retrieval_chain(retriever,question_answer_chain)

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET","POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input": msg})
    print("Response : ",response["answer"])
    return str(response["answer"])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)