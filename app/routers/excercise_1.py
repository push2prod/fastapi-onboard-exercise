from typing import Annotated
from fastapi import APIRouter, Depends, UploadFile
from fastapi.responses import JSONResponse,Response
from ..models.flights import FlightStats, FlightStatus, Flight
from ..services.exercise_1 import parse_csv
import polars as pl

router = APIRouter(
    prefix='/excersice_1',
    tags=['excersice_1'],
)



@router.post('/count')
def count_by_flight_state(df:pl.DataFrame = Depends(parse_csv), state: FlightStatus  = None) -> list[FlightStats]:
    """
    return a list of dictionaries with entries "state" and "count".
    if @state is not provided return all the dictionaries with states defined in FlightState.  
    """
    #TODO: implement
    pass
    
@router.post('/delay')
def max_delay(df:pl.DataFrame = Depends(parse_csv)) -> Flight:
    """
    return information about the max delay flight 
    """
    #TODO: implement
    pass
    

    