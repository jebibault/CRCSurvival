from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app, server
from tabs import intro, predict, explain, evaluate

style = {
    'maxWidth': '800px', 
    'margin': 'auto'}

app.title = 'Prostate cancer survival prediction with AI'

app.layout = html.Div([
    html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/logo.png?raw=true',style={"width": "100%","margin-bottom": "25px"}),
    dcc.Markdown("## Predict prostate cancer survival with AI"),
    html.P([
	    'This model allows you to predict 10-year overall survival in patients with prostate cancer.', 
	    html.Br(),
	    html.Br(),
	    html.Br()]),
    #dcc.Markdown("""This model allows you to predict 10-year overall survival in patients with prostate cancer."""),
    dcc.Tabs(id='tabs', value='tab-intro', parent_className='custom-tabs', className='custom-tabs-container', children=[
        dcc.Tab(label='Introduction', value='tab-intro', className='custom-tab', selected_className='custom-tab--selected'),
        dcc.Tab(label='Methods', value='tab-explain', className='custom-tab', selected_className='custom-tab--selected'),
        dcc.Tab(label='Performances', value='tab-evaluate', className='custom-tab', selected_className='custom-tab--selected'),
        dcc.Tab(label='Predict survival', value='tab-predict', className='custom-tab', selected_className='custom-tab--selected')
    ]),
    html.Div(id='tabs-content-classes'),
], style=style)

@app.callback(Output('tabs-content-classes', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-intro': return intro.layout
    elif tab == 'tab-predict': return predict.layout
    elif tab == 'tab-explain': return explain.layout
    elif tab == 'tab-evaluate': return evaluate.layout

if __name__ == '__main__':
    app.run_server(debug=True)
