from sqlalchemy.orm import Session

from . import models, schemas

from datetime import date

import requests

def get_timesheet(db: Session, timesheet_id: int):
    return db.query(models.Timesheet).filter(models.Timesheet.id == timesheet_id).first()


def get_timesheet_by_employee(db: Session, employee: int):
    return db.query(models.Timesheet).filter(models.Timesheet.employee_id == employee).all()


def get_timesheet_by_employee_and_date(db: Session, employee: int, date:date):
    return db.query(models.Timesheet).filter(models.Timesheet.employee_id == employee, models.Timesheet.date == date).first()


def create_timesheet(db: Session, timesheet: schemas.TimesheetCreate):
    db_timesheet = models.Timesheet(date=timesheet.date, employee_id=timesheet.employee_id,hours=timesheet.hours)
    employee_api_response = requests.get(f'http://127.0.0.1:8000/employees/{db_timesheet.employee_id}')
    if employee_api_response.status_code == 200:
        db.add(db_timesheet)
        db.commit()
        db.refresh(db_timesheet)
        return db_timesheet


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
    db_item = models.Item(**item.dict(), owner_id=user_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item