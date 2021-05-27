import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd
from dash.dependencies import Input, Output

from charts.bar_chart1 import BarChart1
from charts.bar_chart2 import BarChart2
from charts.bar_chart3 import BarChart3
from charts.box_plot import BoxPlot
from charts.word_cloud import Wordcloud
from dataset.data import data

class container:
    layout = html.Div(children=[
    html.H1(children='All Recipes'),

    html.Div(children='''
        Charts
    '''),

    html.Br(),

    html.Div(children=[
        html.Div(children=[
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H3('BOX PLOT'),
                        BoxPlot.fig
                    ]
                )
            )
        ], className="col1 shadow p-3 mb-5 bg-white rounded"),

        html.Div(children=[
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H3('BAR CHART'),
                        BarChart2.fig
                    ]
                )
            )
        ], className="col2 shadow p-3 mb-5 bg-white rounded"),
    ], className="row"),

    html.Br(),
    html.Br(),

    html.Div(children=[
        html.Div(children=[
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H3('BAR CHART'),
                        BarChart1.fig
                    ]
                )
            )
        ], className="col1 shadow p-3 mb-5 bg-white rounded"),

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
    ], className="row"),

    html.Br(),
    html.Br(),

    html.Div(children=[
        html.Div(children=[
            dbc.Card(
                dbc.CardBody(
                    [
                        html.H3('BAR CHART'),
                        BarChart3.fig
                    ]
                )
            )
        ], className="col1 shadow p-3 mb-5 bg-white rounded"),
    ]),

], className="container")