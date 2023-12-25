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
        self.execution_type: enum.ExecutionType = execution_type
        self.database_type: enum.DatabaseType = database_type

        print(f"DatabaseService created! Attempting to establish a {database_type} connection.")

        # TODO there is a much, much better way to do this.
        match database_type:
            case enum.DatabaseType.SQLITE:
                database_connection = peewee.SqliteDatabase("data/" + execution_type)
            case enum.DatabaseType.POSTGRES:
                # TODO compatibility for this should be plug and play but not sure. Will test this later
                raise Exception("Postgresql is not fully tested yet!")
                #database_connection = peewee.PostgresqlDatabase("data/" + execution_type)
            case _:
                raise Exception("Expected a valid DatabaseType!")
        
        print("DatabaseService connected and initialized!")


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