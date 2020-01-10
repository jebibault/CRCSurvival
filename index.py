from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app, server
from tabs import intro, predict, explain, evaluate

style = {'maxWidth': '960px', 'margin': 'auto'}

app.title = 'Prostate cancer survival prediction with AI'

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

app.layout = html.Div([
    html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/logo.png?raw=true',
             style={
                 "width": "100%",
                 "margin-bottom": "25px"
             }
            ),
    dcc.Markdown("# Predict prostate cancer survival with AI"),
    dcc.Markdown("""This model allows you to predict 10-year overall survival in patients with prostate cancer."""),
    dcc.Tabs(id='tabs', value='tab-intro', children=[
        dcc.Tab(label='Introduction', value='tab-intro', style='tab_style', selected_style='tab_selected_style'),
        dcc.Tab(label='Methods', value='tab-explain', style='tab_style', selected_style='tab_selected_style'),
        dcc.Tab(label='Performances', value='tab-evaluate', style='tab_style', selected_style='tab_selected_style'),
        dcc.Tab(label='Predict', value='tab-predict', style='tab_style', selected_style='tab_selected_style')
    ]),
    html.Div(id='tabs-content-inline'),
], 
    #style=style
)

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-intro': return intro.layout
    elif tab == 'tab-predict': return predict.layout
    elif tab == 'tab-explain': return explain.layout
    elif tab == 'tab-evaluate': return evaluate.layout

if __name__ == '__main__':
    app.run_server(debug=True)
