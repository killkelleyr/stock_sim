from dbWriter import dbWriter
import datetime
print(datetime.datetime.now())

dbWriter.writetransactionhistory('z_howey','TSLA',1000.25,0,datetime.datetime.now())
