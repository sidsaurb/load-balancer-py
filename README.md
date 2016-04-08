# load-balancer-py

A load balancer which acts as a reverse proxy to two webservers running same code. The balancer code can be run in following two ways:
* A standalone flask application: run as `python balancer/run.py`. On generating 10000 concurrent requests from apache jmeter this show a request drop of about 15%.
* Using apache as a webserver using mod_wsgi. Both wsgi as well as server configuration files are provided. On generating 10000 concurrent requests from apache jmeter this show a request drop of about 6%.

The balancer uses redis to store data shared between requests.

There is another file util.py: This file pings the servers on regular interval, monitors the response time and stores it in redis. This response time also decides which server will handle the next request 
