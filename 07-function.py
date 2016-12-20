#encoding:utf-8

# 普通函数
def jieCheng( num ):
    "计算一个数的阶乘"
    result = 1;
    for i in range(1,num+1):
        result *= i;
    return result;

'''
print "1000!=",jieCheng(1000)
'''

print "---------------------------------"

def stu(name,age = 21):
    "输出一个学生的信息"
    print "Name:",name;
    print "Age:",age;
    return;

stu("文卡".decode("utf-8"),20)
stu(age=0,name="文卡".decode("utf-8"))

#参数缺省
stu(name="文卡".decode("utf-8"))

print "---------------------------------"

#不定长参数
def printNum(arg1,*arg):
    "打印任意多的数值"
    print arg1;
    print "---"
    for i in arg:
        print i;
    return;

printNum(1,2,3,4,5,6,7,8,9,0);

print "---------------------------------"

#lambda函数
sum = lambda num1,num2:num1+num2;

print sum(1,2)
