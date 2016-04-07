from flask import Flask, request
from time import sleep

app = Flask(__name__)

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
	#sleep(0.5)
	return str(a+b)

if __name__ == '__main__':
        app.run(threaded=True, host='0.0.0.0', port=9999)

