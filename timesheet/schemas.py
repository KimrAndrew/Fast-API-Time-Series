from typing import List, Optional

from datetime import date

from pydantic import BaseModel


class TimesheetBase(BaseModel):
    date: date
    hours: int
    employee_id: int


class TimesheetCreate(TimesheetBase):
    pass


class Timesheet(TimesheetBase):
    id: int

    class Config:
        orm_mode = True