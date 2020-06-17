from datetime import datetime
import sys

class logger(object):
    def __init__(self):
        # TODO: Use this to create log dir
        self.logDir = '../logs/'
        
    def data(self, message):
        '''
        This function should be used for logging data to the log files. This should
            be used to record a successful data retreived or stored action.
        '''
        self.errorType = 'DATA'
        self.__writeLog(message)
    
    def info(self, message):
        '''
        This function should be used to display useful information for specific actions,
            and their status
        '''
        self.errorType = 'INFO'
        self.__writeLog(message)
        
    def error(self, message):
        '''
        This function should be used to log any errors which occur and do not 
            result in the script failing.
        '''
        self.errorType = 'ERROR'
        self.__writeLog(message)
    
    def exitSuccess(self, message):
        '''
        This function should be called whenever a sys.exit is called for 
            a successful execution
        '''
        self.errorType = 'SUCCESS'
        self.__writeLog(message,True)
        
    def exitError(self, message):
        '''
        This function should be called for any error which must result in the 
            script exiting or result in an uncaught exception.
        '''
        self.errorType = 'ERROR'
        self.__writeLog(message, True)
        
    def __writeLog(self, message, EXITSTATUS = None):
        '''
        Private method for writing to the log file. 
        
        A new log file is created for each date
        '''
        curDate = datetime.now()
        fileName = "{}{}_StockSim.log".format(self.logDir,curDate.strftime("%m-%d-%Y"))
        log = open(fileName, "a+")
        if EXITSTATUS:
            log.write("[{}][{}][{}] {}\n".format(curDate,"EXIT",self.errorType,message))
            sys.exit()
        else:
            log.write("[{}][{}] {}\n".format(curDate,self.errorType,message))
        log.close()