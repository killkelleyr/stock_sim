import mysql.connector
import os, sys
from datetime import datetime
from logger import logger

dbWriterLogger = logger()

class dbWriter(object):
    def __init__(self):
        try:
            stocksim_config = {
                'user': os.environ['STOCK_DB_USER'],
                'password': os.environ['STOCK_DB_PASS'], # pragma: allowlist secret
                'port': os.environ['STOCK_DB_PORT'],
                'charset': 'utf8',
                'host': os.environ['STOCK_DB_HOST'],
                'database': 'stocksimdb'
                }
            self.stocksimdb = mysql.connector.connect(**stocksim_config)
            dbWriterLogger.info("Logged into stocksimdb")
        except:
            dbWriterLogger.exitError("Cannot connect to stocksimdb")
            
    def currentTime():
        """
        Function used to ensure time values are in a consistent format
        """
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def writeUserName(user_id, user_level, user_hash_pass):
        """
        Used for writing to database
        """
        try:
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
            dbWriterLogger.data("Adding to db: [{}, {}, {}, {}]".format(user_id, 
                                            user_level, user_hash_pass))
        except:
            dbWriterLogger.error("Could not write: [{}, {}, {}]".format(user_id, 
                                            user_level, user_hash_pass))
            
    def updateUserLogin(user_id):
        """
        Function for updating when a user last logged into the system. This will
            update the user_recent_login field in the database
        """
        try:
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
            dbWriterLogger.data("Adding to db: [{}]".format(user_id))
        except:
            dbWriterLogger.error("Could not write: [{}]".format(user_id))

    def writetransactionhistory(user_id,ticker,price,volume,buysell,transaction_time):
        """
        Fuction used to update the trancations table that are acuring
        user_id = the user Id
        ticker = the stock symbol
        price = the price of the that stock at purchise
        buysell = are we buying or selling the stock
        transaction_time = the time the actual transaction when throught
        """
        try:
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
            dbWriterLogger.data("Adding to db: [{},{},{},{},{}]".format(user_id,ticker,
                                            price,buysell,transaction_time))
        except:
            dbWriterLogger.error("Could not write: [{}, {}, {}, {}, {}]".format(user_id,
                                        ticker,price,buysell,transaction_time))
