from sqlalchemy import create_engine

engine = create_engine('sqlite:///game_env.db', echo=True, pool_pre_ping=True)