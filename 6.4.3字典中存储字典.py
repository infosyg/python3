#users里嵌套存储两个用户字典.
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },

    }
for username,user_info in users.items(): #使用两个参数接收字典数据
    print("\nUsername: " + username)
    full_name = user_info['first'] + "" + user_info['last']
    location = user_info['location']
    print("\tFull name:" + full_name.title())
    print("\tLocation:" + location.title())


