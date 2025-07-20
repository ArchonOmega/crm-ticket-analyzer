# utils/analyzer.py

import pandas as pd
import plotly.express as px

def plot_ticket_categories(df):
    df.columns = df.columns.str.strip()  # Clean headers
    if 'Category' not in df.columns:
        raise ValueError("Missing 'Category' column in uploaded data.")
    
    dist = df['Category'].value_counts().reset_index()
    dist.columns = ['Category', 'Count']
    
    return px.pie(
        dist,
        names='Category',
        values='Count',
        title='Tickets by Category'
    )


def plot_ticket_status(df):
    df.columns = df.columns.str.strip()
    if 'Status' not in df.columns:
        raise ValueError("Missing 'Status' column in uploaded data.")
    
    dist = df['Status'].value_counts().reset_index()
    dist.columns = ['Status', 'Count']
    
    return px.bar(
        dist,
        x='Status',
        y='Count',
        title='Tickets by Status',
        color='Status'
    )


def plot_priority_distribution(df):
    df.columns = df.columns.str.strip()
    if 'Priority' not in df.columns:
        raise ValueError("Missing 'Priority' column in uploaded data.")
    
    dist = df['Priority'].value_counts().reset_index()
    dist.columns = ['Priority', 'Count']
    
    return px.bar(
        dist,
        x='Priority',
        y='Count',
        title='Tickets by Priority',
        color='Priority'
    )
