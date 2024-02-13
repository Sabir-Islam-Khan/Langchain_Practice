import langchain_helper as helper 
import streamlit as st 

st.title("Car Suggestion LangChain")
st.markdown("<div style='margin-bottom:20px'></div>", unsafe_allow_html=True)
st.selectbox("What type of car you like?", ("German", "Japaneese", "Italian", "American", "French"))
st.markdown("<div style='margin-bottom:10px'></div>", unsafe_allow_html=True)
st.selectbox("What is your budget range?", ("10000$-20000$", "25000$-40000$", "70000$-10000$", "More than 100000$"))

