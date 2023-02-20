from pydantic import BaseModel

class Tool(BaseModel):
    name: str
    size: int
    material: str
