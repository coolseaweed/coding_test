import grpc
import example_pb2 as pb2
import example_pb2_grpc as pb2_grpc
import logging
from pathlib import Path
import numpy as np
from example_pb2 import Report


class HelloClient(object):

    def __init__(self, host: str = "localhost", port: int = 50051) -> None:
        self.host = host
        self.server_port = port
        self.channel = grpc.insecure_channel(f"{host}:{port}")
        self.stub = pb2_grpc.HelloStub(self.channel)

    def get_response(self, text):
        message = pb2.Message(text=text)
        print(f"client: {text}")
        return self.stub.GetServerResponse(message)


if __name__ == "__main__":
    logging.basicConfig()
    client = HelloClient()
    result = client.get_response(text="Hello are you there?")
    print(f"server: {result.text}")
