import lifx_http_client
import lifx_lan_client
import paho.mqtt.client as mqtt

def on_connect(client, userdata, rc):
	print('Connected with result code '+str(rc))
	client.subscribe('lights/#')

def turn_lights_on(client, userdata, message):
	print 'Lights on'
	lifx_lan_client.turn_lights_on()
	return

def turn_lights_off(client, userdata, message):
	print 'Lights off'
	lifx_lan_client.turn_lights_off()
	return

def set_color_all_lights(client, userdata, message):
	print 'Change color'
	print message.payload
	params = message.payload.split(' ')
	print params
	lifx_lan_client.set_color_all_lights(params)
	return	

client = mqtt.Client("lifx_controller_2")
client.on_connect = on_connect
client.message_callback_add('lights/on', turn_lights_on)
client.message_callback_add('lights/off', turn_lights_off)
client.message_callback_add('lights/color', set_color_all_lights)

client.connect('localhost', 1883, 60)

print 'Running LIFX controller - listening for messages on localhost:1883'

client.loop_forever()