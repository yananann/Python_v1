# Python 学习练习项目

> 个人 Python 编程学习与练习仓库，记录从基础语法到项目实战的完整学习过程。

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/Python-3.12+-green)](https://www.python.org/)
[![GitHub Pages](https://img.shields.io/badge/学习看板-Online-brightgreen)](https://yananann.github.io/Python_v1/)

---

## 📖 项目简介

这是一个 **Python 编程学习练习项目**，包含：

- 🐍 Python 基础语法练习代码
- 🗄️ MySQL 数据库连接与操作封装
- 📊 数据结构与算法练习
- 🎯 小项目实战（爬虫、自动化、小游戏等）
- 🖥️ 一个纯前端的学习数据看板（用于展示学习进度，非项目核心）

**核心是 Python 代码学习**，前端页面只是辅助展示。

---

## 📚 学习内容

### 第一阶段：Python 基础语法
- 变量与数据类型（整数、浮点数、字符串、布尔值）
- 条件判断（if / elif / else）
- 循环语句（for / while / break / continue）
- 函数定义与调用（参数、返回值、作用域）
- 列表、元组、字典、集合的使用
- 文件读写操作
- 异常处理（try / except / finally）
- 模块与包的导入

### 第二阶段：面向对象编程
- 类与对象
- 构造方法 `__init__`
- 实例方法、类方法、静态方法
- 继承与多态
- 魔术方法（`__str__`、`__len__` 等）

### 第三阶段：数据库编程
- MySQL 数据库连接
- 增删改查（CRUD）操作封装
- 配置文件管理（密码与代码分离）
- 事务处理

### 第四阶段：常用第三方库
- `requests` — 网络请求 / 爬虫
- `pandas` — 数据处理与分析
- `numpy` — 数值计算
- `matplotlib` — 数据可视化

### 第五阶段：项目实战
- 猜数字小游戏
- 自动化脚本
- 简单爬虫
- 待办事项命令行工具

---

## 📁 项目结构

```
Python_v1/
├── db/                            # 数据库相关
│   ├── config.py                  # 数据库配置（本地，含密码，不上传）
│   ├── config_template.py         # 配置模板（公开，复制后填写自己的信息）
│   └── mysql_conn.py              # MySQL 连接与操作封装
├── main.py                        # 主程序入口
├── demo1.py                       # 基础语法练习示例
├── micrograd.py                   # 微梯度自动求导实现（机器学习练习）
├── requirements.txt               # Python 第三方依赖清单
├── web2/                          # 前端学习看板（辅助展示，非核心）
│   ├── index.html                 # 登录页
│   ├── register.html              # 注册页
│   └── dashboard.html             # 学习数据看板
├── .github/workflows/
│   └── pages.yml                  # GitHub Actions 自动部署看板
├── .gitignore                     # Git 忽略规则（保护密码、虚拟环境）
├── GIT_GUIDE.md                   # Git 推送操作指南（新手参考）
├── LICENSE                        # Apache-2.0 开源协议
└── README.md                      # 项目说明（本文件）
```

---

## 🚀 快速开始

### 1. 环境要求

- Python 3.10 及以上（推荐 3.12）
- MySQL 8.0（可选，运行数据库相关代码时需要）

### 2. 克隆项目

```bash
git clone git@github.com:yananann/Python_v1.git
cd Python_v1
```

### 3. 创建虚拟环境

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

### 4. 安装依赖

```bash
pip install -r requirements.txt
```

### 5. 数据库配置（可选）

如果需要运行数据库相关代码：

1. 复制 `db/config_template.py`，重命名为 `db/config.py`
2. 填入你自己的数据库连接信息：

```python
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_USER = "你的用户名"
DB_PASSWORD = "你的密码"
DB_NAME = "你的数据库名"
```

> ⚠️ `db/config.py` 已在 `.gitignore` 中，不会上传到 GitHub，密码安全。

### 6. 运行代码

```bash
# 运行主程序
python main.py

# 运行示例
python demo1.py
```

---

## 🗄️ 数据库模块说明

### `db/mysql_conn.py`

封装了 MySQL 数据库的常用操作，包含：

- 数据库连接管理（自动重连）
- 查询操作（`fetch_one`、`fetch_all`）
- 增删改操作（`execute`）
- 事务支持（`begin`、`commit`、`rollback`）

### 使用示例

```python
from db.mysql_conn import MySQLConn

# 创建连接
db = MySQLConn()

# 查询
result = db.fetch_all("SELECT * FROM users WHERE age > %s", (18,))

# 插入
db.execute("INSERT INTO users (name, age) VALUES (%s, %s)", ("张三", 20))

# 关闭
db.close()
```

---

## 📊 学习看板（辅助展示）

项目附带一个纯前端的学习数据看板，用于可视化展示学习进度，**不是项目核心**。

**访问地址：** https://yananann.github.io/Python_v1/

**测试账号：** `admin` / `123456`

看板包含：
- 学习时长、练习题数、代码行数、打卡天数统计
- 各模块学习进度条
- 最近学习活动记录
- 六大学习模块导航

> 纯前端模拟数据，无后端接口，仅用于 UI 展示。

---

## 📝 学习记录

| 日期 | 学习内容 | 完成情况 |
|------|----------|----------|
| 持续更新中 | Python 基础语法 | 进行中 |
| 持续更新中 | MySQL 数据库操作 | 进行中 |
| 持续更新中 | 面向对象编程 | 待开始 |
| 持续更新中 | 爬虫与自动化 | 待开始 |
| 持续更新中 | 数据分析 | 待开始 |

---

## 🔧 开发工具

- **编辑器**：PyCharm / VS Code
- **Python 版本**：3.12
- **数据库**：MySQL 8.0
- **版本控制**：Git + GitHub
- **代码规范**：PEP 8

---

## 📄 相关文档

- [Git 推送操作指南](./GIT_GUIDE.md) — 新手如何提交代码到 GitHub
- [数据库配置模板](./db/config_template.py) — 复制后填写自己的数据库信息
- [开源协议](./LICENSE) — Apache-2.0

---

## 🔒 安全说明

- `db/config.py` 包含真实数据库密码，已通过 `.gitignore` 排除，**不会上传**
- 所有敏感配置均与代码分离，通过模板文件提供参考
- 前端看板为纯模拟，无真实用户数据存储

---

## 📄 开源协议

本项目基于 [Apache License 2.0](./LICENSE) 协议开源，可自由学习、修改、分发。

---

> 💡 **学习建议**：Python 学习重在动手练习，每学一个知识点就写一段代码跑一跑，遇到问题多查文档、多调试。坚持每天写代码，进步会很快！