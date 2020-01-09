from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [
	dcc.Markdown("""#### Confusion matrix:"""),
	html.Div([
		html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yOSConfusionMatrix.png?raw=true')],
		style={'text-align':'center'}
	)
]
