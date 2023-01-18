from peewee import *

db = SqliteDatabase('db/database.db')


class BaseModel(Model):
    class Meta:
        database = db


class Device(BaseModel):
    id = IntegerField(primary_key=True)
    name = CharField()
    sn = IntegerField(unique=True)

    class Meta:
        order_by = id
        db_table = 'devices'


class Request(BaseModel):
    uuid = CharField(primary_key=True, unique=True)
    to = CharField()
    frmo = CharField()
    device_id = ForeignKeyField(Device, backref="Request")

    class Meta:
        db_table = 'requests'
