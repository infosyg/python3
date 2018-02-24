players = ['Ryan','Xiaoxiao','Ming','Greas']
print(players[0:3])#从开始到3位
print(players[2:]) #从2开始到最后
print(players[-3:])#从后边第三个开始到结束

likefood = ['apple','milk','bear','banna']
friendfood = likefood[:]  #代表切片所有列表中的内容 ，如果不用[:]切片likefood的变化将同步friendfood.
print(friendfood)
likefood.append('suger')
friendfood.append('orange')
print(likefood)
print(friendfood)
