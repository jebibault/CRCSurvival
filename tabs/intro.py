from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Intro
This model was trained on data from the prospective randomized multicenter trial PLCO that assessed the interest of prostate cancer screening with annual PSA testing for 6 years and digital rectal examination for 4 years.

From 1993 through 2001, 76,693 men at 10 U.S. study centers were randomly assigned to receive either annual screening (38,343 subjects) or usual care as the control (38,350 subjects).

To build this model we selected the patients that were diagnosed with prostate cancer during follow-up (n=13,738). The dataset was split into a training (n=10,990) and a testing (n=2748) dataset.

XGBoost was used to predict 10-year overall survival. Hyperparameters were tuned with Bayesian Optimization in a nested cross-validation manner. Performances were evaluated on the test dataset.
""")]
