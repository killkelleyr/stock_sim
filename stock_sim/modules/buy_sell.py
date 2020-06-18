from dbWriter import dbWriter
from logger import logger
from stock import stock
import requests
import os
import datetime
import random
import time

buySellLogger = logger()

class buy_sell(object):
    def __init__(self,ticker,volume,buysell,user_id):
        sim = True
        self.timer = (random.randint(100,400)/1000)
        purchese = False
        if buysell == 'buy':
            buysell = 1
        elif buy_sell == 'sell':
            buy_sell = 0

        if sim == False:
            try:
                APIKEY = os.environ['APIKEY']
                TD_transaction = requests.get('https://api.tdameritrade.com/v1/marketdata/{}/quotes?apikey={}'.format(ticker,APIKEY))
                "(logic for determination of a good perches whenth trew)"
                buySellLogger.info("{} of {} was purchesed").format()
                #set athurisation time
            except:
                print("API purches faild")

        else:
            time.sleep(self.timer)
            stock_info=stock(ticker)
            transaction_time=datetime.datetime.now()

        dbWriter.writetransactionhistory(user_id,ticker,stock_info.askPrice,volume,buysell,transaction_time)
