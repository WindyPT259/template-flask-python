from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    TIMESTAMP,
    Boolean,
)
from src.models.db import db


class UserApp(db.Model):
    __tablename__ = "user_app"
    _table_args_ = {"extend_existing": True}
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    username = Column(String(255), nullable=False, unique=True)
    full_name = Column(String(255), default=None)
    email = Column(String(255), nullable=False, unique=True)
    phone_number = Column(String(255), default=None)
    report_access = Column(Boolean, default=None)
    view_costs = Column(Boolean, default=None)
    last_login_date = Column(TIMESTAMP, default=None)
    enabled = Column(Boolean, nullable=False, default=True, server_default="1")
    is_corporated = Column(Boolean, nullable=False, default=False, server_default="0")
    created_on = Column(DateTime, default=None)
    modified_on = Column(DateTime, default=None)

    def __init__(
        self,
        username,
        full_name,
        email,
        phone_number,
        report_access,
        view_costs,
        last_login_date,
        enabled,
        is_corporated,
        created_on,
        modified_on,
    ):
        self.username = username
        self.full_name = full_name
        self.email = email
        self.phone_number = phone_number
        self.report_access = report_access
        self.view_costs = view_costs
        self.last_login_date = last_login_date
        self.enabled = enabled
        self.is_corporated = is_corporated
        self.modified_on = modified_on
        self.created_on = created_on

    def __repr__(self) -> str:
        return "<UserApp {}>".format(self.username)
