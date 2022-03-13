import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from app.models import Base, Company
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
        self._delete_all()
        self._parsing_csv()

    def remove_session(self):
        self.session.remove()

    def _delete_all(self):
        self.session.query(Company).delete()

    def _parsing_csv(self):
        total_row_count = 0
        company_list = []
        with open('/wanted_temp_data.csv', encoding='utf-8') as f:
            lines = list(csv.reader(f, delimiter=","))
            for row in lines:
                if not total_row_count:
                    total_row_count += 1
                    continue
                company = Company()
                company.company_code = total_row_count
                company.locate = "ko"
                company.company_name = row[0]
                self.session.add(company)
                total_row_count += 1

            self.session.commit()

db = Database(SQLALCHEMY_DATABASE_URI, Base)

