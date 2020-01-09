from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [
  html.Div(html.P([html.Br()])),
	html.Div(html.P([html.Br()])),
  dcc.Markdown("""
The management of prostate cancer that is detected on the basis of prostate-specific antigen (PSA) levels remains controversial. In the United States alone, each year, an estimated 180,890 new 
cases will be diagnosed and 26,120 men will die from the disease. PSA testing has resulted in a significant increase in the diagnosis and treatment of prostate cancer, but many men do not benefit
from intervention because the disease is either indolent or disseminated at diagnosis. Prostate cancer often progresses slowly, and many men die of competing causes. 

In order to assess whether a patient with prostate cancer could actually benefit from cancer treatment, and not die from another cause, we created a model to predict 10-year overall survival. 
We also provide explainability for the model's predictions, using SHAP values.

This model was trained on data from the prospective randomized multicenter trial PLCO that assessed the interest of prostate cancer screening with annual PSA testing for 6 years and digital rectal examination for 4 years.

From 1993 through 2001, 76,693 men at 10 U.S. study centers were randomly assigned to receive either annual screening (38,343 subjects) or usual care as the control (38,350 subjects).

To build this model we selected the patients that were diagnosed with prostate cancer during follow-up (n=13,738).
""")]



