'''
import json
numbers = [2,3,4,5,11,13]
filename = 'numbers.json'
with open(filename,'w') as file_object:
    json.dump(numbers,file_object)
'''




import json
# 如果以前存储了用户名，就加载它
# 否则，就提示用户输入用户名并存储它
filename = 'username.json'
try:
    with open(filename)as fileobject: 
#尝试打开文件username.json如果这个文件存在就将其中的用户名读取到内存中
        username = json.load(file_object) #再执行else 代码块即打印一条欢迎用户回来的消
except FileNotFoundError:       
    #文件username.json不存在，将引发FileNotFoundError 异常,因此Python将执行except 代码块,提示用户输入其用户名
    username = input("what is your name?")
    with open(filename,'w')as file_object: 
        #再使用json.dump() 存储该用户名，并打印一句问候语
        json.dump(username,file_object)
        print("We'll remember you when you comeback,"+ username + "!")
else:
    print("Wecome back,"+ username + "!")
