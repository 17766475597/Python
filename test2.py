#if语句

cars = ['Audi','Benz','Toyota'];

if cars[0] == cars[1]:                              #简单的if-else语句
    print(cars[0] + ' is equal to ' + cars[1]);
else:
    print(cars[0] + ' is not equal to ' + cars[1]);


score = [75,55,80,82,53];
for i in range(0,len(score)):
    if(score[i]>=60 and score[i]<=100):             #and 语句表与
        print(str(score[i]) + "passed!");


if 'Audi' in cars:
    print('Audi is in the list!');               #判断某特定值在列表中

if 'Honda' not in cars:                           #判断某特定值不在列表中
    print('Honda is not in the list!');


age = 12;
if age<4:                                         #if-elif-else语句
    print('free!');
elif age>=4 and age<=14:
    print('40￥');
else:
    print('80$');


#practice1
my_fruit = ['apple','banana','pear'];
favorite_fruit = 'mango';
if favorite_fruit in my_fruit:
    print('hahaha');
else:
    print('wuwuwu');


request_topping = [];                                      #空列表
if request_topping:
    print("i am not empty");
else:
    print("我是空列表！");


require_Cars = ['Audi','BMW','Ferrari','Toyota'];
available_Cars = ['Audi','Benz','Toyota'];
for require_Car in require_Cars:                              #使用多个列表
    if require_Car in available_Cars:
        print(require_Car + ' is available!');
    else:
        print(require_Car + ' is not available!');