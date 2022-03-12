from sqlalchemy import create_engine, Column, Integer, String, Text, Boolean, Float
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

Base = declarative_base()

class Company(Base):
    __tablename__ = "company"
    company_code: int
    locate: str
    company_name: str

    company_code = Column(Integer, primary_key=True)
    locate = Column(String(10), primary_key=True)
    company_name = Column(String(100), nullable=True, index=True)

    def __init__(self):
        self.company_name = None
        self.locate = None
        self.company_name = None

# class Tag(Base):
#     company_code: int
#     locate: str
#     tag_name: str
#
#     company_code = db.Column(db.Integer, primary_key=True)
#     locate = db.Column(db.String(10), primary_key=True)
#     tag_name = db.Column(db.String(100), nullable=True, index=True)
#
#     parent = db.relationship("Company", back_populates="tags", lazy="joined", innerjoin=True)
#
#     __tablename__ = "tag"
#     __table_args__ = {'mysql_collate': 'utf8_general_ci'}

