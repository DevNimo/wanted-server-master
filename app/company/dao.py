from app.models import *
from utils.database import db


class CompanyDao:
    def __init__(self, db):
        self._table_name = Company.__tablename__
        self.db = db

    def get_all(self):
        return self.db.session().query(Company).all()

    def get_auto_search_by_company_name(self, company_name):
        return self.db.session().query(Company).filter(Company.company_name.like("{}%".format(company_name))).all()


companyDao = CompanyDao(db)
