import peewee

from odv import enum

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