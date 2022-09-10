import pandas as pd
import os, sys
import streamlit as st

sys.path.append(os.path.abspath(os.path.join('../scripts')))
from log import get_logger
from db_script import DBScript
db = DBScript()

def make_prediction(page=None):
    train = pd.read_sql('select * from pharmaceuticalData', db.get_engine())
    train.reset_index(drop=True)
    train.drop('index',axis =1, inplace=True)
    train.set_index('Date',inplace=True)

    # to be continued