import streamlit as st

def show_metrics(summary):

    c1, c2, c3= st.columns(3)

    c1.metric(
        "Processed",
        summary["processed"],
    )

    c2.metric(
        "Skipped",
        summary["skipped"],
    )

    c3.metric(
        "Avg Confidence",
        f"{summary['avg_confidence']:.1%}",
    )

