import threading, uvicorn

from odv import enum, database

def initialize_database_service(database_type: enum.DatabaseType) -> tuple[database.DatabaseService | None, str]:
    """Sets up FastAPI, loads peewee connection with a SQLite database.

    Args:
        database_type (enum.DatabaseType): Target database files.

    Returns:
        tuple[bool, str]: Success/Failure, Status Message.
    """
    
    print(f"Initializing database, target: {database_type.name}")
    database_api = database.DatabaseAPI(
        database_type=database_type
    )
    
    database_service = database.DatabaseService(
        database_api=database_api
    )
    
    return database_service, "Success!"
    
    
    
    

def publish_database_service(database_service: database.DatabaseService) -> tuple[bool, str]:
    """Starts a new thread with uvicorn and runs the FastAPI instance made by initialize_database_service.
    
    Args:
        api_port (enum.DatabasePort): Target API port.
        api_host (enum.DatabaseHost): Target API host.
        
    Returns:
        tuple[bool, str]: Success/Failure, Status Message.
    """
    
    database_service.api.initialize_peewee_connection()
    database_service.api.initialize_api_endpoints()
    
    # TODO thread handling probably?...
    uvicorn.run(
        app=database_service.api.fast_api,
        host=database_service.host,
        port=database_service.port
    )