import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt
from plotly.tools import mpl_to_plotly
from wordcloud import WordCloud  
import io
import base64
import random

from dataset.data import data

class Wordcloud:
    word_data = data.df[['name','rating','rating_count']]
    word_data['rating_product'] = word_data.rating.mul(word_data.rating_count)
    word_data_top = word_data.sort_values('rating_product',ascending=False)

    def orange_color_func(word, font_size, position, orientation, random_state=None,**kwargs):
        return "hsl(%d, 100%%, 60%%)" % random.randint(20, 55)

    stopword_list = ['Best', 'Flavor', 'Flavour', 'With', 'Chef', 'John', 'I', 'II', 'III', 'Easy', 'Slow', 'and']
    word_data_str = word_data_top['name'].str.cat(sep=',')
    top_wordcloud = WordCloud(max_font_size= 50, background_color='white',prefer_horizontal = 0.7, stopwords = stopword_list).generate(word_data_str)
    
    # top keywords in recipe name
    plt.figure()
    plt.imshow(top_wordcloud.recolor(color_func = orange_color_func, random_state = 3), interpolation='bilinear')
    plt.axis('off')

    buf = io.BytesIO()
    plt.savefig(buf, format = "png")
    plt.close()
    data = base64.b64encode(buf.getbuffer()).decode("utf8") 
    fig = "data:image/png;base64,{}".format(data)