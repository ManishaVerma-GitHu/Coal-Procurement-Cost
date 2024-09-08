# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 23:52:22 2024

@author: Manisha
"""

import pandas as pd
import numpy as np
df = pd.read_csv("C:/Users/Manisha/Downloads/merged_economic_data.csv")

## FIRST BUSINESS DECISION 
## MEAN , MEDIAN ,MODE

mean = df['Coal_RB_4800_FOB_London_Close_USD'].mean()
median = df['Coal_RB_4800_FOB_London_Close_USD'].median()
mode = df['Coal_RB_4800_FOB_London_Close_USD'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['Coal_RB_5500_FOB_London_Close_USD'].mean()
median = df['Coal_RB_5500_FOB_London_Close_USD'].median()
mode = df['Coal_RB_5500_FOB_London_Close_USD'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['Coal_RB_5700_FOB_London_Close_USD'].mean()
median = df['Coal_RB_5700_FOB_London_Close_USD'].median()
mode = df['Coal_RB_5700_FOB_London_Close_USD'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].mean()
median = df['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].median()
mode = df['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['Coal_India_5500_CFR_London_Close_USD'].mean()
median = df['Coal_India_5500_CFR_London_Close_USD'].median()
mode = df['Coal_India_5500_CFR_London_Close_USD'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['Price_WTI'].mean()
median = df['Price_WTI'].median()
mode = df['Price_WTI'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['Price_Brent_Oil'].mean()
median = df['Price_Brent_Oil'].median()
mode = df['Price_Brent_Oil'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['Price_Dubai_Brent_Oil'].mean()
median = df['Price_Dubai_Brent_Oil'].median()
mode = df['Price_Dubai_Brent_Oil'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['Price_ExxonMobil'].mean()
median = df['Price_ExxonMobil'].median()
mode = df['Price_ExxonMobil'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['Price_NTPC'].mean()
median = df['Price_NTPC'].median()
mode = df['Price_NTPC'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['Price_Shenhua'].mean()
median = df['Price_Shenhua'].median()
mode = df['Price_Shenhua'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['tempmax_RB'].mean()
median = df['tempmax_RB'].median()
mode = df['tempmax_RB'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['tempmax_RB'].mean()
median = df['tempmax_RB'].median()
mode = df['tempmax_RB'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['tempmin_RB'].mean()
median = df['tempmin_RB'].median()
mode = df['tempmin_RB'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['temp_RB'].mean()
median = df['temp_RB'].median()
mode = df['temp_RB'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['dew_RB'].mean()
median = df['dew_RB'].median()
mode = df['dew_RB'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['humidity_RB'].mean()
median = df['humidity_RB'].median()
mode = df['humidity_RB'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['precip_RB'].mean()
median = df['precip_RB'].median()
mode = df['precip_RB'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['windspeed_RB'].mean()
median = df['windspeed_RB'].median()
mode = df['windspeed_RB'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['tempmax_Limpopo'].mean()
median = df['tempmax_Limpopo'].median()
mode = df['tempmax_Limpopo'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['tempmin_Limpopo'].mean()
median = df['tempmin_Limpopo'].median()
mode = df['tempmin_Limpopo'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['temp_Limpopo'].mean()
median = df['temp_Limpopo'].median()
mode = df['temp_Limpopo'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['dew_Limpopo'].mean()
median = df['dew_Limpopo'].median()
mode = df['dew_Limpopo'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['humidity_Limpopo'].mean()
median = df['humidity_Limpopo'].median()
mode = df['humidity_Limpopo'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['precip_Limpopo'].mean()
median = df['precip_Limpopo'].median()
mode = df['precip_Limpopo'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

mean = df['windspeed_Limpopo'].mean()
median = df['windspeed_Limpopo'].median()
mode = df['windspeed_Limpopo'].mode()
print("mean =", mean)
print("median =", median)
print("mode = ", mode)

## SECOND BUSINESS DECISION
## STANDARD VARIANCE

df['Coal_RB_4800_FOB_London_Close_USD'].std()
df['Coal_RB_5500_FOB_London_Close_USD'].std()
df['Coal_RB_5700_FOB_London_Close_USD'].std()
df['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].std()
df['Coal_India_5500_CFR_London_Close_USD'].std()
df['Price_WTI'].std()
df['Price_Brent_Oil'].std()
df['Price_Dubai_Brent_Oil'].std()
df['Price_ExxonMobil'].std()
df['Price_NTPC'].std()
df['Price_Shenhua'].std()
df['tempmax_RB'].std()
df['tempmin_RB'].std()
df['temp_RB'].std()
df['dew_RB'].std()
df['humidity_RB'].std()
df['precip_RB'].std()
df['windspeed_RB'].std()
df['tempmax_Limpopo'].std()
df['tempmin_Limpopo'].std()
df['temp_Limpopo'].std()
df['dew_Limpopo'].std()
df['humidity_Limpopo'].std()
df['precip_Limpopo'].std()
df['windspeed_Limpopo'].std()

## VARIANCE

df['Coal_RB_4800_FOB_London_Close_USD'].var()
df['Coal_RB_5500_FOB_London_Close_USD'].var()
df['Coal_RB_5700_FOB_London_Close_USD'].var()
df['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].var()
df['Coal_India_5500_CFR_London_Close_USD'].var()
df['Price_WTI'].var()
df['Price_Brent_Oil'].var()
df['Price_Dubai_Brent_Oil'].var()
df['Price_ExxonMobil'].var()
df['Price_NTPC'].var()
df['Price_Shenhua'].var()
df['tempmax_RB'].var()
df['tempmin_RB'].var()
df['temp_RB'].var()
df['dew_RB'].var()
df['humidity_RB'].var()
df['precip_RB'].var()
df['windspeed_RB'].var()
df['tempmax_Limpopo'].var()
df['tempmin_Limpopo'].var()
df['temp_Limpopo'].var()
df['dew_Limpopo'].var()
df['humidity_Limpopo'].var()
df['precip_Limpopo'].var()
df['windspeed_Limpopo'].var()


## RANGE

df['Coal_RB_4800_FOB_London_Close_USD'].max() - df['Coal_RB_4800_FOB_London_Close_USD'].min()
df['Coal_RB_5500_FOB_London_Close_USD'].max() - df['Coal_RB_5500_FOB_London_Close_USD'].min()
df['Coal_RB_5700_FOB_London_Close_USD'].max() - df['Coal_RB_5700_FOB_London_Close_USD'].min()
df['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].max() - df['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].min()
df['Coal_India_5500_CFR_London_Close_USD'].max() - df['Coal_India_5500_CFR_London_Close_USD'].min()
df['Price_WTI'].max() - df['Price_WTI'].min()
df['Price_Brent_Oil'].max() - df['Price_Brent_Oil'].min()
df['Price_Dubai_Brent_Oil'].max() - df['Price_Dubai_Brent_Oil'].min()
df['Price_ExxonMobil'].max() - df['Price_ExxonMobil'].min()
df['Price_NTPC'].max() - df['Price_NTPC'].min()
df['Price_Shenhua'].max() - df['Price_Shenhua'].min()
df['tempmax_RB'].max() - df['tempmax_RB'].min()
df['tempmin_RB'].max() - df['tempmin_RB'].min()
df['temp_RB'].max() - df['temp_RB'].min()
df['dew_RB'].max() - df['dew_RB'].min()
df['humidity_RB'].max() - df['humidity_RB'].min()
df['precip_RB'].max() - df['precip_RB'].min()
df['windspeed_RB'].max() - df['windspeed_RB'].min()
df['tempmax_Limpopo'].max() - df['tempmax_Limpopo'].min()
df['tempmin_Limpopo'].max() - df['tempmin_Limpopo'].min()
df['temp_Limpopo'].max() - df['temp_Limpopo'].min()
df['dew_Limpopo'].max() - df['dew_Limpopo'].min()
df['humidity_Limpopo'].max() - df['humidity_Limpopo'].min()
df['precip_Limpopo'].max() - df['precip_Limpopo'].min()
df['windspeed_Limpopo'].max() - df['windspeed_Limpopo'].min()

## THIRD MOMENT BUSINESS DECISION
## SKEWNESS

import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew
df = pd.read_csv("C:/Users/Manisha/Downloads/merged_economic_data.csv")

skewness = skew(df[''])
plt.figure(figsize=(10,6))
df[''].skew()
plt.show()

df['Coal_RB_5500_FOB_London_Close_USD'].skew()
df['Coal_RB_5700_FOB_London_Close_USD'].skew()
df['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].skew()
df['Coal_India_5500_CFR_London_Close_USD'].skew()
df['Price_WTI'].skew()
df['Price_Brent_Oil'].skew()
df['Price_Dubai_Brent_Oil'].skew()
df['Price_ExxonMobil'].skew()
df['Price_NTPC'].skew()
df['Price_Shenhua'].skew()
df['tempmax_RB'].skew()
df['tempmin_RB'].skew()
df['temp_RB'].skew()
df['dew_RB'].skew()
df['humidity_RB'].skew()
df['precip_RB'].skew()
df['windspeed_RB'].skew()
df['tempmax_Limpopo'].skew()
df['tempmin_Limpopo'].skew()
df['temp_Limpopo'].skew()
df['dew_Limpopo'].skew()
df['humidity_Limpopo'].skew()
df['precip_Limpopo'].skew()
df['windspeed_Limpopo'].skew()

## FOURTH MOMENT BUSINESS DECISION
## KURTOSIS

df['Coal_RB_4800_FOB_London_Close_USD'].kurt()
df['Coal_RB_5500_FOB_London_Close_USD'].kurt()
df['Coal_RB_5700_FOB_London_Close_USD'].kurt()
df['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'].kurt()
df['Coal_India_5500_CFR_London_Close_USD'].kurt()
df['Price_WTI'].kurt()
df['Price_Brent_Oil'].kurt()
df['Price_Dubai_Brent_Oil'].kurt()
df['Price_ExxonMobil'].kurt()
df['Price_NTPC'].kurt()
df['Price_Shenhua'].kurt()
df['tempmax_RB'].kurt()
df['tempmin_RB'].kurt()
df['temp_RB'].kurt()
df['dew_RB'].kurt()
df['humidity_RB'].kurt()
df['precip_RB'].kurt()
df['windspeed_RB'].kurt()
df['tempmax_Limpopo'].kurt()
df['tempmin_Limpopo'].kurt()
df['temp_Limpopo'].kurt()
df['dew_Limpopo'].kurt()
df['humidity_Limpopo'].kurt()
df['precip_Limpopo'].kurt()
df['windspeed_Limpopo'].kurt()

## GRAPHICAL REPRESENTATION

import matplotlib.pyplot as plt
import seaborn as sns

sns.histplot(df['Coal_RB_4800_FOB_London_Close_USD'],kde=True)
plt.title('Histogram for Coal_RB_4800_FOB_London_Close_USD')
plt.xlabel('Coal_RB_4800_FOB_London_Close_USD')
plt.ylabel('Frequency')
plt.show()

sns.histplot(df['Coal_RB_5500_FOB_London_Close_USD'],kde=True)
plt.title('Histogram for Coal_RB_5500_FOB_London_Close_USD')
plt.xlabel('Coal_RB_5500_FOB_London_Close_USD')
plt.ylabel('Frequency')
plt.show()

sns.histplot(df['Coal_RB_5700_FOB_London_Close_USD'],kde=True)
plt.title('Histogram for Coal_RB_5700_FOB_London_Close_USD')
plt.xlabel('Coal_RB_5700_FOB_London_Close_USD')
plt.ylabel('Frequency')
plt.show()

sns.histplot(df['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'],kde=True)
plt.title('Histogram for Coal_RB_6000_FOB_CurrentWeek_Avg_USD')
plt.xlabel('Coal_RB_6000_FOB_CurrentWeek_Avg_USD')
plt.ylabel('Frequency')
plt.show()

sns.histplot(df['Coal_India_5500_CFR_London_Close_USD'],kde=True)
plt.title('Histogram for Coal_India_5500_CFR_London_Close_USD')
plt.xlabel('Coal_India_5500_CFR_London_Close_USD')
plt.ylabel('Frequency')
plt.show()

sns.histplot(df['Price_WTI'],kde=True)
plt.title('Histogram for Price_WTI')
plt.xlabel('Price_WTI')
plt.ylabel('Frequency')
plt.show()


sns.histplot(df['Price_Brent_Oil'],kde=True)
plt.title('Histogram for Price_Brent_Oil')
plt.xlabel('Price_Brent_Oil')
plt.ylabel('Frequency')
plt.show()


sns.histplot(df['Price_Dubai_Brent_Oil'],kde=True)
plt.title('Histogram for Price_Dubai_Brent_Oil ')
plt.xlabel('Price_Dubai_Brent_Oil')
plt.ylabel('Frequency')
plt.show()


sns.histplot(df['Price_ExxonMobil'],kde=True)
plt.title('Histogram forPrice_ExxonMobil ')
plt.xlabel('Price_ExxonMobil')
plt.ylabel('Frequency')
plt.show()


sns.histplot(df['Price_NTPC'],kde=True)
plt.title('Histogram for Price_NTPC ')
plt.xlabel('Price_NTPC')
plt.ylabel('Frequency')
plt.show()


sns.histplot(df['Price_Shenhua'],kde=True)
plt.title('Histogram for Price_Shenhua')
plt.xlabel('Price_Shenhua')
plt.ylabel('Frequency')
plt.show()


sns.histplot(df['tempmax_RB'],kde=True)
plt.title('Histogram for tempmax_RB')
plt.xlabel('tempmax_RB')
plt.ylabel('Frequency')
plt.show()


sns.histplot(df['tempmin_RB'],kde=True)
plt.title('Histogram for tempmin_RB ')
plt.xlabel('tempmin_RB')
plt.ylabel('Frequency')
plt.show()

sns.histplot(df['temp_RB'],kde=True)
plt.title('Histogram for temp_RB ')
plt.xlabel('temp_RB')
plt.ylabel('Frequency')
plt.show()

sns.histplot(df['dew_RB'],kde=True)
plt.title('Histogram for dew_RB ')
plt.xlabel('dew_RB')
plt.ylabel('Frequency')
plt.show()

sns.histplot(df['humidity_RB'],kde=True)
plt.title('Histogram for humidity_RB')
plt.xlabel('humidity_RB')
plt.ylabel('Frequency')
plt.show()

sns.histplot(df['precip_RB'],kde=True)
plt.title('Histogram for precip_RB ')
plt.xlabel('precip_RB')
plt.ylabel('Frequency')
plt.show()

sns.histplot(df['windspeed_RB'],kde=True)
plt.title('Histogram for  windspeed_RB')
plt.xlabel('windspeed_RB')
plt.ylabel('Frequency')
plt.show()

sns.histplot(df['tempmax_Limpopo'],kde=True)
plt.title('Histogram for tempmax_Limpopo ')
plt.xlabel('tempmax_Limpopo')
plt.ylabel('Frequency')
plt.show()

sns.histplot(df['tempmin_Limpopo'],kde=True)
plt.title('Histogram for tempmin_Limpopo ')
plt.xlabel('tempmin_Limpopo')
plt.ylabel('Frequency')
plt.show()

sns.histplot(df['temp_Limpopo'],kde=True)
plt.title('Histogram for temp_Limpopo ')
plt.xlabel('temp_Limpopo')
plt.ylabel('Frequency')
plt.show()

sns.histplot(df['dew_Limpopo'],kde=True)
plt.title('Histogram for  dew_Limpopo')
plt.xlabel('dew_Limpopo')
plt.ylabel('Frequency')
plt.show()

sns.histplot(df['humidity_Limpopo'],kde=True)
plt.title('Histogram for humidity_Limpopo')
plt.xlabel('humidity_Limpopo')
plt.ylabel('Frequency')
plt.show()

sns.histplot(df['precip_Limpopo'],kde=True)
plt.title('Histogram for precip_Limpopo')
plt.xlabel('precip_Limpopo')
plt.ylabel('Frequency')
plt.show()

## DENSITY PLOT
import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np

sns.kdeplot(df.Coal_RB_4800_FOB_London_Close_USD)
plt.show()

sns.kdeplot(df.Coal_RB_5500_FOB_London_Close_USD)
plt.title('Density Plot')
plt.xlabel('Coal_RB_5500_FOB_London_Close_USD')
plt.ylabel('Density')
plt.show()

sns.kdeplot(df.Price_WTI)
plt.show()

sns.kdeplot(df.Price_Brent_Oil)
plt.show()

sns.kdeplot(df.Price_ExxonMobil)
plt.show()

sns.kdeplot(df.Price_Shenhua)
sns.kdeplot(df.tempmin_RB_RB)
sns.kdeplot(df.temp_RB)
sns.kdeplot(df.dew_RB)
sns.kdeplot(df.humidity_RB)
sns.kdeplot(df.precip_RB)
sns.kdeplot(df.windspeed_RB)
sns.kdeplot(df.tempmax_Limpopo)
sns.kdeplot(df.tempmin_Limpopo)
sns.kdeplot(df.temp_Limpopo)
sns.kdeplot(df.dew_Limpopo)
sns.kdeplot(df.humidity_Limpopo)
sns.kdeplot(df.precip_Limpopo)
sns.kdeplot(df.windspeed_Limpopo)
plt.show()

## LINE PLOT

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("C:/Users/Manisha/Downloads/merged_economic_data.csv")

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['Coal_RB_4800_FOB_London_Close_USD'], label = 'label')
plt.xlabel('Date')
plt.ylabel('Coal_RB_4800_FOB_London_Close_USD')
plt.title('Date vs Coal_4800')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['Coal_RB_5500_FOB_London_Close_USD'], label = 'label')
plt.xlabel('Date')
plt.ylabel('Coal_RB_5500_FOB_London_Close_USD')
plt.title('Date vs Coal_5500')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['Coal_RB_5700_FOB_London_Close_USD'], label = 'label')
plt.xlabel('Date')
plt.ylabel('Coal_RB_5700_FOB_London_Close_USD')
plt.title('Date vs Coal_5700')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['Coal_RB_6000_FOB_CurrentWeek_Avg_USD'], label = 'label')
plt.xlabel('Date')
plt.ylabel('Coal_RB_6000_FOB_CurrentWeek_Avg_USD')
plt.title('Date vs Coal_6000')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['Coal_India_5500_CFR_London_Close_USD'], label = 'label')
plt.xlabel('Date')
plt.ylabel('Coal_India_5500_CFR_London_Close_USD')
plt.title('Date vs Coal_5500')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['Price_WTI'], label = 'label')
plt.xlabel('Date')
plt.ylabel('Price_WTI')
plt.title('Date vs Price_WTI')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['Price_Brent_Oil'], label = 'label')
plt.xlabel('Date')
plt.ylabel('Price_Brent_Oil')
plt.title('Date vs Price_Brent_Oil')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['Price_Dubai_Brent_Oil'], label = 'label')
plt.xlabel('Date')
plt.ylabel('Price_Dubai_Brent_Oil')
plt.title('Date vs Price_Dubai_Brent_Oil')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['Price_ExxonMobil'], label = 'label')
plt.xlabel('Date')
plt.ylabel('Price_ExxonMobil')
plt.title('Date vs Price_ExxonMobil')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['Price_NTPC'], label = 'label')
plt.xlabel('Date')
plt.ylabel('Price_NTPC')
plt.title('Date vs Price_NTPC')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['Price_Shenhua'], label = 'label')
plt.xlabel('Date')
plt.ylabel('Price_Shenhua')
plt.title('Date vs Price_Shenhua')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['Price_Shenhua'], label = 'label')
plt.xlabel('Date')
plt.ylabel('Price_Shenhua')
plt.title('Date vs Coal_4800')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['tempmax_RB'], label = 'label')
plt.xlabel('Date')
plt.ylabel('tempmax_RB')
plt.title('Date vs tempmax_RB')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['tempmin_RB'], label = 'label')
plt.xlabel('Date')
plt.ylabel('tempmin_RB')
plt.title('Date vs tempmin_RB ')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['temp_RB'], label = 'label')
plt.xlabel('Date')
plt.ylabel('temp_RB')
plt.title('Date vs temp_RB')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['dew_RB'], label = 'label')
plt.xlabel('Date')
plt.ylabel('dew_RB')
plt.title('Date vs dew_RB')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['humidity_RB'], label = 'label')
plt.xlabel('Date')
plt.ylabel('humidity_RB')
plt.title('Date vs humidity_RB')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['precip_RB'], label = 'label')
plt.xlabel('Date')
plt.ylabel('precip_RB')
plt.title('Date vs precip_RB')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['windspeed_RB'], label = 'label')
plt.xlabel('Date')
plt.ylabel('windspeed_RB')
plt.title('Date vs windspeed_RB')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['tempmax_Limpopo'], label = 'label')
plt.xlabel('Date')
plt.ylabel('tempmax_Limpopo')
plt.title('Date vs tempmax_Limpopo')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['tempmin_Limpopo'], label = 'label')
plt.xlabel('Date')
plt.ylabel('tempmin_Limpopo')
plt.title('Date vs tempmin_Limpopo')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['temp_Limpopo'], label = 'label')
plt.xlabel('Date')
plt.ylabel('temp_Limpopo')
plt.title('Date vs temp_Limpopo')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['dew_Limpopo'], label = 'label')
plt.xlabel('Date')
plt.ylabel('dew_Limpopo')
plt.title('Date vs dew_Limpopo')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['humidity_Limpopo'], label = 'label')
plt.xlabel('Date')
plt.ylabel('humidity_Limpopo')
plt.title('Date vs humidity_Limpopo')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['precip_Limpopo'], label = 'label')
plt.xlabel('Date')
plt.ylabel('precip_Limpopo')
plt.title('Date vs precip_Limpopo')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize = (10,6))
plt.plot(df['Date'], df['windspeed_Limpopo'], label = 'label')
plt.xlabel('Date')
plt.ylabel('windspeed_Limpopo')
plt.title('Date vs windspeed_Limpopo')
plt.legend()
plt.grid(True)
plt.show()


## DATA PRE-PROCESSING

import pandas as pd
import numpy as np 

df = pd.read_csv("C:/Users/Manisha/Downloads/merged_economic_data.csv")


## FORWARD FILL

##  find the numerical missing value by forward fill
num_missing_value=df[['Coal_RB_4800_FOB_London_Close_USD', 'Coal_RB_5500_FOB_London_Close_USD',
       'Coal_RB_5700_FOB_London_Close_USD','Coal_RB_6000_FOB_CurrentWeek_Avg_USD',
       'Coal_India_5500_CFR_London_Close_USD', 'Price_WTI', 'Price_Brent_Oil',
       'Price_Dubai_Brent_Oil', 'Price_ExxonMobil', 'Price_NTPC','Price_Shenhua', 'tempmax_RB', 
       'tempmin_RB', 'temp_RB', 'dew_RB', 'humidity_RB', 'precip_RB', 'windspeed_RB','tempmax_Limpopo', 'tempmin_Limpopo', 'temp_Limpopo', 'dew_Limpopo',
       'humidity_Limpopo', 'precip_Limpopo', 'windspeed_Limpopo']].ffill()

## find categorical missing value
cat_missing_values=df[['preciptype_RB','preciptype_Limpopo']].fillna('No rain')

## count the number of values stored in the column
df['preciptype_RB'].value_counts()
df['preciptype_Limpopo'].value_counts()

## concating the both varibales into new dataframe
data_no_missing = pd.concat([df[['Date']], num_missing_value, cat_missing_values], axis=1)

## Price NTPC first row contain Nan Value backward fill used
data_no_missing['Price_NTPC'] = data_no_missing[['Price_NTPC']].bfill()

## OUTLIERS

import pandas as pd
import numpy as np

data = pd.read_csv("C:/Users/Manisha/Downloads/merged_economic_data.csv")
df1 = pd.DataFrame(data)
outliers_dict = {}

## define the list of columns
columns_to_check = ['Coal_RB_4800_FOB_London_Close_USD', 'Coal_RB_5500_FOB_London_Close_USD',
       'Coal_RB_5700_FOB_London_Close_USD','Coal_RB_6000_FOB_CurrentWeek_Avg_USD',
       'Coal_India_5500_CFR_London_Close_USD', 'Price_WTI', 'Price_Brent_Oil',
       'Price_Dubai_Brent_Oil', 'Price_ExxonMobil', 'Price_NTPC','Price_Shenhua', 'tempmax_RB', 
       'tempmin_RB', 'temp_RB', 'dew_RB', 'humidity_RB', 'precip_RB', 'windspeed_RB','tempmax_Limpopo', 'tempmin_Limpopo', 'temp_Limpopo', 'dew_Limpopo',
       'humidity_Limpopo', 'precip_Limpopo', 'windspeed_Limpopo']


## for loop to calculate the each column to replace outliers with NONE 
for col in columns_to_check:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    
    ## IQR (Interquantile Range)
    IQR = Q3 - Q1
    
    ##  calculate lower and upper bound for outliers
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    ## replace outliers with Nan
    df1.loc[(df1[col]< lower_bound) | (df1[col] > upper_bound), col] = np.nan
    print(df1)
    
    ## detect outliers
    outliers = df1[(df1[col] < lower_bound) | (df1[col] > upper_bound)][col]
    ## store the outliers in dictionary
    outliers_dict[col] = outliers 
    
    
## print outliers for each column
for col , outliers in outliers_dict.items():
   print(f"Outliers in {col}:")
   print(outliers)
    
 
### LINEAR INTERPOLATION OF NAN VALUES

linear_inter_data = data_no_missing[['Coal_RB_4800_FOB_London_Close_USD',
       'Coal_RB_5500_FOB_London_Close_USD',
       'Coal_RB_5700_FOB_London_Close_USD',
       'Coal_RB_6000_FOB_CurrentWeek_Avg_USD',
       'Coal_India_5500_CFR_London_Close_USD', 'Price_WTI', 'Price_Brent_Oil',
       'Price_Dubai_Brent_Oil', 'Price_ExxonMobil', 'Price_NTPC',
       'Price_Shenhua', 'tempmax_RB', 'tempmin_RB', 'temp_RB', 'dew_RB',
       'humidity_RB', 'precip_RB', 'windspeed_RB', 'tempmax_Limpopo',
       'tempmin_Limpopo', 'temp_Limpopo', 'dew_Limpopo', 'humidity_Limpopo',
       'precip_Limpopo', 'windspeed_Limpopo']].interpolate(method='linear',limit_direction='both',axis=1)

### COMBINING THE INTERPOLATED DATA WITH OTHER CATEGORICAL COLUMNS
data_interpolated = pd.concat([data_no_missing['Date'], linear_inter_data, data_no_missing[['preciptype_RB','preciptype_Limpopo']]],axis=1)

## AUTO EDA  
 
## DTALE

#pip install dtale
import dtale
d=dtale.show(data_interpolated)
d.open_browser()


## SWEETVIZ

#pip install sweetviz
import sweetviz as sv
s=sv.analyze(data_interpolated)
s.show_html()

    
## Ydata_Profiling

#pip install ydata-profiling

import pandas as pd
from ydata_profiling import ProfileReport 

p = ProfileReport(data_interpolated)
p.to_file('ydata_profiling')


## Glook

#pip install Glook
import pandas as pd
from glook import Glook
data = pd.read_csv(r'C:/Users/Manisha/Downloads/merged_economic_data.csv')
eda = Glook(data)
eda.generate_report()



