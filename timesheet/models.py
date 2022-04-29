from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship

from .database import Base

from datetime import date


class Timesheet(Base):
    __tablename__ = "timesheet"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer)
    date = Column(Date)
    hours = Column(Integer)