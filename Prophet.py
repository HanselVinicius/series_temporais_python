# -*- coding: utf-8 -*-
"""Aula10-1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1HcczzxLLm0FVTPOyYoNU_tQ1ETK_isUW
"""

!pip uninstall torch

!pip install prophet

import pandas as pd
import prophet as pr



dataset = pd.read_csv('https://api.bcb.gov.br/dados/serie/bcdata.sgs.1402/dados?formato=csv', sep=';', parse_dates=['data'])

dataset = dataset.reset_index(drop=True)

dataset.hist()

dataset['data']

dataset['valor']

dataset = dataset[['data', 'valor']].rename(columns = {'data': 'ds', 'valor': 'y'})
dataset

dataset = dataset.sort_values(by='ds')
dataset

model = pr.Prophet()
model.fit(dataset)

future = model.make_future_dataframe(periods=90)
forecast = model.predict(future)

forecast

forecast.tail(90)

model.plot(forecast,xlabel = 'data',ylabel='value')

model.plot_components(forecast)