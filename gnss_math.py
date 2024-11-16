from grpc import aio

from protos import api_pb2_grpc
from protos import api_pb2
import service


class GnssMathService(api_pb2_grpc.GnssMathServiceServicer):
    async def ListCoordinates(self, request, context):
        cds = service.gnss_coordinates()
        print(request, cds)
        return api_pb2.ListCoordinatesResponse(coordinates=cds)


async def runGrpc(addr):
    server = aio.server()
    api_pb2_grpc.add_GnssMathServiceServicer_to_server(
        GnssMathService(), server
    )
    server.add_insecure_port(addr)
    print(f"App started on {addr}")
    await server.start()
    await server.wait_for_termination()