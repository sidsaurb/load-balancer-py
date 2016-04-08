from flask import Flask
import processrequest

app = Flask(__name__)

app.add_url_rule("/add/<int:a>/<int:b>", "processrequest", processrequest.add, methods=['GET'])

if __name__ == "__main__":
    app.run(threaded=True, host='0.0.0.0', port=9090)

