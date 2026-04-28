from app.database import SessionLocal
from app.models.user import User
from app.utils.password_utils import hash_password, verify_password


def create_user(username, password):
    """
    创建用户
    注册时先检查用户名是否存在，再对密码进行加密后保存
    """
    db = SessionLocal()
    try:
        # 检查用户名是否已存在
        existing_user = db.query(User).filter(User.username == username).first()
        if existing_user:
            return None

        # 对密码进行加密
        hashed_password = hash_password(password)

        # 创建用户对象，保存加密后的密码
        user = User(username=username, password=hashed_password)

        db.add(user)
        db.commit()
        db.refresh(user)

        return user
    finally:
        db.close()


def login_user(username, password):
    """
    用户登录
    先根据用户名查用户，再校验密码是否正确
    """
    db = SessionLocal()
    try:
        # 先根据用户名查询用户
        user = db.query(User).filter(User.username == username).first()

        # 用户不存在
        if user is None:
            return None

        # 校验密码
        if not verify_password(password, user.password):
            return None

        return user
    finally:
        db.close()