from odv import enum, database

# NOTE do i make two versions of the CLI/interface? One sync & one async?

def __get_datatype_from_parameters(parameters: list[enum.LaunchParameter]) -> enum.DatabaseType | None:
    """_summary_

    Args:
        parameters (list[enum.LaunchParameter]): _description_

    Returns:
        enum.DatabaseType | None: _description_
    """
    for launch_parameter in parameters:
        match type(launch_parameter):
            case enum.DatabaseType:
                return launch_parameter


def execute(service_type: enum.ServiceType, launch_parameters: list[enum.LaunchParameter]):
    """_summary_

    Args:
        service_type (enum.ServiceType): _description_
        launch_parameters (list[enum.LaunchParameter]): _description_
    """
    match service_type:
        case enum.ServiceType.DATABASE:
            database_type: enum.DatabaseType | None = __get_datatype_from_parameters(parameters=launch_parameters)
            database_service: database.service.DatabaseService | None = database.create_database_service(database_type=database)
            