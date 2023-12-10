"""
This is a boilerplate pipeline 'preprocessing'
generated using Kedro 0.18.14
"""
import pandas as pd 

def clean_data(raw:pd.DataFrame)-> pd.DataFrame:
    l1 = raw.drop(['Unnamed: 0','preciptype' ,'Stop Number', 'Route Destination','Day Type','Scheduled Time','date_key','id','precip_ind'],axis = 1)
    return l1

def onh_encoder(data: pd.DataFrame) -> pd.DataFrame:
    pass


def split_data(raw:pd.DataFrame) -> pd.DataFrame:
    clean_raw = clean_data(raw)
    names = clean_raw.loc[:,"Route Name"].unique()
    route1 = clean_raw.loc[raw.loc[:,"Route Name"] == names[0],:]
    route2 = clean_raw.loc[raw.loc[:,"Route Name"] == names[1],:]
    return route1,route2



def lag_values(inter:pd.DataFrame) ->pd.DataFrame:
    inter['lag1'] = inter.Deviation.shift(1)
    inter['lag2'] = inter.Deviation.shift(2)
    inter = inter.dropna().reset_index()
    inter_name = inter.loc[0,'Route Name']
    inter = inter.drop("Route Name",axis = 1)
    return inter

