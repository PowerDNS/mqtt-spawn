#!/usr/bin/env python
import mosquitto, sys
import subprocess
import signal

client = mosquitto.Mosquitto()
client.connect(sys.argv[1])

def on_connect(mosq, userdata, rc):
	for topic in sys.argv[3:]:
		client.subscribe(topic, 0)

def on_message(mosq, obj, msg):
	print("Message received on topic "+msg.topic+" with QoS "+str(msg.qos)+" and payload "+msg.payload)
	p = subprocess.Popen(sys.argv[2], shell=True, stdin=subprocess.PIPE)	
	p.stdin.write(msg.payload)
	p.stdin.close()

signal.signal(signal.SIGCHLD, signal.SIG_IGN)

client.on_connect = on_connect
client.on_message = on_message

while True:
	client.loop()