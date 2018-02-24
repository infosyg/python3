'''
每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表，在遍历该字典的for 循环中，我们需要再使
用一个for 循环来遍历相关联的
'''

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():      #languages已取到所有值在同级缩进下再for
    print("\n" + name.title() + "'s favorite languages are:")#如果这里也返回languages值将返的是列表。
    for language in languages:                 #在languages中遍历language的值并返回，这样做的样式更适合我们的审美
        print("\t" + language.title())

