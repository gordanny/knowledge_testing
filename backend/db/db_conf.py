import os
from contextlib import contextmanager
from functools import lru_cache
from typing import Generator

from sqlalchemy.engine import Engine, create_engine, Connection
from sqlalchemy.orm import sessionmaker, Session


class DbConfig:

    def __init__(self, type: str, host: str, port: int, user: str, password: str,
                 base: str, app_name: str = 'knowledge_testing', charset: str = 'utf8',
                 pool_recycle: int = 15):
        self.type = type
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.base = base
        self.app_name = app_name
        self.charset = charset
        self.pool_recycle = pool_recycle
        self.check_connection_config()

    def check_connection_config(self) -> None:
        required_fields = [
            'host',
            'port',
            'user',
            'password',
            'base',
            'app_name',
            'type'
        ]
        for field in required_fields:
            if field not in dir(self):
                raise Exception('required field for connection not found: ' + field)
            if not getattr(self, field):
                raise Exception(f'field {field} is None')


class Database:

    def __init__(self, config: DbConfig):
        self.config = config

    def get_dsn_connection_string(self) -> str:
        dsn = self.config.type + '://' + self.config.user + ':' + self.config.password + '@' + self.config.host + ':' +\
            str(self.config.port) + '/' + self.config.base
        if self.config.type == 'mysql+pymysql':
            dsn += '?charset=utf8'
        if self.config.type == 'postgresql':
            dsn += '?application_name=' + self.config.app_name
        return dsn

    @lru_cache(maxsize=None)
    def get_engine(self) -> Engine:
        dsn = self.get_dsn_connection_string()
        return create_engine(dsn, pool_recycle=self.config.pool_recycle,
                             connect_args={'application_name': self.config.app_name} if self.config.type == 'postgresql'
                             else {})

    @contextmanager
    def get_connect(self) -> Connection:
        engine = self.get_engine()
        connection = None
        try:
            connection = engine.connect()
            yield connection
        finally:
            if connection is not None:
                connection.detach()
                connection.close()

    @contextmanager
    def get_session(self) -> Generator[Session, None, None]:
        engine = self.get_engine()
        session = sessionmaker()
        s = None
        try:
            session.configure(bind=engine)
            s = session()
            yield s
        finally:
            if s is not None:
                s.close()


database = Database(config=DbConfig(
    type=os.getenv('DB_TYPE', 'postgresql'),
    host=os.getenv('DB_HOST', 'localhost'),
    port=int(os.getenv('DB_PORT', 5432)),
    user=os.getenv('DB_USER', 'admin'),
    password=os.getenv('DB_PASS', 'root'),
    base=os.getenv('DB_NAME', 'knowledge_testing')
))
