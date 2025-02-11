import streamlit as st
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="gemma2-9b-it",
    temperature=0,
    groq_api_key="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"
)

st.title("GenAI Grammar Checker")
st.write("Query Box")
user_input = st.text_input("Write your sentence: ", "")

if st.button("Get Response") and user_input.strip():
    res = llm.invoke(user_input)  
    response_text = res.content if hasattr(res, "content") else str(res)
    
    st.write("Response👇: ")
    st.write(response_text)
