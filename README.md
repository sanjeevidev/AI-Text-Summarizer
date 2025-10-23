# 📝 AI Text Summarizer

[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/) 
[![Streamlit](https://img.shields.io/badge/streamlit-1.30-green)](https://streamlit.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**Summarize any text quickly — powered by LangChain, Hugging Face, and Streamlit.**

> AI Text Summarizer is a web application that generates concise, meaningful summaries from long text inputs. Simply paste your text and get a compressed version in seconds — all 100% local with no external API calls.

---

## 🚀 Features

- 📄 **Text Input:** Paste any text or document content to summarize.  
- 🤖 **AI Summarization:** Uses Hugging Face transformer models with LangChain pipeline integration.  
- ⚡ **Quick Summary:** Generate a shorter summary with fewer words.  
- 📊 **Word Count & Compression Metrics:** See the number of words in the original and summary and the compression ratio.  
- 🗑 **Clear Output:** Reset the summary and input text easily.  
- 🌐 **Streamlit UI:** Modern, clean interface with two-column layout and custom styling.  

---

## 🧠 How It Works

1. **Load Model:** Hugging Face’s `distilbart-cnn-12-6` model is loaded into a LangChain pipeline.  
2. **Input Text:** User enters text into the Streamlit text area.  
3. **Summarization:** The model generates a summary via a direct pipeline call for reliability.  
4. **Display Output:** Shows the summarized text along with word counts and compression metrics.  
5. **Quick or Full Summary:** Option to generate shorter or detailed summaries.  

---

## 🏗️ Tech Stack

| Component | Description |
|------------|-------------|
| **Frontend** | Streamlit |
| **LLM Integration** | LangChain + Hugging Face Pipeline |
| **Model** | `sshleifer/distilbart-cnn-12-6` (transformers) |
| **Backend Framework** | Python |
| **Caching** | Streamlit `st.cache_resource` and `st.cache_data` for performance |
| **Environment Variables** | Optional for further model configurations |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/sanjeevidev/AI-Text-Summarizer.git
cd AI-Text-Summarizer
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

### 4️⃣ Run the app
``` bash
streamlit run app.py
```

Then open your browser at:

> http://localhost:8501

## 📦 Requirements

``` requirements.txt ```

- streamlit
- langchain-huggingface
- transformers
- torch

---

## 📚 Example Usage

- Paste an article, essay, or paragraph into the input box.
- Click 🎯 Generate Summary for a detailed summary or 🔥 Quick Summary for a shorter one.
- See the summary appear instantly along with word count and compression stats.

---

## 💡 Future Enhancements

- 📌 Support file uploads (PDF, DOCX, TXT).
- 🧠 Integration with larger models for better summarization quality.
- 🌈 Advanced UI improvements for multi-document summarization.
- 💾 Option to download summarized text.

---

## 👨‍💻 Author

Developed by [Sanjeevi Kumar V](https://github.com/sanjeevidev/) \
Built with ❤️ using LangChain, Hugging Face, and Streamlit.

---

## 🪄 License

This project is licensed under the MIT License — feel free to use and modify.

---

> “AI Text Summarizer — compress long text into concise insights in seconds.”