from sqlalchemy import *
# from sqlalchemy import MetaData , MetaData use w/ multiple tables
from DB_engine import engine


meta = MetaData()

environment = Table('users', meta,
                    # collection of tables can be defined in the MetaData cataloge
                    Column('id', Integer, primary_key=True),
                    Column('name', String(20)),
                    Column('email', String(40)),
                    Column('date_and_time', String(40))
                    )


meta.create_all(engine)
