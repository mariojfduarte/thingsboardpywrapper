
# ThingsBoard Python Wrapper

A simple python wrapper for ThingsBoard IoT Platform Telemetry API

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

1. ThingsBoard account
2. Python2.7 installed
3. PIP Dependency Management 


### Installing

To start using thingsboardpywrapper you need to first configure your credentials. Open __init__.py file and replace the following strings with yours:

```
USERNAME = 'YOUR_USER_NAME' 
PASSWORD = 'YOUR_PASSWORD'
BASE_URL = 'https://demo.thingsboard.io #for example
```

And then import thingsboard module to wherever your want to use it

```
from thingsboard import *
```

Now you are ready to get the data from the Devices.

## How Does it Work

What this wrapper does it basically doing GET requests according to our needs. There are two ways you can do it.

### #1 CREATE A DEVICE INSTANCE with a DEVICE ID
 hint: used when you already know what device you want your data from 

Got to ThingsBoard dashboard and choose a Device. Then, create a device object using its ID

```
deviceOne = startDeviceInstance('INPUT_DEVICE_ID_HERE')
```

Now we can call methods on this device object to get the last datakey value:

```
print deviceOne
print deviceOne.getDataAttributes()
print deviceOne.getDataKeys()
print deviceOne.getDataValue('accelarationX')
```

Or an aggregation of values for a specific interval:

```
key  = 'temperature'
fromDateTime = '2017-12-18,11:26'
toDateTime	 = '2017-12-18,12:30'
agg = 'AVG'
print  deviceOne.getDataValuesInterval(key,fromDateTime,toDateTime,agg)
```

### #2 CREATE INSTANCES FOR ALL DEVICES
 hint: used when you dont know what device you want your data from

Calling the following function will map all devices present on ThingsBoard dashboard and instantiate objects for all of them.

```
deviceList = startAllDevices() 
```

Then you can print all their information like this:

```
for i in deviceList:
	print i.id, i.token,i.entityType, i.dataKeys, i.attributes 
´´´

To retrieve our data we have two functions. One to get get the latest values simply by passing the device's list and the intendend datakey:

```
print searchDataValueForKey(deviceList,'humidity')
´´´

Another to get values for a specific time interval by passing the same parameter plus inital and final datetime:

```
print searchDataIntervalForKey(deviceList,'temperature','2017-12-18,11:26',\
	'2017-12-18,12:30','AVG')
´´´

Note: We assume that each datakey is unique accross all different Devices and the that the time format is respected.

## Deployment

Either user ThingsBoard [demo version](https://demo.thingsboard.io) or follow the [instructions](https://thingsboard.io/docs/) to deploy your own instance.

## Built With

* [ThingsBoard](https://thingsboard.io/docs/) - The IoT Platform used
* [Python2.7](https://www.python.org/) - Programming Language
* [PIP](https://pypi.python.org/pypi/pip) - Dependency Management

## Authors

* **Mário Duarte** - *Initial work* - [thingsboardpywrapper](https://github.com/mariojfduarte/thingsboardpywrapper)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* ISQ
