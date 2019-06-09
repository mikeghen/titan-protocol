build:
	cd lndash && docker build -t lndash:latest .

run:
	docker run -d --rm \
  -v=/Users/mikeghen/app-container/.lnd1/tls.cert:/usr/src/app/config/tls.cert \
  -v=/Users/mikeghen/app-container/.lnd1/data/chain/bitcoin/regtest/admin.macaroon:/usr/src/app/config/admin.macaroon \
  -p 8000:8000 \
  -e LNDASH_LND_SERVER="127.0.0.1:10009" \
  lndash:latest

sync-config:
	cp ./config/originator-lnd.conf ~/app-container/.lnd1/lnd.conf
	cp ./config/investor-lnd.conf ~/app-container/.lnd2/lnd.conf
	cp ./config/bitcoin.conf ~/app-container/.bitcoin/bitcoin.conf
	cp ./config/.bash_profile ~/.bash_profile
	source ~/.bash_profile
