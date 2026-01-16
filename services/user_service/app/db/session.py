from typing import Generator
import time
from sqlmodel import SQLModel, create_engine, Session
from core.config import settings

# print(">>> FULL DATABASE_URL =", repr(settings.database_url))
engine = create_engine(
    settings.database_url,
    echo=True,
    future=True,
)

def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session

def init_db():
    SQLModel.metadata.create_all(engine)

