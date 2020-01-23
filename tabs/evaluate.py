from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [
dcc.Markdown("""
	### Overall survival model metrics

	|  Metric      |  Result   |
	|--------------|-----------|
	| Accuracy     | 87.55%    |
	| Precision    | 66.19%    |
	| Recall       | 86.13%    |
	| ROC AUC      | 94.31%    |
	| PR AUC       | 87.73%    |

	"""),
dcc.Markdown("""
	### Cancer-specific survival model metrics

	|  Metric      |  Result   |
	|--------------|-----------|
	| Accuracy     | 98.29%    |
	| Precision    | 85%       |
	| Recall       | 77.86%    |
	| ROC AUC      | 95.34%    |
	| PR AUC       | 81.93%    |

	""")
]
