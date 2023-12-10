"""
This is a boilerplate pipeline 'modeling'
generated using Kedro 0.18.14
"""
import logging
from typing import Dict,Tuple

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score    
from sklearn.model_selection import train_test_split

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


def split_data(data:pd.DataFrame,parameters:Dict) -> Tuple:
    x = data[parameters["features"]]
    y = data[parameters["target"]]

    x_train,x_test,y_train,y_test = train_test_split(
        x,y,test_size = parameters["test_size"],random_state = parameters["random_state"]
    )
    return x_train,x_test,y_train,y_test


def train_model(x_train:pd.DataFrame,y_train:pd.Series) -> LinearRegression:

    cat_cols = ['name','hour']
    num_cols = ['windspeed', 'precip', 'Total', 'lag1', 'lag2']
    enc = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
    scaler = StandardScaler()
    transformer = ColumnTransformer([('ohe', enc, cat_cols),
                                ('num',scaler,num_cols)])

    model = LinearRegression()

    pipe = Pipeline([('trans',transformer),
                ('model',model)
                ])

    pipe.fit(x_train,y_train)
    return pipe

def evaluate_model(model: LinearRegression,x_test:pd.DataFrame,y_test:pd.DataFrame):
    y_pred = model.predict(x_test)
    score = r2_score(y_test,y_pred)
    logger = logging.getLogger(__name__)
    logger.info("Model has the coefficient R^2 of %.3f on test data." %score) 
    x_test['target'] = y_test
    x_test['pred'] = y_pred
    return x_test