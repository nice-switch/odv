import peewee

from odv.enum.database import DatabaseInfo

# NOTE/TODO is this okay??...
database_connection: peewee.SqliteDatabase | peewee.PostgresqlDatabase | peewee.MySQLDatabase | None = peewee.SqliteDatabase(":memory:")

class BaseModel(peewee.Model):
    class Meta:
        database = database_connection

class AccountData(BaseModel):
    username = peewee.TextField(primary_key=True,index=True,unique=True)
    password = peewee.TextField()
    salt = peewee.TextField()
    data = peewee.TextField()


class VaultData(BaseModel):
    id = peewee.TextField(primary_key=True, index=True, unique=True)
    data = peewee.TextField()

"""class BaseModel(peewee.Model):
    target_path: str = ""
    class Meta:
        def __init__():
            database = database_connections[target_path]"""