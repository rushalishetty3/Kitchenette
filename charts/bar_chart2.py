import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from dataset.data import data


class BarChart2:
    recipe_list = data.df['name'].unique()

    recipe_list_dict = []
    for x in recipe_list:
        recipe_list_dict.append({'label': x, 'value': x})

    nutrients = ['carbohydrates_g', 'sugars_g', 'fat_g']
    recipes = [recipe_list[0], recipe_list[1]]

    nutrients_df = data.nutrients_df
    daily_nutrients_intake = dict(
        zip(nutrients_df['nutrients'], nutrients_df['value']))

    daily_dose = []
    for x in nutrients:
        if(x.endswith('mg')):
            daily_dose.append(daily_nutrients_intake[x]/1000)
        else:
            daily_dose.append(daily_nutrients_intake[x])

    recipe_nutrients = []
    for x in recipes:
        recipe_data = data.df[data.df['name'] == x]
        temp = []
        for y in nutrients:
            temp.append(recipe_data[y].to_string(index=False))
        temp = [float(i) for i in temp]
        recipe_nutrients.append(temp)

    figure = go.Figure(data=[
        go.Bar(name=recipes[0], x=nutrients, y=recipe_nutrients[0]),
        go.Bar(name=recipes[1], x=nutrients, y=recipe_nutrients[1]),
        go.Bar(name='daily intake', x=nutrients, y=daily_dose)
    ])

    fig = html.Div(children=[
        html.Div(children=[
            dcc.Dropdown(
                id='bar_dropdown1',
                options=recipe_list_dict,
                optionHeight=25,
                value=recipe_list[0],
                disabled=False,
                multi=False,
                searchable=True,
                search_value='',
                placeholder='Select...',
                clearable=True,
                # style = { 'width' : "95%" },
            ),
            dcc.Dropdown(
                id='bar_dropdown2',
                options=recipe_list_dict,
                optionHeight=25,
                value=recipe_list[1],
                disabled=False,
                multi=False,
                searchable=True,
                search_value='',
                placeholder='Select...',
                clearable=True,
                # style = { 'width' : "95%" }
            ),
        ], className="row"),

        html.Br(),

        dcc.Dropdown(
            id='bar_dropdown3',
            options=[
                {'label': 'Carbohydrate', 'value': 'carbohydrates_g'},
                {'label': 'Sugar', 'value': 'sugars_g'},
                {'label': 'Fat', 'value': 'fat_g'},
                {'label': 'Protein', 'value': 'protein_g'},
                {'label': 'Sodium', 'value': 'sodium_mg'},
                {'label': 'Calcium', 'value': 'calcium_mg'},
                {'label': 'Iron', 'value': 'iron_mg'},
                {'label': 'Magnesium', 'value': 'magnesium_mg'},
                {'label': 'Potassium', 'value': 'potassium_mg'},
                {'label': 'Cholestrol', 'value': 'cholesterol_mg'},
                {'label': 'Zinc', 'value': 'zinc_mg'},
                {'label': 'Phosphorous', 'value': 'phosphorus_mg'},
            ],
            optionHeight=25,
            value=nutrients,
            disabled=False,
            multi=True,
            searchable=True,
            search_value='',
            placeholder='Select...',
            clearable=False,
            style={'width': "95%"}
        ),

        html.Br(),
        dcc.Graph(
            id='bar_graph2',
            figure=figure
        )
    ])
