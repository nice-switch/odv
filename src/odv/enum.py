import enum


class ServiceType(enum.StrEnum):
    DATABASE = "database"
    AUTHORIZATION = "authorization"


class ExecutionType(enum.StrEnum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    DEBUG = "debug"
    

class DatabaseType(enum.StrEnum):
    SQLITE = "sqlite"
    POSTGRES = "postgres"
