#9.1.1　创建Dog 类
'''class Dog():  #在Python中，首字母大写的名称指的是类
    def _init_(self, name, age):
        self.name = name #以self为前缀的变量都可供类中的所有方法使用，我们还可以通过类的任何实例来访问这些变量
        self.age = age
#初始化属性name和age,  _init_是方法，在这个方法的定义中，形参self 必不可少，
# 还必须位于其他形参的前面，每个与类相关联的方法调用都自动传递实参self
#它是一个指向实例本身的引用，让实例能够访问类中的属性和方法
 def sit(self):  #模拟小狗被命令时蹲
        print(self.name.title() + "is now sitting.")

    def roll_over(self):  #模拟小狗被命令时打滚
        print(self.name.title() + " rolled over!")
        '''
'''
class Dog():
    my_dog = Dog('willie',6)
    your_dog = ('lucy',3)
print("My dog's name is " + my_dog.name.title()+ ".")
print("my dog is " + str(my_dog.age)+ "years old.")
my_dog.sit()
print("p\nYour dog's name is " + your_dog.anme.title() + ".")
print("your dog is " + str(your_dog.age)+"years old.")
your_dog.sit()
'''
class Restaurant():
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name=restaurant_name
        self.cuisine_type=cuisine_type
    def describe_restaurant(self):
        print(self.restaurant_name.title())
        print(self.cuisine_type)

    def open_restaruant(self):

        print('The restaurant is opening.')

restaurant = Restaurant("Ryan","china food")
print("The restaurant's name is " + restaurant.restaurant_name.title() + ".")
print("The restaurant is good at " + restaurant.cuisine_type + ".")

restaurant.describe_restaurant()
restaurant.open_restaruant()
'''
用户：创建一个名为User的类，其中包含属性first_name和last_name，还有用户简介通常会存储的其他几个属性。
在User中定义一个名为describ
e_user()的方法，它打印用户信息摘要；再定义一个名为greet_user()的方法，它向用户发出个性化的问候。
 创建多个表示不同用户的实例，并对每个实例都调用上述方法。'''
class User():
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age =age
    def describe_user(self):
        full_name=self.first_name + self.last_name
        print("\nMy name is "+ full_name.title()+".")
        print("\nI'm " + str(self.age)+ " years old.")

    def greet_user(self):
        print("Hello,"+ self.first_name.title() + ' '+ self.last_name.title()+".")
user_1 = User("Shi",'yugang',35)
user_1.describe_user()
user_1.greet_user()
user_2 = User("huai",'jin',26)
user_2.describe_user()
user_2.greet_user()


'''Car 类
表示汽车的类，它存储了有关汽车的信息。'''
class Car():
    '''一次模拟汽车的简单尝试'''
    def __init__(self,make,model,year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        return long_name.title()

    def update_odometer(self,mileage):                            
        self.odometer_reading = mileage

    def read_odometer(self):
        '''打印一条指出汽车里程的消息'''
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi','a4',2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)                                     
my_new_car.read_odometer()
'''使用句点表示法来直接访问并设置汽车的属性odometer_reading
让Python在实例my_new_car 中找到属性odometer_reading ，并将该属性的值
设置为23'''

class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' +self.model
        return long_name.title()
    def update _odometer_reading = mileage
