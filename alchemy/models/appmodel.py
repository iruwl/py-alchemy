from sqlalchemy import Column, DateTime, ForeignKey, Integer, SmallInteger, String, text
from sqlalchemy.orm import relationship

from .meta import Base


class App(Base):
    __tablename__ = 'apps'
    __table_args__ = {u'schema': 'app'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    kode = Column(String, nullable=False, unique=True)
    nama = Column(String, nullable=False, unique=True)
    path = Column(String, nullable=False)
    is_active = Column(SmallInteger, server_default=text("1"))
    is_locked = Column(SmallInteger, server_default=text("0"))
    created_by = Column(String(12))
    created_at = Column(DateTime)
    updated_by = Column(String(12))
    updated_at = Column(DateTime)


class RolePermission(Base):
    __tablename__ = 'role_permissions'
    __table_args__ = {u'schema': 'app'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    role_id = Column(ForeignKey(u'app.roles.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)
    route_id = Column(ForeignKey(u'app.routes.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)
    created_by = Column(String(12))
    created_at = Column(DateTime)
    updated_by = Column(String(12))
    updated_at = Column(DateTime)

    role = relationship(u'Role')
    route = relationship(u'Route')


class Role(Base):
    __tablename__ = 'roles'
    __table_args__ = {u'schema': 'app'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    app_id = Column(ForeignKey(u'app.apps.id', ondelete=u'CASCADE', onupdate=u'CASCADE'), nullable=False)
    kode = Column(String, nullable=False, unique=True)
    nama = Column(String, nullable=False, unique=True)
    is_active = Column(SmallInteger, server_default=text("1"))
    is_locked = Column(SmallInteger, server_default=text("0"))
    created_by = Column(String(12))
    created_at = Column(DateTime)
    updated_by = Column(String(12))
    updated_at = Column(DateTime)

    app = relationship(u'App')


class Route(Base):
    __tablename__ = 'routes'
    __table_args__ = {u'schema': 'app'}

    id = Column(Integer, primary_key=True, autoincrement=True)
    kode = Column(String, nullable=False, unique=True)
    nama = Column(String, nullable=False, unique=True)
    path = Column(String, nullable=False)
    is_active = Column(SmallInteger, server_default=text("1"))
    is_hidden = Column(SmallInteger, server_default=text("0"))
    created_by = Column(String(12))
    created_at = Column(DateTime)
    updated_by = Column(String(12))
    updated_at = Column(DateTime)


class User(Base):
    __tablename__ = 'users'
    __table_args__ = {u'schema': 'app'}

    id = Column(String(12), primary_key=True)
    pwd = Column(String, nullable=False)
    nama = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    nip = Column(String)
    jabatan = Column(String)
    handphone = Column(String)
    is_active = Column(SmallInteger, server_default=text("1"))
    is_locked = Column(SmallInteger, server_default=text("0"))
    is_superuser = Column(SmallInteger, server_default=text("0"))
    last_login = Column(DateTime)
    created_by = Column(String(12))
    created_at = Column(DateTime)
    updated_by = Column(String(12))
    updated_at = Column(DateTime)
