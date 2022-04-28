from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

from datetime import date


class TimeSeries(Base):
    __tablename__ = "timeseries"

    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer)
    date=Column(date)