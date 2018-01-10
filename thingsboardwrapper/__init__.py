# thingsboard/__init__.py
######################################################################################################################
#																													 #
#Data Query API - Telemetry plugin provides following API to fetch entity data:	Timeseries data keys API 			 #																									 #
#Useful links:																										 #
# https://thingsboard.io/docs/user-guide/telemetry/#data-query-api        											 #                                          
# https://demo.thingsboard.io/swagger-ui.html#/																		 #
# https://thingsboard.io/docs/reference/http-api/#telemetry-upload-api  											 #
# https://demo.thingsboard.io/dashboards/b0ef7e30-e0b4-11e7-a701-1d8d2edf4f93										 #
#																													 #
#By: Mario Gamas																		                             #
######################################################################################################################

import os
import requests

#USERNAME = 'tenant@thingsboard.org' 
#PASSWORD = 'tenant'
#BASE_URL = 'http://130.192.85.32:8080'

USERNAME = 'tmluna@isq.pt' 
PASSWORD = 'isq2018'
BASE_URL = 'https://demo.thingsboard.io'

#USERNAME = 'mariojfonseca.duarte@gmail.com' 
#PASSWORD = 'tenant'
#BASE_URL = 'https://demo.thingsboard.io'
 
headers = {'Content-Type': 'application/json','Accept': 'application/json'}
data = '{"username":"'+ USERNAME + '", "password":"' + PASSWORD + '"}'
tokenDict = requests.post(BASE_URL+'/api/auth/login', headers=headers, data=data).json()
TBAPI_TOKEN_KEY = tokenDict['token']

class APIKeyMissingError(Exception):
    pass

if TBAPI_TOKEN_KEY is None:
    raise APIKeyMissingError(
        "All methods require an TOKEN key passed in Headers."
    )

session = requests.Session()
session.headers = {'Content-Type': 'application/json','X-Authorization': '',}
session.headers['X-Authorization'] = str('Bearer ' + TBAPI_TOKEN_KEY)

from device import DEVICE
from tenant import TENANT

def startDeviceInstance(deviceID):
	print 'Starting DEVICE Mapping..'
	# Instantiate device object by ID and then set device credentials 
	deviceInstance = DEVICE(BASE_URL, session, deviceID)
	print 'Finished mapping device.'
	return deviceInstance

def startAllDevices():
	print 'Starting DEVICE Mapping..'
	tenant_deviceIdsList = TENANT().getDevicesIds(BASE_URL,session)
	deviceInstanceList = []
	# Instantiate device objects then set device credentials 
	for i in range(0,len(tenant_deviceIdsList)):
		deviceInstance = DEVICE(BASE_URL,session,tenant_deviceIdsList[i]) 
		deviceInstanceList.append(deviceInstance)
		print 'Device ' + str(i+1) + ' mapped.'
	print 'Finished mapping devices.'
	return deviceInstanceList

def searchDataValueForKey(deviceList, key):
	for i in deviceList:
		for ii in i.dataKeys:
			if (ii == key):
				return i.getDataValue(ii)

def searchDataIntervalForKey(deviceList, key, fromDateTime,toDateTime,agg):
	for i in deviceList:
		for ii in i.dataKeys:
			if (ii == key):
				return i.getDataValuesInterval(ii,fromDateTime,toDateTime,agg)
