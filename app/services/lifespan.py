from contextlib import asynccontextmanager
from fastapi import FastAPI
import httpx

@asynccontextmanager
async def lifespan(app: FastAPI):
    #TODO: manage httpx async client at server startup
    yield
    #TODO: manage httpx async client at server teardown