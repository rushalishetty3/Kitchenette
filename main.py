import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

from charts.bar_chart1 import BarChart1
from charts.bar_chart2 import BarChart2
from charts.box_plot import BoxPlot
from charts.word_cloud import Wordcloud
from charts.recommendation import Recommendation
from dataset.data import data

class container:
    layout = html.Div(children=[
    html.H1(children='All Recipes'),

    html.Br(),

    html.Div(children=[
        html.Div(children=[
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H3('Rating Distribution (Box Plot)'),
                        BoxPlot.fig
                    ]
                )
            )
        ], className="col1 shadow p-3 mb-5 bg-white rounded"),

        html.Div(children=[
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H3('Recipe Count (Bar Graph)'),
                        BarChart1.fig
                    ]
                )
            )
        ], className="col2 shadow p-3 mb-5 bg-white rounded"),
    ], className="row"),

    html.Br(),
    html.Br(),

    html.Div(children=[
        dbc.Card(
            dbc.CardBody(
                [
                    html.H3("WORD CLOUD"),
                    html.Img(src=Wordcloud.fig)
                ]
            )
        )
    ], className="col2 shadow p-3 mb-5 bg-white rounded"),

    html.Br(),
    html.Br(),

    html.Div(children=[
        html.Div(children=[
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H3('Nutrients comparison among two recipes and daily intake'),
                        BarChart2.fig
                    ]
                )
            )
        ], className="col1 shadow p-3 mb-5 bg-white rounded"),
    ]),

    html.Br(),
    html.Br(),

    html.Div(children=[
        html.Div(children=[
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H3('Alternate Recipe Recommendation'),
                        Recommendation.fig
                    ]
                )
            )
        ], className="col1 shadow p-3 mb-5 bg-white rounded"),
    ]),

], className="container")