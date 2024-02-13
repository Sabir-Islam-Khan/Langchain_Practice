import langchain_helper as helper 
import streamlit as st 

st.title("Car Suggestion LangChain")
st.markdown("<div style='margin-bottom:20px'></div>", unsafe_allow_html=True)
car_make = st.selectbox("What type of car you like?", ("German", "Japanese", "Italian", "American", "French"))
st.markdown("<div style='margin-bottom:10px'></div>", unsafe_allow_html=True)
budget = st.selectbox("What is your budget range?", ("10000$-20000$", "25000$-40000$", "70000$-100000$", "More than 100000$"))

is_searched = st.button(label="Search")

if is_searched:
    response = helper.suggest_cars(car_make, budget)
    with st.container():
        st.write(response["text"], type="info")
