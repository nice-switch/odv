import enum


class ServiceType(enum.StrEnum):
    DATABASE = "database"
    AUTHORIZATION = "authorization"


class DatabaseType(enum.StrEnum):
    PRODUCTION = "production"
    DEVELOPMENT = "development"
    