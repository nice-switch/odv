import enum # NOTE This is Python's builtin enum.
# NOTE from odv import enum This is the applications enum.

class ServiceType(enum.Enum):
    DATABASE = ["db", "database"]
    

class LaunchParameter(enum.Enum):
    """Available launch parameters through interface.
    
    
    ### Environment Options:
    LaunchParameter.DEVELOPMENT_ENVIRONMENT: 
        Will start the application in development environment including database targets.
            
            
            
    LaunchParameter.PRODUCTION_ENVIRONMENT:
        Will start the application in production environment including database targets.
    
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


class DatabaseType(enum.Enum):
    """Available database types to store & manage data.

    
    """
    SQLITE = "sqlite"
    POSTGRES = "postgres"
    