import lifx_http_client
import lifx_lan_client
import paho.mqtt.client as mqtt

def on_connect(client, userdata, rc):
	print('Connected with result code '+str(rc))
	client.subscribe('lights/#')
	client.subscribe('devices/discover')

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

def reply_with_devices(client, userdata, message):
	print 'Sharing all devices'
	devices = lifx_lan_client.discover_devices()
	for d in devices:
		print type(d)
		print d.get_label()
		client.publish('devices/new', '{{ "name": "{0}", "type": "light", "subType": "lifx_light" "state": "{1}", "color": "{2}" }}'.format(d.get_label(),d.get_power(),d.get_color()))

client = mqtt.Client("lifx_controller")
client.on_connect = on_connect
client.message_callback_add('lights/on', turn_lights_on)
client.message_callback_add('lights/off', turn_lights_off)
client.message_callback_add('lights/color', set_color_all_lights)
client.message_callback_add('devices/discover', reply_with_devices)

client.connect('192.168.1.74', 1883, 60)

print 'Running LIFX controller - listening for messages on localhost:1883'

client.loop_forever()