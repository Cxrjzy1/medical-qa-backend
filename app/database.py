# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# MySQL 连接地址
# root:123456 要和你的 MySQL 用户名、密码一致
DATABASE_URL = "mysql+pymysql://root:123456@localhost:3306/medical_qa?charset=utf8mb4"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()