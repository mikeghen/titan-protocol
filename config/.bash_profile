export BITSTEIND_DIR="$HOME/app-container/.bitcoin"
alias bitsteind="/Users/mikeghen/Documents/Projects/bitcoin-0.18.0/bin/bitcoind -datadir=$BITSTEIND_DIR"
alias bitstein-cli="/Users/mikeghen/Documents/Projects/bitcoin-0.18.0/bin/bitcoin-cli -datadir=$BITSTEIND_DIR"
export LND_ORIGINATOR_DIR="/Users/mikeghen/app-container/.lnd1"
export LND_INVESTOR_1_DIR="/Users/mikeghen/app-container/.lnd2"
alias originator-lnd="/Users/mikeghen/Documents/Projects/lnd-darwin-amd64-v0.6.1-beta/lnd --lnddir=$LND_ORIGINATOR_DIR";
alias originator-lncli="/Users/mikeghen/Documents/Projects/lnd-darwin-amd64-v0.6.1-beta/lncli -n regtest --lnddir=$LND_ORIGINATOR_DIR --rpcserver=localhost:11009"
alias investor-1-lnd="/Users/mikeghen/Documents/Projects/lnd-darwin-amd64-v0.6.1-beta/lnd --lnddir=$LND_INVESTOR_1_DIR";
alias investor-1-lncli="/Users/mikeghen/Documents/Projects/lnd-darwin-amd64-v0.6.1-beta/lncli -n regtest --lnddir=$LND_INVESTOR_1_DIR --rpcserver=localhost:10009"
