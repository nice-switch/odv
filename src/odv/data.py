import peewee

from odv import enum

database_connection: peewee.SqliteDatabase | peewee.PostgresqlDatabase | None = None


class BaseModel(peewee.Model):
    class Meta:
        database = database_connection


class DatabaseService():
    """Main interface for data management.
    """
    def __init__(self, execution_type: enum.ExecutionType, database_type: enum.DatabaseType):
        """Main interface for data management initialization.
        (You shouldn't be creating this by yourself, use odv.data.initialize_database(...))

        Args:
            execution_type (enum.ExecutionType): Changes how the service will run. Ports, logging, etc,.
            database_type (enum.DatabaseType): What database to use when launching the application.
        """
        print("DatabaseService created! Initializing...")
        self.execution_type: enum.ExecutionType = execution_type
        self.database_type: enum.DatabaseType = database_type

        # TODO this is a much much better way to do this probably.
        match execution_type:
            case enum.ExecutionType.PRODUCTION:
                print("DatabaseService is in PRODUCTION mode!")
                match database_type:
                    case enum.DatabaseType.SQLITE:
                        print("DatabaseService establishing SQLITE connection with data/" + self.execution_type)
                        database_connection = peewee.SqliteDatabase("data/" + self.execution_type)
                    case enum.DatabaseType.POSTGRES:
                        print("DatabaseService establishing POSTGRESQL connection with data/" + self.execution_type)
                        database_connection = peewee.PostgresqlDatabase("data/" + self.execution_type)
                    case _:
                        pass
                    
            case enum.ExecutionType.DEVELOPMENT:
                print("DatabaseService in DEVELOPMENT mode!")
                match database_type:
                    case enum.DatabaseType.SQLITE:
                        print("DatabaseService establishing SQLITE connection with data/" + self.execution_type)
                        database_connection = peewee.SqliteDatabase("data/" + self.execution_type)
                    case enum.DatabaseType.POSTGRES:
                        print("DatabaseService establishing POSTGRESQL connection with data/" + self.execution_type)
                        database_connection = peewee.PostgresqlDatabase("data/" + self.execution_type)
                    case _:
                        pass
        
        print(f"DatabaseService __init__ finished!: {execution_type}, {database_type}")

    



def initialize_database(execution_type: enum.ExecutionType, database_type: enum.DatabaseType) -> DatabaseService | None:
    """Creates DatabaseService and does some pre-requisite configuration.

    Args:
        execution_type (enum.ExecutionType): Changes how the service will run. Ports, logging, etc,.
        database_type (enum.DatabaseType): What database to use when launching the application.

    Returns:
        DatabaseService | None: If the combination of args are correct it will create DatabaseService. Failure will return None.
    """
    return DatabaseService(
        execution_type=execution_type,
        database_type=database_type
    )