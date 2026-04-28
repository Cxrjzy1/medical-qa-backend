# -*- coding: utf-8 -*-

from app.database import SessionLocal
from app.models.qa_history import QAHistory
from app.utils.redis_client import redis_client

def save_question(question, answer):
    """
    保存一条问答记录到数据库
    :param question: 用户提问
    :param answer: 系统回答
    :return: 保存后的记录对象
    """
    db = SessionLocal()
    try:
        # 创建一条问答历史记录对象
        record = QAHistory(question=question, answer=answer)

        # 加入数据库会话
        db.add(record)

        # 提交事务
        db.commit()

        # 刷新对象，拿到数据库生成的 id
        db.refresh(record)

        return record
    finally:
        # 关闭会话，避免资源泄漏
        db.close()


def get_history():
    """
    查询所有历史记录
    :return: 历史记录列表
    """
    db = SessionLocal()
    try:
        # 查询 qa_history 表的全部数据
        records = db.query(QAHistory).all()

        # 把 ORM 对象转换成普通字典，方便接口直接返回 JSON
        return [
            {
                "id": item.id,
                "question": item.question,
                "answer": item.answer
            }
            for item in records
        ]
    finally:
        db.close()


def generate_answer(question: str):
    #先查Redis
    cached_answer = redis_client.get(question)
    if cached_answer:
        return cached_answer
    #没命中，正常生成
    answer = f"你问的是：{question}，这是AI回答"
    #写入Redis(设置过期时间1小时）
    redis_client.set(question,answer,ex=3600)
    return answer