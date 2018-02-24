'''字典（dictionary)：它就是键－值对。如在C++语言中为map的容器。它的特点就是可以快速查找，需要占用大量的内存，内存浪费多。通过key计算位置的算法称为哈希算法（Hash）。

用 {} 定义dictionary哦；

随着dictionary的增加，查找时间不会增加的。

多次对一个key放入value，后面的值会把前面的值冲掉：

可以用  ‘key’in dic 或 dic.get(‘key’)的方法来查看key是否存在。注意：dict提供的get方法，如果key不存在，可以返回None，或者自己指定的value，返回None的时候Python的交互式命令行不显示结果。

删除用: pop(key)。添加时，直接用key值的索引添加就可以的。
'''
#dict是动态的 随时可以向里边添加。
ufos = {'color':'red','points':5,'age':30}
ufos['x_position'] = 0
ufos['y_position'] = 25
#遍历字典中的所有值 不包含键，使用values 方法
for ufo in ufos.values():
    print(ufo)



#空字典
ufo1 = {}
ufo1['color'] = 'green'
ufo1['points'] = 5
ufo1['color'] = 'yellow'  #可以修改字典内的值
print(ufo1)

ryan = {'x_position':0,'y_position':25,'speed':''}
print("original x=position:" + str(ryan['x_position']))
# 向右移动外星人，据外星人当前速度决定 将其移动多远。
if ryan['speed'] == 'solw':
    x_increment = 1
elif ryan ['speed'] == 'medium':
    x_increment = 2
elif ryan['speed'] == 'fast':
    x_increment = 3
else:
    #这个外星人速度一定很快
    x_increment = 4
    #新位置等于老位置加上增量
ryan['x_position'] = ryan['x_position'] + x_increment
print("New x_position: " + str(ryan['x_position']))
print(ryan)

#for 遍历字典 值给key，须声明两个变量，因为字典中每组有两个值，key 和value,可使用任何名称。
myinfo = {
    'firstname':'shi',
    'lastname':'yugang',
    'age':'34',
    'city':'wuxi'
    }
mywifi = ['age','city']
for name in myinfo.keys():
    print(name.title())
    if name in mywifi:
        print("hi" + name.title() + ",i see your myinfo is " +
              myinfo[name].title() + "!")
'''指出两位朋友喜欢的语言。我们像前面一样遍历字典中的名字，但在名字为指定朋友的名字时，打
印一条消息，指出其喜欢的语言
'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
if 'erin' not in favorite_languages.keys():
    print("erin,please take our poll!")
friends = ['phil', 'sarah']
for name in sorted(favorite_languages.keys()): #sprted 按顺序对字典进行排序
    #print(name.title())
    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " +
            favorite_languages[name].title() + "!")

'''以上的做法都是提取字典中所有的值，而没有考虑是否重复。
为剔除重复项，可使用集合（set），集合类似于列表，但每个元素都必须是独一无二的。
'''
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())


#作业
rivers = {'china':'changjiang','aiji':'nile','rosa':'huanghe'}
if 'baihe' not in rivers:
    print("sorry,baihe not in this river list ")
for river in set(rivers.keys()):
    print("Great's river  " + river.title())