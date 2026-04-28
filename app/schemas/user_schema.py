from pydantic import BaseModel

# 用户注册 / 登录请求体
class UserRequest(BaseModel):
    username: str
    password: str

# 用户响应体
class UserResponse(BaseModel):
    id: int
    username: str