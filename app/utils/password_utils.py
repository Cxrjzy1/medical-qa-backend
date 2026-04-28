# -*- coding: utf-8 -*-

from passlib.context import CryptContext

# 创建密码上下文对象
# bcrypt 是常用的密码哈希算法
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    对原始密码进行加密
    :param password: 原始密码
    :return: 加密后的密码
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    校验用户输入的原始密码是否和数据库中的加密密码匹配
    :param plain_password: 用户输入的原始密码
    :param hashed_password: 数据库中存储的加密密码
    :return: 是否匹配
    """
    return pwd_context.verify(plain_password, hashed_password)