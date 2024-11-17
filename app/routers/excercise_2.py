from typing import Annotated
from fastapi import APIRouter, Depends, Request
from fastapi.responses import JSONResponse,Response, StreamingResponse
from ..services.exercise_2 import get_client
from ..models.jokes import Joke
import httpx

router = APIRouter(
    prefix='/excersice_2',
    tags=['excersice_2'],
)


@router.get('/jokes')
async def random_jokes(request: Request, num_jokes: int = 1) -> list[Joke]:
    """
    returns @num_jokes in a list from https://official-joke-api.appspot.com/random_joke
    all jokes must be unique! its not funny teliing the same joke twice
    """
    #TODO: implement
    pass


@router.get('/dogs',
    responses = {
        200: {
            "content": {"image/jpeg": {}}
        }
    })
async def random_dog_image(client: httpx.AsyncClient = Depends(get_client)):
    """
    returns a picture of a random dog using https://dog.ceo/api/breeds/image/random
    """
    #TODO: implement
    pass

@router.get('/dogs/gray',
    responses = {
        200: {
            "content": {"image/jpeg": {}}
        }
    })
async def random_dog_gray_image(client: httpx.AsyncClient = Depends(get_client), img = Depends(random_dog_image)):
    """
    returns a picture of a random dog using @random_dog_image and return it in grey scale using cv2

    """
    #TODO: implement
    pass


    

    