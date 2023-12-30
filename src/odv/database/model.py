import peewee

# NOTE/TODO is this okay??...
database_connections: dict[ str: 
    peewee.SqliteDatabase | 
    peewee.PostgresqlDatabase | 
    peewee.MySQLDatabase
] = {}

class BaseModel(peewee.Model):
    def __init__(self, connection_index: str):
        self.connection_index = connection_index
    
    class Meta:
        def __init__(self):
            self.database = database_connections[self.connection_index]



"""class BaseModel(peewee.Model):
    target_path: str = ""
    class Meta:
        def __init__():
            database = database_connections[target_path]"""