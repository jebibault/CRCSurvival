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
  dcc.Markdown('#### Please answer these 30 questions to predict 10-year cancer-specific survival'),
  dcc.Markdown('#### Answers must reflect data at diagnosis.'),
  dcc.Markdown('Each form must be carefully filled out to obtain the prediction.'),
  html.P([html.Br()]),
  dcc.Markdown('#### Prostate cancer history'),
  dcc.Markdown('###### Age at diagnosis (years)'),
  dcc.Input(
    id='age_at_diagnosis',
    placeholder='Enter a value',
    type='number',
    value=''),
  
  dcc.Markdown('###### PSA (ng/mL)'),
  dcc.Input(
    id='psa_at_diagnosis',
    placeholder='Enter a value',
    type='number',
    value=''),
  
  dcc.Markdown('###### T stage'),
  dcc.Dropdown(
    id='t_stage',
    options=[
        {'label': 'T0', 'value': '0'},
        {'label': 'T1', 'value': '100'},
        {'label': 'T1a', 'value': '110'},
        {'label': 'T1b', 'value': '120'},
        {'label': 'T1c', 'value': '130'},
        {'label': 'T2', 'value': '200'},
        {'label': 'T2a', 'value': '210'},
        {'label': 'T2b', 'value': '220'},
        {'label': 'T2c', 'value': '230'},
        {'label': 'T3', 'value': '300'},
        {'label': 'T3a', 'value': '310'},
        {'label': 'T3b', 'value': '320'},
        {'label': 'T3c', 'value': '330'},
        {'label': 'T4', 'value': '400'},
        {'label': 'T4a', 'value': '410'},
        {'label': 'T4b', 'value': '420'},
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
  
  dcc.Markdown('###### Gleason Score'),
  dcc.Input(
    id='gleason_score',
    placeholder='Enter a value',
    type='number',
    value=''),

  dcc.Markdown('###### What was the initial primary treatment performed?'),
  dcc.Dropdown(
    id='treatment',
    options=[
        {'label': 'Prostatectomy', 'value': '1'},
        {'label': 'Radiation therapy without prostatectomy', 'value': '2'},
        {'label': 'Radiation therapy and hormone therapy, without prostatectomy', 'value': '3'},
        {'label': 'Hormone therapy, without prostatectomy or radiation', 'value': '4'},
        {'label': 'Other ablative treatment', 'value': '5'},
        {'label': 'Non-curative treatment', 'value': '6'},
        {'label': 'Do not know', 'value': '10'}
    ],
    value=''
  ),

  dcc.Markdown('###### How often do you wake up to urinate?'),
  dcc.Dropdown(
    id='nocturia',
    options=[
        {'label': 'Never', 'value': '0'},
        {'label': 'Once', 'value': '1'},
        {'label': 'Twice', 'value': '2'},
        {'label': 'Thrice ', 'value': '3'},
        {'label': 'Four times or more', 'value': '4'},
    ],
    value=''
  ),

  html.P([html.Br()]),
  html.P([html.Br()]),
  dcc.Markdown('#### Medical history'),

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

  dcc.Markdown('###### What is your smoking status?'),
  dcc.Dropdown(
    id='current_smoker',
    options=[
        {'label': 'Never smoked cigarettes', 'value': '0'},
        {'label': 'Current cigarette smoker', 'value': '1'},
        {'label': 'Former cigarette smoker', 'value': '2'}
    ],
    value='',
  ),
  
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

  dcc.Markdown('###### Do you have an history of prostatitis?'),
  dcc.Dropdown(
    id='history_of_prostatitis',
    options=[
        {'label': 'No', 'value': '0'},
        {'label': 'Yes', 'value': '1'}
    ],
    value='',
  ),
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

  dcc.Markdown('###### What was you hair pattern at age 45?'),
  dcc.Dropdown(
    id='hair_pattern',
    options=[
        {'label': 'No balding', 'value': '0'},
        {'label': 'Mild forehead recession', 'value': '1'},
        {'label': 'Mild forehead recession + Small Top Balding', 'value': '2'},
        {'label': 'Forehead + top balding', 'value': '3'},
        {'label': 'Hair only on sides and back', 'value': '4'}
    ],
    value='',
  ),

  dcc.Markdown('###### What is your weight gain pattern?'),
  dcc.Dropdown(
    id='weight_gain',
    options=[
        {'label': 'I do not gain weight', 'value': '1'},
        {'label': 'Around chest and shoulders', 'value': '2'},
        {'label': 'Around waist and stomach', 'value': '3'},
        {'label': 'Around hips and thighs', 'value': '4'},
        {'label': 'Equally all over', 'value': '5'}
    ],
    value='',
  ),

  html.P([html.Br()]),  
  html.P([html.Br()]),
  html.Div(html.P(['The predicted probability of dying from prostate cancer within 10 years after diagnosis is:']), style={'fontWeight': 'bold', 'color': '#820000', 'font-size': 'large'}),
  html.Div(id='CSSprediction-content', style={'fontWeight': 'bold', 'color': '#820000', 'font-size': 'large', 'text-align': 'center'}),
  html.Div(html.P(['This chart shows the most important features associated with a higher (red) or lower (blue) risk of dying.']), style={'text-align': 'center'}),
  html.P([html.Br()])
])

