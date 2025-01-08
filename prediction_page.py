import dash
from dash import html, dcc, Input, Output, State
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE  # type: ignore

# Register page
dash.register_page(__name__, path='/prediction_page', name="Prediction")

# Load and preprocess the dataset
data = pd.read_csv("H:/Zunaira/Machine Learning/Data Preprocessing/Heart Disease Prediction/SVM/Heart Disease Dataset.csv")
data.fillna(data.mean(), inplace=True)
data['num'] = data['num'].apply(lambda x: 1 if x > 0 else 0)

# Prepare input and output data
x = data[['Age', 'Sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
          'exang', 'oldpeak', 'slope', 'ca', 'thal']]
y = data['num']

# Handle imbalanced data using SMOTE
smote = SMOTE(random_state=42)
x_resampled, y_resampled = smote.fit_resample(x, y)

# Normalize the data
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x_resampled)

# Split the scaled features into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x_scaled, y_resampled, test_size=0.2, random_state=42)

# Train the KNN model
model = KNeighborsClassifier(n_neighbors=5, weights='distance', algorithm='auto')  # Use optimized parameters
model.fit(x_train, y_train)

layout = html.Div([
    # Title Section
    html.H1("Heart Disease Prediction Using KNN", style={
        'textAlign': 'center',
        'backgroundColor': 'navy',
        'color': 'white',
        'padding': '10px',
        'fontFamily': 'Cambria'
    }),

    # Main Container for Center Alignment
    html.Div([
        # Row Container with Flex for Horizontal Alignment
        html.Div([
            # Box 1: Description of the Model
            html.Div([
                html.H3("About the Model", style={'fontFamily': 'Cambria', 'fontSize': '20px', 'textAlign': 'center'}),
                html.P("This model predicts the likelihood of a person having heart disease based on several health parameters. "
                        "Enter the details in the form to make a prediction.",
                        style={'fontFamily': 'Cambria', 'textAlign': 'center'}),
            ], className="col-12", style={
                "padding": "10px", "backgroundColor": "#f4f4f4", "borderRadius": "5px", "margin": "10px", 'textAlign': 'center'}),

            # Box 2: Form Inputs for Prediction
            html.Div([
                html.H3("Enter Patient Data", style={'fontFamily': 'Cambria', 'fontSize': '20px', 'textAlign': 'center', "color": "white", "backgroundColor": "navy"}),

                # Age and Sex
                html.Div([
                    html.Div([html.Label("Age", style={'textAlign': 'center'})], style={'flex': '1', 'padding': '10px'}),
                    html.Div([html.Label("Sex (1 = Male, 0 = Female)", style={'textAlign': 'center'})], style={'flex': '1', 'padding': '10px'})
                ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '10px'}),

                html.Div([
                    html.Div([dcc.Input(id="age", type="number", placeholder="Enter Age", required=True)], style={'flex': '1', 'padding': '10px'}),
                    html.Div([dcc.Input(id="sex", type="number", placeholder="Enter Sex", required=True)], style={'flex': '1', 'padding': '10px'})
                ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '10px'}),

                # Chest Pain and Resting Blood Pressure
                html.Div([
                    html.Div([html.Label("Chest Pain Type (cp)", style={'textAlign': 'center'})], style={'flex': '1', 'padding': '10px'}),
                    html.Div([html.Label("Resting Blood Pressure (trestbps)", style={'textAlign': 'center'})], style={'flex': '1', 'padding': '10px'})
                ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '10px'}),

                html.Div([
                    html.Div([dcc.Input(id="cp", type="number", placeholder="Enter CP", required=True)], style={'flex': '1', 'padding': '10px'}),
                    html.Div([dcc.Input(id="trestbps", type="number", placeholder="Enter resting bp", required=True)], style={'flex': '1', 'padding': '10px'})
                ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '10px'}),

                # Serum Cholesterol and Fasting Blood Sugar
                html.Div([
                    html.Div([html.Label("Serum Cholesterol (chol)", style={'textAlign': 'center'})], style={'flex': '1', 'padding': '10px'}),
                    html.Div([html.Label("Fasting Blood Sugar > 120 mg/dl (fbs, 1=True, 0=False)", style={'textAlign': 'center'})], style={'flex': '1', 'padding': '10px'})
                ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '10px'}),

                html.Div([
                    html.Div([dcc.Input(id="chol", type="number", placeholder="Enter chol", required=True)], style={'flex': '1', 'padding': '10px'}),
                    html.Div([dcc.Input(id="fbs", type="number", placeholder="Enter fbs", required=True)], style={'flex': '1', 'padding': '10px'})
                ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '10px'}),

                # Resting ECG and Maximum Heart Rate Achieved
                html.Div([
                    html.Div([html.Label("Resting ECG (restecg)", style={'textAlign': 'center'})], style={'flex': '1', 'padding': '10px'}),
                    html.Div([html.Label("Maximum Heart Rate Achieved (thalach)", style={'textAlign': 'center'})], style={'flex': '1', 'padding': '10px'})
                ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '10px'}),

                html.Div([
                    html.Div([dcc.Input(id="restecg", type="number", placeholder="Enter restecg", required=True)], style={'flex': '1', 'padding': '10px'}),
                    html.Div([dcc.Input(id="thalach", type="number", placeholder="Enter thalach", required=True)], style={'flex': '1', 'padding': '10px'})
                ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '10px'}),

                # Exercise-Induced Angina and ST Depression Induced by Exercise
                html.Div([
                    html.Div([html.Label("Exercise-Induced Angina (exang, 1=Yes, 0=No)", style={'textAlign': 'center'})], style={'flex': '1', 'padding': '10px'}),
                    html.Div([html.Label("ST Depression Induced by Exercise (oldpeak)", style={'textAlign': 'center'})], style={'flex': '1', 'padding': '10px'})
                ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '10px'}),

                html.Div([
                    html.Div([dcc.Input(id="exang", type="number", placeholder="Enter exang", required=True)], style={'flex': '1', 'padding': '10px'}),
                    html.Div([dcc.Input(id="oldpeak", type="number", placeholder="Enter oldpeak", required=True)], style={'flex': '1', 'padding': '10px'})
                ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '10px'}),

                # Slope of the Peak Exercise ST Segment and Number of Major Vessels
                html.Div([
                    html.Div([html.Label("Slope of the Peak Exercise ST Segment (slope)", style={'textAlign': 'center'})], style={'flex': '1', 'padding': '10px'}),
                    html.Div([html.Label("Number of Major Vessels (ca)", style={'textAlign': 'center'})], style={'flex': '1', 'padding': '10px'})
                ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '10px'}),

                html.Div([
                    html.Div([dcc.Input(id="slope", type="number", placeholder="Enter slope", required=True)], style={'flex': '1', 'padding': '10px'}),
                    html.Div([dcc.Input(id="ca", type="number", placeholder="Enter ca", required=True)], style={'flex': '1', 'padding': '10px'})
                ], style={'display': 'flex', 'justifyContent': 'space-between', 'marginBottom': '10px'}),

                # Thalassemia (thal)
                html.Div([
                    html.Label("Thalassemia (thal, 0=Normal, 1=Fixed, 2=Reversible)", style={'textAlign': 'center'})
                ], style={'flex': '1', 'padding': '10px'}),
                html.Div([
                    dcc.Input(id="thal", type="number", placeholder="Enter thal", required=True),
                ], style={'flex': '1', 'padding': '10px'}),


                html.Br(),
                html.Button("Predict", id="predict-button", n_clicks=0),
            ], className="col-12", style={
                "padding": "10px", "backgroundColor": "#f4f4f4", "borderRadius": "5px", "margin": "10px", 'textAlign': 'center'
            }),

        ], style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center'}),  # Vertical alignment for the entire section

       # Prediction Output Section
html.Div([
    html.H3("Prediction Result", style={'fontFamily': 'Cambria', 'fontSize': '20px', 'textAlign': 'center'}),
    html.Div(id="prediction-output", style={
        'marginTop': '20px', 
        'fontSize': '20px', 
        'textAlign': 'center', 
        'padding': '10px', 
        'backgroundColor': '#fce4ec',  # Light pink color
        'borderRadius': '5px'
    })
], style={
    "marginTop": "30px",
    "backgroundColor": "#fce4ec",  # Light pink background for the entire section
    "padding": "20px",  # Optional, for better spacing
    "borderRadius": "5px"  # Optional, to add rounded corners to the whole section
}),
    ]),  # Closing the main container
])  # Closing the layout

# Callback for prediction
@dash.callback(
    Output("prediction-output", "children"),
    [Input("predict-button", "n_clicks")],
    [
        State("age", "value"), State("sex", "value"), State("cp", "value"),
        State("trestbps", "value"), State("chol", "value"), State("fbs", "value"),
        State("restecg", "value"), State("thalach", "value"), State("exang", "value"),
        State("oldpeak", "value"), State("slope", "value"), State("ca", "value"),
        State("thal", "value")
    ]
)
def predict_heart_disease(n_clicks, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    if n_clicks > 0:  # Only trigger after the button is clicked
        # Ensure all inputs are filled
        if None in [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]:
            return "Please fill all input fields before making a prediction."

        # Prepare input data for prediction
        input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        input_scaled = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(input_scaled)
        result = "Oh no!! You're a heart patient😔 " if prediction[0] == 1 else "Congratulations!! No Heart Disease Detected🤗"

        return result
    return "Awaiting input for prediction."
