import streamlit as st
from services.api import API

st.set_page_config(
    page_title="Dashboard",
    layout="wide",
)

st.title("📨 Dashboard")

st.info("No emails classified yet.")

if st.button(
    "✨ Classify Inbox",
    use_container_width=True,
):
    with st.spinner("Classifying emails..."):

        API.classify_inbox()

    st.success("Completed!")

    st.rerun()
