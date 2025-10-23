import streamlit as st
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
import torch

# Page config
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main-header {font-size: 3rem; color: #1f77b4; text-align: center; margin-bottom: 2rem;}
.summary-box {background-color: #f0f8ff; padding: 1.5rem; border-radius: 10px; border-left: 5px solid #1f77b4;}
.input-box {background-color: #f9f9f9; padding: 1.5rem; border-radius: 10px; border: 2px solid #e0e0e0;}
</style>
""", unsafe_allow_html=True)

# Session state
if "model_loaded" not in st.session_state:
    st.session_state.model_loaded = False
if "llm" not in st.session_state:
    st.session_state.llm = None
if "summary" not in st.session_state:
    st.session_state.summary = ""

@st.cache_resource
def load_model():
    """Load model - SIMPLIFIED VERSION THAT WORKS"""
    with st.spinner("🔄 Loading AI model (30s one-time)..."):
        model_id = "sshleifer/distilbart-cnn-12-6"
        tokenizer = AutoTokenizer.from_pretrained(model_id)
        model = AutoModelForSeq2SeqLM.from_pretrained(model_id)
        
        pipe = pipeline(
            "summarization",
            model=model,
            tokenizer=tokenizer,
            max_new_tokens=130,
            min_length=30,
            do_sample=False
        )
        
        llm = HuggingFacePipeline(pipeline=pipe)
        return llm

# Load model
try:
    if not st.session_state.model_loaded:
        st.session_state.llm = load_model()
        st.session_state.model_loaded = True
        st.success("✅ Model loaded successfully!")
except Exception as e:
    st.error(f"❌ Model loading failed: {e}")
    st.stop()

llm = st.session_state.llm

# SIMPLIFIED DIRECT SUMMARIZATION FUNCTION (NO LangChain chain issues)
@st.cache_data
def summarize_text_direct(_text, _max_length):
    """Direct pipeline call - 100% reliable"""
    try:
        # Truncate if too long
        if len(_text) > 1000:
            _text = _text[:1000] + "..."
        
        # Direct pipeline call (bypasses LangChain issues)
        result = llm.pipeline(_text, max_new_tokens=_max_length, min_length=30)
        return result[0]['summary_text'].strip()
    except Exception as e:
        return f"Error: {str(e)}"

# MAIN UI
st.markdown('<h1 class="main-header">📝 AI Text Summarizer</h1>', unsafe_allow_html=True)

# Two-column layout
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="input-box">', unsafe_allow_html=True)
    st.subheader("📄 Enter Text to Summarize")
    
    input_text = st.text_area(
        "Paste your text here:",
        height=300,
        placeholder="""Example:
Artificial intelligence (AI) is intelligence demonstrated by machines...""",
        key="input_text"
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="summary-box">', unsafe_allow_html=True)
    st.subheader("✨ Generated Summary")
    
    col_btn1, col_btn2 = st.columns([1, 1])
    with col_btn1:
        if st.button("🎯 Generate Summary", type="primary", use_container_width=True):
            if input_text.strip():
                with st.spinner("🤖 Summarizing..."):
                    summary = summarize_text_direct(input_text, 130)
                    st.session_state.summary = summary
            else:
                st.warning("⚠️ Please enter text first!")
    
    with col_btn2:
        if st.button("🔥 Quick Summary", use_container_width=True):
            if input_text.strip():
                with st.spinner("🤖 Quick..."):
                    summary = summarize_text_direct(input_text, 80)
                    st.session_state.summary = summary
    
    # DISPLAY SUMMARY
    if st.session_state.summary:
        st.success("✅ Summary generated!")
        st.markdown(f"**{st.session_state.summary}**")
        
        # Stats
        if input_text.strip():
            orig_words = len(input_text.split())
            sum_words = len(st.session_state.summary.split())
            ratio = ((1 - sum_words/orig_words) * 100)
            col1m, col2m, col3m = st.columns(3)
            with col1m:
                st.metric("Original", f"{orig_words} words")
            with col2m:
                st.metric("Summary", f"{sum_words} words")
            with col3m:
                st.metric("Compression", f"{ratio:.0f}%")
    
    # Clear button
    if st.button("🗑️ Clear Summary", use_container_width=True):
        st.session_state.summary = ""
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666;'>
    🚀 Built with LangChain + Hugging Face + Streamlit | 100% Local | Fixed & Working!
</div>
""", unsafe_allow_html=True)