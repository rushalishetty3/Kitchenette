import pandas as pd


class data:
    df = pd.read_csv("test-crawl8.csv")

    nutrients_df = pd.read_csv("nutrients.csv")

    stats = {
        'total_recipes': len(df),
        'total_authors': df['author'].nunique(),
        'total_reviews': df['review_count'].nunique(),
        'total_ratings': df['rating_count'].nunique(),
        'total_categories': df['category'].nunique(),
    }
