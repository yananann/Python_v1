# ===================== Python列表 list [] 完整笔记 =====================
# 1.列表应用场景：存储多个有序数据，可存放不同类型，支持增删改查
# 2.列表格式：变量 = [元素1, 元素2, 元素3]
import random

# 定义列表
my_list = ["张三", "李四", 20, 3.14, True]
print("原始列表：", my_list)
print("-"*60)

# ===================== 列表常用操作：增、删、改、查 =====================
# -------- 查询 --------
print("下标0取值：", my_list[0])         # 下标从0开始
print("下标-1倒数取值：", my_list[-1])    # -1代表最后一个元素
print("len获取列表长度：", len(my_list))
print("index查找元素下标：", my_list.index("李四"))

list2 = [1,2,2,3,2]
print("count统计元素次数：", list2.count(2))

# -------- 增加元素 append / extend / insert --------
# append(数据)：整体当做1个元素，追加到末尾
# extend(可迭代对象)：拆开内容，逐个追加到末尾
# insert(下标,数据)：指定下标位置插入，原元素后移

# append示例
append_list = [10,20]
append_list.append(30)
print("append加数字：", append_list)        # [10, 20, 30]

list_e = [1,2]
list_e.append("abc")
print("append加字符串：", list_e)           # [1, 2, 'abc']

list_a = [10,20]
list_a.append([30,40])
print("append加列表(产生嵌套)：", list_a)   # [10, 20, [30, 40]]

print("-"*40)

# extend示例
extend_list = [1,2]
extend_list.extend([3,4,5])
print("extend加列表：", extend_list)        # [1, 2, 3, 4, 5]

list_d = [1,2]
list_d.extend("abc")
print("extend加字符串(拆成字符)：", list_d)  # [1, 2, 'a', 'b', 'c']

print("-"*40)

# insert示例
insert_list = [10,20,30]
insert_list.insert(1,99)
print("insert下标1插入99：", insert_list)   # [10, 99, 20, 30]


# -------- 修改元素 --------
change_list = [100,200,300]
change_list[1] = 888                     # 通过下标直接赋值修改
print("下标修改元素：", change_list)

# -------- 删除元素 --------
del_list = [1,2,3,4]
del del_list[0]                          # del：按下标删除
print("del按下标删除：", del_list)

pop_list = ["a","b","c"]
res_pop = pop_list.pop()                 # pop() 默认删除末尾，返回被删元素
print("pop删除末尾，返回值：", res_pop, "列表：", pop_list)

pop_list2 = ["a","b","c"]
pop_list2.pop(1)                         # pop(下标) 删除指定下标
print("pop删除指定下标：", pop_list2)

remove_list = [11,22,33,22]
remove_list.remove(22)                   # remove(元素) 删除第一个匹配元素
print("remove删除匹配元素：", remove_list)

clear_list = [1,2,3]
clear_list.clear()                       # clear() 清空列表
print("clear清空列表：", clear_list)
print("-"*60)

# ===================== 列表切片 [start:end:step] 包头不包尾 =====================
slice_list = [10,20,30,40,50,60]
print("切片[1:4]：", slice_list[1:4])     # 取1,2,3下标，不取4
print("切片[:3]从头到下标3：", slice_list[:3])
print("切片[2:]从下标2到末尾：", slice_list[2:])
print("切片[:]完整浅拷贝：", slice_list[:])
print("切片[::2]步长2：", slice_list[::2])
print("切片[::-1]反转：", slice_list[::-1])
print("-"*60)

# ===================== 列表复制、排序、反转 =====================
ori = [1,2,3]
copy1 = ori.copy()                       # 浅拷贝方式1
copy2 = ori[:]                           # 浅拷贝方式2
print("copy浅拷贝：", copy1, "切片浅拷贝：", copy2)


# ----------深拷贝 deepcopy()：完全独立，所有层级全部复制 ----------
import copy   # 使用深拷贝需要导入copy模块
n2 = [[1,2],100]
deep1 = copy.deepcopy(n2)
deep1[0][0] = 999
print("深拷贝deepcopy：n2", n2, "deep", deep1) #原数据不受影响
print("-"*50)


num_sort = [5,2,9,1]
num_sort.sort()                          # sort原地升序
print("sort升序：", num_sort)
num_sort.sort(reverse=True)              # sort原地降序
print("sort降序：", num_sort)

num_rev = [1,2,3,4]
num_rev.reverse()                        # reverse原地反转
print("reverse原地反转：", num_rev)
print("-"*60)

# ===================== 列表循环遍历 =====================
name_list = ["小明", "小红", "小刚"]
print("for循环遍历：")
for name in name_list:
    print(name)

i = 0
print("while循环遍历：")
while i < len(name_list):
    print(name_list[i])
    i += 1
print("-"*60)

# ===================== 列表嵌套：列表里面存放列表 =====================
student = [["小明",18], ["小红",19], ["小刚",20]]
print("嵌套列表整体：", student)
print("取外层第一个列表：", student[0])
print("取小明年龄：", student[0][1])      # 外层下标[0]，内层下标[1]

teacher=["李","王","哇","的","额","发","就"]
offices=[[],[],[]]
for name in teacher:
    num = random.randint(0, 2)
    offices[num].append(name)
print(offices)
nub=1
for i in offices:
    print(f'{nub}人数为：{len(i)}')
    for name in i:
        print(f'名字：{name}')
    nub+=1