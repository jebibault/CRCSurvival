from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app, server
from tabs import intro, predict, explain, evaluate

style = {'maxWidth': '960px', 'margin': 'auto'}

app.title = 'Prostate cancer survival prediction with AI'

app.head = [
    html.Link(
        href='https://www.stanford.edu/favicon.ico',
        rel='icon'
    ),
]

app.layout = html.Div([
    html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/logo.png?raw=true',
             style={
                 "width": "100%"
             }
            ),
    dcc.Markdown("# Predict prostate cancer survival with AI"),
    dcc.Markdown("""This model allows you to predict 10-year overall survival in patients with prostate cancer."""),
    dcc.Tabs(id='tabs', value='tab-intro', children=[
        dcc.Tab(label='Introduction', value='tab-intro'),
        dcc.Tab(label='Methods', value='tab-explain'),
        dcc.Tab(label='Performances', value='tab-evaluate'),
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
