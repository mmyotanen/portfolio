import streamlit as st
from send_email import send_email

st.set_page_config(layout="wide")
st.header("Contact me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address", key="email")
    raw_message = st.text_area("Your message", key="msg")
    submit = st.form_submit_button("Submit")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
    """

    if submit:
        send_email(message)
        st.info("Your email was sent successfully!")