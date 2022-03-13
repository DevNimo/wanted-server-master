from app.models import *
from utils.database import db


class CompanyDao:
    def __init__(self, db):
        self._table_name = Company.__tablename__
        self.db = db

    def get_all(self):
        return self.db.session().query(Company).all()


companyDao = CompanyDao(db)
