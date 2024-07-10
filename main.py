from langchain_setup import get_few_shot_db_chain
import streamlit as st

#Setting out online shop streamlit page
st.title("Rude Manners T Shirts: Database Q&A")
question = st.text_input("Question: ")

if question:
    chain = get_few_shot_db_chain()
    answer = chain.run(question)
    st.header("Answer: ")
    st.write(answer)