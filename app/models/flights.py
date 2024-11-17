from pydantic import BaseModel, computed_field, AwareDatetime
from functools import cached_property
import polars as pl
from enum import Enum
from datetime import datetime

class FlightStatus(Enum):
    @classmethod
    def list(cls):
        """
        return a list of all values of objects defined in the enum class
        """
        return list(map(lambda c: c.value, cls))
    LANDED = 'LANDED'
    DEPARTED = 'DEPARTED'


class FlightStats(BaseModel):
    status: FlightStatus
    count: int

class Flight(BaseModel):
    flight_company_id: str
    flight_id: str
    scheduled_time: datetime
    actual_time: datetime
  
    @cached_property
    @computed_field
    def delay(self) -> datetime:
        return self.actual_time - self.scheduled_time