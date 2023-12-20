import socket

from enum import StrEnum, IntEnum


class DatabaseType(StrEnum):
    """_summary_

    Args:
        StrEnum (_type_): _description_
    """
    PRODUCTION = "production"
    DEVELOPMENT = "development"

class ServiceType(StrEnum):
    """_summary_

    Args:
        StrEnum (_type_): _description_
    """
    DATABASE = "database"
    CLIENT = "client"
    GUARD = "guard"
    WEB = "web"

# TODO add config loader for DatabaseHost & DatabasePort    
class DatabaseHost(StrEnum):
    """_summary_

    Args:
        StrEnum (_type_): _description_
    """
    MACHINE = "127.0.0.1"
    LOCALHOST = socket.gethostbyname(socket.gethostname())


class DatabasePort(IntEnum):
    """_summary_

    Args:
        IntEnum (_type_): _description_
    """
    PRODUCTION = 6000
    DEVELOPMENT = 6500