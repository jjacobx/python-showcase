from dash import dcc
from dash import html
from dash.dependencies import Input, Output

from app import app

import pandas as pd
import plotly.graph_objs as go

# For now copy example code from 
# https://www.datacamp.com/community/tutorials/learn-build-dash-python

df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/' +
    '5d1ea79569ed194d432e56108a04d188/raw/' +
    'a9f9e8076b837d541398e999dcbac2b2826a81f8/'+
    'gdp-life-exp-2007.csv')

colors = {
    'background': '#FFFFF0', # ivory
    'text': '#80461B',       # russet
    'line': '#00A86B'        # jade
}

markdown_text = '''
### Markdown with R vectors

These are some vector: 

```
a <- 1:3
b <- 4:6
```

'''

layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(
        children='Hello Dash with a twist',
        style={
            'textAlign': 'center',
            'color': colors['text']
        }
    ),
    html.Div(children='Dash: A pretty visualisation tool for virtual CVs.', style={
        'textAlign': 'center',
        'color': colors['text']
    }),
    dcc.Markdown(children=markdown_text), 
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x=df[df['continent'] == i]['gdp per capita'],
                    y=df[df['continent'] == i]['life expectancy'],
                    text=df[df['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.8,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': colors['line']}
                    },
                    name=i
                ) for i in df.continent.unique()
            ],
            'layout': go.Layout(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    ), 
    dcc.Input(id='my-id', value='Dash App', type='text'),
    html.Div(id='my-div'), 
    dcc.Link('Go to About Me', href='/apps/about-me')
])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered "{}"'.format(input_value)
