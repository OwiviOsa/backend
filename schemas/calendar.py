from datetime import datetime
from typing import List
from pydantic import BaseModel
from game_configs.game_config import Location


class CalendarCreate(BaseModel):
    created_time: datetime

    date: str
    event_str: str


class Calendar(CalendarCreate):
    id: int
    save_id: int
