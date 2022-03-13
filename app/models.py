from sqlalchemy import Column, Integer, String, Text, Boolean, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relation

Base = declarative_base()


class Company(Base):
    __tablename__ = "company"
    company_code: int

    company_code = Column(Integer, primary_key=True, autoincrement=True)
    company_name = relation('CompanyName')
    tag_name = relation('TagName')

    def __init__(self):
        self.company_code = None


class CompanyName(Base):
    __tablename__ = "company_name"
    id: int
    company_code: int
    # language: str
    company_name: str

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_code = Column(Integer, ForeignKey('company.company_code'))
    language = Column(String(10), ForeignKey('lang.language'))
    company_name = Column(String(100), nullable=True)

    def __init__(self):
        self.id = None
        self.company_name = None


class Lang(Base):
    __tablename__ = "lang"
    language: str
    language = Column(String(10), primary_key=True)

    company_name = relation('CompanyName')
    tag_name = relation('TagName')

    def __init__(self):
        self.language = None


class TagName(Base):
    __tablename__ = "tag_name"
    id: int
    company_code: int
    tag_name: str

    id = Column(Integer, primary_key=True, autoincrement=True)
    company_code = Column(Integer, ForeignKey('company.company_code'))
    language = Column(String(10), ForeignKey('lang.language'))
    tag_name = Column(String(100), nullable=True)

    def __init__(self):
        self.id = None
