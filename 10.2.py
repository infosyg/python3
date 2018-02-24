#写入文件
filename = 'learning_python.txt'
with open(filename,'w')as file_object:
    file_object.write("i love programming!")


#写入空文件
filename = 'learning_python2.txt'  #如果不存在这个文件将自动创建它
with open(filename,'w') as file_object:
    file_object.write ("i love programming.")


#写入多行
filename = 'programming.txt'
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

#附加到文件
filename = 'programming.txt'
with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")
    