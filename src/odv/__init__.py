from odv import enum

def initialize_database_service(database_type: enum.DatabaseType, api_port: enum.DatabasePort, api_host: enum.DatabaseHost) -> tuple[bool, str]:
    """_summary_

    Args:
        database_type (enum.DatabaseType): _description_
        api_port (enum.DatabasePort): _description_
        api_host (enum.DatabaseHost): _description_

    Returns:
        tuple[bool, str]: _description_
    """
    print(database_type)
    

def publish_database_service() -> tuple[bool, str]:
    pass