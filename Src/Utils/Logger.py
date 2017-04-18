#InBuilt Import.
import datetime

#Class Definition
class Logger:
    def logger(self, logs):
        print '['+str(datetime.datetime.now().date())+', '+str(datetime.datetime.now().time())+'] ' + logs
