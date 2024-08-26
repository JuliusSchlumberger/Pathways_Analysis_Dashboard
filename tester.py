from dash import Dash, dcc, html, Input, Output, MATCH, ALL
import dash

app = Dash(__name__)

app.layout = html.Div([
    dcc.Input(id={'type': 'dynamic-input', 'index': 1}, value=''),
    dcc.Input(id={'type': 'dynamic-input', 'index': 2}, value=''),
    html.Div(id='output')
])

@app.callback(
    Output('output', 'children'),
    [Input({'type': 'dynamic-input', 'index': ALL}, 'value')]
)
def update_output(values):
    ctx = dash.callback_context
    triggered_id = ctx.triggered[0]['prop_id'].split('.')[0]
    print(type(triggered_id))
    try:
        triggered_id = eval(triggered_id)
    except:
        pass

    if isinstance(triggered_id, dict):
        if triggered_id['index'] == 2:
            return "he's a clown"
        else:
            return "he's a prince"
    return f'Input values: {values}'

if __name__ == '__main__':
    app.run_server(debug=True)
