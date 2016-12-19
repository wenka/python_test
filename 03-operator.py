# 操作符
a = 2.0
b = 3.0;

'''
print "2+3 =",a+b
print "2-3 =",a-b
print "2*3 =",a*b
print "2/3 =",a/b
print "2%3 =",a%b

print "2**3 =",a**b
print "2//3 =",a//b

# 比较运算符
print "a == b",a==b
print "a <> b",a<>b

if 0:
    print True
else:
    print False

'''

'''
# 逻辑运算符
print 2 and 3
print 2 or 3
print "---------------------------------"
print not 0
print not 4
print "---------------------------------"
print not(a>b)
'''
#成员运算符
list = [1,2,3,4,5]
if 6 in list:
    print a,"在 list 集合中！"
else:
    print a,"不在 list 集合中！"

#身份运算符
c = "wo"
d = c
e = c
f = "wo"
if d is f:
    print d,f,"引用同一个对象"
else:
    print d,f,"引用不同的对象"
