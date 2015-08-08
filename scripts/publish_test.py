import paho.mqtt.client as mqtt
import time

mqttc = mqtt.Client("lifx_test")
mqttc.connect('localhost', 1883)

mqttc.publish('lights/on', '50000 50000 50000 5000')
time.sleep(2)
mqttc.publish('lights/off', '50000 50000 50000 5000')
mqttc.loop(2)