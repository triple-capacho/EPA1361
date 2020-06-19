import numpy as np
import scipy as sp
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import networkx as nx

# Aggregate a data frame with selected columns and return a dataframe
def agg(df,name_list):
    for i in name_list:
        list = df.filter(like = i).columns
        df['Total'+" "+ i] = df[list].sum(axis=1)
        df.drop(columns = list, inplace = True)
    return df

def plot_sob (Si_df, ax):
    sns.set_style('white')

    indices = Si_df[['S1','ST']]
    err = Si_df[['S1_conf','ST_conf']]
    #fig.set_size_inches(12,8)
    indices.plot.bar(yerr=err.values.T,ax=ax)   