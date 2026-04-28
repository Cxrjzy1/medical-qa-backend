# -*- coding: utf-8 -*-

from jose import jwt
from datetime import datetime, timedelta

# JWT 密钥
# 实际项目里不要直接写死，后面我们会改成配置文件读取
SECRET_KEY = "your-secret-key"

# 加密算法
ALGORITHM = "HS256"

# token 过期时间（分钟）
ACCESS_TOKEN_EXPIRE_MINUTES = 60


def create_access_token(data: dict):
    """
    生成 JWT token
    :param data: 需要写入 token 的数据，例如 user_id
    :return: 生成后的 token 字符串
    """
    # 复制一份数据，避免直接修改原字典
    to_encode = data.copy()

    # 设置 token 过期时间
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    # 生成 token
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_token(token: str):
    """
    校验并解析 token
    :param token: 前端传来的 JWT token
    :return: 解析后的 payload；如果失败则返回 None
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except Exception:
        return None