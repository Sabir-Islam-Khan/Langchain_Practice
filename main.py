import langchain_helper as helper 
import streamlit as st 

st.title("Emotion Category Detector")
st.markdown("<div style='margin-bottom:20px'></div>", unsafe_allow_html=True)
human_text = st.text_input(label="Please enter how you feel:")
st.markdown("<div style='margin-bottom:10px'></div>", unsafe_allow_html=True)

is_searched = st.button(label="Detect")

if is_searched:
    response = helper.detectEmotion(human_text)
    with st.container():
        st.write(response["text"])
