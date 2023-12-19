from enum import StrEnum

class ServiceType(StrEnum):
    DATABASE = "database"
    CLIENT = "client"
    GUARD = "guard"
    WEB = "web"


class DatabaseType(StrEnum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"


