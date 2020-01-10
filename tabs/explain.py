from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [
	dcc.Markdown("""
	#### The PLCO Trial
	The Prostate, Lung, Colorectal, and Ovarian (PLCO) Cancer Screening Trial was conducted
	to assess the role of prostate cancer screening on survival. From 1993 through 2001, 76,693 men at 10 
	U.S. study centers were randomized to receive either annual screening (38,343 subjects) or usual care as the control (38,350 subjects). 
	Men in the screening group were offered annual PSA testing for 6 years and digital rectal examination for 4 years. 
	The subjects and health care providers received the results and decided on the type of follow-up evaluation. 
	Results of the trial were published in three articles:"""),
	
	dcc.Link('Andriole GL et al., New England Journal of Medicine, 2009', 
		 href='https://www.ncbi.nlm.nih.gov/pubmed/19297565',
		 target='_blank',
		 style={'font-weight': 'bold', 'color': '#820000'}),
	
	html.P([]),
	
	dcc.Link('Andriole GL et al., Journal of the National Cancer Institute, 2012', 
		 href='https://www.ncbi.nlm.nih.gov/pubmed/22228146',
		 target='_blank',
		 style={'font-weight': 'bold', 'color': '#820000'}),
	
	html.P([]),
	
	dcc.Link('Pinsky PF et al., Cancer, 2017', 
		 href='https://www.ncbi.nlm.nih.gov/pubmed/19297565',
		 target='_blank',
		 style={'font-weight': 'bold', 'color': '#820000'}),
	
	html.P([]),
	
	dcc.Markdown("""
	#### Data
	The data with a 13-years median follow-up was obtained from the National Cancer Institute Cancer Data Access System:"""),
	
	dcc.Link('NCI CDAS', 
		 href='https://cdas.cancer.gov/plco/',
		 target='_blank',
		 style={'font-weight': 'bold', 'color': '#820000'}),
	
	dcc.Markdown("""
	#### Model Creation
	To build this model we selected the patients that were diagnosed with prostate cancer during follow-up (n=13,738). 
	The dataset was split into a training (n=10,990) and a testing (n=2748) dataset.
	XGBoost was used to predict 10-year overall survival. Hyperparameters were tuned with Bayesian Optimization 
	in a nested cross-validation manner. Performances were evaluated on the test dataset.""")]
