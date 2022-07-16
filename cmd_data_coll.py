import requests  #for sending
import jsons # for reading and writing json dicts
import os #
#import sys
#import pandas as pd
#import numpy as np
import date  # for datestring manipulation
import time  # for timing, sleeps etc.
import random
import matplotlib.pyplot as plt

class DataCollector:
    #handles data collection, storage, file read/write
    def __init__(self):
        pass

    
    def url_construct():
        pass

class Strategy:
    #singular api for different strategies
    #each strategy needs it's own class for it's
    #own data manipulation and edge cases, 
    
    options={"next400":next400,}

    def __init__(self,option):
        self.strategy=option[random.choice(list(Strategy.options.keys()))

class next400:
    pass

class View:

    def __init__(self):
        self.fig=plt.figure()
        self.ax=plt.axes(projection="3d")

    def update(self,):
        self.clear_view()
        self.draw_all()
        
    def draw_all(self,):
        pass

    def clear_view(self,):
        pass



if __name__=="__main__":
    pass

    

url='https://web-api.coinmarketcap.com/v1/cryptocurrency/listings/historical?convert=USD,USD,BTC&date=2021-05-09&limit=200&start=201'
r=requests.get(url)


data=r.json()

data=data[0]["quote"]['USD']


