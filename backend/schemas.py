from pydantic import BaseModel
from typing import Optional

class ResumeBase(BaseModel):
    filename: str

class ResumeCreate(ResumeBase):
    predicted_category: Optional[str] = None
    recommended_job: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    skills: Optional[str] = None
    education: Optional[str] = None
    name: Optional[str] = None

class ResumeResponse(ResumeBase):
    id: int
    predicted_category: Optional[str] = None
    recommended_job: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    skills: Optional[str] = None
    education: Optional[str] = None
    name: Optional[str] = None

    class Config:
        from_attributes = True
        # orm_mode = True    