from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H1('Super-resolution of astronomical photos'), 
    html.Div([
        html.Div(
            html.Figure([
                html.P([
                    html.Figcaption("DnCNN results"), 
                    html.Img(src=app.get_asset_url('astro-dncnn.png'))
                ], className='aligncenter')
            ]), 
            className = 'column'
        ), 
        html.Div(
            html.Figure([
                html.P([
                    html.Figcaption("CycleGAN results"), 
                    html.Img(src=app.get_asset_url('astro-cgan.png'))
                ], className='aligncenter')
            ]), 
            className = 'column'
        )
    ], className='row'), 
    html.Br(), 
    dcc.Link('Index', href='/index')
])
