from app import app

import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

app.run(host='0.0.0.0', port=9090, threaded=True)
