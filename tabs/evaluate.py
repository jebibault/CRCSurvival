from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = html.Div([
	html.P('Confusion matrix:'),
	html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yOSConfusionMatrix.png?raw=true'),
	html.P(html.Br(), html.Br(), 'ROC AUC:'),
	html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yOSROC.png?raw=true'),
	html.P(html.Br(), html.Br(), 'Precision Recall AUC:'),
	html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yOSPR.png?raw=true'),
	html.P(html.Br(), html.Br(), 'Kaplan-Meier overall survival curves:'),
	html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yOS.png?raw=true'),
	html.P(html.Br(), html.Br(), 'The 20 most important features predicting survival (according to SHAP values:)'),
	html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yTreeExplainer.png?raw=true')
])
