import numpy as np
from server import app
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import pandas as pd
from layouts.inputs import sliders, selected_cols, df, column_names
from joblib import load
import plotly.express as px

pd.options.plotting.backend = "plotly"
pipeline = load('assets/model_best.joblib')

# def _generate_plot(dataframe):

#     data = [trace2]
#     fig = dataframe.plot()
#     fig = go.Figure(data=dataframe)

#     return fig


def _generate_chart(val1, val2):

    trace2 = go.Scatter(
        x=[val1],
        y=[val2],
        mode='markers'
    )
    data = [trace2]
    fig = go.Figure(data=data)

    return fig


inputs = []
# tried to avoid hard-coding, but it seems the values are not updating
for num in range(len(df.columns)):
    inputs.append(Input(f"d{num}", "value"))

# Updating slider text below the slider


def update_sliders(value):
    return '{}'.format(value)


for idx, slider in enumerate(sliders):
    app.callback(
        Output(f"val{idx}", 'children'),
        [Input(slider.id, "value")]
    )(update_sliders)


@app.callback(
    Output('prediction', 'children'),
    # This is really crazy can we do it without hard-coding the values?
    [Input("d0", "value"), Input("d1", "value"), Input("d2", "value"), Input("d3", "value"), Input("d4", "value"), Input("d5", "value"), Input("d6", "value"), Input("d7", "value"), Input("d8", "value"), Input("d9", "value"), Input("d10", "value"), Input("d11", "value"), Input("d12", "value"), Input("d13", "value"), Input("d14", "value"), Input("d15", "value"), Input("d16", "value"), Input("d17", "value"), Input("d18", "value"), Input("d19", "value"), Input(
        "d20", "value"), Input("d21", "value"), Input("d22", "value"), Input("d23", "value"), Input("d24", "value"), Input("d25", "value"), Input("d26", "value"), Input("d27", "value"), Input("d28", "value"), Input("d29", "value"), Input("d30", "value"), Input("d31", "value"), Input("d32", "value"), Input("d33", "value"), Input("d34", "value"), Input("d35", "value"), Input("d36", "value"), Input("d37", "value"), Input("d38", "value")]
)
def update_output(value0, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18, value19, value20, value21, value22, value23, value24, value25, value26, value27, value28, value29, value30, value31, value32, value33, value34, value35, value36, value37, value38):
    vals = [value0, value1, value2, value3, value4, value5, value6, value7, value8, value9, value10, value11, value12, value13, value14, value15, value16, value17, value18, value19, value20,
            value21, value22, value23, value24, value25, value26, value27, value28, value29, value30, value31, value32, value33, value34, value35, value36, value37, value38]
    dff = pd.DataFrame(
        columns=column_names,
        data=[vals]
    )
    prediction = pipeline.predict(dff)[0]
    return prediction


# @ app.callback(Output('output-data', component_property='figure'), [Input('d1', 'value'), Input('d11', 'value'), ])
# def update_visualization(dropdown1, dropdown2):
#     chart_layout = _generate_chart(dropdown1, dropdown2)
#     return chart_layout
