FROM python

WORKDIR /service

COPY . .

RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
RUN python3 -m grpc_tools.protoc --proto_path=. ./hello.proto \
            --python_out=. --grpc_python_out=.

EXPOSE 5002

ENTRYPOINT ["python", "server.py"]
