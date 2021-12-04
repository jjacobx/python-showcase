from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app
from apps import test, about_me, forecasting, nialm, super_resolution, terra_nova


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

index_page = html.Div([
    dcc.Link('About Me', href='/apps/about-me'), html.Br(), 
    dcc.Link('Forecasting', href='/apps/forecasting'), html.Br(), 
    dcc.Link('NIALM', href='/apps/nialm'), html.Br(), 
    dcc.Link('Super-resolution', href='/apps/super-resolution'), html.Br(), 
    dcc.Link('terraNova', href='/apps/terra-nova'), html.Br(), 
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
