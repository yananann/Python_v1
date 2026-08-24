# 导入数据库连接函数
import prinf

from db.mysql_conn import test_mysql
# 执行mysql连接测试
test_mysql()

# string格式化
'''
def string_demo():
# ----------------------方式一：f-string格式化（Python3.6+推荐，简洁直观）----------------------
    a = 11
    # 将数字格式化为保留20位小数的浮点数输出
    print(f"{a:.20f}")

    """
    占位符说明：
        %s  字符串占位符（可以接收任意类型，会自动转字符串）
        %d  整数占位符，接收数字整数
        %f  浮点数占位符，默认保留6位小数； %.3f 保留3位小数
    """
# ----------------------方式二：% 占位符格式化（旧版格式化语法）----------------------
    name1 = "yananan"
    age1 = 22
    price = 999.88
    # %s通用占位符，输出天数和金额
    print("第%s天,得到了%s元" % (name1, age1))
    message1 = "xuexi%s" % price
    print(message1)
    message2 = "我是%s,你多大了%d\n,多少钱%f，原来是:%.3f" % (name1, age1, price, price)
    print(message2)

# ----------------------f-string 实战示例，支持直接大括号内写表达式计算----------------------
    name1 = "yanan"
    age1 = 22
    price = 999.88
    # f-string直接嵌入变量
    print(f"我是{name1},今年{age1},还有{price}")
    # f-string支持直接写运算表达式
    print(f"计算得{3 * 5}")
    print("计算得%d" % (3 * 5))
'''


'''
age=1
print('%03d'% age)\n
print('%06.2f'% age)\n
print(f"{age:06.2f}")\n
print('%s'% age)\n

# f'{}'表达式
print(f"{age:06.2f}")
'''

'''
text = f"""
年龄：{1}
编号：{1:07.2f}
"""
print(text)
'''

