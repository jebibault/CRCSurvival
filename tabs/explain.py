from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
#### The PLCO Trial
The effect of screening with prostate-specific–antigen (PSA) testing and digital rectal examination on the rate of death
from prostate cancer is unknown. This is the first report from the Prostate, Lung, Colorectal, and Ovarian (PLCO) 
Cancer Screening Trial on prostate-cancer mortality. From 1993 through 2001, we randomly assigned 76,693 men at 10 
U.S. study cen- ters to receive either annual screening (38,343 subjects) or usual care as the control (38,350 subjects). 
Men in the screening group were offered annual PSA testing for 6 years and digital rectal examination for 4 years. 
The subjects and health care providers received the results and decided on the type of follow-up evaluation. 
Usual care sometimes included screening, as some organizations have recommend- ed. The numbers of all cancers 
and deaths and causes of death were ascertained.

Results of the trial were published in three articles:
- https://www.ncbi.nlm.nih.gov/pubmed/19297565
- https://www.ncbi.nlm.nih.gov/pubmed/22228146
- https://www.ncbi.nlm.nih.gov/pubmed/27911486

#### The Data and Evaluation Protocol
The data with 13 years median follow-up was obtained from the National Cancer Institute Cancer Data Access System:
https://cdas.cancer.gov/plco/

#### Model Creation
To build this model we selected the patients that were diagnosed with prostate cancer during follow-up (n=13,738). 
The dataset was split into a training (n=10,990) and a testing (n=2748) dataset.
XGBoost was used to predict 10-year overall survival. Hyperparameters were tuned with Bayesian Optimization 
in a nested cross-validation manner. Performances were evaluated on the test dataset.
""")]
