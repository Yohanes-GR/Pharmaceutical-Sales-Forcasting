import sys
import os
import sys
from matplotlib import testing
import numpy as np
import pandas as pd
import streamlit as st

# import sys, os
# sys.path.append(os.path.abspath(os.path.join('../scripts')))

def storeDataLoad():
    df = pd.read_csv("../data/store.csv")
    return df


def trainingDataLoad():
    df = pd.read_csv("../data/train.csv", low_memory=False)
    return df


def testingDataLoad():
    df = pd.read_csv("../data/test.csv")
    return df


def app():
    st.title('Pharmaceutical Sales Prediction Across Multiple Stores')

    st.header('Table Description')
    st.markdown(
    '''
       The Pharmaceutical Supplemental Information About the Stores
    ''')
    df = storeDataLoad()
    st.write(df, width=1200)

    st.header('Training Sample Data')
    st.markdown(
    '''
       The Training Historical data Including Sales
    ''')
    df = trainingDataLoad()
    st.write(df.head(10))

    st.header('Testing Sample Data')
    st.markdown(
    '''
       The Historical Testing Data Excluding Sales
    ''')
    df = testingDataLoad()
    st.write(df.head(10))
