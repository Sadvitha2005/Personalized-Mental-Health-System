import streamlit as st

def menu():
    st.sidebar.title("Navigation")
    st.sidebar.page_link("app.py", label="Welcome")
    st.sidebar.page_link("pages/depression_test.py", label="Depression Test")
    st.sidebar.page_link("pages/selfEsteem_test.py", label="Self Esteem Test")
    st.sidebar.page_link("pages/socialAnxiety_test.py", label="Social Anxiety Test")
    st.sidebar.page_link("pages/insomnia&sleepProblems_test.py", label="Insomnia & Sleep Problems Test")