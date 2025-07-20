# app.py

import streamlit as st
import pandas as pd
from utils import analyzer

st.set_page_config(page_title="CRM Support Ticket Analyzer", layout="wide")
st.title("CRM Support Ticket Analyzer")
st.markdown("Upload a CSV of support tickets to see insights.")

uploaded_file = st.file_uploader("Upload your CRM ticket CSV file", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        df.columns = df.columns.str.strip().str.title()  # Normalize headers
        st.success("File uploaded successfully.")
        st.dataframe(df.head())

        # Charts Section
        st.subheader("Ticket Analysis")
        
        col1, col2 = st.columns(2)
        with col1:
            try:
                st.plotly_chart(analyzer.plot_ticket_categories(df), use_container_width=True)
            except Exception as e:
                st.error("Couldn't plot ticket categories.")
                st.exception(e)

        with col2:
            try:
                st.plotly_chart(analyzer.plot_ticket_status(df), use_container_width=True)
            except Exception as e:
                st.error("Couldn't plot ticket statuses.")
                st.exception(e)

        st.subheader("Priority Overview")
        try:
            st.plotly_chart(analyzer.plot_priority_distribution(df), use_container_width=True)
        except Exception as e:
            st.error("Couldn't plot ticket priorities.")
            st.exception(e)

    except Exception as e:
        st.error("Error loading the CSV. Please check the format.")
        st.exception(e)
