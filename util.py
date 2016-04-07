#!/usr/bin/python

import threading
import subprocess
import redis
import requests

r = redis.StrictRedis(host='localhost', port=6379, db=0)

timerInterval = 5.0

def monitor():
	print "timer hit"
        try:
		host = "52.77.220.121"
		ping_response = subprocess.Popen(["/bin/ping", "-c1", "-w100", host], stdout=subprocess.PIPE).stdout.read()
		time = ping_response.split("\n")[1].split(" ")[-2][5:]
		r.set("last-ping-1", time)
		xf = int(r.get("fail-count-1"))
		if xf > 50:
			req = requests.get('http://52.77.220.121:9999/add/2/3')
			r.set("fail-count-1", 0)
        except:
		xf = int(r.get("fail-count-1"))
		if xf > 50:
                	print "alarm: 1 seems down"
	try:
		host = "192.168.56.101"
		ping_response = subprocess.Popen(["/bin/ping", "-c1", "-w100", host], stdout=subprocess.PIPE).stdout.read()
		time = ping_response.split("\n")[1].split(" ")[-2][5:]
		r.set("last-ping-2", time)
		yf = int(r.get("fail-count-2"))
		if yf > 50:
			req = requests.get('http://192.168.56.101:9999/add/2/3')
			r.set("fail-count-2", 0)
        except:
		yf = int(r.get("fail-count-2"))
		if yf > 50:
                	print "alarm: 2 seems down"

        timer = threading.Timer(timerInterval, monitor)
        timer.start()

timer = threading.Timer(timerInterval, monitor)
timer.start()
#sendPing()
