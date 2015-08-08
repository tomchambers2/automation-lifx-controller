import requests
import os

lifx_token = os.environ['LIFX_TOKEN']

headers = {
    "Authorization": "Bearer %s" % lifx_token,
}

def get_lights():
	response = requests.get('https://api.lifx.com/v1beta1/lights/all', headers=headers)
	return response.json()

def toggle(lightId):
	if lightId is None:
		lightId = 'all'
	response = requests.post('https://api.lifx.com/v1beta1/lights/%s/toggle' % lightId, headers=headers)
	return response.json()

def change_light_colour(lightId, colour):
	if lightId is None:
		lightId = 'all'
	response = requests.put('https://api.lifx.com/v1beta1/lights/%s/power' % lightId, headers=headers)
	return response.json()

def change_light_power(lightId, power):
	if lightId is None:
		lightId = 'all'
	response = requests.put('https://api.lifx.com/v1beta1/lights/%s/power' % lightId, headers=headers)
	return response.json()