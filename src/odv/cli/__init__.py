from odv import enum

def execute(service: enum.ServiceType, args: list[str]):
    """Interface for running the application in a command-line environment.

    Args:
        service (odv.enum.ServiceType): Target service.
        args (list[str]): Args for the target service.
    """
    match service:
        case enum.ServiceType.DATABASE:
            print("DB")
        case enum.ServiceType.AUTHORIZATION:
            print("AUTH")