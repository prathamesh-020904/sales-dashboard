import pandas as pd

def load_data(path):
    df = pd.read_csv(path, encoding="ISO-8859-1")
    df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])
    df["MONTH"] = df["ORDERDATE"].dt.strftime('%B')
    return df
