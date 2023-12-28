from odv import enum
from odv.database import model, service


def create_database_service(database_type: enum.LaunchParameter) -> service.DatabaseService | None:
    pass