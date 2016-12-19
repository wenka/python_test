#encoding=utf-8

'''
# while 循环
count = 0;
while (count < 10):
    print "循环：",count
    count += 1
print "End..."
'''

'''
# for 循环
for word in "hello world":
    print word
print "End..."

print "-------------------------------------"

fruits = ["banana" , "apple" , "mango"]
for fruit in fruits:
    print fruit
print "End..."

print "-------------------------------------"

for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for i in range(2,num): # 根据因子迭代
      if num%i == 0:      # 确定第一个因子
         j=num/i          # 计算第二个因子
         print '%d = %d * %d' % (num,i,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'
'''
#循环输出2~100之间的素数：
print range(5,6)
for num in range(2,100):
    for i in range(2,num):
       if num % i == 0:
           break
        
    else:
        print num,"是素数！"
