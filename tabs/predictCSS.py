from plotly.tools import mpl_to_plotly
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
import pickle
import numpy as np
import pandas as pd
import shap
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('agg')
import base64
from io import BytesIO

from app import app

style = {'padding': '1.5em'}

layout = html.Div([
  html.P([html.Br()]),
  html.P([html.Br()]),
  dcc.Markdown('#### Please answer these 33 questions to predict 10-year cancer-specific survival'),
  dcc.Markdown('#### Answers must reflect data at diagnosis'),
  dcc.Markdown('Each form must be carefully filled out to obtain the prediction'),
  html.P([html.Br()]),
  dcc.Markdown('#### Colorectal cancer history'),
  dcc.Markdown('###### Age at diagnosis (years)'),
  dcc.Input(
    id='age_at_diagnosis',
    placeholder='Enter a value',
    type='number',
    value=''),
  
  dcc.Markdown('###### T stage'),
  dcc.Dropdown(
    id='t_stage',
    options=[
        {'label': 'T0', 'value': '0'},
        {'label': 'Tis', 'value': '20'},
        {'label': 'T1', 'value': '100'},
        {'label': 'T2', 'value': '200'},
        {'label': 'T3', 'value': '300'},
        {'label': 'T4', 'value': '400'},
        {'label': 'Tx', 'value': '999'}
    ],
    value=''
  ),
  
  dcc.Markdown('###### N stage'),
  dcc.Dropdown(
    id='n_stage',
    options=[
        {'label': 'N0', 'value': '0'},
        {'label': 'N1', 'value': '100'},
        {'label': 'N2', 'value': '200'},
        {'label': 'Nx', 'value': '999'}
    ],
    value=''
  ),
  
  dcc.Markdown('###### M stage'),
  dcc.Dropdown(
    id='m_stage',
    options=[
        {'label': 'M0', 'value': '0'},
        {'label': 'M1a', 'value': '110'},
        {'label': 'M1b', 'value': '120'},
        {'label': 'M1c', 'value': '130'},
        {'label': 'Mx', 'value': '999'}
    ],
    value=''
  ),

  dcc.Markdown('###### Tumor Grade'),
  dcc.Dropdown(
    id='tumor_grade',
    options=[
        {'label': 'Grade Cannot Be Assessed (GX)', 'value': '1'},
        {'label': 'Well Differentiated (G1)', 'value': '2'},
        {'label': 'Moderately Differentiated (G2)', 'value': '3'},
        {'label': 'Poorly Differentiated (G3)', 'value': '4'},
        {'label': 'Undifferentiated (G4)', 'value': '5'},
        {'label': 'Not available', 'value': '99'}
    ],
    value=''
  ),

  dcc.Markdown('###### What is the type of cancer?'),
  dcc.Dropdown(
    id='cancer_type',
    options=[
        {'label': 'Colorectal cancer', 'value': '1'},
        {'label': 'Colorectal carcinoid', 'value': '2'}
    ],
    value=''
  ),

  dcc.Markdown('###### What is the histology?'),
  dcc.Dropdown(
    id='histology',
    options=[
        {'label': 'Adenocarcinoma, not otherwise specified', 'value': '2'},
        {'label': 'Mucinous Adenocarcinoma', 'value': '3'},
        {'label': 'Signet Ring Cell Carcinoma', 'value': '4'},
        {'label': 'Squamous Cell Carcinoma', 'value': '5'},
        {'label': 'Adenosquamous Carcinoma', 'value': '6'},
        {'label': 'Undifferentiated Carcinoma', 'value': '8'},
        {'label': 'Carcinoma', 'value': '9'},
        {'label': 'Carcinoma, not otherwise specified', 'value': '31'},
        {'label': 'Adenocarcinoid', 'value': '36'},
        {'label': 'Carcinoid/Neuroendocrine Carcinoma', 'value': '37'},
        {'label': 'Carcinosarcoma/Sarcoma/GIST (Gastroinstestinal Stromal Tumor)', 'value': '39'},
        {'label': 'Not available', 'value': '99'}
    ],
    value=''
  ),

dcc.Markdown('###### What is the location?'),
  dcc.Dropdown(
    id='cancer_location',
    options=[
        {'label': 'Rectum', 'value': '1'},
        {'label': 'Rectosigmoid junction', 'value': '2'},
        {'label': 'Sigmoid colon', 'value': '3'},
        {'label': 'Descending colon', 'value': '4'},
        {'label': 'Splenic flexure of colon', 'value': '5'},
        {'label': 'Transverse colon', 'value': '6'},
        {'label': 'Hepatic flexure of colon', 'value': '7'},
        {'label': 'Ascending colon', 'value': '8'},
        {'label': 'Cecum', 'value': '10'},
        {'label': 'Colon, not otherwise specified', 'value': '12'}
    ],
    value=''
  ),

  dcc.Markdown('###### On which side is the cancer?'),
  dcc.Dropdown(
    id='cancer_side',
    options=[
        {'label': 'Distal', 'value': '1'},
        {'label': 'Proximal', 'value': '2'},
        {'label': 'Unclear', 'value': '3'}

    ],
    value=''
  ),

  dcc.Markdown('###### Was surgery performed in the initial treatment?'),
  dcc.Dropdown(
    id='curative_surgery',
    options=[
        {'label': 'No', 'value': '0'},
        {'label': 'Yes', 'value': '1'}
    ],
    value=''
  ),

  dcc.Markdown('###### If yes, was any curative treatment performed before surgery (neoadjuvant)?'),
  dcc.Dropdown(
    id='neoadjuvant_treatment',
    options=[
        {'label': 'No', 'value': '0'},
        {'label': 'Yes', 'value': '1'}
    ],
    value=''
  ),

  dcc.Markdown('###### Was radiotherapy performed in the initial treatment?'),
  dcc.Dropdown(
    id='curative_radiotherapy',
    options=[
        {'label': 'No', 'value': '0'},
        {'label': 'Yes', 'value': '1'}
    ],
    value=''
  ),

  dcc.Markdown('###### Did you receive chemotherapy in the initial treatment?'),
  dcc.Dropdown(
    id='curative_chemotherapy',
    options=[
        {'label': 'No', 'value': '0'},
        {'label': 'Yes', 'value': '1'}
    ],
    value=''
  ),

  html.P([html.Br()]),
  html.P([html.Br()]),
  dcc.Markdown('#### Medical history'),

  dcc.Markdown('###### Do you have a firs-degree family history of colorectal cancer?'),
  dcc.Dropdown(
    id='family_history',
    options=[
        {'label': 'No', 'value': '0'},
        {'label': 'Yes, immediate family', 'value': '1'},
        {'label': 'Possibly, relative or cancer type not clear', 'value': '9'}
    ],
    value=''
  ),

  dcc.Markdown('###### Height (in meters)'),
  dcc.Input(
    id='height',
    placeholder='Enter a value in meters',
    type='number',
    value=''),

  dcc.Markdown('###### Weight (in kilograms)'),
  dcc.Input(
    id='weight',
    placeholder='Enter a value in kilograms',
    type='number',
    value=''),
  
  dcc.Markdown("""
    ###### Years of smoking 
    """),
  dcc.Input(
    id='years_smoking',
    placeholder='Enter a value',
    type='number',
    value=''),

    dcc.Markdown("""
    ###### Pack of cigarettes smoked each day
    """),
  dcc.Input(
    id='packs',
    placeholder='Enter a value',
    type='number',
    value=''),

  dcc.Markdown('###### Number of drinks of alcohol per day'),
  dcc.Input(
    id='alcohol',
    placeholder='Enter a value',
    type='number',
    value=''),

  dcc.Markdown('###### Do you have an history of arthritis?'),
  dcc.Dropdown(
    id='history_of_arthritis',
    options=[
        {'label': 'No', 'value': '0'},
        {'label': 'Yes', 'value': '1'}
    ],
    value='',
    ),
    
  dcc.Markdown('###### Do you have an history of bronchitis?'),
  dcc.Dropdown(
    id='history_of_bronchitis',
    options=[
        {'label': 'No', 'value': '0'},
        {'label': 'Yes', 'value': '1'}
    ],
    value='',
    ),
    
  dcc.Markdown('###### Do you have an history of diabetes?'),
  dcc.Dropdown(
    id='history_of_diabetes',
    options=[
        {'label': 'No', 'value': '0'},
        {'label': 'Yes', 'value': '1'}
    ],
    value='',
    ),

  dcc.Markdown('###### Do you have an history of emphysema?'),
  dcc.Dropdown(
    id='history_of_emphysema',
    options=[
        {'label': 'No', 'value': '0'},
        {'label': 'Yes', 'value': '1'}
    ],
    value='',
    ),

  dcc.Markdown('###### Do you have an history of heart attack?'),
  dcc.Dropdown(
    id='history_of_heart_attack',
    options=[
        {'label': 'No', 'value': '0'},
        {'label': 'Yes', 'value': '1'}
    ],
    value='',
    ),

  dcc.Markdown('###### Do you have an history of hypertension?'),
  dcc.Dropdown(
    id='history_of_hypertension',
    options=[
        {'label': 'No', 'value': '0'},
        {'label': 'Yes', 'value': '1'}
    ],
    value='',
    ),

  dcc.Markdown('###### Do you have an history of liver disease?'),
  dcc.Dropdown(
    id='history_of_liver_disease',
    options=[
        {'label': 'No', 'value': '0'},
        {'label': 'Yes', 'value': '1'}
    ],
    value='',
    ),

  dcc.Markdown('###### Do you have an history of osteoporosis?'),
  dcc.Dropdown(
    id='history_of_osteoporosis',
    options=[
        {'label': 'No', 'value': '0'},
        {'label': 'Yes', 'value': '1'}
    ],
    value='',
    ),

  dcc.Markdown('###### Do you have an history of stroke?'),
  dcc.Dropdown(
    id='history_of_stroke',
    options=[
        {'label': 'No', 'value': '0'},
        {'label': 'Yes', 'value': '1'}
    ],
    value='',
    ),

  dcc.Markdown('###### Do you have an history of cholesterol?'),
  dcc.Dropdown(
    id='history_of_cholesterol',
    options=[
        {'label': 'No', 'value': '0'},
        {'label': 'Yes', 'value': '1'}
    ],
    value='',
  ),

  html.P([html.Br()]),
  html.P([html.Br()]),
  dcc.Markdown('#### Physical activity'),

  dcc.Markdown('###### Were you active at least once a month in the past 12 months?'),
  dcc.Dropdown(
    id='physical_activity',
    options=[
        {'label': 'No', 'value': '0'},
        {'label': 'Yes', 'value': '1'}
    ],
    value='',
  ),

  dcc.Markdown('###### How would you describe your physical activity at work?'),
  dcc.Dropdown(
    id='work_activity',
    options=[
        {'label': 'Did not work', 'value': '1'},
        {'label': 'Mostly sitting', 'value': '2'},
        {'label': 'Mostly walking, some sitting', 'value': '3'},
        {'label': 'Mostly walking, with some manual labor', 'value': '4'},
        {'label': 'Mostly manual labor', 'value': '5'}
    ],
    value=''
  ),

  html.P([html.Br()]),  
  html.P([html.Br()]),
  dcc.Markdown('#### Miscellaneous'),

  dcc.Markdown('###### What is your current family income?'),
  dcc.Dropdown(
    id='income',
    options=[
        {'label': '< $20,000', 'value': '1'},
        {'label': '$20,000-$49,000', 'value': '2'},
        {'label': '$50,000-$99,000', 'value': '3'},
        {'label': '$100,000-$200,000', 'value': '4'},
        {'label': '>$200,000', 'value': '5'},
        {'label': 'Prefer not to answer', 'value': '6'}
    ],
    value='',
  ),

  dcc.Markdown('###### What is the highest grade or level of schooling you completed?'),
  dcc.Dropdown(
    id='education',
    options=[
        {'label': 'less than 8 years', 'value': '1'},
        {'label': '8 to 11 years', 'value': '2'},
        {'label': 'High School', 'value': '3'},
        {'label': 'Post High School Training', 'value': '4'},
        {'label': 'College dropout', 'value': '5'},
        {'label': 'College graduate', 'value': '6'},
        {'label': 'Postgraduate', 'value': '7'}
    ],
    value='',
  ),

  html.P([html.Br()]),  
  html.P([html.Br()]),
  html.Div(html.P(['The predicted probability of dying from colorectal cancer within 10 years after diagnosis is:']), style={'fontWeight': 'bold', 'color': '#820000', 'font-size': 'large'}),
  html.Div(id='CSSprediction-content', style={'fontWeight': 'bold', 'color': '#820000', 'font-size': 'large', 'text-align': 'center'}),
  html.Div(html.P(['This chart shows the most important features associated with a higher (red) or lower (blue) risk of dying.']), style={'text-align': 'center'}),
  html.P([html.Br()])
])

