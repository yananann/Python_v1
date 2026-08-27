# ===================== 1. str.replace(old, new[, count]) 替换 =====================
# 作用：把字符串 old子串 替换为 new子串；count可选，控制只替换前count个
# 返回：返回替换后的新字符串，**原字符串不会被修改**
s1 = "苹果,香蕉,苹果,橘子"
res_replace1 = s1.replace("苹果", "西瓜")
print("replace全部替换:", res_replace1)  # 西瓜,香蕉,西瓜,橘子

res_replace2 = s1.replace("苹果", "西瓜", 1)
print("replace只替换1个:", res_replace2) # 西瓜,香蕉,苹果,橘子

print("原字符串s1不变：", s1)
print("-" * 60)

# ===================== 2. str.split(sep=None, maxsplit=-1) 分割 =====================
# 作用：按分隔符sep切割字符串，返回列表list
# sep：分隔符；maxsplit：最大分割次数，-1表示全部切割
# sep不传参：自动按任意空白（空格、换行\n、tab\t）分割
s2 = "张三,李四,王五,赵六"
res_split1 = s2.split(",")
print("split按逗号分割:", res_split1)  # ['张三', '李四', '王五', '赵六']

res_split2 = s2.split(",", maxsplit=2)
print("split最多分割2次:", res_split2) # ['张三', '李四', '王五,赵六']

s2_2 = "a b   c\nd"
res_split3 = s2_2.split()
print("split不带参数(切空白):", res_split3) # ['a', 'b', 'c', 'd']
print("-" * 60)

# ===================== 3. str.join(可迭代对象) 拼接 =====================
# 作用：以当前字符串作为连接符，把列表/元组里面所有元素拼接成一个字符串
# 注意：列表里面元素必须全部是字符串，不能放数字
list_data = ["张三", "李四", "王五"]
res_join1 = ",".join(list_data)
print("join逗号拼接:", res_join1)   # 张三,李四,王五

res_join2 = " ".join(list_data)
print("join空格拼接:", res_join2)   # 张三 李四 王五

res_join3 = "".join(list_data)
print("join空字符直接相连:", res_join3) # 张三李四王五
print("-" * 60)

# ===================== 4. strip() / lstrip() / rstrip() 去除空白 =====================
# strip()：去除左右两边空白(空格、换行、tab)；lstrip()只去左边；rstrip()只去右边
# 也可以传字符：strip("*") 去掉两端的*号
s3 = "   你好Python   \n"
res_strip = s3.strip()
print("strip去除两端空白:", repr(res_strip))

s3_2 = "***测试***"
print("strip去除指定字符:", s3_2.strip("*"))
print("-" * 60)

# ===================== 5. upper() / lower() 大小写转换 =====================
# upper()全部转大写；lower()全部转小写；返回新字符串，原字符串不变
s4 = "Hello Python"
res_upper = s4.upper()
res_lower = s4.lower()
print("upper大写：", res_upper)
print("lower小写：", res_lower)
print("-" * 60)

# ===================== 6. find(sub) 查找子串 =====================
# 找到返回下标位置；找不到返回 -1，不会程序崩溃
s5 = "I like python"
pos1 = s5.find("like")
pos2 = s5.find("java")
print("find找到like下标：", pos1)
print("find找不到java返回：", pos2)
print("-" * 60)

# ===================== 7. count(sub) 统计子串出现次数 =====================
# 返回子串在字符串中出现多少次
s6 = "苹果香蕉苹果橘子苹果"
cnt = s6.count("苹果")
print("count统计苹果次数：", cnt)
print("-" * 60)

# ===================== 8. startswith() / endswith() 判断开头结尾 =====================
# 返回布尔值 True / False
s7 = "hello.txt"
print("startswith是否hello开头：", s7.startswith("hello"))
print("endswith是否.txt结尾：", s7.endswith(".txt"))
print("-" * 60)

# ===================== 9. center / ljust / rjust 对齐填充 =====================
# center(宽度,填充字符)居中；ljust左对齐；rjust右对齐
s8 = "python"
print("center居中：|", s8.center(15, "*"), "|")
print("ljust左对齐：|", s8.ljust(15, "-"), "|")
print("rjust右对齐：|", s8.rjust(15, "#"), "|")
print("-" * 60)

