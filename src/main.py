import odv

from odv.enum import database as db_enum

dev_db_service = odv.database.service.DatabaseService(
    database_type=db_enum.DatabaseType.SQLITE,
    database_info=db_enum.DatabaseInfo.DEVELOPMENT_SQLITE_PATH
)


prod_db_service = odv.database.service.DatabaseService(
    database_type=db_enum.DatabaseType.SQLITE,
    database_info=db_enum.DatabaseInfo.PRODUCTION_SQLITE_PATH
)


dev_db_service.create_database_connection()
prod_db_service.create_database_connection()