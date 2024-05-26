import streamlit as st 
from PyPDF2 import PdfReader
from langchain_core.messages import AIMessage, HumanMessage



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
    if "chat_hist" not in st.session_state:
        st.session_state.chat_hist = [
            AIMessage("Hello! I am your Document guide. How can I help you today?")
        ]
    user_query  = st.chat_input("Type your message here...")
    if user_query is not None and user_query != "":
        response = get_response(user_query)
        st.session_state.chat_hist.append(HumanMessage(user_query)) 
        st.session_state.chat_hist.append(AIMessage(response))
        

    #conversation
    for msg in st.session_state.chat_hist:
        if isinstance(msg, AIMessage):
            with st.chat_message("AI"):
                st.write(msg.content)
        else:
            with st.chat_message("Human"):
                st.write(msg.content)





