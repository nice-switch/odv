import peewee

from odv.database import model

from odv.enum.database import DatabaseType, DatabaseInfo

class DatabaseService():
    def __init__(self, database_type: DatabaseType, database_info: DatabaseInfo):
        self.database_type: DatabaseType = database_type
        self.database_info: DatabaseInfo = database_info
        self.peewee_connection: peewee.SqliteDatabase

    def create_database_connection(self):
        database_info_value = self.database_info.value

        match self.database_type:
            case DatabaseType.SQLITE:
                self.peewee_connection = peewee.SqliteDatabase(database_info_value)
                self.peewee_connection.connect()

                model.database_connections[database_info_value] = self.peewee_connection

            case _:
                raise Exception("GUHHHHHH???")