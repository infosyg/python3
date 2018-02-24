def make_pizza(sizi, *toppings):
    print(
        "\nMaking a " + str(str) + "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


#8.6.1 导入整个模块module_name.function_name()
#8.6.2　导入特定的函数  from module_name import function_name
#8.6.3　使用as 给函数指定别名 from module_name import function_name as fn
#8.6.4　使用as 给模块指定别名 import module_name as mn
import pizza as p
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#8.6.5　导入模块中的所有函数  from module_name import *
from pizza import *
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
'''8.7　函数编写指南
编写函数时，需要牢记几个细节。应给函数指定描述性名称，且只在其中使用小写字母和下划线。描述性名称可帮助你和别人明白代码想要做什么。给模块命名时也应遵循上述
约定。
每个函数都应包含简要地阐述其功能的注释，该注释应紧跟在函数定义后面，并采用文档字符串格式。文档良好的函数让其他程序员只需阅读文档字符串中的描述就能够使用
它：他们完全可以相信代码如描述的那样运行；只要知道函数的名称、需要的实参以及返回值的类型，就能在自己的程序中使用它。
给形参指定默认值时，等号两边不要有空格：
def function_name(parameter_0, parameter_1='default value')
对于函数调用中的关键字实参，也应遵循这种约定：
function_name(value_0, parameter_1='value')
如果程序或模块包含多个函数，可使用两个空行将相邻的函数分开，这样将更容易知道前一个函数在什么地方结束，下一个函数从什么地方开始
所有的import 语句都应放在文件开头，唯一例外的情形是，在文件开头使用了注释来描述整个程序。
'''