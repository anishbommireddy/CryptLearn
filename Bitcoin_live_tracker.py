# -*- coding: utf-8 -*-
"""StockMarket.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EfOA841jkUlpPnMph7gkOXBt05ASeMXE
"""



import cryptocompare
def get_crypto_price(cryptocurrency,currency):
    return cryptocompare.get_price(cryptocurrency,currency=currency)[cryptocurrency][currency]

def get_crypto_name(cryptocurrency):
    return cryptocompare.get_coin_list()[cryptocurrency]['FullName']

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import cryptocompare
from datetime import datetime 

plt.style.use('seaborn')

x_vals = []
y_vals = []

def animate(i):
  x_vals.append(datetime.now())
  y_vals.append(get_crypto_price('BTC','USD'))
  plt.title(get_crypto_name('BTC') + ' Price Live Plotting')  
  plt.xlabel('Date')
  plt.ylabel('Price($)')
  plt.plot_date(x_vals,y_vals,linestyle="solid",ms=0)
  plt.tight_layout()      
ani = FuncAnimation(plt.gcf(), animate, interval=1000)
plt.show()
