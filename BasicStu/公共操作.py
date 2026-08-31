# Python 序列公共操作：字符串、列表、元组；集合部分不支持+、*、切片、enumerate
str_data = "abcd"
list_data = [10, 20, 30]
tuple_data = (100, 200, 300)
set_data = {1, 2, 3}

print("===== 1. + 拼接（集合不支持） =====")
print(str_data + "123")
print(list_data + [40, 50])
print(tuple_data + (400,))

print("\n===== 2. * 复制（集合不支持） =====")
print(str_data * 2)
print(list_data * 2)
print(tuple_data * 2)

print("\n===== 3. in / not in 成员判断（全部支持） =====")
print("a" in str_data)
print(10 in list_data)
print(100 in tuple_data)
print(2 in set_data)
print(99 not in set_data)

print("\n===== 4. len() 获取长度（全部支持） =====")
print(len(str_data))
print(len(list_data))
print(len(tuple_data))
print(len(set_data))

print("\n===== 5. max() min() 最大最小值（全部支持） =====")
print(max(list_data), min(list_data))
print(max(tuple_data), min(tuple_data))
print(max(set_data), min(set_data))

print("\n===== 6. range() 生成数字序列（配合for使用，不是序列本身方法） =====")
for i in range(1, 4):
    print(i, end=" ")
print()

print("\n===== 7. enumerate() 获取下标和值（集合不支持） =====")
for idx, val in enumerate(list_data):
    print(idx, val)

print("\n===== 8. 类型转换 list() tuple() set() =====")
print("转列表：", list(tuple_data))
print("转元组：", tuple(list_data))
print("转集合(自动去重)：", set([1,1,2,2,3]))
