from odv.enum import DebugType, EnvironmentType, DatabaseType
from odv.enum.database import DatabasePath, SqliteDatabasePath, PostgresDatabasePath
from odv.database import model

class DatabaseService():
    def __init__(self, debug_type: DebugType, environment_type: EnvironmentType, database_type: DatabaseType):
        print(f"Creating DatabaseService...\n[Debug] {debug_type.name}\n[Environment] {environment_type.name}\n[Database Type] {database_type.name}")
        self.debug_type: DebugType = debug_type
        self.environment_type: EnvironmentType = environment_type
        self.database_type: DatabaseType = database_type
        
        self.connection_path: DatabasePath | SqliteDatabasePath | PostgresDatabasePath | None = None
        print("DatabaseService created!")
        
    def create_database_connection(self):
        print(f"Creating {self.database_type.name} database connection...")
        
        match self.database_type:
            case DatabaseType.SQLITE:
                self.connection_path = self.environment_type is EnvironmentType.DEVELOPMENT and SqliteDatabasePath.DEVELOPMENT or SqliteDatabasePath.PRODUCTION
                model.database_connection = model.peewee.SqliteDatabase(self.connection_path.value)
                model.database_connection = model.database_connection.connect()
            case DatabaseType.POSTGRES:
                self.connection_path = self.environment_type is EnvironmentType.DEVELOPMENT and PostgresDatabasePath.DEVELOPMENT or PostgresDatabasePath.PRODUCTION
                print("POSTGRES")
        
        match model.database_connection:
            case None:
                raise Exception(f"{self.database_type.name} database connection failed!")
            case _:
                print(f"{self.database_type.name} connection was successfully created!")
    
    def validate_database_models(self):
        pass