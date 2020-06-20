import requests
import json, os, sys
import time
import datetime
from logger import logger

stockLogger = logger()

class stock():
    def __init__(self):
        self.symbol = None
        self.bidPrice = None
        self.bidSize = None
        self.askPrice = None
        self.askSize = None
        self.lastPrice = None
        self.lastSize = None
        self.openPrice = None
        self.highPrice = None
        self.lowPrice = None
        self.bidTick = None
        self.closePrice = None
        self.netChange = None
        self.volatility = None
        self.assetType = None
        self.description = None
        self.totalVolume = None
        self.mark = None
        self.WkHigh = None
        self.WkLow = None
        self.divAmount = None
        self.divYield = None
        self.divDate = None

    def hist(self,start,end):
        self.hist = builder(self.symbol,start,end)
        stockLogger.data("[HIST] {}".format(self.hist))
        
    def lookupTicker(self,ticker):
        try:
            APIKEY=os.environ['APIKEY']
            TD_PULL = requests.get('https://api.tdameritrade.com/v1/marketdata/{}/quotes?apikey={}'.format(ticker,APIKEY))
            stock_info = TD_PULL.json()
            #print(stock_info)
        except:
            stockLogger.exitError("Unable too pull information about {} ticker may be miss spelled".format(ticker))
            
        stockLogger.data("[STOCK] {}".format(stock_info))
        self.symbol = stock_info[ticker]['symbol']
        self.bidPrice = stock_info[ticker]['bidPrice']
        self.bidSize = stock_info[ticker]['bidSize']
        self.askPrice = stock_info[ticker]['askPrice']
        self.askSize = stock_info[ticker]['askSize']
        self.lastPrice = stock_info[ticker]['lastPrice']
        self.lastSize = stock_info[ticker]['lastSize']
        self.openPrice = stock_info[ticker]['openPrice']
        self.highPrice = stock_info[ticker]['highPrice']
        self.lowPrice = stock_info[ticker]['lowPrice']
        self.bidTick = stock_info[ticker]['bidTick']
        self.closePrice = stock_info[ticker]['closePrice']
        self.netChange = stock_info[ticker]['netChange']
        self.volatility = stock_info[ticker]['volatility']
        self.assetType = stock_info[ticker]['assetType']
        self.description = stock_info[ticker]['description']
        self.totalVolume = stock_info[ticker]['totalVolume']
        self.mark = stock_info[ticker]['mark']
        self.WkHigh = stock_info[ticker]['52WkHigh']
        self.WkLow = stock_info[ticker]['52WkLow']
        self.divAmount = stock_info[ticker]['divAmount']
        self.divYield = stock_info[ticker]['divYield']
        self.divDate = stock_info[ticker]['divDate']
        


class builder():
    def __init__ (self,ticker,start,end):
        self.open ={}
        self.high ={}
        self.low ={}
        self.close ={}
        self.volume ={}
        APIKEY=os.environ['APIKEY']
        unixstart = int(time.mktime(start.timetuple()))
        unixend = int(time.mktime(end.timetuple()))
        try:
            stock_hist_raw = requests.get('https://api.tdameritrade.com/v1/marketdata/{}/pricehistory?apikey={}&periodType=day&frequencyType=minute&endDate={}000&startDate={}000'.format(ticker,APIKEY, unixend, unixstart))
            stock_hist_tuple = stock_hist_raw.json()['candles']
        except:
            print('Error: unable too pull information about ticker \n ticker may be miss spelled \n or date may be wrong')
            stockLogger.exitError("Could not pull data from history for {}".format(ticker))
        for x in stock_hist_tuple:
            self.open[x.get('datetime')]= x.get('open')
            self.high[x.get('datetime')]= x.get('high')
            self.low[x.get('datetime')]= x.get('low')
            self.close[x.get('datetime')]= x.get('close')
            self.volume[x.get('datetime')]= x.get('volume')
