# Compare datasets of irrigated crop yield and Kayrokum lake volume and Geoid height
# Build regression models using train and test datasets
# Predict internal market price for 1 kg of rice

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\kachk\Documents\09 - Startups\Numiter\KayrokumCropYield\Kayrokum_volume.csv')

df['Start time'] = pd.to_datetime(df['Start time'])
df['Month'] = df['Start time'].apply(lambda x: x.month)

df_1 = df.loc[df['Month'] == 1]
df_2 = df.loc[df['Month'] == 2]
df_3 = df.loc[df['Month'] == 3]
df_4 = df.loc[df['Month'] == 4]
df_5 = df.loc[df['Month'] == 5]
df_6 = df.loc[df['Month'] == 6]
df_7 = df.loc[df['Month'] == 7]
df_8 = df.loc[df['Month'] == 8]
df_9 = df.loc[df['Month'] == 9]
df_10 = df.loc[df['Month'] == 10]
df_11 = df.loc[df['Month'] == 11]
df_12 = df.loc[df['Month'] == 12]


sns.distplot(df_1['Value'], bins=15)
sns.distplot(df_2['Value'], bins=15)
sns.distplot(df_3['Value'], bins=15)
sns.distplot(df_4['Value'], bins=15)
sns.distplot(df_5['Value'], bins=15)
sns.distplot(df_6['Value'], bins=15)
sns.distplot(df_7['Value'], bins=15)
sns.distplot(df_8['Value'], bins=15)
sns.distplot(df_9['Value'], bins=15)
sns.distplot(df_10['Value'], bins=15)
sns.distplot(df_11['Value'], bins=15)
sns.distplot(df_12['Value'], bins=15)

plt.legend(df['Month'].unique())

plt.show()