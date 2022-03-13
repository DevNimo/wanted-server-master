import csv

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
        lang_set = ['ko', 'en', 'ja']
        for l in lang_set:  # Language Setting
            lang = Lang()
            lang.language = l
            self.session.add(lang)
        self.session.commit()

        with open('/wanted_temp_data.csv', encoding='utf-8') as f:
            lines = list(csv.reader(f, delimiter=","))
            for row in lines:
                if not total_row_count:
                    column = row
                    total_row_count += 1
                    continue
                company = Company()

                for c in company_row_list:
                    company_name = CompanyName()
                    company_name.language = column[c].split("_")[1]
                    company_name.company_name = row[c]
                    company.company_name.append(company_name)

                for t in tag_row_list:
                    for n in row[t].split("|"):
                        tag_name = TagName()
                        tag_name.language = column[t].split("_")[1]
                        tag_name.tag_name = n
                        company.tag_name.append(tag_name)

                self.session.add(company)
                total_row_count += 1

            self.session.commit()


db = Database(SQLALCHEMY_DATABASE_URI, Base)

