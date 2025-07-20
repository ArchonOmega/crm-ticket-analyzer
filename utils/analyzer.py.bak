# utils/analyzer.py

import pandas as pd
import plotly.express as px

def summarize_tickets(df):
    total_tickets = len(df)
    open_tickets = df[df['Status'].str.lower() != 'resolved'].shape[0]
    high_priority = df[df['Priority'].str.lower() == 'high'].shape[0]

    return {
        "total": total_tickets,
        "open": open_tickets,
        "high_priority": high_priority
    }

def get_category_distribution(df):
    return df['Category'].value_counts().reset_index().rename(columns={'index': 'Category', 'Category': 'Count'})

def plot_ticket_categories(df):
    dist = get_category_distribution(df)
    fig = px.pie(dist, names='Category', values='Count', title='Tickets by Category')
    return fig

def plot_priority_bar(df):
    priority_count = df['Priority'].value_counts().reset_index().rename(columns={'index': 'Priority', 'Priority': 'Count'})
    fig = px.bar(priority_count, x='Priority', y='Count', title='Tickets by Priority', color='Priority')
    return fig

def flag_tickets(df):
    # Return flagged subset of tickets (e.g., high priority & unresolved)
    return df[(df['Priority'].str.lower() == 'high') & (df['Status'].str.lower() != 'resolved')]
