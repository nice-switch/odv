import socket

from enum import StrEnum, IntEnum

class DatabaseType(StrEnum):
    """Types of databases that are available to use."""
    PRODUCTION = "production"
    DEVELOPMENT = "development"

class ServiceType(StrEnum):
    """Types of services that are available to use."""
    DATABASE = "database"
    CLIENT = "client"
    GUARD = "guard"
    WEB = "web"

# TODO add config loader for DatabaseHost & DatabasePort    
class DatabaseHost(StrEnum):
    """Available IPs to host the API."""
    MACHINE = "127.0.0.1"
    # NOTE this is potentionally unsafe, will be looking more into this.
    LOCALHOST = socket.gethostbyname(socket.gethostname())


class DatabasePort(IntEnum):
    """Available ports for the API."""
    PRODUCTION = 6000
    DEVELOPMENT = 6500


