import peewee

from odv import enum

class DatabaseService():
    def __init__(self, execution_type: enum.ExecutionType, database_type: enum.DatabaseType):
        self.execution_type: enum.ExecutionType = execution_type
        self.database_type: enum.DatabaseType = database_type


def initialize_database(execution_type: enum.ExecutionType, database_type: enum.DatabaseType) -> DatabaseService | None:
    return DatabaseService(
        execution_type=execution_type,
        database_type=database_type
    )