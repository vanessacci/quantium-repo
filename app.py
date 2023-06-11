# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

colors = {
    'background': '#8ecae6',
    'text': '#fb8500'
}

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('data_sales_data_pink_morsel.csv')

fig = px.line(df, x="date", y="sales", title='Daily Sales of Pink Morsels')
fig.update_layout(
    title={'x': 0.5},
    plot_bgcolor='#edf6f9',
    paper_bgcolor='#edf6f9',
    yaxis_range=[0, 3000],
    font_color='#006d77',
    font={'family': 'Arial'}
)
fig.update_traces(line_color='#e29578')

app.layout = html.Div(
    style={'backgroundColor': '#edf6f9', 'fontFamily': 'Arial'},
    children=[html.H1(
        style={'color': '#006d77'},
        children="Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?"),

        html.Div(style={'color': '#006d77'}, children='''
           The answer is obvious...YES!!
        '''),

        dcc.Graph(
            id='pink-morsel-sale',
            figure=fig
        )
    ])

if __name__ == '__main__':
    app.run_server(debug=True)