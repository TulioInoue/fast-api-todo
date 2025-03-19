from pydantic import BaseModel, Field

class TodoRequest(BaseModel):
    title: str = Field(min_length = 1)
    description: str = Field(min_length = 3, max_length = 100)
    priority: int = Field(ge = 1, le = 5)



