from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H1('terra_Nova Hackathon'), 
    html.Img(src=app.get_asset_url('australia.gif')), 
    html.Br(), 
    dcc.Link('Index', href='/index')
])
