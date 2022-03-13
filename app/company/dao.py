from sqlalchemy import and_, func

from app.models import *
from utils.database import db, check_new_language, check_duplicate_tag_name



class CompanyDao:
    def __init__(self, db):
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

    def new_company(self, json_data, lang):
        check_new_language(lang)
        company = Company()
        _company_name = json_data['company_name']
        for key in _company_name:
            company_name = CompanyName()
            company_name.language = key
            company_name.company_name = _company_name[key]
            company.company_name.append(company_name)

        _tags = json_data['tags']
        for _tag in _tags:
            _tag_name = _tag['tag_name']
            for key in _tag_name:
                check_new_language(lang)
                tag_name = TagName()
                tag_name.language = key
                tag_name.tag_name = _tag_name[key]
                if not check_duplicate_tag_name(tag_name):
                    company.tag_name.append(tag_name)
        self.db.session.add(company)
        self.db.session.commit()
        return company_name.company_name


companyDao = CompanyDao(db)
