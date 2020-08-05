<<<<<<< HEAD
import json
=======

>>>>>>> 6c2695f11b40bf781504438c72da9b9fbf39f9b5
from logger import logger

stockLogger = logger()

class portfolio(object): # this class will catilog the actions going on within the positions within
    def __init__(self,positions = {}, bank=1000):
<<<<<<< HEAD
        self.positions = positions
=======
        self.positions= positions
>>>>>>> 6c2695f11b40bf781504438c72da9b9fbf39f9b5
        self.balance = bank

    def addstock(self,stock,v):#stock object, volume , transaction_time
        if validate().cash(v,stock.lastPrice,self.balance) == True:
            if stock.symbol in self.positions.keys():
                x = position(stock,v,self.positions)
<<<<<<< HEAD
                print(self.positions[stock.symbol])
                self.positions[stock.symbol].update(invested = x.invested,stock_num = x.total)
=======
                self.positions[stock.symbol].invested = x.invested
                self.positions[stock.symbol].stock_num = x.stock_num
>>>>>>> 6c2695f11b40bf781504438c72da9b9fbf39f9b5
                self.minus_balance((stock.lastPrice * v))
            else:
                self.positions.update({stock.symbol:position(stock,v)})
                self.minus_balance((stock.lastPrice * v))
        else:
            stockLogger.data("[PORT] insificiont funds {} vs {}".format(self.balance,stock.lastPrice*v))
            return(False)

    def sellstock(self,stock,v): # ensure when selling that Volume being  passed is negitive
        if validate().stock(self.positions,stock.symbol,v) == True:
            x = position(stock,-v,self.positions)
            self.positions[stock.symbol].invested=x.invested
            self.positions[stock.symbol].stock_num = x.stock_num
            self.add_balance(stock.lastPrice * v)
        else:
            stockLogger.data("[PORT] insificiont stock holdings {} of {}".format(stock.symbol,v))
            return(False)

    def add_balance(self, money):
        x = self.balance
        self.balance = x + money
        stockLogger.data("[PORT] ${} was added to balance".format(money))
        print(1)

    def minus_balance(self,money):
        print(2)
        if self.balance >= money:
            x = self.balance
            self.balance = x - money
            stockLogger.data("[PORT] ${} was sumbracted from balance".format(money))
        else:
            stockLogger.exitError("balance too low for ${} witdraw").format(money)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
<<<<<<< HEAD
    
    def from_json(self, json_object):
        if 'balance' in json_object:
            return self.Portfolio(json_object['balance'])
=======
>>>>>>> 6c2695f11b40bf781504438c72da9b9fbf39f9b5

class position(object):
    def __init__(self,s,v,p=None):
        try:
            x=p[s.symbol].invested
            y=p[s.symbol].stock_num
        except:
            x = 0
            y = 0

        self.stock_num = y + v
        self.invested = x + (s.lastPrice * v)

class validate(object):
    def cash(self,volume,price,balance):
        if volume*price <= balance:
            return True
        else:
             return False

    def stock(self,positions,ticker,volume):#NEEDS pORFOLIO INORDER TO valiate spending
        self.ans=()
        if ticker in positions.keys(): #checks to see if the stock is in porfolio
            self.num_of_stock = positions[ticker].stock_num #sums  the numer of stock within the system
            '''validates if their is enough stock to initalize a sell.
            responds true if their is enought stock'''
            if abs(volume) > self.num_of_stock:
                self.ans = False
            if abs(volume) <= self.num_of_stock:
                self.ans = True
        else:
            self.ans = False

        return(self.ans)
