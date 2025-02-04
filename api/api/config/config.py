from os import environ


class Config:
    ENV = environ.get("Repovisor_API_ENV", "production")

    DEBUG = bool(int(environ.get("Repovisor_API_DEBUG", "0")))

    TESTING = bool(int(environ.get("Repovisor_API_TESTING", "0")))

    SECRET_KEY = environ.get("Repovisor_API_ENV", "secretkey")
