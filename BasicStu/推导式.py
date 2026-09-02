# ========== 1.列表推导式 [表达式 for 变量 in 可迭代对象 if 条件] ==========
# 基础：生成0~9列表
list1 = [i for i in range(10)]
print("基础列表推导：", list1)

# 带条件：只取偶数
list2 = [i for i in range(10) if i % 2 == 0]
print("取偶数：", list2)

# 表达式做运算：每个数*2
list3 = [i*2 for i in range(1,6)]
print("每个数乘2：", list3)

# 双重for循环
list4 = [(i,j) for i in range(1,3) for j in range(3,5)]
print("双重循环：", list4)


# ========== 2.集合推导式 {表达式 for 变量 in 可迭代对象 if 条件} ==========
# 自动去重
set1 = {i**2 for i in [1,2,2,3,3]}
print("\n集合推导式：", set1)

# 条件筛选
set2 = {x for x in range(10) if x > 4}
print("集合条件筛选：", set2)


# ========== 3.字典推导式 {key表达式:value表达式 for 变量 in 可迭代对象 if 条件} ==========
# key:value 简单生成
dict1 = {i:i*10 for i in range(1,4)}
print("\n字典推导式：", dict1)

# 键值对互换
old_dict = {"a":1, "b":2, "c":3}
dict2 = {v:k for k,v in old_dict.items()}
print("键值互换：", dict2)

# 条件过滤，只保留value大于1的
dict3 = {k:v for k,v in old_dict.items() if v>1}
print("条件过滤字典：", dict3)


# ========== 注意：()不是元组推导式，是生成器对象 ==========
gen = (i for i in range(5))
print("\n()得到生成器：", gen)
# 想要元组，套tuple()
t = tuple(i for i in range(5))
print("转成元组：", t)
