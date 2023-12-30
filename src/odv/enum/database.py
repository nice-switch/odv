import enum


class DatabaseType(enum.Enum):
    SQLITE = "sqlite"
    # TODO add more


class DatabaseInfo(enum.Enum):
    # TODO add config loader
    DEVELOPMENT_SQLITE_PATH = "data/development_data.sqlite"
    PRODUCTION_SQLITE_PATH = "data/production_data.sqlite"


