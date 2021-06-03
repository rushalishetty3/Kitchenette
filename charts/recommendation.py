import pandas as pd
import itertools
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

from dataset.data import data

class Recommendation:
    recipe_list = data.df['name'].unique()

    recipe_list_dict = []
    for x in recipe_list:
        recipe_list_dict.append({'label' : x, 'value' : x})

    def score_cal(name_of_recipe):
        temp_df = data.df[data.df['name']==name_of_recipe]
        category = temp_df['category'].item()

        # get data of recipes in same category
        category_df = data.df[data.df['category']==category].reset_index()
        category_df = category_df[['name','ingredients','rating','calories']]

        category_df.dropna(inplace=True)
        tf = TfidfVectorizer(analyzer='word', ngram_range=(1, 3), min_df=0, stop_words='english')
        matrix = tf.fit_transform(category_df['ingredients'])

        cosine_similarities = linear_kernel(matrix,matrix)

        indices = pd.Series(category_df.index, index=category_df['name'])
        idx = indices[name_of_recipe]

        # sim_scores - (index,cosine value)
        sim_scores = list(enumerate(cosine_similarities[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[0:11]

        recipe_indices = [i[0] for i in sim_scores]

        sim_df = category_df.iloc[recipe_indices]

        sim_df = sim_df.set_index('name')
        sim_df = sim_df[['rating', 'calories']]

        rating = sim_df.loc[name_of_recipe]['rating']
        calories = sim_df.loc[name_of_recipe]['calories']

        sim_df = sim_df.drop(name_of_recipe)

        sim_df['score'] = 0.4*(sim_df['rating']/rating) + 0.6*(calories/sim_df['calories'])
        sim_df = sim_df.sort_values('score', ascending = False)

        sim_df = sim_df.reset_index()
        sim_df_merge = pd.merge(sim_df, data.df, on='name')
        sim_df_merge = sim_df_merge[['name','url','rating_x','calories_x']]

        return sim_df_merge, [rating,calories]

    sim_recipe_list = []

    fig = html.Div([
        html.Div([
            dcc.Dropdown(
                id = 'bar_dropdown7',
                options = recipe_list_dict,
                optionHeight = 25,
                value = '',
                disabled = False,
                multi = False,
                searchable = True,
                search_value = '',
                placeholder = 'Search a recipe!',
                clearable = True,
                style = { 'width' : "400px" },
            ),
        ]),

        html.Div(
            id="alternate_recipes",
            children=[
                sim_recipe_list
            ]
        )
    ])