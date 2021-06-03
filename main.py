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
            html.Span([
                "Kitchenette"
            ], className="projectname"),

            html.Div([
                html.Div([
                    html.Span([data.stats['total_recipes']],
                              className="statbox-value"),  # data
                    html.Span(["Recipes"], className="statbox-title")
                ], className="statbox"),

                html.Div([
                    html.Span([data.stats['total_authors']],
                              className="statbox-value"),  # data
                    html.Span(["Authors"], className="statbox-title"),
                    # html.Span("face", className = 'material-icons')
                ], className="statbox"),

                html.Div([
                    html.Span([data.stats['total_ratings']],
                              className="statbox-value"),  # data
                    html.Span(["Ratings"], className="statbox-title")
                ], className="statbox"),

                html.Div([
                    html.Span([data.stats['total_categories']],
                              className="statbox-value"),  # data
                    html.Span(["Categories"], className="statbox-title")
                ], className="statbox"),

                html.Div([
                    html.Span([data.stats['total_reviews']],
                              className="statbox-value"),  # data
                    html.Span(["Reviews"], className="statbox-title")
                ],
                    className="statbox"),
            ],
                className="statbox-container"),

            html.Div([
                html.Div([
                    html.H1("Rating per category"),
                    BoxPlot.fig
                ],
                    className="graphbox"),

                html.Div([
                    html.H1("Recipes per category"),
                    BarChart1.fig
                ],
                    className="graphbox"),

                html.Div([
                    html.H1("Word cloud"),
                    html.Img(src=Wordcloud.fig)
                ],
                    className="graphbox"),

                html.Div([
                    html.H1(
                        "Daily intake tracker"),
                    html.P(
                        "Compare the nutritional values of recipes against the daily intake"),
                    BarChart2.fig
                ],
                    className="graphbox barchart2"),
            ],
                className="graph-container"),

            html.Div([
                html.Div([
                    html.H1("Recipe Recommender"),
                    Recommendation.fig
                ], className="recommendbox"),
            ],
                className="recommend-container"),

        ], className="actualcontent")
    ], className="wholedamnpage")
