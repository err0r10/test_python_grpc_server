import grpc

from faker import Faker

import hello_pb2
import hello_pb2_grpc


class HelloClient:

    def __init__(self, host='localhost', port=5002):
        self.host = host
        self.port = port
        self.channel = grpc.insecure_channel(f'{self.host}:{self.port}')
        self.stub = hello_pb2_grpc.HelloStub(self.channel)

    def get_hello_message(self, message):
        _message = hello_pb2.RequestMessage(req=message)
        return self.stub.GetMessage(_message)


if __name__ == '__main__':
    name = Faker().name()
    client = HelloClient()
    result = client.get_hello_message(name)
    print(result)
