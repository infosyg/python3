'''
def build_person(first_name, last_name,
                 age=''):  #函数build_person() 接受名和姓，并将这些值封装到字典person中
    person = {'first':first_name,'last':last_name}#实参返回字典
    if age:
        person['age'] = age
    return person
musician = build_person('jimi','hendrix',age = 30)  #实参传递给build_person()
print(musician)
'''

#8.3.4结合使用函数和while 循环


def get_formatted_name(first_name, last_name):
    #返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
# 这是一个无限循环!
while True:
    print("\nPlease tell me your name:" +
          "\n if your want exit ,pls input 'quit'!")
    f_name = input("First name: ")
    if f_name == 'quit':
        break
    l_name = input("Last name: ")
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!" )








#8.4　传递列表

