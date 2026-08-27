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

# ===================== 1. str.replace(old, new[, count]) 替换 =====================
# 作用：把字符串中的 old子串 替换成 new子串，count可选，代表替换前count个
# 返回：替换后的新字符串，原字符串不变

s1 = "苹果,香蕉,苹果,橘子"
# 将"苹果"替换成"西瓜"
res_replace1 = s1.replace("苹果", "西瓜")
print("replace全部替换:", res_replace1)  # 西瓜,香蕉,西瓜,橘子

# 只替换前1个"苹果"
res_replace2 = s1.replace("苹果", "西瓜", 1)
print("replace只替换1个:", res_replace2) # 西瓜,香蕉,苹果,橘子

print("原字符串s1不变：", s1)
print("-" * 60)


# ===================== 2. str.split(sep=None, maxsplit=-1) 分割 =====================
# 作用：按照分隔符sep把字符串切割，返回**列表list**
# sep：分隔符；maxsplit：最大分割次数，-1代表全部分割
s2 = "张三,李四,王五,赵六"

# 按逗号分割
res_split1 = s2.split(",")
print("split按逗号分割:", res_split1)  # ['张三', '李四', '王五', '赵六']

# 只分割2次
res_split2 = s2.split(",", maxsplit=2)
print("split最多分割2次:", res_split2) # ['张三', '李四', '王五,赵六']

# 不传sep，默认按任意空白（空格、换行、tab）分割
s2_2 = "a b   c\nd"
res_split3 = s2_2.split()
print("split不带参数(切空白):", res_split3) # ['a', 'b', 'c', 'd']
print("-" * 60)


# ===================== 3. str.join(iterable) 拼接 =====================
# 作用：用【当前字符串】作为连接符，把列表/元组里面所有元素拼接成一个大字符串
# 注意：列表里面必须全部是字符串类型，不能是数字！
list_data = ["张三", "李四", "王五"]

# 用逗号作为连接符，把列表拼起来
res_join1 = ",".join(list_data)
print("join用逗号拼接:", res_join1)  # 张三,李四,王五

# 用.拼接
res_join2 = "......".join(list_data)
print("join用...拼接:", res_join2) # 张三 李四 王五

# 空字符串拼接，直接连在一起
res_join3 = "".join(list_data)
print("join空字符直接相连:", res_join3) # 张三李四王五

print("-" * 60)

# ========== 经典组合示例：split + join 配合使用 ==========
text = "小明|小红|小刚"
# 分割成列表，再换分隔符拼接
lst = text.split("|")
new_text = "-".join(lst)
print("split+join组合结果：", new_text) # 小明-小红-小刚


# ========== 1. upper() / lower() 大小写转换 ==========
# upper()：全部转大写；lower()：全部转小写
s = "Hello Python"
res_upper = s.upper()
res_lower = s.lower()
print("upper大写：", res_upper)   # HELLO PYTHON
print("lower小写：", res_lower)   # hello python

# capitalize() 首字母大写，其余小写
res_cap = s.capitalize()
print("capitalize首字母大写：", res_cap)  # Hello python

# title() 每个单词首字母大写
res_title = s.title()
print("title每个单词首字母大写：", res_title) # Hello Python
print("-"*50)


# ========== 2. strip() / lstrip() / rstrip() 去除首尾空白 ==========
# strip()：去掉左右两边空格、换行、tab
# lstrip()：只去左边；rstrip()：只去右边
s2 = "   你好世界   \n"
res_strip = s2.strip()
print("strip去首尾空白：", repr(res_strip)) # repr可以看见看不见的换行空格
print("原字符串：", repr(s2))

# 还可以指定要删除的字符
s2_2 = "***abc***"
print(s2_2.strip("*")) # abc
print("-"*50)


# ========== 3. find() / index() 查找子串位置 ==========
# find：找到返回下标，找不到返回 -1
# index：找到返回下标，找不到直接报错！
s3 = "I like python"
pos1 = s3.find("like")
print("find位置：", pos1) # 2
pos2 = s3.find("java")
print("find找不到返回：", pos2) # -1

# pos3 = s3.index("java") # 找不到会报错，慎用
print("-"*50)


# ========== 4. count() 统计子串出现次数 ==========
s4 = "苹果香蕉苹果橘子苹果"
cnt = s4.count("苹果")
print("count统计次数：", cnt) # 3
print("-"*50)


# ========== 5. startswith() / endswith() 判断开头结尾，返回布尔True/False ==========
s5 = "hello.txt"
print("是否以hello开头：", s5.startswith("hello")) # True
print("是否以.txt结尾：", s5.endswith(".txt"))     # True
print("-"*50)


# ========== 6. is系列判断：isalpha、isdigit、isalnum ==========
# isalpha() 是否全部是字母汉字
# isdigit() 是否全部是数字
# isalnum() 是否字母+数字
print("'abc'.isalpha()", 'abc'.isalpha())      # True
print("'123'.isdigit()", '123'.isdigit())      # True
print("'a123'.isalnum()", 'a123'.isalnum())    # True
print("-"*50)


# ========== 7. format() 字符串格式化 ==========
name = "小明"
age = 18
text = "姓名：{}，年龄：{}".format(name, age)
print("format格式化：", text) # 姓名：小明，年龄：18

# f-string（更常用，Python3.6+）
text2 = f"姓名：{name}，年龄：{age}"
print("f-string：", text2)
print("-"*50)


# ========== 8. zfill() 补零，做编号很常用 ==========
num_str = "5"
print(num_str.zfill(3)) # 005，总长度3，左边补0
print("-"*50)


# ========== 9. 之前学过的回顾 replace split join ==========
s_old = "a,b,c"
s_rep = s_old.replace("a", "A")   # 替换
lst = s_old.split(",")            # 字符串切列表
s_new = "-".join(lst)             # 列表拼接字符串
print("replace:", s_rep)
print("split:", lst)
print("join:", s_new)

