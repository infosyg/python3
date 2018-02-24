users = ['admin']
if users:                                   #检查列表中是否为空，先if 后遍历，有返回True,none返回False
    for user in users:
        print("good " + user)
else:
    print("We need to find some users!")
'''
        #print(user)
        if user == 'admin':
            print("Hello admin,would oyou like to see a status report?")
        else:
            print("Hello Eric,thank you for logging in again!")
            '''