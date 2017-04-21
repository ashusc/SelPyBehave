#Import Section.
from Utils.Logger import Logger
# -- FILE:Features/environment.py
from behave.log_capture import capture

@capture
def before_all(context):
    print("Starting Framework.....")
	#wd = obj.getDriver('CHROME')
	#wd.get('http://ww.google.co.in')
	#time.sleep(5)
	#Closing Drivers.
	#print 'Closing WebDriver...'
	#obj.closeWebDriverObject(wd)


@capture
def before_scenario(self, context):
    print("Starting Scenario.....")

@capture
def before_feature(self, context):
    print("Starting Feature.....")

@capture
def after_scenario(self, context):
    print("Ending Scenario.....")

@capture
def after_feature(self, context):
    print("Ending Feature.....")

@capture
def after_all(context):
    #Copy and rename the created output of JSON Format.
    print("After all.....")
