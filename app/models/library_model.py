from dataclasses import dataclass
from datetime import datetime, timedelta
from sqlalchemy import Column, String, Date
from app.configs.database import db


@dataclass
class LibraryModel(db.Model):

    __tablename__ = "library"

    library_id: str = Column(String, primary_key=True)
    date_withdrawal: str = Column(Date, nullable=False, default=datetime.now())
    date_return: str = Column(Date, nullable=True)
    date_accurancy: str = Column(Date, nullable=False, default=(datetime.now() + timedelta(15)))
