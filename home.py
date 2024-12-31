import dash
from dash import html

# Register the home page
dash.register_page(__name__, path='/', name="Home 🏠")

# Layout for the home page
layout = html.Div(
    children=[
        html.H1("Heart Disease Prediction Dashboard", style={"text-align": "center"}),
        html.P(
            "Welcome to the Heart Disease Prediction Dashboard. This application allows you to explore relationships "
            "between different features in the dataset and visualize data using interactive charts.",
            style={"text-align": "center", "margin-top": "20px", "font-size": "18px"}
        ),
        html.Div(
            children=[
                html.H2("Available Features", style={"margin-top": "40px", "text-align": "center"}),
                html.Ul(
                    children=[
                        html.Li("📈 Explore relationships between dataset features."),
                        html.Li("🔥 Visualize trends using scatter charts, heatmaps, and bubble charts."),
                        html.Li("🔍 Interactive dropdowns to customize graphs."),
                        html.Li("🎯 Gain insights into heart disease predictors.")
                    ],
                    style={"list-style-type": "square", "font-size": "16px", "margin-left": "20px"}
                )
            ]
        )  
    ]
)  # Closing parenthesis for the main layout

