from flask import Flask
from clients.lnd import Lnd


app = Flask(__name__)
lnd = LndLTC()


@app.route("/")
def index():
    """
    Get all of the open channels and calculate the net asset value
    """
    return "Hello World!"
