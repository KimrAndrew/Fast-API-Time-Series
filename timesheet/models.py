from sqlalchemy import Column, Integer, Date

from .database import Base


class Timesheet(Base):
    __tablename__ = "timesheet"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer)
    date = Column(Date)
    hours = Column(Integer)