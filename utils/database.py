import csv
from sqlalchemy import and_

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from app.models import Base, Company, CompanyName, Lang, TagName
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
        self._drop_all()
        self.base.metadata.create_all(bind=self.engine)
        self._parsing_csv()

    def remove_session(self):
        self.session.remove()

    def _drop_all(self):
        self.base.metadata.drop_all(self.engine)

    def _parsing_csv(self):
        total_row_count = 0
        company_row_list = [0, 1, 2]
        tag_row_list = [3, 4, 5]
        column = []
        lang_set = ['ko', 'en', 'jp']
        for l in lang_set:  # Language Setting
            lang = Lang()
            lang.language = l
            self.session.add(lang)
        self.session.commit()

        with open('wanted_temp_data.csv', encoding='utf-8') as f:
            lines = list(csv.reader(f, delimiter=","))
            for row in lines:
                if not total_row_count:
                    column = row
                    total_row_count += 1
                    continue
                company = Company()

                for c in company_row_list:
                    company_name = CompanyName()
                    _lang = column[c].split("_")[1]
                    company_name.language = _lang if _lang != 'ja' else 'jp'
                    company_name.company_name = row[c]
                    company.company_name.append(company_name)

                for t in tag_row_list:
                    for n in row[t].split("|"):
                        tag_name = TagName()
                        _lang = column[t].split("_")[1]
                        tag_name.language = _lang if _lang != 'ja' else 'jp'
                        tag_name.tag_name = n
                        company.tag_name.append(tag_name)

                self.session.add(company)
                total_row_count += 1

            self.session.commit()


db = Database(SQLALCHEMY_DATABASE_URI, Base)

import logging
logging.basicConfig(format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
    datefmt='%Y-%m-%d:%H:%M:%S',
    level=logging.DEBUG)


def check_new_language(lang):
    _lang = db.session().query(Lang.language).filter(Lang.language == lang).scalar()
    logging.info(_lang)
    if _lang is None:
        new_lang = Lang()
        new_lang.language = lang
        db.session.add(new_lang)
        db.session.commit()


def check_duplicate_tag_name(tag: TagName):
    _check = db.session().query(TagName).filter(and_(
        TagName.company_code == tag.company_code,
        TagName.language == tag.language,
        TagName.tag_name == tag.tag_name)).scalar()
    return False if _check is None else True

