# 🏥 Medical Chatbot with RAG Architecture

A powerful medical question-answering chatbot built using Retrieval-Augmented Generation (RAG) architecture. This chatbot leverages medical encyclopedia data to provide accurate, context-aware responses to medical queries.
<img width="704" height="659" alt="image" src="https://github.com/user-attachments/assets/ff7e0f1e-9a93-47f3-a704-4448523e6c7c" />


## 🌟 Features

- **RAG Architecture**: Combines retrieval from medical documents with generative AI
- **Medical Knowledge Base**: Powered by "The Gale Encyclopedia of Medicine 3rd Edition"
- **Free AI Model**: Uses Groq's Llama3-8b-8192 model (no OpenAI billing required)
- **Vector Search**: Pinecone vector database for efficient document retrieval
- **Web Interface**: Clean, responsive chat interface built with Flask
- **Real-time Responses**: Fast inference with Groq's optimized infrastructure

## 🏗️ Architecture

```
User Query → Embedding → Vector Search → Document Retrieval → LLM Processing → Response
```

### Components:
1. **Document Processing**: PDF medical encyclopedia split into chunks
2. **Embeddings**: HuggingFace sentence-transformers for text vectorization
3. **Vector Store**: Pinecone for similarity search
4. **LLM**: Groq's Llama3-8b-8192 for response generation
5. **Web App**: Flask-based chat interface

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Pinecone account (free tier available)
- Groq account (free tier available)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/SelvaKarthik01/Medical-Chatbot.git
   cd Medical-Chatbot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API Keys**
   - Get Pinecone API key from [Pinecone Console](https://app.pinecone.io/)
   - Get Groq API key from [Groq Console](https://console.groq.com/keys)
   - Update API keys in `app.py`

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the chatbot**
   - Open your browser and go to `http://localhost:8080`

## 📁 Project Structure

```
Medical-Chatbot/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── setup.py              # Package setup configuration
├── data/                 # Medical documents
│   └── The-Gale-Encyclopedia-of-Medicine-3rd-Edition...pdf
├── src/                  # Source code modules
│   ├── __init__.py
│   ├── helpers.py        # Utility functions
│   ├── prompt.py         # System prompts
│   └── store_index.py    # Vector store operations
├── templates/            # HTML templates
│   └── chat.html         # Chat interface
├── static/               # Static files
│   └── style.css         # Styling
└── research/             # Jupyter notebooks
    └── trials.ipynb      # Development and testing
```

## 🔧 Key Components

### Document Processing (`src/helpers.py`)
- **PDF Loading**: Extract text from medical encyclopedia
- **Text Splitting**: Chunk documents for optimal retrieval
- **Embeddings**: Convert text to vector representations

### Vector Store (`app.py`)
- **Pinecone Integration**: Cloud-based vector database
- **Similarity Search**: Find relevant medical information
- **Retrieval**: Get top-k most relevant document chunks

### Language Model
- **Groq Llama3-8b-8192**: Fast, free inference
- **Temperature 0.1**: Focused, consistent responses
- **System Prompt**: Medical assistant persona

## 🎯 Usage Examples

### Sample Queries:
- "What is acne and what causes it?"
- "What are the symptoms of diabetes?"
- "How is hypertension treated?"
- "What is the difference between viral and bacterial infections?"

### Expected Response Format:
- Concise (max 3 sentences)
- Medically accurate
- Based on encyclopedia content
- Clear "I don't know" when information unavailable

## 🔑 Configuration

### API Keys Setup
Update the following in `app.py`:

```python
# Pinecone Configuration
pinecone_api_key = "your_pinecone_api_key_here"
index_name = "medical-chatbot"

# Groq Configuration  
groq_api_key = "your_groq_api_key_here"
```

### Model Configuration
```python
chatModel = ChatGroq(
    model="llama3-8b-8192",    # Free, fast model
    api_key=groq_api_key,
    temperature=0.1            # Low for consistency
)
```

## 🛠️ Development

### Setting up Development Environment

1. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install in development mode**
   ```bash
   pip install -e .
   ```

3. **Run Jupyter notebook for experimentation**
   ```bash
   jupyter notebook research/trials.ipynb
   ```

### Data Processing Pipeline

1. **Load Documents**: PDF → Text chunks
2. **Create Embeddings**: Text → Vectors (384 dimensions)
3. **Store in Pinecone**: Vector database setup
4. **Build Retriever**: Similarity search configuration
5. **Setup RAG Chain**: Retrieval + Generation pipeline

## 🔄 RAG Pipeline Details

### Retrieval Phase:
1. User query embedded using sentence-transformers
2. Similarity search in Pinecone vector database
3. Top 3 most relevant document chunks retrieved

### Generation Phase:
1. Retrieved context combined with user query
2. Sent to Groq's Llama3 model with medical prompt
3. Concise, accurate response generated

## 🎨 Web Interface

### Features:
- **Responsive Design**: Works on desktop and mobile
- **Real-time Chat**: Instant message exchange
- **Medical Theme**: Professional healthcare styling
- **Message History**: Conversation tracking
- **Typing Indicators**: Enhanced user experience

### Technologies:
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Backend**: Flask (Python)
- **AJAX**: Asynchronous communication

## 📦 Dependencies

### Core Libraries:
- **LangChain**: RAG framework and document processing
- **Pinecone**: Vector database
- **Groq**: Fast LLM inference
- **Flask**: Web application framework
- **Sentence Transformers**: Text embeddings

### Installation:
```bash
pip install langchain==0.3.26
pip install flask==3.1.1
pip install sentence-transformers==4.1.0
pip install pypdf==5.6.1
pip install langchain-pinecone==0.2.8
pip install langchain-community==0.3.26
pip install langchain-groq
```

## 🚨 Troubleshooting

### Common Issues:

1. **API Key Errors**
   - Verify Pinecone and Groq API keys
   - Check key permissions and quotas

2. **Import Errors**
   - Update to latest LangChain version
   - Install missing dependencies

3. **Vector Store Connection**
   - Ensure Pinecone index exists
   - Check index name and configuration

4. **Slow Responses**
   - Check internet connection
   - Verify Groq API status

### Debug Mode:
Run with debug output:
```bash
python app.py
```
Check console for detailed error messages.

## 🔮 Future Enhancements

### Planned Features:
- [ ] **Multi-source Knowledge**: Add more medical databases
- [ ] **User Authentication**: Secure access control
- [ ] **Conversation Memory**: Context-aware conversations
- [ ] **Medical Specializations**: Specialized knowledge domains
- [ ] **Voice Interface**: Speech-to-text integration
- [ ] **Mobile App**: React Native implementation

### Technical Improvements:
- [ ] **Caching**: Redis for faster responses
- [ ] **Monitoring**: Application performance tracking
- [ ] **Testing**: Comprehensive test suite
- [ ] **Deployment**: Docker containerization
- [ ] **CI/CD**: Automated deployment pipeline

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Author

**Selva Karthik**
- GitHub: [@SelvaKarthik01](https://github.com/SelvaKarthik01)
- Project: [Medical-Chatbot](https://github.com/SelvaKarthik01/Medical-Chatbot-RAG)

## 🙏 Acknowledgments

- **The Gale Encyclopedia of Medicine** for the comprehensive medical knowledge base
- **Groq** for providing free, fast LLM inference
- **Pinecone** for the vector database infrastructure
- **LangChain** for the RAG framework
- **HuggingFace** for the embedding models

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Open an issue on GitHub
3. Refer to the documentation of individual components:
   - [LangChain Docs](https://python.langchain.com/)
   - [Pinecone Docs](https://docs.pinecone.io/)
   - [Groq Docs](https://console.groq.com/docs)

---

**⚠️ Disclaimer**: This chatbot is for educational and informational purposes only. Always consult qualified healthcare professionals for medical advice, diagnosis, or treatment.


