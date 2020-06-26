import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import random
import math
# import column_values
df = pd.read_csv(r"assets/column_values.csv")
# sliders - used for updating slider values in visualizations.py
sliders = []
# column layout
column = dbc.Col([], md=6,)
# storage for sliders and dropdowns
selected_cols = {}
options = []
column_names = []
# populate storage
for col, coldata in df.select_dtypes(include=np.number).iteritems():
    selected_cols[col] = list(coldata.dropna())
    #{"label" : [min,max]}
    column_names.append(col)

for col, coldata in df.select_dtypes(exclude=np.number).iteritems():
    opt = []
    for value in coldata:
        if not value != value:
            opt.append({"label": str(value), "value": str(value), })
    opts = {col: opt}
    options.append(opts)
    column_names.append(col)

# iterate, we want to maintain index
i = 0
for key in selected_cols:
    column.children.append(html.H3(key))
    step = 0.1 if selected_cols[key][1] < 10 else 1
    value = random.uniform(0, float(selected_cols[key][1]))
    slid = dcc.Slider(
        id=f'd{i}',
        min=0,
        max=float(selected_cols[key][1]),
        step=0.1,
        value=value,
        className='mb-2')
    column.children.append(slid)
    sliders.append(slid)
    column.children.append(html.Div(id=f"val{i}", children="value"))
    #column.children.append(html.Button('randomize', id=f'rb{i}', n_clicks=0))
    i = i + 1

for opt in options:
    key = list(opt.keys())[0]
    option = opt[key]
    value = option[0]["label"]

    column.children.append(html.H3(key))
    dd = dcc.Dropdown(
        id=f'd{i}',
        options=option,
        value=option[0]["value"],
        className='mb-5 mt-3')
    column.children.append(dd)
    i = i + 1


column2 = dbc.Col(
    [
        html.H3("Predicted scan quality",
                className="justify-content-center ml-2"),
        html.H1(id='prediction', className="mt-3 ml-2"),
    ], style={"position": "fixed", "right": "150px"},
    md=4,
)
layout_inputs = [dbc.Row([column, column2]), ]
