import pandas as pd

def not_boring_movies(cinema: pd.DataFrame) -> pd.DataFrame:
    return cinema.query("description != 'boring' & id % 2 != 0").sort_values("rating", ascending=False)
    