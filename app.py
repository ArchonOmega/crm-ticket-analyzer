import streamlit as st
import pandas as pd
from utils import analyzer

st.set_page_config(page_title="CRM Ticket Analyzer", layout="wide")

st.title("CRM Support Ticket Analyzer")
st.markdown("Upload your exported ticket data (CSV) to get a breakdown of issues, categories, priorities, and flagged tickets.")

# File uploader
uploaded_file = st.file_uploader("Upload your ticket CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    st.subheader("Raw Ticket Data")
    st.dataframe(df.head(10))

    # Summary stats
    summary = analyzer.summarize_tickets(df)
    st.subheader("Summary")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Tickets", summary['total'])
    col2.metric("Open Tickets", summary['open'])
    col3.metric("High Priority", summary['high_priority'])

    # Charts
    st.subheader("Ticket Categories")
    st.plotly_chart(analyzer.plot_ticket_categories(df), use_container_width=True)

    st.subheader("Priority Distribution")
    st.plotly_chart(analyzer.plot_priority_bar(df), use_container_width=True)

    # Flagged tickets
    flagged = analyzer.flag_tickets(df)
    st.subheader("Flagged High Priority Open Tickets")
    st.dataframe(flagged)
else:
    st.info("Please upload a CSV file to begin.")
