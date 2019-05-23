from lndgrpc import LNDClient

# pass in the ip-address with RPC port and network ('mainnet', 'testnet', 'simnet')
# the client defaults to 127.0.0.1:10009 and mainnet if no args provided

print('Listening for invoices...')
for invoice in lnd.subscribe_invoices():
    print(invoice)


class Lnd:

    def __init__(self):
        self.client = LNDClient("lnd-ltc:10009", network='mainnet')


    def healthcheck(self):
        self.client.get_info()


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
