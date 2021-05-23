import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from dataset.data import data

class BoxPlot:
    # box_df  = data.df.groupby("category").agg({'rating' : ['mean','median'], 'rating_count' : 'count'})
    # box_df = box_df.reset_index()
    # box_df.columns = ['category','mean_rating','median_rating','rating_count']
    # box_df = box_df[box_df['rating_count']>1000].reset_index()
    # box_df = box_df.sort_values('mean_rating',ascending=False)
    # print(box_df)

    # category vs rating
    fig = html.Div(children=[
        dcc.Graph(
            id='box_plot',
            figure=px.box(data.df[data.df['rating_count']>1000],x="rating",y="category",
                            orientation='h',height=600, width=500)
        )
    ])