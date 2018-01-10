# Import libraries 				   
from thingsboardwrapper import *

import json
import time
import random

## Python Wrapper Tests  - Out of ThinksBoards.io Package Scope

#############################################################################
#---------------------------------------------------------------------------#
# CREATE A DEVICE INSTANCE with a DEVICE ID 								#						
# hint: used when you already know what device you want your data from      #
#---------------------------------------------------------------------------#
deviceOne = startDeviceInstance('YOUR_DEVICE_ID_HERE')
#----------------------------------------------------------------------------
print deviceOne																#
print deviceOne.getDataAttributes()											#
print deviceOne.getDataKeys()												#
print deviceOne.getDataValue('YOUR_DATA_KEY_HERE')							#
#---------------------------------------------------------------------------#
# Get values for a specific interval  										#
#---------------------------------------------------------------------------#
key  = 'temperature'														#
fromDateTime = '2017-12-18,11:26'											#
toDateTime	 = '2017-12-18,12:30'											#
agg = 'AVG'																	#
print  deviceOne.getDataValuesInterval(key,fromDateTime,toDateTime,agg)		#
#---------------------------------------------------------------------------#
#############################################################################


#############################################################################
#---------------------------------------------------------------------------#
# CREATE ALL DEVICES INSTANCES 												#
# hint: used when you dont know what device you want your data from         #
#---------------------------------------------------------------------------#
deviceList = startAllDevices() 												#
#																			#
for i in deviceList:														#
	print i.id, i.token,i.entityType, i.dataKeys, i.attributes 				#
print searchDataValueForKey(deviceList,'quantityPP') 						#
print searchDataValueForKey(deviceList,'humidity')     						#
#---------------------------------------------------------------------------#
# Get values for a specific interval  										#
#---------------------------------------------------------------------------#
#																			#
print searchDataIntervalForKey(deviceList,'temperature','2017-12-18,11:26',\
	'2017-12-18,12:30','AVG')
#---------------------------------------------------------------------------#
#############################################################################


#############################################################################
#---------------------------------------------------------------------------#
# Post values to ThinksBoard Device 0 - example 							#
#---------------------------------------------------------------------------#
#																			#
# while True:
# 	#temperature =random.randint(10,20)
#  	#humidity =random.randint(30,70)
# 	data = json.dumps({'quantityPP': 5290})
#  	#print 'Temperature: ' + str(temperature) + ' Humidity: ' + str(humidity)
# 	response =  deviceList[0].postDataValues(data)
# 	print response
# 	time.sleep(1)
#---------------------------------------------------------------------------#
#############################################################################