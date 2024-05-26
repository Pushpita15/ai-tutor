import streamlit as st 
from langchain_core.messages import AIMessage, HumanMessage



def get_response(user_query):
    response = "How can I help you today?"
    return response
#app config
st.set_page_config(page_title="Get tutored for your coding skills", page_icon="🤖")
st.title("Coding Tutor")

#sidebar
with st.sidebar:
    
    option = st.selectbox(
    "Enter your preferred programming language",
    ("C", "C++", "Python","Java"))
    
    
if option is None or option == "":
    st.info("Please select a programming language")
else: 
    if "chat_hist" not in st.session_state:
        st.session_state.chat_hist = [
            AIMessage("Hello! I am your coding tutor. How can I help you today?")
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





