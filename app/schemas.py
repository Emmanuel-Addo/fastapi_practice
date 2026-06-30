from pydantic import BaseModel

class PosrCreate(BaseModel):
    title: str
    content: str