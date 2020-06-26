import dash_html_components as html
from layouts.inputs import layout_inputs
from layouts.visualization import layout_visualization
from server import app

# Main Layout (Two columns: Inputs / Chart)
main_layout = html.Div([
    html.Div([
        html.Div(html.Img(src=('https://static.tildacdn.com/tild6265-3631-4632-a566-316135646639/ta_logo_white2x.png'),
                          style={'height': 'auto', 'width': '180px', 'object-fit': "cover", 'background-color': 'black'})),
        # html.Div([
        #     html.H1("TraceAir")
        # ]),
    ], className="row", style={"justify-content": "flex-start"}),
    html.Br(),
    html.Div(layout_inputs),
    html.Div(layout_visualization)
], className="container")
