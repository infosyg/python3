username = 'guest.txt'
with open(username,'a') as file_object: # 附加
    while True:
        print("enter 'q' to quit the programmer: ")
        guest=input("Pls enter your name: ")
        if guest == 'q':
            break
        else:
            print("welcome your login")
        file_object.write(guest.title() + "\n")

username = 'inquire.txt'
with open(username,'a') as inqu:
    while True:
        print("if you input 'q' ,program will quit! ")
        inquire = input("pls enter your idea: ")
        if inquire == 'q':
            break
        else:
            print("thank your idea!")
    inqu.write(inquire.title() + '\n')