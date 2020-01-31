import dash

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
server = app.server

app.scripts.config.serve_locally = False
app.scripts.append_script({
    'external_url': 'https://cdn.jsdelivr.net/gh/jebibault/ProstateCancerSurvival/assets/async_src.js'
    })
app.scripts.append_script({
    'external_url': 'https://cdn.jsdelivr.net/gh/jebibault/ProstateCancerSurvival/assets/gtag.js'
    })