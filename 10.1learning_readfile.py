'''
filename = 'learning_python.txt'
with open(filename) as file_object:
    #contents = file_object.read()  读取整个文件
    for content in file_object:  #遍历文件逐行读取
        print(content.rstrip()) #.rstrip方法去除空行
'''



filename = 'learning_python.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

learning_string = ''                      #创建一个空的变量 存储lines
for line in lines:
    learning_string += line.rstrip()      #逐行读取learning_string

print(learning_string)
print(len(learning_string))

#读取文本文件时，Python将其中的所有文本都解读为字符串。如果读取的是数字，并要将其作为数值使用，
#就必须使用函数int()将其转换为整数，或使用函数float()将其转换为浮点数
