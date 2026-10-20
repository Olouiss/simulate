from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    database_url: str = "sqlite:///./ledgerlab.db"
    session_secret: str = "dev-only-change-me-please-use-a-long-random-secret"
    cookie_secure: bool = False
    cors_origins: str = "http://localhost:3000,http://127.0.0.1:3000"
    session_ttl_hours: int = 12
    max_transfer_ngn: str = "10000000"
    model_config = {"env_file": ".env", "extra": "ignore"}
    @property
    def origins(self): return [x.strip() for x in self.cors_origins.split(",") if x.strip()]
settings = Settings()
