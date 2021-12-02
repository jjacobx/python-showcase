from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app
from apps import test, about_me


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

index_page = html.Div([
    dcc.Link('Go to Test', href='/apps/test'),
    html.Br(),
    dcc.Link('Go to About Me', href='/about-me'),
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/index':
        return index_page
    elif pathname == '/apps/test':
        return test.layout
    elif pathname == '/apps/about-me':
        return about_me.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)