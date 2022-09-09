import pandas as pd
import numpy as np
import seaborn as sns 
import streamlit as st
import matplotlib.pyplot as plt
from IPython.display import Image
import plotly.express as px
import plotly.io as pio
from plotly.subplots import make_subplots
import plotly.graph_objects as go  

class Plots:
    def __init__(self) -> None:
        pass

    def hist(self, df:pd.DataFrame, column:str, color:str)->None:
        plt.figure(figsize=(9, 7))
        sns.displot(data=df, x=column, color=color, kde=True, height=7, aspect=2)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        plt.show()


    def box_plot(self, df: pd.DataFrame, x_col: str, title: str)->None:
        plt.figure(figsize=(10, 5))
        sns.boxplot(data=df, x=x_col)
        plt.title(title, size=20)
        plt.xticks(fontsize=14)
        plt.show()


    def plot_scatter(self, df: pd.DataFrame, x_col: str, y_col: str, title: str, hue: str, style: str) -> None:
        plt.figure(figsize=(10, 8))
        sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue, style=style)
        plt.title(title, size=20)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.xlim(0, 10000)
        plt.ylim(0, 10000)
        plt.show()


    def heatmap(self, df, title='', annot=True): 
        plt.figure(figsize=(12,6))
        plt.title(title)
        correlation = df.corr()
        sns.heatmap(correlation,square = True, linewidths = .5, cmap = "BuPu", annot=annot)
        return
         

    def plot_bar(self, column, title, xlabel, ylabel):
        plt.figure(figsize=(10,5))
        sns.barplot(x=column.index, y=column.values) 
        plt.title(title, size=14, fontweight="bold")
        plt.xlabel(xlabel, size=13, fontweight="bold") 
        plt.ylabel(ylabel, size=13, fontweight="bold")
        plt.xticks(rotation=90)
        plt.show() 

    def mult_hist(self, sr, rows, cols, title_text, subplot_titles, interactive=False):
        fig = make_subplots(rows=rows, cols=cols, subplot_titles=subplot_titles)
        for i in range(rows):
            for j in range(cols):
                x = ["-> " + str(i) for i in sr[i+j].index]
                fig.add_trace(go.Bar(x=x, y=sr[i+j].values), row=i+1, col=j+1)
        fig.update_layout(showlegend=False, title_text=title_text)
        if(interactive):
            fig.show()
        else:
            return Image(pio.to_image(fig, format='png', width=1200))


    def plot_hist(self, df: pd.DataFrame, column: str, color: str) -> None:
        plt.figure(figsize=(9, 7))
        sns.displot(data=df, x=column, color=color, kde=True, height=7, aspect=2)
        plt.title(f'Distribution of {column}', size=20, fontweight='bold')
        plt.show()