import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2, empty = st.columns([1.5, 2, 0.5])

with col1:
    st.image("images/linkedin.jpg", width=400)

with col2:
    st.title("Miika Myötänen")
    content = """
    This is my portfolio webpage, consisting of my Python projects
    from various coding courses and some of my own ideas, website is made
     with only Python!
     """
    st.info(content)

st.write("Below you can find some of the apps built in Python. Feel free to contact me!")


col3, empty, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image(f"images/{row['image']}")
        st.write(f"[Source Code]({row['url']})")





