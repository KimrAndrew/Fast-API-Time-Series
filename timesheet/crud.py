from sqlalchemy.orm import Session

from . import models, schemas

def get_timesheet(db: Session, timesheet_id: int):
    return db.query(models.Timesheet).filter(models.Timesheet.id == timesheet_id).first()


def get_timesheet_by_employee(db: Session, employee: int):
    return db.query(models.Timesheet).filter(models.Timesheet.employee_id == employee).all()


def get_timesheet_by_employee_and_date(db: Session, employee: int, date:str):
    return db.query(models.Timesheet).filter(models.Timesheet.date == date).all()


def create_timesheet(db: Session, timesheet: schemas.TimesheetCreate):
    db_timesheet = models.Timesheet(date=timesheet.date, employee_id=timesheet.employee_id,hours=timesheet.hours)
    db.add(db_timesheet)
    db.commit()
    db.refresh(db_timesheet)
    return db_timesheet