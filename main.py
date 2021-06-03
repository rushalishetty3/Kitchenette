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
    layout = html.Div([
        html.Div([
            html.Div([
                html.Div([
                    html.Span(["42069"], className="statbox-value"), #data
                    html.Span(["Recipes"], className="statbox-title")
                ], 
                className="statbox"),
                
                html.Div([
                    html.Span(["738"], className="statbox-value"), #data
                    html.Span(["Authors"], className="statbox-title"),
                    # html.Span("face", className = 'material-icons')
                ], 
                className="statbox"),

                html.Div([
                    html.Span(["8975"], className="statbox-value"), #data
                    html.Span(["Ratings"], className="statbox-title")
                ], className="statbox"),
                html.Div([
                    html.Span(["45"], className="statbox-value"), #data
                    html.Span(["Nutrients"], className="statbox-title")
                ], 
                className="statbox"),

                html.Div([
                    html.Span(["69"], className="statbox-value"), #data
                    html.Span(["Nice"], className="statbox-title")
                ], 
                className="statbox"),
            ], 
            className="statbox-container"),

            html.Div([
                html.Div([
                    html.H1("Rating Kebabs"),
                    BoxPlot.fig
                ],
                className="graphbox"),
                
                html.Div([
                    html.H1("Big Bars"),
                    BarChart1.fig
                ],
                className="graphbox"),
            ],
            className="graph-container"),

            html.Div([            
                html.Div([
                    html.H2("Recipe Recommender"),
                    Recommendation.fig
                ],className="recommendbox"),
            ],
            className="recommend-container"),

        ],className="actualcontent")
    ], className="wholedamnpage")
