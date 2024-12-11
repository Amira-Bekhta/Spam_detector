import pandas as pd

def load_data(dataset, path):
    return pd.read_csv(f"../data/{path}/" + dataset)

def save_data(df, name):
    df.to_csv("../data/processed/" + name, index=False)