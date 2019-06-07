import os
from flask import Flask, render_template
from clients.lnd import Lnd
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
# lnd = Lnd(username=os.environ["LND_RPC_USERNAME"],
#              password=os.environ["LND_RPC_USERNAME"],
#              host=os.environ["LND_HOST"],
#              port=os.environ["LND_PORT"],
#              tlscert_path=os.environ["LND_TLSCERT_PATH"])


@app.route("/")
def index():
    """
    Get all of the open channels and calculate the net asset value
    """
    # node_info = lnd.get_node_info()
    # channels = lnd.get_channels()
    return render_template('index.html') #, channels=channels, node_info=node_info)
