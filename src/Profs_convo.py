import streamlit as st 
from langchain_core.messages import AIMessage, HumanMessage



def get_response(user_query):
    response = "How can I help you today?"
    return response


#app config
st.set_page_config(page_title="Chat with our AI Professor", page_icon="🤖")
st.title("AI Professor")

#sidebar
with st.sidebar:
    
    option = st.selectbox(
    "Enter your preferred course",
    ("Maths", "Physics", "Chemistry","Biology","Computer Science"),index=None,placeholder="Select a course")
    
    duration_option = st.number_input("Enter the duration of the course in months", min_value=1, max_value=12, value=None,placeholder="Choose a duration")
    expertise = st.selectbox(
    "Enter your preferred expertise",
    ("Beginner", "Intermediate", "Advanced"),index=None,placeholder="Select an expertise")
    
    
if option is None or option == "" or duration_option is None or duration_option == "" or expertise is None or expertise == "":
    st.info("Please select a course")
else: 
    if "chat_hist" not in st.session_state:
        st.session_state.chat_hist = [
            AIMessage("Hello! I am your AI Professor. How can I help you today?")
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














