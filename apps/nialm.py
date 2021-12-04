from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H3('Nonintrusive Appliance Load Monitoring'), 
    dcc.Link('Index', href='/index')
])
