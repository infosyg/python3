def sandwich(*dosings):
    print("\n The sandwich's dosing is : ")
    for dosing in  dosings:
        print("-" + dosing)

sandwich('apple')
sandwich('milk','apple','orange')

def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile
user_profile = build_profile('Ryan', 'shi',location='Jiangyin,Jiangsu,China',field='ruifuyuan')
print(user_profile)


def carsinfo(model,type,**config):
    profiles = {}
    profiles['carmodel'] = model
    profiles['cartype'] = type   
    for key ,value in config.items():
        profiles[key] = value
    return profiles
carsconfig = carsinfo('BMW','GTX7',emo = 'outback',color='blue',tow_package=True)
print(carsconfig)