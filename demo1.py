import random
from turtledemo.chaos import line

from db.mysql_conn import test_mysql
test_mysql() # 执行 mysql 连接测试

"""
# ==================== string字符串格式化 ====================
def string_demo():
    # 方式一：f‑string格式化(Python3.6+ 推荐，简洁直观)
    age = 1
    name1 = "yanan"
    print(f"{age:06.2f}")
    print(f"我是{name1},今年{age}") # f‑string直接嵌入变量
    print(f"{3 * 5}") # f‑string大括号内支持直接写运算表达式
    print(text)
# string_demo()  # 取消注释即可运行
"""

"""
def show_python_datatype():
    # int 整数：正负数字，没有小数
    a = 10
    b = -99

    # float 浮点数：带小数点的数字
    c = 3.14
    d = -2.5

    # bool 布尔值：只有True / False，属于int的子类
    e = True
    f = False

    # str 字符串：文本，单引号/双引号/三引号
    g = "hello python"
    h = '测试'

    # list 列表：有序、可变，允许重复，[]
    my_list = [1, 2, 3, "abc"]

    # tuple 元组：有序、不可变，允许重复，()
    my_tuple = (10, 20, 30, "xyz")

    # dict 字典：键值对，无序(3.7+插入有序)，key不可重复，{}
    my_dict = {"name":"张三", "age":18}

    # set 集合：无序、元素不可重复，{}
    my_set = {1,2,3,3,4}

    # ----------------------数据类型转换----------------------
    # int() 转为整数
    num1 = int(3.9)      # float转int，直接截断小数 → 3
    num2 = int("100")    # 数字字符串转int → 100

    # float() 转为浮点数
    f1 = float(5)        # int转float → 5.0
    f2 = float("2.33")   # 字符串转float → 2.33

    # bool() 转为布尔True/False
    b1 = bool(0)         # 0 → False
    b2 = bool(123)       # 非0数字 → True
    b3 = bool("")        # 空字符串 → False
    b4 = bool("hi")      # 非空字符串 → True

    # str() 转为字符串
    s1 = str(666)        # int转字符串 → "666"
    s2 = str(3.14)       # float转字符串 → "3.14"

    # list() 转列表
    li1 = list((1,2,3))  # 元组转列表 → [1,2,3]
    li2 = list("abc")    # 字符串转列表 → ['a','b','c']

    # tuple() 转元组
    t1 = tuple([10,20])  # 列表转元组 → (10, 20)
    t2 = tuple("xyz")    # 字符串转元组 → ('x','y','z')

    # dict() 转字典
    d1 = dict([("name","张三"),("age",18)]) #嵌套列表转字典

    # set() 转集合，自动去重
    se1 = set([1,1,2,2,3]) #列表转集合 → {1,2,3}
    se2 = set("aabbcc")    #字符串转集合 → {'a','b','c'}

    # 如果想看输出，打开下面注释运行
    # print(locals())
# show_python_datatype() # 调用（不调用函数内部代码不会执行）
num1 = random.randint(0,2)
print (num1)
"""

"""
for i in 'Python':  # 第一个实例
    print("当前字母: %s" % letter)

fruits = ['banana', 'apple', 'mango']
for i in fruits:  # 第二个实例
    print('当前水果: %s' % fruit)
"""

"""
# 打印正方形
j=0 # 打印5行
while j<5:
    i=0 # 打印1行
    while i<5:
        print("* ",end="")
        i+=1
    print() #一行结束用print自带换行
    j+=1
"""

"""
# 打印三角形
j=0 # 打印5行
while j<5:
    i=0 # 打印1行
    while i<j+1: # i<=j
        print("* ",end="")
        i+=1
    print() #一行结束用print自带换行
    j+=1

# for循环实现打印三角形
for j in range(5):       # j控制行数，一共5行 0,1,2,3,4
    for i in range(j+1): # 每行打印 j+1 个星号
        print("* ", end="")
    print()
    
range(起始,结束,步长)
range(5)   # 0,1,2,3,4
range(2,6)  # 2,3,4,5
range(1,10,2) # 1,3,5,7,9
range(5,0,-1) # 5,4,3,2,1 负数步长倒着数           
"""

# 九九乘法表
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}", end="\t")
    print()
"""

"""
j=1 # 行数
while j<=9:
    i = 1 #每行i个
    while i < j+1:
        print(f"{i}×{j}={i*j}", end="\t")
        i += 1
    print()
    j+=1
"""

"""
# 倒序九九乘法表
j = 9
while j >= 1:
    i = 1
    while i <= j:
        print(f"{i}×{j}={i*j}", end="\t")
        i += 1
    print()
    j -= 1
"""
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{i}×{j}={i * j}", end="\t")
    print()
"""