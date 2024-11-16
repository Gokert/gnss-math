import grpc
from protos import api_pb2_grpc
from fastapi import Request
from settings import GNSS_GRPC_SERVER_ADDR, GNSS_GRPC_MATH_SERVER_ADDR

async def grps_gnss_math_client():
    channel = grpc.aio.insecure_channel(GNSS_GRPC_MATH_SERVER_ADDR)
    client = api_pb2_grpc.GnssMathServiceStub(channel)
    return client

async def grps_gnss_client():
    channel = grpc.aio.insecure_channel(GNSS_GRPC_SERVER_ADDR)
    client = api_pb2_grpc.GnssMathServiceStub(channel)
    return client