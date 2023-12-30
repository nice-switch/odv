import odv

dev_db_service = odv.database.service.DatabaseService(
    database_type=odv.enum.database.DatabaseType.SQLITE,
    database_info=odv.enum.database.DatabaseInfo.DEVELOPMENT_SQLITE_PATH
)


prod_db_service = odv.database.service.DatabaseService(
    database_type=odv.enum.database.DatabaseType.SQLITE,
    database_info=odv.enum.database.DatabaseInfo.PRODUCTION_SQLITE_PATH
)


dev_db_service.create_database_connection()
prod_db_service.create_database_connection()