#encoding:utf-8
import time; #引入 time 模块

print "当前时间为：".decode("utf-8"),time.time()

localTime = time.localtime(time.time())
print "本地时间为：",localTime

t = time.asctime(localTime)
print "格式化后的时间为：",t

# 格式化日期 strftime(format[ ,t])
print time.strftime("%Y 年 %m 月 %d 日 %H:%M:%S",localTime)
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
