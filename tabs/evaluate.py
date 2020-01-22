from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [
dcc.Markdown("""
	### Metrics
	Evaluating models trained on unbalanced classes (the two classes we need to predict are not present in the dataset at the same ratio) can be difficult. We provide several methods to assess the performances of the model. All metrics are reported on the test dataset.

	|  Metric      |  Result   |  Definition					                                       |
	|--------------|-----------|-----------------------------------------------------------------------|
	| Accuracy     | 87.55%    |  Number of correct predictions / total number of input samples        |
	| Precision    | 66.19%    |  Number of correct positive predictions / number of positive samples  |
	| Recall       | 86.13%    |  Number of correct positive results / number of all positive samples  |
	| ROC AUC      | 94.31%    |  See below                                                            |
	| PR AUC       | 87.73%    |  See below                                                            |

	"""),
dcc.Markdown("""
	#### Confusion matrix
	This is a table with two rows and two columns that reports the number of false positives, false negatives, true positives, and true negatives.
	"""),
html.Div([
	html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yOSConfusionMatrix.png?raw=true')], style={'text-align' : 'center'}),
dcc.Markdown("""
	#### ROC AUC
	The ROC curve is created by plotting the true positive rate (y-axis) and the false positive rate (x-axis) at various threshold settings.
	It illustrates the diagnostic ability of the model as its discrimination threshold is varied. The optimal value of the AUC is 1.
	"""),
html.Div([
	html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yOSROC.png?raw=true')], style={'text-align' : 'center'}),
dcc.Markdown("""
	#### Precision Recall AUC
	A precision-recall curve is a plot of the precision (y-axis) and the recall (x-axis) for different probability thresholds.
	The optimal value of the PR AUC is 1.
	"""),
html.Div([
	html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yOSPrecisionRecall.png?raw=true')], style={'text-align' : 'center'}),
dcc.Markdown("""
	#### Kaplan-Meier survival curve
	This curve estimates the survival of the patients included in the study. High-risk patients are patients that the model identifies as having a high risk of dying within 10 years from diagnosis.
	"""),
html.Div([
	html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yOS.png?raw=true')], style={'text-align' : 'center'}),
dcc.Markdown("""
	#### The 20 most important features predicting survival
	The SHAP value is a way to estimate the contribution of a feature to the prediction performed by the model.
	- Feature importance: Variables are ranked in descending order.
	- Impact: The horizontal location shows whether the feature is associated with a higher or lower risk of dying.
	- Original value: Color shows whether that variable is high (in red) or low (in blue) for that observation.
	- Correlation: As an example, in this model younger patients (blue dots) at diagnosis have a lower risk of dying within 10 years (negative SHAP values).
	"""),
html.Div([
	html.Img(src='https://github.com/jebibault/ProstateCancerSurvival/blob/master/figures/10yOSTreeExplainer.png?raw=true')], style={'text-align' : 'center'})
]
