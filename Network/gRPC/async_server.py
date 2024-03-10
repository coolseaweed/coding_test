import logging
import grpc
import example_pb2 as pb2
import example_pb2_grpc as pb2_grpc
from concurrent import futures
import asyncio


class HelloService(pb2_grpc.HelloServicer):
    async def GetServerResponse(self, request, context):
        message = request.text
        result = f"Hello I am up and running received '{message}' message from you "
        result = {"text": result, "received": True}

        return pb2.MessageResponse(**result)


async def serve(port="50051", n_worker=2):
    server = grpc.aio.server()
    pb2_grpc.add_HelloServicer_to_server(HelloService(), server)
    server.add_insecure_port(f"[::]:{port}")
    await server.start()
    logging.info(f"Server started, listening at port: {port}")
    await server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(serve())
