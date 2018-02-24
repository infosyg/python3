def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


#不管收到的是一个值还是三个值，这个函数都能妥善地处理：
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
'''8.5.1　结合使用位置实参和任意数量实参
如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。Python先匹配位置实参和关键字实参，再将余下的实参都收集到最后一个形参中。
例如，如果前面的函数还需要一个表示比萨尺寸的实参，必须将该形参放在形参*toppings 的前面：'''


def make_pizza(size, *toppings):
    print(
        "\nMaking a " + str(size) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
'''8.5.2　使用任意数量的关键字实参
有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种情况下，可将函数编写成能够接受任意数量的键—值对——调用语句提供了多少就接
受多少。一个这样的示例是创建用户简介：你知道你将收到有关用户的信息，但不确定会是什么样的信息。在下面的示例中，函数build_profile() 接受名和姓，同时还接受
任意数量的关键字实参：'''


def build_profile(first, last, **user_info):
    #形参**user_info 中的两个星号让Python创建一个名为user_info 的空字典
    # 并将收到的所有名称—值对都封装到这个字典中。在这个函数中，可以像访问其他字典
    # 那样访问user_info 中的名称—值对。
    profile = {}  #我们将名和姓加入到这个字典中
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():  
    #我们遍历字典user_info 中的键—值对并将每个键—值对都加入到字典profile 中
        profile[key] = value
    return profile
'''调用build_profile() ，向它传递名（'albert' ）、姓（'einstein' ）和两个键—值对（location='princeton' 和field='physics' ），并将返回
的profile 存储在变量user_profile 中，再打印这个变量'''
user_profile = build_profile(
    'albert', 'einstein', location='princeton', field='physics')
print(user_profile)