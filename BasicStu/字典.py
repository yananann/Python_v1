# ========== 1. 字典创建 ==========
d1 = {"name": "张三", "age": 18, "gender": "男"}
d2 = dict(a=1, b=2, c=3)          # dict()关键字参数创建
d3 = dict([("x", 10), ("y", 20)]) # 二元元组可迭代对象创建
d4 = {}                           # 空字典
d5 = dict.fromkeys(["a", "b"], 0)  # fromkeys:批量建key，统一初始值
print("d1", d1)
print("d2", d2)
print("d3", d3)
print("d5", d5)

# ========== 2. 取值 2种方式 ==========
d = {"name":"小明", "age":20}
# [] ，key不存在抛 KeyError
print(d["name"])
# get()，key不存在返回None，支持自定义默认返回值
print(d.get("age"))
print(d.get("xxx"))          # None

# ==========3. 增加 / 修改元素 ==========
d = {"a":1, "b":2}
d["a"] = 99      # key存在 → 修改value
d["c"] = 300     # key不存在 → 新增键值对
print(d)

# update()批量更新，存在覆盖、不存在新增
d.update({"b":88, "d":400})
print("update后", d)

# ==========4. 删除元素 ==========
d = {"a":1, "b":2, "c":3, "d":4}
val = d.pop("b")          # pop(key):删除，返回被删除值；key不存在报错
print("pop删除b，返回值", val, d)

val2 = d.popitem()        # popitem():删除最后插入的键值对，返回(k,v)
print("popitem删除", val2, d)

del d["a"]                # del 删除指定key
print("del删除a后", d)

d.clear()                 # clear()清空字典，保留对象
print("clear清空", d)

# ==========5. 获取视图 keys / values / items ==========
d = {"name":"Lily", "age":16, "score":90}
ks = d.keys()      # 所有键 dict_keys
vs = d.values()    # 所有值 dict_values
its = d.items()    # 所有(键,值)元组 dict_items
print("keys:", list(ks))
print("values:", list(vs))
print("items:", list(its))

# ==========6. 字典遍历 ==========
d = {"a":10, "b":20, "c":30}
# 直接遍历，默认拿到key
for k in d:
    print(k, d[k])

# 遍历key+value，items()最常用
for k, v in d.items():
    print(f"key={k}, value={v}")

# 只遍历value
for v in d.values():
    print(v)

# ==========7. in 判断成员（⚠in判断的是key，不是value！） ==========
d = {"a":1, "b":2}
print("'a' in d:", 'a' in d)      # True 判断key
print(1 in d)                     # False 1是value
print(1 in d.values())            # True 判断值使用 .values()

# ==========8. 字典推导式 {k:v for ... if...} ==========
lst = [("apple",5), ("banana",3), ("orange",7)]
my_dict = {k:v for k, v in lst}
print("推导式1", my_dict)
# 条件过滤，只保留value大于4
d2 = {k:v for k, v in lst if v>4}
print("推导式带if", d2)

# ==========9. 字典复制 ==========
import copy
d1 = {"x":1, "y":[1,2]}
d_shallow = d1.copy()   # 浅拷贝，嵌套可变对象共用
d_shallow["y"].append(99)
print("浅拷贝原字典变化", d1)

d_deep = copy.deepcopy(d1) # 深拷贝，嵌套对象完全独立
d_deep["y"].append(666)
print("深拷贝原字典不受影响", d1, d_deep)

# ==========10. setdefault方法 ==========
d = {}
# key不存在则插入，存在不修改，返回对应value
ret = d.setdefault("count", 0)
print("setdefault返回", ret, d)
d.setdefault("count", 999)
print(d)

# ==========11. 字典合并 Python3.9+ | 运算符 ==========
d_a = {"a":1, "b":2}
d_b = {"b":99, "c":3}
d_merge = d_a | d_b   # 返回新字典，后面key覆盖前面
print("|合并", d_merge)
d_a |= d_b            # 原地合并，修改d_a
print("|=原地合并", d_a)




"""
练习1：统计字符串各个字符出现次数
输入字符串，输出字典 {字符:出现次数}
"""
s = "banana"
count = {}
for char in s:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1
print("练习1字符统计结果：", count)


"""
练习2：字典值求和，计算学生总分
students = {"小明":88, "小红":95, "小刚":76}
求所有分数总和、平均分
"""
students = {"小明":88, "小红":95, "小刚":76}
total = 0
for score in students.values():
    total += score
avg = total / len(students)
print(f"练习2 总分:{total}, 平均分:{avg:.2f}")


"""
练习3：字典过滤，筛选分数大于80的学生，生成新字典
"""
high_score_stu = {name:score for name, score in students.items() if score > 80}
print("练习3 80分以上学生：", high_score_stu)


"""
练习4：键值对互换（注意：值不能重复，否则会丢失数据）
d = {"a":1, "b":2, "c":3} → {1:"a",2:"b",3:"c"}
"""
d = {"a":1, "b":2, "c":3}
swap_d = {v: k for k, v in d.items()}
print("练习4 键值互换：", swap_d)


"""
练习5：合并两个学生字典，重复key以后面字典覆盖前面
d1={"a":10,"b":20}, d2={"b":99,"c":30}
"""
d1 = {"a":10, "b":20}
d2 = {"b":99, "c":30}
res = d1 | d2
print("练习5合并字典：", res)
