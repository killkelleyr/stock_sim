from dbReader import dbReader
from stock import stock
from buy_sell import buy_sell
import pandas as pd
import json
from logger import logger
import numpy as np

stockLogger = logger()

class portfolio(object): # this class will catilog the actions going on within the positions within
    def __init__(self):
        self.positions={}

    def addstock(self,stock,v,t):#stock object, volume , transaction_time
        self.positions.update({stock.symbol:position(stock,v,t)})


    def sellstock(self,stock,v,t): # ensure when selling that Volume being  passed is negitive
        self.positions.update({stock.symbol:position(stock,-v,t)})

class position(object):
    def __init__(self,s,v,t):
        self.price = s.lastPrice
        self.amount = v
        self.datetime = t

class validate(object):
    def __init__(self,portfolio,ticker,volume):#NEEDS pORFOLIO INORDER TO valiate spending
        self.ans=()
        if buy_sell.symbol in portfolio.Stock: #checks to see if the stock is in porfolio
            self.transaction =  portfolio.Stock.get(ticker) #pulles all information on stock in question
            self.num_of_stock = sum(len(self.transaction.get(Volume))) #sums  the numer of stock within the system
            '''validates if their is enough stock to worint a sell.
            responds true if their is enought stock'''
            if abs(volume) > self.num_of_stock:
                self.ans = False
            if abs(volume) <= self.num_of_stock:
                self.ans = True
        else:
            self.ans = False
