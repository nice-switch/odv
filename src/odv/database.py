import fastapi, peewee

from odv import enum
from uuid import uuid4

# WARNING i do not know what i am doing. i wanna try something neat with classes...        

class DatabaseAPI():
    def __init__(self, database_type: enum.DatabaseType):
        self.type: enum.DatabaseType = database_type
        self.fast_api: fastapi.FastAPI = fastapi.FastAPI()
    
    def initialize_peewee_connection(self):
        pass
    
    def initialize_api_endpoints(self):
        pass
    

class DatabaseService():
    def __init__(self, database_api: DatabaseAPI):
        self.api: DatabaseAPI = database_api
        self.type: enum.DatabaseType = database_api.type
        
        self.port: enum.DatabasePort
        self.host: enum.DatabaseHost
        
        match self.api.type:
            case enum.DatabaseType.PRODUCTION:
                self.port = enum.DatabasePort.PRODUCTION
                self.host = enum.DatabaseHost.LOCALHOST
            case enum.DatabaseType.DEVELOPMENT:
                self.port = enum.DatabasePort.DEVELOPMENT
                self.host = enum.DatabaseHost.MACHINE
            case _:
                raise Exception("GUHHH WHA DA FOOOOOAHAHH?? " + str(_))