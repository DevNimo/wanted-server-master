from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from app.models import *
from config import SQLALCHEMY_DATABASE_URI


class Database(object):
    def __init__(self, db_url, base):
        self.engine = create_engine(db_url)
        self.base = base
        self.session = scoped_session(sessionmaker(autocommit=False,
                                                   autoflush=False,
                                                   bind=self.engine))

    def reconnect(self):
        self.engine.dispose()

    def init_db(self):
        self.base.metadata.create_all(bind=self.engine)

    def remove_session(self):
        self.session.remove()


class ComapnyDao:
    def __init__(self, db):
        self.db = db
        self._table_name = Company.__tablename__

    def get(self):
        return self.db.session.query(Company).all()


db = Database(SQLALCHEMY_DATABASE_URI, Base)
company_dao = ComapnyDao(db)
