from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3('terraNova hackathon'), 
    dcc.Link('Index', href='/index')
])
