from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    app_name: str = Field(default="User Service")
    environment: str = Field(default="local")
    debug: bool = Field(default=True)

    db_host: str = Field(default="user-db")
    db_port: int = Field(default=5432)
    db_name: str = Field(default="user_service")
    db_user: str = Field(default="user_service")
    db_password: str = Field(default="user_service")

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+psycopg2://{self.db_user}:{self.db_password}"
            f"@{self.db_host}:{self.db_port}/{self.db_name}"
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()