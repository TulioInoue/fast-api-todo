from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os

SQLALCHEMY_DATABASE_URL = os.getenv(key = "DATABASE_URL", default = "mysql+pymysql://root:My_SQL_Tulio_1!!!@127.0.0.1:3306/posts")

# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:My_SQL_Tulio_1!!!@127.0.0.1:3306/posts"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)

Base = declarative_base()
