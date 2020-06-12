import mysql.connector
import os, sys

class dbReader(object):
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
    
    def executeQuery(query):
        """
        This method is used for executing queries within the database. Provided
            an input query this will return a 2D array containing the data
        """
        cxn=dbReader()
        cursor=cxn.stocksimdb.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        cxn.stocksimdb.close()
        
        queryResult = []
        for row  in result:
            rowData = []
            for column in row:
                rowData.append(column)
            queryResult.append(rowData)
            
        return queryResult