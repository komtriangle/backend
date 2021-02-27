from pydantic import BaseModel

class User(BaseModel):
    SberId: int
    Name: str
    Age: int
    Gender: str
    Active: int

class Progres(BaseModel):
    UserId: int
    Date: str
    Completed: bool

class Categoriya(BaseModel):
    Name: str