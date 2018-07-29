#从一个模块中导入类
from test6 import Car,ElectricCar

my_new_car = Car('Audi','A4',2016);
print(my_new_car.get_descriptive_name());

my_tesla = ElectricCar('tesla','models',2017);
print(my_tesla.get_descriptive_name());

#不推荐使用from classA import *


#导入Python标准库
from collections import OrderedDict      #有序字典

favorite_languages = OrderedDict();

favorite_languages['jen'] = 'python';
favorite_languages['sarah'] = 'c';
favorite_languages['edward'] = 'ruby';
favorite_languages['phil'] = 'python';

for name, language, in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".");