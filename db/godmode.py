from datetime import datetime

from sqlalchemy import Integer, Column, DateTime, String, ForeignKey, Boolean

from base.db import BaseDatabase


class GodModeDatabase(BaseDatabase):
    dsn = "sqlite:///internal/godmode.sqlite"


GodModeDatabase.bind()


class UsersTable(GodModeDatabase.TableBase):
    __tablename__ = "gm_users"

    id = Column(Integer, primary_key=True)
    login = Column(String(32), unique=True)
    password = Column(String(64))
    acl = Column(String(16))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class PoliciesTable(GodModeDatabase.TableBase):
    __tablename__ = "gm_policies"

    id = Column(Integer, primary_key=True)
    godmode_user_id = Column(Integer, nullable=False)
    policy = Column(String(128), nullable=False)
    params = Column(String(128), nullable=True)
    has_access = Column(Boolean, nullable=False)
    is_enabled = Column(Boolean, nullable=False)


class SessionsTable(GodModeDatabase.TableBase):
    __tablename__ = "gm_sessions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("gm_users.id"))
    token = Column(String(32))
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class LogTable(GodModeDatabase.TableBase):
    __tablename__ = "gm_log"

    id = Column(Integer, primary_key=True)
    user = Column(String(32))
    model = Column(String(64))
    action = Column(String(512))
    ids = Column(String(4096))
    details = Column(String(512))
    reason = Column(String(64))
    created_at = Column(DateTime, default=datetime.now)
