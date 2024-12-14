import pandas as pd

# function to load a dataset
def load_data(dataset, path):
    return pd.read_csv(f"../data/{path}/" + dataset)


# function to load a dataset from root directory
def load_data_root(dataset, path):
    return pd.read_csv(f"data/{path}/" + dataset)

# function to save a dataset to the processed folder
def save_data(df, name):
    df.to_csv("../data/processed/" + name, index=False)
    
# function to save a dataset to the processed folder from the root directory
def save_data_root(df, name):
    df.to_csv("data/processed/" + name, index=False)


