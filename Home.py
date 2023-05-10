import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/linkedin.jpg", width=300)

with col2:
    st.title("Miika Myötänen")
    content = """This is my portfolio webpage, consisting of my Python projects
    from various coding courses and some of my own ideas, website is made
     with only Python!"""
    st.info(content)



