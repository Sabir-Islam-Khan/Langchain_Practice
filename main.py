import streamlit as st
import langchain_helper as helper
st.title("Emotion Category Detector")


st.markdown("<div style='margin-bottom:20px'></div>", unsafe_allow_html=True)

human_text = st.text_area(label="Please enter how you feel:", height=150)

st.markdown("<div style='margin-bottom:20px'></div>", unsafe_allow_html=True)

is_searched = st.button(label="Detect Emotion")


st.markdown("<div style='margin-bottom:20px'></div>", unsafe_allow_html=True)

if is_searched:
    if human_text.strip() != "":
        response = helper.detectEmotion(human_text)
        st.success(f"Detected Emotion Category: {response["text"]}")
    else:
        st.warning("Please enter some text before detecting emotion.")
