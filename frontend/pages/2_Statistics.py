import streamlit as st
import pandas as pd
import plotly.express as px

from services.api import API


st.set_page_config(
    page_title="Statistics",
    layout="wide",
)

st.title("📊 Statistics")

stats = API.stats()

if not stats:
    st.warning("No statistics available.")
    st.stop()
    
c1, c2 = st.columns(2)

c1.metric(
    "Emails Processed",
    stats["total_processed"],
)

c2.metric(
    "Average Confidence",
    f"{stats['average_confidence']:.1%}",
)

col1, col2 = st.columns([1, 5])

with col1:
    if st.button("🔄 Refresh"):
        st.rerun()

st.subheader("📂 Category Distribution")

category_df = pd.DataFrame(
    {
        "Category": stats["categories"].keys(),
        "Count": stats["categories"].values(),
    }
)

fig = px.bar(
    category_df,
    x="Category",
    y="Count",
    text="Count",
)

st.plotly_chart(
    fig,
    use_container_width=True,
)


st.subheader("🧠 Decision Sources")

source_df = pd.DataFrame(
    {
        "Source": stats["decision_source"].keys(),
        "Count": stats["decision_source"].values(),
    }
)

fig = px.pie(
    source_df,
    names="Source",
    values="Count",
)

st.plotly_chart(
    fig,
    use_container_width=True,
)

st.subheader("🤖 Models Used")

model_df = pd.DataFrame(
    {
        "Model": stats["models"].keys(),
        "Count": stats["models"].values(),
    }
)

st.dataframe(
    model_df,
    use_container_width=True,
    hide_index=True,
)

