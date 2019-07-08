# Import libraries 				   
from thingsboardwrapper import *

import json
import time
import random

## ISQ Digital Factory @ 2018

#############################################################################
#---------------------------------------------------------------------------#
# CREATE ALL DEVICES INSTANCES 												#
# hint: used when you dont know what device you want your data from         #
#---------------------------------------------------------------------------#

deviceList = startAllDevices() 												#
#																			#
for i in deviceList:														#
    print i.id, i.token,i.entityType, i.dataKeys, i.attributes, i.name, i.description				
#	print i.name, i.attributes

#print searchDataValueForAttribute(deviceList,'S1 Unit Cost [EUR/kg]') 						
#print searchDataValueForKey(deviceList,'humidity')     						

#---------------------------------------------------------------------------#
# Post values to:
# sensor 1 (SENSOR 1 - Raw Materials)								
#---------------------------------------------------------------------------#
#	
																#
while True:
	quantityS1 = round(random.uniform(3.5,4.1),2)
	data = json.dumps({'Quantity S1 [Kg]':quantityS1})
	deviceIndex = getDeviceIndex(deviceList, 'Sensor 1 - Raw Materials')
 	response =  deviceList[deviceIndex].postDataValues(data)
	print 'Quantity S1 [Kg] ' + str(quantityS1) + " -> " + str(response)
	
	quantityS2 = round(random.uniform(0.003,0.004),4)
	data = json.dumps({'Quantity S2 [Kg]':quantityS2})
	deviceIndex = getDeviceIndex(deviceList, 'Sensor 2 - Raw Material Storage')
 	response =  deviceList[deviceIndex].postDataValues(data)
	print 'Quantity S2 [Kg] ' + str(quantityS2) + " -> " + str(response)


	quantityS31 = round(random.uniform(0.00044,0.00045),6)
	data = json.dumps({'Quantity S3.1 [Kg]':quantityS31})
	deviceIndex = getDeviceIndex(deviceList, 'Sensor 3 - Injection')
 	response =  deviceList[deviceIndex].postDataValues(data)
	print 'Quantity S3.1 [Kg] ' + str(quantityS31) + " -> " + str(response)

	quantityS32 = round(random.uniform(0.00041,0.00043),6)
	data = json.dumps({'Quantity S3.2 [Kg]':quantityS32})
	deviceIndex = getDeviceIndex(deviceList, 'Sensor 3 - Injection')
 	response =  deviceList[deviceIndex].postDataValues(data)
	print 'Quantity S3.2 [Kg] ' + str(quantityS32) + " -> " + str(response)


	quantityS41 = round(random.uniform(0.0015,0.0017),5)
	data = json.dumps({'Quantity S4.1 [Kg]':quantityS41})
	deviceIndex = getDeviceIndex(deviceList, 'Sensor 4 - Packaging')
 	response =  deviceList[deviceIndex].postDataValues(data)
	print 'Quantity S4.1 [Kg] ' + str(quantityS41) + " -> " + str(response)

	quantityS42 = round(random.uniform(0.037,0.039),4)
	data = json.dumps({'Quantity S4.2 [Kg]':quantityS42})
	deviceIndex = getDeviceIndex(deviceList, 'Sensor 4 - Packaging')
 	response =  deviceList[deviceIndex].postDataValues(data)
	print 'Quantity S4.2 [Kg] ' + str(quantityS42) + " -> " + str(response)

	quantityS5 = round(random.uniform(0.018,0.020),4)
	data = json.dumps({'Quantity S5 [Kg]':quantityS5})
	deviceIndex = getDeviceIndex(deviceList, 'Sensor 5 - Final Product')
 	response =  deviceList[deviceIndex].postDataValues(data)
	print 'Quantity S5 [Kg] ' + str(quantityS5) + " -> " + str(response)


	energyS61 = round(random.uniform(0.05,3.07),2)
	data = json.dumps({'Energy S61 [MJ]':energyS61})
	deviceIndex = getDeviceIndex(deviceList, 'Sensor 6 - Energy Consumption')
	response =  deviceList[deviceIndex].postDataValues(data)
	print 'Energy S61 [MJ] ' + str(energyS61) + " -> " + str(response)

	energyS62 = round(random.uniform(25,26),2)
	data = json.dumps({'Energy S62 [MJ]':energyS62})
	deviceIndex = getDeviceIndex(deviceList, 'Sensor 6 - Energy Consumption')
	response =  deviceList[deviceIndex].postDataValues(data)
	print 'Energy S62 [MJ] ' + str(energyS62) + " -> " + str(response)


	time.sleep(1)

#	pass







#print searchDataIntervalForKey(deviceList,'temperature','2017-12-18,11:26',\
#	'2017-12-18,12:30','AVG')
#---------------------------------------------------------------------------#
#############################################################################


#############################################################################
#---------------------------------------------------------------------------#
# Post values to ThinksBoard Device 0 - example 							#
#---------------------------------------------------------------------------#
#																			#
# print searchDataValueForKey(deviceList, 'accelarationX')
# time.sleep(2222)

# while True:
#   	accelarationX =random.randint(5,10)
#    	accelarationY =random.randint(10,20)
#   	data = json.dumps({'accelarationX':str(accelarationX), 'accelarationY':str(accelarationY)})
#   	print data
# #   	print data
# #   	#print 'Temperature: ' + str(temperature) + ' Humidity: ' + str(humidity)
#   	response =  deviceList[0].postDataValues(data)
# #  	#print response
# 	print searchDataValueForKey(deviceList, 'accelarationY')
#   	time.sleep(5)
#---------------------------------------------------------------------------#
#############################################################################

