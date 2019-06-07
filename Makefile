run-platform:
	docker-compose up

run-app:
	cd app && FLASK_APP=server.py flask run --host=0.0.0.0

build-rpc:
	curl -o rpc.proto -s https://raw.githubusercontent.com/lightningnetwork/lnd/master/lnrpc/rpc.proto
	python3 -m grpc_tools.protoc --proto_path=protos:. --python_out=./app --grpc_python_out=./app rpc.proto
