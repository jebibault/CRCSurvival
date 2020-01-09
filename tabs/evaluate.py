from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [
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
dcc.Markdown("""#### Confusion matrix:
	This is a table with two rows and two columns that reports the number of false positives, false negatives, true positives, and true negatives."""),
html.Div([
	html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yOSConfusionMatrix.png?raw=true')],
	style={'text-align':'center'}),
dcc.Markdown("""#### ROC AUC:
	The ROC curve is created by plotting the true positive rate (TPR) against the false positive rate (FPR) at various threshold settings.
	It illustrates the diagnostic ability of the model as its discrimination threshold is varied. The optimal value of the AUC a model is 1. An AUC of 0.5 shows a model has no classifying skill."""),
html.Div([
	html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yOSROC.png?raw=true')],
	style={'text-align':'center'}),
dcc.Markdown("""#### Precision Recall AUC:
	In classification tasks with class imbalance (the two classes we need to predict are not present in the dataset at the same ratio), we need to use specific metrics:
	- Precision is a metric that quantifies the number of correct positive predictions made. 
	- Recall quantifies the number of correct positive predictions made out of all positive predictions that could have been made. 
	A precision-recall curve is a plot of the precision (y-axis) and the recall (x-axis) for different probability thresholds.
	The optimal value of the PR AUC is 1."""),
html.Div([
	html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yOSPrecisionRecall.png?raw=true')],
	style={'text-align':'center'}),
dcc.Markdown("""#### Kaplan-Meier survival curve:
	This curve estimates the survival of the patients included in the study. High-risk patients are patients that the model identifies as having a high risk of dying within 10 years from diagnosis."""),
html.Div([
	html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yOS.png?raw=true')],
	style={'text-align':'center'}),
dcc.Markdown("""#### The 20 most important features predicting survival
	The SHAP values are a way to estimate the contribution of a feature to the prediction performed by the model.
	- Feature importance: Variables are ranked in descending order.
	- Impact: The horizontal location shows whether the effect of that value is associated with a higher or lower prediction.
	- Original value: Color shows whether that variable is high (in red) or low (in blue) for that observation.
	- Correlation: Younger patients (blue dots) at diagnosis have a lower risk of dyng within 10 years (negative SHAP values). """),
html.Div([
	html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yOSTreeExplainer.png?raw=true')],
	style={'text-align':'center'})
]
