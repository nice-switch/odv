import inspect

from odv import enum, data


def execute(service: enum.ServiceType, args: list[str | enum.DatabaseType | enum.ExecutionType]):
    """Interface for running the application in a command-line environment.

    Args:
        service (odv.enum.ServiceType): Target service.
        args (list[str | odv.enum.DatabaseType | odv.enum.ExecutionType]): Args for the target service.
    """
    match service:
        case enum.ServiceType.DATABASE:
            execution_type: enum.ExecutionType | None = None
            database_type: enum.DatabaseType | None = None
            
            for arg in args:
                match type(arg):
                    case enum.ExecutionType:
                        execution_type = arg
                    case enum.DatabaseType:
                        database_type = arg
                    case _:
                        pass
            
            
            database_service = data.initialize_database(
                execution_type=execution_type,
                database_type=database_type
            )
            
            
        case enum.ServiceType.AUTHORIZATION:
            print("AUTH")