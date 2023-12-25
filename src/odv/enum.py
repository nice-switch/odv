import enum


class ServiceType(enum.StrEnum):
    """Available services for odv.
    """
    DATABASE = "database"
    AUTHORIZATION = "authorization"


class ExecutionType(enum.StrEnum):
    """Available launch options.
    """
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    

class DatabaseType(enum.StrEnum):
    """Target data for launch.
    """
    SQLITE = "sqlite"
    POSTGRES = "postgres"
