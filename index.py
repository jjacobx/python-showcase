from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app
from apps import test, about_me, forecasting, nialm, super_resolution, terra_nova


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

# Menu
index_page = html.Div([
    dcc.Link('About Me', href='/apps/about-me'), 
    html.Br(), 
    dcc.Link(
        html.Img(src=app.get_asset_url('forecasting.png')), 
        href='/apps/forecasting'
    ), 
    dcc.Link(
        html.Img(src=app.get_asset_url('nialm.png')), 
        href='/apps/nialm', 
        style={"margin-left": "15px"}
    ), 
    dcc.Link(
        html.Img(src=app.get_asset_url('super_resolution.png')), 
        href='/apps/super-resolution', 
        style={"margin-left": "15px"}
    ), 
    dcc.Link(
        html.Img(src=app.get_asset_url('terra_nova.png')), 
        href='/apps/terra-nova', 
        style={"margin-left": "15px"}
    ), 
    html.Br(), 
    dcc.Link('Test', href='/apps/test')
])

# List of URLs
@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/index':
        return index_page
    elif pathname == '/apps/about-me':
        return about_me.layout
    elif pathname == '/apps/forecasting':
        return forecasting.layout
    elif pathname == '/apps/nialm':
        return nialm.layout
    elif pathname == '/apps/super-resolution':
        return super_resolution.layout
    elif pathname == '/apps/terra-nova':
        return terra_nova.layout
    elif pathname == '/apps/test':
        return test.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)