@app.callback(
    Output('CSSprediction-content', 'children'),
    [Input('age_at_diagnosis', 'value'),
     Input('psa_at_diagnosis', 'value'),
     Input('t_stage', 'value'),
     Input('n_stage', 'value'),
     Input('m_stage', 'value'),
     Input('gleason_score', 'value'),
     Input('treatment', 'value'),
     Input('nocturia', 'value'),
     Input('height', 'value'),
     Input('weight', 'value'),
     Input('current_smoker', 'value'),
     Input('years_smoking', 'value'),
     Input('packs', 'value'),
     Input('history_of_prostatitis', 'value'),
     Input('history_of_arthritis', 'value'),
     Input('history_of_bronchitis', 'value'),
     Input('history_of_diabetes', 'value'),
     Input('history_of_emphysema', 'value'),
     Input('history_of_heart_attack', 'value'),
     Input('history_of_hypertension', 'value'),
     Input('history_of_liver_disease', 'value'),
     Input('history_of_osteoporosis', 'value'),
     Input('history_of_stroke', 'value'),
     Input('history_of_cholesterol', 'value'),
     Input('physical_activity', 'value'),
     Input('work_activity', 'value'),
     Input('alcohol', 'value'),
     Input('income', 'value'),
     Input('education', 'value'),
     Input('hair_pattern', 'value'),
     Input('weight_gain', 'value')])

def predict(age_at_diagnosis, psa_at_diagnosis, t_stage, n_stage, m_stage, gleason_score, treatment, nocturia, height, weight, current_smoker, years_smoking, packs, history_of_prostatitis, history_of_arthritis, history_of_bronchitis, history_of_diabetes, history_of_emphysema, history_of_heart_attack, history_of_hypertension, history_of_liver_disease, history_of_osteoporosis, history_of_stroke, history_of_cholesterol, physical_activity, work_activity, alcohol, income, education, hair_pattern, weight_gain):

  age_at_diagnosis = float(age_at_diagnosis)
  psa_at_diagnosis = float(psa_at_diagnosis)
  t_stage = int(float(t_stage))
  n_stage = int(float(n_stage))
  m_stage = int(float(m_stage))
  gleason_score = int(float(gleason_score))
  treatment = int(float(treatment))
  nocturia = int(float(nocturia))
  current_smoker = int(float(current_smoker))
  history_of_prostatitis = int(float(history_of_prostatitis))
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
  hair_pattern = int(float(hair_pattern))
  weight_gain = int(float(weight_gain))
  alcohol = float(alcohol)

  packs = float(packs)
  years_smoking = float(years_smoking)
  weight = float(weight)
  height = float(height)
  pack_years = packs * years_smoking
  current_bmi = weight / (height*height)
  alcohol_consumption = alcohol * 14

  df = pd.DataFrame(
    columns=['t_stage','n_stage','m_stage','gleason_score','psa_at_diagnosis','treatment','education','current_smoker','pack_years','current_bmi','history_of_arthritis','history_of_bronchitis','history_of_diabetes','history_of_emphysema','history_of_heart_attack','history_of_hypertension','history_of_liver_disease','history_of_osteoporosis','history_of_stroke','history_of_prostatitis','alcohol_consumption','income','weight_gain','history_of_cholesterol','physical_activity','work_activity','hair_pattern','nocturia','age_at_diagnosis'],
    data=[[t_stage, n_stage, m_stage, gleason_score, psa_at_diagnosis, treatment, education, current_smoker, pack_years, current_bmi, history_of_arthritis, history_of_bronchitis, history_of_diabetes, history_of_emphysema, history_of_heart_attack, history_of_hypertension, history_of_liver_disease, history_of_osteoporosis, history_of_stroke, history_of_prostatitis, alcohol_consumption, income, weight_gain, history_of_cholesterol, physical_activity, work_activity, hair_pattern, nocturia, age_at_diagnosis]]
    )

  model = pickle.load(open('model/10yCSSmodel.pkl', 'rb'))
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