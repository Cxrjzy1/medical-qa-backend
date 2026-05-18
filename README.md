# Medical QA Backend

基于 **FastAPI + MySQL + Redis + JWT + LangChain + Ollama + DeepSeek-R1 + LangGraph** 的智能医疗问答后端项目，并扩展了一个 **AI Coding 测试 Agent Demo**。

---

## 项目简介

本项目是一个面向 AI 应用开发学习与实践的后端系统，主要包含两部分：

1. **智能医疗问答系统**
   - 支持用户注册、登录、JWT 鉴权、医疗问题问答、历史记录查询、Redis 缓存优化和本地大模型调用。

2. **AI Coding 测试 Agent Demo**
   - 基于 LangGraph 构建多节点 Agent 工作流，可根据接口功能描述自动生成测试分析、测试用例、请求示例和 pytest 测试代码。

项目适用于：

- Python 后端开发实践
- FastAPI 接口开发
- MySQL / Redis 工程应用
- 本地大模型调用实践
- LangChain / LangGraph / Agent 入门实践
- AI Coding 辅助测试场景探索

---

## 技术栈

### 后端

- Python 3.11
- FastAPI
- SQLAlchemy
- Pydantic
- JWT

### 数据库与缓存

- MySQL
- Redis

### AI / 大模型

- LangChain
- LangGraph
- Ollama
- DeepSeek-R1

### 工具

- Git / GitHub
- Swagger
- RESTful API
- pytest

---

## 项目功能

### 1. 用户系统

- 用户注册
- 用户登录
- JWT Token 鉴权
- 根据 Token 获取当前用户信息

---

### 2. 智能医疗问答

- 用户输入医疗相关问题
- 后端调用本地 DeepSeek-R1 模型生成回答
- 支持问答结果返回
- 回答内容仅供参考，不替代专业医疗诊断

---

### 3. 问答历史记录

- 使用 MySQL 保存用户问答历史
- 问答记录绑定 `user_id`
- 用户只能查询自己的历史记录
- 实现不同用户之间的数据隔离

---

### 4. Redis 缓存优化

- 对重复问题结果进行缓存
- 减少重复模型调用
- 提升接口响应速度
- 降低本地大模型推理开销

缓存流程：

```text
用户提问
↓
查询 Redis 缓存
↓
命中：直接返回缓存答案
↓
未命中：调用本地大模型生成答案
↓
写入 Redis
↓
返回答案
```

---

### 5. AI Coding 测试 Agent

项目新增基于 **LangGraph** 的 AI Coding 测试 Agent Demo，用于根据接口功能描述自动生成测试方案。

用户输入：

- 接口功能描述
- 接口路径
- 请求方法

Agent 会依次完成：

1. 接口测试目标分析
2. 测试用例生成
3. Swagger / Postman 请求示例生成
4. pytest 自动化测试代码生成
5. 测试报告汇总

---

## AI Coding 测试 Agent 说明

### Agent 工作流

```text
接口功能描述
↓
需求分析节点
↓
测试用例生成节点
↓
请求示例生成节点
↓
pytest 测试代码生成节点
↓
测试报告汇总节点
↓
输出完整测试方案
```

### 技术实现

- 使用 LangGraph 构建多节点 Agent 工作流
- 使用 LangChain 调用本地 Ollama DeepSeek-R1 模型
- 使用 FastAPI 暴露 Agent 调用接口
- 支持通过 Swagger 页面直接调用测试

### 接口地址

```http
POST /agent/test
```

### 请求示例

```json
{
  "feature": "测试用户登录接口，用户输入用户名和密码，登录成功后返回JWT token，密码错误时返回错误提示",
  "api_path": "/user/login",
  "method": "POST"
}
```

### 返回内容包括

- 接口测试目标分析
- 正常场景测试用例
- 异常场景测试用例
- Swagger / Postman 请求示例
- pytest 自动化测试代码
- 测试执行建议

---

## 项目结构

