from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import PromptTemplate
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

# Load the open-source summarization model (DistilBART-CNN from Hugging Face)
model_id = "sshleifer/distilbart-cnn-12-6"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSeq2SeqLM.from_pretrained(model_id)

# Create the Hugging Face pipeline for summarization
summarizer_pipe = pipeline(
    "summarization",
    model=model,
    tokenizer=tokenizer,
    max_new_tokens=100,  # Limit summary length
    min_length=30,       # Minimum summary length
    do_sample=False      # Deterministic output
)

# Wrap the pipeline in LangChain's HuggingFacePipeline
llm = HuggingFacePipeline(pipeline=summarizer_pipe)

# Define a prompt template for the summarization task
template = """Summarize the following text concisely:

{text}

Summary:"""
prompt = PromptTemplate.from_template(template)

# Create the LangChain chain: Prompt + LLM
chain = prompt | llm

# Function to get user input and generate summary
def summarize_text():
    print("Enter the text to summarize (or type 'exit' to quit):")
    while True:
        input_text = input("> ")
        if input_text.lower() == 'exit':
            break
        if not input_text.strip():
            print("Please enter some text.")
            continue
        
        # Invoke the chain
        result = chain.invoke({"text": input_text})
        print("\nSummary:\n", result, "\n")

# Run the app
if __name__ == "__main__":
    summarize_text()