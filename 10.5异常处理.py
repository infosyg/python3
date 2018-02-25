'''
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)
'''
while True:
    first = input("\nFirst number: ")
    if first == 'q':
        break
    second = input("Second number: ")
    if second == 'q':
        break
    try:
        answer = int(first)/int(second)
    except ZeroDivisionError:
        print("you can't divide by 0 !")
    else:
        print(answer)
"""
10-8 猫和狗：
创建两个文件 cats.txt 和 dogs.txt，在第一个文件中至少存储三只猫的名字，在第二个文件中至少存储三条狗的名字。
编写一个程序，尝试读取这些文件，并将其内容打印到屏幕上。将这些代码放在一个 try-except 代码块中，以便在文件不
存在时捕获 FileNotFound 错误，并打印一条友好的消息。将其中一个文件移到另一个地方，并确认 except 代码块中的
代码将正确地执行。 
"""

catsname = "chapter_10/cats.txt"
dogsname = "chapter_10/dogs.txt"

def readfile(filename):

        try:
            with open(filename) as f:
                print filename.upper()
                print f.read()
        except IOError:
            print "The '" + filename + "' does not exist!"

readfile(catsname)   
readfile(dogsname) 
