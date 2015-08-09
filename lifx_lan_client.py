from lifxlan import *
from lib import colorTools

lifxlan = LifxLAN()

def discover_devices():
	return lifxlan.get_lights()

def turn_lights_on():
	print 'Turn lights on'
	lifxlan.set_power_all_lights("on", rapid=True)

def turn_lights_off():
	print 'Turn lights off'
	lifxlan.set_power_all_lights("off", rapid=True)	

def set_color_all_lights(params):
	#print 'Changing colour with ' + str(*arg)
	color = colorTools.getColor(params)
	if color is None:
		print 'Given color is incorrect'
		return
	lifxlan.set_color_all_lights(color, rapid=True)