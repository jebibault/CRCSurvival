from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Metrics

Evaluating models trained on unbalanced classes can be difficult. We provide several methods to assess the performances 
of the model. All metrics are reported on the test dataset.

Accuracy: 91.19%
f1 Score: 79.10%
Average Precision: 84.88%
Precision: 80.78%
Negative Predictive Value: 91.05%
Recall: 77.50%
False Positive Rate: 8.95%
Specificity: 91.05%
False Negative Rate: 16.97%
False Discovery Rate: 16.97%
AUC: 92.04%
"""),

html.Img(src='https://raw.githubusercontent.com/jebibault/ProstateCancerSurvival/master/figures/10yOSConfusionMatrix.png')]
html.Img(src='https://raw.githubusercontent.com/jebibault/ProstateCancerSurvival/master/figures/10yOSROC.png')]
html.Img(src='https://raw.githubusercontent.com/jebibault/ProstateCancerSurvival/master/figures/10yOS.png')]
