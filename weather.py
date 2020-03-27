
from datetime import datetime
import os
import pytz
from flask import requests
import math
API_KEY = ''
API_URL = ('http;//api.openweathermap.org/data/2.5/weather?q={} & mode=json///7units=metric&appid={}')

def query_api(city):
	try:
		print(API_URL.format(city, API_KEY)).json()
	except Exception as exc:
		print(exc)
		data=None
	return data
