#创建两个列表，一个待打印，一个为已打印为空
unprinted_designs = ['iphone case ','robot pendant','dodecahedron']
completed_models = []
while unprinted_designs:#循环unprinted_designs列表
    current_desigh = unprinted_designs.pop(
    )  #从该列表末尾删除一个设计，将其存储到变量current_design 中，
    print("pinting model:" + current_desigh)  #并显示一条消息，指出正在打印当前的设计
    completed_models.append(current_desigh)  #再将该设计加入到列表completed_models 中
print("\n The following models have benn printed:")  #循环结束后，显示已打印的所有设计
for completed_model in completed_models:
    print(completed_model)

#函数实现的作法
def print_models(unprinted_designs,completed_models):#定义了函数print_models() 包含两个形参一个需要打印的设计列表和一个打印好的模型列表
    while unprinted_designs:  
        current_desigh = unprinted_designs.pop()#从unprinted_designs后边删除然后放入current_desigh.
        print_models("printing model:" + current_desigh)
        completed_models.append(current_design)#已打印completed_models从current_desigh追加

def show_completed_models(completed_models)：
    print("\n The following models have been printed:")
    for completed_model in completed_models:
        print(completed_models)
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

print_models(unprinted_designs,completed_models)
show_completed_models(completed_models)

　#禁止函数修改列表