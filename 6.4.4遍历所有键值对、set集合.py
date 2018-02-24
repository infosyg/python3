#　遍历所有的键—值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print("\nKey:" + key)
    print("value:" + value)

favorite_languages = {
    'jen':'python',
    'serah':'c',
    'edward':'ruby',
    'phil':'python',
    }
for name,language in favorite_languages.items():
    print(name.title() + ',' + language.title() )
if 'ryan' not in favorite_languages.keys():  #检查Ryan 是否在字典里。
    print("Ryan,please take our poll!"


'''set 集合类似于列表，但每个元素都必须 是独一无二的。'''
for language in set(favorite_languages.values()):
    print(language.title())