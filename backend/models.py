from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from database import Base

class Resume(Base):
    __tablename__ = 'resumes'

    id = Column(Integer, primary_key=True, index=True)
    filename = Column(String, index=True)
    predicted_category = Column(String, nullable=True)
    recommended_job = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    email = Column(String, nullable=True)
    skills = Column(Text, nullable=True)
    education = Column(Text, nullable=True)
    name = Column(String, nullable=True)
    created_At = Column(DateTime(timezone=True), server_default=func.now())