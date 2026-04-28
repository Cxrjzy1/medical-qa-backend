from sqlalchemy import Column, Integer, String
from app.database import Base

# 用户表模型
class User(Base):
    # 数据库表名
    __tablename__ = "users"

    # 用户 id，主键，自增
    id = Column(Integer, primary_key=True, index=True)

    # 用户名，不能为空，唯一
    username = Column(String(50), unique=True)

    # 密码，不能为空
    password = Column(String(255))