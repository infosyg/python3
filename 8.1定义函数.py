def favorite_book(book):
    print("one of my favorite books is alice in wonderland" + book.title() )
favorite_book('ryan') #‘ryan’为实参，传递实参给形参（book）

#编写函数时，可给每个形参指定默认值,实参的优先级更高
def describe_pet(animal_type,pet_name):

    print("\nIhave a " + animal_type + ".")
    print("My" +animal_type + "'s name is "+ pet_name.title() + ".")

describe_pet('hamster','harry')  #位置实参

describe_pet(animal_type='hamster',pet_name='harry')  #关键字实参

def make_shirt(shirt_sizi,shirt_type):
    print("your shirt sizi is "+ shirt_sizi ,"your sizi type is " + shirt_type  )

make_shirt('39','adidas')


