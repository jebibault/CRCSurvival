from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = html.Div([
	dcc.Markdown("""
		### Metrics
		Evaluating models trained on unbalanced classes can be difficult. We provide several methods to assess the performances 
		of the model. All metrics are reported on the test dataset.

		|  Metric      |  Result   |
		|--------------|-----------|
		| Accuracy     |  91.9%    |
		| Precision    | 80.78%    |
		| Recall       | 77.5%     |
		| ROC AUC      | 92.04%    |
		| PR AUC       | 84.88%    |

	"""),
	dcc.Markdown("""Confusion matrix:"""),
	html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yOSConfusionMatrix.png?raw=true'),
	html.Div(html.P([html.Br()])),
	html.Div(html.P([html.Br()])),
	dcc.Markdown("""ROC AUC:"""),
	html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yOSROC.png?raw=true'),
	html.Div(html.P([html.Br()])),
	html.Div(html.P([html.Br()])),
	dcc.Markdown("""Precision Recall AUC:"""),
	html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yOSPR.png?raw=true'),
	html.Div(html.P([html.Br()])),
	html.Div(html.P([html.Br()])),
	dcc.Markdown("""Kaplan-Meier overall survival curves:"""),
	html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yOS.png?raw=true')],
	html.Div(html.P([html.Br()])),
	html.Div(html.P([html.Br()])),
	dcc.Markdown("""The 20 most important features predicting survival (according to SHAP values:"""),
	html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yTreeExplainer.png?raw=true')],
	style={'text-align':'center'})
