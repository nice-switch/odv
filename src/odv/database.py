import fastapi, peewee

# WARNING i do not know what i am doing. i wanna try something neat with classes...
class BaseDatabase():
    def __init__(self, database_id: str | None = None):
        self.id: str = database_id

class DatabaseConnection(BaseDatabase):
    def __init__(self, database_id: str | None = None):
        BaseDatabase.__init__(
            self,
            database_id=database_id
        )
        

class DatabaseAPI(BaseDatabase):
    pass