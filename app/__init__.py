from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from app.company.controller import company_api
import config
from app.models import Base
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


app = Flask(__name__)
app.config.from_object(config)
app.register_blueprint(company_api)
db = Database(SQLALCHEMY_DATABASE_URI, Base)

db.init_db()
app.config['my_database'] = db


