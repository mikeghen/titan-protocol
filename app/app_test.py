import os
from clients.lnd import Lnd
from dotenv import load_dotenv

load_dotenv() # TODO: .env.test file

lnd = Lnd(username=os.environ["LND_RPC_USERNAME"],
             password=os.environ["LND_RPC_USERNAME"],
             host=os.environ["LND_HOST"],
             port=os.environ["LND_PORT"],
             tlscert_path=os.environ["LND_TLSCERT_PATH"])


import unittest

class TestLnd(unittest.TestCase):
    """
    Simple test harness for testing the Lnd Client
    """
    def test_healthcheck(self):
        self.assertTrue(lnd.healthcheck())


    def test_get_channels(self):
        channels = lnd.get_channels()
        self.assertTrue(isinstance(channels, list))
        for channel in channels:
            self.assertTrue(isinstance(channel, dict))


    def test_get_node_info(self):
        node_info = lnd.get_node_info()
        self.assertTrue(isinstance(node_info, dict))


if __name__ == '__main__':
    unittest.main()