@app.callback(
    Output('CSSprediction-content', 'children'),
    [Input('t_stage', 'value'),
     Input('n_stage', 'value'),
     Input('m_stage', 'value'),
     Input('tumor_grade', 'value'),
     Input('cancer_type', 'value'),
     Input('histology', 'value'),
     Input('cancer_location', 'value'),
     Input('cancer_side', 'value'),
     Input('family_history', 'value'),
     Input('family_history_age', 'value'),
     Input('curative_chemotherapy', 'value'),
     Input('curative_radiotherapy', 'value'),
     Input('curative_surgery', 'value'),
     Input('neoadjuvant_treatment', 'value'),
     Input('education', 'value'),
     Input('years_smoking', 'value'),
     Input('packs', 'value'),
     Input('height', 'value'),
     Input('weight', 'value'),
     Input('history_of_arthritis', 'value'),
     Input('history_of_bronchitis', 'value'),
     Input('history_of_diabetes', 'value'),
     Input('history_of_emphysema', 'value'),
     Input('history_of_heart_attack', 'value'),
     Input('history_of_hypertension', 'value'),
     Input('history_of_liver_disease', 'value'),
     Input('history_of_osteoporosis', 'value'),
     Input('history_of_stroke', 'value'),
     Input('alcohol', 'value'),
     Input('income', 'value'),
     Input('history_of_cholesterol', 'value'),
     Input('physical_activity', 'value'),
     Input('work_activity', 'value'),
     Input('age_at_diagnosis', 'value')
     ])

