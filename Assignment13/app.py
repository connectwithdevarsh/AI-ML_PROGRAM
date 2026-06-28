import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly.express as px
from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv(override=True)

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Home", "Dataset Explorer", "AI Assistant"],
        icons=["house", "table", "robot"],
        menu_icon="cast",
        default_index=0
    )

if selected == "Home":
    st.title("Enterprise Analytics & AI Assistant Portal")
    st.write("This application helps in analyzing employee salary data using interactive charts and an AI assistant. You can explore the dataset and ask the AI questions about data analysis or career guidance.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="Total Records", value="35")
    with col2:
        st.metric(label="Target Variable", value="Salary")

elif selected == "Dataset Explorer":
    st.title("Dataset Explorer")
    df = pd.read_csv("employee_salary.csv")
    st.dataframe(df)
    
    fig = px.scatter(df, x="Years_Experience", y="Salary", title="Salary vs Experience")
    st.plotly_chart(fig)

elif selected == "AI Assistant":
    st.title("AI Assistant")
    
    api_key = os.getenv("GROQ_API_KEY")
    if api_key:
        api_key = api_key.strip("'\" ")
    
    if not api_key:
        st.warning("Please set the GROQ_API_KEY in your .env file.")

    else:
        client = Groq(api_key=api_key)
        
        if "messages" not in st.session_state:
            st.session_state.messages = []
            
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.write(msg["content"])
                
        user_query = st.chat_input("Ask the AI anything about data analysis or career paths...")
        
        if user_query:
            with st.chat_message("user"):
                st.write(user_query)
            st.session_state.messages.append({"role": "user", "content": user_query})
            
            try:
                res = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[
                        {"role": "user", "content": user_query}
                    ]
                )
                ans = res.choices[0].message.content
                
                with st.chat_message("assistant"):
                    st.write(ans)
                st.session_state.messages.append({"role": "assistant", "content": ans})
            except Exception as e:
                st.error(f"Error: {e}")

