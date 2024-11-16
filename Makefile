up:
	uvicorn api:app --reload

docker-run:
	docker build . --gnss_radar fastapi && docker run -p 80:80 fastapi

install:
	python3 -m pip install --upgrade pip
	pip install --upgrade pip
	pip install -r requirements.txt

generate:
	python3 -m grpc_tools.protoc --python_out=. --grpc_python_out=. --pyi_out=. --proto_path=. ./protos/*.proto
