#函数input() 让程序暂停运行，等待用户输入一些文本。获取输入后Python将其存储在一个变量中。
#message = input('Tell me something,and i will repeat it back to you:')
#print(message)

#求模运算符  % 求模运算符不会指出一个数是另一个数的多少倍，而只指出余数是多少。
#可利用这一点来判断一个数是奇数还是偶数 如果一个数可被另一个数整除，余数就为0
'''
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

'''


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)


#使用break 退出循环

#在循环中使用continue