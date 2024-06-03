import streamlit as st
import datetime
import sqlite3
from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load GPT-2 model and tokenizer
model_name = 'gpt2-medium'
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Database connection
conn = sqlite3.connect('study_plan.db')
c = conn.cursor()

# Create tables if they do not exist
c.execute('''CREATE TABLE IF NOT EXISTS plans
             (language TEXT, plan TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS progress
             (language TEXT, current_day INTEGER, start_date TEXT)''')
c.execute('''CREATE TABLE IF NOT EXISTS chat_history
             (language TEXT, day INTEGER, explanation TEXT)''')

conn.commit()

def generate_text(prompt, max_length=200):
    inputs = tokenizer.encode(prompt, return_tensors='pt')
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1)
    text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return text

def generate_study_plan(language, time_frame, level):
    prompt = f"Generate a {time_frame}-day study plan for learning {language} at {level} level."
    return generate_text(prompt)

def explain_topic(topic):
    prompt = f"Explain the topic '{topic}' in detail with examples and code snippets."
    return generate_text(prompt)

def store_plan(language, plan):
    c.execute("INSERT INTO plans (language, plan) VALUES (?, ?)", (language, plan))
    conn.commit()

def retrieve_plan(language):
    c.execute("SELECT plan FROM plans WHERE language = ?", (language,))
    result = c.fetchone()
    return result[0] if result else None

def store_progress(language, current_day, start_date):
    c.execute("INSERT INTO progress (language, current_day, start_date) VALUES (?, ?, ?)", (language, current_day, start_date))
    conn.commit()

def update_progress(language, current_day):
    c.execute("UPDATE progress SET current_day = ? WHERE language = ?", (current_day, language))
    conn.commit()

def retrieve_progress(language):
    c.execute("SELECT current_day, start_date FROM progress WHERE language = ?", (language,))
    result = c.fetchone()
    return result if result else (None, None)

def store_chat_history(language, day, explanation):
    c.execute("INSERT INTO chat_history (language, day, explanation) VALUES (?, ?, ?)", (language, day, explanation))
    conn.commit()

def retrieve_chat_history(language):
    c.execute("SELECT day, explanation FROM chat_history WHERE language = ?", (language,))
    return c.fetchall()

st.sidebar.title("Study Plan Generator")
language = st.sidebar.text_input("Enter the language you want to study")
time_frame = st.sidebar.number_input("Enter the number of days for the plan", min_value=1, max_value=365)
level = st.sidebar.selectbox("Select your level", ["Beginner", "Intermediate", "Advanced"])

if st.sidebar.button("Generate Plan"):
    existing_plan = retrieve_plan(language)
    if not existing_plan:
        plan = generate_study_plan(language, time_frame, level)
        store_plan(language, plan)
        store_progress(language, 1, datetime.datetime.now().strftime("%Y-%m-%d"))
        st.sidebar.success(f"Plan for {language} generated!")
    else:
        st.sidebar.info(f"Plan for {language} already exists.")

st.title("Your Study Plan")

current_day, start_date = retrieve_progress(language)

if current_day:
    st.header(f"Plan for {language}")
    plan = retrieve_plan(language).split("\n")
    st.subheader(f"Day {current_day}: {plan[current_day - 1]}")

    if st.button("Explain Today's Topic"):
        topic = plan[current_day - 1]
        explanation = explain_topic(topic)
        store_chat_history(language, current_day, explanation)
        st.write(explanation)

    if st.button("Next Day"):
        update_progress(language, current_day + 1)
        st.experimental_rerun()
else:
    st.write("Generate a study plan to get started.")

st.sidebar.title("Chat History")

if st.sidebar.button("Load Chat History"):
    chat_history = retrieve_chat_history(language)
    if chat_history:
        for day, explanation in chat_history:
            st.sidebar.write(f"Day {day}: {explanation}")
    else:
        st.sidebar.write("No chat history found.")
