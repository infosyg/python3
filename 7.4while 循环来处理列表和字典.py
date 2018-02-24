unconfirmed_users = ['alice','brian','candace']  #未验证列表
confirmed_users = []                              #存储验证用户空列表
#验证每个用户，直到没有为至将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop() #函数pop() 以每次一个的方式从列表unconfirmed_users末尾删除未验证的用户

    print("verifying user:" + current_user.title())
    confirmed_users.append(current_user)  #附加用户到空列表

    #显示所有已验证的用户
print("\nThe flolowing users have benn confirmed:")
for confirmed_user in confirmed_users:               #遍历存储验证用户列表
    print(confirmed_user.title())



　#删除包含特定值的所有列表元素
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat'  in pets:
    pets.remove('cat')

print(pets)


#7.3.3　使用用户输入来填充字典
'''这个程序首先定义了一个空字典（responses ），并设置了一个标志（polling_active ），用于指出调查是否继续。只要polling_active 为True ，Python就运
行while 循环中的代码。
在这个循环中，提示用户输入其用户名及其喜欢爬哪座山（见❶）。将这些信息存储在字典responses 中（见❷），然后询问用户调查是否继续（见❸）。如果用户输入yes
，程序将再次进入while 循环；如果用户输入no ，标志polling_active 将被设置为False ，而while 循环将就此结束。最后一个代码块（见❹）显示调查结果。
如果你运行这个程序，并输入一些名字和回答，输出将类似于下面这样：'''

responses = {}
# 设置一个标志，指出调查是否继续
polling_active = True
while polling_active:
# 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
# 将答卷存储在字典中  
    responses[name] = response
# 看看是否还有人要参与调查
     repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
# 调查结束，显示结果
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")