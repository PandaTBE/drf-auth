from dotenv import load_dotenv
import os

load_dotenv()


config = {
    "DEBUG": bool(int(os.getenv("DEBUG"))),
    "SECRET_KEY": os.getenv("SECRET_KEY"),
    "STATIC_ROOT": os.getenv("STATIC_ROOT"),
    "MEDIA_ROOT": os.getenv("MEDIA_ROOT"),
    "ALLOWED_HOSTS": os.getenv("ALLOWED_HOSTS"),
    "CORS_ALLOWED_ORIGINS": os.getenv("CORS_ALLOWED_ORIGINS"),
    "JWT_ACCESS_TOKEN_LIFETIME_IN_HOURS": os.getenv(
        "JWT_ACCESS_TOKEN_LIFETIME_IN_HOURS"
    ),
    "JWT_REFRESH_TOKEN_LIFETIME_IN_DAYS": os.getenv(
        "JWT_REFRESH_TOKEN_LIFETIME_IN_DAYS"
    ),
    "JWT_SIGNING_KEY": os.getenv("JWT_SIGNING_KEY"),
    "DB_URL": f"postgres://{os.getenv("DB_USER")}:{os.getenv("DB_PASSWORD")}@{os.getenv("DB_HOST")}:{os.getenv("DB_PORT")}/{os.getenv("DB_NAME")}",
}
