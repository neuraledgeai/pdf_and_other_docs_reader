import streamlit as st
from PyPDF2 import PdfReader
from docx import Document

# Function to read PDF
def read_pdf(file):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        # Extract text and ensure paragraph separation
        page_text = page.extract_text()
        if page_text:
            text += page_text.strip() + "\n\n"  # Add extra line breaks
    return text

# Function to read Word document
def read_word(file):
    doc = Document(file)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return text

# File uploader
uploaded_file = st.file_uploader("Upload a PDF or Word file", type=["pdf", "docx"])

if uploaded_file is not None:
    file_type = uploaded_file.name.split(".")[-1].lower()
    
    if file_type == "pdf":
        try:
            text = read_pdf(uploaded_file)
            st.subheader("Extracted Text from PDF:")
            st.text_area("PDF Content", text, height=300)
        except Exception as e:
            st.error(f"Error reading PDF: {e}")
    
    elif file_type == "docx":
        try:
            text = read_word(uploaded_file)
            st.subheader("Extracted Text from Word Document:")
            st.text_area("Word Content", text, height=300)
        except Exception as e:
            st.error(f"Error reading Word document: {e}")
    
    else:
        st.error("Unsupported file type! Please upload a PDF or Word document.")
    

st.title("PDF/Document Reader")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
