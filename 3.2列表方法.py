UFO = ['aaa', 'bbb', 'ccc', 'ddd']
print(UFO)
UFO.append('Ryan')  #.append添加元素到结尾
print(UFO)
UFO.insert(0, 'ming')  #insert
del UFO[1]  #del
print(UFO)

#方法POP()可删除列表未元素，并让你能够接着使用它。
killed_UFO = UFO.pop(0)
print(killed_UFO)
deadlist = "Has been dead is " + killed_UFO + "!"
print(deadlist)

#remove
UFO = ['aaa', 'bbb', 'ccc', 'ddd']
UFO.insert(0,'ming')
too_fin = 'ming'
print(UFO)
UFO.remove(too_fin)
print("This UFO " + too_fin +" is too low.")

#sampl 移除不能参加的，并打印不能参加和能参加的最终名单
invite_people = ['ryan','xiaoxiao','chun','pin']
print("Have dinner togather list " + str(invite_people).upper() + ".")
toobusy = invite_people.pop(0)
print("can't arrive people is " + toobusy.title() + "." )
print(
    "Can join in  dinner togather list is " + str(invite_people).upper() + ".")
#use insert(index,object),append(结尾),pop(index)
New_people = invite_people.insert(0, 'Tian')
New_people2 = invite_people.insert(2, 'fat')
New_people3 = invite_people.append('CCTV')
print("The final join in  dinner togather list is " + str(invite_people).upper() + ".")
TheFinalList1 = invite_people.pop(0)
TheFinalList2 = invite_people.pop(1)
TheFinalList3 = invite_people.pop(2)
print("Sorry, " + TheFinalList1 + "," + TheFinalList2 + "," + TheFinalList3 +
      " You can't join in our dinner.")
print("The Final list is" + str(invite_people).upper() + "!")
del invite_people[0]
del invite_people[0]
del invite_people[0]
print(invite_people)