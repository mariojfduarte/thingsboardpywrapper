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
#deviceOne = startDeviceInstance('9496e830-2d0e-11e8-801f-efa7ab79a01b')
#----------------------------------------------------------------------------
#print deviceOne																#
#print deviceOne.getDataKeys()												#
#print deviceOne.getDataValue('Active Energy')								#
#---------------------------------------------------------------------------#
# Get values for a specific interval  										#
#---------------------------------------------------------------------------#
#key  = 'Active Energy'														#
#fromDateTime = '2018-06-01,11:26'											#
#toDateTime	 = '2018-06-18,12:30'											#
#agg = 'AVG'																	#
#print  deviceOne.getDataValuesInterval(key,fromDateTime,toDateTime,agg)		#
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
	print i.id, i.token,i.entityType, i.name, i.dataKeys, i.attributes 		#

#print searchDataValueForKey(deviceList,'Prima Power','Active Energy') 						#
#print searchDataValueForKey(deviceList,'Prima Power','Active Power')     					#
#---------------------------------------------------------------------------#
# Get values for a specific interval  										#
#---------------------------------------------------------------------------#
#																			#
#print searchDataIntervalForKey(deviceList,'Prima Power','Active Energy','2018-06-01,11:26',\
#	'2018-06-18,12:30','AVG')
#---------------------------------------------------------------------------#
#############################################################################


#############################################################################
#---------------------------------------------------------------------------#
# Post values to ThinksBoard Device 0 - example 							#
#---------------------------------------------------------------------------#
#																			#
#print searchDataValueForKey(deviceList, 'activePower')
#time.sleep(2222)

# deviceName  = 'TESTE'B
# deviceIndex = getDeviceIndex(deviceList, deviceName)

# print deviceIndex 

while True:
   	activePower =random.randint(5,10)
   	activeEnergy =random.randint(10,20)
   	data = json.dumps({'activePower':str(activePower), 'activeEnergy':str(activeEnergy)})
   	response =  deviceList[0].postDataValues(data)
  	print deviceList[0]
 	#print searchDataValueForKey(deviceList,deviceName, 'activeEnergy')
  	time.sleep(5)
#---------------------------------------------------------------------------#
#############################################################################

