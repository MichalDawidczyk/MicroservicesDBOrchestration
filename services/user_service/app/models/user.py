from typing import Optional
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime, timezone

class UserBase(SQLModel):
    email: Optional[str] = None
    is_active: Optional[bool] = True


class User(UserBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True, nullable=False)
    first_name: str = Field(nullable=False),
    last_name: str = Field(nullable=False),
    hashed_password: str = Field(nullable=False)
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc),
        nullable=False
    )
    address: Optional["Address"] = Relationship(
        back_populates="user",
        sa_relationship_kwargs={"cascade": "all, delete"}
    )

class UserCreate(UserBase):
    email: str
    first_name: str
    last_name: str
    password: str

class UserUpdate(UserBase):
    password: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None

class UserRead(SQLModel):
    id: int
    email: str
    first_name: str
    last_name: str
    is_active: bool
    created_at: datetime
    address: Optional["AddressRead"] = None

from models.address import Address, AddressRead
UserRead.update_forward_refs()