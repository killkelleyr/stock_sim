from dbWriter import dbWriter
from logger import logger
import requests
import os
import datetime
import random
import time

buySellLogger = logger()

class buy_sell(object):
    def __init__(self,stock,volume,buysell,userName):
        sim = True
        self.timer = (random.randint(100,400)/1000)

        if sim == False:
            #TODO: Utilize td's trading API to create an order
            '''
            try:
                APIKEY = os.environ['APIKEY']
                TD_transaction = requests.get('https://api.tdameritrade.com/v1/marketdata/{}/quotes?apikey={}'.format(stock.symbol,APIKEY))
                "(logic for determination of a good perches whenth trew)"
                buySellLogger.info("{} of {} was purchesed").format()
                #set athurisation time
            except:
                print("API purches faild")
            '''
            pass
        else:
            time.sleep(self.timer)
            stock_info=stock.lookupTicker(stock.symbol)
            transaction_time=datetime.datetime.now()

        dbWriter.writetransactionhistory(userName.userName,stock_info.symbol,stock_info.askPrice,volume,buysell,transaction_time)
        if buysell == 1:
            userName.portfolio.addstock(stock_info, volume, transaction_time)
        elif buysell == 0:
            userName.portfolio.sellstock(stock_info, volume, transaction_time)
