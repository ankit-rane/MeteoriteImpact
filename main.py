import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('dark_background')
import seaborn as sns
df = pd.read_csv('nasa.csv')
df.head()
df.shape
df.info()
df = df.drop(['Neo Reference ID', 'Name', 'Orbit ID', 'Close Approach Date', 'Epoch Date Close Approach', 'Orbit Determination Date'] , axis = 1)
df.head()
hazardous_labels = pd.get_dummies(df['Hazardous'])
hazardous_labels