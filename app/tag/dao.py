from sqlalchemy import and_, func
from app.models import *
from utils.database import db, check_new_language, check_duplicate_tag_name


class TagDao:
    def __init__(self, db):
        self.db = db

    def get_by_company_name(self, company_name, lang):
        sub_query = db.session().query(CompanyName.company_code).filter(
            CompanyName.company_name == company_name).subquery()
        return self.db.session().query(TagName).filter(
            and_(TagName.company_code.in_(sub_query), TagName.language == lang)).all()

    def get_compnay_by_tag(self, tag_name):
        sub_name = self.db.session().query(TagName.company_code).filter(
            TagName.tag_name == tag_name).subquery()
        return self.db.session().query(CompanyName).filter(and_(
            CompanyName.company_code.in_(sub_name), CompanyName.company_name != "")).all()

    def tag_update_by_company(self, company_name, json_data):
        company_code = self.db.session().query(CompanyName.company_code).filter(
            CompanyName.company_name == company_name).scalar()
        for obj in json_data:
            for key in obj['tag_name']:
                check_new_language(key)
                tag = TagName()
                tag.company_code = company_code
                tag.language = key
                tag.tag_name = obj['tag_name'][key]
                if not check_duplicate_tag_name(tag):
                    self.db.session.add(tag)

        self.db.session.commit()

    def delete_tag_by_company(self, company_name, tag_name, lang):
        company_code = self.db.session().query(CompanyName.company_code).filter(
            CompanyName.company_name == company_name).scalar()
        tag_split = tag_name.split('_')
        tag_split_len = len(tag_split)
        tag_num = "_".join(tag_split[1:])
        self.db.session.query(TagName).filter(and_(
            func.substring_index(TagName.tag_name, '_', -(tag_split_len-1)) == tag_num,
            TagName.company_code == company_code)).delete(synchronize_session='fetch')
        self.db.session.commit()


tagDao = TagDao(db)
