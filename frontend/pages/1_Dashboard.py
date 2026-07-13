import streamlit as st
from services.api import API
from components.metrics import show_metrics
import pandas as pd
import json
from datetime import datetime
from components.category_style import CATEGORY_COLORS


def color_category(value):
    color = CATEGORY_COLORS.get(value, "#6b7280")

    return f"""
        background-color: {color};
        color: white;
        font-weight: bold;
    """


st.set_page_config(
    page_title="Dashboard",
    layout="wide",
)

history = API.history()

st.title("📨 Dashboard")

if st.button(
    "✨ Classify Inbox",
    use_container_width=True,
):
    with st.spinner("Classifying emails..."):
        API.classify_inbox()

    st.success(f"Successfully classified {len(history)} emails.")


if history:

    processed = len(history)

    avg_conf = sum(h["final"]["confidence"] for h in history) / processed

    summary = {
        "processed": processed,
        "skipped": 0,
        "avg_confidence": avg_conf,
    }

    show_metrics(summary)


rows = []

for h in history:
    # Some records use 'timestamp' while others may have 'received_at'.
    # Use 'received_at' if present, otherwise fall back to 'timestamp'.
    received = h.get("received_at") or h.get("timestamp")

    if received:
        try:
            date = datetime.fromisoformat(received).strftime("%d %b")
        except Exception:
            # If parsing fails, fall back to the raw value or a short substring
            date = str(received).split("T")[0]
    else:
        date = ""

    rows.append(
        {
            "Sender": h["sender"],
            "Subject": h["subject"],
            "Category": h["final"]["category"],
            "Date": date,
            "Confidence": round(
                h["final"]["confidence"],
                2,
            ),
            "Source": h["decision_source"],
        }
    )

df = pd.DataFrame(rows)

styled = df.style.map(
    color_category,
    subset=["Category"],
)

st.dataframe(
    styled,
    use_container_width=True,
    hide_index=True,
)


col1, col2 = st.columns(2)

col1.download_button(
    "Download JSON",
    json.dumps(
        history,
        indent=2,
    ),
    "emails.json",
    "application/json",
)

col2.download_button(
    "Download CSV",
    df.to_csv(index=False),
    "emails.csv",
    "text/csv",
)
