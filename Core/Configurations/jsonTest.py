import json
from collections import OrderedDict
from pprint import pprint
##############################################################

#Json Object Class [ Returns Python Object for JSON Data]
class JSONObject:
	def __init__(self, data):
		self.__data__ = data
		
#Loading Json File and Setting Python Object for it.
with open('Configurations.json', 'r') as f:
     data = json.load(f, object_hook=JSONObject)

#Prining attributers of data.
print size(data)
	
#print len(a)
#pprint(data.settings.windowsDriverPath)
