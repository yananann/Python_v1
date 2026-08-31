# 定义集合
s = {10, 20, 30}
print("初始集合：", s)

# ========== 增 ==========
# add() 添加单个元素
s.add(40)
print("add(40)：", s)

# update() 批量添加多个元素，接收可迭代对象
s.update([50, 60])
print("update([50,60])：", s)

# ========== 删 ==========
s2 = {10, 20, 30, 40, 50}
print("\n删除测试集合：", s2)

# remove(x) 删除指定元素，不存在则报错
s2.remove(20)
print("remove(20)：", s2)

# discard(x) 删除指定元素，不存在不报错
s2.discard(99)
print("discard(99)：", s2)

# pop() 随机删除一个元素，返回被删元素
res = s2.pop()
print(f"pop() 删除：{res}，集合：{s2}")

# clear() 清空集合
s2.clear()
print("clear() 清空：", s2)

# ========== 改 ==========
"""
集合没有直接修改元素的方法！
思路：删掉旧元素，添加新元素
"""
s3 = {1, 2, 3}
# 把2改成22
s3.remove(2)
s3.add(22)
print("\n修改元素(2→22)：", s3)

# ========== 查 ==========
s4 = {1, 2, 3, 4}
# 成员运算符 in / not in，判断元素是否存在
print("\n2 in s4：", 2 in s4)
print(99 not in s4)

# 遍历查询
print("遍历集合：")
for item in s4:
    print(item)

# 获取长度
print("集合长度 len(s4)：", len(s4))


# 集合 交、并、差、对称差 代码演示
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print("a =", a)
print("b =", b)

# 1.交集：两个集合都有的元素   &  / intersection()
res1 = a & b
res1_2 = a.intersection(b)
print("\n交集 &：", res1)
print("交集 intersection：", res1_2)

# 2.并集：两个集合全部元素，去重  |  / union()
res2 = a | b
res2_2 = a.union(b)
print("\n并集 |：", res2)
print("并集 union：", res2_2)

# 3.差集：a中有，b中没有的   -  / difference()
res3 = a - b
res3_2 = a.difference(b)
print("\n差集 a-b：", res3)
print("差集 difference：", res3_2)

# 4.对称差集：只在其中一个里面有的元素 ^ / symmetric_difference()
res4 = a ^ b
res4_2 = a.symmetric_difference(b)
print("\n对称差集 ^：", res4)
print("对称差集 symmetric_difference：", res4_2)


# ===== 原地修改集合(更新本身) =====
c = {1,2,3}
d = {3,4,5}

c.intersection_update(d)   # 原地求交集，c变成交集结果
print("\nintersection_update c：", c)

e = {1,2,3}
e.difference_update(d)     # 原地求差集
print("difference_update e：", e)

f = {1,2,3}
f.symmetric_difference_update(d) # 原地对称差
print("symmetric_difference_update f：", f)


# ===== 判断子集、超集 =====
s1 = {1,2}
s2 = {1,2,3}
print("\ns1是s2子集：", s1.issubset(s2))      # s1 <= s2
print("s2是s1超集：", s2.issuperset(s1))    # s2 >= s1
print("两个集合是否无交集：", s1.isdisjoint({4,5})) # 没有共同元素返回True
