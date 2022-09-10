import sys
import os
import sys
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import testing
import numpy as np
import pandas as pd
import streamlit as st

sys.path.append(os.path.abspath(os.path.join('../scripts'))) 
from plots import Plots

def compare_test_train(train_data, test_data, feature, title):
    fig, ax = plt.subplots(1, 2, sharex=True, figsize=(12, 4))
    ax[0].set_title("Train " + title)
    sns.countplot(x=feature, data=train_data, ax=ax[0])
    ax[1].set_title("Test " + title)
    sns.countplot(x=feature, data=test_data, ax=ax[1])
    fig.subplots_adjust(wspace=0.3)
    # fig.show()


# def storeDataLoad():
#     df = pd.read_csv("../data/store.csv")
#     return df


def trainingDataLoad():
    df = pd.read_csv("../data/cleaned_train.csv")
    return df


def testingDataLoad():
    df = pd.read_csv("../data/cleaned_test.csv")
    return df


def transform_date(df):
     
    df['Month'] = pd.DatetimeIndex(df['Date']).month 
    return df


def app():

    promo = ["Not participating", "Participating"]
    train_data = trainingDataLoad()
    test_data = testingDataLoad()

    st.title('Pharmaceutical Sales Prediction Across Multiple Stores')
    
    st.header('Table Description')
    st.markdown(
    '''
       The Pharmaceutical Supplemental Information About the Stores
    ''')
    # train_data["Promo"] = train_data["Promo"].apply(lambda x: promo[x])
    # test_data["Promo"] = test_data["Promo"].apply(lambda x: promo[x])
    # compare_test_train(train_data, test_data, 'Promo', 'Promotion Count')

    df = transform_date(train_data.copy())
    sns.factorplot(data = df, x ="Month", y = "Sales",
               hue = 'Promo',
              sharex=False)