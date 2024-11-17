from fastapi import Request
import httpx

def get_client(request: Request) -> httpx.AsyncClient:
    #TODO: return asyncClient from fastapi state
    pass