from fastapi import FastAPI
from app.api import qa,user
from app.database import engine, Base
#显示导入模型，确保 create_all 能识别这些表
from app.models.qa_history import QAHistory
from app.models.user import User
app = FastAPI()

#根据模型自动创建表
Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"msg": "服务已启动"}

app.include_router(qa.router)
app.include_router(user.router)