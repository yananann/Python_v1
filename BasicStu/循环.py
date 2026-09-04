# ===================== for循环 和 while循环 总结 =====================
# while：条件循环，满足条件就执行，需要手动维护计数器，忘记i+=1会造成死循环
# for：遍历循环，遍历字符串、列表、range，自动迭代，不需要手动写计数器自增
# print(xxx, end="")  # print默认换行，end="" 取消换行
# print()             # 空print，只输出换行
from calendar import day_abbr

import match

# ===================== 1. for循环遍历字符串、列表 =====================
# for 变量 in 可迭代对象: 依次取出里面每一个元素
for i in 'Python':
    print("当前字母: %s" % i)

fruits = ['banana', 'apple', 'mango']
for i in fruits:
    print('当前水果: %s' % i)

print("-" * 50)

# ===================== 2. range() 函数 for循环核心 =====================
# range(起始,结束,步长)  包头不包尾：包含起始，不包含结束数字
print(list(range(5)))        # 0,1,2,3,4  只给结束，默认从0开始
print(list(range(2, 6)))     # 2,3,4,5    起始，结束
print(list(range(1, 10, 2))) # 1,3,5,7,9  步长为2
print(list(range(5, 0, -1))) # 5,4,3,2,1  负数步长，倒序

print("-" * 50)

# ===================== 3. while嵌套：打印5*5正方形 =====================
j = 0               # j控制行数
while j < 5:
    i = 0           # i控制每行的星号
    while i < 5:
        print("* ", end="") # end="" 不换行，同一行打印
        i += 1      # 内层计数器自增
    print()         # 一行打印完，换行
    j += 1          # 外层计数器自增
print("-" * 50)

# ===================== 4. while嵌套：直角三角形 =====================
j = 0
while j < 5:
    i = 0
    while i < j + 1:  # 第j行打印 j+1个星
        print("* ", end="")
        i += 1
    print()
    j += 1
print("-" * 50)

# ===================== 5. for嵌套：直角三角形 =====================
for j in range(5):           # j代表行数，0 1 2 3 4，共5行
    for i in range(j + 1):   # 每一行打印 j+1个星
        print("* ", end="")
    print()  # 每行结束换行
print("-" * 50)

# ===================== 6. 九九乘法表 for版本（正序） =====================
for i in range(1, 10):               # i：行数 1~9
    for j in range(1, i + 1):        # j：每行循环i次
        print(f"{j}×{i}={i*j}", end="\t")
    print()  # 换行
print("-" * 50)

# ===================== 7. 九九乘法表 while版本（正序） =====================
j = 1
while j <= 9:
    i = 1
    while i < j + 1:
        print(f"{i}×{j}={i*j}", end="\t")
        i += 1
    print()
    j += 1
print("-" * 50)

# ===================== 8. 倒序九九乘法表 while =====================
j = 9
while j >= 1:
    i = 1
    while i <= j:
        print(f"{i}×{j}={i*j}", end="\t")
        i += 1
    print()
    j -= 1
print("-" * 50)

# ===================== 9. 倒序九九乘法表 for =====================
for i in range(9, 0, -1):
    for j in range(1, i + 1):
        print(f"{j}×{i}={i*j}", end="\t")
    print()

day = input("输入1-7:")
match day:
    case "1":
        print(1)
    case "2":
        print(2)
    case "3":
        print(3)
    case "4":
        print(4)
    case "5":
        print(5)
    case "6 | 7":
        print(6,7)
    case _:
        print("错误")
