# -*- coding: utf-8 -*-
"""forestFires.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uJ46P_WJ4kInnT70-QaUf1-G4HBL7KD8
"""

import pandas as pd
from googletrans import Translator
import matplotlib.pyplot as plt

data = pd.read_csv("amazon.csv", thousands = '.', encoding="WINDOWS-1252")

data.head()

data.describe(include= "all")

forest_fire_per_month = data.groupby('month')['number'].sum()

print(forest_fire_per_month)

months_unique = list(data.month.unique())

forest_fire_per_month = forest_fire_per_month.reindex(months_unique, axis=0)

months_unique

print(forest_fire_per_month)

forest_fire_per_month = forest_fire_per_month.to_frame()

forest_fire_per_month.head()

forest_fire_per_month.reset_index(level=0, inplace=True)

forest_fire_per_month.head()

translator = Translator()

for i, m in enumerate(months_unique):
    translated = translator.translate(m)  
    month1 = translated.text    
    forest_fire_per_month.at[i, 'month'] = month1

forest_fire_per_month

plt.figure(figsize=(15, 10))


plt.bar(
forest_fire_per_month['month'],
forest_fire_per_month['number'], 
color = (0.5,0.1,0.5,0.6)) 



plt.yticks(fontsize=16)
plt.xticks(fontsize=10)
plt.suptitle('Brazil Forest Fires Over the Months', fontsize=20)
plt.title('Using Data from Years 1998 - 2017', fontsize=20) 
plt.xlabel('Month', fontsize=20) 
plt.ylabel('Number of Forest Fires', fontsize=20)



for i, num in enumerate(forest_fire_per_month['number']):
    plt.text(i, num + 10000, num, ha='center',fontsize=15)

forest_fire_per_month['number']