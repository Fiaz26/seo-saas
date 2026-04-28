
from sqlalchemy import Column, Integer, String
from backend.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
    plan = Column(String, default="free")


class APIKey(Base):
    __tablename__ = "api_keys"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    key = Column(String, unique=True)
    usage = Column(Integer, default=0)
from sqlalchemy import Column, Integer, String

class BillingRequest(Base):
    __tablename__ = "billing_requests"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    plan = Column(String)
    status = Column(String, default="pending")
