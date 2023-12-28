import enum

class DatabasePath(enum.Enum):
    pass


class SqliteDatabasePath(DatabasePath):
    PRODUCTION = "data/production_data.sqlite"
    DEVELOPMENT = "data/development_data.sqlite"
    

class PostgresDatabasePath(DatabasePath):
    PRODUCTION = "??"
    DEVELOPMENT = "??"