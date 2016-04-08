#from flask import Flask
import redis
import requests

r = redis.StrictRedis(host='localhost', port=6379, db=0)
#app = Flask(__name__)

#import logging
#log = logging.getLogger('werkzeug')
#log.setLevel(logging.ERROR)

# ensure following keys already exist in redis:
# s1, s2, ts1, ts2, fail-count-1, fail-count-2
# last-ping-1, last-ping-2

def getServerNo():
	try:
		xf = int(r.get("fail-count-1"));
		yf = int(r.get("fail-count-2"));
        	#print xf, yf
        	if xf > 50 and yf > 50:
			#print "critical alarm: both machines seem to have failed"
			return 3
		if xf > 50:
			#print "alarm: 1 seems to be have failed"
			return 2
		if yf > 50:
			#print "alarm: 2 seems to be have failed"
			return 1
	
		x = float(r.get("s1"))
		y = float(r.get("s2"))
		xp = float(r.get("last-ping-1"))
		yp = float(r.get("last-ping-2"))
		#print x, y
		if x * xp <= y * yp:
			return 1
		else:
			return 2
	except:
		return 3

def addFailCount(x):
	r.incr("fail-count-" + x)

def clearFailCount(x):
	r.set("fail-count-" + x, 0)

#@app.route("/add/<int:a>/<int:b>")
def add(a,b):
	x = getServerNo()
	if x == 1:
		try:
			r.incr("s1")
			r.incr("ts1")
			req = requests.get('http://52.77.220.121:9999/add/' + str(a) + '/' + str(b))
			r.decr("s1")
			clearFailCount("1")
			return req.text
		except:
			r.decr("s1")
			addFailCount("1")
			return "Request cannot be processed"
	elif x == 2:
		try:
			r.incr("s2")
			r.incr("ts2")
			req = requests.get('http://192.168.56.101:9999/add/' + str(a) + '/' + str(b))
			r.decr("s2")
			clearFailCount("2")
			return req.text
		except:
			r.decr("s2")
			addFailCount("2")
			return "Request cannot be processed"
	else:
		return "Request cannot be processed"

#if __name__ == '__main__':
#	app.run(threaded=True, host='0.0.0.0', port=9090)
