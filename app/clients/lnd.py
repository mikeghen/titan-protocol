import os

LND_DIR = "/Users/mikeghen/app-container/.lnd2"
LND ="/Users/mikeghen/Documents/Projects/lnd-darwin-amd64-v0.6.1-beta/lncli -n regtest --lnddir={0} --rpcserver=localhost:11009".format(LND_DIR)

# TODO: Read only, Admin, etc.
# MACAROON_FILEPATH = '/mnt/data/sparkswap/shared/lnd-engine-admin-ltc.macaroon'
TLS_FILEPATH = '/Volumes/FriendFund/data/lnd/tls.cert'
os.environ["GRPC_SSL_CIPHER_SUITES"] = 'HIGH+ECDSA'


class UsernamePasswordCallCredentials(grpc.AuthMetadataPlugin):
    """Metadata wrapper for raw access token credentials."""
    def __init__(self, username, password):
        self._username = username
        self._password = password

    def __call__(self, context, callback):
        auth_str = bytes('{0}:{1}'.format(self._username, self._password), 'ascii')
        basic_auth = "Basic {0}".format(b64encode(auth_str).decode('utf-8'))
        metadata = (('authorization', basic_auth),)
        callback(metadata, None)

class Lnd:

    def __init__(self):
        pass


    def healthcheck(self):
        """
        Return true or false based on the information
        """
        result = os.system("investor-1-cli getinfo")
        print(result)
        return result



    def get_channels(self):
        """
        Return a list of dicts containing channel information
        """
        # channels_response = self.stub.ListChannels(lnd.ListChannelsRequest(active_only=True))
        # channels = []
        # for channel in channels_response.channels:
        #     channel_dict = {
        #         "active": channel.active,
        #         "chan_id": channel.chan_id,
        #         "capacity": channel.capacity,
        #         "commit_fee": channel.commit_fee,
        #         "local_balance": channel.local_balance,
        #         "remote_balance": channel.remote_balance,
        #         "sent": channel.total_satoshis_sent,
        #         "received": channel.total_satoshis_received
        #     }
        #     channels.append(channel_dict)
        # self.channels = channels
        # return channels
        return [
          { "active": True, "chan_id": "983y42ufh3piqh2f92", "capacity": 100000, "commit_fee": 1000, "local_balance": 10000, "remote_balance": 90000, "sent": 10000, "received": 10000 },
          { "active": True, "chan_id": "j3f2bij3h0ihb2fi3p", "capacity": 100000, "commit_fee": 1000, "local_balance": 10000, "remote_balance": 90000, "sent": 10000, "received": 10000 },
          { "active": True, "chan_id": "3vqwh0ibq3v324qvr3", "capacity": 100000, "commit_fee": 1000, "local_balance": 10000, "remote_balance": 90000, "sent": 10000, "received": 10000 },
          { "active": True, "chan_id": "qw3rv3qv3vqvq3ver3", "capacity": 100000, "commit_fee": 1000, "local_balance": 10000, "remote_balance": 90000, "sent": 10000, "received": 10000 },
          { "active": True, "chan_id": "lnk3vrio34fvve3346", "capacity": 100000, "commit_fee": 1000, "local_balance": 10000, "remote_balance": 90000, "sent": 10000, "received": 10000 }
        ]


    def get_node_info(self):
        """
        Return a dict of information about the LND node
        """
        # node_info = self.stub.GetInfo(lnd.GetInfoRequest())
        # node_info_detail = self.stub.GetNodeInfo(
        #     lnd.NodeInfoRequest(pub_key=node_info.identity_pubkey)
        # )
        # return {
        #     "identity_pubkey": node_info.identity_pubkey,
        #     "uris": node_info.uris,
        #     "alias": node_info.alias,
        #     "chains": node_info.chains,
        #     "version": node_info.version,
        #     "block_height": node_info.block_height,
        #     "synced": str(node_info.synced_to_chain),
        #     "block_hash": node_info.block_hash,
        #     "num_active_channels": node_info.num_active_channels,
        #     "num_inactive_channels": node_info.num_inactive_channels,
        #     "num_pending_channels": node_info.num_pending_channels,
        #     "num_peers": node_info.num_peers,
        #     "total_capacity": node_info_detail.total_capacity
        # }
        return {
            "identity_pubkey": "3f8ho3boiv3boi@ltc.lnd.crypdex.io",
            "uris": "uris",
            "alias": "crypdex",
            "version": "0.6.0-beta commit=v0.6-beta",
            "block_height": 1637531,
            "synced": True,
            "num_active_channels": 5,
            "num_inactive_channels": 0,
            "num_pending_channels": 0,
            "num_peers": 5,
            "total_capacity": 500000
        }



    def open_channel(self, address, amount):
        """Open a channel to an existing peer"""
        request = ln.OpenChannelRequest(
            node_pubkey_string=node_pubkey,
            local_funding_amount=local_funding_amount,
            push_sat=push_sat,
            private=private
        )
        response = self._ln_stub.OpenChannel(request)
        return response
        pass


    def close_channel(self, address, transaction_id):
        pass


    def get_invoices(self):
        pass


    def create_invoice(self, address, amount, memo):
        pass


    def approve_invoice(self, address, amount):
        pass
