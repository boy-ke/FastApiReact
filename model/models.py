from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    date_created = Column(DateTime, default=datetime.utcnow)
    date_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<Note {self.id} {self.title} {self.description} {self.date_created} {self.date_updated}>"