# ===================== 10. isdigit() / isalpha() / isalnum() 判断字符串内容 =====================
# isdigit() 是否全部数字；isalpha()是否全部字母汉字；isalnum()字母+数字
print("'123'.isdigit()", '123'.isdigit())
print("'abc'.isalpha()", 'abc'.isalpha())
print("'a123'.isalnum()", 'a123'.isalnum())
print("-" * 60)

# ===================== 11. zfill(总长度) 左边补零 =====================
num_str = "5"
print("zfill补零：", num_str.zfill(3)) # 005

#===================================================================================================================
#===================================================================================================================
#===================================================================================================================
# 原始杂乱字符串：有多余空格、逗号、小写英文、换行
raw_text = "  apple, banana , orange , apple, grape , apple  \n"

# 1. strip() 去除首尾空格换行
clean_text = raw_text.strip()
print("1、去掉首尾空白：", repr(clean_text))

# 2. replace 把里面的空格全部删掉
clean_text = clean_text.replace(" ", "")
print("2、删除全部空格：", clean_text)

# 3. split 按逗号切割，变成列表
fruit_list = clean_text.split(",")
print("3、split分割成列表：", fruit_list)

# 4. count统计 apple 出现多少次
apple_num = clean_text.count("apple")
print(f"4、apple出现次数：{apple_num}")

# 5. join 使用 " | " 把列表拼接回字符串
join_str = " | ".join(fruit_list)
print("5、join拼接：", join_str)

# 6. upper全部转大写
upper_str = join_str.upper()
print("6、全部转大写：", upper_str)

# 7. startswith 判断是否以APPLE开头
is_start = upper_str.startswith("APPLE")
print(f"7、是否以APPLE开头：{is_start}")

# 8. center居中格式化输出，总宽度50，用#填充
print("\n8、居中展示结果：")
print(upper_str.center(50, "#"))


# ---------------------- 拓展小任务 ----------------------
# 任务：遍历水果列表，每一个水果居中打印
print("\n===== 遍历打印每个水果 =====")
for fruit in fruit_list:
    print(fruit.center(12, "-"))


raw = "  Hello Python 123\n"

# 1. strip 去除首尾空白
s1 = raw.strip()
print("1 strip去除空白:", repr(s1))

# 2. lower / upper 大小写
s_low = s1.lower()
s_up = s1.upper()
print("2 lower小写:", s_low)
print("2 upper大写:", s_up)

# 3. capitalize 首字母大写；title每个单词首字母大写
s_cap = s_low.capitalize()
s_tit = s_low.title()
print("3 capitalize:", s_cap)
print("3 title:", s_tit)

# 4. find 查找，找不到返回-1
pos = s1.find("Python")
print("4 find Python下标：", pos)

# 5. count统计
c = s1.count("o")
print("5 count o出现次数：", c)

# 6. startswith endswith 判断开头结尾
print("6 是否Hello开头：", s1.startswith("Hello"))
print("6 是否123结尾：", s1.endswith("123"))

# 7. ljust rjust center 对齐
print("7 ljust左对齐 |", s1.ljust(20, "-"), "|")
print("7 rjust右对齐 |", s1.rjust(20, "#"), "|")
print("7 center居中  |", s1.center(20, "*"), "|")

# 8. zfill补零
num_str = "42"
print("8 zfill补零：", num_str.zfill(5))

# 9. partition 分割成三部分 前,分隔符,后
text2 = "name=小明"
part_res = text2.partition("=")
print("9 partition：", part_res)

# 10. splitlines 按换行切分
multi_line = "第一行\n第二行\n第三行"
line_list = multi_line.splitlines()
print("10 splitlines：", line_list)

# 11. is系列判断
print("11 isdigit是否全数字：", "1234".isdigit())
print("11 isalpha是否全字母：", "abcd".isalpha())
print("11 isalnum字母数字：", "a1b2".isalnum())
print("11 isspace是否全空白：", "  \t".isspace())

# 12. replace替换
s_rep = s1.replace("Python", "Java")
print("12 replace替换：", s_rep)

# 13. split切列表、join拼接
my_str = "a,b,c,d"
li = my_str.split(",")
join_out = " → ".join(li)
print("13 split+join：", join_out)