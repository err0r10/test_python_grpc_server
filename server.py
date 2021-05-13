import grpc
import time

from concurrent import futures

import hello_pb2
import hello_pb2_grpc


class HelloService(hello_pb2_grpc.HelloServicer):

    def GetMessage(self, request, context):
        result = dict(res=f'Hello {request.req}')
        return hello_pb2.ResponseMessage(**result)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloServicer_to_server(HelloService(), server)
    server.add_insecure_port('[::]:5002')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
