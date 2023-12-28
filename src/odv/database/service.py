from odv import enum
from odv.database import model

class DatabaseService():
    def __init__(self, debug_type: enum.DebugType, environment_type: enum.EnvironmentType, database_type: enum.DatabaseType):
        self.debug_type: enum.DebugType = debug_type
        self.environment_type: enum.EnvironmentType = environment_type
        self.database_type: enum.DatabaseType = database_type
        
        