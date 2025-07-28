from pydantic import BaseModel

class DocumentBase(BaseModel):
    filename: str

class Document(DocumentBase):
    id: int
    owner_id: int

    class Config:
        from_attributes = True