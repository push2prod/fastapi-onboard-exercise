from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware

from  .services.lifespan import lifespan
from .routers import (excercise_1, excercise_2)
import uvicorn


# add middleware for 

app = FastAPI(
    title='hafifa time!',
    docs_url='/api/docs',
    lifespan=lifespan
)

api = APIRouter(
    prefix='/api'
)

api.include_router(excercise_1.router)
api.include_router(excercise_2.router)


app.include_router(api)

if __name__ == '__main__':
    uvicorn.run('app.main:app', port=8000, host='0.0.0.0')