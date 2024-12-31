import dash
from dash import html, dcc, callback
import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output

# Register the subpage
dash.register_page(__name__, path='/numerical', name="Numerical 📊")

# Load the dataset
data_path = 'H:\Zunaira\Machine Learning\Data Preprocessing\Heart Disease Prediction\Heart Disease Dataset.csv'
data = pd.read_csv(data_path)  # Ensure the dataset is loaded properly

# numerical columns
numerical_columns = ["Age", "trestbps", "chol", "thalach", "oldpeak"]

# Dropdown options for numerical columns
dd = dcc.Dropdown(
    id="dist_column",
    options=[{"label": col, "value": col} for col in numerical_columns],
    value="Age",  # Default value
    clearable=False,
    className="mb-3"
)

# Dropdown options for plot types
plot_type_dd = dcc.Dropdown(
    id="plot_type",
    options=[
        {"label": "Histogram", "value": "histogram"},
        {"label": "Line Plot", "value": "line"},
        {"label": "KDE Plot", "value": "kde"},
        {"label": "Box Plot", "value": "box"},
        {"label": "Area Plot", "value": "area"}  # Added Area Plot option
    ],
    value="histogram",  # Default plot type
    clearable=False,
    className="mb-3"
)

# Function to create histogram
def create_histogram(col_name="Age"):
    return px.histogram(
        data_frame=data,
        x=col_name,
        title=f"Histogram of {col_name}",
        height=600,
        labels={col_name: col_name},
        template="plotly_dark"
    )

# Function to create line plot
def create_line_plot(col_name="Age"):
    return px.line(
        data_frame=data,
        x=data.index,  # Use the index for the x-axis
        y=col_name,
        title=f"Line Plot of {col_name}",
        height=600,
        labels={col_name: col_name},
        template="plotly_dark"
    )

# Function to create KDE plot
def create_kde_plot(col_name="Age"):
    return px.density_contour(
        data_frame=data,
        x=col_name,
        title=f"KDE Plot of {col_name}",
        height=600,
        labels={col_name: col_name},
        template="plotly_dark"
    )

# Function to create box plot
def create_box_plot(col_name="Age"):
    return px.box(
        data_frame=data,
        y=col_name,
        title=f"Box Plot of {col_name}",
        height=600,
        labels={col_name: col_name},
        template="plotly_dark"
    )

# Function to create area plot
def create_area_plot(col_name="Age"):
    return px.area(
        data_frame=data,
        x=data.index,  # Use the index for the x-axis
        y=col_name,
        title=f"Area Plot of {col_name}",
        height=600,
        labels={col_name: col_name},
        template="plotly_dark"
    )


# Page Layout
layout = html.Div(
    children=[
        html.Br(),
        html.H3("Select a Numerical Column for Visualization", className="text-center text-primary mb-4"),
        html.P("Choose a column to visualize its distribution:", className="fw-bold"),
        dd,
        html.P("Choose a plot type:", className="fw-bold"),
        plot_type_dd,
        
        # Debug output displayed on the page
        html.Div(id="debug-output", style={"color": "red", "font-weight": "bold"}),

        # Placeholder for graphs
        dcc.Graph(id="plot-graph"),
    ],
    className="container py-4"
)

# Callback to update the plot based on selected column and plot type
@callback(
    Output("plot-graph", "figure"),
    [Input("dist_column", "value"),
     Input("plot_type", "value")]
)
def update_plot(dist_column, plot_type):
    if plot_type == "histogram":
        return create_histogram(dist_column)
    elif plot_type == "line":
        return create_line_plot(dist_column)
    elif plot_type == "kde":
        return create_kde_plot(dist_column)
    elif plot_type == "box":
        return create_box_plot(dist_column)
    elif plot_type == "area":
        return create_area_plot(dist_column)  
