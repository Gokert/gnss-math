import typing as t
from fastapi import Depends, FastAPI, status, HTTPException
from fastapi.responses import JSONResponse
from grpc.aio import AioRpcError

from clients import grps_gnss_math_client
from protos import api_pb2
from google.protobuf.json_format import MessageToDict

from gnss_math import runGrpc
import asyncio
from settings import GNSS_GRPC_SERVER_ADDR, GNSS_GRPC_MATH_SERVER_ADDR

app = FastAPI()

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(runGrpc(GNSS_GRPC_MATH_SERVER_ADDR))

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(runGrpc(GNSS_GRPC_SERVER_ADDR))

@app.get("/list_coordinates")
async def list_coordinates(client: t.Any = Depends(grps_gnss_math_client)):
    try:
        listCoordinates = await client.ListCoordinates(api_pb2.ListCoordinatesRequest(satellite_name="kek"))
    except AioRpcError as e:
        raise HTTPException(status_code=500, detail=e.details())
    return JSONResponse({"items": MessageToDict(listCoordinates)})
