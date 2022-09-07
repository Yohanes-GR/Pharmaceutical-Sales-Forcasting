# data visualization
import matplotlib.pyplot as plt
import seaborn as sns # advanced vizs

def setup():
  plt.figure(figsize=(12,6))

def bar(x, y, title=''):
  setup()
  plt.title(title)
  sns.barplot(x=x, y=y)
  plt.show()
  return
  

def scatter(df, x, y, title=''):
  setup()
  plt.title(title)
  sns.scatterplot(data=df, x=x, y=y)
  plt.show()
  return

def heatmap(df,title='', annot=True):
  setup()
  plt.title(title)
  correlation = df.corr()
  sns.heatmap(correlation,square = True, linewidths = .5, cmap = "BuPu", annot=annot)
  return
