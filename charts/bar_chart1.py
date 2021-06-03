import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from dataset.data import data

class BarChart1:
    bar_data = data.df.groupby("category").agg({'name':'count'}).reset_index()
    bar_data = bar_data.rename(columns = {'name':'number of recipes'})
    bar_data = bar_data.sort_values(['number of recipes'], ascending=[True])

    #category vs no of recipes
    fig = html.Div(children=[
        dcc.Graph(
            id='bar_graph1',
            figure=px.bar(
                data_frame=bar_data[bar_data['number of recipes']>100], 
                x="number of recipes", 
                y="category", 
                orientation= "h",
                width=600,
                )
        )
    ])