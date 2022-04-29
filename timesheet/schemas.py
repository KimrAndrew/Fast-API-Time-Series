from pydantic import BaseModel

from datetime import date

class TimesheetBase(BaseModel):
    employee_id: int
    date: date
    hours: int

class TimesheetCreate(TimesheetBase):
    pass


class Timesheet(TimesheetBase):
    id: int

    class Config:
        orm_mode = True