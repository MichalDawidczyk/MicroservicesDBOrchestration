from sqlmodel import Session, select
from fastapi import HTTPException
from models.user import User, UserCreate, UserUpdate
import hashlib


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()


def get_user_by_id(user_id: int, session: Session) -> User:
    user = session.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


def create_user(user_in: UserCreate, session: Session) -> User:
    existing = session.exec(select(User).where(User.email == user_in.email)).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        email=user_in.email,
        first_name=user_in.first_name,
        last_name=user_in.last_name,
        hashed_password=hash_password(user_in.password),
        is_active=True,
    )
    session.add(user)
    session.commit()
    session.refresh(user)
    return user


def update_user(user_id: int, user_in: UserUpdate, session: Session) -> User:
    user = get_user_by_id(user_id, session)

    if user_in.email is not None:
        user.email = user_in.email
    if user_in.first_name is not None:
        user.first_name = user_in.first_name
    if user_in.last_name is not None:
        user.last_name = user_in.last_name
    if user_in.password is not None:
        user.hashed_password = hash_password(user_in.password)
    if user_in.is_active is not None:
        user.is_active = user_in.is_active

    session.commit()
    session.refresh(user)
    return user


def delete_user(user_id: int, session: Session):
    user = get_user_by_id(user_id, session)
    session.delete(user)
    session.commit()


def list_users(
    session: Session,
    limit: int,
    offset: int,
    first_name: str | None,
    last_name: str | None,
    is_active: bool | None,
    sort_by: str | None,
    sort_order: str,
):
    statement = select(User)

    if first_name:
        statement = statement.where(User.first_name.ilike(f"%{first_name}%"))
    if last_name:
        statement = statement.where(User.last_name.ilike(f"%{last_name}%"))
    if is_active is not None:
        statement = statement.where(User.is_active == is_active)

    if sort_by:
        column = getattr(User, sort_by)
        statement = statement.order_by(
            column.desc() if sort_order == "desc" else column.asc()
        )

    statement = statement.offset(offset).limit(limit)
    return session.exec(statement).all()