def predict(t_stage, n_stage, m_stage, tumor_grade, cancer_type, histology, cancer_location, cancer_side, family_history, family_history_age, curative_chemotherapy, curative_radiotherapy, curative_surgery, neoadjuvant_treatment, education, packs, years_smoking, weight, height, history_of_arthritis, history_of_bronchitis, history_of_diabetes, history_of_emphysema, history_of_heart_attack, history_of_hypertension, history_of_liver_disease, history_of_osteoporosis, history_of_stroke, alcohol, income, history_of_cholesterol, physical_activity, work_activity, age_at_diagnosis):

  t_stage = int(float(t_stage))
  n_stage = int(float(n_stage))
  m_stage = int(float(m_stage))
  tumor_grade = int(float(tumor_grade))
  cancer_type = int(float(cancer_type))
  histology = int(float(histology))
  cancer_location = int(float(cancer_location))
  cancer_side = int(float(cancer_side))
  family_history = int(float(family_history))
  curative_chemotherapy = int(float(curative_chemotherapy))
  curative_radiotherapy = int(float(curative_radiotherapy))
  curative_surgery = int(float(curative_surgery))
  neoadjuvant_treatment = int(float(neoadjuvant_treatment))
  history_of_arthritis = int(float(history_of_arthritis))
  history_of_bronchitis = int(float(history_of_bronchitis))
  history_of_diabetes = int(float(history_of_diabetes))
  history_of_emphysema = int(float(history_of_emphysema))
  history_of_heart_attack = int(float(history_of_heart_attack))
  history_of_hypertension = int(float(history_of_hypertension))
  history_of_liver_disease = int(float(history_of_liver_disease))
  history_of_osteoporosis = int(float(history_of_osteoporosis))
  history_of_stroke = int(float(history_of_stroke))
  history_of_cholesterol = int(float(history_of_cholesterol))
  physical_activity = int(float(physical_activity))
  work_activity = int(float(work_activity))
  income = int(float(income))
  education = int(float(education))
  alcohol = float(alcohol)
  packs = float(packs)
  years_smoking = float(years_smoking)
  weight = float(weight)
  height = float(height)
  pack_years = packs * years_smoking
  current_bmi = weight / (height*height)
  alcohol_consumption = alcohol * 14

  df = pd.DataFrame(
    columns=['t_stage','n_stage','m_stage','tumor_grade','cancer_type','histology','cancer_location','cancer_side','family_history','curative_chemotherapy','curative_radiotherapy','curative_surgery','neoadjuvant_treatment','education','pack_years','current_bmi','history_of_arthritis','history_of_bronchitis','history_of_diabetes','history_of_emphysema','history_of_heart_attack','history_of_hypertension','history_of_liver_disease','history_of_osteoporosis','history_of_stroke','alcohol_consumption','income','history_of_cholesterol','physical_activity','work_activity','age_at_diagnosis'],
    data=[[t_stage, n_stage, m_stage, tumor_grade, cancer_type, histology, cancer_location, cancer_side, family_history, curative_chemotherapy, curative_radiotherapy, curative_surgery, neoadjuvant_treatment, education, pack_years, current_bmi, history_of_arthritis, history_of_bronchitis, history_of_diabetes, history_of_emphysema, history_of_heart_attack, history_of_hypertension, history_of_liver_disease, history_of_osteoporosis, history_of_stroke, alcohol_consumption, income, history_of_cholesterol, physical_activity, work_activity, age_at_diagnosis]]
    )

  model = pickle.load(open('models/10yCSSmodel.pkl', 'rb'))
  y_pred_proba = model.predict_proba(df)[:,1]
  y_pred = float(y_pred_proba) * 100
  y_pred = np.round(y_pred, 2)
  results = f'{y_pred}%'

  explainer = shap.TreeExplainer(model)
  shap_values = explainer.shap_values(df)
  shap.force_plot(explainer.expected_value, shap_values, df, matplotlib=True, show=False)
  buf = BytesIO()
  plt.savefig(buf, format="png")
  data = base64.b64encode(buf.getbuffer()).decode("ascii")
  displ = html.Div(html.P([html.Br(), html.Br(), html.Br()]))
  graph = html.Img(src='data:image/png;base64,{}'.format(data), style={'width' : '900px', 'text-align': 'center'})

  return results, displ, graph