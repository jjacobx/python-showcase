from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3('About Me'),
    dcc.Dropdown(
        id='about-me-dropdown',
        options=[
            {'label': 'My name - {}'.format(i), 'value': i} for i in [
                'Jakub', 'Jaka', 'Kuba'
            ]
        ]
    ),
    html.Div(id='about-me-display-value'),
    dcc.Link('Go to Test', href='/apps/test')
])


@app.callback(
    Output('about-me-display-value', 'children'),
    Input('about-me-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)