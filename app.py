import dash
from dash import html, dcc
import plotly.express as px

# Set Plotly template
px.defaults.template = "plotly-dark"

# External CSS for Bootstrap and custom styling
external_css = [
    "https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css",
]

# Initialize Dash app
app = dash.Dash(__name__, use_pages=True, external_stylesheets=external_css)
server = app.server

# Main layout with dcc.Location and page container
app.layout = html.Div([ 
    dcc.Location(id='url', refresh=False),  # Set up location component for handling paths

    # Header section with custom background and title
    html.Div(
        [
            html.H1(
                'Heart Disease Prediction Dashboard',
                className="text-white text-center fw-bold",
                style={'backgroundColor': '#000000', 'padding': '10px', 'borderRadius': '10px', 'fontSize': '2rem', 'fontFamily': 'Cambria'}
            ),
            html.P(
                'Predict and analyze the risk of heart disease based on various features',
                className="text-light text-center fs-5",
                style={'fontSize': '1.2rem', 'backgroundColor': '#000000', 'fontFamily': 'Cambria'}
            ),
        ],
        style={'backgroundColor': '#000000', 'borderRadius': '5px', 'marginBottom': '5px', 'width': '100%', 'padding': '0', 'margin': '0', 'fontFamily': 'Cambria'}
    ),

    # Navigation links with hover effect and custom button styling
    html.Div([  
        dcc.Link("Home", href="/", className="btn btn-dark m-2 fs-5", style={'fontFamily': 'Cambria'}),  # Home page
        dcc.Link("Dataset", href="/dataset", className="btn btn-dark m-2 fs-5", style={'fontFamily': 'Cambria'}),
        dcc.Link("Categorical", href="/categorical", className="btn btn-dark m-2 fs-5", style={'fontFamily': 'Cambria'}),
        dcc.Link("Numerical", href="/numerical", className="btn btn-dark m-2 fs-5", style={'fontFamily': 'Cambria'}),
        dcc.Link("Prediction", href="/prediction_page", className="btn btn-dark m-2 fs-5", style={'fontFamily': 'Cambria'}),  
    ], className="text-center", style={'padding': '0', 'margin': '0'}),

    html.Br(),

    # Dash page container for rendering pages
    html.Div(
        dash.page_container,  # Placeholder for the pages
        className="col-12 mx-auto",
        style={'padding': '0', 'margin': '0', 'fontFamily': 'Cambria'}
    )
], style={'padding': '0', 'margin': '0', 'width': '100%', 'fontFamily': 'Cambria'})

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True, port=8051)
