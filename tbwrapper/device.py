# thingsboardwrapper/device.py
import requests
import datetime
import time

class DEVICE(object):

	def __init__(self,base_url,session, id):
		self.id = id #TENANT Id
		self.session = session
		self.entityType = 'DEVICE'
		self.base_url = base_url

		url_path = base_url + '/api/device/{}'.format(id)
		responseName = session.get(url_path, params = {'limit':'100'})
		self.name = responseName.json()['name']
		try:
			self.description = responseName.json()['additionalInfo']['description']
		except:
			self.description = ""

		url_path = base_url + '/api/device/{}/credentials'.format(id)
		responseToken = session.get(url_path, params = {'limit':'100'})
		self.token = responseToken.json()['credentialsId']
		
		url_path = self.base_url + '/api/v1/{}/attributes'.format(self.token)
		response = self.session.get(url_path, params = {'limit':'100'})
		try:
			self.attributes = response.json()
		except:
			self.attributes = ""
		
		url_path = base_url + '/api/plugins/telemetry/{}/{}/keys/timeseries'.format(self.entityType,self.id)
		responseKeys = session.get(url_path, params = {'limit':'100'})
		self.dataKeys = responseKeys.json()
	

	# 
	# Methods
	#

	def getDataKeys(self):
		url_path = self.base_url + '/api/plugins/telemetry/{}/{}/keys/timeseries'.format(self.entityType,self.id)
		response = self.session.get(url_path, params = {'limit':'100'})
		self.dataKeys = response.json()
		return response.json()

	def getAttributeValue(self,keys):
		url_path = self.base_url + '/api/plugins/telemetry/{}/{}/values/attributes'.format(self.entityType,self.id)
		try:
			response = self.session.get(url_path, params = {'keys':keys})
			return response.json()[0]['value']
		except:
			pass

	def getDataValue(self,keys):
		url_path = self.base_url + '/api/plugins/telemetry/{}/{}/values/timeseries'.format(self.entityType,self.id)
		try:
			response = self.session.get(url_path, params = {'keys':keys})
			print response.json()
			return response.json()[keys][0]['value']
		except:
			pass

####################################################################################################
#--------------------------------------------------------------------------------------------------#
#ThingsBoard will use startTs, endTs and interval to identify aggregation partitions or 		   #
#sub-queries and execute asynchronous queries to DB that leverage built-in aggregation functions.  #
#The supported parameters are described below:													   #
#--------------------------------------------------------------------------------------------------#
#keys - comma separated list of telemetry keys to fetch.									       #
#startTs - unix timestamp that identifies start of the interval in milliseconds.                   #
#endTs - unix timestamp that identifies end of the interval in milliseconds.					   #
#interval - the aggregation interval, in milliseconds.											   #
#agg - the aggregation function. One of MIN, MAX, AVG, SUM, COUNT, NONE. 						   #
#limit - the max amount of data points to return or intervals to process.                          #
#--------------------------------------------------------------------------------------------------#
####################################################################################################

	def getDataValuesInterval(self,keys,startTs,endTs,agg):
		url_path = self.base_url +'/api/plugins/telemetry/{}/{}/values/timeseries'.format(self.entityType,self.id)
		dts = datetime.datetime.strptime(startTs,'%Y-%m-%d,%H:%M')
		startT = str(int(time.mktime(dts.timetuple()))*1000)
		dte = datetime.datetime.strptime(endTs,'%Y-%m-%d,%H:%M')
		endT = str(int(time.mktime(dte.timetuple()))*1000)
		interval = int((dte-dts).total_seconds()*1000)
		limit = 100
		if (agg == 'DIFF'):
			try:
				maxValue = self.session.get(url_path, params = {'keys':keys,'startTs':startT,'endTs':endT,'interval':interval,'limit':limit,'agg':'MAX'}).json()[keys][0]['value']
				minValue = self.session.get(url_path, params = {'keys':keys,'startTs':startT,'endTs':endT,'interval':interval,'limit':limit,'agg':'MIN'}).json()[keys][0]['value']
				return float(maxValue)-float(minValue)
			except:
				pass
		else:
			try:
				response = self.session.get(url_path, params = {'keys':keys,'startTs':startT,'endTs':endT,'interval':interval,'limit':limit,'agg':agg})
				return response.json()[keys][0]['value']
			except:
				pass

	def postDataValues(self,data):
		url_path = self.base_url + '/api/v1/{}/telemetry'.format(self.token)
		response = requests.post(url_path, data = data)		
		return response


