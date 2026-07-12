import streamlit as st

st.set_page_config(
    page_title="AI Email Organizer",
    page_icon="📧",
    layout="wide",
)

st.title("📧 AI Email Organizer")

st.write("""
Organize your Gmail inbox using a
multi-stage AI classification pipeline.
""")

st.divider()

st.link_button(
    "Sign in with Google",
    "http://localhost:8000/auth/login",
    use_container_width=True,
)