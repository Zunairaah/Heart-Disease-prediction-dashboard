import pandas as pd
import dash
from dash import html, dcc, callback
import plotly.express as px
from dash.dependencies import Input, Output

# Register the subpage
dash.register_page(__name__, path='/categorical', name="Categorical 📊")

# Load the dataset
data_path = 'H:/Zunaira/Machine Learning/Data Preprocessing/Heart Disease Prediction/Heart Disease Dataset.csv'
data = pd.read_csv(data_path)  

# Categorical columns in one variable
categorical_columns = ["Sex", "cp", "fbs", "restecg", "exang", "slope", "ca", "thal", "num"]

# Dropdown options for categorical columns
dd_categorical = dcc.Dropdown(
    id="cat_column",
    options=[{"label": col, "value": col} for col in categorical_columns],
    value="Sex",  # Default value
    clearable=False,
    className="mb-3"
)

# Dropdown options for plot types
plot_type_dd = dcc.Dropdown(
    id="plot_type",
    options=[
        {"label": "Bar Graph", "value": "bar"},
        {"label": "Pie Chart", "value": "pie"},
        {"label": "Violin Plot", "value": "violin"},
    ],
    value="bar",  # Default plot type
    clearable=False,
    className="mb-3"
)

# Function to create bar graph
def create_bar_graph(col_name="Sex"):
    return px.bar(
        data_frame=data,
        x=col_name,
        title=f"Bar Graph of {col_name}",
        height=600,
        labels={col_name: col_name},
        template="seaborn"
    )

# Function to create pie chart
def create_pie_chart(col_name="Sex"):
    return px.pie(
        data_frame=data,
        names=col_name,
        title=f"Pie Chart of {col_name}",
        height=600,
        labels={col_name: col_name},
        template="seaborn"
    )

# Function to create violin plot
def create_violin_plot(col_name="Sex"):
    return px.violin(
        data_frame=data,
        y=col_name,
        title=f"Violin Plot of {col_name}",
        height=600,
        labels={col_name: col_name},
        template="seaborn"
    )

# Page Layout
layout = html.Div(
    children=[
        html.Br(),
        html.H3("Select a Categorical Column for Visualization", className="text-center text-primary mb-4"),
        html.P("Choose a column to visualize its distribution:", className="fw-bold"),
        dd_categorical,
        html.P("Choose a plot type:", className="fw-bold"),
        plot_type_dd,
        # Placeholder for graphs
        dcc.Graph(id="cat-plot-graph"),
    ]
)

# Callback to update the plot based on selected column and plot type
@callback(
    Output("cat-plot-graph", "figure"),
    [Input("cat_column", "value"),
     Input("plot_type", "value")]
)
def update_categorical_plot(cat_column, plot_type):
    print(f"Selected Column: {cat_column}, Plot Type: {plot_type}")  # Debugging line
    if plot_type == "bar":
        return create_bar_graph(cat_column)
    elif plot_type == "pie":
        return create_pie_chart(cat_column)
    elif plot_type == "violin":
        return create_violin_plot(cat_column)


# Run the app
if __name__ == '__main__':
    dash.Dash(__name__).run_server(debug=True)
