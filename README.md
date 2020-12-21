# Predict 10-year cancer-specific survival in colorectal cancer
Colorectal cancer (CRC) is the third most commonly diagnosed cancer in males and the second in females, with 1.8 million new cases and almost 861,000 deaths in 2018 according to the World Health Organization GLOBOCAN database. In the US alone, approximately 147,950 new cases of large bowel cancer are diagnosed, . Annually, approximately 53,200 Americans die of CRC, accounting for approximately 8 percent of all cancer deaths.', 
In order to be able to better personalize treatment strategies, we created an interpretable AI model to predict 10-year cancer-specific survival of patients with CRC.

# Paper published in Gut
https://gut.bmj.com/content/early/2020/09/03/gutjnl-2020-321799

# PLCO Trial
From 1993 through 2001, 154,900 men and women 55 to 74 years of age were randomized either to screening with flexible sigmoidoscopy, with a repeat screening at 3 or 5 years, or to usual care. Significant reductions were observed in the incidence of both distal colorectal cancer (479 cases in the intervention group vs. 669 cases in the usual-care group; relative risk, 0.71; 95% CI, 0.64 to 0.80; P<0.001) and proximal colorectal cancer (512 cases vs. 595 cases; relative risk, 0.86; 95% CI, 0.76 to 0.97; P=0.01). There were also fewer death in the screening arm of the trial: 2.9 deaths from colorectal cancer per 10,000 person-years in the intervention group (252 deaths), as compared with 3.9 per 10,000 person-years in the usual-care group (341 deaths), which represents a 26% reduction (relative risk, 0.74; 95% CI, 0.63 to 0.87; P<0.001).',

# Data
The data were obtained from the National Cancer Institute Cancer Data Access System.

# Model creation
To build this model we selected the patients that were diagnosed with CRC cancer during follow-up (n=2,359). The dataset was split into a training (n=1,887) and a testing (n=472) dataset. XGBoost was used to predict 10-year cancer-specific. Hyperparameters were tuned with Bayesian Optimization	in a nested cross-validation manner. Performances were evaluated on the test dataset with the bootstrap procedure.

The contents of the repository include the following:

assets
- custom css
- favicon

figures
- logo of the app

models
- 10yCSSmodel.pkl - the XGBoost model used for cancer-specific survival prediction

tabs
- intro.py - The code for the 'About' tab
- predictCSS.py - The code for the 'Predict cancer-specific survival' tab

main app
- app.py - Initiates the Dash app
- index.py - The main Dash code with the layout and callback
- Procfile - The Procfile for Heroku
- requirements.txt - The requirements.txt file for Heroku
