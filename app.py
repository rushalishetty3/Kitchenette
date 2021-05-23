# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from dash.dependencies import Input, Output

from main import container
from dataset.data import data

app = dash.Dash(__name__,prevent_initial_callbacks=True,external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = container.layout

#interactive bar chart
@app.callback(
    Output(component_id='bar_graph2', component_property='figure'),
    [Input(component_id='bar_dropdown1', component_property='value'),Input(component_id='bar_dropdown2', component_property='value')]
)
def update_barchart(selected_value1,selected_value2):
    nutrients = ['carbohydrates_g', 'sugars_g', 'fat_g']
    category = [selected_value1, selected_value2]

    bar_data = data.df.groupby("category").agg({'name':'count',nutrients[0]:'mean',nutrients[1]:'mean',nutrients[2]:'mean'}).reset_index()
    bar_data = bar_data[bar_data['name']>100]

    category_nutrients = []

    for x in category:
        category_data = bar_data[bar_data['category']==x]
        temp = []
        for y in nutrients:
            temp.append(category_data[y].to_string(index=False))
        temp = [float(i) for i in temp]
        category_nutrients.append(temp)

    figure = go.Figure(data=[
        go.Bar(name=category[0], x=nutrients, y=category_nutrients[0]),
        go.Bar(name=category[1], x=nutrients, y=category_nutrients[1])
    ])

    return figure

if __name__ == '__main__':
    app.run_server(debug=True)