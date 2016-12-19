#coding:utf-8
'''
# 数据类型
age = 20 #赋值整型变量

height = 173.5;#浮点型

name = "wenka" #字符串

isBoy = True #布尔类型
print age;
print height;
print name;
print isBoy

#删除引用
# del age
# print age;

# 字符串操作
s = "i love python";
print s[-8] #取从右到左的第八个字符
print s[2:6]; #取从左到右 [2，6）之间的字符
print s[2:]; #取小标为2之后的所有字符，包括2
print s * 3; #  s * N :代表重复输出N次
print s + " this is my python"; # 拼接字符串

'''
'''
#列表操作
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
 
print list               # 输出完整列表
print list[0]            # 输出列表的第一个元素
print list[1:3]          # 输出第二个至第三个的元素 
print list[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinylist * 2       # 输出列表两次
print list + tinylist    # 打印组合的列表
list[0] = "wenka";
print list[0]

# 元组操作
tuple = ( 'runoob', 786 , 2.23, 'john', 70.2 )
tinytuple = (123, 'john')
 
print tuple               # 输出完整元组
print tuple[0]            # 输出元组的第一个元素
print tuple[1:3]          # 输出第二个至第三个的元素 
print tuple[2:]           # 输出从第三个开始至列表末尾的所有元素
print tinytuple * 2       # 输出元组两次
print tuple + tinytuple   # 打印组合的元组
# tuple[0] = "wenka" 元组不允许更新
'''
# 字典
dict = {}
dict['name'] = "文卡"
dict['age'] = 20
print dict;
print dict.keys() # 输出所有 key
print dict.values() # 输出所有 values

print dict['name'].decode("utf-8")
print "年龄:" + str(dict['age']) + "岁"
