from odv.enum import DebugType, EnvironmentType, DatabaseType
from odv.database.service import DatabaseService


def create_database_service(debug_type: DebugType, environment_type: EnvironmentType, database_type: DatabaseType) -> DatabaseService | None:
    database_service = DatabaseService(
        debug_type=debug_type,
        environment_type=environment_type,
        database_type=database_type,
    )
    
    return database_service
    
    