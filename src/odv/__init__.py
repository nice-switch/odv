from odv import enum

def initialize_database_service(database_type: enum.DatabaseType, api_port: enum.DatabasePort, api_host: enum.DatabaseHost) -> tuple[bool, str]:
    """Sets up FastAPI, loads peewee connection with a SQLite database.

    Args:
        database_type (enum.DatabaseType): Target database files.
        api_port (enum.DatabasePort): Target API port.
        api_host (enum.DatabaseHost): Target API host.

    Returns:
        tuple[bool, str]: Success/Failure, Status Message.
    """
    print(database_type)
    

def publish_database_service() -> tuple[bool, str]:
    """_summary_

    Returns:
        tuple[bool, str]: _description_
    """
    pass