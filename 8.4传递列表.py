#传递列表
def greet_users(names):
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)


usernames = ['ryan', 'ty', 'margot']
greet_users(usernames)
'''
def print_models(unprinted_designs, completed_models):

模拟打印每个设计，直到没有未打印的设计为止
打印每个设计后，都将其移到列表completed_models中

while unprinted_designs:
    current_design = unprinted_designs.pop()
# 模拟根据设计制作3D打印模型的过程
    print("Printing model: " + current_design)
    completed_models.append(current_design)
def show_completed_models(completed_models):
"""显示打印好的所有模型"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, complete)
'''


def show_magicians(printed_names):
    for printed_name in printed_names:
        print(printed_name.title())


def make_great(changed_lists):
    for i in range(4):
        changed_lists[i] = 'the Great is new ' + changed_lists[i]
    return changed_lists


magicians = ['job', 'jane', 'stand', 'smile']
magician_nice = magicians[:]
make_great(magician_nice)
show_magicians(magician_nice)