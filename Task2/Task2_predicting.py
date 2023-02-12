import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

def read_data(path: str) -> pd.DataFrame:
    return pd.read_json(path, orient='split').T.reset_index()

def split_data(data: pd.DataFrame, testing_data_size_precent: float) -> (pd.DataFrame, pd.DataFrame):
    size = len(data.index)
    point = int(size * testing_data_size_precent)
    return data[data.index < point], data[data.index >= point]

def train(reg: LinearRegression, poly: PolynomialFeatures, data: pd.DataFrame, currency: str) -> None:
    X = data.index.to_frame().to_numpy()
    Y = data[currency].to_numpy()
    X_poly = poly.fit_transform(X)
    reg.fit(X_poly, Y)

def predict(reg: LinearRegression, poly: PolynomialFeatures, indexes: pd.Series) -> np.array:
    X = indexes.to_frame().to_numpy()
    X_poly = poly.fit_transform(X)
    return reg.predict(X_poly).reshape(-1, 1)

df = read_data("data.json")
training_df, testing_df = split_data(df, 0.8)

poly = PolynomialFeatures(degree=2)
reg = LinearRegression()

train(reg, poly, training_df, 'EUR')
prediction = predict(reg, poly, df.index)

df['predicted'] = prediction

df[['EUR', 'predicted']].plot()