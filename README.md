# Predict 10-year survival in prostate cancer
This model was trained on data from the prospective randomized multicenter trial PLCO that assessed the interest of prostate cancer screening with annual PSA testing for 6 years and digital rectal examination for 4 years. From 1993 through 2001, 76,693 men at 10 U.S. study centers were randomly assigned to receive either annual screening (38,343 subjects) or usual care as the control (38,350 subjects).

To build this model we selected the patients that were diagnosed with prostate cancer during follow-up (n=8,776). The dataset was split into a training (n=7,021) and a testing (n=1,755) dataset. 

XGBoost was used to predict 10-year cancer-specific and overall survival. Hyperparameters were tuned with Bayesian Optimization in a nested cross-validation manner. Performances were evaluated on the test dataset.

The contents of the repository include the following:

assets
- custom css
- favicon

figures
- logo of the app

models
- 10yCSSmodel.pkl - the XGBoost model used for cancer-specific survival prediction
- 10yOSmodel.pkl - the XGBoost model used for overall survival prediction

tabs
- intro.py - The code for the 'About' tab
- predictCSS.py - The code for the 'Predict cancer-specific survival' tab
- predictOS.py - The code for the 'Predict overall survival' tab

main app
- app.py - Initiates the Dash app
- index.py - The main Dash code with the layout and callback
- Procfile - The Procfile for Heroku
- requirements.txt - The requirements.txt file for Heroku
