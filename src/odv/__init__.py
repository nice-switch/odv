import threading

from odv import enum

def initialize_database_service(database_type: enum.DatabaseType) -> tuple[bool, str]:
    """Sets up FastAPI, loads peewee connection with a SQLite database.

    Args:
        database_type (enum.DatabaseType): Target database files.

    Returns:
        tuple[bool, str]: Success/Failure, Status Message.
    """
    print(f"Initializing database, target: {database_type.name}")
    
    

def publish_database_service(api_port: enum.DatabasePort, api_host: enum.DatabaseHost) -> tuple[bool, str]:
    """Starts a new thread with uvicorn and runs the FastAPI instance made by initialize_database_service.
    
    Args:
        api_port (enum.DatabasePort): Target API port.
        api_host (enum.DatabaseHost): Target API host.
        
    Returns:
        tuple[bool, str]: Success/Failure, Status Message.
    """
    pass