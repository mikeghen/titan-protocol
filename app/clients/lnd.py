import os
import binascii
import grpc
import rpc_pb2, rpc_pb2_grpc

lnd = rpc_pb2
lndrpc = rpc_pb2_grpc

# TODO: Read only, Admin, etc.
MACAROON_FILEPATH = '/mnt/data/sparkswap/shared/lnd-engine-admin-ltc.macaroon'
TLS_FILEPATH = '/mnt/data/sparkswap/shared/lnd-engine-tls-ltc.cert'
os.environ["GRPC_SSL_CIPHER_SUITES"] = 'HIGH+ECDSA'


class MacaroonMetadataPlugin(grpc.AuthMetadataPlugin):
    """Metadata plugin to include macaroon in metadata of each RPC request"""

    def __init__(self, macaroon):
        self.macaroon = macaroon

    def __call__(self, context, callback):
        callback([('macaroon', self.macaroon)], None)


class LndLTC:

    def __init__(self):
        cert = open(TLS_FILEPATH, 'rb')
        macaroon = binascii.hexlify(open(MACAROON_FILEPATH, 'rb').read()).decode

        cert_creds = grpc.ssl_channel_credentials(cert)
        metadata_plugin = MacaroonMetadataPlugin(macaroon)
        auth_creds = grpc.metadata_call_credentials(metadata_plugin)
        self._creds = grpc.composite_channel_credentials(cert_creds, auth_creds)
        self.channel = grpcsecure_channel(
            'localhost', self._creds, options=[('grpc.max_receive_message_length', 1024*1024*50)]
        )
        self.lnd_stub = lnrpc.LightningStub(channel)


    def healthcheck(self):
        return self.lnd_stub.GetInfo(ln.GetInfoRequest())


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
