#创建和使用类

#创建Dog类
class Dog():
    """一次模拟小狗的尝试"""

    def __init__(self, name, age):
        self.name = name;
        self.age = age;

    def sit(self):
        print(self.name.title() + "is now sitting.");

#根据类创建实例
my_dog = Dog('Carol','3');
print("Dog name : " + my_dog.name);
print("Dog age : " + my_dog.age);

my_dog.sit();

 ###############################################

class Car():
    """一次模拟汽车的尝试"""

    def __init__(self,make,model,year):
        """初始化汽车属性"""
        self.make = make;
        self.model = model;
        self.year = year;
        self.odometer_reading = 0;

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model;
        return long_name.title();

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.");

    def update_odometer(self, mileage):
        """将里程表读数设定为指定的值"""
        if(mileage<50):
            self.odometer_reading = mileage;
        else:
            print("too much!");

    def increment(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles;

my_car = Car('BMW', 'X7', 2017);
print(my_car.get_descriptive_name());
my_car.read_odometer();

#三种修改属性的方法
"""直接修改属性的值"""
my_car.odometer_reading = 23;
my_car.read_odometer();

"""通过方法修改属性"""
my_car.update_odometer(35);
my_car.read_odometer();

my_car.update_odometer(70);
#my_car.read_odometer();

"""通过方法对属性的值进行递增"""
my_car.increment(20);
my_car.read_odometer();


##########继承##########
class ElectricCar(Car):
    """电动汽车"""

    def __init__(self,make,model,year):
        super().__init__(make,model,year);
        self.battery_size = 70;                 #给子类定义新属性

    def describe_battery(self):
        """打印一条形容电瓶容量的语句"""
        print("This car has a " + str(self.battery_size) + " kWh battery size");

my_tesla = ElectricCar('tesla', 'models', 2016);
print(my_tesla.get_descriptive_name());
my_tesla.describe_battery();

#将实例用作属性
class Age():
    def __init__(self,age = 30):
        self.age = age;

    def decribe_age(self):
        print(self.age);


class Person():
    def __init__(self,name):
        self.name = name;
        self.age = Age();          #self.age在此作为一个实例属性

a_person = Person("Jack");
a_person.age.decribe_age();
