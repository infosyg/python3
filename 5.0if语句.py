'''
= 赋值
== 对比两端数据
！= 不等于
>=,<=
in  ,not in 
True   False #布尔
and  or   
if  - else , if -  elif  - else
'''
#
age = 17
if age <= 4:
    price = 0
elif age <= 8:
    price = 4
else:
    price = 10
print("Your ticket price is :" + str(price))

#检查多个条件为True 可以用这种方式
requested_toppings = ['mushrooms', 'extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!")
'''
如果你只想执行一个代码块，就使用if-elif-else 结构；如果要运行多个代码块，就使用一系列独立的if 语句。
'''
alien_color = ['green','yellow','red']
if 'green'in alien_color:
    print("you get 5 bit")
if 'red' in alien_color:
    print("you get 5 bit")
##########
alien_color = ['greenss', 'yellowd', 'red']
if 'green' in alien_color:
    print("you get 50000000$")
elif 'yellow' in alien_color:
    print("you get a women!")
else:
    print("No women,no moneny!")

###################
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("sorry,we are out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

