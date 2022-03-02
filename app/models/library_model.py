from datetime import datetime, timedelta
from sqlalchemy import Column, String, Date
from app.configs.database import db



class LibraryModel(db.Model):

    __tablename__ = "library"

    library_id = Column(String, primary_key=True)
    date_withdrawal = Column(Date, nullable=False, default=datetime.now())
    date_return = Column(Date, nullable=True)
    date_accurancy = Column(Date, nullable=False, default=(datetime.now() + timedelta(15)))
