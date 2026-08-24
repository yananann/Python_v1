# -*- coding:utf-8 -*-
# 爬虫项目MySQL数据库操作测试脚本
# 字符集统一使用utf8mb4，支持emoji、生僻汉字、多国语言，适配爬虫网页文本存储
import pymysql
# 导入pymysql数据库异常类，用于捕获连接、执行SQL报错
from pymysql import err

# 从本地配置文件读取数据库信息（config.py不上传git）
from db.config import DB_CONFIG, DB_NAME

# -------------------------- 通用工具函数：获取数据库连接 --------------------------
def get_conn(use_spider_db: bool = False):
    """
    获取MySQL数据库连接对象
    :param use_spider_db: 是否直接连接爬虫库spider_db；False仅连接MySQL服务，不指定库
    :return: pymysql连接实例
    """
    # 拷贝基础配置，避免修改原字典
    cfg = DB_CONFIG.copy()
    # 如果需要直接进入爬虫库，追加database参数
    if use_spider_db:
        cfg["database"] = DB_NAME
    # 返回数据库连接
    return pymysql.connect(**cfg)

# -------------------------- 初始化爬虫数据库函数 --------------------------
def init_spider_db():
    """
    自动创建爬虫数据库spider_db
    字符集utf8mb4，排序规则utf8mb4_unicode_ci，适配多语言爬虫场景
    """
    # 先连接MySQL服务（不指定数据库）
    conn = get_conn(use_spider_db=False)
    cur = conn.cursor()
    # 建库SQL：IF NOT EXISTS防止重复创建报错
    create_db_sql = f"""
    CREATE DATABASE IF NOT EXISTS {DB_NAME}
    DEFAULT CHARACTER SET utf8mb4
    DEFAULT COLLATE utf8mb4_unicode_ci;
    """
    # 执行建库语句
    cur.execute(create_db_sql)
    # 提交DDL操作
    conn.commit()
    # 释放游标、关闭连接
    cur.close()
    conn.close()
    print(f"✅ 数据库 {DB_NAME} 初始化完成")

# -------------------------- 测试MySQL服务连通性 --------------------------
def test_mysql_connect():
    """
    测试MySQL服务是否能正常连通
    输出数据库版本、现有库列表，自动检测并创建爬虫库
    """
    conn = None  # 初始化连接对象，避免finally未定义报错
    cur = None   # 初始化游标对象
    try:
        # 获取MySQL服务连接（未指定数据库）
        conn = get_conn(use_spider_db=False)
        cur = conn.cursor()
        print("✅ MySQL数据库连接成功！")

        # 查询MySQL版本号
        cur.execute("SELECT VERSION();")
        res = cur.fetchone()
        print(f"数据库版本：{res[0]}")

        # 查询服务器下所有数据库
        cur.execute("SHOW DATABASES;")
        db_list = cur.fetchall()
        db_names = [i[0] for i in db_list]
        print("现有数据库：", db_names)

        # 判断爬虫库是否存在，不存在则自动创建
        if DB_NAME not in db_names:
            print(f"⚠️ 未检测到{DB_NAME}，自动创建...")
            init_spider_db()

    # 捕获连接失败异常（端口/密码/服务未启动等）
    except err.OperationalError as e:
        print(f"❌ 连接失败：{e}")
    finally:
        # 无论成功失败，都关闭游标与连接，释放资源
        if cur:
            cur.close()
        if conn:
            conn.close()
        print("🔌 服务连接已关闭\n")

# -------------------------- 爬虫库读写测试（建表+插入数据） --------------------------
def test_spider_db_insert():
    """
    测试spider_db库的表创建、数据插入
    验证utf8mb4字符集能否正常存储emoji、中文文本，模拟爬虫入库逻辑
    """
    conn = None
    cur = None
    try:
        # 直接连接爬虫专用数据库
        conn = get_conn(use_spider_db=True)
        cur = conn.cursor()
        print(f"✅ 成功进入 {DB_NAME} 库")

        # 爬虫文章表建表SQL：不存在则创建
        create_table_sql = """
        CREATE TABLE IF NOT EXISTS article (
            id INT PRIMARY KEY AUTO_INCREMENT COMMENT '主键自增ID',
            title VARCHAR(800) COMMENT '网页标题',
            content TEXT COMMENT '网页正文内容',
            url VARCHAR(1000) NOT NULL COMMENT '爬取的原始链接',
            publish_time DATETIME COMMENT '文章发布时间',
            create_time DATETIME DEFAULT NOW() COMMENT '数据入库时间'
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='爬虫文章存储表';
        """
        cur.execute(create_table_sql)
        conn.commit()

        # 插入SQL，使用%s占位符，防止SQL注入（爬虫必用，不能直接拼接字符串）
        insert_sql = """
        INSERT INTO article (title, content, url, publish_time)
        VALUES (%s, %s, %s, NOW())
        """
        # 测试数据：包含emoji，验证utf8mb4兼容性
        test_data = ("Python爬虫测试标题🎉", "测试包含表情、中文的数据存储", "https://test-demo.com")
        cur.execute(insert_sql, test_data)
        conn.commit()
        print("✅ 测试数据插入成功")

        # 查询最新插入的一条数据，验证入库效果
        cur.execute("SELECT * FROM article ORDER BY id DESC LIMIT 1;")
        row = cur.fetchone()
        print(f"查询结果：{row}")

    # 捕获所有数据库操作异常
    except Exception as e:
        print(f"❌ spider_db操作失败：{e}")
        # 出错回滚事务，避免产生脏数据
        conn.rollback()
    finally:
        # 释放资源
        if cur:
            cur.close()
        if conn:
            conn.close()
        print("🔌 spider_db连接已关闭")

# -------------------------- 程序入口 --------------------------
if __name__ == "__main__":
    # 第一步：测试MySQL服务连通，自动创建爬虫库
    test_mysql_connect()
    # 第二步：测试爬虫库建表、写入测试数据
    test_spider_db_insert()


def test_mysql():
    return None
