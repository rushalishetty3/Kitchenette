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
    [Input(component_id='bar_dropdown1', component_property='value'),Input(component_id='bar_dropdown2', component_property='value'),Input(component_id='bar_dropdown3', component_property='value')]
)
def update_barchart(selected_value1,selected_value2,selected_value3):
    nutrients = selected_value3
    category = [selected_value1, selected_value2]

    daily_nutrients_intake = {
        'carbohydrates_g' : 260,
        'sugars_g' : 90,
        'fat_g' : 70,
        'protein_g' : 50,
        'dietary_fiber_g' : 25,
        'sodium_mg' : 2300,
        'calcium_mg' : 1000,
        'iron_mg' : 14.8,
        'magnesium_mg' : 400,
        'potassium_mg' : 4700,
    }

    daily_dose = []
    for x in nutrients:
        if(x.endswith('mg')):
            daily_dose.append(daily_nutrients_intake[x]/1000)
        else: 
            daily_dose.append(daily_nutrients_intake[x])

    dict_temp = dict(map((lambda x: (x,'mean')), nutrients))
    dict_temp['name'] = 'count'

    bar_data = data.df.groupby("category").agg(dict_temp).reset_index()
    bar_data = bar_data[bar_data['name']>100]

    category_nutrients = []

    for x in category:
        category_data = bar_data[bar_data['category']==x]
        temp = []
        for y in nutrients:
            if(y.endswith('mg')):
                temp.append(float(category_data[y].to_string(index=False))/1000)
            else:
                temp.append(float(category_data[y].to_string(index=False)))
        
        category_nutrients.append(temp)

    figure = go.Figure(data=[
        go.Bar(name=category[0], x=nutrients, y=category_nutrients[0]),
        go.Bar(name=category[1], x=nutrients, y=category_nutrients[1]),
        go.Bar(name='daily intake', x=nutrients, y=daily_dose)
    ])

    return figure

if __name__ == '__main__':
    app.run_server(debug=True)