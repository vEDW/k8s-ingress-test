import os
import socket
from flask import Flask
app = Flask(__name__)

podname = socket.gethostname()

@app.route("/")
def hello():
    message = "ping - " + podname 
    return message

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
