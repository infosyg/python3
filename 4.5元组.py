area = (200,50,90,44)
for are in area:   #元组遍历
    print(are)
print(area[0])
print(area[1])
'''
area[0] = 250   #python 不能给元组赋值，但可以直接给变量赋值
#相比于列表，元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都不变，可使用元组。

'''

 restaurants = ('pizza','milk','orange')
 for restaurant in restaurants:
     print(restaurant)
restaurants = ('pizza')
print(restaurants)     