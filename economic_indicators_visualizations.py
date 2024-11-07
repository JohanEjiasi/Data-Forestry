import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Load the data from the CSV
file_path = 'C:/Users/Johan/OneDrive/Desktop/Data-Forestry/downloaded_files/Key_Economic_Indicators.csv'
df = pd.read_csv(file_path)

# Data Cleaning: Removing rows with NaN values for relevant columns
df_clean = df.dropna(subset=['Year', 'Unemployment TX', 'Unemployment U.S.'])

# 1. Unemployment Rate (TX vs. U.S.)
fig_unemployment = px.line(
    df_clean, x='Year', y=['Unemployment TX', 'Unemployment U.S.'],
    title='Unemployment Rate: TX vs U.S.',
    labels={'value': 'Unemployment Rate (%)', 'variable': 'Location'},
    markers=True
)

# 2. Consumer Confidence Index Comparison
fig_confidence = px.line(
    df, x='Year', y=['Consumer Confidence Index TX', 'Consumer Confidence Index US'],
    title='Consumer Confidence Index: TX vs U.S.',
    labels={'value': 'Consumer Confidence Index', 'variable': 'Location'},
    markers=True
)

# 3. Nonfarm Employment (TX vs U.S.)
fig_nonfarm_employment = px.line(
    df_clean, x='Year', y=['Nonfarm Employment TX', 'Nonfarm Employment U.S.'],
    title='Nonfarm Employment: TX vs U.S.',
    labels={'value': 'Nonfarm Employment (Thousands)', 'variable': 'Location'},
    markers=True
)

# 4. CPI Comparison (TX vs U.S.)
fig_cpi = px.line(
    df_clean, x='Year', y=['Consumer Price Index TX', 'Consumer Price Index U.S.'],
    title='Consumer Price Index: TX vs U.S.',
    labels={'value': 'Consumer Price Index (CPI)', 'variable': 'Location'},
    markers=True
)

# 5. Retail Gasoline Price in TX
fig_gasoline_price = px.line(
    df, x='Year', y='Retail Gasoline Price TX',
    title='Retail Gasoline Price in TX',
    labels={'Retail Gasoline Price TX': 'Price per Gallon (USD)'}
)

# 6. Retail Diesel Price in TX
fig_diesel_price = px.line(
    df, x='Year', y='Retail Diesel Price TX',
    title='Retail Diesel Price in TX',
    labels={'Retail Diesel Price TX': 'Price per Gallon (USD)'}
)

# 7. Correlation Heatmap: Visualizing correlations between different economic indicators
correlation_matrix = df.corr()
fig_corr = px.imshow(correlation_matrix, text_auto=True, title='Correlation Heatmap of Economic Indicators')

# Layout of the Dash app
app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Economic Indicators Dashboard", className="text-center"), width=12)
        ]),
        
        dbc.Row([
            dbc.Col(dcc.Graph(figure=fig_unemployment), width=6),
            dbc.Col(dcc.Graph(figure=fig_confidence), width=6),
        ]),
        
        dbc.Row([
            dbc.Col(dcc.Graph(figure=fig_nonfarm_employment), width=6),
            dbc.Col(dcc.Graph(figure=fig_cpi), width=6),
        ]),
        
        dbc.Row([
            dbc.Col(dcc.Graph(figure=fig_gasoline_price), width=6),
            dbc.Col(dcc.Graph(figure=fig_diesel_price), width=6),
        ]),
        
        dbc.Row([
            dbc.Col(dcc.Graph(figure=fig_corr), width=12)
        ])
    ])
])

import os

# Run the app on a server for Heroku deployment
if __name__ == '__main__':
    app.run_server(debug=False, host='0.0.0.0', port=int(os.environ.get("PORT", 8050)))