'''
prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program."

active = True  #将变量active 设置成了True 让程序最初处于活动状态,这样做简化了while 语句，因为不需要在其中做任何比较——相关的逻辑由程序的其他
#部分处理。只要变量active 为True ，循环就将继续运行
while active:
    message = input(
        prompt)  #在while 循环中，我们在用户输入后使用一条if 语句来检查变量message 的值。如果用户输入的是'quit'
    if message == 'quit':  #我们就将变量active 设置为False ，这将导致while 循环不再继续执行。如果用户输入的不是'quit'
        active = False
    else:
        print(message)




prompt = "\nTell me something, and i will repeat it back to you:"
prompt += "\n(Enter 'quit' to end the program.)"

while True:
    city = input(prompt)
    if city == 'quit':
        break
    #else:
        print("i'd love to go to " + city.title()+ "!")
'''

prompt = "pls input your age: \n(if your want exit ,pls input quit) "

while True:
    age = int(input(prompt))
    if age =='quit':
        break
    elif age > 12:
        print("your price is 20$")
    elif age <=3:
        print("your price free!")  
    elif age <=12:
        print("your price is  10$")
    
    else:
        print("your's inofmation is error!")