from odv import enum, database

def __convert_parameters_to_ordered_tuple(parameters: list[enum.LaunchParameter]) -> tuple[enum.DebugType, enum.EnvironmentType, enum.DatabaseType | None]:
    """_summary_

    Args:
        parameters (list[enum.LaunchParameter]): _description_

    Raises:
        Exception: _description_

    Returns:
        tuple[enum.DebugType | enum.DebugType.NO_OUTPUT, enum.EnvironmentType | None, enum.DatabaseType | None]: _description_
    """
    debug_type: enum.DebugType | enum.DebugType.NO_OUTPUT = enum.DebugType.NO_OUTPUT
    environment_type: enum.EnvironmentType | enum.EnvironmentType.DEVELOPMENT = None
    database_type: enum.DatabaseType | enum.DatabaseType.SQLITE = None
    
    for parameter in parameters:
        match type(parameter):
            case enum.DebugType:
                debug_type = parameter
            case enum.EnvironmentType:
                environment_type = parameter
            case enum.DatabaseType:
                database_type = parameter
            case _:
                raise Exception("HUHHHHHH??")
    
    return debug_type, environment_type, database_type


def execute(service_type: enum.ServiceType, launch_parameters: list[enum.LaunchParameter]):
    """_summary_

    Args:
        service_type (enum.ServiceType): _description_
        launch_parameters (list[enum.LaunchParameter]): _description_
    """
    
    debug_type, environment_type, database_type = __convert_parameters_to_ordered_tuple(parameters=launch_parameters)
    
    match service_type:
        case enum.ServiceType.DATABASE:
            database_service: database.DatabaseService | None = database.create_database_service(debug_type=debug_type, environment_type=environment_type, database_type=database_type)
            database_service.create_database_connection()
            database_service.validate_database_models()