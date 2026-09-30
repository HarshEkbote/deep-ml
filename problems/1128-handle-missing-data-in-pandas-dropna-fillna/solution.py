import pandas as pd

def solution(df):
    df=df.loc[:, df.isnull().mean()<=0.5]
    df=df.loc[df.isnull().mean(axis=1)<=0.5,:]

    numeric_cols=df.select_dtypes(include=["number"]).columns
    other_cols=df.select_dtypes(include=["string","object"]).columns

    df[numeric_cols]=df[numeric_cols].fillna(df[numeric_cols].mean())
    for col in other_cols:
        if not df[col].mode().empty:
            df[col]=df[col].fillna(df[col].mode()[0])
    
    df=df.reset_index(drop=True)
    return df