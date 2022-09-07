import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import sys, os
from pandas.plotting import scatter_matrix
sys.path.append(os.path.abspath(os.path.join('../scripts')))
from log_config import logger
def plot_hist(df: pd.DataFrame, column: str, color: str) -> None:
    plt.figure(figsize=(9, 7))
    sns.displot(data=df, x=column, color=color, kde=True, height=7, aspect=2)
    plt.title(f'Distribution of {column}', size=20, fontweight='bold')
    logger.info('Plotting a histogram')

    plt.show()


def plot_dist(df: pd.DataFrame, column: str):
    plt.figure(figsize=(9, 7))
    sns.distplot(df).set_title(f'Distribution of {column}')
    logger.info('Plotting using plot dist')

    plt.show()


def plot_count(df: pd.DataFrame, column: str) -> None:
    plt.figure(figsize=(12, 7))
    sns.countplot(data=df, x=column)
    plt.title(f'Plot count of {column}', size=20, fontweight='bold')
    logger.info('Plotting using plot count')

    plt.show()


def plot_bar(df: pd.DataFrame, x_col: str, y_col: str, title: str, xlabel: str, ylabel: str) -> None:
    plt.figure(figsize=(9, 7))
    sns.barplot(data=df, x=x_col, y=y_col)
    plt.title(title, size=20)
    plt.xticks(rotation=75, fontsize=14)
    plt.yticks(fontsize=14)
    plt.xlabel(xlabel, fontsize=16)
    plt.ylabel(ylabel, fontsize=16)
    logger.info('Plotting a plot_bar')

    plt.show()


def plot_heatmap(df: pd.DataFrame, title: str, cbar=False) -> None:
    plt.figure(figsize=(12, 7))
    sns.heatmap(df, annot=True, cmap='viridis', vmin=0,
                vmax=1, fmt='.2f', linewidths=.7, cbar=cbar)
    plt.title(title, size=18, fontweight='bold')
    logger.info('Plotting a plot_heatmap')

    plt.show()


def plot_box(df: pd.DataFrame, x_col: str, title: str) -> None:
    plt.figure(figsize=(12, 7))
    sns.boxplot(data=df, x=x_col)
    plt.title(title, size=20)
    plt.xticks(rotation=75, fontsize=14)
    logger.info('Plotting a plot_box')
    plt.show()


def plot_box_multi(df: pd.DataFrame, x_col: str, y_col: str, title: str) -> None:
    plt.figure(figsize=(12, 7))
    sns.boxplot(data=df, x=x_col, y=y_col)
    plt.title(title, size=20)
    plt.xticks(rotation=75, fontsize=14)
    plt.yticks(fontsize=14)
    logger.info('Plotting a plot_box_multi')
    plt.show()


def plot_scatter(df: pd.DataFrame, x_col: str, y_col: str, title: str, hue: str, style: str) -> None:
    plt.figure(figsize=(10, 8))
    sns.scatterplot(data=df, x=x_col, y=y_col, hue=hue, style=style)
    plt.title(title, size=20)
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    logger.info('Plotting a plot_scatter')

    plt.show()
def heatmap(df,title='', annot=True):
  #setup()
  plt.title(title)
  correlation = df.corr()
  sns.heatmap(correlation,square = True, linewidths = .5, cmap = "BuPu", annot=annot)
  logger.info('Plotting a heatmap')
  return
#subplot
def plot_subplots(self, x: str, y: str, xtitle: str, ytitle: str) -> None:
    sns.set(style="whitegrid")
    fig, axes = plt.subplots(nrows=1, ncols=2)
    fig.set_size_inches(25, 8)
    x.hist(ax=axes[0], alpha=0.3, color='red', bins=20)
    y.hist(ax=axes[1], alpha=0.3, color='blue', bins=20)
    axes[0].set_title(xtitle, size=20)
    axes[1].set_title(ytitle, size=20)
    logger.info('Plotting a subplots')
    plt.show()