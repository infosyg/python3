#组织列表 Sort() 列表永久排序
cars = ['toyota', 'byd', 'bmw', 'gw']
cars.sort()  #按字母顺序排序
print(cars)

cars.sort(reverse=True)  #按反序排列
print(cars)

cars = ['toyota', 'byd', 'bmw', 'gw']   #sorted() 列表临时排序,物理顺序不 变
print("\nHere is the sorted list:" + str(cars))
print(sorted(cars))
len(cars)   #len测长度
print(cars)



freecite = ['xian','luoyang','dali','sanya','haerbin']
print(freecite)  #物理顺序
print(sorted(freecite))  #临时排序
print(freecite)          #输出会发现恢复物理顺序
freecite.sort(reverse=True) #彻底改变排序
print(freecite)

print ("There is have " + str(len(freecite)) + " people.")#len 统计数量