import os
import dash
from dash import html, dash_table, dcc
import pandas as pd
import plotly.graph_objects as go

# Register page
dash.register_page(__name__, path='/dataset', name="Dataset 📄")

# Load the data
data = pd.read_csv('H:\Zunaira\Machine Learning\Data Preprocessing\Heart Disease Prediction\Heart Disease Dataset.csv')

# Page Layout
layout = html.Div(children=[
    html.Br(),
    # Title section
    html.H3("User Behavior Dataset", className="text-center text-dark mb-4"),

    # Description section
    html.P("This table displays the user behavior dataset, which contains various features like device specifications, "
           "app usage patterns, and demographic information of the users.", className="text-center text-dark mb-4"),

    # DataTable displaying the dataset
    dash_table.DataTable(
        data=data.to_dict('records'),
        page_size=20,  # Number of rows per page
        style_cell={
            "background-color": "lightgrey",
            "border": "1px solid black",
            "color": "black",
            "font_size": "12px",
            "text-align": "left",
            "padding": "8px",
        },
        style_header={
            "background-color": "dodgerblue",
            "font-weight": "bold",
            "color": "white",
            "font-size": "16px",
            "text-align": "center",
            "padding": "10px",
        },
        style_table={
            "border-collapse": "collapse",
            "width": "100%",
            "margin": "0 auto",
        },
        style_data_conditional=[{
            'if': {'row_index': 'odd'},
            'backgroundColor': 'rgba(0, 0, 0, 0.05)',
        }],
    ),
], className="container")
