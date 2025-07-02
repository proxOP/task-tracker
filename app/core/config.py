from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    project_name: str
    debug: bool
    database_url: Optional[str]

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()

#Debug prints
print("Loaded settings:")
print("PROJECT NAME:", settings.project_name)
print("DEBUG:", settings.debug)
print("DATABASE URL:", settings.database_url)