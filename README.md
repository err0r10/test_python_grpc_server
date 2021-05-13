# test_python_grpc_server

Run server
1. Copy ```git clone https://github.com/err0r10/test_python_grpc_service.git```
2. ```cd test_python_grpc_service```
3. Build ```docker build -t test_python_grpc_service .```
4. Run docker container ```docker run -d -p 5002:5002 test_python_grpc_service```

Run client
1. Create protoc ```python3 -m grpc_tools.protoc --proto_path=. ./hello.proto --python_out=. --grpc_python_out=.```
2. Run client ```python3 client.py```
