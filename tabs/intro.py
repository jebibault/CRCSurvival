from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [
html.P([html.Br()]),
html.P([html.Br()]),
dcc.Markdown("""
#### What is this model for?"""),
html.P([
	'Colorectal cancer (CRC) is the third most commonly diagnosed cancer in males and the second in females, with 1.8 million new cases and almost 861,000 deaths in 2018 according to the World Health Organization GLOBOCAN database. In the US alone, approximately 147,950 new cases of large bowel cancer are diagnosed annually and 53,200 Americans die of CRC, accounting for 8 percent of all cancer deaths.', 
	html.Br(),
	html.Br(),
	'In order to be able to better personalize treatment strategies, we created an interpretable AI model to predict 10-year cancer-specific survival of patients with CRC.',
	html.Br(),
	html.Br(),
]),
dcc.Markdown("""
#### The PLCO Trial"""),
html.P([
	'From 1993 through 2001, 154,900 men and women 55 to 74 years of age were randomized either to screening with flexible sigmoidoscopy, with a repeat screening at 3 or 5 years, or to usual care. Significant reductions were observed in the incidence of both distal colorectal cancer (479 cases in the intervention group vs. 669 cases in the usual-care group; relative risk, 0.71; 95% CI, 0.64 to 0.80; P<0.001) and proximal colorectal cancer (512 cases vs. 595 cases; relative risk, 0.86; 95% CI, 0.76 to 0.97; P=0.01).', 
	html.Br(),
	html.Br(),
	'There were also fewer death in the screening arm of the trial: 2.9 deaths from colorectal cancer per 10,000 person-years in the intervention group (252 deaths), as compared with 3.9 per 10,000 person-years in the usual-care group (341 deaths), which represents a 26% reduction (relative risk, 0.74; 95% CI, 0.63 to 0.87; P<0.001).',
	html.Br(),
	html.Br(),
	'Results of the trial were published in 2012:',
	html.Br(),
	html.A("Schoen RE et al., New England Journal of Medicine, 2012", href='https://www.ncbi.nlm.nih.gov/pubmed/22612596', target="_blank", style={'font-weight': 'bold', 'color': '#820000', 'text-decoration': 'none'}),
	html.Br(),
	html.Br(),
]),
	dcc.Markdown("""
	#### Data
	The data were obtained from the National Cancer Institute Cancer Data Access System:"""),
	html.A("National Cancer Institute Cancer Data Access System", href='https://cdas.cancer.gov/plco/', target="_blank", style={'font-weight': 'bold', 'color': '#820000', 'text-decoration': 'none'}),
	html.Br(),
	html.Br(),
	dcc.Markdown("""
	#### Model creation
	To build this model we selected the patients that were diagnosed with CRC cancer during follow-up (n=2,359). 
	The dataset was split into a training (n=1,887) and a testing (n=472) dataset.
	XGBoost was used to predict 10-year cancer-specific. Hyperparameters were tuned with Bayesian Optimization	in a nested cross-validation manner. Performances were evaluated on the test dataset with the bootstrap procedure."""),
	html.Br(),
	dcc.Markdown("""
	#### Model metrics: Cancer-specific survival (CSS)
	Evaluating models trained on unbalanced classes (the two classes we need to predict are not present in the dataset at the same ratio) can be difficult. We provide several methods to assess the performances of the model. All metrics are reported on the test dataset.

	|  Metric      |  Definition				 	                                                           |     CSS      |
	|--------------|-------------------------------------------------------------------------------------------|--------------|
	| Accuracy     |  Number of correct predictions / total number of input samples                            | 0.80 (±0.04) |
	| Precision    |  Number of correct positive predictions / number of positive predictions                  | 0.62 (±0.05) |
	| Recall       |  Number of correct positive predictions / number of all positive samples                  | 0.87 (±0.07) |
	| f1-score     |  Harmonic mean of the precision and the recall                                            | 0.72 (±0.07) |
	| ROC AUC      |  Area under the curve of true positive rate and false positive rate at various thresholds | 0.82 (±0.04) |
	| PR AUC       |  Area under the curve of precision and recall at various thresholds                       | 0.59 (±0.08) |
	"""),
	html.Br(),
	html.Br(),
dcc.Markdown("""
### Disclaimer:
This application does not store any of the data provided for the predictions.
All information contained on this application is for general informational purposes only and does not constitute medical or other professional advice. It should not be used for medical purpose. The information you find on this application is provided as is and to the extent permitted by law, the creators disclaim all other warranties of any kind, whether express, implied, statutory or otherwise. In no event will the authors or its affiliates be liable for any damages whatsoever, including without limitation, direct, indirect, incidental, special, exemplary, punitive or consequential damages, arising out of the use, inability to use or the results of use of this application, any websites linked to this application or the materials or information or services contained at any or all such websites, whether based on warranty, contract, tort or any other legal theory and whether or not advised of the possibility of such damages. If your use of the materials, information or services from this application or any website linked to this application results in the need for servicing, repair or correction of equipment or data, you assume all costs thereof.""")
]