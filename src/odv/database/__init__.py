from odv import enum
from odv.database import model, service


def create_database_service(debug_type: enum.DebugType, environment_type: enum.EnvironmentType, database_type: enum.DatabaseType) -> service.DatabaseService | None:
    database_service = service.DatabaseService(
        debug_type=debug_type,
        environment_type=environment_type,
        database_type=database_type,
    )
    
    