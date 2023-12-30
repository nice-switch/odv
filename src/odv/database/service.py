import peewee

from odv.enum.database import DatabaseType, DatabaseInfo
from odv.database import model

class DatabaseService():
    """_summary_
    """
    def __init__(self, database_type: DatabaseType, database_info: DatabaseInfo):
        """_summary_

        Args:
            database_type (DatabaseType): _description_
            database_info (DatabaseInfo): _description_
        """
        self.database_type: DatabaseType = database_type
        self.database_info: DatabaseInfo = database_info
        self.peewee_connection: peewee.SqliteDatabase


    def create_database_connection(self):
        """_summary_

        Raises:
            Exception: _description_
        """
        match self.database_type:
            case DatabaseType.SQLITE:
                self.peewee_connection = peewee.SqliteDatabase(self.database_info.value)
                self.peewee_connection.connect()
                model.database_connection = self.peewee_connection

            case _:
                raise Exception("GUHHHHHH???")
    

    def initialize_database_tables(self):
        """_summary_
        """
        self.peewee_connection.connect()
        self.peewee_connection.create_tables(model.AccountData)