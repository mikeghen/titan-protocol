import os
from base64 import b64encode
import grpc
import rpc_pb2, rpc_pb2_grpc

lnd = rpc_pb2
lndrpc = rpc_pb2_grpc

# TODO: Read only, Admin, etc.
# MACAROON_FILEPATH = '/mnt/data/sparkswap/shared/lnd-engine-admin-ltc.macaroon'
TLS_FILEPATH = '/Volumes//FriendFund/data/lnd/tls.cert'
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

class LndLTC:

    def __init__(self):
        cert = open(TLS_FILEPATH, 'rb').read()
        #macaroon = binascii.hexlify(open(MACAROON_FILEPATH, 'rb').read()).decode

        cert_creds = grpc.ssl_channel_credentials(cert)
        auth_metadata = UsernamePasswordCallCredentials("friendfund", "friendfund")
        auth_creds = grpc.metadata_call_credentials(auth_metadata)
        self._creds = grpc.composite_channel_credentials(cert_creds, auth_creds)
        self._channel = grpc.secure_channel(
            'localhost:10009', self._creds
        )
        self.lnd_stub = lndrpc.LightningStub(self._channel)


    def healthcheck(self):
        return self.lnd_stub.GetInfo(lnd.GetInfoRequest())


    def open_channel(self, address, amount):
        pass


    def close_channel(self, address, transaction_id):
        pass


    def get_invoices(self):
        pass


    def create_invoice(self, address, amount, memo):
        pass


    def approve_invoice(self, address, amount):
        pass
