import streamlit as st
from PyPDF2 import PdfReader
from transformers import pipeline

st.title("📄 PDF Text Extractor & Summarizer")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    try:

        pdf = PdfReader(uploaded_file)
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"

        st.header("Extracted Text")
        st.text_area("Full text from PDF", text, height=300)

        # Summarization
        st.header("Summary")
        if len(text.strip()) == 0:
            st.warning("No extractable text found in PDF.")
        else:
            summarizer = pipeline("summarization")

            # Summarize in chunks for long text
            max_chunk = 1000
            text_chunks = [text[i:i+max_chunk] for i in range(0, len(text), max_chunk)]

            summary = ""
            with st.spinner("Generating summary..."):
                for chunk in text_chunks:
                    summ = summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
                    summary += summ + " "

            st.write(summary.strip())

    except Exception as e:
        st.error(f"Error processing PDF: {e}")
else:
    st.info("Please upload a PDF file to extract and summarize its content.")
