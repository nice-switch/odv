import enum # NOTE This is Python's builtin enum.
# NOTE from odv import enum This is the applications enum.

class ServiceType(enum.Enum):
    """Available services to launch.

    ### Services:
    ServiceType.DATABASE:
        The database service.
    """
    DATABASE = ["db", "database"]


class LaunchParameter(enum.Enum):
    pass


class EnvironmentType(LaunchParameter):
    """Available environments for launch.
    
    ### Environment Options:
    EnvironmentType.DEVELOPMENT_ENVIRONMENT: 
        Will start the application in development environment including database targets.    
            
    EnvironmentType.PRODUCTION_ENVIRONMENT:
        Will start the application in production environment including database targets.
    """
    DEVELOPMENT = ["dev", "development"]
    PRODUCTION = ["prod", "production"]


class DebugType(LaunchParameter):
    """Debug types available for launch.

    ### Debug Options:
    DebugType.NO_DEBUG_OUTPUT:
        No console output will be made when launched, only errors & rogue outputs will be shown.
            
    DebugType.PARTIAL_DEBUG_OUTPUT:
        Will show bare minimum information when there is activity.
            
    DebugType.FULL_DEBUG_OUTPUT:
         Will show all non-sensitive information available in output when there is activity.
        
    DebugType.SENSITIVE_DEBUG_OUTPUT:
        Will show all possible output including sensitive information like API-keys etc,.
    
    """
    NO_OUTPUT = ["nodebug", "ndebug"]
    
    PARTIAL_OUTPUT = ["partialdebug", "pdebug"]
    FULL_OUTPUT = ["fulldebug", "fdebug"]
    
    SENSITIVE_OUTPUT = ["sensitivedebug", "sdebug"]


class DatabaseType(LaunchParameter):
    """Database types available for launch.

    ### Database Options:
    DatabaseType.SQLITE_DATABASE_TYPE
        Will use a sqlite database for managing data.
    
    DatabaseType.POSTGRES_DATABASE_TYPE
        Will use a postgres database for managing data.
    """
    SQLITE = "sqlite"
    POSTGRES = "postgres"