from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.schemas.qa_schema import QuestionRequest, QuestionResponse
from app.services.qa_service import save_question, get_history, generate_answer
from app.utils.jwt_utils import verify_token

# 创建路由对象
router = APIRouter(tags=["qa"])

# 定义 Bearer Token 认证方式
security = HTTPBearer()


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    """
    获取当前登录用户
    从请求头中拿到 token，校验 token 是否有效
    """
    token = credentials.credentials
    payload = verify_token(token)

    if payload is None:
        raise HTTPException(status_code=401, detail="token无效或已过期")

    return payload


@router.post("/qa", response_model=QuestionResponse)
def ask(req: QuestionRequest, user=Depends(get_current_user)):
    """
    问答接口
    1. 校验用户身份
    2. 根据问题生成回答
    3. 保存问答历史
    4. 返回结果
    """

    # 调用 service 层的问答逻辑
    answer = generate_answer(req.question)

    # 保存历史记录
    save_question(req.question, answer)

    # 返回响应
    return {
        "question": req.question,
        "answer": answer
    }


@router.get("/history")
def history(user=Depends(get_current_user)):
    """
    获取历史记录接口
    需要登录后访问
    """
    return get_history()