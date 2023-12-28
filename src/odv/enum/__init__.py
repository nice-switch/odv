import enum # NOTE This is Python's builtin enum.
# NOTE from odv import enum This is the applications enum.

from odv.enum import debug, database, api

class ServiceType(enum.Enum):
    """Available services to launch.

    ### Services:
    ServiceType.DATABASE:
        The database service.
    """
    DATABASE = ["db", "database"]
    

class LaunchParameter(enum.Enum):
    """Available launch parameters through interface.
    
    ### Environment Options:
    LaunchParameter.DEVELOPMENT_ENVIRONMENT: 
        Will start the application in development environment including database targets.    
            
    LaunchParameter.PRODUCTION_ENVIRONMENT:
        Will start the application in production environment including database targets.

    
    ### Database Options:
    LaunchParameter.SQLITE_DATABASE_TYPE
        Will use a sqlite database for managing data.
    
    LaunchParameter.POSTGRES_DATABASE_TYPE
        Will use a postgres database for managing data.
    
    
    ### Debug Options:
    LaunchParameter.NO_DEBUG_OUTPUT:
        No console output will be made when launched, only errors & rogue outputs will be shown.
            
    LaunchParameter.PARTIAL_DEBUG_OUTPUT:
        Will show bare minimum information when there is activity.
            
    LaunchParameter.FULL_DEBUG_OUTPUT:
         Will show all non-sensitive information available in output when there is activity.
        
    LaunchParameter.SENSITIVE_DEBUG_OUTPUT:
        Will show all possible output including sensitive information like API-keys etc,.
    
    """
    DEVELOPMENT_ENVIRONMENT = ["dev", "development"]
    PRODUCTION_ENVIRONMENT = ["prod", "production"]
    
    NO_DEBUG_OUTPUT = ["nodebug", "ndebug"]
    
    PARTIAL_DEBUG_OUTPUT = ["partialdebug", "pdebug"]
    FULL_DEBUG_OUTPUT = ["fulldebug", "fdebug"]
    
    SENSITIVE_DEBUG_OUTPUT = ["sensitivedebug", "sdebug"]
    
    SQLITE_DATABASE_TYPE = ["sqlite"]
    POSTGRES_DATABASE_TYPE = ["postgres"]

