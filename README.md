# 📘 DocuChat

**Chat with your PDFs — powered by LangChain, OpenAI, and Streamlit.**

> DocuChat is an AI-powered web application that allows you to interact with your PDF documents using natural language.  
Simply upload a PDF, ask questions, and get accurate, context-aware answers — just like chatting with a human who’s read the entire file.

---

## 🚀 Features

- 🧾 **PDF Upload:** Easily upload any PDF document.
- 🔍 **Smart Retrieval:** Automatically extracts and indexes text for fast, accurate lookup.
- 🤖 **AI Chat:** Uses GPT-4 (via LangChain) to answer questions conversationally.
- 🧠 **Context Memory:** Remembers previous questions for natural multi-turn conversations.
- ⚙️ **LangChain + RAG:** Built with Retrieval-Augmented Generation using FAISS vector search.
- 🌐 **Streamlit UI:** Intuitive and modern chat-style interface.

---

## 🧠 How It Works

1. **Upload** a PDF file.  
2. **Extract & Split:** Text is extracted and split into manageable chunks.  
3. **Embed:** Each chunk is converted into numerical vectors using OpenAI embeddings.  
4. **Store:** Embeddings are stored in a FAISS vector database for similarity search.  
5. **Retrieve & Answer:** When you ask a question, LangChain retrieves relevant chunks and GPT-4 generates an accurate response.  
6. **Remember:** Conversation history is preserved using LangChain’s memory module.

---

## 🏗️ Tech Stack

| Component | Description |
|------------|-------------|
| **Frontend** | Streamlit |
| **LLM** | OpenAI GPT-4 / GPT-3.5 |
| **Framework** | LangChain |
| **Vector Store** | FAISS |
| **Embeddings** | OpenAIEmbeddings |
| **PDF Parsing** | PyPDFLoader |
| **Memory** | ConversationBufferMemory |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/yourusername/docuchat.git
cd docuchat
```

### 2️⃣ Create a virtual environment
``` bash
python -m venv venv
source venv/bin/activate  # (use venv\Scripts\activate on Windows)
```

### 3️⃣ Install dependencies
``` bash
pip install -r requirements.txt
```

### 4️⃣ Add your OpenAI API key

Create a file named .env in the project root:

``` bash
OPENAI_API_KEY=your_openai_api_key_here
```

### 5️⃣ Run the app
``` bash
streamlit run app.py
```

Then open your browser at:

> http://localhost:8501

## 📦 Requirements

``` requirements.txt ```

- streamlit
- langchain
- langchain-community
- langchain-openai
- openai
- faiss-cpu
- tiktoken
- python-dotenv
- PyPDF2

---

## 📚 Example

### You: What is LangChain?
DocuChat: LangChain is a framework for developing applications powered by large language models. It enables chaining together LLMs, prompts, and retrievers to build complex reasoning systems.

---

## 💡 Future Enhancements

- 🗂 Support for multiple PDFs

- 💬 Persistent chat history

- 🧾 Source citations (showing which page info came from)

- 🧠 Local model support (Ollama, GPT4All)

- 🌈 UI improvements with Streamlit Chat Elements
 
 ---

## 👨‍💻 Author

Developed by [Sanjeevi Kumar V](https://github.com/sanjeevidev/) \
Built with ❤️ using LangChain, OpenAI, and Streamlit.

---

## 🪄 License

This project is licensed under the MIT License — feel free to use and modify.

---

> “DocuChat — your intelligent document companion.”
