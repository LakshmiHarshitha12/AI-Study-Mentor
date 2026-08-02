import streamlit as st
from pdf_reader import read_pdf
from word_reader import read_word
from summarizer import summarize

st.title("📚 AI Study Mentor")
st.write("👋 Welcome! Upload a PDF or Word document and I'll help you learn it.")

st.sidebar.title("Study Options")

generate_summary = st.sidebar.checkbox("Summary", value=True)
generate_history = st.sidebar.checkbox("History", value=True)
generate_topics = st.sidebar.checkbox("Important Topics", value=True)
generate_concepts = st.sidebar.checkbox("Key Concepts", value=True)
generate_applications = st.sidebar.checkbox("Applications", value=True)
generate_interview = st.sidebar.checkbox("Interview Questions", value=True)
generate_quiz = st.sidebar.checkbox("Quiz", value=True)
generate_flashcards = st.sidebar.checkbox("Flashcards", value=True)

uploaded_file = st.file_uploader(
    "Choose a PDF or Word document",
    type=["pdf", "docx"]
)

if uploaded_file is not None:

    # Read the uploaded document
    if uploaded_file.name.endswith(".pdf"):
        document_text = read_pdf(uploaded_file)

    elif uploaded_file.name.endswith(".docx"):
        document_text = read_word(uploaded_file)

    # Show success message
    st.success("✅ Document read successfully!")

    # Show extracted text (optional)
    with st.expander("View Extracted Text"):
        st.text_area("Extracted Text", document_text, height=300)

    # Generate AI Summary
    with st.spinner("🤖 AI is reading your document..."):
        summary = summarize(document_text)

    # Display summary
    st.subheader("📖 AI Summary")
    st.markdown(summary)




