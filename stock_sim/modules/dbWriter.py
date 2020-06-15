import mysql.connector
import os, sys
from datetime import datetime

class dbWriter(object):
    def __init__(self):
        try:
            stocksim_config = {
                'user': os.environ['DB_USER'],
                'password': os.environ['DB_PASS'], # pragma: allowlist secret
                'port': os.environ['DB_PORT'],
                'charset': 'utf8',
                'host': os.environ['DB_HOST'],
                'database': 'stocksimdb'
                }
            self.stocksimdb = mysql.connector.connect(**stocksim_config)
        except:
            print("Cannot connect to stocksimdb database")
            sys.exit()
    def currentTime():
        """
        Function used to ensure time values are in a consistent format
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    def writeUserName(user_id, user_level, user_hash_pass):
        cxn = dbWriter()
        statement = '''INSERT INTO username
                     (user_id, user_level, user_hash_pass, user_recent_login)
                     VALUES("{}","{}","{}","{}")'''.format(user_id, user_level,
                     user_hash_pass, cxn.currentTime())
        cursor=cxn.stocksimdb.cursor()
        cursor.execute(statement)
        cxn.stocksimdb.commit()
        cursor.close()
        cxn.stocksimdb.close()
    def updateUserLogin(user_id):
        """
        Function for updating when a user last logged into the system. This will
            update the user_recent_login field in the database
        """
        cxn = dbWriter()
        statement = ("""UPDATE username
                     SET user_recent_login = {}
                     WHERE user_id = "{}"
                     """).format(cxn.currentTime(),user_id)
        cursor=cxn.stocksimdb.cursor()
        cursor.execute(statement)
        cxn.stocksimdb.commit()
        cursor.close()
        cxn.stocksimdb.close()

    def writetransactionhistory(user_id,ticker,price,buysell,transaction_time):

        """
        Fuction used to update the trancations table that are acuring
        user_id = the user Id
        ticker = the stock symbol
        price = the price of the that stock at purchise
        buysell = are we buying or selling the stock
        transaction_time = the time the actual transaction when throught
        """
        cxn = dbWriter()
        statement= '''INSERT INTO Transaction_history
                    (user_id,ticker,price,buysell,transaction_time)
                    VALUES("{}","{}","{}","{}","{}")'''.format(user_id,ticker,
                    price,buysell,transaction_time)
        cursor=cxn.stocksimdb.cursor()
        cursor.execute(statement)
        cxn.stocksimdb.commit()
        cursor.close()
        cxn.stocksimdb.close()
