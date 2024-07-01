from dotenv import dotenv_values


settings: dict = dotenv_values(".env")
DB_HOST: str = settings.get("DB_HOST")
DB_PORT: str = settings.get("DB_PORT")
DB_NAME: str = settings.get("DB_NAME")
DB_USER: str = settings.get("DB_USER")
DB_PASSWORD: str = settings.get("DB_PASSWORD")
