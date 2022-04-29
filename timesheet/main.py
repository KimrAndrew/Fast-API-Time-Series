import stat
from typing import List, Optional

from datetime import date

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

import requests

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/timesheets/", response_model=schemas.Timesheet)
def create_timesheet(timesheet: schemas.TimesheetCreate, db: Session = Depends(get_db)):
    employee_api_response = requests.get(f'http://127.0.0.1:8000/employees/{timesheet.employee_id}')

    if employee_api_response.status_code != 200:
        raise HTTPException(status_code=400, detail="Employee not found")

    db_timesheet = crud.create_timesheet(db=db, timesheet=timesheet)
    return db_timesheet


@app.get("/timesheets/", response_model=List[schemas.Timesheet])
def read_timesheets(employee: int, date: Optional[date] = None, db: Session = Depends(get_db)):
    if date:
        db_timesheets = crud.get_timesheet_by_employee_and_date(db,employee=employee, date=date)
    else:
        db_timesheets = crud.get_timesheet_by_employee(db, employee=employee)

    if db_timesheets is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return db_timesheets

# @app.get("/timesheets/date", response_model=schemas.Timesheet)
# def read_timesheets_by_date(employee: int, date: date, db: Session = Depends(get_db)):
#     db_timesheets = crud.get_timesheet_by_employee_and_date(db,employee=employee, date=date)
#     return db_timesheets
