# + - * \ ，**乘方，运算符运用
a = 3**2
print(a)
b=2 + 3 * 4
print(b)

#要求绝对精度时慎用浮点数，小数位是不确定的
c = 0.2 + 0.1
d = 3 * 0.1
print(c)
print(d)

#str类型不能和int相加，可以使用str()强制转换
age = 23
message = "Happy" +'\t'+ str(age) + " rd Birthday!"
print(message)

mynumber = int(7)
numbergame = "each moth "+ str(mynumber) + "day is good days"
print(numbergame)

