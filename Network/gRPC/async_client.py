import grpc
import example_pb2 as pb2
import example_pb2_grpc as pb2_grpc
import logging
from pathlib import Path
import numpy as np
import asyncio


class HelloClient(object):

    def __init__(self, host: str = "localhost", port: int = 50051) -> None:
        self.host = host
        self.port = port
        # self.channel = grpc.aio.insecure_channel(f"{host}:{port}")
        # self.stub = pb2_grpc.HelloStub(self.channel)

    async def get_response(self, text):
        message = pb2.Message(text=text)
        print(f"client: {text}")
        async with grpc.aio.insecure_channel(f"{self.host}:{self.port}") as channel:
            stub = pb2_grpc.HelloStub(channel)
            result = await stub.GetServerResponse(message)
            return result


async def run_client():
    client = HelloClient()
    tasks = [client.get_response(text=f"sending {i} message") for i in range(100)]

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)


if __name__ == "__main__":
    logging.basicConfig()
    asyncio.run(run_client())
