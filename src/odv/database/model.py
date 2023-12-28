import peewee

database_connection: peewee.SqliteDatabase | peewee.PostgresqlDatabase | None = None

class BaseModel(peewee.Model):
    class Meta:
        database = database_connection

class AccountModel(BaseModel):
    username = peewee.TextField(primary_key=True, index=True)
    password = peewee.TextField() # NOTE input processing will handle lengths.
    email = peewee.TextField()
    salt = peewee.TextField()
    data = peewee.TextField()