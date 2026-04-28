from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base


class QAHistory(Base):
    __tablename__ = "qa_history"

    id = Column(Integer, primary_key=True, index=True)

    question = Column(String(255))   # 👈 必须加长度
    answer = Column(String(1000))    # 👈 建议大一点

    created_at = Column(DateTime, default=datetime.utcnow)