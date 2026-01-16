from typing import Optional
from sqlmodel import SQLModel, Field, Relationship

class Address(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    street: str
    city: str
    postal_code: str
    country: str
    user_id: int = Field(foreign_key="user.id", ondelete="CASCADE")
    user: Optional["User"] = Relationship(back_populates="address")


class AddressCreate(SQLModel):
    user_id: int
    street: str
    city: str
    postal_code: str
    country: str


class AddressUpdate(SQLModel):
    street: Optional[str] = None
    city: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None

class AddressRead(SQLModel):
    id: int
    street: str
    city: str
    postal_code: str
    country: str
