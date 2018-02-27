#你经常会遇到这样的情况：代码能够正确地运行，但可做进一步的改进——将代码划分为一系列完成具体工作的函数。
#这样的过程被称为重构 。重构让代码更清晰、更易于理解、更容易扩展。
import json
def greet_user():
    filename = 'username.json'
    try:
        with open(filename)as file_object:
            username =json.load(file_object)
    except FileNotFoundError:
        username = input("what is your name?")
        with open (filename,'w')as file_object:
            json.dump(username,fileo_bject)
            print("we'll remember you when you come back," + username + "!")
    else:
        print("welcome back, " + username + "!")
greet_user()
'''考虑到现在使用了一个函数，我们删除了注释，转而使用一个文档字符串来指出程序是做什么的（见❶）。这个程序更清晰些，但函数greet_user() 所做的不仅仅是问候用
户，还在存储了用户名时获取它，而在没有存储用户名时提示用户输入一个。
下面来重构greet_user() ，让它不执行这么多任务。为此，我们首先将获取存储的用户名的代码移到另一个函数中：
'''

import json
def get_stored_username():
"""如果存储了用户名，就获取它"""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def greet_user():
"""问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We'll remember you when you come back, " + username + "!")
greet_user()
'''
新增的函数get_stored_username() 目标明确，❶处的文档字符串指出了这一点。如果存储了用户名，这个函数就获取并返回它；如果文件username.json不存在，这个函数
就返回None （见❷）。这是一种不错的做法：函数要么返回预期的值，要么返回None ；这让我们能够使用函数的返回值做简单测试。在❸处，如果成功地获取了用户名，就打
印一条欢迎用户回来的消息，否则就提示用户输入用户名。
我们还需将greet_user() 中的另一个代码块提取出来：将没有存储用户名时提示用户输入的代码放在一个独立的函数中：
'''

import json
def get_stored_username():
    """如果存储了用户名，就获取它"""
    --snip--
def get_new_username():
    """提示用户输入用户名"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username
def greet_user():
    """问候用户，并指出其名字"""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
greet_user()