from sqlalchemy import and_

from app.models import *
from utils.database import db


class CompanyDao:
    def __init__(self, db):
        self._table_name = Company.__tablename__
        self.db = db

    def get_all(self):
        return self.db.session().query(Company).all()

    def get_auto_search_by_company_name(self, company_name, lang):
        sub_query = db.session().query(CompanyName.company_code).filter(
            CompanyName.company_name.like("%{}%".format(company_name))).subquery()
        return self.db.session().query(CompanyName).filter(
            and_(CompanyName.company_code.in_(sub_query), CompanyName.language == lang)).all()

    def get_by_company_name(self, company_name, lang):
        sub_query = db.session().query(CompanyName.company_code).filter(
            CompanyName.company_name == company_name).subquery()
        return self.db.session().query(CompanyName).filter(
            and_(CompanyName.company_code.in_(sub_query), CompanyName.language == lang)).all()


companyDao = CompanyDao(db)
