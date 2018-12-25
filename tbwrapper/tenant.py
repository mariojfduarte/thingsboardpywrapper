# thingsboardwrapper/device.py

class TENANT(object):
	def __init__(self):
		pass

	def getDevicesIds(self,base_url, session):
		response = session.get(base_url +'/api/tenant/devices', params = {'limit':'100'})
		json_dict = response.json()
		deviceIds = []
		for i in range(0, len(json_dict['data'])):
			deviceIds.append(json_dict['data'][i]['id']['id'])
		return deviceIds



