from sqlalchemy import and_

from app.models import *
from utils.database import db


class TagDao:
    def __init__(self, db):
        self._table_name = TagName.__tablename__
        self.db = db

    def get_by_company_name(self, company_name, lang):
        sub_query = db.session().query(CompanyName.company_code).filter(
            CompanyName.company_name == company_name).subquery()
        return self.db.session().query(TagName).filter(
            and_(TagName.company_code.in_(sub_query), TagName.language == lang)).all()


tagDao = TagDao(db)
