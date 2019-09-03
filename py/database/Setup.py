from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from py.Config import Config


engine = create_engine(Config.DB_LOCATION.value, echo=False)

session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = session.query_property()

def reset_data():
	# I don't know why, but putting this in a separate method and then calling it seemed to work.
	# It should have automatically run on app creation, I would have thought... weird.
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)


"""
This is currently unused; currently what's happening is that the session is created on program start,
and then closed
"""
@contextmanager
def create_session(*, is_init: bool = False) -> scoped_session:
	engine = create_engine(Config.DB_LOCATION.value, echo=True)  # "echo" is verbose mode (default: False)

	# I'm keeping the defaults of autoflush=True and autocommit=False.
	session = scoped_session(sessionmaker(bind=engine))

	if is_init:
		Base.metadata.drop_all(engine)
		Base.metadata.create_all(engine)

	Base.query = session.query_property()

	try:
		yield session
		...
		session.commit()
	except Exception as e:
		session.rollback()
		raise e
	finally:
		session.remove()


def close_session():
	global session

	session.remove()
	del session