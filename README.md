# Medical QA Backend

基于 FastAPI + LangChain + Ollama + DeepSeek-R1 的智能医疗问答系统。

---

# 项目简介

本项目是一个 AI 医疗问答系统，结合本地大模型、知识图谱与缓存机制，实现医疗相关问题的智能问答功能。

系统支持：

- 用户注册与登录
- JWT 身份认证
- 医疗问题智能问答
- Redis 高速缓存
- 本地 DeepSeek-R1 大模型调用
- 问答历史记录存储

适用于：

- AI 应用开发学习
- RAG 系统实践
- FastAPI 后端开发
- 大模型本地部署实践

---

# 技术栈

## 后端

- FastAPI
- Python 3.11
- SQLAlchemy
- JWT

## 数据库

- MySQL
- Redis

## AI / 大模型

- LangChain
- Ollama
- DeepSeek-R1

## 其他

- Git / GitHub
- RESTful API

---

# 项目功能

## 用户系统

- 用户注册
- 用户登录
- JWT Token 鉴权

## AI 医疗问答

- 用户输入医疗问题
- 调用本地 DeepSeek-R1 模型生成回答
- 返回智能问答结果

## Redis 缓存优化

- 对高频问题进行缓存
- 降低重复推理开销
- 提升接口响应速度

---

# 项目结构

```text
medical-qa-backend
│
├── app
│   ├── api             # 接口层
│   ├── models          # 数据模型
│   ├── schemas         # Pydantic数据结构
│   ├── services        # 业务逻辑
│   ├── utils           # 工具类
│   └── main.py         # 项目入口
│
├── requirements.txt
└── README.md
