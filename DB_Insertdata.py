from DB_engine import engine
from DB_Creation import environment


def add_data(user_name, email, current_date):
    ins = environment.insert().values(
                                      name=user_name,
                                      email=email,
                                      date_and_time=current_date
                                      )
    connection = engine.connect()
    result = connection.execute(ins)
    result.close()