```text
medical-qa-backend
│
├── app
│   ├── agents
│   │   └── test_agent
│   │       ├── state.py        # Agent 状态定义
│   │       ├── nodes.py        # Agent 节点逻辑
│   │       └── graph.py        # LangGraph 工作流
│   │
│   ├── api
│   │   ├── agent.py            # AI Agent 接口
│   │   ├── qa.py               # 问答接口
│   │   └── user.py             # 用户接口
│   │
│   ├── models                  # 数据模型
│   ├── schemas                 # Pydantic 数据结构
│   ├── services                # 业务逻辑
│   ├── utils                   # 工具类
│   ├── database.py             # 数据库连接
│   └── main.py                 # 项目入口
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 本地启动

### 1. 克隆项目

```bash
git clone https://github.com/Cxrjzy1/medical-qa-backend.git
cd medical-qa-backend
```

---

### 2. 创建虚拟环境

```bash
python -m venv .venv
```

Windows 激活虚拟环境：

```bash
.venv\Scripts\activate
```

---

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

---

### 4. 准备 MySQL

创建数据库：

```sql
CREATE DATABASE medical_qa;
```

项目中数据库连接配置示例：

```text
mysql+pymysql://root:123456@localhost:3306/medical_qa
```

实际使用时请根据本地 MySQL 用户名、密码和数据库名进行修改。

---

### 5. 启动 Redis

如果 Redis 已加入环境变量，可以直接执行：

```bash
redis-server
```

也可以进入 Redis 安装目录后执行：

```bash
redis-server.exe
```

测试 Redis 是否正常：

```bash
redis-cli ping
```

返回：

```text
PONG
```

说明 Redis 启动成功。

---

### 6. 启动 Ollama DeepSeek-R1

确保本地已经安装 Ollama，并下载 DeepSeek-R1：

```bash
ollama run deepseek-r1
```

模型可以正常对话后，再启动后端项目。

---

### 7. 启动 FastAPI 后端

```bash
uvicorn app.main:app --reload
```

启动成功后访问 Swagger：

```text
http://127.0.0.1:8000/docs
```

---

## API 示例

### 用户注册

```http
POST /user/register
```

请求示例：

```json
{
  "username": "test",
  "password": "123456"
}
```

---

### 用户登录

```http
POST /user/login
```

请求示例：

```json
{
  "username": "test",
  "password": "123456"
}
```

返回示例：

```json
{
  "access_token": "token字符串",
  "token_type": "bearer"
}
```

---

### 智能问答

```http
POST /qa
```

请求示例：

```json
{
  "question": "感冒怎么办？"
}
```

---

### 查询问答历史

```http
GET /qa/history
```

说明：

```text
需要携带 JWT Token。
后端会根据当前用户 user_id 查询该用户自己的问答历史。
```

---

### AI Coding 测试 Agent

```http
POST /agent/test
```

请求示例：

```json
{
  "feature": "测试智能问答接口，用户携带JWT token提交问题，后端先查询Redis缓存，未命中时调用本地DeepSeek-R1生成回答，并保存问答历史",
  "api_path": "/qa",
  "method": "POST"
}
```

---

## 项目亮点

- 使用 FastAPI 完成后端接口开发，覆盖用户认证、问答、历史记录等核心功能
- 使用 MySQL 持久化存储用户信息和问答历史
- 使用 Redis 缓存重复问题结果，减少重复模型调用
- 基于 JWT + user_id 实现用户认证与数据隔离
- 基于 LangChain 接入本地 Ollama DeepSeek-R1，实现本地大模型调用
- 基于 LangGraph 构建 AI Coding 测试 Agent Demo，实践多节点 Agent 工作流
- 通过 Swagger 提供接口文档与在线测试能力
- 使用 Git / GitHub 进行版本管理和项目托管

---

## 后续优化方向

- 接入 FAISS，实现更完整的 RAG 向量检索流程
- 优化医疗知识检索与回答生成效果
- 为 Agent 增加自动读取 FastAPI 路由的能力
- 支持 Agent 自动运行 pytest 并分析测试结果
- 接入 Playwright / Selenium，实现前端自动化测试
- 使用 Docker / Docker Compose 完成项目容器化部署
- 接入 LangGraph 更复杂的条件分支和工具调用能力

---

## 注意事项

本项目中的医疗回答仅作为 AI 应用开发学习和技术实践示例，不构成任何医疗建议，不能替代医生诊断或治疗。

---

## GitHub

项目地址：

```text
https://github.com/Cxrjzy1/medical-qa-backend
```
