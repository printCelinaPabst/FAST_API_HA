from sqlmodel import SQLModel, Field

class Mitarbeiter(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    email: str
    abteilung: str


