run:
	docker-compose up

build-rpc:
	curl -o rpc.proto -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/lnrpc/rpc.proto
	python3 -m grpc_tools.protoc --proto_path=protos:. --python_out=./app --grpc_python_out=./app rpc.proto
