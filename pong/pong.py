import os 

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "pong!"

if __name__ == "__main__":
	app.run(debug=False,host='0.0.0.0', port=int(os.getenv('PORT', '5000')))

