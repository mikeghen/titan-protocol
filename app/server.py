from flask import Flask
from clients.lnd import Lnd

app = Flask(__name__)
lnd = Lnd()

@app.route("/")
def hello():
    return "Hello World!"
