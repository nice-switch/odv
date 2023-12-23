import fastapi, peewee

from odv import enum
from uuid import uuid4

# WARNING i do not know what i am doing. i wanna try something neat with classes...        

peewee_database_connection: peewee.Database

class BaseModel(peewee.Model):
    class Meta:
        database = peewee_database_connection

class DatabaseAPI():
    def __init__(self, database_type: enum.DatabaseType):
        self.type: enum.DatabaseType = database_type
        self.fast_api: fastapi.FastAPI = fastapi.FastAPI()
    
    def initialize_api_endpoints(self):
        pass
    

class DatabaseService():
    def __init__(self, database_api: DatabaseAPI):
        self.api: DatabaseAPI = database_api
        self.type: enum.DatabaseType = database_api.type
        
        self.port: enum.DatabasePort
        self.host: enum.DatabaseHost
        
        match self.type:
            case enum.DatabaseType.PRODUCTION:
                self.port = enum.DatabasePort.PRODUCTION
                self.host = enum.DatabaseHost.LOCALHOST
            case enum.DatabaseType.DEVELOPMENT:
                self.port = enum.DatabasePort.DEVELOPMENT
                self.host = enum.DatabaseHost.MACHINE
            case _:
                raise Exception("GUHHH WHA DA FOOOOOAHAHH?? " + str(_))
    
    def initialize_peewee_connection(self):
        global peewee_database_connection
        
        match self.type:
            case enum.DatabaseType.PRODUCTION:
                peewee_database_connection = peewee.SqliteDatabase("data/production.sqlite")
            case enum.DatabaseType.DEVELOPMENT:
                peewee_database_connection = peewee.SqliteDatabase("data/development.sqlite")
            case _:
                raise Exception("Uhhh, Excuse me I think the word you're searching for is 'Space Ranger'.")
        
        # TODO create check checking if the databsae is new and stuff needs to be initialized.