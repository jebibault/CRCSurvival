from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app, server
from tabs import intro, predict, explain, evaluate

style = {'maxWidth': '960px', 'margin': 'auto'}

app.title = 'Predict 10-year overall survival in prostate cancer patients'

app.layout = html.Div([
    dcc.Markdown('# Predict 10-year overall survival in prostate cancer'),
    dcc.Tabs(id='tabs', value='tab-intro', children=[
        dcc.Tab(label='Introduction', value='tab-intro'),
        dcc.Tab(label='Creation', value='tab-explain'),
        dcc.Tab(label='Model performances', value='tab-evaluate'),
        dcc.Tab(label='Predict', value='tab-predict')
    ]),
    html.Div(id='tabs-content'),
], style=style)

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-intro': return intro.layout
    elif tab == 'tab-predict': return predict.layout
    elif tab == 'tab-explain': return explain.layout
    elif tab == 'tab-evaluate': return evaluate.layout

if __name__ == '__main__':
    app.run_server(debug=True)
