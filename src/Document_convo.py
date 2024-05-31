import streamlit as st 
from PyPDF2 import PdfReader
from langchain_core.messages import AIMessage, HumanMessage
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI



def get_response(user_query):
    response = "How can I help you today?"
    return response
#app config
st.set_page_config(page_title="Chat with your Document", page_icon="🤖")
st.title("Document Tutor")

#sidebar
with st.sidebar:
    
    from io import StringIO
    pdf = st.file_uploader("Choose a file",type="pdf")
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text=""
        for page in pdf_reader.pages:
            text+=page.extract_text()
        st.write(text)

    
if pdf is None or pdf == "":
    st.info("Please upload a file")
else: 
    
    pdf_reader = PdfReader(pdf)
    text=""
    for page in pdf_reader.pages:
        text+=page.extract_text()
        
    #split into chunks
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    
    #creating embeddings
    embeddings = OpenAIEmbeddings()
    knowledge_base = FAISS.from_texts(chunks, embeddings)
    
    
    
    
    user_query  = st.chat_input("Ask question about your PDF")
    if user_query is not None and user_query != "":
        docs = knowledge_base.similarity_search(user_query)
        
        llm = OpenAI()
        chain = load_qa_chain(llm,chain_type = "stuff")
        with get_openai_callback() as cb:
            response = chain.run(input_documents=docs, question=user_query)
            print(cb)
        st.write(response)
        

    #conversation
    for msg in st.session_state.chat_hist:
        if isinstance(msg, AIMessage):
            with st.chat_message("AI"):
                st.write(msg.content)
        else:
            with st.chat_message("Human"):
                st.write(msg.content)





