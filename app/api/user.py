from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserRequest, UserResponse
from app.services.user_service import create_user, login_user
from app.utils.jwt_utils import create_access_token
# 创建用户路由
router = APIRouter(prefix="/user", tags=["user"])

# 用户注册接口
@router.post("/register", response_model=UserResponse)
def register(req: UserRequest):
    # 调用 service 创建用户
    user = create_user(req.username, req.password)

    # 如果用户名已存在，返回 400 错误
    if user is None:
        raise HTTPException(status_code=400, detail="用户名已存在")

    return {
        "id": user.id,
        "username": user.username
    }

# 用户登录接口
@router.post("/login")
def login(req: UserRequest):
    user = login_user(req.username, req.password)

    if user is None:
        raise HTTPException(status_code=401, detail="用户名或密码错误")

    # 👉 生成 token（核心）
    token = create_access_token({
        "user_id": user.id,
        "username": user.username
    })

    return {
        "msg": "登录成功",
        "access_token": token,
        "token_type": "bearer"
    }