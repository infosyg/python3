#需要分别存储大量名和姓的大型程序中，像get_formatted_name() 这样的函数非常有用。你分别存储名和姓，每当需要显示姓名时都调用这个函数.
#middle_name  这个形参指定了一个默认值为空格，为了防止一些人没有中间名。用户没有输入时程序能继续。
def get_formatted_name(first_name, last_name, middle_name=' '):  #允许空值需要在形参加 =‘’
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)



#返回字典


def build_person(first_name, last_name, age=''):
    #"""返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# 结合使用函数和while 循环
def get_formatted_name1(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    formatted_name = get_formatted_name1(f_name, l_name)
    print("\nHello, " + formatted_name + "!")