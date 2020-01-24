from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app, server
from tabs import intro, predictOS, predictCSS

style = {
    'maxWidth': '900px', 
    'margin': 'auto'}

app.title = 'Prostate cancer survival prediction with AI'

app.layout = html.Div([
    html.A([html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/logo.png?raw=true', style={'width' : '100%', 'margin-bottom': '15px', 'margin-top': '25px'})], href='http://med.stanford.edu/xinglab.html', target='_blank'),
    dcc.Markdown("## Predict prostate cancer survival with AI"),
    html.P([
	    'This model allows you to predict 10-year cancer-specific and overall survival in patients with prostate cancer.', 
	    html.Br(),
	    html.Br(),
	    html.Br()]),
    dcc.Tabs(id='tabs', value='tab-intro', parent_className='custom-tabs', className='custom-tabs-container', children=[
        dcc.Tab(label='About', value='tab-intro', className='custom-tab', selected_className='custom-tab--selected'),
        dcc.Tab(label='Predict cancer-specific survival', value='tab-predictCSS', className='custom-tab', selected_className='custom-tab--selected'),
        dcc.Tab(label='Predict overall survival', value='tab-predictOS', className='custom-tab', selected_className='custom-tab--selected')
    ]),
    html.Div(id='tabs-content-classes'),
], style=style)

@app.callback(Output('tabs-content-classes', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-intro': return intro.layout
    elif tab == 'tab-predictOS': return predictOS.layout
    elif tab == 'tab-predictCSS': return predictCSS.layout

if __name__ == '__main__':
    app.run_server(debug=True)
