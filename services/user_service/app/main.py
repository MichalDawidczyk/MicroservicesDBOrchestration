from fastapi import FastAPI, Depends, Query
from sqlmodel import Session
from contextlib import asynccontextmanager

from core.config import settings
from db.session import get_session, init_db
from models.user import UserCreate, UserUpdate, User, UserRead
from crud.user_methods import (
    create_user,
    update_user,
    delete_user,
    get_user_by_id,
    list_users,
)
from crud.address_methods import create_address_for_user, update_address
from models.address import AddressCreate, AddressUpdate, Address

@asynccontextmanager
async def lifespan(app: FastAPI):
    init_db()
    yield


app = FastAPI(title=settings.app_name, lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok", "service": "user-service"}


@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int, session: Session = Depends(get_session)):
    return get_user_by_id(user_id, session)


@app.get("/users", response_model=list[UserRead])
def get_users(
    session: Session = Depends(get_session),
    limit: int = Query(10, ge=1, le=100),
    offset: int = Query(0, ge=0),
    first_name: str | None = None,
    last_name: str | None = None,
    is_active: bool | None = None,
    sort_by: str | None = Query(None, regex="^(last_name|is_active)$"),
    sort_order: str = Query("asc", regex="^(asc|desc)$"),
):
    return list_users(
        session,
        limit,
        offset,
        first_name,
        last_name,
        is_active,
        sort_by,
        sort_order,
    )


@app.post("/users", response_model=User)
def create_user_endpoint(user_in: UserCreate, session: Session = Depends(get_session)):
    return create_user(user_in, session)


@app.patch("/users/{user_id}", response_model=User)
def update_user_endpoint(
    user_id: int, user_in: UserUpdate, session: Session = Depends(get_session)
):
    return update_user(user_id, user_in, session)


@app.delete("/users/{user_id}", status_code=204)
def delete_user_endpoint(user_id: int, session: Session = Depends(get_session)):
    delete_user(user_id, session)
    return None


@app.post("/users/{user_id}/address", response_model=Address)
def add_address(
    user_id: int,
    address_in: AddressCreate,
    session: Session = Depends(get_session)
):
    return create_address_for_user(user_id, address_in, session)

@app.patch("/users/{user_id}/address", response_model=Address)
def update_user_address(
    user_id: int,
    address_in: AddressUpdate,
    session: Session = Depends(get_session)
):
    return update_address(user_id, address_in, session)
