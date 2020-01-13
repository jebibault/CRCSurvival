from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [
dcc.Markdown("""
#### What is this model for?"""),
html.P([
	'The management of prostate cancer that is detected on the basis of prostate-specific antigen (PSA) levels remains controversial. In the United States alone, each year, an estimated 180,890 new cases will be diagnosed and 26,120 men will die from the disease. PSA testing has resulted in a significant increase in the diagnosis and treatment of prostate cancer, but many men do not benefit from intervention because the disease is either indolent or disseminated at diagnosis. Prostate cancer often progresses slowly, and many men die of competing causes.', 
	html.Br(),
	html.Br(),
	'In order to assess whether a patient with prostate cancer could actually benefit from cancer treatment, and not die from another cause, we created a model to predict 10-year overall survival. This model was trained on data from the prospective randomized multicenter trial PLCO that assessed the interest of prostate cancer screening with annual PSA testing for 6 years and digital rectal examination for 4 years. In this trial, 76,693 men at 10 U.S. study centers were randomly assigned to receive either annual screening (38,343 subjects) or usual care as the control (38,350 subjects).',
	html.Br(),
	'To build this model we selected the patients that were diagnosed with prostate cancer during follow-up (n=8,776).',
	html.Br(),
	html.Br(),
]),
dcc.Markdown("""
#### Disclaimer:
All information contained on this application is for general informational purposes only and does not constitute medical or other professional advice. It should not be used for medical purpose. The information you find on this application is provided as is and to the extent permitted by law, the creators disclaim all other warranties of any kind, whether express, implied, statutory or otherwise. In no event will the authors or its affiliates be liable for any damages whatsoever, including without limitation, direct, indirect, incidental, special, exemplary, punitive or consequential damages, arising out of the use, inability to use or the results of use of this application, any websites linked to this application or the materials or information or services contained at any or all such websites, whether based on warranty, contract, tort or any other legal theory and whether or not advised of the possibility of such damages. If your use of the materials, information or services from this application or any website linked to this application results in the need for servicing, repair or correction of equipment or data, you assume all costs thereof.'""")
]




